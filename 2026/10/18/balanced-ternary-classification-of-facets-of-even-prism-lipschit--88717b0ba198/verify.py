"""Independent exact checks of prism facet enumeration (Python 3 standard library)."""
from itertools import product
from math import comb

def central_trinomial(n):
    return sum(comb(n, 2*k)*comb(2*k, k) for k in range(n//2+1))

def bipyramid_orientations(n):
    # Dual has side-ring edges c_i, two hub edges a_i,b_i.
    # For each assignment to a_i and c_i, Kirchhoff forces b_i.
    count=0
    for c in product((-1,1),repeat=n):
        for a in product((-1,1),repeat=n):
            if sum(a)!=0: continue
            if all(c[(i-1)%n]-c[i]-a[i] in (-1,1) for i in range(n)):
                count+=1
    return count

def primal_facets(n):
    # Independent enumeration of ALL integral Lipschitz heights anchored at the first top vertex.
    count=0
    top=[0];bot=[]
    def is_connected():
        roots=list(range(2*n))
        def find(x):
            while roots[x]!=x:
                roots[x]=roots[roots[x]];x=roots[x]
            return x
        def union(x,y):roots[find(x)]=find(y)
        for j in range(n):
            nxt=(j+1)%n
            if abs(top[j]-bot[j])==1:union(j,j+n)
            if abs(top[j]-top[nxt])==1:union(j,nxt)
            if abs(bot[j]-bot[nxt])==1:union(j+n,nxt+n)
        return len({find(j) for j in range(2*n)})==1
    def grow():
        nonlocal count
        if len(top)==n:
            if abs(top[-1]-top[0])<=1 and abs(bot[-1]-bot[0])<=1 and is_connected():count+=1
            return
        for da,db in product((-1,0,1),repeat=2):
            x=top[-1]+da;y=bot[-1]+db
            if abs(x-y)<=1:
                top.append(x);bot.append(y);grow();top.pop();bot.pop()
    for b0 in (-1,0,1):
        bot.append(b0);grow();bot.pop()
    return count

def trace_coefficient_via_transfer(n):
    # Direct Laurent polynomial multiplication of 2-by-2 transfer matrix.
    from collections import defaultdict
    def add(a,b):
        d=defaultdict(int,a)
        for power,c in b.items():d[power]+=c
        return dict(d)
    def mul(a,b):
        d=defaultdict(int)
        for p,aa in a.items():
            for q,bb in b.items():d[p+q]+=aa*bb
        return dict(d)
    t={-1:1,1:1};p={1:1};q={-1:1}
    M=[[t,q],[p,t]]
    result=[[{0:1},{ }],[{ },{0:1}]]
    for _ in range(n):
        result=[[add(mul(result[i][0],M[0][j]),mul(result[i][1],M[1][j])) for j in range(2)] for i in range(2)]
    return result[0][0].get(0,0)+result[1][1].get(0,0)

def main():
    assertions=0
    for n in range(2,21):
        v=trace_coefficient_via_transfer(n)
        expect=2*central_trinomial(n) if n%2==0 else 0
        assert v==expect,(n,v,expect)
        assertions+=1
    for n in (4,6,8,10):
        brute=bipyramid_orientations(n)
        assert brute==2*central_trinomial(n),(n,brute)
        assertions+=1
    for n in (4,6):
        fac=primal_facets(n)
        assert fac==2*central_trinomial(n),(n,fac)
        assertions+=1
    print('PASS:',assertions,'independent exact theorem-level consistency checks')
    print('even prism facets:',[(n,2*central_trinomial(n)) for n in (4,6,8,10,12,14)])
if __name__=='__main__':main()
