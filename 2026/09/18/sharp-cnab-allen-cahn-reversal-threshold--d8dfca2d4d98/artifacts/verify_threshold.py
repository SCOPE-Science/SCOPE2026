import math


def g(x):
    return x * (1.0 - x*x)


def exact_starter(a, h):
    return 1.0 / math.sqrt(1.0 + (a**-2 - 1.0) * math.exp(-2.0*h))


def threshold_state(a, alpha=1.5):
    if not (0.0 < a < 1.0 and alpha > 1.0):
        raise ValueError("require 0<a<1 and alpha>1")
    q = (alpha - 1.0) / alpha
    arg = -(3.0*math.sqrt(3.0)/2.0) * q * a * (1.0-a*a)
    return (2.0/math.sqrt(3.0)) * math.cos(math.acos(arg)/3.0)


def threshold_h(a, alpha=1.5):
    q = (alpha - 1.0) / alpha
    b = threshold_state(a, alpha)
    return 0.5 * math.log(b**3 / (q*a**3))


def extrapolation_bracket(a, h, alpha=1.5):
    b = exact_starter(a, h)
    return alpha * ((alpha-1.0)/alpha * g(a) - g(b))


def source_sufficient_h(a):
    return 0.5 * math.log(3.0/a**3)


print("AB2 sharp threshold checks")
for a in [0.01, 0.1, 0.5, 1.0/math.sqrt(3.0), 0.8, 0.95, 0.99]:
    b = threshold_state(a)
    h = threshold_h(a)
    hs = source_sufficient_h(a)
    root_res = 3.0*g(b) - g(a)
    starter_res = exact_starter(a, h) - b
    em = extrapolation_bracket(a, h-1e-7)
    ep = extrapolation_bracket(a, h+1e-7)
    assert abs(root_res) < 2e-13
    assert abs(starter_res) < 2e-13
    assert em < 0.0 < ep
    print(f"a={a:.15g} b*={b:.15g} h*={h:.15g} h_src={hs:.15g} gap={hs-h:.15g}")

astar = 1.0/math.sqrt(3.0)
bmin = threshold_state(astar)
gapmax = -1.5*math.log(bmin)
print(f"max_source_gap_at_a=1/sqrt(3): b*={bmin:.15g}, gap={gapmax:.15g}")
print(f"near_equilibrium_AB2_limit={0.5*math.log(3.0):.15g}")

print("general over-extrapolation checks at a=0.5")
for alpha in [1.1, 1.2, 1.5, 2.0, 3.0, 10.0]:
    q = (alpha-1.0)/alpha
    b = threshold_state(0.5, alpha)
    h = threshold_h(0.5, alpha)
    root_res = g(b)-q*g(0.5)
    em = extrapolation_bracket(0.5, h-1e-7, alpha)
    ep = extrapolation_bracket(0.5, h+1e-7, alpha)
    assert abs(root_res) < 2e-13
    assert em < 0.0 < ep
    print(f"alpha={alpha:.6g} q={q:.15g} bq={b:.15g} hq={h:.15g} equilibrium_limit={0.5*math.log(1.0/q):.15g}")
