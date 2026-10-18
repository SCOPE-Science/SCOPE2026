# Independent mathematical audit

## correctness

PASS

Starting from the exact closed homogeneous SIR equations with beta(t)=beta0 exp(at), set Q=beta S/(gamma N), P=beta I/(a N) for a>0. Direct differentiation gives Qdot=aQ(1-P), Pdot=gamma P(Q-1+a/gamma), a genuine predator-prey Lotka-Volterra system. Its first integral H=gamma Q-(gamma-a)log Q+aP-a log P is conserved. For 0<a<gamma, H is strictly convex and coercive in log coordinates; all non-minimal levels are compact regular periodic curves. dI/dt=gamma I(Q-1); the orbit crosses Q=1 exactly twice, generating one strict maximum and minimum each period iff E>H(1,1)=gamma+a. For E<=gamma+a no interior maximum. Incidence logarithmic derivative at the Q turning points is gamma(Q-1), giving at least one strict incidence peak each cycle in the supercritical case. Periodicity of Q,P and exponential beta give exact S,I,C attenuation e^{-aT}. For a<=0, Q strictly decreases; for a>=gamma, P increases, Q has at most one turning point and I at most one maximum. Independent polynomial conservation and exact exemplar (N=gamma=1,a=1/2,beta0=5,S0=2/5,I0=1/10) checked. Finite computations do not establish global periodicity, which follows from compact regular level sets.

## originality

PASS

The Lotka-Volterra periodicity itself is classical, and state-feedback controlled SIR-to-LV reductions predate this work. However the exogenous single-exponential beta law, exact scaled conjugacy, sharp energy threshold for repeated strict prevalence peaks and attenuation are more specific than earlier general multiwave SIR representability, with no dominating equivalence found after targeted comparison.

## value

PASS

The coexistence of unbounded transmission growth and indefinitely many *strict* yet geometrically decaying epidemic prevalence/incidence peaks in a closed, non-replenished SIR model is a nonobvious dynamical boundary. It demonstrates that a single log-affine forcing segment can generate unlimited mathematical peak count and provides an exact parameter/energy phase classification, which is useful to distinguish structural peak count from statistical wave-complexity claims. It is not merely an LV relabeling because the original physical observables and attenuation are classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
