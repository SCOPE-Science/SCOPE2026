---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For ordered normalized horizontal coordinates, integrating the vertical difference between each quadratic secant and the parabola gives area/H=s^3-sum(gap^3), H=a*l^3/6. The n-2 interior order statistics conditioned on extremes produce m=n-1 Dirichlet(1,...,1) spacings; the free sample range has Beta(n-1,2) independent of internal normalized gaps. Direct Dirichlet rising-factorial calculations give E[Z]=6/[n(n+1)], E[Z^2]=36(n+18)/[n(n+1)(n+2)(n+3)(n+4)] and the stated variances; beta third/sixth moments give the full free variance polynomial. The two extreme deficits n*T_(1) and n*(1-T_(n)) converge jointly to iid exponential(1), hence n(1-S^3)->3 Gamma(2,1). Exponential Dirichlet representation gives a bivariate CLT for (mean E, mean E^3), delta-method gradient (-18,1), variance 324+684-648=360; exact range/shape independence yields the joint independent Gaussian correction. All n>=3, arbitrary affine graph terms and a>0 survive normalization; finite tests are not limit proofs.

## originality

PASS

Compared complete-closed-boundary CLTs, polytopal-boundary asymptotics, and perturbed spherical parabolic hull processes with the exact open-parabola horizontal-sampling model. Classical uniform-order-statistic, beta and Dirichlet tools are acknowledged; no inspected primary result directly entails both finite exact area laws and the two independent limit mechanisms. Priority remains qualified against hidden conic-arc gap calculations.

## value

PASS

Fixing versus not fixing endpoints is a canonical sampling-design choice for convex-boundary approximation. The exact beta-Dirichlet coupling separates endpoint uncertainty from interior spacing noise and explains the non-Gaussian order-n^-1 missing-area law versus order-n^-5/2 centered Gaussian fluctuations; complete finite-size moments quantitatively support that structural difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
