---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For any P subset of primes 1(mod4), a_k=2^k product_{r in P,r<=k}r forms a divisibility chain with log a_k=O(k). On Q=product_{r in P,r<=sqrt(log X)}r, CRT makes 1_{r|n} independent Bernoulli(1/r) over residues, and reduced-prime-square sums independent Bernoulli(2/(r-1)). Exponential Markov bounds high T(n) and low T(p²+q²) with shared exponent delta=1-t+t log t, t=1/log2, checked independently. Q=exp(O(sqrt(log X))) allows uniform Brun-Titchmarsh for p,q<=sqrt X; shifts k or l<ceil sqrt(log X) and primes dividing Q cost O(X/sqrt(log X)). Combining disjoint cases yields the claimed uniform finite-X bound. Mertens in progression 1 mod4 yields exponent delta/2 for loglog X. Independent finite checks validate eight prime moduli, not the analytic uniform bound.

## originality

PASS

Yan–Xu 2026 already proves density zero for all divisibility chains with divergent reciprocal divisor sum and Dai–Pan provides prior positive density under bounded reciprocal sum. The distinct quantitative theorem is an explicit uniform finite-scale large-deviation rate for this specific critical-growth chain, not the qualitative o(X) corollary or the elementary local CRT probability.

## value

PASS

Effective sparsity with an explicit exponent for a logarithmic-counting divisibility chain on the boundary of a Romanoff-type positive-density criterion supplies a motivated quantitative refinement, not just a parameter change or numerical small gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
