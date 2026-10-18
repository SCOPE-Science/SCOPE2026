---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: The bracket is det(x,y,z)e1. Preservation yields exactly Pe1=det(P)e1, equivalent to upper-left λ≠0 and lower-right SL2. In char≠2 a nonscalar involution has complementary 1+2 eigenspaces, every such eigenspace is a ternary-abelian subalgebra. For any endomorphism, the Nijenhuis defect vanishes by the source symbolic multilinear expansion; the inspected independent sympy checker substitutes a fully arbitrary nine-entry operator, not one normal form. The characteristic line D=Ke1 has exactly three invariant incidences and group shears/SL2 act transitively on each, as seen by bases modulo D. Each line in F_q^3 has q² plane complements; counting whether D is the line, lies in the plane, or neither yields q²,q²(q+1),q²(q²−1) per eigenspace signature and total formula. Inspected exact F3 F5 orbit enumeration algorithm and normal forms; no characteristic-2 inference.

## originality

PASS

PASS best of knowledge for COMPLETE orbit quotient/census: Sheng-Tang 2017 Example 5.22 has only three example matrices (two mutually conjugate), and Hou-Sheng 2021 records universal Nijenhuisness, neither yields six conjugacy classes or finite-field orbit sizes. Published Resultary search showed only other algebra automorphism counts. Core Nijenhuis premise and classification criterion are credited as prior.

## value

PASS

PASS: Completes the natural moduli/orbit classification of product structures on the unique nontrivial 3D ternary Lie algebra. Incidence of the derived line splits strong/perfect/generic types, and an exact F_q stabilizer-orbit census is useful for later moduli, deformation and counting comparisons. Not a mere relabeling of three prior examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
