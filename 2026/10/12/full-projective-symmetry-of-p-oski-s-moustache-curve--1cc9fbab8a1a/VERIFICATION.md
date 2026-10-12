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

The proof has a symbolic replay in `verify.py`. The script uses exact SymPy arithmetic and checks:

- \(q_\lambda\circ U_t=q_\lambda\) for symbolic \(t\) and \(\lambda\);
- \(q_\lambda\circ R_m=-q_{{m+1-\lambda}}\);
- \(R_m^2=\operatorname{diag}(1,-1,1)\), \(R_m^4=1\), and \(R_mU_tR_m^{-1}=U_{{it}}\);
- determinant \(-1/4\) for every finite member of the pencil \(y^2+xz+\lambda x^2\);
- the coefficient identities \(c^2=ag\), \(af+2bc=0\), and the resulting affine parameter map;
- \(\sum_{{j=1}}^m(j-(m+1)/2)^2=m(m^2-1)/12\);
- the four normal forms \(U_bR_m^k\);
- the infinitesimal identity \(x(q_\lambda)_y-2y(q_\lambda)_z=0\).

For \(2\le m\le8\), it also exhausts permutations of \(\{1,\ldots,m\}\) as a diagnostic and finds only the identity and reflection affine maps. The theorem for arbitrary \(m\ge2\) rests on the symbolic second-moment proof, not on this finite diagnostic.

A successful replay prints `VERIFY_OK`. The verification does not test or claim any automorphisms outside projective linear transformations of \(\mathbb P^2\).
