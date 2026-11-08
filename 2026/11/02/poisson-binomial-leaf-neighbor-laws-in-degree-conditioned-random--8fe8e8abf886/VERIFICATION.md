---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Deleting the fixed vertex gives a uniform rooted forest on N=n-1 labels with d rooted components and singleton components corresponding to leaf neighbors. Labeled rooted-tree EGF T=ze^T, Lagrange inversion [z^m]exp(jT)=j(m+j)^(m-1)/m!, and the diagonal action of D_N=N+(1-t)∂_t on (t-1)^k yield exactly the stated normalized PGF. The root-preservation lemma is not merely tested: coefficient [(N-k)a_k+(k+1)a_(k+1)] is nonnegative for degree< N, while logarithmic quotient N+(1-t)sum b_j/(t+lambda_j) is strictly decreasing between poles, giving all nonpositive real roots incl multiplicity. Grace-Walsh-Szegő polarization converts the univariate stable PGF to the real-stable symmetric multiaffine joint PGF; Borcea-Brändén-Liggett Thm4.9 yields negative association. The exact two-leaf probability ratio is <1 for 2<=d<=n-2 (including d=2 zero case); forest component sizes realize every claimed support value. Prüfer enumeration independently confirmed all PGFs for n=3..7 and checks sampled roots, not an all-n proof.

## originality

PASS

Best-of-knowledge statement-level novelty after primary-literature and semantic published-result comparison; known general tools/special cases are explicitly carved out. Known general results supply essential implications after establishing a new hypothesis, and do not supply the theorem as a direct named corollary.

## value

PASS

A degree-conditioned leaf-neighbor count is a standard local statistic of uniform labeled trees; exact joint strong Rayleigh dependence is meaningful because scalar expectations and covariances do not imply it. The all-size Poisson-binomial representation and precise feasible support are mathematically nontrivial refinements useful in random-tree concentration and coupling arguments, not an arbitrary small-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
