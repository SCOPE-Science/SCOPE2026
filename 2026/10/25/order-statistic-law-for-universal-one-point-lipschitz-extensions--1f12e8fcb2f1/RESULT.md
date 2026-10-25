# Order-statistic law for universal one-point Lipschitz extensions of equilateral metrics

## Finding
Let \(n\ge2\), let \(X=\{x_1,\ldots,x_n\}\) have the unit equilateral metric, and adjoin a point \(o\) with \(r_i=d(o,x_i)>0\). Assume the triangle inequalities \(r_i+r_j\ge1\) and \(|r_i-r_j|\le1\) for distinct indices. After arranging the radii in nondecreasing order \(r_{(1)}\le\cdots\le r_{(n)}\), put \(R_k=\sum_{j=1}^k r_{(j)}\).

The least universal real-Banach-valued one-point Lipschitz extension factor is exactly
\[
\boxed{\Lambda(X,X\cup\{o\})=\max\left\{1,\max_{2\le k\le n}\frac{k-1}{R_k}\right\}.}
\]
Here *universal* means that the extension factor works for every real Banach target and every original Lipschitz map. The same sharp number is the minimum norm among **all real-linear constant-preserving scalar-valued** extension operators, including operators with signed interpolation coefficients.

One optimal extension is **positive** and works for every real Banach target: \(Ef(o)=\sum_{i=1}^n\alpha_i f(x_i)\), where \(\alpha_i\ge0\), \(\sum_i\alpha_i=1\), and \(\alpha_i\ge(1-\Lambda r_i)_+\). When \(\Lambda>1\), these weights are uniquely determined among nonnegative vectors:
\[
\boxed{\alpha_i=(1-\Lambda r_i)_+.}
\]
Thus varying the distances can switch off some source points entirely. For example, the compatible radii \((1/2,1/2,1/2,1,1)\) give \(\Lambda=4/3\) and weights \((1/3,1/3,1/3,0,0)\).

For \(n\ge3\), the largest value over every compatible radius tuple is \(2-2/n\), attained **only** at \(r_1=\cdots=r_n=1/2\). This extremal equiradial value was already known in the literature; the contribution here is the complete heterogeneous radius profile, the explicit optimal weights, and their support transitions, not the extremal numerical bound in isolation.

## Assumptions and scope
All spaces and scalars are real; target Banach spaces may be infinite-dimensional. The source metric satisfies \(d(x_i,x_j)=1\) for \(i\ne j\). The additional positive radii and stated triangle inequalities are precisely the conditions needed for the displayed distances to define a metric on the \(n+1\) distinct points. The extension agrees exactly with the source map. Lipschitz seminorms are used, so constant functions are preserved. If \(n=2\), the formula reads \(\Lambda=1\) for every valid pair of radii; in general \(\Lambda\ge1\) since the original points remain in the extension domain.

For the scalar statement, operators act from the real vector space of all functions on \(X\) to all functions on \(X\cup\{o\}\), agree with source values, are real-linear, preserve constants, and are normed by the induced Lipschitz seminorm. The Banach-target statement does not assume that an arbitrary extension procedure must be linear in the input; positivity gives a single universal construction anyway.

## Proof
**Step 1: positive coefficients and their norm.** If \(\alpha_i\ge0\) and \(\sum_i\alpha_i=1\), define \(Ef(o)=\sum_j\alpha_j f(x_j)\). For \(L=\operatorname{Lip}(f)\) and every \(i\),
\[
\|Ef(o)-f(x_i)\|\le\sum_{j\ne i}\alpha_j\|f(x_j)-f(x_i)\|\le(1-\alpha_i)L.
\]
Thus the extension factor is at most \(\max\{1,\max_i(1-\alpha_i)/r_i\}\). This bound is also sharp for that particular coefficient vector already for scalar source functions: the values \(f(x_i)=0\), \(f(x_j)=1\) for \(j\ne i\) have source Lipschitz seminorm one and attain the ratio \((1-\alpha_i)/r_i\).

