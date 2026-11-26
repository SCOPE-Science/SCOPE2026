# Independent mathematical audit

## correctness

PASS

At zero detuning the one-step product is bd; the scalar iterate has g(x)-x=x((b-A)x-bd)/(Ax+bd). Monotonicity of each orbit and the unique positive fixed point give the full stable line and both escape limits, including initial y=0. For small detuning the equilibrium has an eigenvalue near zero and an expanding eigenvalue near B/b. The forward local stable-manifold theorem with smooth parameter dependence applies also at the endomorphism parameter: the unstable block is invertible, and no inverse of the stable block is needed. The stable tangent has nonzero y component. Its one-step pullback has x derivative B/(A+y) on the unperturbed graph, uniformly positive on each prescribed compact. Local constructions can use slightly larger open intervals, including a small extension at y=0; the map is smooth there. For uniqueness even among eventual entrants, write the map in (x,-y) coordinates. It is strictly order preserving and the equilibrium derivative has positive entries and a positive left Perron vector for the expanding eigenvalue. In a convex neighborhood of the equilibrium the left-vector weighted gap of comparable points increases by a uniform factor greater than one, by integrating the derivative on their joining segment. Two distinct points with the same y and both converging would contradict this after entering the neighborhood. Joint smoothness with at least three parameter and two ordinate derivatives gives the compact C² remainder. Separate exact-symbolic substitution into the graph identity gave zero first- and second-order residuals, with u(q)=1/q and v(q)=0; differentiation gives v''=-2bq/[d B³(A+y)³]. This coefficient is bounded away from zero in magnitude on each compact, not along the full unbounded curve. The supplied verify.py was inspected, not run; its finite shooting is not evidence of global uniqueness or the compact-uniform remainder. The decisive symbolic calculation is replayable by expanding (d(A+y)+ε)/(s0+εu+ε²v) to order two and comparing the two sides of RESULT.md lines 72–96.

## originality

PASS

Pass for the explicit compact-C² unfolding in the original coordinates, especially the first nonzero curvature coefficient on both detuning sides. The singular scalar reduction and nondegenerate qualitative separation are credited as prior, and the singular stable line is an immediate consequence of the reduction, not a separate novelty. Available statements do not supply the mixed ordinate/parameter derivatives.

## value

PASS

For a previously studied competitive system this resolves a specific geometric question not answered by a basin split: the first displacement is purely affine, but a nonzero quadratic effect bends the actual separator to the same side for either sign of detuning. The compact-uniform C² estimate makes that sign a conclusion about a true stable graph, rather than a formal curve or a few numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
