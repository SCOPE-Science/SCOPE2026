"""Independent arithmetic checks of the harmonic-quadruple classification.

No external dependencies. Run: python verify_finite_fields.py
Finite tests corroborate the algebraic proof; they do not replace it.
"""
from itertools import combinations

class Field:
    # Represent elements as tuples of coefficients of 1,t,...,t^(d-1).
    def __init__(self, degree, relation):
        self.d = degree
        self.n = 3**degree
        self.relation = relation  # coefficients of t^degree in descending reduction
    def co(self, x):
        return tuple((x//(3**i))%3 for i in range(self.d))
    def enc(self, a):
        return sum((x%3)*3**i for i,x in enumerate(a))
    def add(self,a,b):
        x,y=self.co(a),self.co(b)
        return self.enc([x[i]+y[i] for i in range(self.d)])
    def neg(self,a):
        return self.enc([-x for x in self.co(a)])
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        x,y=self.co(a),self.co(b)
        p=[0]*(2*self.d-1)
        for i in range(self.d):
            for j in range(self.d):
                p[i+j]+=x[i]*y[j]
        for i in range(len(p)-1,self.d-1,-1):
            factor=p[i]
            for j in range(self.d):
                p[i-self.d+j]+=factor*self.relation[j]
        return self.enc(p[:self.d])
    def inv(self,a):
        if a==0:raise ZeroDivisionError
        for b in range(1,self.n):
            if self.mul(a,b)==1:return b
        raise ArithmeticError('not a field')
    def div(self,a,b):return self.mul(a,self.inv(b))
    def points(self):return range(self.n)

# F9 = F3[t]/(t^2+1), so t^2 = -1.
# F27 = F3[t]/(t^3-t-1), so t^3 = t+1 (irreducible).
for d, relation in [(2,(2,0)), (3,(1,1,0))]:
    F=Field(d,relation)
    q=F.n
    assert all(F.mul(x,F.inv(x)) == 1 for x in range(1,q))
    def cr(a,b,c,w):
        # Send ordered a,b,c to infinity,zero,one; compute image of w.
        if a is None:
            return F.div(F.sub(w,b),F.sub(c,b))
        if b is None:
            return F.div(F.sub(c,a),F.sub(w,a))
        if c is None:
            return F.div(F.sub(w,b),F.sub(w,a))
        if w is None:
            return F.div(F.sub(c,a),F.sub(c,b))
        return F.div(F.mul(F.sub(w,b),F.sub(c,a)),
                     F.mul(F.sub(w,a),F.sub(c,b)))
    counts=[0,0,0,0,0,0]
    curves=[0]*5
    for u in F.points():
        for v in F.points():
            if 0 in (u,v) or 1 in (u,v) or u==v:
                continue
            P=[None,0,1,u,v]
            h=[]
            for i in range(5):
                quad=[P[j] for j in range(5) if j!=i]
                h.append(cr(*quad)==2)
            assert sum(h)<=1, (d,u,v,h)
            counts[sum(h)]+=1
            expected=(u==2,v==2,F.add(u,v)==0,
                      F.add(F.add(u,v),1)==0,
                      F.add(F.add(F.mul(u,v),u),v)==0)
            # The indices of h omit infinity,0,1,u,v respectively.
            assert h==list(expected[::-1]),(d,u,v,h,expected)
            for i,hit in enumerate(expected):
                curves[i]+=bool(hit)
    assert curves==[q-3]*5,(q,curves)
    assert counts == [(q-3)*(q-7),5*(q-3),0,0,0,0],(q,counts)
    print('FINITE_FIELD_OK', 'q=',q, 'ordinary=',counts[0],
          'rank4=',counts[1], 'five_loci=',curves)
