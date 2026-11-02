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

# Finite reproducibility checks

Compile `verify.cpp` with `c++ -std=c++17 -O3 verify.cpp -o verify` and run `./verify`. The program independently enumerates all 0/1/2 singleton assignments at weights \(2n-3\) and \(2n-2\) for \(2\le n\le5\), evaluates row and column neighbourhood constraints, identifies the four sets of missing-colour rows/columns, compares each optimal configuration to the two-bar/disjoint-matching theorem, and checks exact enumerations for every interior size.

Observed minimum placement counts: \(M_2=4\), \(M_3=18\), \(M_4=320\), \(M_5=8450\). The exhaustive scanner reports `EXHAUSTIVE_OPTIMA_OK` for each of four orders and finishes with `CLASSIFICATION_AND_DERANGEMENT_CENSUS_OK n=2..5` and `VERIFY_OK`.

The verification enumerates finite cases only. Its execution does not establish the infinite classification, which follows from the written proof; no independent mathematical audit is claimed.
