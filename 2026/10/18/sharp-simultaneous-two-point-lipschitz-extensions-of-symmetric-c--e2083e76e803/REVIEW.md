# Independent mathematical audit

## correctness

PASS

The metric conditions check the three triangle types: within-class sides t are at most both 2 and 2a; cross-class apex triangles require b-a<=1<=a+b; and triangles with both apices require b-a<=h<=a+b. Bounded extension preserves constants. Averaging conjugates by the independent class permutations and the class/apex swap preserves extension and does not increase the seminorm operator norm, so every candidate is bounded below by the infimum over invariant operators with a single real coefficient alpha. On [0,1], a distance-to-point test exactly attains each probability-barycenter edge contribution, (1+(w-1)alpha)/a and (w-(w-1)alpha)/b. The two-level class test gives the exact inter-apex norm |2alpha-1|/h. For alpha<0 use the class-level test at A and the distance test at B to bound the two old-to-new terms below by their values at 0; for alpha>1 swap these roles to bound by their values at 1. The new edge also dominates its respective endpoint value in both cases. Thus signed coefficients cannot improve the minimum. For L>=1, the three closed intervals [0,1], [(w-bL)/(w-1),(aL-1)/(w-1)] and [(1-hL)/2,(1+hL)/2] intersect exactly when each lower end is no larger than every upper end. This yields the claimed four terms after dropping the weaker b-versions by a<=b; no strict inequality is used at the feasibility boundaries. An alpha in the intersection at the closed optimum attains it. Finite-dimensional adjoint duality on the anchored spaces gives the same constant for the isometric free-space inclusion. As an exact spot check, at n=3,t=2,a=1,b=3/2,h=1/2 the two tight bounds force alpha=3/13 at L=14/13, while assigning each apex the mean of the farther class alone is contractive on its one-point extension. Read RESULT.md lines 4–79, VERIFICATION.md and check_two_apex.py. The package's LP is a supplementary unrestricted floating-point check, not a proof. The file as written lists 13 supercritical cases and one skipped w=1 case, so the narrative count of 12 is not independently established; the script was not executed and this count does not affect the Finding.

## originality

PASS

The supported distinction is the exact coupled two-apex norm and its h-dependent contractivity obstruction over all real-linear extensions. One-point cluster formulas, symmetry averaging, and the projection reformulation are prior machinery or overlapping subproblems, not themselves the contribution. The strongest distinct same-day match was read; it gives the one-apex problem, not a joint result.

## value

PASS

The exact invariant addresses whether two individually contractive linear extensions can be realized by a single contractive operator. This natural compatibility question has a negative answer with a sharp threshold and fully attained norm in a whole symmetric metric family, not only a chosen example. The obstruction does not follow from the two separate extension constants and is relevant also to relative Lipschitz-free projection constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
