# Independent mathematical audit

## correctness

PASS

The stable linear trap gives a unique stationary coordinate, with bounded active part. I independently computed the moments by integrating over ordered past times, expanding the cosine product as Fourier sign words. Uniform angular phase imposes zero total frequency; independently distributed angular increments give a factor 1/(kb+j^2+iuj) for each gap, where j is the tail frequency, k its tail length, and u is the scaled angular drift. The resulting even-moment combination equals the claimed rational sixth cumulant exactly. Its denominator is positive. Independently recomputed the resultant factorization and root count (one root in (0,1/2), in (11/25,9/20)), the positive shifted coefficients excluding zeros for b>=1/2, and the two positive roots at b=1/10. Strict convexity, positivity at x=0 and the positive quartic leading coefficient prevent changes in the number of positive roots except by collision; on compact b-intervals away from zero, roots cannot escape to infinity. There must therefore be exactly one positive double-root collision. Exact Taylor coefficient bounds give Q_x(b,6)<0<Q_x(b,8) throughout the isolating b interval. Refinement gives (0.4475510940308399394...,6.835392739927954179...). Both simple roots of the weak-trap boundary quadratic continue from b=0. Rotation by pi centers the scalar law; no reflection symmetry of the full torque-driven dynamics is needed. The added independent stationary OU coordinate is Gaussian, hence invisible to the sixth cumulant. Replay: python /workspace/branches/independent-continuous.py swimmer.

## originality

PASS

The known torque-driven trapped model, moment methods, and fourth-order reentrance are not new. The supported distinction is the evaluated stationary sixth Cartesian cumulant and its full sign classification, including the unique finite-confinement collision and weak-trap endpoints. No inspected prior source supplied an equivalent classification.

## value

PASS

The previously observed fourth-order reentrance raises a concrete higher-order question about non-Gaussian stationary fluctuations. The sixth order has a different exact negative window and a confinement cutoff that can be used without recomputing a parameter grid. The uniqueness and weak-trap endpoint results add information beyond evaluation of the recurrence at order six, and the invariance under translational Brownian forcing gives the sign criterion a robust interpretation within the model. A zero of this cumulant is not a test of Gaussianity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
