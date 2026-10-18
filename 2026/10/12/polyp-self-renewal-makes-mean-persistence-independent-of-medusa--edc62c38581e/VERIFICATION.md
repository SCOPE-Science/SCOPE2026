---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For positive initial data, b,b1,d*>0 and nonnegative coefficients, write rP=a−d−sigma1²/2>0. Multiplication of the polyp equation by the positive Itô integrating factor R_t=exp(−sigma1 B1_t+sigma1² t/2) yields a random differential equation whose extra forcing b R_t M_t is nonnegative. The stochastic logistic scalar equation X driven by the same B1 with identical initial P0 is therefore a pathwise lower comparator P_t>=X_t; its explicit solution has log X_t/t→0 and time-average X_t→rP/b1 almost surely. Hence liminf time-average P>=rP/b1 independent of sigma2. Set x=(d*/b)P,y=M and W=x+y. The linear transfer cancels because (d*/b)b=d*, leaving drift (a−d+bc/d*)x−(bb1/d*)x²−b2y²<=A W−k W², k=0.5 min{bb1/d*,b2}. Itô log W has drift <=A−kW plus a continuous martingale of quadratic variation <=max(sigma1²,sigma2²)t, so its normalized martingale tends to zero. Since W>= (d*/b)X implies liminf log W/t>=0, the time-average upper bound <=A/k follows. This establishes the original weighted definition of persistence in mean for any sigma2. Independent exact rational witness reconstruction for original source parameters sigma1=.1,sigma2=1 yields rP=181/1250, polyp mean >=14480, weighted W>=14842/425, medusa corrected growth −813/2000<0; the 2022 source theorem is inapplicable to that witness. No finite SDE simulations are being used as proof.

## originality

PASS

The exact same model and coefficients in Win and Tian (2022/2023) have Theorem3.9 requiring two simultaneous noise-corrected positive growth rates, a−d−sigma1²/2>0 and c−d*−sigma2²/2>0. Direct full-text examination of its model (3), Definition3.8, Theorem3.9 and numerical source parameters confirms that it does not state the one-sided condition. The present proof uses positive coupling and scalar stochastic logistic comparison to remove the medusa-noise condition entirely. Stochastic logistic persistence is classical, and originality is confined to this precise two-stage jellyfish implication with the explicit weighted upper/lower estimates. The earlier paper's flawed-looking subsequent algebra does not itself prove the new conclusion.

## value

PASS

The source model's persistence criterion explicitly made survival conditional on small noise in both life stages; showing source-parameter persistence even when the medusa-only corrected growth is negative answers a structurally motivated qualitative threshold question. This is not merely an algebraic sign correction: it provides a pathwise stochastic comparison and a genuine stage-asymmetric sufficient condition with verifiable quantitative bounds. No claim of sharp necessity, unique stationary law or almost-sure permanence of both components is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
