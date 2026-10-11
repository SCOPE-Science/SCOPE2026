import math

# Adjacent cuboctahedral square vertices on the unit sphere.
p = (1/math.sqrt(2), 0.0, -1/math.sqrt(2))
q = (0.0, 1/math.sqrt(2), -1/math.sqrt(2))
dot = sum(x*y for x,y in zip(p,q))
assert abs(dot - 0.5) < 1e-15
side = math.acos(dot)
assert abs(side - math.pi/3) < 1e-15

# Independent check from the stereographic square vertices r and i r.
r = math.sqrt(2) - 1

def inv_stereo(x, y):
    d = 1 + x*x + y*y
    return (2*x/d, 2*y/d, (x*x+y*y-1)/d)

u = inv_stereo(r, 0.0)
v = inv_stereo(0.0, r)
dot2 = sum(x*y for x,y in zip(u,v))
assert abs(dot2 - 0.5) < 2e-15
assert abs(math.acos(dot2) - math.pi/3) < 2e-15
assert abs(4*side - 4*math.pi/3) < 4e-15
print("VERIFY_OK side=pi/3 smooth_total=4pi/3")
