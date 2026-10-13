---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the exact incidence computation

Execute `python3 verify_dodecagon.py` with standard Python 3.10 or later. No specialized computer algebra dependency is required.

The code constructs twelve vertices with coordinates in \(\mathbb Z[\sqrt3]\), computes the twelve side lines and their 66 distinct intersections, then enumerates every pair of those points to form the 49 lines containing at least four seed points. It enumerates all 1176 pairs of final lines to obtain the exact characteristic-zero multiplicity basket. It next clears denominators, takes primitive coefficient triples, tests all 18424 triple determinants by exact quadratic-integer arithmetic, factors every nonzero determinant norm, and checks the two different kinds of good-reduction obstruction (vanishing line coefficients and coincident lines) using coordinate-norm gcds.

The code computes the complete exceptional-prime intersection multiplicities at both embeddings \(\sqrt3\mapsto\pm5\) in characteristic 11 and \(\sqrt3\mapsto\pm4\) in characteristic 13. A nonexceptional check at characteristic 23 is a supplemental comparison, not the justification for the all-primes conclusion. Expected output starts with `VERIFY_OK`.

The finite exhaustive determinant calculation yields the necessary infinite-prime conclusion by a number-theoretic implication: if a nonzero quadratic-integer determinant vanishes modulo a prime over \(p\), then \(p\) divides its integer field norm. The full list of norms, rather than any tested bound on primes, controls all primes \(p\ge5\).

This verification is of the written result and the included algorithm only; it is not an independent external audit. It establishes no behavior in characteristics two or three, no statement about rational points, and no positive-characteristic freeness claim.
