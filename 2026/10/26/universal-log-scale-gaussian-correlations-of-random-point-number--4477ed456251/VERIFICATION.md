---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The exact pair expansion has deterministic diagonal Ns(1-s) and coefficient 2 per unordered pair. The centered overlap kernel has zero conditional expectation given either point, so only identical unordered pairs contribute to the covariance; their factor is 4*binom(N,2). Complementation gives reduced lengths 0<a<=b<=1/2, and the two overlap lobes give integral a^2*b-a^3/3; centering subtracts a^2*b^2. This gives (1), with bracket >=b/6. For the bridge, set a_s=1_(0,s]-s and let K_s be its circular autocorrelation. Then Khat_s(0)=0, Khat_s(k)=|ahat_s(k)|^2, and the common real white noise has independent complex modes at positive frequencies, with negative frequencies their conjugates. Parseval gives (9) with lambda_k=2*Khat_s(k), and summing their products gives (10) exactly as 2*integral(K_s*K_t), where the integrand denotes the pointwise product. The Isserlis shorthand in line 66 should be read with this Parseval identity: the mixed increment covariance is the cross-correlation of a_s and a_t, not K_s, and its squared L2 norm equals the integral of the product of the two autocorrelations by Parseval. Thus (9) and (10) are jointly valid with the same exponentials. For a fixed linear combination the maximal normalized coefficient is O(sqrt(epsilon_N)), squared coefficients converge in total to the prescribed variance, and absolute cubes vanish. One can truncate the infinite row with vanishing variance tail before Lyapunov; for zero limiting variance Chebyshev applies. A common periodic empirical-bridge approximation gives the two terms in (12) with the asserted rates; after division by s^(3/2) both vanish under (2) for each of the finitely many lengths. Cramér–Wold and Slutsky give the joint limit. The Fourier transform of the two exponentials gives (5); repeated log-lengths give identical coordinates without contradicting positive definiteness on distinct log-lengths.

## originality

PASS

The supported contribution is the exact off-diagonal covariance for two circular lengths and the explicit joint Gaussian log-scale kernel in the stated shrinking-window regime. The closest same-statistic primary source supplies the scalar result, diagonal covariance, common empirical-process coupling and scalar weights; none of the inspected scalar statements identify off-diagonal covariances or joint Gaussianity. Distinct multiscale point-process results concern a different statistic and sampling regime, with different limiting covariances. The closest same-statistic indexed record supplies a one-window higher cumulant, not the mixed-scale law.

## value

PASS

One-scale variances do not describe redundancy or dependence between choices of window length. The finite-N covariance quantifies it exactly across the entire circle-length range; the joint limit captures dependence between nearby shrinking lengths through a nontrivial stationary kernel with an explicit spectrum. This adds a useful multiscale invariant rather than another marginal approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
