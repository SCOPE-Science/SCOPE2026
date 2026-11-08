---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A full ordered-bigram count vector c_ij of a word length m+1 is exactly an integer 3×3 arc-count matrix admitting an Eulerian directed trail. The standard necessary-and-sufficient criterion is weak connectivity on all positive-degree vertices and degree imbalance either (0,0,0) or permutation (+1,-1,0). In balanced class write δ01=δ12=δ20=t; t≠0 forces directed triangle, t=0 splits by one/2/3 occupied vertices with loops and bidirected edges. In each unbalanced ordered start/end type δ01=t+1, δ12=δ20=t; all entries parameterized by opposite arc pairs and loops, subtract the precise t=0 disconnected third-vertex loop class. Combining balanced A(z) and six(F(z)-B(z)) gives z(9−12z+5z²+19z³−4z⁴−10z⁵−14z⁶+14z⁷+6z⁸−9z⁹+3z¹⁰)/((1−z)^7(1+z)^2(1+z+z²)). Independently simplified expressions in SymPy to identical rational fraction and checked coefficients 9,24,65,... for small m. Dominant pole z=1 order seven with numerator 7 and cofactor 12 gives 7m^6/8640+O(m^5), period divides six. m≥1; length-one host has a single empty profile separately. Code-size follows by one representative per profile.

## originality

PASS

Qualified PASS: Euler trail criterion, generic reconstruction algorithms, and binary exact two-gram multispectrum are prior. Bernardini–Conte–Gabory and collaborators study equality of *sets* of factors, not the *multiplicity* count vector; changing sets to multisets changes equivalence classes. The new exact all-m ternary integral Euler-flow count and degree-six quasipolynomial are not implied by those published statements, though an older enumeration of 3×3 integer Euler trails could subsume it.

## value

PASS

Complete cardinality of a natural noiseless sequencing readout alphabet and zero-error reconstruction code, providing the first nontrivial three-symbol exact multiset profile law with circulation/connectivity correction and sharp growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
