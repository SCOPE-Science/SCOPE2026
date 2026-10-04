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
The bundled checker first scans a box containing the complete canonical triangle for every \(2\le r\le30\). It recomputes canonicity and terminality directly from every nonidentity Reid--Tai group element in both heavy charts, then checks the predicted age-one index lists on every canonical non-terminal pair. It independently verifies the histogram
\[
\{1:2r-2,\ 2:r,\ 3:1,\ 5:1\}
\]
and the total \(4r+6\).

A second boundary-only replay checks the explicit junior-index formulas directly through \(r=300\). This is a finite regression test only; the all-dimensional proof is in `RESULT.md`.

Expected terminal output: `VERIFY_OK`.
