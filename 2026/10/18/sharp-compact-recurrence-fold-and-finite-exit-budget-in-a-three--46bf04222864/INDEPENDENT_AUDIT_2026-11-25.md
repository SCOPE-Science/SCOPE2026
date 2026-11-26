# Independent mathematical audit

## correctness

PASS

The inverse recovers the first two old coordinates from the new second and third and then divides the first-coordinate residual by δ. Substitution into H=x+(δ−σ)y+δz cancels the y,z terms in H∘F−H and leaves x²+(δ−σ−1)x+α=(x−c)²+ε. On an interval of N steps the increment is at least Nε. For ε>0 the height difference between two points in the cube is at most 2R(1+|δ−σ|+δ); separately H(F^Np)≥H(p)+Nε and H≤(1+|δ−σ|+δ)||·||∞ give the liminf bound and eventual permanent exit. At ε=0, bounded forward orbits have summable squared first-coordinate deviations by telescoping, hence all three coordinates converge by the shifts. For any full bounded orbit the same sum over all integers is finite; both limiting states are the fixed one, so both limiting heights agree and the sum is zero. This applies to any point of F(K)=K by invertibility, not to arbitrary forward-invariant compact sets. Integrating the identity under a compactly supported invariant law gives the moment equation, and the marginal shifts prove Dirac uniqueness at equality. Solving the fixed-point equation gives the stated two fixed points below the fold. This is an exact existence boundary, not a claim that the runtime bound is the optimal finite exit time, or that all trajectories converge at the fold. Replay: RESULT.md lines 39–68 and direct substitution above. The inspected verify.py checks finitely many rational substitutions including δ=0 as a check of the identity only; it was not executed and does not prove the orbit statements.

## originality

PASS

The fixed-point fold and the starting recurrence are exactly Hampton–Meiss's. Their recurrence is a short route to the balance once the height is chosen, but the fixed-point and enclosure theorems do not give global exclusion above the fold or full bounded-orbit rigidity at the fold. The distinct delayed-square map in edd60670a63c uses essentially the same coboundary method and proves parallel global theorems; it neither states nor subsumes this three-dimensional family with arbitrary σ. The supported contribution is the use of the exact height to turn the known fixed-point fold into a global boundary, with critical two-sided rigidity and explicit exit and moment consequences. It is not priority for the map, fold calculation, general telescoping method, or stationary parabolas.

## value

PASS

A local fixed-point discriminant need not decide global bounded recurrence. The exact height settles that distinction for all real linear feedback values in this family and rules out nontrivial compact two-sided dynamics on the entire critical locus. The orbit-by-orbit residence bound is directly quantitative above the fold without any assumption about trapping or local stability. The value lies in these global decisions, not in recomputing the fixed-point locus or asserting optimality of the residence bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
