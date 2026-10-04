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
The theorem is proved uniformly in `RESULT.md`. The accompanying `artifacts/verify.py` is a finite replay designed to catch normalization and counting mistakes.

It reconstructs \(\mathrm{PSL}_2(p)\) as \(\mathrm{SL}_2(p)/\{\pm I\}\) for \(p=5,7,11,13\), identifies projective involutions, and checks
\[
|X|=\frac{p(p+\chi)}2,\qquad
\deg_{\Delta}(t)=\frac{p-\chi}{2},\qquad
|E(\Delta)|=\frac{p(p^2-1)}8.
\]
It also checks an explicit induced \(6\)-cycle in the involution commuting graph for \(q=7\), and verifies the arithmetic density inequality for odd integers \(7\le q<1000\).

The replay is supplementary: it does not establish the prime-power theorem by enumeration. The proof uses the standard involution-centralizer structure of \(\mathrm{PSL}_2(q)\), the elementary structure of involutions in a dihedral group, and the perfect-elimination-ordering characterization of chordal graphs.

Run:
`python3 artifacts/verify.py`

Expected terminal line:
`VERIFY_OK`
