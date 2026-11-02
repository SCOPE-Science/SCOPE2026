"""Direct arithmetic checks for finite Nottingham-jet involution spectra.
No external packages required; fields represented by binary polynomial bases.
"""
from itertools import product
from collections import Counter

def make_field(e,red):
    q=1<<e
    M=[[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            x,y=a,b;r=0
            while y:
                if y&1:r^=x
                y>>=1;x<<=1
                if x&q:x^=red
            M[a][b]=r
    assert all(len(set(M[a]))==q for a in range(1,q))
    return M

def square_difference(coeff,M,degree):
    # f(t) = t+sum_{i=2}^{N-1}a_i t^i;
    # returns f(f(t))-t modulo t^degree.
    p=[0]*degree
    for j in range(1,min(degree,len(coeff))):p[j]=coeff[j]
    v=[0]*degree;pw=[0]*degree;pw[0]=1
    for j in range(1,degree):
        new=[0]*degree
        for a,ca in enumerate(pw):
            if ca:
                for b in range(1,degree-a):
                    if p[b]:new[a+b]^=M[ca][p[b]]
        pw=new
        if j<len(coeff) and coeff[j]:
            aj=coeff[j]
            for k,z in enumerate(pw):
                if z:v[k]^=M[aj][z]
    v[1]^=1
    return v

def predicted(N,d,q,lift):
    if d%2==0:
        if lift or 2*d+1<N:return 0
        return (q-1)*q**(N-d-2)
    if lift:
        constraints=(N+d-1)//2-d
    else:
        constraints=max(0,(N-1)//2-d)
    return (q-1)*q**(N-d-2-constraints)

def check(e,red,N):
    M=make_field(e,red);q=1<<e
    hist=Counter(); lhist=Counter(); all_count=0
    for v in product(range(q), repeat=N-2):
        if not any(v):
            hist[0]+=1; lhist[0]+=1; continue
        d=next(i+1 for i,z in enumerate(v) if z)
        f=[0,1]+list(v)
        sq=square_difference(f,M,N)
        if not any(sq):
            hist[d]+=1;all_count+=1
            if d%2 and not any(square_difference(f,M,N+d)):
                lhist[d]+=1
    for d in range(1,N-1):
        assert hist[d]==predicted(N,d,q,False),(q,N,d,'finite',hist[d],predicted(N,d,q,False))
        assert lhist[d]==predicted(N,d,q,True),(q,N,d,'lift',lhist[d],predicted(N,d,q,True))
    assert hist[0]==lhist[0]==1
    print(f'q={q} N={N}: order_le_2={sum(hist.values())} liftable={sum(lhist.values())} depth_fibers={dict(sorted(hist.items()))}')

if __name__=='__main__':
    for N in range(3,14):check(1,0b11,N)
    for N in range(3,9):check(2,0b111,N)
    for N in range(3,7):check(3,0b1011,N)
    print('NOTTINGHAM_JET_INVOLUTION_DEPTH_AND_LIFTABILITY_OK')
