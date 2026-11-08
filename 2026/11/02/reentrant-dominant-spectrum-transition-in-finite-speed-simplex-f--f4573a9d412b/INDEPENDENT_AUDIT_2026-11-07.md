# Independent mathematical audit

## correctness

PASS

PASS: For N>=2 and ambient d>=N-1 at a resting regular simplex, the base relative velocities vanish. Derivatives of distance-dependent delays and communication weights multiply zero base velocity differences, so the linear disagreement equation is w_dot=-(N-1)a w-a w(t-tau), a=(1+D)^(-p), tau=D/c. Its characteristic roots are -(N-1)a+W_k(-q exp((N-1)q))/tau. The dominant branch changes from two real roots to complex conjugates at q=W0((N-1)/e)/(N-1), and all disagreement roots have strictly negative real part. Differentiating q(D)=D/[c(1+D)^p] yields the exact one/two/zero crossing cases and c threshold for p>1. Asymptotics q_N~logN/N give D-~c logN/N, D+~(N/(c logN))^(1/(p-1)); p=0 limiting damping rates follow from the scalar characteristic equation. Independent high-precision calculations checked q_N and representative two-crossing parameter regimes; these cannot prove all N. Neutral position and uniform-velocity modes explicitly excluded from exponential stability.

## originality

PASS

PASS best of knowledge with method prior acknowledged. Haskovec and Rodriguez Cartabia define the precise finite propagation speed model and prove flocking by different methods; older papers cover fixed reaction delays and Lambert-W spectral tools. The combined geometric stationary-simplex double transition and population-size scaling were not implied by the inspected source statements. A general delayed consensus characteristic-root theorem may contain this scalar case.

## value

PASS

PASS: The sign of a dominant linearized mode (real versus nonreal, while still damped) controls qualitative relaxation and is motivated in communication-delay flocking. Complete nonmonotone distance/speed threshold classification at p>1, including degeneration at tangency and N scaling, is an interpretable precise invariant and distinguishes spectral oscillation from nonlinear instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
