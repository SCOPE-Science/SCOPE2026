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

# Exact computational verification

The included standalone Python program constructs every nondecreasing positive-integer partition for each census of size 1 through 16 and every distinct unordered two-taxon merger. The exact indicator-covariance calculation and an independent integer generating-function computation of the full richness distribution agree on the expectations and variances of every original and merged profile. No stochastic simulation, floating-point root test or unproved infinite extrapolation is used.

Execute `python verify_taxon_merger_three_reversals.py taxon_merger_census_recreated.csv` and compare the output CSV byte-for-byte to the supplied `taxon_merger_census.csv`. Expected number of rows excluding header: 3380; exactly one row has three strict adjacent reversals, with census 16, original abundances eight ones plus 2 and 6, and merged abundances seven ones plus 3 and 6.

Limitations: the finite enumeration proves no classification beyond 16; the program requires Python 3.9+ standard library. Source originality was checked against inspected accessible primary work and research records but not independently audited; the 1975 primary text was available in abstract only.
