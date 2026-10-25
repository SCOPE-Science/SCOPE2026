---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: On f(x)=||x||^2/2 the central difference is z^Tx independent of h; inverse-covariance correction is unbiased for z~N(0,Sigma). Wick gives E[zz^TQzz^T]=2Sigma Q Sigma+tr(Sigma Q)Sigma, so Q_(k+1)=c Q_k+eta^2 tr(Sigma Q_k)Sigma^-1 and tr(Sigma Q_k)=L^k tr(Sigma Q_0). Solving yields the exact stated all-k norm moment for all SPD Sigma. Convex F(B)=sup_{||x||=1,||Px||^2 in [a,b]} x^TB^-1x for B=Sigma^-1/tr(Sigma^-1) permits Haar averaging over O(r)xO(s), giving a GLOBAL block-optimum (not assumed diagonal). Endpoint maximization and positive linear-plus-inverse minimization give the exact three-phase t*, Phi*. For every nonzero x0 the L^k coefficient is positive and L>c>0, proving the covariance-independent asymptotic threshold 0<eta<2/(d+2). Fresh independent code checked 140 SPD symmetrization/moment identities and d=10,r=2,[.8,.9] optimum t=.25, Phi=6.4. Bounded numerical checks corroborate, not prove arbitrary SPD/infinite horizons.

## originality

PASS

PASS best-of-knowledge: the all-SPD, inverse-covariance-corrected, band-adversarial moment criterion is not implied by Ma/Huang isotropically constrained probe variance, Ryabchenko/Qian/Mou control-variate directional hints, or Starnes anisotropic smoothing; same normalized quadratic geometry alone is insufficient. Resultary semantic query finds only different Haar SSD/relaxation objectives. Priority may remain under alternative importance-sampled gradient estimator names; the recent directional-hints manuscript was substantially inspected beyond abstract here, not declared globally noncovering.

## value

PASS

PASS: A sharp three-regime minimax threshold and exact all-positive-horizon risk quantify when directional prior alignment can improve an unbiased stochastic gradient estimate. It also establishes a substantive impossibility distinction: no SPD probe shaping changes the leading mean-square exponent. This is a naturally motivated uncertainty-band optimization rather than an arbitrary covariance recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
