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

Exact standalone `verify.py` was run from this package's source before serialization. It lists scalar-permutation orbits of nonzero quadruples summing to zero modulo each prime \(3\le p\le41\), and determines which of the three double transpositions lift with a common multiplier. Counts agree with the proved three-way partition for every tested prime. The output ends `VERIFY_OK orbit_census_and_liftable_Klein_four=all_tested_primes`. These checks are finite. The general theorem is justified by Kummer descent, the base Klein four stabilizer, group extensions, and exact inversion-orbit counting; the independent historical novelty question remains open.
