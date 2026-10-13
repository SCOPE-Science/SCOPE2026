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

# Analytical and finite checks

The analytical proof in `RESULT.md` covers all \(n\ge2\), all positive neighboring birth/death rates, every \(h>0\), and \(\theta\ge1\). Its nonstandard steps are the resolvent identity \(P=\alpha I+\beta G\), the rank-one off-diagonal Green factorization, the exact adjacent minor \(-\alpha\beta G_{i,i+2}\), the strictly separated three-row sign ratios, and the TN factorization of the tridiagonal resolvent.

A standard-library Python checker (`verify.py`) constructs birth-death generators and inverses using exact `fractions.Fraction`, enumerates all ordered minors for the backward-Euler cases, and verifies stochasticity, strict positivity, mixed-minor identities, and constructed sign witnesses in 192 rational parameter cases. It checks an explicit three-state example separately. Reproduce with `python verify.py`; expected final line begins `VERIFY_OK: 192 exact-rational parameter cases`.

This is not a computer-assisted proof of the infinite theorem. The finite cases cannot establish universality, nor does this check certify absence from prior literature. There has been no independent audit.
