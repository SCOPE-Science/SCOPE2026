# Independent mathematical audit

## correctness

PASS

For the given vertices, signs determine the edge intersections. In a 2+2 chamber the normal can be written (1,y,z) with |y|+|z|<1 after symmetry and sign reversal. The two opposite-side chords have the stated squared lengths by solving the plane equation on the four edges. They are both >=2 in length, with simultaneous equality only on the axis; the axis section has the four cross vertices with shorter sides. For 1+3, the intersection fractions have sum of reciprocals 4, so some pair averages >=3/4 by Cauchy–Schwarz. The 60-degree edge angle makes its side at least 3 sqrt(2)/2. To justify the equality classification at chamber boundaries, one zero vertex dot product permits perturbation into a 1+3 chamber (move the zero sign to the majority side), and two zeros mean the section contains an edge. The section diameter is continuous: compactness gives the upper limit, and points can first be contracted toward the interior origin then rotated into nearby planes to give the lower limit. Strict convexity of squared distance forces any globally diametral pair to be two original vertices. The six edge planes are distinct, and continuity and full spherical support give the whole support interval. Near an axis the two long chords dominate and L-2=max(y^2,z^2)+O((y^2+z^2)^2). Near a maximizing normal the new points at A,B move along their incident edges with fractions alpha=|a|/sqrt(2)+O(x^2+y^2), beta=|b|/sqrt(2)+O(x^2+y^2). Their chord has deficit |a|+|b|+O(x^2+y^2). The CD point remains separated by a strict distance gap; in opposite-sign chambers the extra AB point at fraction lambda=|a|/(|a|+|b|) loses to the long pair, with squared-distance difference divided by 8 equal to lambda(2-lambda-beta)-alpha(1-alpha), positive since alpha=O(|a|) and the first term is at least lambda/2. The symmetric comparison and continuity cover sign boundaries. Both leading local increments are coercive, so the bounded scaled sublevel indicators converge almost everywhere to the square and the stated rectangle. Chart Jacobians tend to 1 and the boundaries of both limiting sets have area zero. Their areas 4 and 1/sqrt(2), with 6 and 12 oriented charts respectively, give 6/pi and 3/(pi sqrt(2)), and normalized local measure gives the conditional limits. Independent replay: python3 /workspace/reproduction/frozen_checks.py 4, computing all pair distances among actual edge intersections on a deterministic spherical-chart grid. At eps=0.004 the ratios are about 1.87724 and 0.68160 (limited by finite threshold and grid); they are checks, not limit proofs. The source checker was inspected, not executed.

## originality

PASS

Closest coverage includes exact random tetrahedral outer-radius laws, exact central-section diameters for cross-polytopes, and high-probability random-section diameter theory. None of those statements give the two sharp planar tetrahedral diameter tails or their conditional direction laws. Credit is confined to the stated sharp fixed-solid endpoints and local laws, not a general random-diameter framework.

## value

PASS

The Euclidean diameter of a central section is a natural shape statistic for the canonical noncentrally symmetric Platonic solid. The quantitative contrast between lower quadratic local stability and upper piecewise-linear deficit gives different probability powers, with explicit equality configurations, weights and conditional direction profiles. These are useful sharp benchmarks beyond general high-probability estimates and cannot be read off from a centered radius distribution. The result does not claim a global CDF or higher-dimensional extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
