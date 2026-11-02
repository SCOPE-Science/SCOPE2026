# Independent mathematical audit

## correctness

PASS

For a strictly positive initial infection and fixed u in [0,1], the physical final-size root s=S0 exp[-R(S0+I0-s)] is unique: the concave residual is positive at A=I0 and negative at A=S0+I0, with derivative negative at its crossing. Thus 0<y=R s<1, A_R=A s/(1-Rs), Q=A/gamma, and Q'/Q=(g_*(u)-y b/(1+bu))/(1-y). At and to the right of the clipped minimizer u_R of R, g_*>=b/(1+bu), giving Q'>0 (strict). At an interior u_R, Q'(u_R)>0, so every global Q minimizer lies strictly to the treatment-heavy left. Peak monotonicity in R requires S0 R(u)>1 throughout. For beta0→∞, uniform s<=S0 exp[-R I0] yields uniform y→0, making Q strictly increasing throughout. The exact beta0=30, S0=.9,I0=.1,b=g=gamma0=1 inequalities establish u_Q=0,u_R=.5; 297 independent finite-difference/implicit-derivative checks corroborate but do not substitute for the analytic proof.

## originality

PASS

The exact two-intervention parameterization, peak objective and interior u_R are published by Maity et al.; the SIR final-size relationship and infectious area under curve also predate this claim. The surviving assertion is the universal strict ordering of optimum for time-integrated I against the R/peak optimizer and high-beta boundary optimum under a *shared constant budget that changes recovery*. Maity's Appendix B computes dI_peak/du, not d(A/gamma)/du; Sereno's Sec.3 ties cumulative I to final size with a dimensionless fixed recovery scale, but does not compare a pair of budget-coupled beta and gamma. Qualified best-of-knowledge originality, not a claim of a new SIR final-size formula.

## value

PASS

Peak inpatient prevalence and total infected person-time are independently motivated, distinct resource objectives under the same concrete fixed allocation. The global strict ordering across every positive parameter quadruple with interior R optimizer, the uniform high-transmission switch to all-treatment, and an exact rationally bounded counterexample are substantive comparative-statistics conclusions; they clarify when optimizing peak does not optimize cumulative burden. No actual public-health prescription is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
