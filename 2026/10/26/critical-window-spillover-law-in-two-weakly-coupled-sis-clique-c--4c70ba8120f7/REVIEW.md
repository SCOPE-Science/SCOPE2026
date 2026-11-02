# Independent mathematical audit

## correctness

PASS

For r>s>=2, 0<delta<1, beta=delta/(s-1), strictly positive admissible within- and cross-transmission, the deterministic independent-state SIS map F_i=1-(1-(1-delta)p_i) product_j(1-b_ij p_j) is monotone and strictly subhomogeneous on positive vectors. Its irreducible Jacobian at zero has Perron root above 1 via the supercritical core, giving a positive lower iterate and F(1)<1; uniqueness by scaling and attraction from every nonzero input follow from strict subhomogeneity, ordered monotone iteration, and eventual positivity. Permutation symmetry reduces to x,y; core x tends to unique x*>0. Satellite fixed-point expansion near kappa=1 is 0=B*eps+delta*(kappa-1)*y-q*y^2+o(eps+abs(kappa-1)*y+y^2), with q=delta*(1-delta)+delta^2*(s-2)/(2(s-1))>0 and B=r*beta*x*>0. Its unique positive root yields y~sqrt(eps)*Z(c) when kappa=1+c sqrt(eps), including critical and subcritical limits; supercritical satellite tends to its isolated nonzero equilibrium. First core-equation expansion gives x-x*~s*beta*(1-x*)/(1-f_r_prime(x*))*eps*y. Independent decimal bisection on (r,s,delta)=(3,2,1/2) eps=1e-6 compared window c=-2,0,2: observed y/sqrt(eps) 0.929345,2.138643,4.917651 versus limiting 0.929777,2.140933,4.929777. The stochastic finite-state SIS process is not covered.

## originality

PASS

Dung and Phuc 2026 establish homogeneous discrete-time product SIS threshold comparisons. Bonaccorsi et al establish weakly coupled communities for continuous-time polynomial NIMFA, a different update law. Both provide predecessor model and general motivation, but inspected statements do not contain the exact discrete product-map critical window, its parameter constants and core feedback equivalent. General forced-transcritical/saddle-node sqrt scaling is standard, not claimed new. A matching specialization in wider epidemic mean-field literature remains a priority risk.

## value

PASS

Near-critical infection spillover is a naturally significant boundary for community-level deterministic epidemic equations: explicit crossover Z(c), the correct sqrt(eps) scale, and global uniqueness/attraction yield quantitative conclusions beyond qualitative spectral threshold statements. Applies to precise specified nonlinear product update, not public-health forecasts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
