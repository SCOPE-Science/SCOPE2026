# Sharp Godbersen coefficient penalty for macroscopic Cartesian decompositions

## Finding
Let \(m\ge2\), \(d_1,\ldots,d_m\ge1\), and \(n=d_1+\cdots+d_m\). Let \(K_i\subset\mathbb R^{d_i}\) be full-dimensional compact convex bodies, and put \(K=K_1\times\cdots\times K_m\). For \(1\le j\le n-1\), define the normalized reflected mixed-volume coefficient
\[
R_{n,j}(K)=\frac{V_n(K[n-j],(-K)[j])}{\binom nj\operatorname{vol}_n(K)},
\]
where \(V_n\) is Minkowski-normalized mixed volume. Define
\[
B_{\mathbf d,j}=\frac{1}{\binom nj^2}\sum_{\substack{0\le h_i\le d_i\\h_1+\cdots+h_m=j}}\prod_{i=1}^m\binom{d_i}{h_i}^{\!2}.
\]
**Sharp finite-dimensional coefficient bound:**
\[
\boxed{R_{n,j}(K)\le B_{\mathbf d,j},}
\]
with equality if and only if every factor \(K_i\) is a simplex (one-dimensional segments count as simplices). Moreover, \(B_{\mathbf d,j}\) is exactly the collision probability of two independent multivariate hypergeometric vectors recording how a uniformly random \(j\)-subset of \(n\) items intersects blocks of sizes \(d_1,\ldots,d_m\).

**Sharp high-dimensional limit:** Fix \(m\). For each \(n\) choose positive integer block sizes summing to \(n\) with \(d_{i,n}/n\to\alpha_i>0\), \(\sum_i\alpha_i=1\), and integers \(j_n/n\to\beta\in(0,1)\). Then
\[
\boxed{B_{\mathbf d_n,j_n}\sim\frac{n^{-(m-1)/2}}{[4\pi\beta(1-\beta)]^{(m-1)/2}\sqrt{\alpha_1\cdots\alpha_m}}.}
\]
Thus the right-hand side gives the **asymptotically sharp universal upper bound** for every such product of arbitrary convex factors, achieved by simplex factors. In the balanced two-factor and central-index case it is \(2/\sqrt{\pi n}\); for three equally large factors it is \(3\sqrt3/(\pi n)\).

## Assumptions and scope
All convex bodies are compact with nonempty interior in their own Euclidean factor subspaces; no smoothness or symmetry is imposed. Cartesian products use orthogonal coordinate subspaces, but the normalized result is unchanged under nonsingular affine images of the entire product. The block count \(m\) is fixed in the asymptotic assertion, each limiting \(\alpha_i\) is strictly positive, and the limiting index fraction \(\beta\) lies strictly between zero and one. No uniform endpoint estimate is asserted. Our normalization is fixed by the identity
\[
\operatorname{vol}_n(A+tB)=\sum_{j=0}^n\binom nj V_n(A[n-j],B[j])t^j.
\]
The input Godbersen inequality and its equality classification for arbitrary convex bodies are prior published theorems, not claims established here.

## Proof
**Step 1: Exact product generating function.** For each factor put
\[
q_{i,h}=\frac{\binom{d_i}{h}V_{d_i}(K_i[d_i-h],(-K_i)[h])}{\operatorname{vol}_{d_i}(K_i)}\quad(0\le h\le d_i).
\]
By Minkowski's polynomial formula and the exact volume product for Cartesian factors,
\[
\frac{\operatorname{vol}_n(K+t(-K))}{\operatorname{vol}_n(K)}
=\prod_{i=1}^m\left(\sum_{h=0}^{d_i}q_{i,h}t^h\right).
\]
All coefficients are nonnegative. The Godbersen--Makai inequality, proved by Kotrbatý and Mouamine and generalized by Fryš, Kotrbatý, Mouamine and Wang, gives
\[
q_{i,h}\le\binom{d_i}{h}^{\!2}\qquad(0\le h\le d_i).
\]
Consequently, comparison of coefficients of \(t^j\) gives
\[
\binom nj R_{n,j}(K)
\le\sum_{\sum_i h_i=j}\prod_i\binom{d_i}{h_i}^{\!2};
\]
this is exactly the first displayed bound. A simplex attains every component inequality, so every product of simplices attains it. Conversely, suppose a factor of dimension \(d_i\ge2\) is not a simplex. The known strict equality characterization makes its coefficient inequality strict whenever \(1\le h\le d_i-1\). For any \(1\le j\le n-1\), choose
\[
h_i=\max\{1,j-(n-d_i)\}.
\]
Then \(1\le h_i\le d_i-1\) and \(0\le j-h_i\le n-d_i\). Hence the other factors admit integers \(h_k\in[0,d_k]\) summing to \(j-h_i\). This gives a strictly smaller positive summand, and hence strictness of the product inequality. If all factors have dimension one they already are simplices.

