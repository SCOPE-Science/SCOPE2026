---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For radial squared coordinate Z=X² with CIR generator 2(α+D−βz)fprime+4Dz fdoubleprime and rate-r resetting to z0=x0², regenerative exponential-age stationarity and generator balances for z,z² yield E Z=(2(α+D)+r z0)/(2β+r), E Z²=(4(α+3D)E Z+r z0²)/(4β+r). With m=(α+D)/β, η=2D/(α+D)∈(0,2), w=z0/m>0, q=r/(2β), the exact normalized variance is F=2η(1+wq)/[(q+1)(q+2)]+(w−1)²q/[(q+1)²(q+2)]. Independent exact symbolic differentiation gives Fprime=2(A−Bq−Cq²−ηwq³)/[(q+1)³(q+2)²], A=(w−1)²+η(2w−3), B=(w−1)²+η(5−2w)>0, C=(w−1)²+η(w+2)>0. Thus A<=0 strictly decreasing for q>0, while A>0 gives one global maximum at unique positive polynomial root. A=(w−w−)(w−w+) with w±=1−η ±sqrt(η(1+η)); w−>0 iff η<1/3 iff α>5D. The two overshoot wings are w>w+ and w<w− when permitted. Implicit-function near each positive critical w_c gives q*=A/B_c+O(A²), gain=A²/(4B_c)+O(A³), B_c>0. Exact CIR moment recursion applies even near α<D when reflecting/canonical nonabsorbing radial boundary specified; no empirical extrapolation.

## originality

PASS

Best-of-knowledge originality assessment of this EXACT final statement against published mathematical results and the source model, not certification of historical priority. General mathematical machinery and prior model definitions are attributed; claim-specific evaluated classification is not found among inspected primaries. A failed search is not novelty proof. Gültekin paper studies same drift potential but reported special-function stationary-density shapes, whereas this theorem studies Var(X²) and reset-rate derivative. Even knowing CIR moments and renewal formula does not directly state positivity of A, B, C or the sharp α>5D lower-wing condition. The result adds a evaluated phase diagram, not a new stationary renewal identity.

## value

PASS

Stationary harmonic energy fluctuations under resetting are physically natural, and the two distinct reset-position windows and sharp strength boundary α>5D give a non-obvious complete phase diagram for variance OVERSHOOT rather than minimizing variance, with unique maximizer and critical onset. Unlike an arbitrary algebraic slice, the invariant has direct interpretation as energy-noise response of the original resetting diffusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
