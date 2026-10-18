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

# Exact finite verification

Run `python3 verify.py` from the directory containing this document and the verifier. It needs only the Python standard library (Python 3.9 or later). The expected last line is `ALL_CHECKS_PASSED`.

The verifier constructs 60 alternating permutations, closes 59 subgroups (58 proper), and enumerates 1,018 distinct left cosets. It evaluates reduced Lefschetz traces for every group element using a fixed-coset-poset recursion, and independently reconstructs these traces from subgroup weights and the exact conjugacy-class intersection formula. Both computations yield character values \(1560,-84,-21,5,5\) on the five complex conjugacy classes. Explicit fixed-chain counts of simplex dimensions zero through three give \((1018,6867,8310,900)\), \((82,195,30,0)\), \((40,60,0,0)\), and \((18,12,0,0)\) at respective element orders one, two, three, five.

The final character arithmetic checks the multiplicities of all four rational irreducible types, including absence of the trivial representation, and accounts for the rational six-dimensional irreducible's character norm two.

The verifier does not independently prove the infinite-homotopy assertion \(X\simeq\bigvee^{1560}S^2\); that is a cited published theorem. Finite checks certify the exhaustive character calculation on this explicitly finite group, not analogous claims for any other group. Independent external validation has not been performed.
