---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Pairwise independence and fairness force E K=n/2 and Var K=n/4. If K=r+qJ with J integer in {0,...,N}, then (J-a)(J-a-1)>=0 gives the sharp minimum variance delta(1-delta), while J(N-J)>=0 gives the sharp maximum m(N-m). Conversely, the nearest-lattice and endpoint laws have the same mean m and these two endpoint variances, so convex mixing realizes every intermediate variance. Conditional on K=k, choosing a uniform k-subset yields coordinate marginal E K/n=1/2 and pair joint E[K(K-1)]/[n(n-1)]=1/4, proving pairwise independence. Mixing residue-specific constructions realizes every residue law. For n=q^2-1, the half-integer variance obstruction is avoided by parity and grid spacing, while the upper variance bound holds uniformly; at n=q^2-2 the stated residue makes m half-integral and requires variance at least 1/4>n/(4q^2). Fresh exact-rational checks for q=2,...,20 reproduced both the full threshold and the forbidden boundary residue.

## originality

PASS

Benjamini--Gurel-Gurevich--Peled use the classical moment problem to study Boolean events under k-wise independence, and Ramachandra--Natarajan optimize tail/union probabilities of Bernoulli sums under pairwise independence. Neither inspected full primary source treats support of the Hamming weight in one residue class or the exact full-simplex threshold for K mod q. Resultary returned nearby pairwise-independent occupancy and rare-sum results but no theorem implying the q^2-1 modular threshold.

## value

PASS

The law of a Hamming weight modulo q is a natural global statistic under limited independence. The theorem gives both an exact residue-vertex feasibility criterion and a sharp all-q eventual threshold, together with an explicit exchangeable construction. This is a reusable finite moment classification rather than a routine tail estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
