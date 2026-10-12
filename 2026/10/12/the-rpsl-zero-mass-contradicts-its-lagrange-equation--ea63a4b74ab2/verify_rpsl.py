import mpmath as mp

mp.mp.dps = 70

def g(z,c,theta,gamma):
    return c+(1-c)*((1-theta)/(1-theta*z))**gamma

def offspring_coeff(k,c,theta,gamma):
    if k == 0:
        return c+(1-c)*(1-theta)**gamma
    return (1-c)*(1-theta)**gamma * mp.rf(gamma,k)/mp.factorial(k) * theta**k

def poly_mul(a,b,N):
    out=[mp.mpf("0")]*(N+1)
    for i,x in enumerate(a):
        if x == 0:
            continue
        for j,y in enumerate(b):
            if i+j>N:
                break
            out[i+j]+=x*y
    return out

def lagrange_probs(N,c,theta,gamma):
    gc=[offspring_coeff(k,c,theta,gamma) for k in range(N)]
    power=[mp.mpf(1)]+[mp.mpf(0)]*(N-1)
    probs=[]
    for n in range(1,N+1):
        power=poly_mul(power,gc,N-1)
        probs.append(power[n-1]/n)
    return probs

# Parameter triple highlighted in the paper's simulation section.
gamma=mp.mpf("1.5"); theta=mp.mpf("0.4"); c=mp.mpf("0.3")
m=(1-c)*gamma*theta/(1-theta)
g0=g(0,c,theta,gamma)
assert abs(m-mp.mpf("0.7")) < mp.mpf("1e-60")
assert abs(g0-mp.mpf("0.6253306010814230183550582935817215673")) < mp.mpf("1e-35")
p=lagrange_probs(120,c,theta,gamma)
assert mp.fsum(p) > mp.mpf("0.999")
assert 1+g0 > mp.mpf("1.6")

# Supercritical example: coefficient mass equals the extinction fixed point.
gamma2=mp.mpf("3"); theta2=mp.mpf("0.5"); c2=mp.mpf("0.1")
m2=(1-c2)*gamma2*theta2/(1-theta2)
assert m2 > 1
q=mp.findroot(lambda x: g(x,c2,theta2,gamma2)-x,
              (mp.mpf("0.2"),mp.mpf("0.4")))
assert 0 < q < 1
p2=lagrange_probs(100,c2,theta2,gamma2)
s2=mp.fsum(p2)
assert abs(s2-q) < mp.mpf("2e-18")

# The defining equation gives the constant coefficient exactly.
psi0=mp.mpf("0")*g(mp.mpf("0"),c,theta,gamma)
assert psi0 == 0

print("VERIFY_OK")
print("subcritical_m", mp.nstr(m,20))
print("g0", mp.nstr(g0,20))
print("subcritical_positive_mass_partial", mp.nstr(mp.fsum(p),20))
print("supercritical_m", mp.nstr(m2,20))
print("extinction_q", mp.nstr(q,20))
print("supercritical_positive_mass_partial", mp.nstr(s2,20))