**Step 2: no signed real-linear extension can do better.** Any constant-preserving scalar-linear extension is evaluation at the original points followed by a coefficient vector \(\alpha\in\mathbb R^n\) with \(\sum_i\alpha_i=1\). The sharp scalar oscillation norm of its difference from evaluation at \(x_i\) is
\[
T_i(\alpha)=\frac12\left(|\alpha_i-1|+\sum_{j\ne i}|\alpha_j|\right),
\]
by maximizing a zero-mass linear form over source functions taking values between zero and one. Write \(p_i=(\alpha_i)_+\), \(P=\sum_ip_i\ge1\), and \(\beta_i=p_i/P\). Direct sign checking gives
\[
T_i(\alpha)=P-\min\{p_i,1\},\qquad T_i(\beta)=1-\frac{p_i}{P}.
\]
If \(p_i\le1\), then \(T_i(\alpha)-T_i(\beta)=(P-1)(1-p_i/P)\ge0\). If \(p_i>1\), then \(T_i(\alpha)=P-1\ge (P-p_i)/P=T_i(\beta)\). Consequently replacing arbitrary signed coefficients by normalized positive coefficients never increases any source-to-new-point Lipschitz ratio. The old-point pairs contribute one in either case. Thus minimizing over positive weights loses no generality.

**Step 3: exact finite feasibility.** A nonnegative probability vector satisfying \((1-\alpha_i)/r_i\le c\) exists exactly when
\[
F(c):=\sum_{i=1}^n(1-cr_i)_+\le1.
\]
Indeed each coordinate must exceed \((1-cr_i)_+\); if their sum is at most one, distribute the leftover mass arbitrarily among coordinates. Moreover,
\[
F(c)=\max_{S\subseteq\{1,\dots,n\}}\left(|S|-c\sum_{i\in S}r_i\right).
\]
For sets of cardinality at most one, the right-hand expression is at most one for every \(c\ge0\) because all radii are positive. For a fixed cardinality \(k\ge2\), the most restrictive sum is the sum of the \(k\) smallest radii, \(R_k\). Hence \(F(c)\le1\) is equivalent to \(c\ge(k-1)/R_k\) for every \(2\le k\le n\). Incorporating preservation of the original Lipschitz norm gives the claimed closed formula and an explicit linear-time scan after sorting.

When \(\Lambda>1\), some \(k\ge2\) attains \((k-1)/R_k=\Lambda\), so \(F(\Lambda)=1\); the coordinate lower bounds already sum to one, forcing every optimal nonnegative coefficient to equal \((1-\Lambda r_i)_+\). In particular, \(\alpha_i>0\) holds exactly where \(\Lambda r_i<1\).

**Step 4: sharpness for arbitrary Banach targets.** Take the finite-dimensional real Banach space
\[
H=\left\{z\in\mathbb R^n:\sum_i z_i=0\right\},\qquad\|z\|_H=\frac12\sum_i|z_i|,
\]
and the isometric map \(f(x_i)=e_i-e_n\). Every putative extension value \(z\in H\) is uniquely expressible as \(z=\sum_i\alpha_i f(x_i)\) with \(\sum_i\alpha_i=1\). The distance to \(f(x_i)\) is exactly \(T_i(\alpha)\). Step 2 reduces its unrestricted minimax radius to the positive weight problem in Step 3. Therefore every extension into this particular Banach space requires factor at least \(\Lambda\). Together with Step 1 this proves sharpness simultaneously for universal Banach-valued extensions and the unrestricted real-linear scalar-valued extension norm.

