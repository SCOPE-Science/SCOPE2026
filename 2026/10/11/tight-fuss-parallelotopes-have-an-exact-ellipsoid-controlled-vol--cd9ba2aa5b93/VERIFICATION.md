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
The arbitrary-dimensional proof is given in `RESULT.md`.

Critical checks:
- the source gives \(\ell_k=\|Aq_k\|\) and \(\sum_k\ell_k^2=\operatorname{tr}(A^2)=1\);
- \(n\)-volume is \(2^n\prod_k\ell_k\);
- Hadamard's determinant inequality gives \(\prod_k\ell_k\ge\det A\), with equality exactly when the frame diagonalizes \(A\);
- arithmetic-geometric mean gives \(\prod_k\ell_k\le n^{-n/2}\);
- the constant-diagonal lemma constructs an orthonormal frame satisfying \(\|Aq_k\|^2=1/n\) for every \(k\);
- continuity and connectedness give every volume between the two endpoints;
- polarity gives \(C_Q=\operatorname{conv}\{\pm q_k/\ell_k\}\), so \(\operatorname{Vol}(C_Q)=2^n/(n!\prod_k\ell_k)\);
- corresponding polar volumes multiply to \(4^n/n!\).

`verify.py` checks deterministic anisotropic positive matrices in dimensions \(2\) through \(7\). It recursively constructs constant-diagonal frames, verifies both endpoint formulas, samples additional orthogonal frames inside the sharp interval, and checks the polar volume product. The finite replay is corroborative only and does not assess originality.
