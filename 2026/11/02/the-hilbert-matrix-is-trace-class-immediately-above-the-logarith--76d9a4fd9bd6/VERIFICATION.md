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

# Verification of the trace-class threshold

The exact orthonormal coefficient matrix is specified in RESULT.md. The central analytic check is that the long-range lower-index geometric terms reduce to a weighted triangular matrix with dyadic-shell trace norm bounded by \(C 2^{h(1-\beta)}(1+h)\); its sum converges exactly for \(\beta>1\). The three remaining matrix regions have absolutely summable trace-norm rank-one expansions. The endpoint lower bound comes from explicit positive-coefficient polynomial probes whose inputs are weakly null.

Run `python3 checks/check_blocks.py` to verify finite exact rational geometric identities and the triangular block-recursion bound. The checker cannot prove the infinite operator ideal statements. Source comparison relies on the indicated primary open-access literature; historical implicit priority and independent verification remain open.
