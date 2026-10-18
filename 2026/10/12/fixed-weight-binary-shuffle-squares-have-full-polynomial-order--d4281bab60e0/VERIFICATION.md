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

Select a weak composition p0+⋯+pk=n−k and choices ci∈[0,pi], i<k. A constructive interleaving of two copies of X=0^p0 1 ⋯ 1 0^pk has gap vector (p0+c0,p0−c0,...,p_(k−1)+c_(k−1),p_(k−1)−c_(k−1),2pk). It is explicitly a shuffle square, and the gap vector uniquely recovers p,c. Thus the number of distinct outputs is ∑_compositions∏_(i<k)(pi+1)=[z^(n−k)](1−z)^(−(2k+1))=binom(n+k,2k); upper bound binom(2n,2k) counts all words with 2k ones. Both are Θ_k(n^(2k)) for fixed k; no assertion of leading constant for k>=2. Independently enumerated construction/inverse at small n,k; analytic injection is the infinite proof.

## originality

PASS

Best-of-knowledge priority for the precisely delimited contribution. Known subfamilies, classical inputs, and plausible stronger derivations separately documented; searches alone are not treated as a novelty proof.

## value

PASS

Resolves the asymptotic polynomial *order* expressly requested in a primary combinatorics paper for every fixed 2k-one slice (new when k≥2), with a clean explicit injective lower-bound construction. It is a motivated enumerative problem, not an arbitrary small table; leading constants remain open and are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
