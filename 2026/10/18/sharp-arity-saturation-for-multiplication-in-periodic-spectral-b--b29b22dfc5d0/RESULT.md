# Sharp arity saturation for multiplication in periodic spectral Barron spaces

## Finding

For every integer \(d\ge1\), every real \(s\ge0\), and every integer \(m\ge2\), consider the \(m\)-linear pointwise multiplication map
\[
M_m:(B^s(\mathbb T^d))^m\longrightarrow B^s(\mathbb T^d),\qquad
(f_1,\ldots,f_m)\longmapsto f_1\cdots f_m,
\]
where
\[
\|f\|_{B^s(\mathbb T^d)}
=\sum_{k\in\mathbb Z^d}(1+|k|^2)^{s/2}|\widehat f(k)|.
\]
Its **exact multilinear operator norm**, in every dimension and independently of the number of factors, is
\[
\boxed{\|M_m\|=(5/4)^{s/2}\qquad(m\ge2,\ d\ge1,\ s\ge0).}
\]
For \(s>0\), among tuples of single Fourier characters, equality holds precisely when exactly two or exactly three factors have the same nonzero frequency \(e_j\) or \(-e_j\) (for one coordinate \(j\)), and the remaining factors have zero frequency. Thus the operator norm is attained by explicit trigonometric monomials. No classification of non-monomial extremizers is asserted.

As one consequence, for each \(m\ge2\),
\[
\|f^m\|_{B^s(\mathbb T^d)}\le(5/4)^{s/2}\|f\|_{B^s(\mathbb T^d)}^m.
\]
This is an upper bound on the diagonal power map; sharpness of that restriction for each \(m\) is not claimed.

There is a sharp distinction from the analogous Euclidean weighted Fourier-\(L^1\) spaces: for \(s>0\) and \(d\ge1\), the \(m\)-linear product norm on \(\mathbb R^d\) satisfies
\[
\|M_m^{\mathbb R^d}\|\ge
\left(\frac{m+1}{(1+1/m)^m}\right)^{s/2}
\sim(m/e)^{s/2}\qquad(m\to\infty),
\]
so it cannot remain bounded as the arity increases.

## Assumptions and scope

The torus is \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\), with normalized Haar measure and Fourier characters \(x\mapsto e^{ik\cdot x}\). All functions and Fourier coefficients are complex-valued. The Euclidean length \(|k|\) is used in the weight. The smoothness \(s\) is any nonnegative real number; dimension \(d\) is any positive finite integer; arity \(m\) is any integer at least two. The space \(B^s(\mathbb T^d)\) is precisely the weighted Fourier-\(\ell^1\) space in Choulli–Lu–Takase, Section 4.5. Its Fourier series converge absolutely, justifying coefficient convolution.

The multilinear norm is the supremum of \(\|f_1\cdots f_m\|_s/\prod_j\|f_j\|_s\) over nonzero input factors. For the Euclidean comparison we use the Fourier-\(L^1\) norm \(\int_{\mathbb R^d}(1+|\xi|^2)^{s/2}|\widehat f(\xi)|\,d\xi\), with any consistent Fourier convention for which products correspond to convolution. The comparison is a lower bound only.

## Proof

**1. Exact reduction to lattice frequencies.** Write \(w_s(k)=(1+|k|^2)^{s/2}\). For finitely supported Fourier coefficients, the convolution identity and triangle inequality give
\[
\left\|\prod_{i=1}^{m}f_i\right\|_s
\le\sum_{k_1,\ldots,k_m\in\mathbb Z^d}
 w_s(k_1+\cdots+k_m)\prod_i|\widehat f_i(k_i)|.
\]
Therefore, with
\[
C_{s,m,d}=
\sup_{k_1,\ldots,k_m\in\mathbb Z^d}
\frac{w_s(k_1+\cdots+k_m)}{\prod_i w_s(k_i)},
\]
we have \(\|M_m\|\le C_{s,m,d}\). Conversely, substituting the individual characters \(f_i(x)=e^{ik_i\cdot x}\) realizes every ratio, so equality holds: \(\|M_m\|=C_{s,m,d}\). Nonnegative absolute summability and Tonelli then extend the upper bound from trigonometric polynomials to all \(B^s\) inputs once finiteness is established.

**2. Optimization over the nonzero frequencies.** Fix a frequency tuple and let \(n\) be the number of its nonzero entries. If \(n=0\) or \(n=1\), its squared-weight ratio is \(1\). Otherwise let \(r_i=|k_i|\ge1\) be the lengths of its \(n\ge2\) nonzero entries and \(S=\sum_i r_i\). The triangle inequality yields
\[
Q:=\frac{1+|\sum_i k_i|^2}{\prod_i(1+|k_i|^2)}
\le F_n(r_1,\ldots,r_n)
:=\frac{1+S^2}{\prod_{i=1}^n(1+r_i^2)}.
\]
For every coordinate \(r_i\ge1\), holding all other lengths fixed,
\[
\frac12\frac{\partial}{\partial r_i}\log F_n
=\frac{S}{1+S^2}-\frac{r_i}{1+r_i^2}
=\frac{(S-r_i)(1-Sr_i)}{(1+S^2)(1+r_i^2)}<0.
\]
Indeed \(S-r_i\ge1\) and \(Sr_i\ge2\). Consequently \(F_n\) is strictly decreasing in every radius on the domain \([1,\infty)^n\), and
\[
Q\le F_n(1,\ldots,1)=h_n:=\frac{n^2+1}{2^n}.
\]
The exact values are \(h_2=h_3=5/4\), whereas \(h_n<5/4\) for \(n\ge4\) because
\[
\frac{h_{n+1}}{h_n}=
\frac{n^2+2n+2}{2(n^2+1)}<1\qquad(n\ge3).
\]
The cases \(n=0,1\) give only \(1\). Hence the supremum of \(Q\) over all finite frequency tuples is exactly \(5/4\), attained already at \((e_1,e_1,0,\ldots,0)\), and also at \((e_1,e_1,e_1,0,\ldots,0)\) when \(m\ge3\). For \(s\ge0\), raising this ratio to the power \(s/2\) gives the asserted exact norm, including \(s=0\).

