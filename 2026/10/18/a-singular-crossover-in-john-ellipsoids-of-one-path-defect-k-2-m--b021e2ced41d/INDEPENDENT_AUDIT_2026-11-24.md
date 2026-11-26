# Independent mathematical audit

## correctness

PASS

Re-derived the resistance and volume without the spanning-tree differentiation: on the zero-sum hyperplane set h=x_u−x_v and z_i=x_{w_i}−(x_u+x_v)/2, and write G=sum g_i. The energy is Gh²/2+2 sum g_i z_i². Since the edge forms are ±h/2−z_i, their squared supports are 1/(2G)+1/(2g_i). The coordinate map has squared Jacobian m+2 (row Gram blocks 2 and I+11ᵀ/2), giving det_H L=(m+2)2^{m−1}G prod g_i and the claimed intrinsic volume. The ordinary support condition fixes a=(1+1/(m−1+r))/2; the exceptional support condition gives the stated quadratic with opposite-sign roots. Thus all contacts hold, including m=2 and t=1. For arbitrary feasible centered shape matrices the positive Laplacian decomposition bounds the log-determinant gain by zero, with equality only at the proposed shape. A translation adds |edge difference of the center| to the necessary support; at the optimal shape all these differences must vanish, so the center is zero. The zero-row-sum extension of the precision matrix L recovers labeled edges from negative off-diagonals, and the covariance determines the contacting lengths. For fixed t, rationalizing the positive root gives r→t⁻² and log(a/a₀)=O(m⁻²). At fixed m, r=2/t²−(m+1)/2+O(t²), giving det_H L~(m+2)t⁻⁴ and the stated prefactor. At t=c/√m the equation for u=r/m is c²u²+(c²−2)u−(1−1/m)=0, so u→ρ; (m+1)log(a/a₀)→−ρ/(1+ρ) and r(m−1+r)/m²→ρ(1+ρ). This gives the profile and both endpoints using ρ~2/c² and ρ~1/c². The bundled NumPy and SymPy programs were read but not executed; this check is analytical and covers the full parameter range.

## originality

PASS

The general D-optimal certificate and the ordinary K_{2,m} baseline are not the new content. The supported distinction is the exceptional-path solution, its persistent contact when t varies, and the normalized volume scaling law. Checked related graph families do not imply this anisotropic formula and limit.

## value

PASS

The one-path defect is a minimal controlled metric perturbation, and the normalized John volume is a specific extremal invariant. The exact solution distinguishes a two-direction collapse at fixed size from the linear large-network response and gives the crossover function, not just a possible scaling exponent. This has quantitative use for sensitivity of these metric balls; it does not assert that general heterogeneous metrics have full contact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
