# Exponent-invariant cross-polytope projection and its sharp Lipschitz threshold

## Finding
For each integer \(n\ge1\), each \(1<p<\infty\), and each radius \(r>0\), let \(Q_{p,n,r}\) denote the nearest-point map, measured in the real \(\ell_p^n\) norm, onto the cross-polytope \(B_1^n(r)=\{y\in\mathbb R^n:\sum_{i=1}^n|y_i|\le r\}\). The map is independent of the exponent \(p\): if \(\sum_i|x_i|\le r\), then \(Q_{p,n,r}(x)=x\); otherwise
\[
Q_{p,n,r}(x)_i=\operatorname{sgn}(x_i)(|x_i|-\tau)_+,
\qquad\sum_{i=1}^n(|x_i|-\tau)_+=r,
\]
where \(\tau>0\) is uniquely determined. Put \(C_k=I_k-k^{-1}{\bf1}{\bf1}^{\mathsf T}\) for \(k\ge2\). The **optimal global Lipschitz constant**, with the domain and codomain both carrying \(\ell_p\), is exactly
\[
L_{p,n}=\max\left\{1,\max_{2\le k\le n}\|C_k\|_{\ell_p^k\to\ell_p^k}\right\}.
\]
The inner maximum is empty when \(n=1\). In particular, \(L_{p,n}=1\) if and only if \(n\le2\) or \(p=2\). For the first dimension admitting expansion, the sharp value at the fourth-power exponent is
\[
L_{4,3}=L_{4/3,3}=\left(\frac{(1+\sqrt[3]{2})^3}{9}\right)^{1/4}\approx1.0641658628581188.
\]
The constants do not depend on \(r\), and the finite-dimensional norm maxima are achieved by differences of inputs lying in a common full-dimensional affine cell of the metric projection.

## Assumptions and scope
Everything is real. The exponent satisfies \(1<p<\infty\), the dimension is a positive integer, and \(r>0\). The ambient norm is \(\|x\|_p=(\sum_i|x_i|^p)^{1/p}\); the target set is the **different** \(\ell_1\) ball. The global Lipschitz constant means the supremum over all distinct input pairs of the output-distance divided by input-distance, both in the indicated \(\ell_p\) norm. No statement about nonunique metric projections at the endpoint exponents is made.

## Proof
**1. The optimizer is exponent-invariant.** Strict convexity of \(\sum_i|x_i-y_i|^p\) gives a unique minimizer over the compact convex ball. If \(\sum_i|x_i|>r\), decreasing an output magnitude above the corresponding input magnitude, or reversing a nonzero output sign away from the input sign, reduces objective without worsening feasibility. Therefore the optimizer has the input signs and magnitudes \(0\le z_i\le|x_i|\). The norm constraint is active: otherwise increasing a positive residual coordinate toward its input strictly improves the objective. For a Lagrange multiplier \(\lambda>0\), each positive optimal magnitude satisfies
\[
p(|x_i|-z_i)^{p-1}=\lambda;
\]
hence all positive coordinates have the same residual \(\tau=(\lambda/p)^{1/(p-1)}\). Complementary slackness at a zero coordinate gives \(|x_i|\le\tau\). Thus \(z_i=(|x_i|-\tau)_+\), and the active constraint uniquely determines \(\tau>0\). This formula has no remaining \(p\)-dependence. If the input belongs to the ball, the unique nearest point is itself.

**2. Sharp global Lipschitz constant.** The explicit formula is a continuous piecewise-affine function with finitely many polyhedral cells: fix coordinate signs, the set of positive output coordinates \(A\), and whether the input is inside the ball. In an exterior full-dimensional cell with \(|A|=k\),
\[
\tau=\frac{\sum_{i\in A}\operatorname{sgn}(x_i)x_i-r}{k}.
\]
Its Jacobian acts by \(D_s C_k D_s\) on the active coordinates and by zero on the remaining coordinates, where \(D_s\) is the diagonal sign matrix; on the ball interior it is the identity. Sign changes are \(\ell_p\) isometries, so the exterior Jacobian norm equals \(\|C_k\|_{p\to p}\). The norm is zero for \(k=1\). Any segment joining two inputs is partitioned by finitely many cell boundaries; integrating the constant affine slopes on its pieces yields the asserted upper Lipschitz bound. The interior identity cell gives the lower bound \(1\). Each \(k\in\{2,\ldots,n\}\) has an open exterior cell: choose \(k\) positive input coordinates equal to \(t+r/k\) and the others zero, with \(t>0\); then the threshold is \(t\) and exactly these \(k\) coordinates remain positive. A sufficiently short perturbation in any prescribed active direction stays in that same cell, so the full operator norm \(\|C_k\|_{p\to p}\) is attained as a ratio of output differences. This proves equality, not merely a bound.

