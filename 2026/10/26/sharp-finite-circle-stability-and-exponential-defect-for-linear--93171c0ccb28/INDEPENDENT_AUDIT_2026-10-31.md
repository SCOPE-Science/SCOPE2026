# Independent mathematical audit

## correctness

PASS

For n>=3 uniform periodic continuous linear splines, nodal hats have Gram matrix (4I+S+S^{-1})/(6n). The infinite Green sequence h_j=(-q)^|j|/(2 sqrt3), q=2-sqrt3, periodizes absolutely to g_{n,j}=((−q)^j+(−q)^{n-j})/(2sqrt3(1−(−q)^n)). The knot kernel on each arc is the affine interpolation of neighboring inverse entries, hence sharp norm 6 sum_j H(g_j,g_{j+1}); convexity of evaluation kernels ensures no interior output exceeds a knot, and the signed kernel attains it. The infinite kernel has absolute L1 mass exactly 2; periodization yields upper defect <=4q^floor(n/2). Even and odd fixed-width opposite-sign overlap windows yield lower defect >=3(7q−1)/(32sqrt3)*q^floor(n/2)>0, hence all finite Lambda<2 and nth-root defect sqrt(q). Independent exact inversion/segment integration for n=3..18 matched first norms and bounds, finite corroboration only. Assumptions include unit circle, normalized Lebesgue and equally spaced distinct n>=3 nodes.

## originality

PASS

The classical spline Gram recursion and uniform stability estimates are prior knowledge. Passenbrunner 2016/2018 full-text article covers arbitrary-knot periodic orthoprojection with L∞ uniform bound independent of knots and localization, but not the displayed sharp uniform-n formula or strictly positive finite-circle exponential defect in inspected theorem sections. Earlier infinite-line norm=2 is only a limiting value and cannot imply strict finite cancellation or exact q^{n/2} rate. Originality restricted to exact finite-circle constant and sharp defect rate, with possible old circulant finite-element antecedents.

## value

PASS

Endpoint stability of L² spline projection is a central approximation-theoretic invariant. Computing the entire finite uniformly periodic Lebesgue constant and proving its exact rate of approach to the infinite-mesh norm is a natural complete finite-size problem, useful for quantitative projector stability and testing spline solvers. It is not a gratuitous numerical fragment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
