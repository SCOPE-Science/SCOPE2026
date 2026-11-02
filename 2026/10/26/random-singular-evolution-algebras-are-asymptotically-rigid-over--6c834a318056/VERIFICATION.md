---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Each square row of M is uniform over F_q^n. Pairwise nonzero, nonproportional rows (2LI) occur with probability ∏_{j=0}^{n-1}(1-[1+j(q-1)]/q^n) by projective-direction occupancy. If 2LI holds, multiplication by each vector of any alternative natural basis annihilates the span of its other columns, hence has rank <=1. A column supported in >=2 coordinates would span >=2 independent square rows, contradiction: all such basis changes are monomial. For q>3 a zero row or proportional pair permits a nonmonomial orthogonal pair, so necessity holds in that field range only. Any monomial automorphism induces a permutation of the nonzero support digraph; if the digraph is asymmetric the permutation is identity. Arc relations t_j=t_i^2 then force all scalars 1 in a strongly connected support graph with a loop. The probability of no loop is q^-n, failure of strong connectivity at most sum_{s=1}^{n-1}C(n,s)q^{-s(n-s)}, and a nontrivial permutation moving k labels can preserve at least k(2n-k) moved Bernoulli positions with probability <=rho^{kn/2}, giving sum_{k=2}^n n^k rho^{nk/2}=O_q(n^2 rho^n). Combining with 2LI failure gives O_q(n^2 rho^n); Pr(M singular)=1-∏_{i=1}^n(1-q^-i)>=1/q, hence the conditional bound follows without independence assumptions. Separately independently enumerated projective 2LI occupancy: 6/16 for q=2,n=2; 210/512 for q=2,n=3; 48/81 for q=3,n=2. Finite checks illustrate, not prove asymptotic claims.

## originality

PASS

PASS for the random uniform-coefficient strong asymptotic trivial-automorphism theorem including positive-density singular matrices; known 2LI deterministic criterion, finite-projective occupancy idea, and random directed-graph asymmetry are acknowledged building blocks, not original discoveries.

## value

PASS

Automorphism rigidity of a random evolution algebra is a natural open structural-probability question. The exact failure-rate estimate with an unrestricted dense matrix is nontrivial because generic matrices can be singular with positive limiting density; extending rigidity to that nonperfect subpopulation is mathematically meaningful. The result integrates deterministic natural-basis geometry and asymmetric random support to control actual algebra automorphisms, beyond a routine projective occupancy calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
