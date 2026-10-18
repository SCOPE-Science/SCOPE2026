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

# Reproducible checks

Run `python3 verify.py` from this directory. Only Python's standard library is needed. The program compares complete exact-rational motif-count distributions obtained by brute-force letter enumeration with those obtained from the independent-window factorial-moment expansion under nonidentical letter laws. It tests both singleton unbordered motifs and cross-bifix-free multiword codes; verifies full coefficient normalization and positivity; checks the stationary placement coefficients over a finite range; and tests the quadratic first-overlap threshold across bordered binary words and three strictly positive rational biases.

The exact finite checks do not certify the infinitely quantified theorem; its critical real-rootedness ingredient is the previously published claw-free graph-polynomial result. The proof of that general theorem was inspected in Bencs (2014), Theorem 1.8. The independent-Bernoulli representation is mathematical, not produced as an explicit parameter list by this checker.
