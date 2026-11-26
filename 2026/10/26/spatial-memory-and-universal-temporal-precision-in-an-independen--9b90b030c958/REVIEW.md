# Independent mathematical audit

## correctness

PASS

The frozen formulas are correct for time-averaged occupancy Q_t, not counts of crossings; the repair makes this explicit. Independently reconstructed the local kernel by solving (r-D d^2/dy^2)u=f_x for the bounded free resolvent. Multiplying u by r gives H_x(y)=exp(-alpha(x-y))/2 below x and 1-exp(-alpha(y-x))/2 above x, matching both value and derivative at x. On the three regions below 0, from 0 to x, and above x, the integrals of H_x against the stationary density are exp(-alpha x)/8, alpha x exp(-alpha x)/4, and 3 exp(-alpha x)/8. The last is also the integral against f_x times that density. Subtracting p_x E H_x gives the stated local covariance integral after division by r. Reset independence and monotonicity give 0<=c_x(s)<=p_x exp(-rs); conditional count second moment is at most m^2+m, and conditional L^2 truncation justifies summing covariances. The lag-weight deficit 1-(1-s/T)_+ is between zero and s/T, giving the repaired conditional bound 2m/(r^2 T^2), in the stated sign direction. For the lattice checked both geometric sums and the first geometric moment; the summand derivative is exp(-2v)(2v+3-3exp(v))<0 for v>0. The one-sided lattice endpoints are translates by one index, differing by precisely the v=0 contribution 1/(4r); sum convergence is uniform for u in [0,1]. Summation followed by uniform-phase integration yields 7/(16r beta). Poisson integral variance gives rho/(8 alpha), and the phase moments of m give the frozen shifted-lattice variance and the 1/48 dense limit. All decisive checks were analytic; the frozen checker and its output were inspected only.

## originality

PASS

Pass for the repaired exact configuration-dependent coefficient and its strictly decreasing shifted-lattice phase profile and exact phase spread. The frozen main annealed temporal coefficient has material existing coverage: the local Resultary rate-disorder proof explicitly computes the same fixed-rate spatially integrated lag kernel and obtains 7/32 for its time integral, before the final random-rate average. Campbell's first-moment identity transfers that spatial average to other anchor correlations without a new covariance calculation. The Poisson and uniform lattice phase plateaus are elementary static integrals. The repaired theorem instead evaluates the off-boundary individual-anchor integral and answers a quenched phase question that is not determined by the spatial average; it uses the explicit dependence on anchor distance. No historical priority inferred from catalogue dates.

## value

PASS

The fixed-anchor coefficient measures trajectory noise separately from the annealed static plateau, which was the question motivating the frozen comparison. The repaired exact formula can compare configurations at fixed density instead of giving only their mean. In the natural lattice example the phase law is strictly monotone with nonzero spread 1/(4r) independent of diffusivity and spacing, despite agreement of the spatial average with Poisson. This quantifies the geometry dependence concealed by that average, not just a new way to reproduce the old scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
