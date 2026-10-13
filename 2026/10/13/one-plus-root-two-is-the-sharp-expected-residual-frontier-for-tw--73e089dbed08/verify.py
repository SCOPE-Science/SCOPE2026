from fractions import Fraction as F

def expected_matrix(a,b,c):
    c=abs(F(c))
    a=F(a); b=F(b)
    if c == 0:
        return [[F(b,a+b),F(0)],[F(0),F(a,a+b)]]
    p=c/a
    q=c/b
    den=p+q
    return [
        [p*(1+p*q)/den, -2*p*q/den],
        [-2*p*q/den, q*(1+p*q)/den]
    ]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

# Exact factorization checks on several SPD rational matrices.
cases=[(2,2,1),(5,3,1),(7,4,2),(10,6,3)]
for a,b,c in cases:
    assert F(c*c) < F(a*b)
    M=expected_matrix(a,b,c)
    p=F(abs(c),a); q=F(abs(c),b)
    Iminus=[[F(1)-M[0][0],-M[0][1]],[-M[1][0],F(1)-M[1][1]]]
    fact=p*q*(p*q-p-q-F(1))*(p*q+p+q-F(1))/(p+q)**2
    assert det2(Iminus)==fact
    criterion=(p+q+p*q <= 1)
    psd=(Iminus[0][0]>=0 and Iminus[1][1]>=0 and det2(Iminus)>=0)
    assert criterion==psd

# Exact kappa=3 witness.
a=b=F(2); c=F(1)
r1,r2=F(1),F(-1)
# coordinate 1
s1=(r2-c/a*r1)
# coordinate 2
s2=(r1-c/b*r2)
assert s1==F(-3,2)
assert s2==F(3,2)
incoming=r1*r1+r2*r2
expected=F(1,2)*s1*s1+F(1,2)*s2*s2
assert incoming==F(2)
assert expected==F(9,4)
assert expected/incoming==F(9,8)

# Equal-diagonal sharpness family for rational kappa values.
for k in [F(2),F(3),F(5),F(10)]:
    aa=(k+1)/2
    cc=(k-1)/2
    rr=2*k*k/(k+1)**2
    # direct expected ratio from r=(1,-1)
    delta=cc/aa
    direct=(1+delta)**2/2
    assert rr==direct

print("VERIFY_OK")
print("witness_ratio_sq", expected/incoming)
