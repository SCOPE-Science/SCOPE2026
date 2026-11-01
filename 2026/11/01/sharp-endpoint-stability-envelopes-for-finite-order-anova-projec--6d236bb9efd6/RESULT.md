# Sharp endpoint stability envelopes for finite-order ANOVA projections

## Finding

Consider an integer \(d\ge1\), an integer \(0\le k\le d\), and finite nontrivial sets \(X_i\) with \(|X_i|=q_i\ge2\). Put a strictly positive probability distribution \(\mu_i\) on each \(X_i\), and let \(\mu=\bigotimes_{i=1}^{d}\mu_i\). Let \(P_{\le k}\) be the real \(L^2(\mu)\)-orthogonal projector onto the sum of the ANOVA (Hoeffding) interaction spaces indexed by subsets of at most \(k\) coordinates, including constants.

Write \(r_i=\min_{a\in X_i}\mu_i(a)\). Let independent \(B_i\) satisfy \(\Pr(B_i=1)=r_i\), and set \(Z_i=B_i/r_i-1\). Then the **exact, attained endpoint norm** is
\[
\boxed{\|P_{\le k}\|_{L^\infty(\mu)\to L^\infty(\mu)}
 =\mathbb E\left|\sum_{\substack{S\subseteq\{1,\ldots,d\}\\ |S|\le k}}\prod_{i\in S}Z_i\right|.}
\tag{1}
\]
A maximizing kernel row uses, in every coordinate, an atom of minimum probability; the sign of that row is an extremizing input. The right side is nonincreasing in each \(r_i\). Consequently, for prescribed alphabet sizes \(q_i\), **uniform marginals globally minimize this norm** among all strictly positive product measures.

The **sharp universal supremum over all strictly positive product measures**, for the prescribed nontrivial alphabet sizes, depends only on \(d\) and \(k\):
\[
\boxed{\sup_{\mu_1,\ldots,\mu_d}\|P_{\le k}\|_{\infty\to\infty}
 =M_{d,k}:=\sum_{j=0}^{k}(-1)^{k-j}2^j\binom dj,\qquad 0\le k\le d.}
\tag{2}
\]
For \(k<d\), the bound is approached by making one atom in every factor arbitrarily rare; at \(k=d\), the projection is the identity and its norm is \(1\). The quantity \(M_{d,0}=1\), while \(M_{d,1}=2d-1\) and \(M_{d,2}=2d(d-2)+1\) whenever the displayed orders are allowed. In particular, for \(d=4\), the sharp envelopes for \(k=0,1,2,3,4\) are \(1,7,17,15,1\): nested target spaces do **not** force monotone endpoint projection amplification. For each fixed nonnegative \(k\) and increasing \(d>k\), the envelope grows as \(2^kd^k/k!+O(d^{k-1})\).

## Assumptions and scope

All spaces and kernels are real. The finite probability spaces have full support, so \(L^\infty\) is the maximum norm and every row sign is a legitimate input. The case \(d=1\) and the boundary orders \(k=0,d\) are included. Empty products equal one. No symmetry or equal alphabet size is assumed. The minimum over fixed alphabets allows all strictly positive marginals but does not assert uniqueness. The supremum in (2), rather than an attained maximum, is used to permit strictly positive probabilities tending to zero.

For each coordinate \(i\), let \(E_i\) average over the \(i\)-th factor while leaving the other factors fixed. The ANOVA summand indexed by \(S\) is the image of \(\prod_{i\in S}(I-E_i)\prod_{j\notin S}E_j\); different summands are mutually orthogonal in \(L^2(\mu)\).

## Proof

