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

The bundled `verify.py` reconstructs the affine Grassmann chart at the standard common-kernel plane and expands the determinant identically in the three plane parameters. It checks all ten cubic coefficients, eliminates the three graph variables, performs the transverse coordinate change, and verifies equality with the seven-generator ideal used in the proof.

It then computes a lexicographic Gröbner basis and confirms the eight standard monomials giving Hilbert function \((1,4,3)\) and length \(8\). It also reduces every cubic monomial in the four transverse generators to zero and confirms local tangent dimension \(6\), consistent with the source tangent-excess formula. The recorded replay output is `VERIFY_OK`.

The proof is exact over characteristic different from \(2\); the script uses symbolic integer/rational polynomial arithmetic. No finite sampling is used to infer the infinite statement. The calculation does not address characteristic \(2\) or other Fano components.
