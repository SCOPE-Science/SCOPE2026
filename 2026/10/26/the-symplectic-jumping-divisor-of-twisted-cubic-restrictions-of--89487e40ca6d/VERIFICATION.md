---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For V=C^6 with nondegenerate bivector pi, the Koszul evaluation quotient yields exact vector-bundle sequence 0->E(-1)->Omega^2_{P5}(2)->O->0: the map is surjective since a five-dimensional subspace cannot be isotropic in symplectic dimension six. On any smooth twisted cubic C in P(U)=P3, Ann(U)=A has dimension two and the middle term is O_C(-2)^3 + O_C(-1)^6 + O_C. The last O maps by pi|Lambda^2 A. If nonzero, split off O and get E|C=O(2)^6 + O(1)^3. If zero, the cross term O(-1)^6 -> O has no basepoint because pi-sharp(A) is a two-plane contained in U and cannot lie in any point line; its linear coefficient sections span H0(O_C(1)). Thus h0(E|C(-3))=1 and h0(E|C(-2))=6. With global generation of E and E^vee(1) as assumed from Denham–Miro-Roig–Schenck and c1(E)=5, all nine splitting degrees lie in [0,3] and sum to 15; their h0 counts force (3,2^4,1^4). Isotropy of two-plane A is one smooth symplectic Plucker hyperplane equation in Gr(2,6), giving the seven-dimensional jumping divisor. I inspected the actual RESULT.md and verify.py; the reported fifteen coordinate-plane checks are consistent but do not establish universality. Boundary: smooth cubics over C and this symplectic bundle only.

## originality

PASS

The originating 2026 Denham–Miro-Roig–Schenck paper builds the same bundle, while Landsberg–Manivel §6.2 already gives its symplectic constant-rank realization up to dual twist. The asserted addition is the exact two-type restriction to every twisted cubic and the isotropic-Grassmannian jump divisor. I examined the relevant Landsberg–Manivel section and the Denham abstract, but not the unavailable complete Denham §3; cannot declare the original paper conclusively noncovering. Best-of-knowledge no direct prior cubic-restriction classification observed; this is a material priority risk.

## value

PASS

For a natural uniform nonhomogeneous rank-nine bundle, uniform splitting on lines does not decide splitting on degree-three rational curves. Computing both nontrivial cubic restriction splittings and a geometric codimension-one jumping locus is a motivated structural classification; it can distinguish a bundle's curve behavior from line-uniformity. This is not a discovery of the underlying already known symplectic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
