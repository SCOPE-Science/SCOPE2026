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

The standalone `verify.py` requires only the Python 3 standard library. Execute `python3 verify.py` in the extracted artifact directory. The script exhaustively iterates all increasing parent arrays for every integer \(3\le n\le9\) and checks leaf moments, the tail event, conditional leaf expectations, strict covariance, and the exact sum formula using rational arithmetic. It checks the limiting covariance constant numerically for three larger sizes. The recorded execution completed with `PASS 178 exact/numerical assertions`.

The infinite proof is analytical: the tail formula is an exact independent-parent product, the leaf recursion is Eulerian, the joint limit follows by an early/late parent-choice decomposition and bounded martingale increments, and the covariance limit follows from a Gaussian tail bound and dominated Riemann sums. The verifier does not prove an infinite limit or certify historical originality. Janson's source is dated by first online publication, not its later journal issue.
