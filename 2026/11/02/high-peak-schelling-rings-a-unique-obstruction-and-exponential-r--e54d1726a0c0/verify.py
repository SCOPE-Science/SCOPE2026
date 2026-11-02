"""Direct and transfer enumerators for the high-peak two-color ring swap game.

The direct oracle evaluates every bilateral swap from actual agent utilities.
The transfer oracle uses closed walks on 3-bit de Bruijn states.
"""
from collections import defaultdict
from itertools import combinations

def utility(word, i):
    n=len(word)
    same=(word[(i-1)%n]==word[i])+(word[(i+1)%n]==word[i])
    return (1,2,0)[same]

def brute_stable(w):
    n=len(w)
    old=[utility(w,i) for i in range(n)]
    improving=0
    for i in range(n):
        for j in range(i+1,n):
            if w[i]==w[j]:continue
            v=list(w);v[i],v[j]=v[j],v[i]
            if utility(v,j)>old[i] and utility(v,i)>old[j]:
                improving+=1
    return improving==0

def criterion(w):
    n=len(w)
    z=any(w[i]==w[(i+1)%n]==w[(i+2)%n]==0 for i in range(n))
    o=any(w[i]==w[(i+1)%n]==w[(i+2)%n]==1 for i in range(n))
    alt=any(tuple(w[(i+j)%n] for j in range(4)) in ((0,1,0,1),(1,0,1,0)) for i in range(n))
    return (not (z and o)) and (not alt)

def transfer(n, exclude0, exclude1):
    # Trace of M^n, coefficient by number of ones. Start state of 3 past bits.
    total=[0]*(n+1)
    for s0 in range(8):
        states={(s0,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (s,k),a in states.items():
                aa=(s>>2)&1; bb=(s>>1)&1; cc=s&1
                for d in (0,1):
                    if exclude0 and bb==cc==d==0:continue
                    if exclude1 and bb==cc==d==1:continue
                    if (aa,bb,cc,d) in ((0,1,0,1),(1,0,1,0)):continue
                    kk=k+d
                    if kk<=n:nxt[((s&3)<<1|d,kk)]+=a
            states=nxt
        for (s,k),a in states.items():
            if s==s0:total[k]+=a
    return total

def exact_counts(n):
    a=transfer(n,True,False)
    b=transfer(n,False,True)
    c=transfer(n,True,True)
    return [x+y-z for x,y,z in zip(a,b,c)]

if __name__=='__main__':
    profiles=0; transitions=0; rows=[]
    for n in range(3,16):
        expected=[0]*(n+1)
        for bits in range(1<<n):
            w=tuple((bits>>i)&1 for i in range(n))
            if not (0<sum(w)<n):continue
            profiles+=1
            direct=brute_stable(w)
            assert direct==criterion(w),(n,w,direct,criterion(w))
            if direct:expected[sum(w)]+=1
            transitions+=sum(w)*(n-sum(w))
        trace=exact_counts(n)
        assert trace[1:n]==expected[1:n],(n,expected,trace)
        rows.append((n,expected[1:n]))
    print('CHECKED_PROFILES',profiles)
    print('POSSIBLE_BILATERAL_SWAPS',transitions)
    print('EXACT_TRACE_MATCH_N_3_TO_15')
    for n,counts in rows:
        print(n,counts)
    print('ALL_CHECKS_PASS')

def matrix(exclude0,exclude1):
    ans=[[0]*8 for _ in range(8)]
    for s in range(8):
        a,b,c=(s>>2)&1,(s>>1)&1,s&1
        for d in (0,1):
            if exclude0 and b==c==d==0:continue
            if exclude1 and b==c==d==1:continue
            if (a,b,c,d) in ((0,1,0,1),(1,0,1,0)):continue
            ans[s][((s&3)<<1)|d]+=1
    return ans

def prod(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(8)) for j in range(8)]for i in range(8)]

def characteristic(M):
    # Newton identities, exact integer division.
    c=[1];P=[[int(i==j) for j in range(8)]for i in range(8)]
    traces=[]
    for k in range(1,9):
        P=prod(P,M)
        traces.append(sum(P[i][i]for i in range(8)))
        s=sum(c[k-j]*traces[j-1]for j in range(1,k+1))
        assert s%k==0
        c.append(-s//k)
    return c

def polynomial_multiply(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

if __name__=='__main__':
    assert characteristic(matrix(True,False)) == [1,-1,0,-2,0,0,1,0,0]
    # (lambda^3-lambda-1)(lambda^3+lambda-1)*lambda^2
    assert characteristic(matrix(True,True))==polynomial_multiply(polynomial_multiply([1,0,-1,-1],[1,0,1,-1]),[1,0,0])
    print('EXACT_CHARACTERISTIC_POLYNOMIALS_PASS')
