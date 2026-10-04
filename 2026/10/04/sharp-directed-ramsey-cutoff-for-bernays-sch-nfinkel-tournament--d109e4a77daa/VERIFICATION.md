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
The mathematical proof is self-contained in `RESULT.md`. The attached script `artifacts/verify_small.py` is a supplementary calibration check, not a substitute for the symbolic argument.

It performs four exact checks:

1. exhaustive enumeration of all \(2^6=64\) labeled tournaments on four vertices, confirming that every one contains a transitive triple;
2. verification that the directed three-cycle contains no transitive triple, hence \(R_{\to}(3)=4\);
3. arithmetic checks that \(N_T(k,3)=k+3\cdot2^k\) for \(0\le k\le8\);
4. construction of the \((k,\ell)=(1,3)\) sharp witness with one existential witness and two three-cycle profile classes, checking total order seven and absence of a transitive triple inside either class.

Expected output:

`VERIFY_OK directed_R3=4 tournaments_n4=64 endpoints_k0_8_ok sharp_k1_l3=7`

The general cloning argument and the extremal construction are symbolic and are reviewed directly in `RESULT.md` and `REVIEW.md`.
