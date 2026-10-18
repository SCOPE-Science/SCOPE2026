# Independent mathematical audit

## correctness

PASS

The actual system is xdot=a*y, ydot=x+z^2, zdot=b+c*x+d*z with a,d<0, c!=0. Direct independent SymPy differentiation confirms Q=z-c*y satisfies Qdot=Delta/(4c)-c(z-d/(2c))^2. For Delta<0 it drifts at nonzero uniform speed, impossible on any bounded forward-complete orbit; for Delta>=0 equilibrium roots z=(d±sqrtDelta)/(2c) produce compact singletons. At Delta=0, monotonic bounded Q on a bounded forward orbit and the invariant zero-derivative locus z=z* force x=-z*^2, y=0, yielding global-on-bounded-orbits convergence and unique compact two-sided invariant set. Invariant measures satisfy E[(z-z*)^2]=Delta/(4c^2). Linearization at equality has lambda(lambda^2-d lambda-a) with two strictly stable roots. Quadratic center graph v=-(d/c)u-u^2+O(u^3), w=(d/a)u^2+O(u^3) yields udot=-c u^2+O(u^3); one-sided convergent center trajectories obey t*u ->1/c, and standard stable-foliation tracking transfers this to all bounded convergent orbits except the strong-stable set. Boundary case c<0 and strong-stable exponential decay handled. No claim about solutions escaping to infinity.

## originality

PASS

Best-of-knowledge comparison against the same primary mathematical object, stronger theorems, equivalent reductions, exact tables and indexed related results finds no previously established result implying the full final statement. Searches alone are not novelty proof. Most relevant full primary texts were read where accessible; restricted sources and mathematical priority uncertainties are named below.

## value

PASS

For a well-known numerical bifurcation model where the source distinguishes equilibria from unproved solution boundedness, identifying the exact discriminant threshold for any compact dynamics, rather than merely the number of equilibria, is mathematically informative. The unique critical stationary law and universal trajectory-level 1/t relaxation outside a codimension-one center direction describe the phase boundary and are meaningful in bifurcation theory. Both sharpness and scope are natural; no general chaos existence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
