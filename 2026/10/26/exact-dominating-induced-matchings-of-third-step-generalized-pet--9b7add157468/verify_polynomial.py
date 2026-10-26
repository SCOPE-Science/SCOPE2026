"""Exact integer-polynomial and five-column checks for the spectral proof.
No symbolic algebra library needed; the mathematical proof identifies the roots.
"""

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]+=ai*bj
    return c

def sub(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]-=v
    return out

p=sub(mul([1,2,1],[1,0,0,2,0,0,1]),[0,0,0,0,1])
phi5=[1,1,1,1,1]
R=[1,1,-1,1,1]
assert p==mul(phi5,R),(p,mul(phi5,R))
# Reduction modulo 2 equals Phi_5 and has no linear or quadratic factor:
assert [v%2 for v in R]==phi5
assert sum(phi5)%2==1 and phi5[0]==1
# In F_2[z], a degree-four polynomial is irreducible if it has no
# linear factor and is not divisible by the sole irreducible quadratic.
def gf2_remainder(f, g):
    while f.bit_length() >= g.bit_length():
        f ^= g << (f.bit_length()-g.bit_length())
    return f
assert gf2_remainder(0b11111, 0b111) != 0
valid=[]
for mask in range(1<<5):
    x=tuple(mask>>i&1 for i in range(5))
    y=tuple(3-2*x[i]-x[(i-1)%5]-x[(i+1)%5] for i in range(5))
    if not all(v in (0,1) for v in y):continue
    if all(x[i]+2*y[i]+y[(i-3)%5]+y[(i+3)%5]==3 for i in range(5)):
        valid.append((x,y))
assert len(valid)==5
assert all(sum(x)==3 and sum(y)==3 for x,y in valid)
print('P(z)=',p)
print('Phi5(z)=',phi5)
print('R(z)=',R)
print('period_five_binary_solutions=',len(valid))
for x,y in valid:print(''.join(map(str,x)),''.join(map(str,y)))
print('PASS: polynomial factorization and 5-period binary classification')
