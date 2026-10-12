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

`verify_f3_m3_jordan_words.py` performs a complete finite verification over \(\mathbb F_3\). It enumerates all \(3^9=19\,683\) matrices, checks ordinary idempotence \(E^2=E\), and finds \(236\) idempotents. It then treats left-nested idempotent words as paths in the exact transition graph \(X\mapsto X\circ E\), expanding every current minimum-depth state by every idempotent \(E\).

The replay output is:

`VERIFY_OK`

`total=19683 idempotents=236 representable=19682 nonrepresentable=[13286]`

`minimal_length_counts=1:236,2:3068,3:12953,4:3308,5:117`

`width=5 length5=117 trace2_nonscalar_involutions=117`

The integer identifier `13286` is only the verifier's base-three encoding of \(-I_3\). The verifier additionally checks exact set equality between the length-five stratum and the nonscalar matrices satisfying \(A^2=I_3\) and \(\operatorname{tr}A=2\).

The computation is exhaustive rather than sampled. Its finite scope does not imply any analogous width statement for other fields or other matrix sizes. The similarity classification of the extremal stratum is established separately from the computation using square-freeness of \(t^2-1\) over \(\mathbb F_3\).
