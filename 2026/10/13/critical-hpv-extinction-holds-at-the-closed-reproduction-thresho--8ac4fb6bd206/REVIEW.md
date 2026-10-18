# Independent mathematical audit

## correctness

PASS

For source six-class standard-incidence HPV ODE on positive-total-population feasible Ω and all rates strictly positive, infected core y=(E,I1,I2) obeys ydot=A0y−(1−S/N)Φ e1, where irreducible Metzler A0 has s(A0)≤0 at R0≤1 and Φ=β1E+β2I1+β3I2. Positive left Perron w gives Ldot=s(A0)L−w1(1−S/N)Φ<0 for y≠0 even at R0=1; LaSalle yields y→0, downstream stable linear A,R→0, S→Λ/d. Stability follows from L control on y, stable downstream filters, and z=Λ/d−S obeying zdot≤−dz+Φ on invariant Ω. Independently checked symbolic A0 determinant and w left-null construction using SymPy, with zero entries first and third identically and middle equal det A0; at R0=1 det=0. Domain N>0 is essential because λ=Φ/N is undefined at origin; solutions with Λ>0 enter N>0 immediately.

## originality

PASS

PASS best-of-knowledge for completing the strict stability theorem of this particular variable-population six-compartment HPV treatment model at the nonhyperbolic equality R0=1. Zhang et al 2020 Theorem 3 only establishes R0<1, with forward bifurcation at R0=1 addressed separately. General Perron-vector epidemic Lyapunov methods (Fall et al 2007; Shuai–van den Driessche 2013) make proof method classical, but their inspected mass-action/multigroup equations are not shown to subsume the present varying N, waning immunity and downstream classes with exactly the source constraints; exact direct coverage remains a priority risk. A SIAM primary full text retrieval via Oxford was blocked by disconnected VPN, and this inaccessibility is not itself a failure.

## value

PASS

Closing a biologically meaningful disease-extinction threshold with global Lyapunov stability at the nonhyperbolic boundary is a motivated model-specific sharp statement beyond strict-subcritical stability; the simple Perron identity has practical threshold significance. It does not purport a new general Lyapunov technique. General prior methods reduce standalone novelty strength and remain a residual value/priority risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
