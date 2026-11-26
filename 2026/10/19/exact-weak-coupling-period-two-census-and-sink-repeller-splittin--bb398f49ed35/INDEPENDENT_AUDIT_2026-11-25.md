# Independent mathematical audit

## correctness

PASS

In real phase space the return equation forces opposite y coordinates; zero would force both x coordinates to vanish and contradict the first recurrence. Ordering by positive y=t makes x_0<0<x_1 for k<1, and the two linear x equations at a=1 give x_0=-t and x_1=1. The remaining recurrences are exactly the two displayed scalar equations, both necessary and sufficient. Within the sine wedge the amplitude can only lie in [b/(1+k), b/(1-k)]; on [0,b/(1-k)] the derivative of t(1+k sin(z+t)) is at least (1-3k)/(1-k)>0 and the endpoint values bracket b. This exhausts the real orbits modulo simultaneous translation, including the one-phase wedge edges. The fixed-point equations are inconsistent. At b=1 the simple unperturbed roots are 1 and exp(±iπ/3). Taking the eigenvalue derivative and using the product determinant gives slopes 2 cos z and (sin 1+cos 1-1)cos z/2 for the real root and conjugate-pair modulus, respectively, so the claimed hyperbolic types and their local continuation follow. Independent Jacobian recomputation agrees; at k=0.01 the return moduli were about (0.979720,0.998211,0.998211) at π and (1.002020,1.002020,1.019727) at zero. The frozen verifier was inspected, not executed; the finite sample does not prove the parameter theorem.

## originality

PASS

The same map and absence of fixed points are known; the exhaustive low-gain phase and amplitude classification and the opposite hyperbolic types are not established by the closest inspected assertions. No equivalent claim was established in the bounded comparison.

## value

PASS

The exact census distinguishes no orbit, the wedge-edge orbit, and two interior orbits globally, independent of any choice of numerical basin. A repelling cycle can evade ordinary forward simulations; showing its robust coexistence with a sink in this fixed-point-free map gives additional dynamical information. The wedge is valid on the stated low-gain range, while stability is only local in parameter near sufficiently small central-line gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
