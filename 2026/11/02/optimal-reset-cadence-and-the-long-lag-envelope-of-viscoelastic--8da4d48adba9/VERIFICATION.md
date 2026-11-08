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

For stationary linear two-coordinate Langevin system dX=(Q−X)dt+sqrt(2)dW, dQ=g(X−Q)dt+sqrt(2g)dB with independent Poisson rate-r resetting only X to 0, generator equations yield exactly U=2(g+r+1)/(r(g+r+2)), V=(2g+r+2)/(r(g+r+2)) and Z=(r+2)(g+r+1)/(r(g+r+2)). Constant-rate pre-reset Palm sampling gives the same U,V. Matrix exponential e^{Mt} at Exp(r) waiting times gives event-chain regressions E[Y_{j+1}|Q_j]=bQ_j, E[Q_{j+1}|Q_j]=aQ_j with b=1/(r+g+1), a=(r+1)/(r+g+1). Iteration gives Corr(Y_j,Y_{j+m})=ba^(m−1)V/U, exactly the displayed positive geometric expression. Its r-log derivative has signed quadratic numerator F=−r²+[g(m−4)−4]r+(g+1)[2g(m−1)−3]. For m=1 F<0, for m>=2 a positive root exists iff g>3/[2(m−1)], and then it is the unique global maximum (r*>0); otherwise F<0 all r>0. Direct root expansion r*_m=gm−2(g+1)+O_g(1/m) gives m rho_m(r*_m,g)→1/(2eg). Independent rational verification reproduced all stationary balances, regression ratios and derivative polynomial on several positive-rate/g parameter grids. Simulations are not used for infinite proof.

## originality

PASS

Best-of-knowledge originality PASS based on direct comparison of exact statements, hypotheses and implications. Prior model ingredients and general lemmas are credited; no inspected full-text theorem establishes the precise additional classification. The named inaccessible and abstract-only comparisons remain risks, not proof of priority. Known stationary moments alone are not a formula for Cov(Y_j,Y_{j+m}), which needs the event-to-event conditional regression of the unreset bath. Once that regression is derived, the derivative sign quadratic and optimized 1/m envelope are further mathematical consequences absent from the compared stationary-law results.

## value

PASS

Different observables of a nonrenewed viscoelastic bath have different memory properties. An exact pre-reset event-indexed correlation sequence, unique reset-rate bifurcation and optimal algebraic 1/m envelope reveal the effect of tuning reset cadence against an unreset bath time scale; the distinction from fixed physical-time autocorrelation and full renewal is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
