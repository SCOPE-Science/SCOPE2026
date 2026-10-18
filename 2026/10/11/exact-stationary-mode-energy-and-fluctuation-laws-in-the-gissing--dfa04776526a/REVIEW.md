# Independent mathematical audit

## correctness

PASS

Reconstructed the complete polynomial generator for Qdot=mu Q-VD, Ddot=-nu D+VQ, Vdot=Gamma-V+QD. Stationarity of arbitrary single-coordinate antiderivative tests gives E[VD|Q]=mu Q, E[VQ|D]=nu D, E[QD|V]=V-Gamma. The independent SymPy check verifies L((Q^2+D^2)/2)=mu Q^2-nu D^2 and all three signed residual identities. Conditional residual orthogonality yields Var(VD)-mu^2 Var(Q)=E[Qdot^2], Var(VQ)-nu^2 Var(D)=E[Ddot^2] and Var(QD)-Var(V)=E[Vdot^2]. If both Q,D energies vanish, invariance on axis Q=D=0 and bounded complete trajectories of Vdot=Gamma-V force the single atom (0,0,Gamma). Nonzero energies have RMS(D)/RMS(Q)=sqrt(mu/nu); at mu=119/1000,nu=1/10 exactly sqrt(119)/10. Compact support justifies integrations; no sampled orbit is used to prove stationarity.

## originality

PASS

The same-object founding model paper and related fractional-order literature were compared on statement scope. The inspected source material establishes equations, chaotic reversals and parameter regimes, not a located all-invariant-measures conditional-regression or exact fluctuation identity. Related indexed stationary laws use different generators and do not imply this result. Priority is best-of-knowledge, not an assertion that search proves novelty.

## value

PASS

Exact invariant-measure energy locking and orthogonal fluctuation defects constrain meaningful dipole/quadrupole dynamics at the published reversal parameters, uniformly across recurrent regimes; they offer independent consistency tests for stationary simulations. More than a single gratuitous moment calculation: the three conditional laws give structurally useful velocity-variance decompositions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
