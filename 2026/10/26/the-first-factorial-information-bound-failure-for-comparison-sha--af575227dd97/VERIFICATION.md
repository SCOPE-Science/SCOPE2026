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

# Verification of the finite comparison-shattering profile

The following commands run the two separately implemented exact checks with Python 3 and no third-party modules:

```sh
python verify_bitsets.py comparison_certificates.json
python verify_posets.py
```

The first program enumerates all \(n!\) lexicographically ordered permutations for each \(1\le n\le7\), builds the exact query-membership bitsets, and uses the complete recursive split criterion. It verifies every stored positive shattered-tree certificate, including \(2048\) leaf witnesses at seven labels. To rule out a twelve-round shattered tree it checks both possible response branches for each of all \(21\) root comparisons.

The second program instead represents every transcript by a transitively closed finite partial order. At each step it exhausts all incomparable pairs and computes the exact number of its linear extensions by a separate vertex-subset recurrence. This independently establishes the seven-label upper bound; the result is not a sampling or random search. It also reproduces the positive lower bounds for all seven sizes.

The supplied execution record is `verification_output.txt`. Its concluding indicators are `BITSET_ALL_CHECKS_PASS` and `POSET_ALL_CHECKS_PASS`. Input data and all generated certificates are present in this package. The seven-label upper bound depends on this complete finite computation and has not been replaced by a shorter calculation-free argument. No independent external audit is claimed.
