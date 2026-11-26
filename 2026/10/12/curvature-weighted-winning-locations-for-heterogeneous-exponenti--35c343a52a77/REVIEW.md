# Independent mathematical audit

## correctness

PASS

Put L=log n and u_n=b_n+y/r_*. At a fixed height y, the exponential tail is sqrt(L)e^(-y)/(nK) times exp[-r''(t_j)z²/(2r_*)](1+o(1)) at t_j+z/sqrt(L), uniformly on compact y,z sets. The shifted lattice has mesh sqrt(L)/n; the quadratic lower bounds at the minima give summable Gaussian majorants and the positive rate gap on their complement gives o(1) total tail mass. The all-site tail sum tends to e^(-y) while the maximum site tail tends to zero, so the product of the CDFs converges to exp(-e^(-y)). At any compact height window the exponential densities are on their positive support for all sufficiently large n. In the exact winner density the all-other-sites product has the same limit uniformly in the removed index and the factor r(i/n)/r_* tends to one on compact rescaled valley windows. Integrating the resulting compact-window density yields the Gaussian mixture times the Gumbel density. The limiting density has total mass one; equivalently the union bound at y=-A and the Gaussian tail control exclude escaping marks. This gives joint weak convergence, including the single-valley case and nearest-minimum ties. No result outside the stated nondegenerate interior-minimum independent exponential setting is audited. The frozen verifier was inspected, not executed. An independent finite diagnostic, `python3 -I /workspace/checks/1.py`, integrates the exact finite-row valley winner densities on [-5,14] for the displayed two-valley example. First-valley masses were 0.6035764 and 0.6038021 at n=4000 and n=32000 versus limiting 0.6043561, with >0.999999 of height mass in the window; this is not a convergence or rate certificate. See /workspace/checks/1.log.

## originality

PASS

The supported distinct claim is the joint marked limit with a shrinking Gaussian location scale, quantitative curvature weights and specified centering for a fixed smooth heterogeneous exponential rate. The closest inspected winner theorems impose different assumptions and do not give this conclusion as stated. The closest catalogue analogue has a different stochastic model and is not mathematical coverage. This is a best-of-knowledge verdict, not a priority certification.

## value

PASS

Several equally favorable sites give a macroscopic ambiguity not resolved by the marginal Gumbel theorem. The result identifies the winner's probabilities across valleys, spatial uncertainty within them and independence from height in one common normalization. The exact curvature constants distinguish profiles with the same minimum rate and are useful in the natural heterogeneous-winner problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
