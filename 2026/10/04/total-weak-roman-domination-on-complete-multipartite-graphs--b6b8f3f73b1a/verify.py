import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def total_dom(vals,L):
    n=len(L)
    return all(any(vals[u]>0 and L[u]!=L[v] for u in range(n)) for v in range(n))

def twrdf(vals,L):
    if not total_dom(vals,L): return False
    n=len(L)
    for v in range(n):
        if vals[v]!=0: continue
        ok=False
        for u in range(n):
            if L[u]!=L[v] and vals[u]>0:
                g=list(vals); g[v]=1; g[u]-=1
                if total_dom(g,L): ok=True; break
        if not ok: return False
    return True

def criterion(vals,parts):
    L=labels(parts); p=[0]*len(parts); s=[0]*len(parts)
    for v,i in enumerate(L):
        if vals[v]>0: p[i]+=1
        s[i]+=vals[v]
    supp=[i for i,x in enumerate(p) if x>0]
    if len(supp)>=3: return True
    if len(supp)!=2: return False
    i,j=supp
    return (p[i]==parts[i] or s[j]>=2) and (p[j]==parts[j] or s[i]>=2)

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def formula(parts):
    N=sum(parts)
    total=[1]
    for _ in range(N): total=conv(total,[1,1,1])
    c=total[:]; c[0]-=1
    A=[]; Q=[]; L=[]; M=[]
    for n in parts:
        a=[1]
        for _ in range(n): a=conv(a,[1,1,1])
        a[0]-=1
        f=[1]
        for _ in range(n): f=conv(f,[0,1,1])
        m=max(len(a),len(f)); a+= [0]*(m-len(a)); f += [0]*(m-len(f))
        q=[a[k]-f[k] for k in range(m)]
        A.append(a); Q.append(q); L.append([0,n]); M.append([0,n if n>=2 else 0])
        for k,x in enumerate(a): c[k]-=x
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            for term,sgn in ((conv(Q[i],L[j]),-1),(conv(Q[j],L[i]),-1),(conv(M[i],M[j]),1)):
                if len(c)<len(term): c += [0]*(len(term)-len(c))
                for k,x in enumerate(term): c[k]+=sgn*x
    return c

def min_formula(parts):
    r=len(parts); N=sum(parts); s=sum(n==1 for n in parts); t=sum(n==2 for n in parts)
    if r>=3:
        if s>=2: return 2, math.comb(s,2)
        e3=sum(parts[i]*parts[j]*parts[k] for i in range(r) for j in range(i+1,r) for k in range(j+1,r))
        return 3, e3+s*(N-1)+t*(N-2)
    a,b=parts
    if a==b==1: return 2,1
    if min(a,b)<=2: return 3, s*(N-1)+t*(N-2)
    h=lambda n:n+math.comb(n,2)
    return 4, h(a)*h(b)+(b if a==3 else 0)+(a if b==3 else 0)

types=labelings=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            L=labels(parts); actual=[0]*(2*N+1)
            for vals in itertools.product(range(3), repeat=N):
                labelings+=1
                got=twrdf(vals,L)
                assert got==criterion(vals,parts)
                if got: actual[sum(vals)]+=1
            pred=formula(parts)+[0]*(2*N+1-len(formula(parts)))
            assert actual==pred[:2*N+1]
            g=next(k for k,x in enumerate(actual) if x)
            assert (g,actual[g])==min_formula(parts)
            types+=1
print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('ternary_labelings_checked =',labelings)
print('orders = 2..9')
print('all-function criterion matched')
print('all weight-enumerator coefficients matched')
print('minimum weights and minimum-function counts matched')