**1. Orthogonal kernel and exact row norm.** The projectors \(E_i\) are commuting self-adjoint idempotents in \(L^2(\mu)\). Therefore
\[
P_{\le k}=\sum_{\substack{S\subseteq[d]\\ |S|\le k}}
\prod_{i\in S}(I-E_i)\prod_{j\notin S}E_j
\]
is precisely the stated orthogonal projector. Its integral kernel relative to \(\mu\) is
\[
K_k(x,y)=\sum_{\substack{S\subseteq[d]\\ |S|\le k}}
\prod_{i\in S}\left(\frac{\mathbf 1_{\{x_i=y_i\}}}{\mu_i(x_i)}-1\right).
\tag{3}
\]
With \(x\) fixed, independent \(y_i\sim\mu_i\) make the equality indicators independent Bernoulli variables having parameters \(p_i=\mu_i(x_i)\). The finite-matrix \(L^\infty\) norm is the maximum of the absolute kernel-row integrals:
\[
\|P_{\le k}\|_{\infty\to\infty}=
\max_{x\in X}\mathbb E\left|\sum_{|S|\le k}\prod_{i\in S}\left(\frac{B_i}{p_i}-1\right)\right|.
\tag{4}
\]
For each fixed row, choosing \(f(y)=\operatorname{sgn}K_k(x,y)\) yields equality. Here any choice in \([-1,1]\) is allowed where the kernel vanishes.

