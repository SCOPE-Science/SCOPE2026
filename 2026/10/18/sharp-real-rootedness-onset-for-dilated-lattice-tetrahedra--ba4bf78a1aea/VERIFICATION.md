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

The final statement is for every full-dimensional lattice tetrahedron in Z^3 and integer m>=1. The involution lambda_i->1-lambda_i shows box coefficients ell1=ell3=A_m. Height-one open-box lattice points equal interior points of mS, so Ehrhart reciprocity yields A_m=sum_{j=0}^3 h_j binom(m+j-1,3). The total count is T_m=6a m^3-4b m^2+E m-3 via lattice-index inclusion-exclusion (full 4D determinant 6a m^3, four 3-column facet indices summing to 4b m^2, six 2-column indices E m, four unit 1-column indices). Thus B_m=T_m-2A_m and G_m=B_m-2A_m=H m^3/3+(E-2(11+2h1-h2+2h3)/3)m+1. Direct arithmetic verifies G2=2E+4h2-11>=1 and G_m=1+m(G2-1)/2+H(m^3-4m)/3>0 for all integer m>=2. For A>0, t[A+(2A+G)t+At^2] has one simple zero and two distinct negative roots, discriminant G(4A+G)>0; A=0 yields a scalar t^2. A1=h3, A2=h2+4h3, A3=h1+4h2+10h3, A4=1+4h1+10h2+20h3, so the onset cases and universal 4 are exact. At m=1 the criterion G1>0 is necessary as well as A1>0; nonnegative coefficient B1 rules out a second negative-discriminant branch. Unimodular S gives ell*(3S)=6t^2 and ell*(4S)=t+19t^2+t^3. Independent SymPy algebra and 16 direct four-dimensional strict-interior lattice enumerations in 4 tetrahedra and m=1..4 agree. Finite checks confirm only those cases, not the universal proof.

## originality

PASS

BKN Proposition 4.5 already supplies the general dimension-three local-h* coefficient formula, so that formula, symmetry and standard reciprocity are not independently original. The new asserted contribution is a sharp uniform lattice-tetrahedron dilation cutoff and the complete earlier-onset criterion with a strict gamma gap. Nill's box theorem only guarantees sufficiently large lattice width, Jochemko's sharp Veronese theorem is for ordinary Ehrhart h*, and Athanasiadis's edgewise-local-h theorem concerns subdivisions rather than arbitrary lattice box polynomials. The actual theorem hypotheses and implications were compared, not merely paper titles. This is qualified best-of-knowledge PASS, not proof of priority.

## value

PASS

A sharp dimension-three universal cutoff m=4 for strict local-box real-rootedness addresses the natural quantitative refinement of eventual root reality. The result classifies all earlier dilations by intrinsic Ehrhart h*-coordinates and lattice edge lengths, and the unimodular example proves optimality of the uniform bound. The explicit edge-based gap is a nontrivial geometric-to-algebraic inequality and the statement covers every lattice tetrahedron, not an arbitrary small table; restricted to three-dimensional simplices, no unsupported higher-dimensional or lattice-width generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
