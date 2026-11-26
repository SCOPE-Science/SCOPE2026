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

Independently rederived the results by conditioning on the renewal schedule and using Gaussian integration by parts. For any centered jointly Gaussian U,V, E[U V^(2m+1)] = (2m+1) Cov(U,V) E[V^(2m)]. With a reset between observations the conditional covariance is zero. With no reset and initial age a, the conditional covariance is 2Da and the variance ages are a and a+t. Thus the conditional contrast is [2(2m+1)! D^(m+1)/m!] a[(a+t)^m-a^m]. For any reset law, length-biasing and uniform location give E[g(A)1{R>t}]=E[integral_0^(T-t)_+ g(a) da]/mu, with no deterministic-time event atoms even for deterministic T. Expanding the conditional polynomial and integrating term by term gives coefficient 2(2m+1)!D^(m+1)/[mu j!(m-j)!(m+2-j)], exactly the stated hierarchy. Finite E[T^(m+2)] gives the stationary marginal moment and via Hölder both mixed moments. At m=1 this yields Delta=6D²t E[(T-t)_+²]/mu, positive exactly when P(T>t)>0. Stationarity, joint reflection and symmetry of the single degree-two mixed monomial prove the minimal degree claim for those lags. The first derivative of the squared positive-part expectation is -2E[(T-t)_+]; the next right derivative gives 2P(T>t) by bounded convergence of the difference quotients, excluding any atom at t as required. H''_+(0)>0 and normalization recovers the full survival law; Delta'(0+)=H(0) gives positive D after recovering the first two moments of T. Exponential and deterministic examples follow by evaluating the stop-loss moment, with maxima at 1/r and b/3, respectively.

## originality

PASS

Credit exact prior coverage of the Poisson complete-reset fourth-order arrow via the earlier random-amplitude theorem with A=0. Credit established renewal and Gaussian ingredients and do not count parameter information as independent of covariance. The distinct supported contribution is the exact arbitrary-renewal positive stop-loss contrast and lag cutoff, its least-degree two-time interpretation, and the higher odd-crossed moment hierarchy; the strongest inspected Poisson statement does not extend to these renewal quantifiers.

## value

PASS

For a natural irreversible stationary process, the result identifies the first available exchange-asymmetric polynomial statistic and predicts its sign and the exact lags with detectable signal, including bounded, atomic, and non-Poisson renewal durations. The expression gives an interpretable tail-weighted magnitude and a positive hierarchy, rather than simply observing jumps or giving another symmetric covariance formula. Its law recovery is an exact theoretical consequence, not a claim of extra information over covariance or a practical estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
