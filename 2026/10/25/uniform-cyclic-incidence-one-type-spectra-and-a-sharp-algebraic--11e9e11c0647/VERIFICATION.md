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

# Reproducibility
The companion Python 3 standard-library program `verify.py` independently enumerates ideals using included lower subsets, independently counts mixed bicliques using neighbor masks, and evaluates an \(r\times r\) transfer-matrix power by ordinary integer matrix multiplication. It checks 18 pairs \(1\le r\le6\), \(2r+1\le n\le2r+3\), and the bivariate polynomial at \((u,v)=(2,3)\). Recorded output is in `verification_output.txt`.

The infinite-parameter equalities and spectral asymptotics are proved in `RESULT.md`; finite enumeration is only corroboration. The all-width proof uses the cyclic-span uniqueness condition \(n\ge2r+1\) and the primitive matrix's Perron eigenvalue. No external or independent audit has taken place.
