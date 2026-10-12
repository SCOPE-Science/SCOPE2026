"""Independent finite checks for affine-direction Boolean modal generator theorem.
Run: python verify.py. Python standard library only.
A finite-field element is encoded by base-p polynomial digits, modulo a chosen
monic irreducible polynomial. Directions are normalized modulo nonzero scalars.
"""
from itertools import combinations, product
from math import comb

FIELD_POLYS = {2:(2,[0,1]), 3:(3,[0,1]), 4:(2,[1,1,1]),
               5:(5,[0,1]), 7:(7,[0,1]), 8:(2,[1,1,0,1]),
               9:(3,[1,0,1]), 11:(11,[0,1])}

class Field:
    def __init__(self,q):
        self.q=q
        self.p,self.poly=FIELD_POLYS[q]
        self.k=len(self.poly)-1
        assert self.p**self.k==q and self.poly[-1]==1
        self.digs=[tuple((x//self.p**i)%self.p for i in range(self.k)) for x in range(q)]
        self.encoding={a:i for i,a in enumerate(self.digs)}
        self.plus=[[self.encoding[tuple((a[j]+b[j])%self.p for j in range(self.k))]
                    for b in self.digs] for a in self.digs]
        self.mult=[]
        for a in self.digs:
            row=[]
            for b in self.digs:
                z=[0]*(2*self.k-1)
                for i in range(self.k):
                    for j in range(self.k):z[i+j]=(z[i+j]+a[i]*b[j])%self.p
                for t in range(len(z)-1,self.k-1,-1):
                    coeff=z[t]
                    for j in range(self.k): z[t-self.k+j]=(z[t-self.k+j]-coeff*self.poly[j])%self.p
                row.append(self.encoding[tuple(z[:self.k])])
            self.mult.append(row)
        for a in range(1,q):
            assert sorted(self.mult[a])==list(range(q)), ('not_field',q,a)
    def add(self,a,b):return self.plus[a][b]
    def mul(self,a,b):return self.mult[a][b]

class Frame:
    def __init__(self,q,d):
        self.F=Field(q);self.q=q;self.d=d
        self.W=list(product(range(q),repeat=d));self.N=len(self.W)
        self.ids={v:i for i,v in enumerate(self.W)}
        F=self.F
        self.directions=sorted({min(tuple(F.mul(a,x) for x in v) for a in range(1,q))
                     for v in self.W[1:]})
        self.lines=[]
        for v in self.directions:
            self.lines.append([tuple(self.ids[tuple(F.add(x[j],F.mul(t,v[j])) for j in range(d))]
                                    for t in range(q)) for x in self.W])
    def diamond(self,mask,di):
        lines=self.lines[di]
        return sum(1<<i for i in range(self.N) if any(mask&(1<<j) for j in lines[i]))
    def dir_index(self,a,b):
        F=self.F; q=self.q
        vec=tuple(F.add(a[i],next(t for t in range(q) if F.add(b[i],t)==0)) for i in range(self.d))
        assert any(vec)
        return self.directions.index(min(tuple(F.mul(t,v) for v in vec) for t in range(1,q)))
    def closure_atoms(self,P):
        # Refine the atoms of the generated Boolean algebra by all modal images,
        # independent of the explicit geometric singleton construction.
        colors=[int(bool(P&(1<<i))) for i in range(self.N)]
        for steps in range(self.N+1):
            keys=[(colors[i],tuple(tuple(sorted({colors[j] for j in direction[i]}))
                       for direction in self.lines)) for i in range(self.N)]
            canon={z:i for i,z in enumerate(sorted(set(keys)))}
            out=[canon[z] for z in keys]
            if len(set(out))==self.N:return True,steps+1
            if len(set(out))==len(set(colors)):return False,steps+1
            colors=out
        raise AssertionError('nonstabilization')
    def check_triangle(self):
        a=(0,)*self.d
        b=(1,)+(0,)*(self.d-1)
        c=(0,1)+(0,)*(self.d-2)
        P=sum(1<<self.ids[v] for v in (a,b,c))
        D_ab=self.dir_index(a,b);D_ac=self.dir_index(a,c)
        full=(1<<self.N)-1
        Q=self.diamond(P,D_ab)&self.diamond(P,D_ac)&(full^P)
        z=(1,1)+(0,)*(self.d-2)
        assert Q==1<<self.ids[z],('corner_fail',self.q,self.d,Q)
        B=P&self.diamond(Q,D_ac)
        C=P&self.diamond(Q,D_ab)
        assert B==1<<self.ids[b] and C==1<<self.ids[c],('seed_fail',self.q,self.d)
        A=P&~(B|C)
        assert A==1<<self.ids[a]
        for x in self.W:
            if x in (a,b,c):continue
            pair=next(((s,t) for s,t in ((a,b),(a,c),(b,c))
                    if self.dir_index(s,x)!=self.dir_index(t,x)),None)
            assert pair is not None,('no_pair',x)
            s,t=pair
            lhs=self.diamond(1<<self.ids[s],self.dir_index(s,x))
            rhs=self.diamond(1<<self.ids[t],self.dir_index(t,x))
            assert lhs&rhs==1<<self.ids[x],('intersection_fail',self.q,self.d,x)
        return P

counter={'triangles':0,'refinements':0,'exhaustive_labelings':0,'fields':0}
for q,d in ((2,2),(2,3),(3,2),(3,3),(4,2),(4,3),(5,2),(7,2),(8,2),(9,2),(11,2)):
    frame=Frame(q,d);counter['fields']+=1
    if q==2:
        P=1<<frame.ids[(0,)*d]
        for x in frame.W[1:]:
            assert frame.diamond(P,frame.dir_index((0,)*d,x))&~P==1<<frame.ids[x]
    else:
        P=frame.check_triangle()
        counter['triangles']+=1
    assert frame.closure_atoms(P)[0],('partition_fail',q,d)
    counter['refinements']+=1
    if (q,d) in ((2,2),(3,2),(4,2)):
        upper=1 if q==2 else 3
        successful=0
        for k in range(upper+1):
            for subset in combinations(range(frame.N),k):
                mask=sum(1<<i for i in subset)
                full,_=frame.closure_atoms(mask)
                counter['exhaustive_labelings']+=1
                if full:
                    assert k==upper,('unexpected_generator',q,d,k,subset)
                    successful+=1
        if q==3 or q==4:
            predicted=frame.N*(frame.N-1)*(frame.N-q)//6
            assert successful==predicted,('bad_three_census',q,successful,predicted)
        else:
            assert successful==frame.N
print('VERIFY_OK',*[f'{k}={v}' for k,v in counter.items()])