**Step 2: Hypergeometric collision identity.** Divide the preceding coefficient bound by \(\binom nj\). If \(H=(H_1,\ldots,H_m)\) records block counts of a uniform \(j\)-subset of an \(n\)-element set partitioned into the indicated blocks, its probability at \(h\) is
\[
p(h)=\Pr(H=h)=\frac{\prod_i\binom{d_i}{h_i}}{\binom nj}.
\]
Consequently, \(B_{\mathbf d,j}=\sum_h p(h)^2=\Pr(H=H')\) for independent copies \(H,H'\). This identity is exact for every admissible finite index. For simplex factors the right-hand side is also exactly their normalized opposite-body mixed volume; it is not just an upper bound.

**Step 3: Uniform local expansion.** Write \(a_{i,n}=d_{i,n}/n\), \(b_n=j_n/n\), and \(r=m-1\). Parameterize feasible lattice vectors by their first \(r\) coordinates and set
\[
z_i=(h_i-b_nd_{i,n})/\sqrt n\quad(1\le i\le r),\qquad z_m=-\sum_{i=1}^r z_i.
\]
Fix \(\varepsilon=1/10\) and restrict to the central window \(|z_i|\le n^\varepsilon\) for all \(i\). Because every \(a_{i,n}\to\alpha_i>0\) and \(b_n\to\beta\in(0,1)\), all factorial arguments in \(p(h)\) are bounded below by a fixed positive multiple of \(n\). Uniform Stirling expansion of the logarithm of the exact factorial formula gives
\[
 p(h)=\frac{1+o(1)}{[2\pi n b_n(1-b_n)]^{r/2}\sqrt{\prod_i a_{i,n}}}
 \exp\!\left[-\frac{1}{2b_n(1-b_n)}\sum_{i=1}^m\frac{z_i^2}{a_{i,n}}\right].
\]
The error is uniform in that window: cubic Taylor remainders are \(O(n^{-1/2+3\varepsilon})=o(1)\), and the Stirling prefactor error is \(o(1)\). Outside the window the hypergeometric Hoeffding bound for sampling without replacement gives \(\Pr(\max_i|H_i-\mathbb EH_i|>n^{1/2+\varepsilon})\le 2m\exp(-c n^{2\varepsilon})\) for a fixed \(c>0\). Hence the contribution to \(\sum_h p(h)^2\) from outside is exponentially small, since each \(p(h)\le1\).

**Step 4: Exact Gaussian integral and sharp constant.** Put \(u=(z_1,\ldots,z_r)\) and
\[
Q=\operatorname{diag}(\alpha_1^{-1},\ldots,\alpha_r^{-1})+\alpha_m^{-1}\mathbf1\mathbf1^{\mathsf T}.
\]
The matrix determinant lemma gives \(\det Q=(\prod_i\alpha_i)^{-1}\). In the first \(r\) integer count coordinates the rescaled lattice spacing is \(n^{-1/2}\), and therefore the squared local probabilities converge after the Riemann-sum normalization to a Gaussian integral. Explicitly,
\[
\int_{\mathbb R^r}\exp\!\left[-\frac{u^{\mathsf T}Qu}{\beta(1-\beta)}\right]du
=\pi^{r/2}[\beta(1-\beta)]^{r/2}\sqrt{\prod_i\alpha_i}.
\]
Multiplying this integral by the squared Stirling prefactor and the lattice density \(n^{r/2}\) gives
\[
\lim_{n\to\infty}n^{r/2}B_{\mathbf d_n,j_n}
=[4\pi\beta(1-\beta)]^{-r/2}(\prod_i\alpha_i)^{-1/2}.
\]
The tail estimate permits unrestricted passage from the central window to the full collision sum. This proves the stated asymptotic, and simplex factors attain the finite-dimensional bound for every \(n\).

## Verification
The accompanying standard-library script `code/check_coefficients.py` checks the independent exact integer polynomial-convolution formula against direct enumeration of two matching multivariate hypergeometric configurations in \(37\) index instances. It separately tests the coefficient bound for a planar triangle--rectangle product against the triangle--triangle extremal product. At balanced two-factor dimensions \(n=60,120,240,480\), the scaled ratios to the predicted constant were approximately \(0.989604,0.994797,0.997397,0.998698\); at balanced three-factor dimensions \(n=60,120,240\), the ratios were approximately \(0.975211,0.987552,0.993763\). The analytic argument, not these finite computations, proves the theorem for all permitted dimensions and every convex factor.

## Relationship to prior work
The 2026 solution of Godbersen's inequality supplies precisely the factorwise coefficient upper bounds and their simplex equality cases; we do not reprove or claim them as new. The present observation is the sharp product-specific convolution with a hypergeometric collision interpretation, and especially the explicit sharp high-dimensional decay constant when a fixed number of factor dimensions and the mixed-volume index grow proportionally. Alon, Elboim, Pach and Tardos independently identify multivariate hypergeometric collision probabilities and obtain the exponent \((1-m)/2\) in a balanced-color necklace problem, but do not state this sharp constant for arbitrary proportions and sampling fractions or a reflected-mixed-volume product bound. Chen, Tang, Wang and Yang study \(\sum_h\binom dh^2 t^h\) via coefficientwise log-convexity, not the constrained multi-factor collision coefficient asymptotic. A published Cartesian-product law for the two-body Bézout coefficient concerns two unrelated auxiliary bodies and has a different normalization and invariant; a published one-vertex simplex-truncation profile concerns a nonproduct family and different parameter scaling. Neither statement contains this conclusion.

## Limitations
The result is asymptotically sharp for a fixed number of factors with positive limiting dimension proportions and an interior limiting mixed-volume index, but it supplies no uniform bounds when factors stay small, the number of factors diverges, or the index approaches an endpoint. The collision-local-limit calculation uses standard Stirling and concentration arguments; its probability exponent has independent precedent, so no claim of a new probabilistic central-limit theorem is made. Independent historical priority validation has not been performed, and earlier unindexed tensorization literature may contain equivalent formulations. The finite verification cannot establish the general analytic or geometric theorem by itself.

## References
1. F. Fryš, J. Kotrbatý, M. A. Mouamine, S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (first public 2026-10-05), https://arxiv.org/abs/2610.06806 .
2. J. Kotrbatý, M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387 (first public 2026-07-22), https://arxiv.org/abs/2607.20387 .
3. O. Friedland, E. Putterman, M. Szusterman, *Equality case in the Kotrbatý--Mouamine inequality*, arXiv:2610.04527 (first public 2026-10-03), https://arxiv.org/abs/2610.04527 .
4. N. Alon, E. Elboim, J. Pach, G. Tardos, *Random necklaces require fewer cuts*, arXiv:2112.14488 (2021), https://arxiv.org/abs/2112.14488 (especially the hypergeometric collision argument in Section 2).
5. W. Y. C. Chen, R. L. Tang, L. X. W. Wang, A. L. B. Yang, *The q-Log-convexity of the Generating Functions of the Squares of Binomial Coefficients*, arXiv:0810.2247 (2008), https://arxiv.org/abs/0810.2247 .
