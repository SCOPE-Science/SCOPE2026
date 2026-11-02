# Exact Euclidean distortion of centrally slab-clipped cubes and a parity reversal

## Finding

For every integer \(n\ge2\) and real \(t\ge1\), equip \(\mathbb R^n\) with the norm
\[
N_{n,t}(x)=\max\left\{\|x\|_\infty,\;t\left|\sum_{i=1}^n x_i\right|\right\}.
\]
Its unit ball is the centrally symmetric clipped cube
\[
K_{n,t}=[-1,1]^n\cap\left\{x:\left|\sum_{i=1}^n x_i\right|\le t^{-1}\right\}.
\]
The exact squared Banach–Mazur distance to a real Hilbert space is
\[
\boxed{
 d_{\mathrm{BM}}\big((\mathbb R^n,N_{n,t}),\ell_2^n\big)^2=
 \begin{cases}
 \dfrac{n\big(n^2t^2-2(n-1)t+n-2\big)}{n^2t^2-1},& n\text{ even},\\[6pt]
 \dfrac{n\big((n^2-n+1)t^2+n-2\big)}{n^2t^2-1},& n\text{ odd}.
 \end{cases}}
\]
Among all permutation-invariant positive-definite Hilbertian quadratic forms, there is a unique optimal one up to positive scaling:
\[
\boxed{H_{n,t}(x)^2=\|x\|_2^2+\frac{nt^2-1}{n-1}\left(\sum_{i=1}^n x_i\right)^2.}
\]
No uniqueness is asserted among nonsymmetric optimal quadratic forms.

The effect of narrowing the slab reverses with parity: for each fixed even \(n\), the exact squared distortion is **strictly increasing** in \(t\ge1\), whereas for each fixed odd \(n\ge3\) it is **strictly decreasing**. At the starting endpoint \(t=1\), the squared distance equals \(n^2/(n+1)\) in even dimensions and \(n\) in odd dimensions. The respective limits as \(t\to\infty\) are \(n\) and \(n-1+1/n\). The latter limit is a limit through full-dimensional norms, not a distance assigned to the singular limiting body.

## Assumptions and scope

The scalars and Hilbert targets are real, and \(n\) is an arbitrary finite integer at least two. The parameter is any real \(t\ge1\), including \(t=1\). The norm is the maximum of the coordinate-supremum norm and one directional linear functional; it is **not** the norm obtained by replacing the coordinate sum with the sum of the absolute coordinate values. The multiplicative Banach–Mazur distance is \(\inf_T\|T\|\,\|T^{-1}\|\), over all invertible linear maps from the stated normed space to \(\ell_2^n\). The infimum is over arbitrary ellipsoids, not only permutation-invariant ones.

## Proof

**1. Global reduction by permutation averaging.** For any positive-definite quadratic form \(Q\), let \(a(Q)=\min_{N_{n,t}(x)=1}Q(x)\) and \(b(Q)=\max_{N_{n,t}(x)=1}Q(x)\). Its squared distortion equals \(b(Q)/a(Q)\). If \(g\) is a permutation matrix, the inequalities \(a(Q)N_{n,t}(x)^2\le Q(gx)\le b(Q)N_{n,t}(x)^2\) hold for every \(x\). Averaging over all permutations gives a positive-definite permutation-invariant form with squared distortion no greater than \(b(Q)/a(Q)\). Every such form is, up to positive scaling,
\[
Q_\beta(x)=\|x\|_2^2+\beta S(x)^2,\qquad S(x)=\sum_i x_i,\qquad \beta>-1/n.
\]
Consequently the unrestricted Banach–Mazur optimum equals the infimum over the single real parameter \(\beta\). This use of averaging does not claim that every unrestricted optimal form is invariant.

