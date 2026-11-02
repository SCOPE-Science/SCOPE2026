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

# Reproducible checks and scientific limits

Execute `python3 verify.py` using Python's standard library. The program directly constructs binary circulant matrices, computes full update matrices, exact powers, bitwise Gaussian-elimination ranks, and the local-polynomial valuation via division by \(X+1\). It asserts each fixed-space dimension and smallest matrix order in the theorem for all 552 symmetric binary circulants at node counts \(4,8,16\), and for 128 deterministically seeded examples at 32 nodes (680 matrices altogether). It also independently enumerates every binary phase state at four nodes for all eight possible couplings, checking that every primitive period belongs to the derived list. Reported result: `PASS: symmetric_circulants_checked= 680 full_state_censuses_for_n4=8`.

All claimed universal rank and primitive-cycle formulas rely on the analytic local-ring proof in `RESULT.md`; the finite diagnostics do not test every matrix size. The proof does not cover odd node counts, phase alphabets other than two, or graph matrices that are not circulant. Independent audit is not performed.
