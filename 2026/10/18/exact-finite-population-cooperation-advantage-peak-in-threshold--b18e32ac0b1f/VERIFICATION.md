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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library. The executed file independently evaluates both focal strategies' hypergeometric payoff expectations, then tests equality with the coupled reduced formula; it independently verifies the exact adjacent-difference identity and integer-mode predictions for all nondegenerate integer triples in the tested finite range.

The executed run returned 43,605 exact direct-payoff comparisons and 13,566 exact increment identities without an assertion failure. It also verified the entire \((Z,N,M,F,c)=(10,5,3,6,1)\) sign sequence and its critical multipliers \(126/25\) and \(9\). These finite computations do **not** certify the theorem for unbounded integers; the proof's two sampling couplings, binomial coefficient identities, and support-boundary analysis establish universal correctness.

The work assumes uniform random co-player sampling without replacement, fixed group size, one common threshold, linear returns after threshold, and a constant cooperator cost. At equal payoffs, positive-probability transitions still occur under Fermi comparison; neutrality does not mean absorption. Independent audit and validation have not been performed.
