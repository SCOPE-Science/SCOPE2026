---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the diffusivity crossover

Using Python 3 and SymPy, run `python verify_crossover.py` from its directory. The checker enumerates all 30 binary step histories of lengths \(1,2,3,4\), factors each annealed path probability by independent sites, and checks their normalized sums, eight static moment identities, four speed coefficients, four diffusivity coefficients and the leading near-centered crossover coefficient. Its verified output is `PASS: 17 exact symbolic identities, 30 enumerated directed histories` with diffusivity coefficients `['1 - d**2', '0', '12*d**2*v', '-8*v**2']`.

The symbolic checker is deliberately finite; universal applicability relies on the path-factorization lemma and on the separately proved analytic remainder. For \(|r|\le1/2\), the regenerative speed is bounded by \(9\) and diffusivity by \(2700\), giving the fourth-order tail \(86400r^4\) by Cauchy estimates. These inequalities suffice to establish strict crossover signs outside the stated margin.

The result concerns annealed nearest-neighbor walks in globally refreshed independent site environments. It does not certify an unsolved critical-line sign, behavior at small \(p\), or independent audit.
