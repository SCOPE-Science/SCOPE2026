---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The power map [x:y:z]->[x^m:y^m:z^m] is etale of degree m^2 on the torus, and the quotient cubic has h(a,b)=(a-b)(b-1)(1-a)/(ab). Exact derivatives factor as -(a^2-b)(b-1)/(a^2 b), -(a-1)(a-b^2)/(a b^2), so the only torus critical parameters are 0 and two roots of lambda^2+27. At the two nonzero values the affine Hessian determinant reduces to -9; every lifted singularity is a node. The 3 coordinate vertices are ordinary m-fold by tangent cone y^m-z^m, and other boundary intersections are smooth. For nonzero lambda, valuations of X/Z and Y/Z at [0:1:1], [1:0:1] form independent rows mod m; their Kummer classes give degree m^2 and geometric integrality. Plane arithmetic genus minus 3*binom(m,2) and optional m^2 nodes yields both genus formulas. Independent SymPy computation reconstructed the Groebner eliminant lambda(lambda^2+27), nonzero nodal Hessian -9, and m=2 genera 7 and 3. The symbolic/Kummer proof, not F13 examples, establishes the full theorem.

## originality

PASS

Falk–Yuzvinsky original primary full-text pages on the Fermat–Ceva multinet study the classical degree-m pencil and arrangement resonance, not this degree-3m pencil involving a lambda (xyz)^m smoothing. Dimca original preprint treats line-arrangement characteristic/resonance varieties and special pencil multiplicity; its primary introduction/pencil theorems differ in statement. Resultary searches found no same Kummer finite-parameter genus trichotomy. The classical Ceva 3m-line baseline is credited, not novel by itself.

## value

PASS

A natural explicit one-term smoothing of a standard 3m-line arrangement has a complete singular-parameter and geometric-genus jump law for every m, including irreducibility despite Kummer branching; the m^2 node correction is useful for normalization families and discriminants. Exact boundary and exceptional fiber regimes make this a meaningful structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
