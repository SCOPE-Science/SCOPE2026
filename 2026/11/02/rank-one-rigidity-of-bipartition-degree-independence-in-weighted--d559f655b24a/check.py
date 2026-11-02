"""Exact small-case checks for the positive weighted bipartite spanning-tree degree law."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from math import factorial

def trees(a,b,w):
    edges=[(i,j) for i in range(a) for j in range(b)]
    for selected in combinations(range(a*b),a+b-1):
        par=list(range(a+b))
        def root(x):
            while par[x]!=x:
                x=par[x]
            return x
        ok=True; da=[0]*a; db=[0]*b; z=F(1)
        for k in selected:
            i,j=edges[k]; x,y=root(i),root(a+j)
            if x==y:ok=False;break
            par[x]=y; da[i]+=1;db[j]+=1;z*=w[i][j]
        if ok:
            yield tuple(da),tuple(db),z

def audit(a,b,w):
    jd=defaultdict(F);total=F(0)
    for da,db,z in trees(a,b,w):
        jd[da,db]+=z;total+=z
    assert total>0
    p=[[w[i][j]/sum(w[k][j] for k in range(a)) for j in range(b)] for i in range(a)]
    for j in range(b):
        bridge=tuple(a if k==j else 1 for k in range(b))
        den=sum(z for (da,db),z in jd.items() if db==bridge)
        assert den>0
        for i in range(a):
            num=sum(F(da[i])*z for (da,db),z in jd.items() if db==bridge)
            conditional=num/den
            formula=1+sum(p[i][k] for k in range(b) if k!=j)
            assert conditional==formula, (a,b,i,j,conditional,formula)
            reconstructed=sum((1+sum(p[i][k] for k in range(b) if k!=h))-1 for h in range(b))/F(b-1)-(conditional-1)
            assert reconstructed==p[i][j]
    row=defaultdict(F);col=defaultdict(F)
    for (da,db),z in jd.items():row[da]+=z;col[db]+=z
    independent=all(z*total==row[da]*col[db] for (da,db),z in jd.items())
    # Also check support product cells that may not occur
    independent=independent and all(jd.get((da,db),F(0))*total==row[da]*col[db] for da in row for db in col)
    rank_one=all(w[i][j]*w[0][0]==w[i][0]*w[0][j] for i in range(a) for j in range(b))
    assert independent==rank_one,(a,b,w,independent,rank_one)
    if rank_one:
        u=[w[i][0] for i in range(a)]
        v=[w[0][j]/w[0][0] for j in range(b)]
        U=sum(u);V=sum(v)
        assert total==U**(b-1)*V**(a-1)*__prod(u)*__prod(v)
        # Exact independent multinomial distribution for each degree-vector pair.
        for (da,db),z in jd.items():
            pa=F(factorial(b-1),__prod(factorial(d-1) for d in da))*__prod((u[i]/U)**(d-1) for i,d in enumerate(da))
            pb=F(factorial(a-1),__prod(factorial(d-1) for d in db))*__prod((v[j]/V)**(d-1) for j,d in enumerate(db))
            assert z/total==pa*pb
    return len(jd),total,independent

def __prod(x):
    ans=F(1)
    for z in x:ans*=z
    return ans

def run():
    cases=0
    for a,b in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,3)]:
        u=[F(i+2) for i in range(a)]
        v=[F(2*j+1) for j in range(b)]
        wr=[[u[i]*v[j] for j in range(b)] for i in range(a)]
        wn=[[F(1+((3*i+7*j+5*i*j)%13)) for j in range(b)] for i in range(a)]
        for typ,w in [('rank-one',wr),('non-rank-one',wn)]:
            n,total,indep=audit(a,b,w)
            cases+=1
            print(a,b,typ,'joint supports',n,'total',total,'independent',indep)
    print('PASS:',cases,'exact small finite-family computations, conditional means, inversion, and joint independence.')
if __name__=='__main__':run()
