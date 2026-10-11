import math

def shoelace(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   - poly[(i+1)%len(poly)][0]*poly[i][1]
                   for i in range(len(poly))))/2.0

prev = None
for n in range(3, 102, 2):
    w = 1.0
    beta = math.pi/(2*n)
    R = w/(2*math.cos(beta))
    verts = [(R*math.cos(2*math.pi*j/n), R*math.sin(2*math.pi*j/n))
             for j in range(n)]

    # Conv(±v_j) in angular order.
    allv = verts + [(-x,-y) for x,y in verts]
    allv.sort(key=lambda p: math.atan2(p[1],p[0]))
    A_poly = shoelace(allv)
    A_poly_formula = n*w*w*math.tan(beta)/2
    assert abs(A_poly-A_poly_formula) < 1e-11

    # Strip normals perpendicular to the n reflection axes.
    for j in range(n):
        theta = 2*math.pi*j/n + math.pi/2
        u = (math.cos(theta), math.sin(theta))
        vals = [abs(x*u[0]+y*u[1]) for x,y in verts]
        assert max(vals) <= w/2 + 1e-12

    # The regular 2n-gon has apothem w/2.
    side_normal_angle = (math.atan2(allv[0][1],allv[0][0])
                         + math.atan2(allv[1][1],allv[1][0]))/2
    apothem = abs(R*math.cos(math.pi/(2*n)))
    assert abs(apothem-w/2) < 1e-12

    # Firey's displayed formula and the simplified formula.
    alpha = math.pi/n
    A_firey = math.pi/2 * (1 - (1-math.cos(alpha))/(alpha*math.sin(alpha)))
    A_simple = math.pi/2 - n*math.tan(beta)/2
    assert abs(A_firey-A_simple) < 1e-12

    E = A_simple/A_poly_formula
    E_formula = math.pi/(n*math.tan(beta))-1
    assert abs(E-E_formula) < 1e-12
    assert 0 < E < 1
    if prev is not None:
        assert E > prev
    prev = E

print("VERIFY_OK")
print("E3 =", math.pi/math.sqrt(3)-1)
print("E101 =", prev)