**3. Characterization of nonexpansiveness.** For \(k=2\),
\[
C_2(x_1,x_2)=\tfrac12(x_1-x_2,x_2-x_1),\qquad \|C_2\|_{p\to p}=1
\]
by Hölder's inequality, with equality at \((1,-1)\). For \(p=2\), every \(C_k\) is an orthogonal projection and has norm \(1\) when \(k\ge2\). Thus \(L_{p,n}=1\) when \(n\le2\) or \(p=2\). Conversely, for \(n\ge3\), consider \(u=(1,1,-2)\in\mathbb R^3\), which has zero mean. The derivative at zero of \(c\mapsto\|u+c\mathbf1\|_p^p\) is
\[
p(2-2^{p-1}),
\]
which is nonzero for every \(p\ne2\). Consequently some nonzero \(c\) satisfies \(\|u+c\mathbf1\|_p<\|u\|_p\), while \(C_3(u+c\mathbf1)=u\). Hence \(\|C_3\|_{p\to p}>1\), forcing \(L_{p,n}>1\). The sign criterion is exact.

**4. The sharp three-dimensional fourth-power value.** If \(v\in\mathbb R^3\) has sum zero, the elementary identity
\[
\sum_{i=1}^3v_i^4=\tfrac12\left(\sum_{i=1}^3v_i^2\right)^2
\]
shows that maximizing \(\|C_3x\|_4\) on the compact constraint \(\sum_i x_i^4=1\) is equivalent to maximizing the quadratic form \(x^{\mathsf T}C_3x\). A positive maximizing value exists. At a maximizer, Lagrange multipliers give
\[
x_i-\bar x=\lambda x_i^3\quad(i=1,2,3),\qquad\lambda>0,
\]
where \(\bar x=(x_1+x_2+x_3)/3\). The three coordinates are roots of one depressed cubic. If they are all distinct, Vieta's formula forces their sum to be zero, thus \(\bar x=0\); the cubic then forces, up to permutation and scaling, \(x=(1,-1,0)\), whose quotient equals \(1\). Otherwise two coordinates agree, so write \(x=(a,a,b)\). Direct substitution gives
\[
\frac{\|C_3x\|_4^4}{\|x\|_4^4}=\frac{2(a-b)^4}{9(2a^4+b^4)}.
\]
By sharp weighted Hölder duality,
\[
\sup_{(a,b)\ne(0,0)}\frac{|a-b|^4}{2a^4+b^4}=(1+2^{-1/3})^3,
\]
attained precisely when \(b=-2^{1/3}a\) (up to overall scaling). This produces \(\|C_3\|_{4\to4}^4=(1+\sqrt[3]2)^3/9>1\). Since the transpose of \(C_3\) is itself, operator-norm duality yields \(\|C_3\|_{4/3\to4/3}=\|C_3\|_{4\to4}\). Part 2 transfers these sharp norms to the nonlinear nearest-point map.

## Verification
The included standalone script `verification/check.py` uses only the Python standard library. Execute `python verification/check.py` after extraction from this package. It checks the exact zero-sum quartic identity on rational inputs, centering columns, the sharp three-coordinate formula and its realizable affine-cell quotient, and 600 deterministic random soft-threshold/KKT cases across four dimensions and several exponents. An actual run printed `CROSSPOLYTOPE_LP_METRIC_PROJECTION_CHECK_OK` and the value `1.0641658628581188`. The infinite-parameter assertions depend on the proof above, not on these finite tests.

## Relationship to prior work
Duchi, Shalev-Shwartz, Singer, and Chandra (2008) derive the Euclidean \(\ell_1\)-ball projection and soft-threshold algorithm. That established \(p=2\) formula is prior art; the projection formula alone is not presented as independently new. Kobos (2014) studies minimal **linear** projections onto hyperplanes of finite-dimensional normed spaces and the sharp Bohnenblust projection bound. Such estimates motivate measuring projection norms but neither compare nearest-point maps on cross-polytopes across all \(\ell_p\) exponents nor calculate the exact three-dimensional fourth-power nonlinear modulus. The result combines exponent-invariant nearest points with an exact all-active-set Lipschitz principle and the first non-Hilbertian failure of nonexpansiveness. No claim of uniqueness against unpublished or unindexed results is made.

## Limitations
The proof does not apply unchanged to weighted coordinate norms, other target convex bodies, complex scalar spaces, or the ambient endpoint exponents. The general-dimension sharp modulus is expressed as a finite maximum of specified induced operator norms, not as a closed elementary formula for every \(p,n\). The explicit radical formula is for dimension three at exponents four and four-thirds. The equivalence-to-prior-work comparison cannot exclude older literature giving the same centering-operator norm or nonlinear projection modulus under another name. 
## References
1. T. Kobos, *Hyperplanes of finite-dimensional normed spaces with the maximal relative projection constant*, arXiv:1411.6214v1 (first publicly submitted 23 November 2014), https://arxiv.org/abs/1411.6214.
2. J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the ℓ1-Ball for Learning in High Dimensions*, Proceedings of ICML 2008, 272–279, DOI:10.1145/1390156.1390191, https://ai.stanford.edu/~jduchi/projects/jd_ss_ys_l1.pdf.
