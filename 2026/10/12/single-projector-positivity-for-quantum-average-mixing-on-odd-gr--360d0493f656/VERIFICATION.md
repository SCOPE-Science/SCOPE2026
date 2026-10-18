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

For vertices k-subsets of [2k+1], the signed transversal ψ(X)=product_i(1_{a_i in X}-1_{b_i in X}) is an eigenvector Aψ=(-1)^kψ: complementary transversals contribute sign (-1)^k, and nontransversal input either has no disjoint transversal or two cancelling signs. Inclusion subspaces U_j from j-subset indicators yield a chain and nonzero orthogonal V_j; the S_(2k+1) commutant has dimension k+1 by intersection-size orbitals. The k+1 mutually orthogonal invariant projections therefore exhaust the commutant and show V_j are inequivalent irreducible modules. Explicit cyclic disjoint-pair products h_j∈V_j have nonzero overlaps <ψ²,h_j>: 2^k (j=0), 2^(k-1) (j=1), 2^(k+1-j) (2<=j<=k). The cyclic sign expectation is 2^(1-m) for even cycle length m, with extra independent mean 1/2 for odd j. Hence the permutation orbit of ψ² spans all modules, implying W∘W spans the entire vertex space, so the Gram expansion E∘E=sum_{p,q}(u_p∘u_q)(u_p∘u_q)^T is strictly positive definite. Other projectors add PSD Schur squares, so average mixing has full rank binom(2k+1,k). The proof handles k=1 and all k, not just tested k<=6.

## originality

PASS

Coutinho–Guo’s full primary survey §4.1 poses positive definiteness/full rank for primitive distance-regular graphs as Open Problem 4.1, with only the general formula sum of projector Schur squares. The odd-graph family is a natural primitive distance-regular subfamily. Existing Johnson-scheme/Krein methods and finite Johnson J(n,3) cases supply foundational mathematics but no inspected unbounded-k strict single-projector statement; the explicit signed-transversal orbit proof bridges this gap.

## value

PASS

A uniform all-size full-rank theorem on a natural unbounded distance-regular family settles a nontrivial subfamily of an explicitly documented quantum-walk average-mixing open problem. Its single-projector Schur positivity is stronger than the final rank statement and structurally useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
