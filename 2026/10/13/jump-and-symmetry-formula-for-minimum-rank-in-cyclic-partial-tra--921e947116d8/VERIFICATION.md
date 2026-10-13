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

# Verification of the minimum-rank formula

Run `python3 verify.py` using Python 3.9 or later. No third-party dependencies are required.

The verifier independently explores the powerset transition graph from the full set for every \(n=2,\ldots,10\), every jump \(1\le h<n\), and every active-set bitmask. It compares the resulting exact reachable minimum ranks against \(|H(A)|\gcd(n/|H(A)|,h)\). It then computes inverse-interval expansion witnesses, verifies the preimage equality at each step, and checks the resulting transformation rank on the original state set for all \(n\le12\) and sampled larger sizes.

A completed run returned:

```
VERIFY_OK exhaustive_subset_bfs_cases=16388 constructive_witness_cases=83324 certified_inverse_expansions=769634
```

The search and witness tests are **finite**. They verify boundary handling and executable transformations but do not prove the all-size statement. The symbolic quotient, residue-class lower bound, and aperiodic inverse-extension argument in `RESULT.md` provide the infinite proof. The script does not certify shortest lengths of minimum-rank words.
