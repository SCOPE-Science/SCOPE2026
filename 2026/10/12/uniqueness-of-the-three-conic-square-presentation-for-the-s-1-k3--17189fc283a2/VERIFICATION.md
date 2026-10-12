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

The verification has three parts.

1. **Published geometric input.** In arXiv:1909.01909v5, Section 3.1 lists exactly six \((-2)\)-curves on an \(S_1\) surface, gives their intersection matrix, identifies the unique square-two polarization \(D\), and records
\[
A_1+A_4=A_2+A_5=A_3+A_6=2D.
\]
Proposition 8 gives the smooth double-plane model, the three six-tangent conics, \(\operatorname{Aut}(X)\cong C_2\), and the deck action \(A_j\mapsto A_{j+3}\). Section 5.1 gives the construction \(F=q_1q_2q_3-f^2\).

2. **Exact deduction.** Any smooth six-tangent conic has even branch divisor on \(\mathbb P^1\), so its double-cover restriction splits. Both components are smooth rational curves on a K3 surface and hence are \((-2)\)-curves. The published completeness of the six \((-2)\)-curves therefore leaves precisely the three deck orbits. For two square presentations, completeness identifies the quadratic factors up to permutation and scalar. The remaining equation
\[
(f'-f)(f'+f)=(c-1)q_1q_2q_3
\]
forces \(c=1\), because a nonzero homogeneous cubic cannot be a product of any subset of irreducible quadrics. Then \(f'=\pm f\).

3. **Projective stabilizer.** A projective transformation preserving the branch sextic lifts, after choosing a square root of the scalar by which it changes \(F\), to the double cover. Since the complete K3 automorphism group is the deck group and both deck-group elements descend to the identity on \(\mathbb P^2\), the projective stabilizer is trivial.

`verify.py` independently checks the six-curve matrix pattern, the three deck orbits, invariance of the matrix under the deck involution, and the factor-degree obstruction. It is finite and exact; it is not used as a substitute for the geometric splitting argument or the published completeness theorem.
