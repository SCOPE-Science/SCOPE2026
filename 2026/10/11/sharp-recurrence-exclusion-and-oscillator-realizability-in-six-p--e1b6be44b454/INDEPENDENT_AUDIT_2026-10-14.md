# Independent mathematical audit

## correctness

PASS

For all real six coefficients with b4 != 0, the actual RESULT.md defines P=z-b3*y-b2*x-(b7/2)*x^2-b8*x*y and derives L_F P=b4*x^2+(b5-b8)*y^2. I independently differentiated this polynomial using SymPy (zero residual). If b4*(b5-b8)>=0, sP is bounded and monotone on a bounded forward orbit; its compact omega-limit has constant P, hence x=0, and invariance of xdot=y,ydot=z forces the origin. For a bounded complete orbit, alpha and omega limits both origin and monotonicity eliminates nontrivial heteroclinic/homoclinic trajectories. Integrating the Lie derivative under compact invariant mu gives the exact second-moment ratio; on the closed sector x=0 mu-a.e., invariance forces delta at zero. The opposite-sign coefficients b2=-omega^2,b3=b5=b7=0,b8=-beta yield an invariant plane z=-omega^2*x, harmonic cycles at every R>0 with omega^2=-b4/beta. No claim made for arbitrary unbounded initial values, or for existence at every opposite-sign parameter.

## originality

PASS

Best-of-knowledge comparison against the same primary mathematical object, stronger theorems, equivalent reductions, exact tables and indexed related results finds no previously established result implying the full final statement. Searches alone are not novelty proof. Most relevant full primary texts were read where accessible; restricted sources and mathematical priority uncertainties are named below.

## value

PASS

This is a natural coefficient-uniform obstruction problem for the six-parameter family used to produce nine nonhyperbolic numerical chaotic models. The closed sign cone rigorously excludes all compact recurrence, including its boundary, and the explicit opposite-sign harmonic family proves sharp uniform possibility; the stationary second-moment balance gives a new diagnostic for candidate recurrent states. This is structural information not a textbook restatement of local eigenvalues or isolated finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
