from fractions import Fraction as F
def coeffs(s,k,g,b,c):
    return s+c*(k-g)/2, -b+c*k
s,k,g,b,c=map(F,[1,1,2,4,2])
q1,q2=coeffs(s,k,g,b,c)
assert q1==0 and q2==-2
assert g>k and 2*s*k<=b*(g-k)
for s,k,g,b in [(F(1),F(1),F(2),F(4)),(F(1,3),F(1,5),F(4,5),F(2)),(F(2),F(0),F(1),F(1))]:
    assert g>k and 2*s*k<=b*(g-k)
    c=2*s/(g-k)
    q1,q2=coeffs(s,k,g,b,c)
    assert q1<=0 and q2<=0
print('VERIFY_OK')
