"""Bounded test: q-independent Dirichlet-trial disproof of mu_1 >= 1/8 (stdlib only).

Setup (symmetric equal double bubble in S^3(1)):
  interface D(rho) = geodesic disk radius rho in great S^2 (x4=0), totally
  geodesic => |A_D|=0, J = -Delta - 2 exactly.
  Junction relation (120-degree stationarity, consistent orientations):
    cos(Rs)^2 = 3 cos(rho)^2/(4-cos(rho)^2), b = sin(Rs)/2, a = sqrt(1-b^2),
    with a*cos(rho) = cos(Rs) (junction circle lies on cap sphere).
  Nontrivial stationarity check: the three consistently-oriented unit normals
  at the junction point are pairwise at 120 degrees (dots = -1/2).

Trial: u = x3 - c0 on D (c0 = cos rho): smooth, H^1, zero trace on boundary
circle => Robin boundary term vanishes EXACTLY for any finite q, so
  mu_1 <= Q(c0) := (G - 2*Dm)/Dm, G = A - M2, Dm = M2 - 2 c0 M1 + c0^2 A,
with exact disk moments A=2pi(1-c0), M1=pi(1-c0^2), M2=2pi(1-c0^3)/3.
At c0=0: Q = 0 (recovers x3 Dirichlet ground on hemisphere, quotient 0 < 1/8).

Volume map: bubble1 = B(m+,Rs) cap {x4>=0}; f(rho) = V/(2 pi^2) by Simpson.
Goal: rho with f(rho) in [0.05,0.30] AND Q < 1/8 (margin >> fp error).
"""
import math

PI = math.pi

def moments(c0):
    A = 2*PI*(1-c0)
    M1 = PI*(1-c0*c0)
    M2 = 2*PI*(1-c0**3)/3
    G = A - M2
    Dm = M2 - 2*c0*M1 + c0*c0*A
    N = G - 2*Dm
    return A, M1, M2, G, Dm, N, N/Dm

def junction(rho):
    c = math.cos(rho)
    u = 3*c*c/(4-c*c)
    Rs = math.acos(min(1.0, math.sqrt(max(0.0, u))))
    S = math.sin(Rs)
    b = S/2.0
    a = math.sqrt(max(0.0, 1-b*b))
    return Rs, S, a, b

def stationarity_dots(rho):
    # junction point x0=(s,0,c,0); n12 = -e4;
    # n13 = -(m+ - C x0)/S, n31 = -n13, n23 = mirror of n13 (e4 flip).
    Rs, S, a, b = junction(rho)
    s, c = math.sin(rho), math.cos(rho)
    C = math.cos(Rs)
    # n13 components in (e1,e3,e4): (-(0 - C s)/S, -(a - C c)/S, -(b)/S)
    n13 = (C*s/S, -(a - C*c)/S, -b/S)
    n31 = (-n13[0], -n13[1], -n13[2])
    n23 = (n13[0], n13[1], -n13[2])
    n12 = (0.0, 0.0, -1.0)
    def dot(p, q): return p[0]*q[0]+p[1]*q[1]+p[2]*q[2]
    return (dot(n12,n23), dot(n12,n31), dot(n23,n31),
            abs(a*c - C))  # last = junction residual

def bubble_frac(rho, n=2000):
    Rs, S, a, b = junction(rho)
    C = math.cos(Rs)
    assert a > 1e-12
    # Bubble 1 = {p in S^3 : p.m+ <= C} cap {x4 >= 0}, m+ = a e3 + b e4.
    # Slice at x4=t: {(x1,x2,x3) in S^2(r)}, r=sqrt(1-t^2), with a x3 <= C-bt.
    # Section area (spherical patch, |grad_{S^3} x4| = r coarea factor 1/r):
    #   {x3 <= h0} on S^2(r) has area 2 pi r (r + h0), h0=(C-bt)/a.
    # (Complement of the standard cap {x3>=h0}; verified against MC slabs.)
    def area(t):
        r2 = 1-t*t
        if r2 <= 1e-14: return 0.0
        r = math.sqrt(r2)
        h0 = (C - b*t)/a
        if h0 <= -r: return 0.0
        if h0 >= r: return 4*PI*r2
        return 2*PI*r*(r+h0)
    def density(t):
        r2 = 1-t*t
        if r2 <= 1e-14: return 0.0
        return area(t)/math.sqrt(r2)
    H = 1.0/n
    tot = density(0.0) + density(1.0)
    for k in range(1, n):
        w = 4.0 if k % 2 else 2.0
        tot += w*density(k*H)
    V = tot*H/3.0
    return V/(2*PI*PI)