**3. Character equality.** If \(s>0\), equality requires \(n\in\{2,3\}\); strict radial monotonicity forces every nonzero \(|k_i|=1\); and equality in the vector triangle inequality forces those unit vectors to be positively aligned. The only integer lattice vectors of Euclidean length one are \(\pm e_j\), so all nonzero frequencies must coincide with one such vector. Conversely every listed tuple attains equality.

**4. Euclidean contrast.** In continuous frequency space, take \(m\) nonnegative Fourier coefficient bumps of unit integral supported in shrinking neighborhoods of the same point \(m^{-1/2}e_1\). By continuity of the weight and dominated convergence after rescaling their supports, the ratio of the weighted Fourier-\(L^1\) norm of the product to the product of input norms tends to
\[
\left(\frac{1+|m\cdot m^{-1/2}e_1|^2}{(1+|m^{-1/2}e_1|^2)^m}\right)^{s/2}
=\left(\frac{m+1}{(1+1/m)^m}\right)^{s/2}.
\]
Since \((1+1/m)^m\to e\), this tends to infinity like \((m/e)^{s/2}\) as \(m\to\infty\) when \(s>0\). No assertion that the displayed Euclidean lower bound is optimal is needed.

## Verification

The standalone standard-library script `CHECK.py` tests the weight inequality using exact rational arithmetic for smoothness \(s=2\). It exhaustively enumerates 125,433 finite lattice frequency configurations in dimensions one through three; checks the precise single-character equality pattern; checks the exact model sequence and arity padding; and tests 2,400 deterministic finite coefficient products and the Euclidean comparison ratios. It reported 253,432 passing exact-rational assertions. Execute `python3 CHECK.py` after extracting this package. These are finite diagnostics; the proof above, not exhaustive enumeration, establishes the unbounded-dimensional and unbounded-arity theorem.

## Relationship to prior work

Choulli, Lu, and Takase establish the weighted Fourier-\(\ell^1\) spectral Barron spaces on tori. Their equations (2.6)–(2.7) bound the two-factor product by \(2^{s/2}\); Section 4.3 treats general Peetre-type constants and Section 4.5 defines the higher-dimensional spaces. Neither statement yields an arity-independent sharp norm, and iterating the displayed estimate gives \(2^{s(m-1)/2}\) instead of the exact \((5/4)^{s/2}\). The framework and Fourier-convolution reduction are acknowledged as known; the novel assertion here is the exact lattice-frequency maximization simultaneously for all arities.

Potts and Schmischke study weighted Wiener norms under ANOVA coordinate projections and high-dimensional approximation. Their Theorem 3.11 concerns inherited smoothness, not multiplicative multilinear norms. Nguyen, Nguyen, and Sickel study \(s\)-numbers of weighted Wiener embeddings; their Section 2.2 explicitly places the question of algebra structure outside their scope. The general concept of weighted Fourier-\(\ell^1\) convolution is classical and is not claimed as new.

## Limitations

The sharp result uses integer-lattice frequency spacing and the specific isotropic weight \((1+|k|^2)^{s/2}\). It is not asserted for negative smoothness, anisotropic or rescaled weights, or arbitrary compact groups. Only extremizing tuples of **single characters** are classified; full equality classification for arbitrary Fourier mixtures is open here. Although the bound applies to \(f^m\), its sharpness when all \(m\) factors must be identical is not claimed for \(m\ge4\). The Euclidean assertion is a lower bound, not an exact Euclidean norm formula. As with any literature comparison, an older equivalent sharp weighted-convolution result might exist under different terminology; the literature checks do not amount to independent priority verification.

## References

1. M. Choulli, S. Lu, H. Takase, *Spectral Barron spaces of periodic functions*, arXiv:2610.06169v1 (first public version 2026-10-05), especially Sections 2.2, 4.3 and 4.5. https://arxiv.org/html/2610.06169v1
2. D. Potts, M. Schmischke, *Approximation of high-dimensional periodic functions with Fourier-based methods*, arXiv:1907.11412, especially Theorem 3.11. https://arxiv.org/pdf/1907.11412
3. V. D. Nguyen, V. K. Nguyen, W. Sickel, *s-Numbers of Embeddings of Weighted Wiener Algebras*, arXiv:2011.07663, especially Section 2.2. https://arxiv.org/pdf/2011.07663
