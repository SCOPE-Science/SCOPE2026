import math

I = ((1+0j,0j),(0j,1+0j))
Y = ((0j,-1j),(1j,0j))
Z = ((1+0j,0j),(0j,-1+0j))

def kron(a,b):
    ar, ac = len(a), len(a[0])
    br, bc = len(b), len(b[0])
    return tuple(tuple(a[i//br][j//bc]*b[i%br][j%bc] for j in range(ac*bc)) for i in range(ar*br))

def kron_all(ops):
    out = ((1+0j,),)
    for op in ops:
        out = kron(out, op)
    return out

def mm(a,b):
    n, m, p = len(a), len(b), len(b[0])
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(m)) for j in range(p)) for i in range(n))

def madd(a,b,sa=1+0j,sb=1+0j):
    return tuple(tuple(sa*a[i][j]+sb*b[i][j] for j in range(len(a[0]))) for i in range(len(a)))

def ident(n):
    return tuple(tuple(1+0j if i==j else 0j for j in range(n)) for i in range(n))

def norm_inf(a):
    return max(abs(x) for row in a for x in row)

def exp_pauli(p,t):
    return madd(ident(len(p)), p, math.cos(t), -1j*math.sin(t))

def mv(a,v):
    return tuple(sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(a)))

def inner(u,v):
    return sum(x.conjugate()*y for x,y in zip(u,v))

def pauli_string(n, mapping):
    return kron_all([mapping.get(i,I) for i in range(n)])

def commutes(a,b,tol=1e-12):
    return norm_inf(madd(mm(a,b),mm(b,a),1,-1)) < tol

def anticommutes(a,b,tol=1e-12):
    return norm_inf(madd(mm(a,b),mm(b,a),1,1)) < tol

star1=[]
for k in range(3):
    star1.append(pauli_string(7,{0:Y,2*k+1:Z,2*k+2:Z}))
for i in range(len(star1)):
    for j in range(i+1,len(star1)):
        assert commutes(star1[i],star1[j])

star2=[]
for k in range(3):
    star2.append(pauli_string(5,{0:Z,1:Z,k+2:Y}))
for i in range(len(star2)):
    for j in range(i+1,len(star2)):
        assert commutes(star2[i],star2[j])

A=pauli_string(4,{0:Z,1:Z,2:Y})
B=pauli_string(4,{1:Z,2:Z,3:Y})
assert anticommutes(A,B)

plus=(1/math.sqrt(2),1/math.sqrt(2))
psi=plus
for _ in range(3):
    psi=tuple(x*y for x in psi for y in plus)

for a,b in [(0.2,0.3),(0.4,0.7),(math.pi/4,math.pi/4)]:
    psi10=mv(mm(exp_pauli(B,b),exp_pauli(A,a)),psi)
    psi01=mv(mm(exp_pauli(A,a),exp_pauli(B,b)),psi)
    got=inner(psi01,psi10)
    want=1-2*(math.sin(a)**2)*(math.sin(b)**2)
    assert abs(got-want)<1e-11

a=b=math.pi/4
psi10=mv(mm(exp_pauli(B,b),exp_pauli(A,a)),psi)
psi01=mv(mm(exp_pauli(A,a),exp_pauli(B,b)),psi)
assert abs(abs(inner(psi01,psi10))**2-0.25)<1e-11

print("VERIFY_OK")
