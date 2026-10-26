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

# Verification and scope

The program `check.py` uses only the Python 3 standard library and can be run as `python check.py`. It builds the weighted complete graph explicitly, grounds the final vertex, forms the reduced Laplacian, computes the exact rational inverse by Gauss–Jordan elimination, reconstructs every column of the cut projector from the weighted incidence matrix, and checks the cycle complement column independently.

Successful execution produced:

`MATCHING_WEIGHTED_COMPLETE_EXACT_OK graphs=32 full_columns=1840 boundary_graphs=12`

Four even graph orders \(N=8,10,12,14\) were used. For each graph order, eight positive rational values of \(x\) were tested, including \(x=1\), both exact rational phase thresholds, and points on both sides of each threshold. Every one of the 1,840 columns was compared with the appropriate symbolic orbit formula using exact rational values, not floating-point tolerances. Grounded-inverse identities and projection diagonal entries were also checked.

The unrestricted proof does not rely on experimental extrapolation: the spectral splitting, voltage descriptions, sign enumeration, orbit comparisons, and global extremum bounds are established algebraically in `RESULT.md`. No formal proof assistant or independent external mathematical validation was used.
