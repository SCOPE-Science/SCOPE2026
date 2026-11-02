# Sharp nuclear-distance mean-width stability for affine harmonic ball maps

## Finding

For each integer \(n\ge3\), the largest admissible coefficient in a natural sharp stability inequality is determined explicitly. Let \(A\) be a real \(n\times n\) matrix with \(\|A\|_{\mathrm{op}}\le1\), let \(0<r\le1\), and put \(f_A(x)=Ax\). The map is componentwise harmonic and maps the Euclidean unit ball into itself. Set \(K_{A,r}=\operatorname{co}f_A(r\mathbb S^{n-1})=rA\overline{\mathbb B^n}\). For normalized spherical measure \(\sigma\), mean width is
\[
W(K)=2\int_{\mathbb S^{n-1}}h_K(u)\,d\sigma(u),\qquad h_K(u)=\sup_{x\in K}\langle x,u\rangle.
\]
Define \(\delta_1(A,O(n))=\inf_{Q\in O(n)}\|A-Q\|_{\mathcal S_1}\), where \(\|\cdot\|_{\mathcal S_1}\) is the nuclear norm. Then
\[
\boxed{\quad 2r-W(K_{A,r})\ge 2r\gamma_n\,\delta_1(A,O(n)),\quad
\gamma_n=1-\frac{\Gamma(n/2)^2}{\Gamma((n-1)/2)\Gamma((n+1)/2)}.\quad}
\]
This \(\gamma_n\) is optimal over all contractions and equality holds if and only if the singular values of \(A\) are either all \(1\), or precisely \(n-1\) ones and one zero. The latter equality family consists of rank-\((n-1)\) partial isometries and realizes a complete loss of one spatial direction. Thus the limiting local coefficient \(1/n\) is strictly larger than the globally optimal one. In dimension three, the exact global coefficient is \(\gamma_3=1-\pi/4\).

## Assumptions and scope

The theorem concerns **all real affine homogeneous harmonic self-maps** of the Euclidean unit ball; translations are not included. Only nonzero sampling radii \(0<r\le1\) are used. For a real matrix \(A\), the singular values are \(s_1,\ldots,s_n\in[0,1]\). The Schatten-one metric is the nuclear norm, not the Frobenius or operator metric. Mean width is normalized by \(W(\overline{\mathbb B^n})=2\). No claim concerns unrestricted nonlinear harmonic self-maps, nor does this identify their sharp quantitative stability constant.

## Proof

**Step 1: exact spectral expression.** Rotational invariance and singular-value decomposition give, for a uniform random point \(U\in\mathbb S^{n-1}\),
\[
\frac{W(K_{A,r})}{2r}=\mathbb E\|A^\mathsf TU\|=\mathbb E\sqrt{\sum_{j=1}^n s_j^2U_j^2}.
\]
Since the singular values of every orthogonal matrix are one, Mirsky's singular-value inequality implies \(\|A-Q\|_{\mathcal S_1}\ge\sum_j|s_j-1|\) for every \(Q\in O(n)\). Equality occurs for the orthogonal factor in a singular-value decomposition. Therefore
\[
\delta_1(A,O(n))=\sum_{j=1}^n(1-s_j)=n-\|A\|_{\mathcal S_1}.
\]

