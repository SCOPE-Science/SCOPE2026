from math import gcd

def c_dual(A, B, V):
    return 3*A - 2*B + V

def triangle_data(d):
    A = d*d
    B = 3*d
    V = 3
    g = (d-1)*(d-2)//2
    delta = c_dual(A,B,V)
    return g, A, delta

def right_triangle_is_smooth(a,b):
    q = gcd(a,b)
    # determinants at the two non-origin vertices have absolute values b/q and a/q
    return b//q == 1 and a//q == 1

triangle_checks = 0
for d in range(2,201):
    g,A,delta = triangle_data(d)
    assert delta - A == 4*g - 1
    assert delta > 0
    triangle_checks += 1

smoothness_checks = 0
for a in range(1,201):
    for b in range(1,201):
        assert right_triangle_is_smooth(a,b) == (a == b)
        smoothness_checks += 1

rectangle_checks = 0
for g in range(0,1001):
    # P=[0,2]x[0,g+1]
    A = 4*(g+1)
    B = 2*(2+(g+1))
    V = 4
    I = (A-B+2)//2
    assert I == g
    delta = c_dual(A,B,V)
    assert delta - A == 4*g
    if g >= 1:
        assert delta > 0
    rectangle_checks += 1

for g in range(0,1001):
    triangular = False
    d_hit = None
    for d in range(2,100):
        if (d-1)*(d-2)//2 == g:
            triangular = True
            d_hit = d
            break
        if (d-1)*(d-2)//2 > g:
            break
    predicted = 4*g - 1 if triangular else 4*g
    if triangular:
        gg,A,delta = triangle_data(d_hit)
        assert gg == g and delta-A == predicted
    else:
        A = 4*(g+1)
        B = 2*(g+3)
        delta = c_dual(A,B,4)
        assert delta-A == predicted

print('VERIFY_OK', triangle_checks, smoothness_checks, rectangle_checks)
