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

For compact invariant mu in the strictly positive quadrant and Q=xy^gamma, use arbitrary C1 one-coordinate antiderivatives F(x),G(y). Stationarity E[L F]=E[F_x(x)(1-Q)]=0 and E[L G]=alpha E[G_y(y)(Q-y)]=0 for all continuous tests gives conditional E[Q|x]=1 and E[Q|y]=y. Since x,y>0 derive E[y^gamma|x]=1/x and E[x|y]=y^(1-gamma), mean EQ=Ey=1, Cov(x,Q)=0, Cov(y,Q)=Var(y). The identity Q=1-xdot=y+ydot/alpha and E[ydot|y]=0 give E[xdot^2]=Var(Q)=Var(y)+alpha^-2 E[ydot^2]. If either speed-energy vanishes, invariant compact complete trajectories with a frozen x or y satisfy scalar linear equations and only equilibrium (1,1) remains. Strict Jensen on convex y^(1-gamma) and y^gamma yields E[x]>1 and E[1/x]>1 for every nonequilibrium compact stationary measure. These opposing moment inequalities force positive mass on x<1 and x>1, while Ey=1 and nonconstant y force both y sides. Strict activity terms yield 0<Corr(y,Q)<1 and its exact formula. For any nonconstant periodic orbit its invariant time measure crosses each level at least twice by continuity. Independent exact rational checks confirmed the two flux-speed algebraic identities; statistical conditional/equality cases are analytic, not inferred from the finite checker.

## originality

PASS

The 1968 original and modern rigorous Selkov phase-portrait work establish kinetic model, equilibria, cycles and global orbit behavior; the two stationary conditional regressions, exact variance-energy identity and strict invariant-measure straddling are different claims. Another published Selkov mass-balance result studies a different two-parameter polynomial model and does not imply these precise Q=xy^gamma conditional laws.

## value

PASS

The result supplies model-exact, all-stationary-measure constraints stronger than pointwise nullcline/equilibrium existence: calibrated nonlinear reaction flux on both coordinate fibers, an exact decomposition of time-dependent fluctuation activity, and orbit crossing constraints for every non-equilibrium compact invariant measure. These are natural structural diagnostics in chemical oscillator dynamics, not arbitrary parameter slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
