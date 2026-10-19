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

# Verification

The analytic proof in `RESULT.md` is self-contained apart from standard finite character orthogonality and elementary finite-field facts. The included `verify.py` enumerates nonzero ordered differences and all Weyl ambiguity coefficients of the displayed example supports. Four dimensions and arbitrary nontrivial phases are checked to confirm the expected three-level modulus multiplicities and exact minimum. It additionally checks that nonflat weights cannot exceed the bound and explicitly reports squared full/trace-free condition numbers. A separate dense \(49\times49\) Hilbert–Schmidt matrix computation for dimension seven was performed separately: its singular values matched the theoretical formula.

**Scope of checks:** these finite computations are supporting tests, not an exhaustive verification for all \(k\), all groups, or all coefficient choices. The universal inequality, equality classification, and Singer infinite-family argument depend on the written exact proof. Priority comparisons are documented in `AUDIT.json`; full manuscripts of arXiv:2608.11850 and arXiv:2609.09614 were inaccessible, so abstract-level comparisons were used with an explicit residual risk. Independent audit has not been performed.
