# Independent mathematical audit

## correctness

PASS

For x with ||x||=r, the exact proximal minimizer is collinear radial with t in [0,r], giving P=min[φ(t)+(r-t)^2/(2α)]; unconstrained squared-tangent minimization yields N=F/(1+αg²/(2F)). If q=√φ is convex, its tangent is dominated on [t0,r], t0=r-2F/g>=0, and for t<t0 the distance penalty gives P>=N. If q is concave, tangent is nonnegative and majorizes q; when model minimizer t_N<0, explicit α-threshold implies P<=r²/(2α)<=N. Affine equality follows. For powers, t+αt^{p-1}=r and the p=1 soft-threshold justify sharp p=2 reversal and signed small/large α limits. Independently solved 105 scalar cases across p=1,...,7 and α from 0.001 to 100 with correct signs.

## originality

PASS

Schaipp–Gower–Taylor 2026 introduces the same NGN/SPP indices but compares each to SGD and shows only quadratic equality, not the cross-model sign classification. Orvieto–Xiao 2024 derives NGN and studies convergence rather than static exact proximal envelope. The current square-root radial curvature criterion (including center-crossing case) determines the NGN/SPP relative order for every α and has two explicit asymptotic constants. Resultary proximal/stability hits treat different model comparisons.

## value

PASS

The relative ordering of NGN and exact-proximal stability indices is not universal for arbitrary convex objectives. This supplies a mathematically motivated geometric sign criterion, a sharp homogeneity phase change at p=2, and quantitative asymptotic gaps in the same objective class used to motivate NGN. The negative-affine-tangent and zero-radius cases make it more than a simple monotonicity substitution; it gives precise benchmarks without claiming algorithmic convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
