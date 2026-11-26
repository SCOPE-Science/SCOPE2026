# Independent mathematical audit

## correctness

PASS

In each row least squares gives e_i=h·g_i/||g_i||² almost surely and Y_i=e_i² equals the excess squared row error by orthogonality. The Gaussian vector h is independent of the pair of regressors; their block covariance has identity diagonal and ρI off-diagonal. Standardizing the conditional numerator gives a unit normal independent of ||g_i||², so the F_{1,q}/q law and inverse-chi-square mean 1/(q−2) follow. Independently of the spherical integral in the paper, the scaled exceedance region |h·u|>||u||² is the disjoint union of open balls centered at ±h/2 with radius ||h||/2, of volume J=2^(1−q)π^(q/2)||h||^q/Γ(q/2+1). For |ρ|<1 put u_i=√t g_i: the Jacobian gives t^(−q), and the joint Gaussian density at the origin is (2π)^(−q)(1−ρ²)^(−q/2). Its exponential factor is at most one and tends to one on the product of the two regions; E J² is finite, so dominated convergence applies. Using E||h||^s=2^(s/2)Γ((q+s)/2)/Γ(q/2), the marginal limit constant is (2π)^(−q/2)E J=C_q and the joint numerator is (2π)^(−q)E J²=K_q by gamma duplication. The orthogonal product ratio is E J²/(E J)²>1 by strict variance, equal to the stated gamma ratio. For ρ=±1 the regressors are equal up to sign and the squared errors coincide, giving the separate t^(−q/2) law. At q=3 these checks give C_3=4/(3π) and K_3=35/(24π). All limits are fixed-angle and the nonaligned coefficient diverges toward either alignment boundary, consistent with nonuniformity.

## originality

PASS

The shared Gaussian forward algorithm and exact one-row Student/F law have clear earlier coverage. The supported distinct claim is the two-row joint fixed-angle power and coefficient for regressors with correlated directions and a shared residual, the singular change of exponent at alignment, and the explicit excess over product risk even for orthogonal directions. The compared mean bounds, marginal laws, and different common-factor models do not identify this joint invariant.

## value

PASS

A shared Gaussian sketch is a natural algorithmic choice, and neither the exact mean nor the marginal law reveals simultaneous catastrophic errors. The exponent changes at alignment without changing either marginal, and orthogonality still leaves a nontrivial factor above independent risk. The coefficient and its divergence as alignment is approached quantify how far independent-error heuristics can fail, and offer a sharp reference for future multirow or uniform-alignment analysis without asserting either extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
