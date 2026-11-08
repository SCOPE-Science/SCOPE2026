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

Shor Proposition 3.4 fully classifies reflective semigroups by admissible multiplicity a with explicit gap layers. For a>=3, only g+ja upper-layer gaps are isolated, including g iff a|(g-1); for a=2, all odd gaps isolated. Thus I(g,a)=floor(g/a)+1_(a|g-1)+(g-1)/2*1_(a=2,g odd). Summing admissible a gives exact integer tail, with at most two exceptional one-unit corrections. Divisor counts provide uniform rate and k=2 lower scale; divisor-sum identity gives mean log g using standard hyperbola estimates. Independently generated actual semigroups and checked every tail for g=2..59.

## originality

PASS

Shor 2022 directly supplies the complete genus/multiplicity classification and gap formula, explicitly credited. This does not itself state isolated-gap histogram, harmonic fixed-genus tail or logarithmic mean. Smith 2022 studies isolated gaps generally but full source unavailable; its possible coverage is retained as material risk.

## value

PASS

Distribution of a natural combinatorial statistic on a precisely classified, nontrivial finite population gives a sharp heavy-tail law and expectation asymptotic with divisor-scale quantitative error; this is mathematically more informative than recomputing the population size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
