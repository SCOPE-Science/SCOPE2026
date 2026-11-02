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

Under three named independently Bernoulli(1/2)-approved candidates and two seats, for each omitted c every 1-cohesive subgroup for a committee must consist of c supporters unless all members already approve an elected candidate. With quota q=ceil(n/2), letting H_c count c-supporters with committee utility <=1, P(H_c>=q)<=exp(-n/32) by Hoeffding because E H_c=3n/8. On H_c<q, if N_c>=q the worst q-member coalition uses all H_c deficient supporters and then two-utility voters, yielding total utility 2q-L_c, so 1-cohesive AJR fails iff N_c>=q and L_c>q. Two-cohesive groups require all n voters and unanimous approval of a common candidate pair, an event at most 3*4^(-n). Thus simultaneous committee failure reduces with exponentially small error to six inequalities in (N_1,N_2,N_3,L_1,L_2,L_3). Enumerating eight equally probable ballots independently gives per-voter covariance Sigma=(1/8)[[2I,3I-J],[3I-J,5I-J]], determinant 2^-16>0, so the multivariate CLT and continuity yield P(exists AJR) -> 1-P(G_1,...,G_6>0). The bivariate submatrix correlation 1/sqrt2 has first-quadrant probability 3/8 and hence each committee succeeds with probability 5/8, expected total 15/8. Independent exact ballot covariance and finite-profile checks plus numerical Gaussian orthant integration gave ~0.98403; the decimal is not a certified interval. No finite search substitutes for the CLT.

## originality

PASS

Han–Tao–Xia–Zhang–Zhou (arXiv:2510.18718, SODA 2026) treat the critical two-seat random-AJR boundary and show both existence and nonexistence have nonzero limiting probability; their Theorem 2.2 and Section 5 give neither this three-candidate explicit six-dimensional Gaussian covariance cone nor fixed-committee success 5/8. The current claim is a genuinely quantitative minimal three-candidate refinement, not the broader qualitative phase diagram; best-of-knowledge PASS with residual risk that a more general published polyhedral CLT has this as an implicit specialization.

## value

PASS

The critical p=1/2, two-seat case is the natural nontrivial phase boundary for randomized approval representation. An exact six-dimensional cone law for the smallest three-candidate instance, its covariance, and the fixed-committee 5/8 benchmark quantify the boundary instead of a mere bounded-away-from-zero dichotomy. The result is a useful precise reference point for larger-candidate asymptotics and probabilistic social choice, despite its narrow natural slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
