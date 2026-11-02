#!/usr/bin/env python3
"""Exact modular and integer checks for a Fibonacci--Lucas digit-sum theorem.

This program uses only the Python standard library. Factored terms at index 827
are transcribed from published Fibonacci/Lucas factorization tables; this
program checks their products and digit sums, not primality certificates.
"""

def matmul(a,b,m):
    return (( (a[0][0]*b[0][0]+a[0][1]*b[1][0])%m,
              (a[0][0]*b[0][1]+a[0][1]*b[1][1])%m ),
            ( (a[1][0]*b[0][0]+a[1][1]*b[1][0])%m,
              (a[1][0]*b[0][1]+a[1][1]*b[1][1])%m ))

def power(m,e):
    q=((1,1),(1,0)); v=((1,0),(0,1))
    for _ in range(e):v=matmul(v,q,m)
    return v

assert power(4,6)==((1,0),(0,1))
assert power(9,24)==((1,0),(0,1))

four=(2,3,3,2,3,3)
nine=(7,8,8,2,2,3,1,2,1,8,8,8,
      2,3,7,5,4,8,8,5,2,3,4,8)
assert len(four)==6 and len(nine)==24
assert all(v!=0 for v in nine)
assert [i for i,x in enumerate(nine) if x%3==0]==[5,13,21]

# Compute the complete period by an independent 2x2 matrix orbit.
for m,period,want in ((4,6,four),(9,24,nine)):
    for n in range(period):
        q=power(m,n); f=q[0][1]; l=(q[0][0]+q[1][1])%m
        got=(f*l-f-l)%m
        assert got==want[n],(m,n,got,want[n])

# Check 10,000 direct recurrence indices against both periodic laws.
f0,f1=0,1; l0,l1=2,1
for n in range(1,10001):
    f0,f1=f1,f0+f1
    l0,l1=l1,l0+l1
    t=f0*l0-f0-l0
    assert t%4==four[n%6]
    assert t%9==nine[n%24]
    assert (t%4==2)==(n%3==0)
    assert (t%9==3)==(n%8==5)

fs=(
  183593,
  6254838942964147339957,
  106300393601859050294647534380697,
  14459470923426350620886866234819533010560061654086793457,
  17239868933231410572458316498947999854910104288278141976517,
)
ls=(
  1257041,
  16721941,
  28837105949471,
  241966641660839,
  1352805356114179046939,
  1081676837823661872260758079,
  317031446954850533955668682035991206482881263542292407676309907499596450018199509431,
)

def digit_sum(n):return sum(map(int,str(n)))
def product(items):
    x=1
    for y in items:x*=y
    return x

f0,f1=0,1; l0,l1=2,1
for _ in range(827):
    f0,f1=f1,f0+f1
    l0,l1=l1,l0+l1
assert product(fs)==f0
assert product(ls)==l0
assert digit_sum(f0)==sum(map(digit_sum,fs))==809
assert digit_sum(l0)==sum(map(digit_sum,ls))==802
assert digit_sum(f0*l0)==1592
assert digit_sum(f0*l0)-809-802==-19
assert (f0*l0-f0-l0)%9==8
assert (digit_sum(f0*l0)-digit_sum(f0)-digit_sum(l0))%9==8

print('VERIFY_OK matrix_periods=6,24 exact_period_residues=6,24 '
      'direct_indices=10000 f827_digit=809 l827_digit=802 '
      'f1654_digit=1592 smith_deficit=-19 factor_products=verified '
      'prime_certificates=not_independently_checked')
