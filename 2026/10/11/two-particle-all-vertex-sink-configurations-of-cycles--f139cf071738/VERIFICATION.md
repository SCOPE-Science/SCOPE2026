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

The proof has two independent layers. First, the published sink-configuration deformation model identifies the relevant finite cubical complex. A geometric deformation then identifies that complex with a genus-one surface having \(m\) boundary components, proving the all-parameter homotopy type. Second, `artifacts/verify.py` reconstructs the cellular boundary matrices directly for \(3\le m\le12\), checks \(\partial_1\partial_2=0\), and computes ranks modulo \(2,3,5,7\).

The verifier records cells \((m^2,2m^2,m(m-1))\), boundary ranks \((m^2-1,m(m-1))\), Betti vector \((1,m+1,0)\), chain trace \((m,0,0)\), first-homology trace \(1-m\), and transposition eigenspace dimensions \((1,m)\). Each modular rank attains a dimension-theoretic maximum, so the corresponding rational ranks are forced as well.

The finite replay is a consistency check only. It does not certify the statement for untested \(m\); arbitrary \(m\) is covered by the surface deformation and Lefschetz argument.
