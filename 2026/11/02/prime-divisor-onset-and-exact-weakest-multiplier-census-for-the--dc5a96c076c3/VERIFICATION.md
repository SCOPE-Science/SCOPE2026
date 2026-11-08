---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The left and right branch derivative matrices are signed monomial; a word with t right visits induces permutation +t mod M with g=gcd(M,t) cycles. Each cycle product has 2-adic exponent t/g plus occupied left gaps of one residue class; thus eigenvalue modulus 2^((t+g ell_c)/M). Partitioning t+1 gaps into g residue classes gives the stated binomial weighted-composition histogram. When g=1 all moduli equal 2^(n/M), whereas g>=2 forces t>=p and min modulus >=2^(p/M); R^p L^(n-p) achieves the bound for n>p, and RL^(n-1) realizes splitting. Complement of all occupied classes at t=p yields E_M(n)=binom(n,p)-binom(n-p,p)-binom(n-p-1,p-1). Primary symbolic coding supplies one isolated point for each non-all-left word, not merely a formal word count. Independently checked 3514 signed-matrix words and 56 histogram cases; not a proof by finite sample.

## originality

PASS

The prior original map paper gives symbolic dynamics and partial spectral information, and the published Resultary real-spectrum law gives the exact signed-cycle characteristic polynomial ∏(λ^(M/g)-(-1)^(t/g)2^a), i.e. a major structural predecessor. Its statement classifies real/nonreal by M|t and counts residues, but it does not determine distribution of the cycle weights a, weakest moduli, prime-divisor onset, or extremal histogram. The audited refinement needs the independent gap-occupancy enumeration.

## value

PASS

The exact least expansion modulus and complete histogram refine the dynamics of a well-defined nonuniformly expanding piecewise-affine system. The smallest prime divisor of phase dimension gives an unexpected sharp onset of spectral heterogeneity and a polynomial-sized family of minimizing periodic words. This is not a routine reformulation of the real/nonreal eigenvalue count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
