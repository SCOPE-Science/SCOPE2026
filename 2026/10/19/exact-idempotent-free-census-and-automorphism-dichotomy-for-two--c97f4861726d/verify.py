#!/usr/bin/env python3
"""Reproducible finite-field checks for two-dimensional evolution-algebra idempotent counts.
Run with Python 3. No external dependencies.
"""
from itertools import product
from collections import Counter

# Polynomial coefficients listed in ascending order; all are irreducible.
FIELD_SPEC = {
    2:(2,[0,1]), 3:(3,[0,1]), 4:(2,[1,1,1]),
    5:(5,[0,1]), 7:(7,[0,1]), 8:(2,[1,1,0,1]),
    9:(3,[1,0,1]), 11:(11,[0,1]), 13:(13,[0,1]),
    16:(2,[1,1,0,0,1]),
}
class Field:
    def __init__(self,q):
        p, poly = FIELD_SPEC[q]
        m=len(poly)-1
        assert p**m==q and poly[-1]==1
        self.q,self.p,self.m,self.poly=q,p,m,poly
        def digits(x):
            out=[]
            for _ in range(m): out.append(x%p);x//=p
            return out
        digits_list=[digits(x) for x in range(q)]
        def encode(a): return sum((v%p)*p**i for i,v in enumerate(a))
        self.add=[[encode([digits_list[x][i]+digits_list[y][i] for i in range(m)]) for y in range(q)] for x in range(q)]
        self.neg=[encode([-z for z in digits_list[x]]) for x in range(q)]
        self.mul=[]
        for x in range(q):
            row=[]
            for y in range(q):
                prod=[0]*(2*m-1)
                for i,xi in enumerate(digits_list[x]):
                    for j,yj in enumerate(digits_list[y]): prod[i+j]=(prod[i+j]+xi*yj)%p
                for k in range(2*m-2,m-1,-1):
                    top=prod[k]
                    for j in range(m): prod[k-m+j]=(prod[k-m+j]-top*poly[j])%p
                row.append(encode(prod[:m]))
            self.mul.append(row)
        self.one=1
        assert all(self.mul[1][v]==v for v in range(q))
        self.inv=[None]*q
        for v in range(1,q):
            matches=[w for w in range(1,q) if self.mul[v][w]==1]
            assert len(matches)==1,(q,v,matches)
            self.inv[v]=matches[0]
    def add4(self,a,b,c,d):return self.add[self.add[a][b]][self.add[c][d]]
    def sub(self,x,y):return self.add[x][self.neg[y]]
    def cube(self,x):return self.mul[self.mul[x][x]][x]
    def bad(self,m):
        a,b,c,d=m
        if self.sub(self.mul[a][d],self.mul[b][c])==0:return False
        if c==0:return False
        for z in range(self.q):
            zz=self.mul[z][z]
            zzz=self.mul[zz][z]
            f=self.add4(self.mul[c][zzz],self.neg[self.mul[d][zz]],self.mul[a][z],self.neg[b])
            if f==0:return False
        return True
    def idem(self,m):
        a,b,c,d=m
        for x,y in product(range(self.q),repeat=2):
            if x==0 and y==0:continue
            xx=self.mul[x][x];yy=self.mul[y][y]
            if self.add[self.mul[a][xx]][self.mul[c][yy]]==x and self.add[self.mul[b][xx]][self.mul[d][yy]]==y:return True
        return False
    def group_action(self,m,s,t,swap):
        a,b,c,d=m
        mul=self.mul; inv=self.inv
        ss=mul[s][s];tt=mul[t][t]
        if not swap:
            return (mul[s][a],mul[mul[ss][b]][inv[t]],mul[mul[tt][c]][inv[s]],mul[t][d])
        return (mul[s][d],mul[mul[ss][c]][inv[t]],mul[mul[tt][b]][inv[s]],mul[t][a])
    def formula_classes(self):
        q=self.q
        return (q*(q+1)+(4 if q%3==1 else 0))//6

def test(q,exhaustive_idempotents=True,orbit_check=True):
    F=Field(q); mat=[]; perfect=0
    for m in product(range(q),repeat=4):
        a,b,c,d=m
        if F.sub(F.mul[a][d],F.mul[b][c])==0:continue
        perfect+=1
        if F.bad(m):mat.append(m)
        if exhaustive_idempotents:
            assert F.bad(m)==(not F.idem(m)),(q,m)
    N=q*(q-1)**2*(q+1)//3
    assert perfect==q*(q-1)**2*(q+1)
    assert len(mat)==N,(q,len(mat),N)
    expected=F.formula_classes()
    aut3class=0
    if orbit_check:
        left=set(mat); orbit_sizes=Counter(); aut_orders=Counter()
        while left:
            m=min(left)
            orbit={F.group_action(m,s,t,swap) for s in range(1,q) for t in range(1,q) for swap in (0,1)}
            assert orbit<=left or orbit<=set(mat),(q,m)
            left-=orbit
            orbit_sizes[len(orbit)]+=1
            order=2*(q-1)**2//len(orbit)
            aut_orders[order]+=1
        assert sum(aut_orders.values())==expected,(q,aut_orders,expected)
        assert set(aut_orders)<={1,3}
        assert aut_orders[3]==(1 if q%3==1 else 0),(q,aut_orders)
        aut3class=aut_orders[3]
    return {'q':q,'perfect_tables':perfect,'idempotent_free_tables':len(mat),
            'isomorphism_classes':expected,'automorphism_order_three_classes':aut3class,
            'orbits_verified':orbit_check,'idempotents_exhausted':exhaustive_idempotents}

if __name__=='__main__':
    for q in (2,3,4,5,7,8,9,11,13,16):
        # exhaustive element-level checks run for q<=9, orbit census for all listed q
        result=test(q,q<=9,True)
        print(result,flush=True)
    print('VERIFY_OK',flush=True)