**Step 5: the already-known sharp equiradial upper envelope and its equality geometry.** Suppose \(n\ge3\) and set \(c=2-2/n\). Define \(A=\{i:r_i<1/c\}\) and \(k=|A|\). If \(k\le1\), then \(F(c)<1\). If \(k\ge2\), summing the pairwise triangle constraints \(r_i+r_j\ge1\) over pairs from \(A\) yields \(\sum_{i\in A}r_i\ge k/2\). Hence
\[
F(c)=k-c\sum_{i\in A}r_i\le k(1-c/2)=k/n\le1.
\]
The exact formula implies \(\Lambda\le c\). Equality requires \(k=n\) and equality in all pairwise constraints on the full set; as \(n\ge3\), all radii must then be \(1/2\). Conversely these radii give \(\Lambda=2-2/n\). This step recovers the known worst-case equilateral-star value and identifies its unique metric equality case; it is not claimed as the source of the novel heterogeneous profile.

## Verification
A standalone standard-library rational-arithmetic checker accompanies this theorem. It checks ordered-partial-sum and positive-part feasibility identities on complete small rational parameter grids satisfying the metric conditions, verifies the exact norms by exhaustive Boolean source potentials and a finite grid of signed coefficient vectors, and includes the nonuniform support-switch example. An independent linear-programming computation also matched the exact formula to numerical precision for 466 compatible metric parameter choices of sizes two through eight. The algebraic argument in Steps 1--5, not the finite tests, proves the theorem for all finite dimensions and every admissible positive real radius vector.

## Relationship to prior work
Basso, *Absolute Lipschitz Extendability and Linear Projection Constants* (2021), Lemma 4.1, establishes the sharp universal **worst-case** constant \(2-2/n\) for an \(n\)-point equilateral source and realizes it at the equidistant added point. Therefore that number by itself is not a new discovery. The inspected proof does not give the exact extension factor for each prescribed **heterogeneous** tuple \((r_i)\), its sorted-partial-sum formula, or the support of optimal positive coefficients. Basso, *Lipschitz Extensions to Finitely Many Points* (2017), supplies general one-point bounds but not these heterogeneous equal-leaf-distance formulas.

Albiac, Ansorena, Cúth and Doucha (2020, primary MSC 46B03) give complementary projections of Lipschitz-free spaces in their analysis of doubling metric spaces; these are general projection frameworks rather than the sharp one-point finite metric profile derived here. The closest available previously published finite-metric calculations for equilateral metric stars with equal radii determine universal quasi-Banach-valued star constants and small-cardinality center behavior; their equiradial hypotheses do not imply the varied-radius formula. These comparisons concern mathematical implication, not merely matching titles. It remains possible that a classical finite-dimensional projection or interpolation treatment expresses an equivalent sorted-radius result under different terminology; there has been no independent literature certification.

## Limitations
The formula is for one added point, an equilateral source, real Banach targets and real-linear scalar-valued interpolation. It does not apply automatically to non-equilateral source metrics, arbitrary multiple-point extensions, or quasi-Banach targets with exponent below one. The already-published extremal equiradial value must not be presented independently as novel. Exhaustive finite checks are supporting evidence only, and both proof and literature comparisons await independent review.

## References
[1] F. Albiac, J. L. Ansorena, M. Cúth and M. Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555v1, first public 2020-05-13, primary MSC 46B03, especially Section 5. https://arxiv.org/abs/2005.06555

[2] G. Basso, *Absolute Lipschitz Extendability and Linear Projection Constants*, arXiv:2104.14238v1, first public 2021-04-29, especially Lemma 4.1 and Section 5. https://arxiv.org/abs/2104.14238

[3] G. Basso, *Lipschitz Extensions to Finitely Many Points*, arXiv:1707.06593v1, first public 2017-07-20, especially Section 4. https://arxiv.org/abs/1707.06593

[4] *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions*, published mathematical finding, 2026-10-11, for equiradial stars, online mathematical research record.

[5] *Sharp three-leaf star extension constants for real \(p\)-Banach targets*, published mathematical finding, 2026-10-11, for three equidistant leaves, online mathematical research record.
