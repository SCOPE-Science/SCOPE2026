---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed formulas (1)–(5). Each prescribed directed k-cycle has probability n^(−k) and fixes exactly k images. A uniform marked vertex is on it with probability k/n, so its indegree in the cycle-weighted law is B_(n−k)+Bern(k/n), independent summands. This is size-weighted by the cycle count, not conditioning on the existence of a cycle. With k=1 this is B_n, explaining vanishing mixed covariances. Merging the residual Bern(p) and Bern(jp) into Bern((j+1)p) changes the PGF by −jp²(z−1)², giving the formula for every score after telescoping and multiplying by n e_(n,k). For the indicators r=0 and r=1 the curvature terms are respectively positive and negative; for r≥3 the ratio b_m(r−1)/b_m(r−2) is strictly below 1/2 whenever the denominator is positive, and the first summand is then strictly positive. For r=2, the reduced curvature P_m decreases strictly with m, so the bracket increments as k increases change sign at most once from positive to negative. The bracket starts positive at k=2 for n≥4, since A_(n−2)(2)=−q^(n−4)(n−3)/(2n); it ends strictly negative at k=n because the tilted indegree is identically one. The polynomial-exponential scalar in (2) has the sign of the bracket under the stated positive factor, including k=n. Small n gives a negative sign for n=2 and zero then negative for n=3. In fact k>2 cannot tie: n²(n−1)q^k=(n−1)^(k+1)/n^(k−2) is not integral, whereas the other term is. For k/n→t, S/n³ tends to (1−t)(1+t²)−exp(−t). The derivative of exp(t)(1−t)(1+t²) is exp(t)t(1−2t−t²), yielding one interior root τ≈0.58472438648, and the finite switch traps κ_n/n between any fixed t values bracketing τ. The bundled finite checker was inspected, not executed; no all-n conclusion is inferred from its finite enumeration.

## originality

PASS

The finite length-resolved sign law and its indegree-two crossover are distinct in the priority-relevant sources inspected. Conditioning on a prescribed cycle is elementary; the convex-order inequality itself and the variance mechanism behind the collision-score corollary are specializations of standard Poisson-binomial comparisons, not independent novelty. The arbitrary-score curvature equality is more explicit than those inequalities. A later Resultary record directly matches the degree-two formula and switch, so they are not distinct from that later recorded slice; the later date and the different scope do not establish earlier coverage of this theorem.

## value

PASS

The mechanism distinguishes every indegree class and every cycle length, not merely marginal means, with an exact finite sign reversal and a nonzero scaled cutoff in the only changing degree class. The arbitrary-score identity explains the geometry of that comparison and is reusable beyond an indicator. Macroscopic cycles can be rare; the cutoff is a sign property of the covariance, not a typical mapping transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
