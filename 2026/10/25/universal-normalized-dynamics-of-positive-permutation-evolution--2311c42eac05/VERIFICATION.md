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

# Computational verification

Run `python3 verify.py` using Python 3 standard library. The program directly enumerates all \(873\) permutations with \(1\le n\le6\), and for each permutation all nonempty coordinate subsets, then constructs their support-rotation orbits and independently compares fixed-support counts \(2^{c(\pi^r)}-1\) for all relevant divisors of the permutation order. It also tests the unique positive gauge relation, the conjugacy identity for sampled weights and interior states, direct versus exact iterate formulas through five updates, and a tied-maxima example. The observed result when executed from the package was `VERIFY_OK permutations 873 exact_period_counts_all_subsets_checked_n_le_6 weighted_conjugacy_and_iterates_checked`.

The script checks a bounded family of small permutations, sample weights and states, and does not enumerate a continuum. The unrestricted-dimensional assertion, superexponential convergence, and stability statement are justified by the mathematical arguments in `RESULT.md`, not by these tests.
