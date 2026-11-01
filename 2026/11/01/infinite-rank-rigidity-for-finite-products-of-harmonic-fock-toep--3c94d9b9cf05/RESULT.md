# Infinite-rank rigidity for finite products of harmonic Fock Toeplitz operators

## Finding

For every positive integer \(N\), a finite product of Toeplitz operators whose symbols are harmonic entire functions of exponential type on the Gaussian Fock space has **either zero or infinite algebraic rank**. More precisely, writing \(\varphi_j=f_j+\overline{g_j}\),

\[
\operatorname{rank}\bigl(T_{\varphi_1}\cdots T_{\varphi_N}\bigr)<\infty
\quad\Longleftrightarrow\quad
\text{some }\varphi_j\equiv0.
\]

The rank is measured on the canonical common invariant dense domain defined below; the statement does not presume bounded extensions of these generally unbounded operators. The conclusion is stronger than the previously established zero-product equivalence.

## Assumptions and scope

Equip the one-variable Fock space with measure \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). Its unnormalized kernels are \(K_a(z)=e^{z\overline a}\). For \(\varphi=f+\overline g\), require both \(f\) and \(g\) to be entire and satisfy, for some positive constants depending on the function, \(|f(z)|\le Ce^{R|z|}\) and likewise for \(g\). The Toeplitz operator is the Gaussian orthogonal compression \(T_{\varphi}h=\Pi(\varphi h)\), defined on the common invariant dense domain

\[
\mathcal H(\mathbb C)=\left(\bigcup_{0<c<1/2}\left\{h:he^{-c|\cdot|^2}\in L^\infty(\mathbb C)\right\}\right)\cap\mathcal O(\mathbb C).
\]

Every kernel \(z\mapsto e^{zw}\), \(w\in\mathbb C\), belongs to this domain. For a linear map defined on this domain, algebraic rank means the vector-space dimension of its image, not a Schatten rank of an unspecified extension.

We use the *proved* analytic-kernel representation and zero-product theorem of Liu–Qin–Huang (2026): for the product \(P\),

\[
(Pe^{w\cdot})(z)=e^{zw}V(z,w),\qquad
|V(z,w)|\le Ce^{R(|z|+|w|)},
\]

with an entire function \(V\); moreover \(V\equiv0\) if and only if one of the symbols is identically zero. These are Theorem 1.2 and the recursion (4.2)–(4.3) in the cited paper, including the jointly exponential-type estimate.

## Proof

**Borel separation lemma.** Let \(s>0\), and suppose \(h_1,\ldots,h_m\) are nonzero entire functions satisfying \(|h_j^{(n)}(0)|\le C_js^n\) for all integers \(n\ge0\). Choose \(\rho>s\). If complex numbers \(a_1,\ldots,a_m\) satisfy \(|a_i-a_j|>2\rho\) whenever \(i\ne j\), then the functions \(w\mapsto e^{a_jw}h_j(w)\) are linearly independent.

To prove this, absorb hypothetical nonzero relation coefficients into the \(h_j\), discarding zero coefficients. Define the Borel transform

\[
\mathscr Bh(\lambda)=\sum_{n=0}^{\infty}\frac{h^{(n)}(0)}{\lambda^{n+1}},
\qquad |\lambda|>s.
\]

The derivative bounds give absolute convergence and \(\mathscr Bh(\lambda)=O(1/|\lambda|)\) at infinity. Expanding the binomial series (or differentiating the product at zero) proves

\[
\mathscr B(e^{a\cdot}h)(\lambda)=\mathscr Bh(\lambda-a)
\]

for sufficiently large \(|\lambda|\). If \(\sum_j e^{a_jw}h_j(w)\equiv0\), linearity therefore makes

\[
H(\lambda)=\sum_{j=1}^m\mathscr Bh_j(\lambda-a_j)
\]

vanish near infinity. Since the closed disks \(\overline D(a_j,\rho)\) are disjoint, their common exterior is connected. The identity theorem forces \(H\equiv0\) throughout that exterior. Fix \(j\). For \(i\ne j\), the transform \(\mathscr Bh_i(\lambda-a_i)\) is holomorphic on a neighborhood of \(\overline D(a_j,\rho)\). The identity \(H=0\) thus analytically continues \(\mathscr Bh_j(\lambda-a_j)\) across its own excluded disk. This continuation is entire and tends to zero at infinity, so Liouville's theorem makes it identically zero. Every derivative \(h_j^{(n)}(0)\) vanishes, contradicting \(h_j\ne0\). The lemma follows. Notice that the argument uses the entire **complex** spectral parameter; real-axis growth comparisons alone would not suffice.

