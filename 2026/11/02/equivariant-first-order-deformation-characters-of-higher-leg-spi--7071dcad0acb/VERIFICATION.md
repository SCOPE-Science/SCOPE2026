---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The finite algebra basis is {1,x_i^s:1<=s<a_i}. Pairwise least-common-multiple monomial syzygies constrain each pure power P_i to images V_i comprising nonconstant x_i-powers and top x_j^{a_j-1} on other axes; each mixed Q_ij maps to W_ij comprising nonconstant i/j powers and top powers on other axes. The remaining syzygies impose no further constraints. Shifting generator weights gives the complete Hilbert tangent character H. The cotangent exact sequence Der(A)->Der(S,A)->Hom_S(I,A)->T1->0, with explicit Der(A) character D and Der(S,A) character B sum t_i^-1, yields T1=H-B sum t_i^-1+D. Dimensions rd+r(r-2)(r+1)/2 and d-1+r(r^2+r-4)/2. Independent rational pair-lcm linear-system calculations at all-two exponents recovered r=4: d=5, tangent=40, derivation-image rank=4, T1=36; r=5: d=6, tangent=75, derivation-image rank=5, T1=70.

## originality

PASS

The three-leg tangent excess 6 and general monomial-ideal tangent-weight algorithms are prior results. Best-of-knowledge the all higher-leg closed equivariant Hilbert tangent character AND abstract T1 character are not stated by those sources, nor implied without nontrivial syzygy simplification and derivation analysis. The assertion does not cover obstruction T2 or smoothing.

## value

PASS

The length-independent tangent excess and full weights refine scalar tangent dimensions and determine equivariant infinitesimal deformation directions for a natural family of nonreduced monomial schemes. These exact characters are independently useful for Hilbert-scheme local geometry and deformation calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
