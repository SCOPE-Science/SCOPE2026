"""Supplementary numerical diagnostics of the explicit two-moment Fourier aperture rule.

Requires mpmath; run `python verify.py`. Finite tests corroborate but do not
establish the theorem for all cyclic orders. The analytic proof is in RESULT.md.
"""
from mpmath import mp

mp.dps = 80
TOL = mp.mpf('1e-49')


def aperture_rule(N):
    assert isinstance(N, int) and N >= 3
    D = (2*N + 2)//3
    if N % 3 == 0:
        return D, {0: mp.mpf(1)/3, N//3: mp.mpf(1)/3, 2*N//3: mp.mpf(1)/3}
    if N == 4:
        return D, {j: mp.mpf(1)/4 for j in range(4)}
    R = mp.pi*D/N
    u0 = mp.cos(R)
    star_cos = -mp.mpf('0.5')/u0
    star_r = mp.acos(star_cos)
    parity = D % 2
    radii = [(q, mp.pi*q/N) for q in range(parity, D, 2)]
    assert radii[0][1] <= star_r + TOL
    assert radii[-1][1] >= star_r - TOL
    hi = next(j for j, (q, radius) in enumerate(radii)
              if radius >= star_r-TOL)
    lo = hi-1 if hi > 0 else hi
    if lo == hi:
        q = radii[lo][0]
        assert abs(mp.cos(mp.pi*q/N) - star_cos) < TOL
        u = star_cos
        weights = [(D, u/(u-u0)), (q, -u0/(u-u0))]
    else:
        q1, q2 = radii[hi][0], radii[lo][0]
        uu = [u0, mp.cos(mp.pi*q1/N), mp.cos(mp.pi*q2/N)]
        ww = [(mp.mpf('0.5')+uu[(j+1)%3]*uu[(j+2)%3])/
              ((uu[j]-uu[(j+1)%3])*(uu[j]-uu[(j+2)%3]))
              for j in range(3)]
        weights = list(zip([D, q1, q2], ww))
    out = {}
    for q, weight in weights:
        assert weight > -TOL
        weight = max(mp.mpf(0), weight)
        if q == 0:
            j = D//2
            out[j] = out.get(j, mp.mpf(0)) + weight
        else:
            for j in ((D-q)//2, (D+q)//2):
                out[j] = out.get(j, mp.mpf(0)) + weight/2
    return D, {j:w for j,w in out.items() if w > TOL}


def test():
    checks=0
    for N in range(3,401):
        D, weights = aperture_rule(N)
        assert D == (2*N+2)//3
        assert weights and len(weights) <= 6
        assert min(weights) == 0 and max(weights) == D
        assert min(weights.values())>0
        assert abs(sum(weights.values())-1) < TOL
        for k in (1,2):
            moment = sum(w*mp.exp(2j*mp.pi*k*j/N) for j,w in weights.items())
            assert abs(moment) < TOL, (N,k,mp.nstr(moment,15))
            checks+=1
        if N % 3 == 0:
            assert len(weights) == 3
            assert all(abs(w-mp.mpf(1)/3)<TOL for w in weights.values())
        # Evaluate the strict dual certificate for all subthreshold integer arcs.
        for d in range(D):
            q = mp.cos(mp.pi*d/N)
            assert q > -mp.mpf('0.5') + TOL, (N,d)
    print(f'VERIFY_OK {checks} high-precision moment-zero comparisons, N=3..400; '
          'strict dual-aperture checks and endpoint checks')


if __name__ == '__main__':
    test()
