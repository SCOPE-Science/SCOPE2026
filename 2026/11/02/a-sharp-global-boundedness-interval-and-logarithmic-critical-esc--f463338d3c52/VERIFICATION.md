---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a>0 and all real b, with f_a(t)=a t(1-t²)e^-t² and F(x,y)=(f_a(x)+b(y-x),f_a(y)+b(x-y)), mean/difference coordinates s=(x+y)/2,d=(x-y)/2 give |s_{n+1}|<=M_a, d_{n+1}=g(s_n,d_n)-2b d_n with |g|<=M_a and g=(f_a(d+s)+f_a(d-s))/2. When |2b|<1 bounded forcing gives common invariant attracting rectangle; for b=-1/2, outside R=M_a+1 the feedback g opposes d and strictly decreases its modulus, and compactness prevents convergence to a nonentering positive threshold, giving eventual absorption. When |2b|>1, outer |d|>M_a/(|2b|-1) diverges geometrically on open set. When b=+1/2, outer d alternates sign while |d| strictly increases to infinity on an open region; every unbounded orbit enters it. There the mean coordinate decays geometrically because f_a’(t)→0; since |d_n|=O(n), d_n s_n→0, giving u_{n+1}-u_n ~a u_n(u_n²-1)e^-u_n² with u=|d|. For r_n=u_n², r_{n+1}-r_n~2a r_n(r_n-1)e^-r_n, and H(r)=e^r/(2a r²) obeys H(r_{n+1})-H(r_n)→1. Hence r_n=log n+2log log n+log(2a)+o(1) for *every* unbounded positive-endpoint orbit. Independent coordinate-step and finite critical ratio calculations corroborated but cannot prove the slow asymptotic. Boundary b=-1/2 included, b=+1/2 excluded.

## originality

PASS

Soula–Jahanshahi–Al-Barakati–Moroz (2023) introduce this exact coupled Gaussian-cubic map and examine local/global bifurcation diagrams, synchronization and numerical basins. The inspected accessible main text does not derive a common compact absorbing set for all initial conditions over a complete coupling interval or the universal b=+1/2 logarithmic escape law. Bounded-forcing comparison yields strict interior/exterior routinely, but asymmetric marginal endpoints and sharp expansion demand further sign/adiabatic analysis.

## value

PASS

Provides a global, all-initial-condition threshold complementing local bifurcation studies, with mathematically unusual asymmetric inclusion of b=-1/2 and a universal two-log correction at b=+1/2. The endpoint results, not merely the elementary |b|<1/2 contraction, give substantive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
