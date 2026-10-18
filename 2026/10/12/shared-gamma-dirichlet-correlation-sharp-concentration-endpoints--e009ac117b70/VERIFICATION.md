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

Independence of normalized Gamma directions and Gamma totals yields X=RW+(1−R)P,Y=SW+(1−S)Q, hence Cov(X,Y)=E[RS](diag(mu)−mu mu^T)/(sc+1) and rho=(c+1)E[RS]/(sc+1). Exchangeability gives s−rho=(c+1)E[(R−S)^2]/(2(sc+1))>0; common T gives Cov(R,S)=Var(E[R|T])>0 and the strict lower bound. c→infinity uses law of large numbers for Gamma totals. At c→0, −c log Gamma(pc,1) converges to Exp(rate p); the shared-total win in the three-way race has probability s/(2−s). Independent small-shape Dirichlet directions converge to categorical vertices with law mu; shared common direction chosen by both precisely on the shared-total win event, giving the stated joint categorical mixture. Independent 120000-draw Monte Carlo diagnostics at s=0.4,c=.1,.5,3,50 yielded empirical correlations .262,.296,.356,.396, matching predicted interval and endpoints .25,.4; stochastic diagnostics are NOT the proof.

## originality

PASS

The 2023 full accessible METRON article by Trick–Rothkopf–Jäkel constructs the same six-Gamma equal-marginal beta/Dirichlet coupling and computes exact product moments/covariances. Section 2.4.3 Eq. (33) proposes a linear shared-fraction approximation, and explicitly leaves its accuracy as an open problem. Section 3 states the correlated Dirichlet construction but no small-concentration categorical joint weak limit or universal strict s−rho bias sign. These new endpoint, strict-bias and coupling laws are more than naming the common model; the preexisting full moment formula can in principle be specialized but the nontrivial small-shape Gamma-race asymptotic is not a quoted corollary.

## value

PASS

The parameter s is frequently interpreted as the desired correlation; the strict finite-concentration overestimate and low-c endpoint s/(2−s) provide an exact calibration boundary. The explicit shared/independent categorical limiting coupling explains loss of calibration in sparse Dirichlet models and is a reusable distributional result, not merely a finite Monte Carlo observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
