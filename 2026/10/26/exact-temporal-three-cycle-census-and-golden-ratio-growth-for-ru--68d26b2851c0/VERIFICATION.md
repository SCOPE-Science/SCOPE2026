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

# Reproducibility

Run `python verify_rule62.py` with Python 3 and SymPy installed. The program generates the entire 64-state transfer matrix and the 4-state one-step transfer directly from the explicit Wolfram-code-62 rule; checks two characteristic-polynomial factorizations symbolically; applies eight exact-rational Schur reduction stages to the octic rescaled by the radius \(3/2\); and independently enumerates all binary cyclic configurations of lengths one through twelve. The polynomial identities and strict rational Schur inequalities supply finite exact certificates needed in the universal trace proof; the enumeration is only a cross-check. No external infinite-domain proof assistant or independent audit was used.

# Scope and limits

The count holds for every positive integer length by cyclic transfer-walk correspondence. The spectral radius certificate bounds subleading octic contributions but does not claim an optimal decay exponent. Direct finite orbit checks do not establish the all-length statement by themselves. Historical-priority limitations are stated in `RESULT.md` and `REVIEW.md`.
