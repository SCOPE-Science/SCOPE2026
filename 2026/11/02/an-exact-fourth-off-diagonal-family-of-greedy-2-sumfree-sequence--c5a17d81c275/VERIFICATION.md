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

Run `python3 verify.py` using only the Python standard library.

The script constructs all candidate intervals through the integer cutoff \(15(5f+7)\), translates each pair of disjoint integer intervals into its exact interval of sums, and uses the correct distinct-element diagonal rule. There are 57 candidate intervals and 1640 generating intervals for sums. Their 3396 affine endpoints, with adjacency offsets, have no slope-crossing at parameter \(f>14\). Exact coverage and disjointness are therefore stable for every \(f\ge15\); all cases \(8\le f\le15\) are checked directly with integer interval arithmetic. The script also independently computes greedy prefixes for \(8\le f\le40\). These checks are finite in the *number of symbolic cases* but, coupled with the explicit affine-crossing lemma in `RESULT.md`, certify the interval assertions for all integer \(f\ge8\). They do not purport to prove the separately cited four-block continuation theorem, nor to establish priority or external audit.

The theorem's remaining steps are analytical: the candidate is periodic modulo \(5f+7\) after \(3(5f+7)\), so the published four-block continuation theorem extends the checked greedy prefix indefinitely, and the three unequal non-unit cyclic gaps establish minimality of the period. The boundary-gap mismatch fixes the minimal preperiod. All assumptions and unproved external dependencies are stated in `RESULT.md`.
