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
# Verification of finite signatures and infinite propagation

Run `python3 verify.py` from the directory containing `verify.py`. The program enumerates every length-\(n\) factor of the period-doubling word for each integer \(1\le n\le10\) by a proved complete block-pair reduction. A second finite-prefix comparison checks these sets independently. For each factor it computes the complete vector of scattered-subsequence counts through order three, recovers the table of factor versus class counts, and identifies the only nonsingleton class. It also checks that the seed pair is distinguishable at order four and remains equivalent at order three through four substitution iterates.

The finite certificate depends on the combinatorial coverage lemma in `RESULT.md`: every length at most ten factor is contained in two consecutive length-sixteen images of an allowed binary pair. The actual infinite statement follows from an exact morphism-stability proof; finite computations do not establish universal morphism stability or infinitely many instances on their own. The 2021 doctoral thesis cited in the discussion was not inspected in full, and independent external verification has not occurred.
