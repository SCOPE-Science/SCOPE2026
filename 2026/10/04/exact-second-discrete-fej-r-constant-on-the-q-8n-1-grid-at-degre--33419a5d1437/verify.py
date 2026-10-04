import math

def check(n):
    q = 8*n + 1
    theta = 2*math.pi/q
    r, s = 3*n, 3*n + 1
    cr, cs = math.cos(r*theta), math.cos(s*theta)
    dr, ds = math.cos(2*r*theta), math.cos(2*s*theta)
    D = cs*dr - cr*ds
    gr = ds/(2*D)
    gs = -dr/(2*D)
    tau0 = 0.5 + cr*cs
    tau1 = -(cr+cs)/2
    lam = tau1/tau0
    closed = (
        2*math.cos(math.pi/4-math.pi/(4*q))*math.cos(math.pi/q)
        /(1+math.sin(math.pi/(2*q))+math.cos(2*math.pi/q))
    )
    grid = [
        (math.cos(theta*y)-cr)*(math.cos(theta*y)-cs)/tau0
        for y in range(q)
    ]
    assert min(grid) >= -2e-12
    assert gr > 0 and gs > 0
    assert abs(2*(gr*cr+gs*cs)+1) < 2e-12
    assert abs(2*(gr*dr+gs*ds)) < 2e-12
    assert abs((gr+gs)-lam) < 2e-12
    assert abs(lam-closed) < 2e-12
    return q, lam

for n in range(1, 101):
    check(n)

for n in range(1, 6):
    q, lam = check(n)
    print(f"n={n} q={q} lambda={lam:.16f}")
print("VERIFY_OK")