**Step 2: a sharp scalar reduction.** Set \(H(t)=1-\sqrt{1-t}\) for \(0\le t\le1\). The derivative \(H'(t)=1/(2\sqrt{1-t})\) is strictly increasing on \((0,1)\). Integrating the derivative shows that for nonnegative \(a_j\) with \(\sum_ja_j\le1\),
\[
H\left(\sum_ja_j\right)\ge\sum_jH(a_j),
\]
with strict inequality whenever at least two of the \(a_j\) are positive and their total is less than one. Indeed, for \(a,b>0\), \(H(a+b)-H(a)=\int_0^bH'(a+t)\,dt>\int_0^bH'(t)\,dt=H(b)\).

For fixed \(x\in(0,1)\), the function \(q_x(s)=\sqrt{1-x+xs^2}\) is strictly convex on \([0,1]\), because
\[
q_x''(s)=\frac{x(1-x)}{(1-x+xs^2)^{3/2}}>0.
\]
Its chord inequality gives \(q_x(s)\le(1-s)q_x(0)+sq_x(1)\), equivalently
\[
H((1-s^2)x)\ge (1-s)H(x),\qquad 0\le s\le1.
\]
This is strict if \(0<s<1\) and \(0<x<1\).

**Step 3: integration.** Almost surely \(U_j^2\in(0,1)\) and \(\sum_jU_j^2=1\). Applying both inequalities with \(a_j=(1-s_j^2)U_j^2\) yields
\[
1-\sqrt{\sum_j s_j^2U_j^2}
=H\left(\sum_j(1-s_j^2)U_j^2\right)
\ge\sum_j(1-s_j)H(U_j^2).
\]
All coordinate marginals have the same law. Since \(U_1^2\sim\operatorname{Beta}(1/2,(n-1)/2)\), the beta-integral calculation is exact:
\[
\mathbb E\sqrt{1-U_1^2}
=\frac{B(1/2,n/2)}{B(1/2,(n-1)/2)}
=\frac{\Gamma(n/2)^2}{\Gamma((n+1)/2)\Gamma((n-1)/2)}.
\]
Therefore \(\mathbb E H(U_1^2)=\gamma_n\). Taking expectations and applying Step 1 proves the inequality.

**Step 4: optimality and equality.** If two singular values are strictly less than one, the superadditivity step is strict almost surely, hence so is the final inequality. If exactly one lies strictly between zero and one, the strict convexity step is strict almost surely. Thus equality permits either no deficient singular value, or exactly one singular value equal to zero with all others one. Conversely, for all singular values one the deficit and right side vanish. If the singular values are \((1,\ldots,1,0)\), every scalar inequality in Step 3 is an equality, making the bound exact. The latter example has positive distance one, and therefore proves that the constant cannot be increased.

**Step 5: coefficients and limiting contrast.** In dimension three the gamma ratio equals \(\pi/4\). As \(H(x)<x\) for every \(x\in(0,1)\), \(0<\gamma_n<\mathbb E U_1^2=1/n\). Since \(H(x)=x/2+O(x^2)\), \(\mathbb E U_1^2=1/n\), and \(\mathbb E U_1^4=3/[n(n+2)]\), one has \(\gamma_n=1/(2n)+O(n^{-2})\). For a one-coordinate perturbation with singular values \((1,\ldots,1,1-\varepsilon)\), dominated differentiation gives
\[
\lim_{\varepsilon\downarrow0}\frac{2r-W(K_{A,r})}{2r\,\delta_1(A,O(n))}
=\mathbb E U_n^2=\frac1n>\gamma_n.
\]
This confirms that the global sharp coefficient is controlled by an exact codimension-one collapse and not by perturbations infinitesimally near the orthogonal group.

**Zonal formulation.** Let \(T_k\) be any rotation-invariant linear operator acting by a positive scalar \(\lambda_1(k)\) on degree-one spherical harmonics. Then for the affine boundary profile \(F_A(\eta)=A\eta\), one has exactly \(T_kF_A(\xi)=\lambda_1(k)A\xi\). Replacing \(r\) by \(\lambda_1(k)\) in the theorem gives the corresponding normalized mean-width stability identity for this affine family. This is a rescaling of the same result, not a claim about arbitrary nonlinear profiles.

## Verification

All critical infinite-dimensional and all-parameter inequalities are proved analytically above. A standalone optional program `CHECKER.py` verifies the beta constants, the scalar chord and superadditivity inequalities on deterministic grids, the equality configurations, and selected spherical integrations. Its finite checks are neither exhaustive proofs nor evidence of novelty. The defining beta integral and strict equality classification are verified directly by the displayed proof.

## Relationship to prior work

Zhong and Kalaj (2026, arXiv:2609.09316, first submitted 8 September 2026) establish a sharp general zonal-operator mean-width inequality and its qualitative orthogonal equality profiles. The present assertion is specifically the optimal quantitative **nuclear-distance deficit** throughout the entire affine harmonic subclass, including an equality classification at singular maps; it does not strengthen their inequality for arbitrary profiles. Only that paper's publicly retrievable abstract and theorem summary were available here; detailed full-text overlap is a residual risk. Böröczky, Fodor and Hug (2025, arXiv:2410.11460) establish stability for other extremal position problems involving origin-symmetric convex bodies, including cube/cross-polytope extremizers under John/Löwner conditions. Their inspected principal results do not imply the displayed sharp constant for ball-to-ellipsoid contraction in Schatten-one distance. Earlier work on mean-width stability for general bodies has different hypotheses and extremizers. The potential for an equivalent sharp ellipsoid stability formula elsewhere cannot be eliminated from accessible evidence.

## Limitations

This is a sharp global result **within the affine harmonic subclass only**; nonlinear harmonic mappings and other Schatten distances are not classified. It does not establish stability for the full set of admissible boundary maps of the motivating zonal operator. The motivating paper's full text was unavailable for inspection, and equivalent unindexed literature is a residual originality risk. Independent mathematical verification has not been performed.

## References

1. D. Zhong and D. Kalaj, *Sharp mean-width and Jacobian bounds for Euclidean and hyperbolic harmonic maps*, arXiv:2609.09316 (first public version 2026-09-08), https://arxiv.org/abs/2609.09316 .
2. K. J. Böröczky, F. Fodor and D. Hug, *Strengthened inequalities for the mean width and the \(\ell\)-norm of origin symmetric convex bodies*, Mathematische Annalen 393 (2025), 271–316, https://doi.org/10.1007/s00208-025-03228-0 ; arXiv:2410.11460.
3. K. J. Böröczky, F. Fodor and D. Hug, *Strengthened inequalities for the mean width and the \(\ell\)-norm*, Journal of the London Mathematical Society 104 (2021), 233–268, https://doi.org/10.1112/jlms.12429 .
