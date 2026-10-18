---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every finite field F_q including characteristic two, Heisenberg bracket [x,y]=z and P²⊆kz force z to annihilate P under Leibniz and associativity. Thus all products arise from one nonzero symmetric 2x2 form S with multiplication uv=(u^T S v)z. Put J=[[0,1],[-1,0]], T=J^-1 S. S symmetric iff tr T=0 in all characteristics. Simultaneous Poisson equivalence changes T by GL2 similarity, with arbitrary two-dimensional central shear. Consequently Aut order =q² |C_GL2(T)|; a linear Lie derivation has matrix A on V and D(z)=tr A z, and its multiplication condition is exactly [A,T]=0, giving dimension 2+dim C_M2(T). For odd q the nonzero trace-zero 2x2 similarity classes are q companion-matrix determinant classes including nilpotent and the split/anisotropic subclasses, all with derivation dimension four. For even q they are q nonscalar Jordan classes and q-1 nonzero scalar classes, yielding 2q-1 classes, with scalar derivation dimension six (otherwise four), and the exact orbit/Aut formulas through GL2 centralizers. Directly enumerated GL2 trace-zero conjugation orbits for q=2,3,5: 3,3,5 classes with orbit partitions [1,3,3], [6,8,12], [20,20,24,30,30]; pinned verify.py additionally implements F4 and checks derivative centralizers, none of which substitutes for all-prime-power argument.

## originality

PASS

Petrov--Pypka arXiv:2609.13784 Theorem 5.2 already *completely classifies the structural Heisenberg mixed family over arbitrary fields* up to weighted congruence of its symmetric form; Corollary 5.3 even gives exactly the odd-characteristic normal representative diag(1,d). These ARE NOT new and must be credited. The current evaluated claim adds finite-field orbit cardinalities of each fixed bracket structure, all Aut group orders, explicit even-characteristic scalar/Jordan strata and the exact derivation-dimension jump 4→6. The earlier published Dedekind Poisson finding independently gives automorphism count of the *anisotropic odd-characteristic subfamily* and is credited rather than double-counted. The full relevant Petrov--Pypka pages 22--25 were read via authorized institutional retrieval, not abstract alone: those passages state equivalence/normal forms but do not give the numerical centralizer or derivation profiles. Distinct original surviving material is the full all-finite-field symmetry stratification and the modular jump.

## value

PASS

For a natural minimal nonabelian Poisson structure, classifying stabilizer sizes and derivation tangent dimensions quantifies moduli-orbit geometry rather than merely renaming existing isomorphism classes. Characteristic-two scalar strata are new finite-field phenomena: exactly q-1 exceptional isomorphism classes have derivation dimension six, while q Jordan classes have four, an interpretable two-dimensional symmetry jump. Uniform q, actual orbit sizes and full Aut orders make this a useful complete finite-field symmetry profile even though general 2x2 similarity theory and Petrov--Pypka structural classification are not new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
