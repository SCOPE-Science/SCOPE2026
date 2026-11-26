# Independent mathematical audit

## correctness

PASS

Zero total mass permits centering a test function's range, replacing its sup norm by half its oscillation. For a nonconstant test, dividing by its d-Lipschitz constant and setting s to the resulting oscillation gives the upper bound by the clipped-metric Lipschitz supremum divided by 1+s/2; centering and rescaling any clipped-metric maximizer gives the reverse inequality. The tree for min(d,s) has clipped full-distance heights and half-height differences as edge lengths; contract zero edges or require their potentials to agree. Telescoping pairs each edge increment with its signed subtree mass. The absolute-mass bound is attained by choosing all edge increments as their lengths times the respective mass signs; the path bounds give a valid leaf test. This proves the numerator B(s)/2 before rescaling. The numerator is affine between distinct heights; its ratio to 2+s is monotone or constant on each interval, is zero in the limit at zero, and is nonincreasing after the diameter. Hence one need only test the heights. The slope updates per edge are +|M(v)| and −|M(v)| at its lower and upper heights, yielding the stated sweep bound on a tree with O(|X|) vertices. A leaf pair at height s gives B(r)=2 min(r,s), uniquely selecting s. In the two-level case B(a)=2aS and B(b)=2[aS+(b−a)P]; subtraction of the two ratios has the sign of (2+a)P−aS. For S>0 the threshold lies strictly between 0 and S, and the displayed four weights realize all P in [0,S].

## originality

PASS

Credit the established tree transport formula, general bounded-Lipschitz norming/LP framework, and exact one-height value. The supported claim is the reduction of the coupled sum norm to a sharp finite height optimization on arbitrary finite ultrametric hierarchies, including the constructive sweep and two-cluster threshold. The closest inspected results do not supply that combined reduction.

## value

PASS

For signed data on a hierarchy, this replaces a coupled test-function optimization by a tree-sized sweep with an explicit norming function and a provably sharp set of candidate scales. The two-level switch explains exactly when net intercluster imbalance can outweigh intracluster variation, independently of the size of the intercluster gap. These are useful consequences of the height reduction beyond the known value of a single tree transport problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
