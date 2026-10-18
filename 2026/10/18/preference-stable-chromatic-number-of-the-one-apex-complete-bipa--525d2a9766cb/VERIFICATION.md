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

# Verification and reproducibility

The proof is self-contained in `RESULT.md`. To reproduce the finite checks, run `python3 artifacts/verify.py` with Python 3 and no third-party packages. The code enumerates all proper colorings under the explicit adversarial preferences for the parameter pairs \((2,2),(3,2),(4,2),(3,3),(4,3),(5,3)\), constructs their envy digraphs, and checks that none are acyclic. It also constructs the upper-bound coloring for 700 deterministic pseudorandom strict preference profiles on seven small parameter pairs, checks properness, and checks absence of directed envy cycles. Separate direct full-map brute force was performed for \((2,2),(3,2),(3,3)\) and agreed with the structured enumerator.

Expected output includes `ALL_FINITE_CHECKS_PASS` and `GREEDY_UPPER_CHECKS_PASS; profiles=700`. Random test instances and exhaustive small instances do not establish an infinite theorem; the universally quantified proof uses the finite-map cycle argument and the greedy ordering. The paper-access limitation and residual originality risk are documented in `RESULT.md` and `REVIEW.md`. Independent external scientific validation has not been performed.
