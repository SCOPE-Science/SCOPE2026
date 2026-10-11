import math

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

for k in range(2, 201):
    n = 3*k
    m = k+1
    a = math.pi/n
    half_delta = math.pi*m/n
    c = math.cos(half_delta)
    s = math.sin(half_delta)

    if k == 2:
        assert abs(c) < 1e-14
    else:
        assert c > 0.0

    R = c/math.cos(a)
    R_alt = 0.5 - math.sqrt(3.0)/2.0*math.tan(a)
    assert abs(R-R_alt) < 2e-13
    if k >= 3:
        assert 0.0 < R < 0.5

    # Determinant/half-plane identity for deterministic phases and centers.
    for phase in (0.0, 0.173, 1.019):
        for j in (0, 1, n//3, n-1):
            alpha = phase + 2*math.pi*j/n
            beta = alpha + 2*half_delta
            P = (math.cos(alpha), math.sin(alpha))
            Q = (math.cos(beta), math.sin(beta))
            u = (math.cos(alpha+half_delta), math.sin(alpha+half_delta))
            for O in ((0.0,0.0),(0.07,-0.03),(-0.11,0.05)):
                lhs = det(sub(P,O), sub(Q,O))
                rhs = 2*s*(c-dot(O,u))
                assert abs(lhs-rhs) < 2e-12

    if k >= 3:
        # Reconstruct vertices from adjacent normal lines u_j.x=c.
        phase = 0.271
        normals = [
            (math.cos(phase+2*math.pi*j/n+half_delta),
             math.sin(phase+2*math.pi*j/n+half_delta))
            for j in range(n)
        ]
        verts=[]
        for j in range(n):
            u=normals[j]
            v=normals[(j+1)%n]
            D=det(u,v)
            # Solve [u;v] x = [c;c].
            x=c*(v[1]-u[1])/D
            y=c*(u[0]-v[0])/D
            verts.append((x,y))
            assert abs(math.hypot(x,y)-R) < 2e-11
        area=0.5*abs(sum(det(verts[j],verts[(j+1)%n]) for j in range(n)))
        area_formula=n*c*c*math.tan(math.pi/n)
        assert abs(area-area_formula) < 2e-10

# Limit benchmarks, intentionally loose because the proof is analytic.
k=100000
n=3*k
c=math.cos(math.pi*(k+1)/(3*k))
R=c/math.cos(math.pi/(3*k))
A=n*c*c*math.tan(math.pi/n)
assert abs(c-0.5) < 1e-5
assert abs(R-0.5) < 1e-5
assert abs(A-math.pi/4) < 4e-5

print("VERIFY_OK")
print("k_range=2..200 determinant_and_polygon_checks")
print("limit_benchmark_k=100000")
