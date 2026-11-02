---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For compact supp(mu) subset {(x,y,z):0<x,y,z<1} and theta on R/pi Z, log x,log y,log z are bounded C1 on a neighbourhood of the support; invariance gives three exact zero drifts. Their pairwise differences yield c(X-Z)=e(Y-X) and A=(c+e)(Y-X)+e(X-Z). Because Q=c²+ce+e²>0, the claimed gaps follow; summing the three gives (3+c-e)(X+Y+Z)=3+A. The phase rotation theta_dot=2omega has unique Haar invariant probability for omega>0; x<1 and gamma>0 imply A>0. For strictly positive full-period periodic orbits the log drifts integrate to zero. Independent SymPy reconstruction from the exact ODE produced five identically zero residuals, nonzero matrix determinant -(3+c-e)Q, face signs and three rational sample checks. Experiments are supporting checks; the proof is analytical.

## originality

PASS

Best of knowledge: the model-specific exact finite-amplitude ratio of two distinct adjacent species means and their strict ordering were not located in the relevant primary sources or independent mathematical-result searches. The derivation relies on standard invariant logarithmic balance, so method novelty is not claimed. No mathematically dominating prior statement for the same forcing architecture was identified; hidden equivalent prior work remains a residual risk.

## value

PASS

The population means are natural observables in a three-species recurrent competition model. Their exact gap ratio is the biologically and dynamically motivated heteroclinic attraction parameter delta=c/e from the primary paper, independent of period, forcing amplitude, frequency or choice of compact-interior stationary law; gamma>0 enforces a definite mean ranking. This exact finite-amplitude model-specific diagnostic is potentially reusable in interpreting invariant measures and recurrent trajectories even though the derivation uses familiar log balances and offers no new attractor existence theorem. It is not merely a normalization or verification result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
