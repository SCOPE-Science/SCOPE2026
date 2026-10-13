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

The checker independently constructs each crown graph, computes all-pairs shortest-path distances by breadth-first search, and tests strong resolution using the defining distance equality. Domination is tested directly from graph neighborhoods; the theorem's structural criterion is implemented separately.

For every \(3\le n\le8\), all vertex subsets are checked. The program compares the exact accepted family with the theorem, then compares the complete cardinality distribution with
\[
z^n\bigl((z+2)^n-2n\bigr).
\]
It also checks the minimum value and the number of minimum sets.

Recorded output:

```text
VERIFY_OK
crown_parameters_checked = 6
parameters n = 3..8
subset_trials = 87360
accepted_strong_resolving_dominating_sets = 9762
minimum_bases_checked = 438
polynomial_coefficients_checked = 39
all strong resolving dominating sets matched the exact classification
all generating polynomials matched x^n((x+2)^n-2n)
all strong resolving domination numbers matched n
all minimum-basis counts matched 2^n-2n
```

Claim-to-evidence map: the hit-every-deleted-pair necessity and sufficiency are proved from the explicit distance table; the domination exception list is proved from the neighborhood of an omitted vertex; the polynomial is obtained only after the set classification. The finite computation is corroborative and does not prove the arbitrary-\(n\) statement.
