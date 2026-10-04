from math import gcd


def hard_lefschetz_age_symmetry(r,a,b):
    # Exact integer test for all nontrivial inertia elements represented
    # in mu_a union mu_b. For k/a, age numerator is r*k plus the
    # residue from the other heavy weight unless that coordinate is fixed.
    for k in range(1,a):
        rem=(b*k)%a
        codim=r if rem==0 else r+1
        age_num=r*k + rem
        if 2*age_num != codim*a:
            return False
    for k in range(1,b):
        rem=(a*k)%b
        codim=r if rem==0 else r+1
        age_num=r*k + rem
        if 2*age_num != codim*b:
            return False
    return True


def predicted(a,b):
    return (a,b) in {(1,1),(1,2),(2,2)}

# Exhaustive replay on a substantial finite box.
for r in range(2,81):
    for a in range(1,81):
        for b in range(a,81):
            got=hard_lefschetz_age_symmetry(r,a,b)
            want=predicted(a,b)
            if got != want:
                raise AssertionError((r,a,b,got,want))

# Direct witness algebra behind the infinite proof.
# Equal heavy weights b=a>2: primitive b-th root has ages r/b and r-r/b.
for r in range(2,50):
    for b in range(3,100):
        assert 2*r != r*b
        assert not hard_lefschetz_age_symmetry(r,b,b)

# Unequal case: primitive b-th root gives necessary equation
# 2(r+a)=b(r+1). Check every integer solution in a broad box is (a,b)=(1,2).
for r in range(2,300):
    sols=[]
    for a in range(1,500):
        num=2*(r+a)
        den=r+1
        if num%den==0:
            b=num//den
            if b>a:
                sols.append((a,b))
    assert sols == [(1,2)], (r,sols)

print('VERIFY_OK')
