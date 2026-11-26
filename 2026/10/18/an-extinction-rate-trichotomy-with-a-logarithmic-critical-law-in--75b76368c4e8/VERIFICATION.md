---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The independent ratio calculation gives dv/dt=v^2 G and dr/dt=rv B, with r=u/v, G(r,0)=beta*r-c and B(r,0)=c-alpha+(alpha/A-beta)r. In the subcritical case r_* lies strictly below A and c/beta; choose R between it and min(A,c/beta). At or above the threshold choose a small R with B(R,0)<0; for equality, B(0,v)<0 for v>0 and the strict derivative B_r(0,0)=-k extends negativity to the wedge. For sufficiently small delta the top v=delta and side r=R point inward, G<=-d_0, and u decreases since R<A. Smoothness and the per-capita form preserve positive solutions for all t; -c*v^2<=v'<=-d_0*v^2 gives both extinction and tau=integral v dt tending to infinity. Subcritically B is eventually uniformly positive for r<=r_*-epsilon and uniformly negative for r>=r_*+epsilon, so solutions enter the smaller band by comparison for log r and cannot leave; r tends to r_*. Integrating (1/v)' and multiplying by r gives the two stated coefficients. At equality r decreases to zero, tv tends to 1/c and tau is asymptotic to log(t)/c. In tau-time v decays exponentially and B=-kr+O(v). Multiplying r by exp(C*integral v d tau) and comparing to w'=-kw^2 gives r>=const/(1+tau), so (1/r)'=k+O(v/r) tends to k. This proves the critical coefficient for physical time. Above equality both r and v decay exponentially in tau. Direct cancellation makes the physical-time derivative of log(u/v^(alpha/c)) of order u+v^2, integrable because dt=d tau/v. Its integral converges to a finite real value, yielding a strictly positive limiting amplitude and the stated exponent. Independent exact symbolic checks verified the cancellation, subcritical constants and both equilibria in the coexistence witness (small equilibrium determinant -1/891; large equilibrium trace -11/100, determinant 3/625). Along the invariant prey-only axis every positive initial u<1 increases to 1, so the origin is not Lyapunov stable on the full quadrant.

## originality

PASS

The same reaction law is prior work, but the supported distinct claim is its small positive extinction sector for all alpha>0 under beta*A>c and the sharp physical-time rate crossover at alpha=c. The source's positive-equilibrium Hopf/Turing analysis is not an origin stability or rate theorem. A closely matching discrete power/log trichotomy is a distinct system, not identified with this ODE.

## value

PASS

The result answers a natural question left by the original pattern-formation analysis: what very small populations in this model can do near the degenerate boundary equilibrium. It separates the existence of an extinction sector from the threshold for its decay law and identifies a sharp logarithmic law and an amplitude that remains nonzero above threshold. The exact example proves that sectorial extinction can coexist with a locally attracting positive state in the same unharvested model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
