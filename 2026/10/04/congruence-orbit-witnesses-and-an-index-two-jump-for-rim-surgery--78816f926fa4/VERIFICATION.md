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

The primary source was inspected at Definition 1.1, Theorem A, Theorem B, and Corollary 9.1. The exact source formula is
\[
E(\Sigma_{g,a,J})
=
\operatorname{Stab}(q_0)
\cap
\operatorname{Stab}(\Gamma_\mu(J)\cdot[a]).
\]
The source's infinite-index proof uses even Dehn twists and the integral orbit of the allowed rim-class set.

The split index-two refinement follows from the sign homomorphism on the setwise stabilizer. A hyperelliptic involution has order two and acts by \(-I\) on integral first homology. It therefore fixes the mod-two Rokhlin quadratic form while reversing \([a]\).

For an odd prime \(p\), the reduction of every squared Dehn twist is a symplectic transvection with coefficient divisible by \(2\); since \(2\) is invertible modulo \(p\), all coefficients occur. The proof in RESULT.md gives an explicit one- or two-transvection path between arbitrary nonzero vectors, establishing transitivity and the orbit sizes
\[
p^{2g}-1
\quad\text{and}\quad
\frac{p^{2g}-1}{2}.
\]

The bundled verifier exhaustively checks the finite transvection orbit mechanism in representative cases and returns:

`VERIFY_OK g2_p3=80/80,pairs=40 g2_p5=624/624,pairs=312 g3_p3=728/728,pairs=364`

The computation is not an infinite proof. The universal statement is established by the symbolic transvection argument.

No independent audit has been performed.