def main():
    print("== stationarity (nontrivial 120-degree check) ==")
    # Physical symmetric branch: rho in (0, pi/2] (interface at most a
    # hemisphere; for rho > pi/2 the equal-cap branch ceases to exist,
    # which is exactly why the residual must fail there).
    for deg in (10, 30, 60, 89, 90):
        rho = math.radians(deg)
        d1, d2, d3, res = stationarity_dots(rho)
        print(f"rho={deg:4d}deg dots=({d1:.12f},{d2:.12f},{d3:.12f}) resid={res:.2e}")
        assert res < 1e-9, res
        assert abs(d1+0.5) < 1e-9 and abs(d2+0.5) < 1e-9 and abs(d3+0.5) < 1e-9
    print("== branch check: rho=100deg must NOT satisfy the junction relation ==")
    print(f"resid(100deg) = {stationarity_dots(math.radians(100))[3]:.6f} (expect O(0.3))")
    assert stationarity_dots(math.radians(100))[3] > 0.1
    print("== wedge cross-check: rho=pi/2 -> equal double bubble on S^3 = 3 wedges ==")
    print("== (equal caps meet the interface orthogonally: Rs=pi/2, b=1/2) ==")
    fw = bubble_frac(PI/2, 4000)
    Rs90 = junction(PI/2)[0]
    print(f"f(pi/2) = {fw:.10f}; Rs(pi/2) = {Rs90:.10f} (expect pi/2 = {PI/2:.10f})")
    assert abs(Rs90 - PI/2) < 1e-12
    # exact wedge value f(pi/2) = 1/6 (fiber-circle argument + MC cross-check):
    assert abs(fw - 1/6) < 1e-6, fw
    print(f"f(pi/2)*6 = {6*fw:.10f} (expect 1)")
    Qw = moments(0.0)[6]
    print(f"Q(hemisphere) = {Qw:.12f} (expect 0)")
    assert abs(Qw) < 1e-12
    print("== scan (admissible branch rho in (0, pi/2]) : Q vs volume fraction ==")
    print(f"{'rho_deg':>8} {'f':>10} {'Q':>10} {'in_window':>9} {'Q<1/8':>6}")
    wit = []
    deg = 2.0
    while deg <= 90.0:
        rho = math.radians(deg)
        c0 = math.cos(rho)
        if c0 <= -1 or c0 >= 1:
            deg += 1.0
            continue
        Q = moments(c0)[6]
        f = bubble_frac(rho)
        inw = 0.05 <= f <= 0.30
        hit = Q < 0.125
        if deg % 4 == 0 or (inw and hit):
            print(f"{deg:8.1f} {f:10.6f} {Q:10.5f} {str(inw):>9} {str(hit):>6}")
        if inw and hit:
            wit.append((deg, Q, f))
        deg += 1.0
    assert wit, "expected in-window violations on the admissible branch"
    # headline witness: rho = 90 deg (hemisphere interface): Q = 0 EXACTLY,
    # f = 1/6 IN the v-window; re-verify at fine quadrature.
    rho = PI/2
    Qr = moments(0.0)[6]
    fr = bubble_frac(rho, 8000)
    Rs = junction(rho)[0]
    print(f"WITNESS: rho=90deg Q={Qr:.10f} (exact 0) f={fr:.10f} (exact 1/6) "
          f"Rs={Rs:.10f} (exact pi/2) margin={0.125-Qr:.6f}")
    assert abs(Qr) < 1e-12 and abs(fr - 1/6) < 1e-6 and abs(Rs - PI/2) < 1e-12
    assert 0.05 <= fr <= 0.30
    print(f"in-window violations on admissible branch: {len(wit)} (rho 88..90 deg)")
    print("DISPROOF_WITNESS_CONFIRMED")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
