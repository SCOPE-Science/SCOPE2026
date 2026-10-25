---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For Gaussian exposure directions, each of (n+1)! strict coordinate permutations has equal probability. For m=1 a winner pattern is a subset of leaves above the hub, of size k, with k!(n-k)! orders; for every m>=2 the triple-simplex winners recover the decreasing ORDERED high-leaf list, with (n-k)! orders. This yields exact Z_{n,1}=(n+1)^(-q) sum C(n,k)^(1-q) and Z_{n,m}=n!/((n+1)!)^q sum(j!)^(q-1), m>=2. Independent permutations check all n=2..5 and all m. Uniform Stirling plus Riemann sums at q=1+t/n and 1+t/(n log n) give the stated h(x) and uniform-x crossover integrals; Shannon limits 1/2 by direct differentiation. Fixed-q and collision limits follow from binomial/factorial dominance. These are genuine analytical asymptotics rather than finite extrapolation, and exclude anisotropic Gaussian metrics.

## originality

PASS

Best-of-knowledge comparison of the exact final statement, including earlier stronger/special-case results and mathematical implications, did not identify decisive coverage of the stated new component; this is not an exhaustive global priority certification.

## value

PASS

The geometric normal-fan refinement at m=2 is known, but its angular probability redistribution drives two quantitatively different sharply scaled Renyi entropy transitions (1/n and 1/(n log n)) with explicit crossover functions. This resolves a motivated angle-spectrum sensitivity of a canonical graphical-zonotope-to-stellohedron family, not a rebranding of vertex enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
