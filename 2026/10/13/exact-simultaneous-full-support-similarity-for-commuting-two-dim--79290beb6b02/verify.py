#!/usr/bin/env python3
"""Direct finite-field enumeration for simultaneous full-support similarity.
Re-run with: python3 verify.py. Python 3 standard library only.
"""
from itertools import product

class Field:
    def __init__(self,p,mod=None):
        self.p=p;self.mod=mod or [0,1];self.k=len(self.mod)-1;self.q=p**self.k
        self.vec=[tuple((i//(p**j))%p for j in range(self.k)) for i in range(self.q)]
        self.a=[[self.pack((x+y)%p for x,y in zip(v,w)) for w in self.vec] for v in self.vec]
        self.m=[[self.multiply(v,w) for w in self.vec] for v in self.vec]
        self.neg=[next(j for j in range(self.q) if self.a[i][j]==0) for i in range(self.q)]
        self.one=self.pack([1]+[0]*(self.k-1))
        self.inv=[None]+[next(j for j in range(1,self.q) if self.m[i][j]==self.one) for i in range(1,self.q)]
    def pack(self,coeffs):return sum(c*self.p**i for i,c in enumerate(coeffs))
    def multiply(self,v,w):
        a=[0]*(2*self.k-1)
        for i,x in enumerate(v):
            for j,y in enumerate(w): a[i+j]=(a[i+j]+x*y)%self.p
        for i in range(2*self.k-2,self.k-1,-1):
            c=a[i]
            if c:
                for j in range(self.k):a[i-self.k+j]=(a[i-self.k+j]-c*self.mod[j])%self.p
        return self.pack(a[:self.k])
    def sub(self,x,y):return self.a[x][self.neg[y]]
    def mul(self,x,y):return self.m[x][y]
    def add(self,x,y):return self.a[x][y]

def mat_conj_class(F,t,d):
    # Companion matrix C = [[0,-d],[1,t]]. Enumerate every ordered basis.
    q=F.q; add=F.add; sub=F.sub; mul=F.mul;inv=F.inv; one=F.one
    target=set()
    for a,b,c,e in product(range(q),repeat=4):
        det=sub(mul(a,e),mul(b,c))
        if det==0:continue
        dinv=inv[det]
        # C P = [[-d*c,-d*e],[a+t*c,b+t*e]]
        cp=(mul(F.neg[d],c),mul(F.neg[d],e),add(a,mul(t,c)),add(b,mul(t,e)))
        # P^-1 = det^-1 [[e,-b],[-c,a]]
        pi=(mul(e,dinv),mul(F.neg[b],dinv),mul(F.neg[c],dinv),mul(a,dinv))
        B=(add(mul(pi[0],cp[0]),mul(pi[1],cp[2])),
           add(mul(pi[0],cp[1]),mul(pi[1],cp[3])),
           add(mul(pi[2],cp[0]),mul(pi[3],cp[2])),
           add(mul(pi[2],cp[1]),mul(pi[3],cp[3])))
        target.add(B)
    return target

def test(F):
    q=F.q; add=F.add;sub=F.sub;mul=F.mul
    full={(t,d):0 for t,d in product(range(q),repeat=2)}
    nonscalar={(t,d):0 for t,d in product(range(q),repeat=2)}
    for a,b,c,e in product(range(q),repeat=4):
        t=add(a,e);d=sub(mul(a,e),mul(b,c))
        if 0 not in (a,b,c,e):full[t,d]+=1
        if not(b==c==0 and a==e):nonscalar[t,d]+=1
    exceptions=[]; checked=0
    for t,d in product(range(q),repeat=2):
        allowed=[a for a in range(q) if a!=0 and sub(t,a)!=0]
        roots=[a for a in range(q) if sub(sub(mul(a,a),mul(t,a)),F.neg[d])==0]
        # a^2-t*a+d, use add method to avoid mixing sign conventions
        roots=[a for a in range(q) if add(sub(mul(a,a),mul(t,a)),d)==0]
        effroots=roots if d!=0 else []
        predicted=(q-1)*(len(allowed)-len(effroots))
        assert full[t,d]==predicted, (q,t,d,full[t,d],predicted)
        if len(roots)==0:orbit=q*(q-1);kind='irreducible'
        elif len(roots)==2:orbit=q*(q+1);kind='split_distinct'
        else:orbit=q*q-1;kind='Jordan'
        assert nonscalar[t,d]==orbit, (q,t,d,kind,nonscalar[t,d],orbit)
        if q<=5:
            cls=mat_conj_class(F,t,d)
            o,b=len(cls),sum(0 not in X for X in cls)
            assert (o,b)==(orbit,predicted),(q,t,d,o,b,orbit,predicted)
            for r in range(q):
                forb={0,t,F.neg[r],add(t,r)}
                roots={x for x in range(q) if add(sub(mul(x,x),mul(t,x)),d)==0}
                expected_joint=(q-1)*sum(x not in forb and x not in roots for x in range(q))
                actual_joint=sum(0 not in X and X[0]!=F.neg[r] and X[3]!=F.neg[r] for X in cls)
                assert actual_joint==expected_joint,(q,t,d,r,actual_joint,expected_joint)
            if q<=4:
                for r,s in product(range(q),repeat=2):
                    forb={0,t,F.neg[r],add(t,r),F.neg[s],add(t,s)}
                    roots={x for x in range(q) if add(sub(mul(x,x),mul(t,x)),d)==0}
                    expected_joint=(q-1)*sum(x not in forb and x not in roots for x in range(q))
                    actual_joint=sum(X[1]!=0 and X[2]!=0 and all(F.add(X[0],shift)!=0 and F.add(X[3],shift)!=0 for shift in (0,r,s)) for X in cls)
                    assert actual_joint==expected_joint,(q,t,d,r,s,actual_joint,expected_joint)
        if predicted==0:exceptions.append((t,d,kind))
        checked+=1
    expected=3 if q in (2,3,4) else 0
    assert len(exceptions)==expected,(q,exceptions)
    print('q=%d pairs=%d full_support_matrices=%d exceptions=%s verified=OK'%(q,checked,sum(full.values()),exceptions))

def check_obstructions():
    F=Field(5)
    t,d,r=1,4,3
    cls=mat_conj_class(F,t,d)
    goodA=[X for X in cls if 0 not in X]
    goodB=[X for X in cls if X[1]!=0 and X[2]!=0 and F.add(X[0],r)!=0 and F.add(X[3],r)!=0]
    assert goodA and goodB and not(set(goodA)&set(goodB))
    print('q=5 commuting pair: individually realizable, jointly impossible, verified=OK')
    # In F_8=F_2[T]/(T^3+T+1), t=1 and the roots are alpha=2,alpha+1=3.
    F=Field(2,[1,1,0,1]); q=F.q;t=1;alpha=2;d=F.mul(alpha,F.add(alpha,t))
    pairs=[]; seen=set()
    for a in range(q):
        b=F.add(a,t)
        if a not in seen:
            pairs.append((a,b));seen.update((a,b))
    omitted={alpha,F.add(alpha,t)}
    shifts=[a for a,b in pairs if {a,b}!=omitted]
    assert len(shifts)==3 and 0 in shifts
    cls=mat_conj_class(F,t,d)
    per=[sum(X[1]!=0 and X[2]!=0 and F.add(X[0],r)!=0 and F.add(X[3],r)!=0 for X in cls) for r in shifts]
    both=sum(all(X[1]!=0 and X[2]!=0 and F.add(X[0],r)!=0 and F.add(X[3],r)!=0 for r in shifts) for X in cls)
    assert all(per) and both==0, (shifts,per,both)
    print('q=8 commuting triple: every member individually realizable, no common basis, verified=OK')

if __name__=='__main__':
    for p,poly in [(2,None),(3,None),(5,None),(7,None),(11,None),(2,[1,1,1]),(2,[1,1,0,1]),(3,[1,0,1])]:
        test(Field(p,poly))
    check_obstructions()
    print('VERIFY_OK')
