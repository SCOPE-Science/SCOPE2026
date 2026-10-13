from itertools import product

BASIS=((1,0,0),(0,1,0),(0,0,1))

def bracket(x,y,z,p):
    return (0,(x[2]*(y[2]*z[1]-y[1]*z[2]))%p,0)

def mv(M,x,p):
    return tuple(sum(M[i][j]*x[j] for j in range(3))%p for i in range(3))

def is_rb(flat,p):
    M=(flat[0:3],flat[3:6],flat[6:9])
    for x in BASIS:
        for y in BASIS:
            for z in BASIS:
                Bx=mv(M,x,p)
                By=mv(M,y,p)
                Bz=mv(M,z,p)
                lhs=bracket(Bx,By,Bz,p)
                terms=(
                    bracket(Bx,By,z,p),
                    bracket(Bx,y,Bz,p),
                    bracket(x,By,Bz,p),
                )
                inside=tuple(sum(t[i] for t in terms)%p for i in range(3))
                if lhs!=mv(M,inside,p):
                    return False
    return True

def formula(q,char2):
    if char2:
        return q**6+3*q**5-3*q**4
    return q**6+2*q**5-q**4-q**3

def stratum_count(q,char2):
    total=q**6
    if char2:
        total+=(q-1)*q**4
    else:
        total+=(q-1)*q**3
    total+=2*(q-1)*q**3
    total+=2*(q-1)**2*q**3
    return total

for p in (2,3):
    n=sum(
        1
        for flat in product(range(p),repeat=9)
        if is_rb(flat,p)
    )
    expected=formula(p,p==2)
    assert n==expected,(p,n,expected)
    print({"field":f"F_{p}","direct_count":n})

for q,char2 in ((2,True),(3,False),(5,False),(7,False),(11,False)):
    assert stratum_count(q,char2)==formula(q,char2)

# Characteristic-two extra boundary witness:
# diag(0,1,1) in the chosen basis.
witness=(0,0,0, 0,1,0, 0,0,1)
assert is_rb(witness,2)
assert not is_rb(witness,3)

# The two polynomials differ by q^3(q-1)^2.
for q in range(2,20):
    assert (
        (q**6+3*q**5-3*q**4)
        -(q**6+2*q**5-q**4-q**3)
        == q**3*(q-1)**2
    )

print("VERIFY_OK")
