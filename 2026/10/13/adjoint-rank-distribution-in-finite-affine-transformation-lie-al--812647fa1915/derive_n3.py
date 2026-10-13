import sympy as s
q,z=s.symbols('q z',integer=True,positive=True)
G=s.prod(q**3-q**i for i in range(3))
from collections import defaultdict
coeff=defaultdict(lambda: s.Integer(0)); cases=[]
def add(label,mult,C,c,blocks):
 k=sum(b for length,b in blocks.items());base=12-c-k
 w=mult*G/C*q**(3-k)
 coeff[base]+=w
 m=0
 for length,b in sorted(blocks.items()):
  m+=b
  coeff[base+m]+=w*q**(m-b)*(q**b-1)
 cases.append((label,mult,C,c,blocks))
# irreducible cubic
add('cubic', (q**3-q)/3, q**3-1, 3,{})
# quad times linear
I2=(q*q-q)/2
add('quad, nonzero linear',I2*(q-1),(q*q-1)*(q-1),3,{})
add('quad, zero linear',I2,(q*q-1)*(q-1),3,{1:1})
# distinct linear
add('three nonzero eigenvalues', s.binomial(q-1,3),(q-1)**3,3,{})
add('three distinct including zero',s.binomial(q-1,2),(q-1)**3,3,{1:1})
# J2(a) + scalar(b)
add('J2 nonzero a; nonzero b', (q-1)*(q-2),q*(q-1)**2,3,{})
add('J2 zero a; nonzero b',q-1,q*(q-1)**2,3,{2:1})
add('J2 nonzero a; zero b',q-1,q*(q-1)**2,3,{1:1})
# aI2 plus scalar b
GL2=(q*q-1)*(q*q-q)
add('repeated scalar a and b both nonzero', (q-1)*(q-2),GL2*(q-1),5,{})
add('repeated scalar a zero',q-1,GL2*(q-1),5,{1:2})
add('only single b zero',q-1,GL2*(q-1),5,{1:1})
# single linear eigen a
add('J3 nonzero',q-1,q*q*(q-1),3,{})
add('J3 zero',1,q*q*(q-1),3,{3:1})
add('J2 J1 nonzero',q-1,q**3*(q-1)**2,5,{})
add('J2 J1 zero',1,q**3*(q-1)**2,5,{1:1,2:1})
add('scalar nonzero',q-1,G,9,{})
add('scalar zero',1,G,9,{1:3})
poly=s.Integer(0)
for d in sorted(coeff):
 val=s.factor(s.cancel(s.expand_func(coeff[d])))
 poly+=val*z**d
 print(d,':',val,'at2',val.subs(q,2))
print('total:',s.factor(poly.subs(z,1)), 'expected', q**12)
print('commuting pair count:',s.factor(s.expand_func(sum(s.cancel(coeff[d])*q**(12-d) for d in coeff))))
expected={
 0:1,
 3:(q-1)*(q+1)*(q**2+1),
 5:q*(q-1)*(q**2+q+1)**2,
 6:q*(q-1)*(q**2+q+1)*(q**3+q**2-1),
 7:q**2*(q-1)*(q**2+q+1)*(q**4+q**3-2*q-1),
 8:q**3*(q-1)*(q**2+q+1)*(q**4+q**3-2*q-1),
 9:q**3*(q-1)*(q+1)*(q**7-2*q**4-q**3+2*q+1),
}
assert set(coeff)==set(expected)
for d in expected:
    assert s.cancel(s.expand_func(coeff[d]-expected[d]))==0,(d,s.factor(coeff[d]-expected[d]))
assert s.cancel(s.expand_func(sum(coeff.values())-q**12))==0
commuting=s.factor(s.expand_func(sum(coeff[d]*q**(12-d) for d in coeff)))
assert s.cancel(s.expand_func(commuting-q**6*(q**9+2*q**8+4*q**7+q**6-6*q**5-5*q**4+4*q**2+q-1)))==0
assert [int(expected[i].subs(q,2)) if hasattr(expected[i], 'subs') else expected[i] for i in sorted(expected)]==[1,15,98,154,532,1064,2232]
print('SYMBOLIC_VERIFY_OK')