**2. Exact objective for an invariant form.** Write \(L=t^{-1}\in(0,1]\). Let
\[
V(\beta)=\max_{x\in K_{n,t}}\big(\|x\|_2^2+\beta S(x)^2\big),\qquad
U(\beta)=\max_{Q_\beta(x)\le1}N_{n,t}(x)^2.
\]
The squared distortion of \(Q_\beta\) is \(P(\beta)=U(\beta)V(\beta)\). The norm \(N_{n,t}\) is the maximum of the absolute values of the \(n\) coordinate linear functionals and \(tS\). Since
\[
(I+\beta\mathbf1\mathbf1^{\mathsf T})^{-1}=I-\frac{\beta}{1+n\beta}\mathbf1\mathbf1^{\mathsf T},
\]
dual-quadratic norms give the exact identity
\[
U(\beta)=\max\left\{\frac{1+(n-1)\beta}{1+n\beta},\frac{nt^2}{1+n\beta}\right\}.
\]
These branches cross at
\[
\beta_0=\frac{nt^2-1}{n-1}\ge1.
\]

**3. No optimizer lies below the crossing.** For \(-1/n<\beta\le\beta_0\), the second branch of \(U\) dominates, so
\[
P(\beta)=nt^2\max_{x\in K_{n,t}}\frac{\|x\|_2^2+\beta S(x)^2}{1+n\beta}.
\]
For each fixed \(x\), the derivative of the displayed fraction with respect to \(\beta\) is
\[
\frac{S(x)^2-n\|x\|_2^2}{(1+n\beta)^2}\le0
\]
by Cauchy–Schwarz. Every term is nonincreasing, hence the maximum and therefore \(P\) are nonincreasing until \(\beta_0\).

**4. Exhaust the clipped-cube vertices.** For \(\beta\ge\beta_0\), the quadratic form \(Q_\beta\) is convex, so \(V(\beta)\) is maximized at a vertex of \(K_{n,t}\). Such vertices consist of original cube vertices obeying the slab condition and points on one of the two clipping hyperplanes with exactly \(n-1\) coordinates equal to \(\pm1\). When \(n\) is even, the admissible original cube vertices have coordinate sum zero and squared Euclidean norm \(n\); a clipped vertex has \(|S|=L\) and squared Euclidean norm \(n-2L+L^2\). When \(n\) is odd, each clipped vertex has \(|S|=L\) and squared Euclidean norm \(n-1+L^2\), and the admissible original vertices at \(L=1\) are included in this description. These assertions follow because a sum of \(n-1\) signs is odd for even \(n\), and even for odd \(n\), so the only possible feasible sign sums are respectively \(\pm1\) and zero.

For even \(n\), the clipped vertices dominate the balanced vertices if and only if \(\beta\ge2/L-1=2t-1\). This holds throughout our branch because
\[
\beta_0-(2t-1)=\frac{n(t-1)^2+2(t-1)}{n-1}\ge0.
\]
Therefore for every \(\beta\ge\beta_0\), in both parities,
\[
V(\beta)=v_0+\beta L^2,\qquad
v_0=\begin{cases}n-2L+L^2,&n\text{ even},\\n-1+L^2,&n\text{ odd}.
\end{cases}
\]

**5. No optimizer lies above the crossing.** On \(\beta\ge\beta_0\),
\[
P(\beta)=\frac{1+(n-1)\beta}{1+n\beta}\big(v_0+\beta L^2\big).
\]
Its derivative has positive denominator \((1+n\beta)^2\) and numerator
\[
F(\beta)=L^2\big(1+2(n-1)\beta+n(n-1)\beta^2\big)-v_0.
\]
The function \(F\) increases strictly for \(\beta\ge\beta_0\ge1\). At the crossing, \(1+(n-1)\beta_0=nt^2\), hence
\[
F(\beta_0)=n(1+n\beta_0)-V(\beta_0).
\]
For every \(x\in K_{n,t}\), we have \(\|x\|_2^2\le n\) and \(|S(x)|\le L\); hence \(V(\beta_0)\le n+\beta_0 L^2\). Therefore
\[
F(\beta_0)\ge\beta_0(n^2-L^2)>0.
\]
Thus \(P\) increases strictly on \([\beta_0,\infty)\). Together with Step 3, this establishes the global minimum at \(\beta_0\). Because the first branch is strictly decreasing for each nonzero \(x\) off the one-dimensional constant-vector line, and the maximizers exist, it also shows this is the unique *permutation-invariant* minimizer up to scale.

