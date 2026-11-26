# Independent mathematical audit

## correctness

PASS

Subtracting the coordinate updates yields (x-y) times a positive factor and gives exactly (1+εr)^2/[(1+εr_x)(1+εr_y)] for U'/U. Its numerator minus denominator is ε[r+ε(r²-r_xr_y)], with the bracket positive for the full |ε|<=1/2 range since r²<r. The estimate |log(1+z)-z|<=z² there gives the stated 4ε² per-step error. Reciprocal total mass t satisfies |t'-(1+t)/a|<=|ε|/a. Iterating gives |t_n-t_*|<=a^(-n)|t_0-t_*|+|ε|/(a-1). Applying the 1-Lipschitz transform 1/(1+t), multiplying by |ε| and summing proves (1) with its precise transient and linear-in-n constants. For fixed s0 the error vanishes uniformly on bounded critical windows, including the floor error, and s tends to a-1 there. Positive initial w=dε^γ gives log U=log(d²)+cτ+o(1) in the window; fixed positive w on the negative side gives log(U/h^(2γ))=log(w²/(1-w²))-cτ+o(1). Inverting gives both claimed profiles. For each threshold, evaluate the strictly monotone limiting profile at the displayed limiting crossing center plus and minus any fixed positive offset; the finite trajectories bracket the threshold for all small perturbations. This proves existence and both scaled first-passage constants without assuming beforehand that the first crossing is in the window. The diagonal is excluded from the logarithm, and ε=0 preserves composition exactly. Fifteen independently written rational spot checks included ε=±1/2 and 0; replay: python3 -I /tmp/opencode/frozen_audit_small_checks.py, clock(). The frozen script was read, not run.

## originality

PASS

The rational competition map and qualitative stability exchange are established. The distinct claim is the global-in-time finite-perturbation bound with explicit transient, and its two-sided logarithmically delayed, time-resolved passage laws for the specified distinct initializations. The strongest accessible identical-model results do not supply this quantitative statement. Relevant inaccessible literature remains a genuine priority risk but does not defeat the available comparison.

## value

PASS

The natural dynamical question is how long a nearly neutral mixture remains apparently balanced before exclusion, or how long it takes to mix in the opposite perturbation. The uniform density-transient control reaches the logarithmically enhanced horizon where an ordinary local stability calculation or inverse-perturbation scaling is insufficient. It gives the actual centering constants and different transition profiles on the two sides, without claiming new equilibrium classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
