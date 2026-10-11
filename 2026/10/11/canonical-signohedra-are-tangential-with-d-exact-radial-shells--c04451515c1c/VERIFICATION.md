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
- the source polar partner \(Q_d=C_d+\Diamond_d\) has vertices equal to the signed coordinate permutations of \((2,1,\ldots,1)\);
- every such vertex has squared norm \(d+3\);
- every nonzero sign vector \(s\) with support \(k\) defines the facet \(\langle s,x\rangle\le k+1\) of \(Q_d\);
- its normalized facet distance is \((k+1)/\sqrt{k}\), and these distances strictly increase with \(k\);
- polarizing the equiradial vertex set gives a signohedron insphere tangent to every facet, of radius \(1/\sqrt{d+3}\);
- the source polar vertex \(s/(k+1)\) has norm \(\sqrt{k}/(k+1)\), strictly decreasing with \(k\);
- antipodal pairs certify uniqueness of all four extremal centers;
- the reciprocal radius identities follow from the polar normalization.

`verify.py` enumerates the complete source vertex and facet systems for \(2\le d\le7\), checks every inequality and facet affine rank, verifies the shell multiplicities, reconstructs the reciprocal polar incidence, and solves the full Chebyshev linear programs for \(Q_d\) and \(\Sigma_d\). Finite computation is corroborative only and does not assess originality.
