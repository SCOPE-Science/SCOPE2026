# Independent mathematical audit

## correctness

PASS

Re-audited the narrowed theorem in repairs/5/RESULT.md. The displayed divergence follows from differentiating rP and completing the square; at the maximum allowed mu its zero set is one point, so recurrence exclusion by strictly negative area integral still holds, including a loop through the hyperbolic saddle. The positive-radius equilibrium determinants have opposite signs and the second trace is negative; the axis equilibrium is a sink. If a reversed stable branch stays below sqrt(5), bounded radial forcing allows infinite continuation, and once |z|>1 the sign of the linear height equation traps it there and the positive lower bound for P forces radial growth. Otherwise the branch would be bounded in both directions and the planar limit-set alternatives force a backward equilibrium. Neither forward sink can be a nonstationary backward limit, and the remaining saddle would give a forbidden homoclinic loop. This works separately for both branches. Past sqrt(5) radius is increasing; it reaches sqrt(10) since z cannot diverge at finite time under bounded radial forcing. For r^2>=10, (r^2-5)(21r^2-20)>=19r^4/2, giving reversed radial growth at least (19*mu/42)r^5. This bounds both the remaining time and the integral of r^2 up to the endpoint, so variation of constants yields a finite z_*. Then h=r^(-4) has derivative 4*mu+O(r^-2); integration first gives h comparable to Delta and then h=4*mu*Delta+O(Delta^(3/2)). Integrating the height equation gives the claimed negative coefficient, and the exact identity theta+ez-t=constant gives the positive signed phase coefficient (for e=0 the phase increment is exactly Delta). Both ends going to unbounded radius prove properness; the planar Jordan separation argument and rotation give the stated cylinder and common boundary. The axis is interior to the origin basin. The proof needs no finite trajectory simulation.

## originality

PASS

For the repaired claim only: both complete saddle stable branches have finite backward escape, with the three exact endpoint profiles; properness and the boundary geometry are stated as consequences. The frozen record presented the parameter-wide forward classification as part of its additional contribution. That part lacks independent distinctness: the same-family power-Dulac result establishes the forward conclusion over a larger interval for positive e, and e enters only through the angle identity. The repair removes that forward originality claim and gives explicit credit without inferring priority from same-day catalogue dates. The checked stronger theorem provides recurrence exclusion, not the two-ended backward continuation and endpoint estimates. The finite-time and profile remainder survived the bounded statement and implication checks.

## value

PASS

The surviving theorem quantifies the two complete ends of a basin boundary in a standard polynomial counterexample family, separating backward incompleteness from bounded forward dynamics. It rules out trapping and height escape at bounded radius on either entire branch, and identifies the anisotropic endpoint behavior: diverging radius, finite height, and finite lifted phase. The result is not just the already described separator role or another finite radius plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
