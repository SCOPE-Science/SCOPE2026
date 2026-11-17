---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The Gram operator F*F has top-left projection V1V1*, off-diagonal V1T and lower diagonal I+T*T; conjugating V1H1⊕ker V1* separates 0_E and the shear Gram G*G. Polar decomposition of T splits ker T*, ker T and K=(ker T)^⊥, reducing the nontrivial part to the commuting positive block [[I,S],[S,I+S²]]. The stated continuous 2×2 unitary W(s) diagonalizes this exactly for all s>=0, yielding unitary |F| normal form with φ(S),φ(S)^−1 and exact exceptional eigenspace multiplicities. At λ≠1 Schur complement reduces Fredholmness to (1−λ²)²/λ²−T*T; at λ=1 the off-diagonal [[0,T],[T*,0]] is Fredholm iff T is Fredholm; infinite ker V1* adds essential 0. Thus the full essential spectrum and Schatten p criteria follow for arbitrary bounded T and two isometries. Independently checked eigenvalues of scalar blocks s=0,.25,1,4 and inspected finite matrix checker for all rectangular ranks; finite data do not establish infinite theorem.

## originality

PASS

Garcia 2009 and Raghupathi 2012 already give nonexceptional singular spectral mapping and norm formulas for classical Foguel-type operators; these are credited, not claimed anew. Nag–Golla 2026 concerns norm/minimum attainment and Fredholm data of generalized two-isometry blocks. The final claim is stronger: full positive unitary decomposition as an operator including identity and zero defect multiplicities, continuous spectrum, and all Schatten-power formulas. No read source establishes this exact complete normal form, but it is derived from elementary polar decomposition; a previously known block-shear normal form remains a material priority risk. Full primary-text access failed, so O is best-knowledge with nontrivial caveat.

## value

PASS

A complete singular spectral normal form for all bounded corners and arbitrary isometric diagonals is a natural uniform classification, not a numerical sample. It resolves exceptional unit and zero multiplicities that setwise spectrum omits, distinguishes Fredholm unit gaps from isolated essential unit points, and gives exact all-p Schatten perturbation costs. These motivate the precise result independently of any broad new operator theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
