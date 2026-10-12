from fractions import Fraction as Q

# Basis: L,A1,...,A16 with Gram diag(16,-2,...,-2).
def dot(x,y):
    return 16*x[0]*y[0] - 2*sum(x[i]*y[i] for i in range(1,17))

def vec(L=0, **a):
    v=[Q(0) for _ in range(17)]
    v[0]=Q(L)
    for k,val in a.items():
        v[int(k[1:])] = Q(val)
    return v

def add(x,y): return [a+b for a,b in zip(x,y)]
def sub(x,y): return [a-b for a,b in zip(x,y)]
def scale(c,x): return [Q(c)*a for a in x]

A=[None]+[vec(**{f'A{i}':1}) for i in range(1,17)]
F=scale(Q(1,2), vec(L=1,A1=-1,A2=-1,A3=-1,A4=-1))
B=[None]
for i in range(1,5):
    coeff={f'A{j}':(-3 if j==i else -1) for j in range(1,5)}
    B.append(scale(Q(1,2), vec(L=1, **coeff)))

assert dot(F,F)==2
for i in range(1,5):
    assert dot(B[i],B[i])==-2
    assert add(A[i],B[i])==F
    assert dot(F,A[i])==1
    assert dot(F,B[i])==1
for i in range(1,5):
    for j in range(i+1,5):
        assert dot(B[i],B[j])==0
for j in range(5,17):
    assert dot(F,A[j])==0

# Symbolic numerical thresholds used in the proof.
# F.Gamma < 0 gives 64 a^2 < 32 a^2 + 4, hence a^2 < 1/8;
# positive a in (1/2)Z has a^2 >= 1/4, contradiction.
assert Q(1,4) > Q(1,8)
# F.Gamma = 0 gives a^2 <= 1/8, hence half-integral a must be zero.
# For a=0, eight nonzero half-integral b_i already give sum b_i^2 >= 2 > 1.
assert 8*Q(1,2)**2 == 2 > 1
# If F=2E+A_j for a contracted A_j, E has L coefficient 1/4,
# forbidden by the source's Lemma 8 (all L coefficients lie in (1/2)Z).
assert F[0]/2 == Q(1,4)
assert F[0]/2 not in {Q(k,2) for k in range(-20,21)}

print('VERIFY_OK')
