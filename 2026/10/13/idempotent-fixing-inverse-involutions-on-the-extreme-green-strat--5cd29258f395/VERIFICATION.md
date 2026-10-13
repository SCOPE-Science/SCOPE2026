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
# Verification of the explicit matchings

Run `python3 verify.py`. The script constructs every order-preserving transformation of rank two and rank \(n-1\) for each \(3\le n\le12\) using complete image tuples. For every such map it constructs its proposed mate and tests involutivity, both full transformation-composition inverse identities, and the equivalence between being a fixed point and being idempotent. It counts distinct two-element orbits and compares them with the symbolic binomial formulas. The final output includes `EXHAUSTIVE_INVERSE_IDENTITIES_AND_FIXED_POINT_COUNTS_OK` and `VERIFY_OK`.

The all-\(n\) assertion relies on the symbolic proof in `RESULT.md`; testing a finite range does not imply the unbounded statement. The enumerator does not check earlier literature or establish priority. No independent audit has been performed.
