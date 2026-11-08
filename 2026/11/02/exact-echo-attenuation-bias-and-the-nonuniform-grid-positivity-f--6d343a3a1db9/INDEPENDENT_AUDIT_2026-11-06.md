# Independent mathematical audit

## correctness

PASS

On the line with bounded initial constant m, the plane-wave ansatz gives G'=g and H'=G^2; exact subflows produce right endpoint R and left endpoint L. For arbitrary positive h_j with q_0=q_N=0, integration and summation by parts give R-I=E+J and L-I=E-J. Independent exact arithmetic for h=(1,2,1), q=(0,2,1,0) gives I=19/3, R=6, L=9, so right splitting underattenuates. The interior q_i can be chosen arbitrarily, proving order equality for all echoes iff every neighboring h_i agrees. Explicit expansion gives 3(R-I)=v^T T_R v and similarly T_L, and the irreducible tridiagonal PSD criterion uses all strict proper leading minors and a nonnegative last determinant, with the stated recurrence. This covers N=2 boundary, all real echo gradients, and all positive durations; it does not imply a general full-solution or non-echo convergence theorem.

## originality

PASS

Classical trapezoidal quadrature and exact gradient phase accumulation are known. Kaltenbacher–Muñoz–Thalhammer study general first-order Lie/Trotter errors for non-autonomous Bloch–Torrey. Neither their accessible general convergence statement nor the older spin-echo abstract determines the exceptional second-order echo observable, universality of equal orders on uniform grids, or the sharp arbitrary-mesh PSD sign criterion. Best-of-knowledge PASS, with specialized older NMR priority risk.

## value

PASS

The sign of echo-signal bias and when opposite Lie orders agree are concrete observables for MRI gradient timestepping. A linear-time semidefinite test and the three-step counterexample show the two-step neighboring-ratio safeguard is not sufficient: useful precise design information beyond a routine local quadrature exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
