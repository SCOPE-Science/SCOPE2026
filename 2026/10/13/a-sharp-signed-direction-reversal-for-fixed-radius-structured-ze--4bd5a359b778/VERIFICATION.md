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

The proof is exact for every finite dimension \(d\ge1\), every frame size \(1\le\ell\le d\), every \(\lambda,h>0\), and every \(0<\alpha\lambda d/\ell<2\). The frame identity \((PP^\top)^2=(d/\ell)PP^\top\) supplies the closed scalar second-moment recursion. Frame isotropy and independence close the mean recursion. A separate Cauchy--Schwarz argument proves the sharp \(q\le\ell\) bound, and explicit coordinate-frame laws attain both ends and every intermediate point.

`verify.py` was executed from this artifact's actual working-directory copy and returned `PASS: 1305 exact-rational transition, moment and endpoint checks`, with the two rational examples stated in the finding. It enumerates exact distributions for selected finite dimensions and steps, so the script corroborates but does not replace the infinite-law proof.

All comparisons to prior literature concern equality, implication, and scope rather than title similarity. Inaccessible full texts are not treated as inspected. The result is self-reviewed; no independent audit or external certification has been performed.