**Apply the lemma to the Fock kernel.** Assume that all \(\varphi_j\) are nonzero. The quoted zero-product theorem implies \(V\not\equiv0\). Choose \(w_0\) so that \(z\mapsto V(z,w_0)\) is not identically zero. Its zero set is discrete. Therefore, given any positive integer \(m\), we may select distinct real numbers \(a_1,\ldots,a_m\), arbitrarily far apart, such that \(V(a_j,w_0)\ne0\) for every \(j\).

By joint exponential type, the functions \(h_j(w)=V(a_j,w)\) are entire of exponential type with a **common** derivative-bound base \(s\); the multiplicative constants may depend on the selected sites. Indeed, Cauchy's estimates give such an \(s\) for the uniform bound \(Ce^{R(|z|+|w|)}\). Choose the sites with mutual gaps exceeding \(2\rho\) for some fixed \(\rho>s\). The Borel separation lemma proves that

\[
w\longmapsto(Pe^{w\cdot})(a_j)=e^{a_jw}V(a_j,w),\qquad 1\le j\le m,
\]

are linearly independent entire functions.

Were \(\operatorname{rank}P<m\), the \(m\) evaluation functionals \(h\mapsto h(a_j)\), restricted to the finite-dimensional image of \(P\), would be linearly dependent. That dependence, evaluated on every kernel \(e^{w\cdot}\), would contradict the displayed independence. Hence \(\operatorname{rank}P\ge m\). Since \(m\) is arbitrary, \(\operatorname{rank}P=\infty\).

If any symbol is zero, its Toeplitz factor and therefore the whole product vanish on the invariant domain; the algebraic rank is zero. Both implications follow.

## Verification

The critical checks are analytic rather than numerical: (i) the joint exponential-type kernel representation and its nonvanishing criterion are explicit in the motivating paper; (ii) the Borel series converges under the stated derivative bounds; (iii) its exponential-shift law follows coefficient by coefficient; (iv) the complement of finitely many pairwise disjoint closed disks is connected; (v) other shifted Borel transforms extend through the selected disk, forcing the remaining transform to extend entire and vanish by Liouville; (vi) finite rank forces a dependence of evaluation rows, contradicting the lemma. These steps prove the result for all finite \(N\) and arbitrarily large finite rank thresholds, not just a computed sample.

## Relationship to prior work

Liu–Qin–Huang, *Finite zero products of Toeplitz operators with harmonic symbols* (arXiv:2610.30209v1, October 21, 2026), establish nonvanishing of all finite products for nonzero harmonic exponential-type symbols. The result here strengthens **nonzero** to **infinite algebraic rank** using a new Borel-transform separation argument; the original paper's introduction distinguishes zero-product problems from finite-rank problems.

Bauer and Le (2011) establish rank-one obstruction for a **single** Toeplitz operator of a more general symbol class and explicitly leave higher ranks open. Agbor (2017) addresses two-factor, quasi-homogeneous radial-symbol situations on a related pluriharmonic Fock model. Cui, Li, and Lu (arXiv:2610.09728v1, 2026) establish an infinite-rank statement for **slant Toeplitz operators on the disk Bergman space**, not the ordinary Gaussian Fock products considered here. A published related result for finite-frequency exponential-polynomial Fock symbols establishes zero-divisor freeness, without this general infinite-rank theorem.

## Limitations

The statement is restricted to one complex variable, finite products, and harmonic symbols with both entire components of exponential type, on the specifically stated invariant domain. No assertions are made for arbitrary bounded measurable symbols, multidimensional Fock spaces, compactness, or Schatten-class behavior of an unspecified bounded realization. The conclusion depends on the previously proved kernel representation and zero-product theorem. Possible equivalent results in older analytic-symbol calculus remain a publication-priority risk; independent mathematical verification has not been performed.

## References

1. Y. Liu, J. Qin, and S. Huang, *Finite zero products of Toeplitz operators with harmonic symbols*, arXiv:2610.30209v1 (2026), especially Theorem 1.2, Lemma 2.1, and equations (4.2)–(4.3). https://arxiv.org/html/2610.30209v1
2. W. Bauer and T. Le, *Algebraic properties and the finite rank problem for Toeplitz operators on the Segal–Bargmann space*, J. Funct. Anal. **261** (2011), 2617–2640, Section 5. https://www.math.utoledo.edu/~tle20/Data/Algebraic2011.pdf
3. D. Agbor, *Algebraic properties of Toeplitz operators on the pluri-harmonic Fock space*, Journal of Mathematics Research **9** (2017), 67–78, Section 6.
4. P. Cui, R. Li, and Y. Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1 (2026).