**6. Evaluate the closed formulas and the parity transition.** At \(\beta_0\), either branch of \(U\) gives \(nt^2/(1+n\beta_0)\), and Step 4 gives the exact maximum \(V\). Their product simplifies to the two rational expressions in the statement. Differentiating them gives
\[
\frac{\partial}{\partial t}d_{\mathrm{BM}}^2=
\begin{cases}
\dfrac{2n(n-1)(n^2t^2-n^2t+1)}{(n^2t^2-1)^2}>0,&n\text{ even},\\[6pt]
-\dfrac{2nt(n-1)^2(n+1)}{(n^2t^2-1)^2}<0,&n\text{ odd}.
\end{cases}
\]
Every denominator is strictly positive in the stated domain; the even numerator is positive because \(t\ge1\). Evaluating at \(t=1\) and taking \(t\to\infty\) completes every endpoint and monotonicity claim.

## Verification

The standalone, Python-standard-library checker `artifacts/verify_slab.py` uses exact rational arithmetic. It constructs coordinate-permutation representatives of the slab-clipped cube vertex types for dimensions \(2\) through \(10\) and eight rational slab parameters, checks dual-branch equality and the closed formula, tests neighboring invariant quadratic forms, and checks the claimed parity monotonicity over additional rational parameters. Its recorded successful output is `CHECK_OK exact_parameter_cases= 72 exact_assertions= 8530 vertex_sets_explicit=yes parity_monotonicity=yes`. The checker is a transcription and finite-case check; the preceding proof is valid for every integer \(n\ge2\) and real \(t\ge1\).

## Relationship to prior work

Zhang–Meng–Wu (2022, arXiv:2207.05499v1) study exact and bounded Banach–Mazur distances between classical coordinate \(\ell_p^3\) spaces and \(\ell_\infty^3\), rather than a directional-sum clipping constraint in arbitrary dimension. Deza–Hiriart-Urruty–Pournin (2020, arXiv:2011.05607v1) study cube intersections with coordinate-\(\ell_1\) balls, which constrain \(\sum_i|x_i|\), not \(|\sum_i x_i|\), and emphasize face structures and volumes. Gotoh–Uryasev (2015) study polyhedral norms with signed-coordinate-permutation symmetry, including \(\ell_1\)/\(\ell_\infty\) mixtures; their defining norm families do not have the single distinguished diagonal functional present here. The cube-to-crosspolytope special-dimensional work of Kobos–Varivoda (2023/2024) does not give the stated parametric family. Other work on one-sided halfcubes or capped hypercubes determines John or Löwner ellipsoids rather than the unrestricted Banach–Mazur distance for this centrally symmetric, *two-sided* slab.

The known regular-hexagon endpoint in dimension two and standard fixed-norm endpoint facts are not claimed to be new. A previously known exact result for \(\max\{\|x\|_1,t|\sum_i x_i|\}\) does **not** imply this theorem merely by exchanging \(\ell_1\) and \(\ell_\infty\): the two parameterized unit balls are crosspolytope versus cube truncations and polarity changes intersections into convex hulls. The new content is the full unrestricted-distance formula for the directionally truncated cube, its optimizer and opposite parity monotonicity.

## Limitations

The theorem covers the stated real spaces and \(t\ge1\), not \(0<t<1\), weighted or oblique clipping functionals, complex Hilbert targets, or arbitrary polyhedral intersections. The selected optimal quadratic form is unique only within the permutation-invariant family. Finite checks are not a proof of the universal statement, and incomplete indexing of older centrally clipped-cube literature leaves residual historical-priority uncertainty. No independent mathematical audit has been performed.

## References

1. L. Zhang, L. Meng and S. Wu, *Banach-Mazur Distance from \(\ell_p^3\) to \(\ell_\infty^3\)*, arXiv:2207.05499v1, first posted 2022-07-12; https://arxiv.org/abs/2207.05499.
2. A. Deza, J.-B. Hiriart-Urruty and L. Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607v1, first posted 2020-11-11; https://arxiv.org/abs/2011.05607.
3. J.-Y. Gotoh and S. Uryasev, *Two pairs of families of polyhedral norms versus \(\ell_p\)-norms: proximity and applications in optimization*, Mathematical Programming 156 (2016), 391–431; DOI: 10.1007/s10107-015-0899-9 (first online 2015).
4. T. Kobos and M. Varivoda, *On the Banach–Mazur Distance in Small Dimensions*, arXiv:2305.06427v1, first posted 2023-05-10; https://arxiv.org/abs/2305.06427.
