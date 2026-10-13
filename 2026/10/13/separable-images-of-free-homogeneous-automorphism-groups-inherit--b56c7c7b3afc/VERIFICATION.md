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

The proof is a source-backed implication chain rather than a computational claim.

1. **Automatic continuity.** Kechris--Rosendal prove that a homomorphism from a Polish group with ample generics into a separable topological group is continuous.
2. **Dense-image closure.** If \(L\) is dense in \(G\) and \(\varphi\) is continuous, then \(\varphi(G)\subseteq\overline{\varphi(L)}\). Since \(\varphi(L)\subseteq\varphi(G)\), the closures are equal.
3. **Local finiteness survives homomorphisms.** Every finitely generated subgroup of \(\varphi(L)\) is the image of a finitely generated subgroup of \(L\), hence is finite.
4. **Torsion-free targets.** A locally finite subgroup of a torsion-free group is trivial. Therefore \(\varphi(L)=\{1\}\), and the closure identity forces \(\varphi(G)=\{1\}\) in a Hausdorff target.
5. **Free homogeneous application.** Siniora--Solecki explicitly provide ample generics and a dense locally finite subgroup for \(\operatorname{Aut}(M)\) when \(M\) is free homogeneous over a finite relational language.

No numerical experiment is relevant to these implications. The self-review rechecked the exact hypotheses and the direction of each implication. No independent audit has been performed.
