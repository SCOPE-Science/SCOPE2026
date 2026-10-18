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

The general proof is a characterisation of integral transportation tables on a complete bipartite support with pairwise disjoint missing edges, followed by an exact convolution and Hilbert numerator comparison. Reproduce ancillary finite checks by running `python3 verification/check_matching_segre.py`. The checker constructs degree-by-degree sets of exponent sums of all permitted individual edges; it does **not** use the Hall-inequality formula as its enumeration algorithm. It matched the claimed formula on 139 parameters/degree instances, ranging from dimensions 3×3 through 6×6 and degree 0 through 5. These are finite checks, not an exhaustive proof for all dimensions or degrees. No independent external audit has been performed.
