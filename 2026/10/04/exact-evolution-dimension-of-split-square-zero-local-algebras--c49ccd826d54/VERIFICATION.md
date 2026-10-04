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
The proof was checked directly from the multiplication law. With coordinates \(x_0,x_1,\ldots,x_r\), the squaring map is \(H=(x_0^2,2x_0x_1,\ldots,2x_0x_r)\). The displayed \(2r+1\)-term decomposition expands exactly to those coordinates.

For the lower bound, the key point is not a finite experiment. If the coordinate span \(W\) is contained in \(L=\operatorname{span}\{\ell_j^2\}\), projection to \(\operatorname{Sym}^2(V^*)\) has kernel containing all of \(W\). The mixed components of the same squares must span \(x_0V^*\), so their \(V^*\)-parts span \(V^*\); choosing \(r\) independent parts gives \(r\) independent projected squares. Rank-nullity therefore forces \(\dim L\ge2r+1\).

As a separate consistency check, the Alder--Strassen lower bound for the local algebra \(A\) is \(2\dim(A)-1=2r+1\). Polarization turns every simultaneous Waring decomposition into a bilinear multiplication decomposition of the same length, yielding the same lower bound.

The source bridge from Waring rank to minimal evolution dimension was checked against arXiv:2609.32784v1. The source's stated application is the truncated-polynomial family; no square-zero-radical formula was located in the inspected text. Characteristic \(2\) remains outside the theorem.
