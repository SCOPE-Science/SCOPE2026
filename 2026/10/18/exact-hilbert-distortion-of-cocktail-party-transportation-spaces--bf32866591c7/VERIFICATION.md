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

# Verification of exact distortion

The standalone standard-library file `check_exact.py` is sufficient to reproduce the finite exact checks using `python check_exact.py`. It enumerates all cut potentials and all non-cut special potentials, checks tight-graph connectivity, and computes the projections into the pair-signed and pair-constant orthogonal subspaces with exact rational arithmetic. The evaluation uses the analytic candidate weights \(2/3\) for \(k=2\), \(3/5\) for \(k=3\), and \(1/2\) for \(k\ge4\).

Observed output: the numbers of polar vertices for \(k=2,3,4,5,6,7,8\) were respectively \(6,56,246,1012,4082,16368,65518\), and the squared distortions at the prescribed candidate forms were \(3,10/3,4,5,6,7,8\). All assertions passed and the program printed `EXACT_COCKTAIL_DISTORTION_CHECKS_PASS: k=2..8`.

The code does **not** solve the infinite-dimensional parameter problem by brute force. The global optimality, symmetry reduction, and every \(k\ge9\) case rely on the proof in `RESULT.md`, including explicit lower-bound extremal points and monotonicity arguments. The sources and independent status are detailed in `REVIEW.md`.
