# Independent mathematical audit

## correctness

PASS

For μ>0 connectedness makes the Metzler matrix irreducible, so its positive principal eigenvector is unique up to scale, including equal fitness. On complete graphs of order two and three the off-diagonal rank-one form gives p_i proportional to 1/(λ+nμ−f_i) with positive denominators, fixing the order. On the three-path the leaf denominators fix their relative order and a center–leaf tie requires λ=f_leaf. The simple eigenvalue derivative equals −pᵀLp/pᵀp, strictly negative unless p is constant, which is possible only with all fitnesses equal. Thus a single crossing, but not two, is allowed in general on the smaller shapes. For the four-path the first, third and fourth rows alone give sign(p3−p1)=sign(1−μ+μ²/(λ−3+μ)), where the last row gives λ−3+μ>0 and the ratio denominator from the third row is positive. This sign is positive at μ≤1. For μ>1 it is the sign of z*−λ, with z*=4+1/(μ−1)>4. The other eigenvalues are ≤3 by the min–max comparison to diag(f), so sign(z*−λ) equals the sign of the characteristic polynomial evaluated at z*. The independent tridiagonal recurrence factors that evaluation as μ²(μ²+2μ−2)F(μ)/(μ−1)^4, whose prefactor is positive for μ>1. Exact endpoint signs for F in the three disjoint brackets establish three simple roots, exactly two admissible. Their signs give the whole asserted ranking with no other tie. The same replay confirms the original remainder/resultant and high-μ correction; normalization does not change rankings.

## originality

PASS

The additive spectral framework is established prior work, as is the general distinction between abundance and intrinsic growth. The supported claim is the sharp minimum and the exact twice-switching comparison in the fixed-fitness graph-Laplacian family. The closest inspected theorem-level ranking matches use different operators or observables, and the closest exact model source does not give the crossing or the small-graph bound.

## value

PASS

The sharp cutoff locates a genuine qualitative limit of a natural symmetric diffusion-plus-growth operator: monotonicity of the top eigenvalue does not make the ordering of its vector coordinates monotone. The minimal path, the exact interval, and the explicit exclusion of every smaller graph give a concise benchmark for reasoning about parameterized equilibrium rankings rather than a numerical example selected at isolated rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
