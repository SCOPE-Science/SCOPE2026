---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The scalar p-th moment CLT holds for p<2 under Var xi<infinity and for p>=2 under finite p-moment (implied by r=max(2,2p−2)). Hence Y_n(t)=n^(−p/2)|sum_{j<=nt}xi_j|^p are uniformly integrable for each t; iid independent coordinates permit a triangular coordinate WLLN by fixed truncation, variance <=K²/d, then K->infinity. For the published convexity decomposition ||S_m||_p^p=T_m+Q_m, T nondecreasing and Q martingale, quadratic variation has d × d^(−2/p) × d^(−(2p−2)/p)=d^(−1); MZ or Lyapunov bound E|sum_{j<=m}xi|^(2p−2)<=C m^(p−1) proves E Q_n²<=C n^p/d. Doob, finite-grid monotonicity and translated-block controls give uniform pairwise metric convergence, hence GH. No relation d vs n other than d->infinity; 1<p<infinity. The p=2 specialization is explicitly prior.

## originality

PASS

PASS, best-of-knowledge for p!=2. Jin Theorem 1.1 establishes the same GH limit for merely uncorrelated coordinates but assumes a 2p moment; the paper uses bivariate 2p estimates. Stronger coordinate independence here permits triangular WLLN and only max(2,2p−2) moments; this is not a theorem under Jin’s existing hypotheses, and is not implied by the Hilbert-only p=2 finite-variance Wiener spiral. Primary proof read and no equivalent non-Hilbert lower-moment theorem identified.

## value

PASS

PASS. Lowering integrability threshold while keeping arbitrary d(n)->infinity and full uniform metric convergence changes which heavy-tailed coordinate laws are covered; moment 2p−2 has a transparent mechanism from squared derivative in the martingale term. This is a natural meaningful analytic extension, not mere renaming or finite sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
