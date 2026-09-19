from mpmath import mp

mp.dps = 60


def bisect(f, lo, hi, iters=220):
    flo = f(lo)
    fhi = f(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        raise RuntimeError(f"no sign change on [{lo}, {hi}]: {flo}, {fhi}")
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = f(mid)
        if fm == 0:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def limiting_a():
    return bisect(lambda z: z * mp.tanh(z) - 1, mp.mpf('1'), mp.mpf('2'))


def limiting_z(k):
    eps = mp.mpf('1e-30')
    lo = (mp.mpf(k) - mp.mpf('0.5')) * mp.pi + eps
    hi = mp.mpf(k) * mp.pi - eps
    return bisect(lambda z: mp.cos(z) + z * mp.sin(z), lo, hi)


def exterior_scaled_root(r):
    rr = mp.mpf(r)
    f = lambda z: rr * mp.cosh((1 - 1/rr) * z) - (rr - 1) * mp.cosh(z)
    z = bisect(f, mp.mpf('1e-30'), mp.mpf('3'))
    x = mp.cosh(z / rr)
    return z, rr**2 * (x - 1)


def interior_scaled_root(r, k):
    rr = mp.mpf(r)
    # The kth root from the upper endpoint lies between consecutive sign nodes
    # theta=(k-1)pi/(r-1) and theta=k*pi/(r-1).
    lo = (mp.mpf(k - 1) * mp.pi * rr / (rr - 1))
    hi = (mp.mpf(k) * mp.pi * rr / (rr - 1))
    eps = mp.mpf('1e-35')
    if lo == 0:
        lo += eps
    else:
        lo += eps
    hi -= eps
    f = lambda z: rr * mp.cos((1 - 1/rr) * z) - (rr - 1) * mp.cos(z)
    z = bisect(f, lo, hi)
    x = mp.cos(z / rr)
    return z, rr**2 * (1 - x)


def normalized_weight(r, x):
    rr = mp.mpf(r)
    return 1 / (2 * rr**2 * (rr - 1)**2 * (1 - x)**2)


def all_atoms_check(r):
    rr = mp.mpf(r)
    atoms = []
    # Interior roots, indexed from the upper endpoint downward.
    for k in range(1, r):
        z, _ = interior_scaled_root(r, k)
        x = mp.cos(z / rr)
        atoms.append((x, normalized_weight(r, x)))
    zext, _ = exterior_scaled_root(r)
    xext = mp.cosh(zext / rr)
    atoms.append((xext, normalized_weight(r, xext)))
    mass = mp.fsum(w for x, w in atoms)
    objective = mp.fsum(w * (1 - x) for x, w in atoms)
    return mass, objective


a = limiting_a()
print("limiting constants")
print("a solving a*tanh(a)=1             =", mp.nstr(a, 30))
print("a^2/2                              =", mp.nstr(a*a/2, 30))
print("exterior limiting mass 2/a^4       =", mp.nstr(2/a**4, 30))
print("interior limiting mass              =", mp.nstr(1-2/a**4, 30))
print("limiting scaled mean 1/2            =", mp.nstr(mp.mpf('0.5'), 30))
print()

print("first five limiting interior atoms")
for k in range(1, 6):
    z = limiting_z(k)
    print(k, "z_k=", mp.nstr(z, 24),
          "location=-z_k^2/2=", mp.nstr(-z*z/2, 24),
          "mass=2/z_k^4=", mp.nstr(2/z**4, 24))
print()

print("finite-r convergence")
print("r  r^2(x_out-1)        w_out              r^2(1-x_top)       w_top")
for r in [10, 20, 50, 100, 200, 500]:
    zext, dext = exterior_scaled_root(r)
    xext = mp.cosh(zext / mp.mpf(r))
    wext = normalized_weight(r, xext)
    z1, dint = interior_scaled_root(r, 1)
    x1 = mp.cos(z1 / mp.mpf(r))
    wint = normalized_weight(r, x1)
    print(f"{r:<3d}", mp.nstr(dext, 17), mp.nstr(wext, 17),
          mp.nstr(dint, 17), mp.nstr(wint, 17))
print()

print("full finite-atom checks")
for r in [10, 20, 50, 100]:
    mass, objective = all_atoms_check(r)
    exact_obj = -1 / (2 * mp.mpf(r) * (r - 1))
    print(f"r={r:3d} mass-1={mp.nstr(mass-1, 8)} "
          f"objective={mp.nstr(objective, 24)} "
          f"exact={mp.nstr(exact_obj, 24)} "
          f"difference={mp.nstr(objective-exact_obj, 8)}")

# Spectral sum identities for F(z)=cos(z)+z sin(z).
zs = [limiting_z(k) for k in range(1, 200)]
sum2 = mp.fsum(1/z**2 for z in zs)
sum4 = mp.fsum(1/z**4 for z in zs)
print()
print("spectral sum partial checks (199 positive roots)")
print("1/a^2 - sum 1/z_k^2       =", mp.nstr(1/a**2 - sum2, 20), "(limit 0.5)")
print("1/a^4 + sum 1/z_k^4       =", mp.nstr(1/a**4 + sum4, 20), "(limit 0.5)")
print("2/a^4 + sum 2/z_k^4       =", mp.nstr(2/a**4 + 2*sum4, 20), "(limit 1)")
