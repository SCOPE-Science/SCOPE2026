---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Mellin transform diagonalizes Carleman as pi sech(pi xi); Gamma reflection yields spectral weight sech(pi xi) for the precisely normalized g. Independent normalization integral of weight is one. The rank-one eigen-equation reduces outside [0,pi] to 1=gamma F(z), with F(z)=(1/pi) integral dtheta/(z-pi cos theta), and F′(z)<0 on both components. F diverges with opposite signs at respective edges, granting one eigenvalue simple on gamma-selected side. Since Mellin g is nowhere zero and the multiplier has simple interior zeros and quadratic maximum at xi=0, (m-lambda)^-1 g is not L2 at any interior/edge lambda; no point eigenvalues there. Expand z=pi+delta: F=sqrt(2/pi)delta^-1/2-2/pi^2+O(sqrt(delta)), yielding delta=(2/pi)gamma^2+O(gamma^3). At z=-a: -F=(2/pi^2)log(2pi/a)+O(a^2 log(1/a)), yielding exponentially small a=2pi exp(-pi^2/(2|gamma|))(1+o(1)). Direct quadrature checked exterior expressions and two landmarks, with strong-coupling moment <g,Cg>=2. Actual check_carleman.py was read for independence of tested numerical assertions; quadrature is corroboration, not the proof.

## originality

PASS

Best-of-knowledge after two real Resultary searches, public-primary reading and comparison of mathematical implications, not merely titles. Known qualitative existence/counters are openly excluded from novelty. Even if Yafaev Theorem 1.3 gives the number of negative bound states for gamma<0, it cannot imply energy -2pi exp(-pi^2/(2|gamma|)) without additional spectral density calculation.

## value

PASS

The two opposite edges of one canonical continuous-spectrum operator produce qualitatively different sharp weak-coupling universality classes with nontrivial prefactors. This supplies an explicit spectral threshold benchmark and exact negative-binding law absent from the broad qualitative eigenvalue-count statements; mathematically motivated and not just reformatting the counting theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
