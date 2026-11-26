# Independent mathematical audit

## correctness

PASS

For D=−ρURVᵀ, substitute the feasible matrices −ρURZVᵀ with ||Z||₂≤1 into the first-order variational inequality. It says I maximizes the pairing with S=Rᵀ(Σ−ερMRN). Orthogonal perturbations of I force S symmetric; reflections I−2vvᵀ force S positive semidefinite; a positive semidefinite S suffices by spectral/nuclear duality. Thus the condition certifies global optimality. At ε=0, a contraction maximizing the pairing with strictly positive diagonal Σ has every diagonal entry one and hence equals I. At ε>0, strict convexity gives uniqueness. On K skew the derivative of skew(S) at zero is −(KΣ+ΣK)/2, invertible even with repeated singular values. The analytic implicit branch has S positive definite by continuity, so all optimizer singular values are exactly ρ there. Differentiating gives K′Σ+ΣK′=−ρC. The linear objective's rotation increment is ρ Σ_{i<j}(σᵢ+σⱼ)Kᵢⱼ²/2 to second order, and the curvature increment is ερ² Σ_{i<j}Cᵢⱼ Kᵢⱼ at first order in K. Substituting the derivative gives the stated positive improvement coefficient and O(ε³) remainder. Setting R=I is exact for all ε; for ε>0 symmetry is commutation, and congruence by Σ⁻¹ᐟ² gives the threshold including its endpoint. The example checks symbolically: with R=[cos k,sin k;−sin k,cos k] the planar increment is 4(1−cos k)+ε(sin²k+sin k cos k)/2, producing the reported candidate expansion at k=−ε/8.

## originality

PASS

The prior work supplies the same optimization model, qualitative rotation examples and general optimality tools. The baseline persistence condition is a direct specialization of that convex optimality framework, not an independent novelty basis. The distinct result is the quantitative full-rank small-curvature law: exact flatness on a neighborhood, the signed commutator response, and the explicit second-order optimal-value coefficient for general two-sided Kronecker curvature. No inspected result covers this combination or supplies those coefficients.

## value

PASS

For the motivated QSD surrogate, the formulas distinguish curvature-induced rotation from amplitude shrinkage at the first perturbative scale and quantify the value of changing the matrix-sign step. The coefficient is interpretable entry by entry and the exact baseline condition clarifies when rotation cannot improve it. This is more informative than the already known statement that quadratic minimization cannot worsen the baseline surrogate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