**2. Reverse convex ordering and localization at rare atoms.** Fix the distributions of all factors except \(i\), and put \(W_p=B_p/p\) where \(B_p\) has success probability \(p\in(0,1)\). For any real \(t\),
\[
\mathbb E(W_p-t)_+=
\begin{cases}1-t,&t<0,\\ (1-pt)_+,&t\ge0.\end{cases}
\]
The mean of \(W_p\) is one, and the stop-loss characterization of convex order implies \(W_p\) dominates \(W_{p'}\) in convex order whenever \(p\le p'\). Indeed the formula above directly establishes the necessary inequality for every \(t\). Conditional on all other factors, the polynomial inside the absolute value in (4) is affine in \(W_p\), so its absolute value is convex in \(W_p\). Independence permits one coordinate at a time to be replaced by its rarer law, never decreasing the expected absolute value. Thus every maximizing row may be chosen with \(p_i=r_i\), proving (1) and its monotonicity. Because \(r_i\le1/q_i\) and equality is achieved by the uniform marginal, the claimed uniform-minimization result follows.

**3. Exact universal envelope.** First take \(0\le k<d\). Expanding the ANOVA projectors in coordinate-averaging operators, and using the alternating binomial identity, gives
\[
P_{\le k}=\sum_{\substack{R\subseteq[d]\\ |R|\le k}}
 c_{|R|}\prod_{i\notin R}E_i,
\quad c_t=\sum_{h=0}^{k-t}(-1)^h\binom{d-t}{h}
 =(-1)^{k-t}\binom{d-t-1}{k-t}.
\tag{5}
\]
Every averaging product has \(L^\infty\) norm one. The triangle inequality thus gives
\[
\|P_{\le k}\|_{\infty\to\infty}
\le\sum_{t=0}^k\binom dt\binom{d-t-1}{k-t}.
\tag{6}
\]
The coefficients in this expression are positive integers. Set each \(r_i=\varepsilon\) by assigning an atom mass \(\varepsilon\) in every coordinate and distributing the remaining positive mass over the other \(q_i-1\) atoms (for sufficiently small \(\varepsilon\)). Consider the row at these rare atoms. Let \(T=\{i:B_i=1\}\) be its matching-coordinate set. Formula (5) says that the kernel there equals
\[
K_k(T)=\sum_{\substack{R\subseteq T\\ |R|\le k}}c_{|R|}\varepsilon^{-|R|}.
\]
For every fixed \(T\) with \(|T|=t\le k\), multiplication by its probability \(\varepsilon^t(1-\varepsilon)^{d-t}\) gives a contribution to the absolute row integral tending to \(|c_t|=\binom{d-t-1}{k-t}\). If \(t>k\), that contribution is \(O(\varepsilon^{t-k})\) and tends to zero. There are \(\binom dt\) sets \(T\) of size \(t\). Hence the bound (6) is sharp as a supremum. Finally,
\[
\sum_{t=0}^k\binom dt\binom{d-t-1}{k-t}
 =[z^k]\frac{(1+2z)^d}{1+z}
 =\sum_{j=0}^k(-1)^{k-j}2^j\binom dj,
\tag{7}
\]
where the coefficient equality follows by summing the binomial series
\(\sum_{h\ge0}\binom{d-t-1}{h}z^h=(1+z)^{d-t-1}\) and the binomial theorem. This proves (2) for \(k<d\). For \(k=d\), every ANOVA summand is included, so \(P_{\le d}=I\); the right side of (2) is \((2-1)^d=1\), as required.

**4. Consequences.** Direct substitution in (2) yields the displayed small-order values and the nonmonotone \(d=4\) sequence. For fixed \(k\), its leading term is \(2^k\binom dk\), while all preceding terms have degree at most \(k-1\) in \(d\); this gives the final asymptotic statement.

## Verification

A standalone exact-rational checker (`verify.py`) independently constructs complete finite matrices using (3) and computes their true maximum absolute row sums for 990 combinations of factor profiles and truncation orders. It independently evaluates the Bernoulli expression, checking exact equality in each case. A further 140 exact checks test monotonicity and the sharp upper bound; 21 rare-atom instances test convergence to (2); and 105 binomial tests check the identity (7). These finite computations do not prove the all-dimension theorem: its complete proof is the analytical argument above.

## Relationship to prior work

Kuo, Sloan, Wasilkowski, and Woźniakowski's *On decompositions of multivariate functions* establishes general ANOVA decompositions via commuting projections and develops a finite-order coefficient compression formula (Theorem 2.1, Example 2.2, and Section 5). In particular, the coefficients underlying (5) are classical and are **not claimed to be new**. Their paper does not determine the endpoint norms on all nonuniform finite products, the rare-atom extremal envelope, or the uniform-minimization principle.

Dick and Gnewuch's *Optimal randomized changing dimension algorithms for infinite-dimensional integration on function spaces with ANOVA-type decomposition* studies projection and error bounds in weighted Hilbert spaces for integration algorithms. It does not establish the stated \(L^\infty\) sharp product-measure norm formula or its optimization. A previously known sharp formula for degree-at-most-one Bernoulli projections is a special case of (1); neither that special case nor the endpoint norm for a **homogeneous degree-two** Hamming Fourier projection covers the arbitrary-order *cumulative* projector. The present claim concerns the exact full finite-product formula, the uniform-minimizer property for arbitrary alphabets, and the all-order sharp envelopes, not the existence of ANOVA decompositions or their classical combinatorial expansions.

## Limitations

Only finite product measures with strictly positive atom masses, real \(L^2\)-orthogonal ANOVA projectors, and the full real \(L^\infty\) norm are considered. The result does not classify general correlated measures, nonproduct weights, projections that select irregular interaction families, or higher \(L^p\) norms. The supremum in (2) is approached by positive distributions tending to the boundary, not asserted to be attained by positive probabilities. While close primary works have been compared, an equivalent formula hidden in older ANOVA, tensor-projection, or probability literature remains a priority risk; no independent validation has been performed.

## References

1. F. Y. Kuo, I. H. Sloan, G. W. Wasilkowski, and H. Woźniakowski, *On decompositions of multivariate functions*, Mathematics of Computation 79 (2010), 953–966. Electronically published November 20, 2009. DOI: 10.1090/S0025-5718-09-02319-9. Public full-text preprint: https://web.maths.unsw.edu.au/~fkuo/pubs/preprint/ksww09-decomp.pdf.
2. J. Dick and M. Gnewuch, *Optimal randomized changing dimension algorithms for infinite-dimensional integration on function spaces with ANOVA-type decomposition*, arXiv:1306.2821, version publicly posted June 12, 2013, https://arxiv.org/abs/1306.2821.
3. *Exact degree-two Hamming projection norms and the Gaussian–Poisson crossover*, publicly available mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-degree-two-hamming-projection-norms-and-the-gaussian-poiss--cd09d9ad5ea2.
