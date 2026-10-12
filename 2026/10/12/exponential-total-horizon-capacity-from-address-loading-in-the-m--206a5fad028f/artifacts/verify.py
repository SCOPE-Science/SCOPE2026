import math

def f(t):
    return t/(2**t)*math.log2(1+t)
vals=[f(t) for t in range(1,1001)]
assert vals[1] == max(vals)
assert abs(vals[1]-0.5*math.log2(3)) < 1e-15
assert f(3) < f(2)
for t in range(3,1000):
    assert f(t+1) < f(t)
# constants in the sandwich
lo=math.log2(3)/32
hi_profile=math.log2(3)/2
assert lo>0 and hi_profile>0
print('VERIFY_OK')
