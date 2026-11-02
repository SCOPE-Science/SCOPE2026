# An alphabet-independent first positivity threshold for Gaussian kernels on Hamming products

## Finding
For every integer \(n\ge 2\) and every integer alphabet size \(r\ge2\), let \(X_{n,r}=\{0,\ldots,r-1\}^n\), equipped with its ordinary (unscaled) Hamming distance \(d_H\). For \(0<q<1\), define the real symmetric matrix
\[
K_{n,r}(q)_{x,y}=q^{d_H(x,y)^2},\qquad x,y\in X_{n,r}.
\]
Set
\[
F_n(q)=\sum_{j=0}^n(-1)^j\binom njq^{j^2},\qquad
u_n=\frac1n+\frac1{n^3}.
\]
There exists exactly one \(q_n\in(0,\nu_n]\) with \(F_n(q_n)=0\); more precisely,
\[
\frac1n<q_n<\frac1n+\frac1{n^3}<\frac1{n-1}.
\]
The matrix \(K_{n,r}(q)\) is positive definite for every \(0<q<q_n\), is positive semidefinite with nullity exactly \((r-1)^n\) at \(q=q_n\), and is indefinite for every \(q_n<q\le\nu_n\). This is an *exact first-loss threshold*, the same for every alphabet size \(r\), not a claim about all larger \(q\).

As \(n\to\infty\), the threshold and its Gaussian inverse bandwidth satisfy
\[
q_n=\frac1n+\frac1{2n^3}-\frac1{2n^4}+\frac1{n^5}-\frac2{n^6}+O(n^{-7}),
\]
\[
-\log q_n=\log n-\frac1{2n^2}+\frac1{2n^3}-\frac7{8n^4}+O(n^{-5}).
\]
In particular, for every fixed \(0<c<1\), \(K_{n,r}(c/n)\) is positive definite for all sufficiently large \(n\), whereas for every fixed \(c>1\), it has a negative eigenvalue for all sufficiently large \(n\). Both statements are uniform in arbitrary integer choices \(r=r(n)\ge2\). Equivalently, the associated unital Schur multiplier \(A\mapsto K_{n,r}(q)\circ A\) is completely positive up to and including the first threshold, and fails even positivity immediately above it.

## Assumptions and scope
The distance \(d_H(x,y)\) counts unequal coordinates. The kernel has entries \(\exp(-t d_H(x,y)^2)\) with \(t=-\log q>0\), *not* \(\exp(-t d_H(x,y))\), nor a Euclidean Gaussian in which squared Euclidean distance represents Hamming distance. Matrix definiteness is over real or complex vectors, with the same result. The parameter \(q\) increases from zero (equivalently, \(t\) decreases from infinity). Nullity counts dimensions over \(\mathbb C\); the real symmetric matrix has the same real nullity. No assertion about the entire interval \(q\in(\nu_n,1)\) is made.

## Proof
**(1) Exact Fourier spectrum.** Identify the alphabet with \(\mathbb Z/r\mathbb Z\) and \(X_{n,r}\) with its \(n\)-fold product. Every additive character diagonalizes the convolution matrix \(K_{n,r}(q)\). For a character nontrivial on exactly \(k\) coordinates, each of the other \(n-k\) coordinates contributes \(r-1\) when a nonzero group difference is selected; each nontrivial character has sum \(-1\) over nonzero differences. The resulting eigenvalue is
\[
\lambda_k^{(n,r)}(q)
=\sum_{a=0}^{n-k}\binom{n-k}{a}(r-1)^a
  \sum_{j=0}^k(-1)^j\binom kj q^{(a+j)^2},
\qquad k=0,\ldots,n.
\]
Its multiplicity is \(\binom nk(r-1)^k\). In particular \(\lambda_n^{(n,r)}(q)=F_n(q)\), independently of \(r\), with multiplicity \((r-1)^n\).

**(2) Bounds and uniqueness of the first zero.** Write \(u_n=1/n+1/n^3\), so \(u_n<1/(n-1)\). At \(q=1/n\), the leading terms \(1-nq\) cancel, and the remaining alternating terms \(\binom njq^{j^2}\), starting at \(j=2\), decrease strictly in magnitude. Hence \(F_n(1/n)>0\). For \(n\ge3\), the bound \(j^2\ge2j\) for \(j\ge2\) gives
\[
0\le\sum_{j=2}^n\binom nj u_n^{j^2}
\le\binom n2u_n^4(1+u_n^2)^{n-2}.
\]
Using \(u_n\le10/(9n)\) and \((n-2)/n^2\le1/8\), we obtain
\[
n^2\sum_{j=2}^n\binom nj u_n^{j^2}
\le\frac12\left(\frac{10}{9}\right)^4
\exp\left(\frac{(10/9)^2}{8}\right)<0.89<1.
\]
Because \(1-nu_n=-1/n^2\), this proves \(F_n(u_n)<0\). For \(n=2\) the same conclusion follows directly from \(F_2(5/8)=1-2(5/8)+(5/8)^4<0\).

Moreover, on \(0\le q\le u_n\),
\[
F_n'(q)\le-n+\sum_{j=2}^n\binom njj^2q^{j^2-1}
\le -n+2n(n-1)u_n^3(1+u_n^2)^{n-2}<0.
\]
The last strict inequality follows for \(n\ge3\) from
\[
2(n-1)u_n^3(1+u_n^2)^{n-2}
\le\frac4{27}\left(\frac{10}{9}\right)^3
\exp\left(\frac{(10/9)^2}{8}\right)<0.24,
\]
and for \(n=2\) by \(F_2'(q)=-2+4q^3<0\) on \([0,5/8]\). Thus \(F_n\) crosses zero precisely once on \([0,u_n]\), at \(q_n\) in the claimed interval.

**(3) No earlier competing Fourier mode.** For integers \(0\le k\le n\), \(0\le a\le n-k\), put
\[
g_{k,a}(q)=\sum_{j=0}^k(-1)^j\binom kj q^{(a+j)^2}.
\]
For \(k=0\), the sum is the single positive term \(q^{a^2}\). For \(k\ge1\) with \((k,a)\ne(n,0)\), the positive magnitudes \(\binom kjq^{(a+j)^2}\) decrease strictly from \(j=0\) onward throughout \(0<q\le u_n\): their first ratio is \(kq^{2a+1}\), bounded by \((n-1)u_n<1\) if \(a=0\), and by \((n-1)u_n^3<1\) if \(a\ge1\); subsequent ratios are smaller. Therefore the alternating sum \(g_{k,a}(q)>0\). Every term contributing to \(\lambda_k^{(n,r)}(q)\) is positive for \(k<n\), while \(\lambda_n^{(n,r)}(q)=F_n(q)\). The spectral claims, including exact nullity and the immediate negative mode, follow.

**(4) Sharp asymptotic.** Uniformly for \(q\in[1/n,u_n]\), the terms with \(j\ge3\) contribute \(O(n^{-6})\), using \(j^2\ge3j\) and the binomial tail bound. Consequently
\[
F_n(q)=1-nq+\binom n2q^4+O(n^{-6}),
\qquad F_n'(q)=-n+O(n^{-1}).
\]
Substitute the expansion \(q=1/n+a/n^3+b/n^4+c/n^5+d/n^6\) into this equation. Coefficient comparison gives \(a=1/2\), \(b=-1/2\), \(c=1\), \(d=-2\). Since \(|F_n'(q)|\) is of order \(n\) on the bracket, the \(O(n^{-6})\) residual moves its zero by only \(O(n^{-7})\). Expanding \(-\log q_n\) yields the second formula. Finally, \(F_n(c/n)=1-c+O(n^{-2})\) for each fixed \(c>0\), which gives the large-dimension dichotomy. The Schur-multiplier conclusion follows from the Schur product/Choi criterion; if \(K\) is indefinite, the multiplier maps the positive all-ones rank-one matrix to the indefinite matrix \(K\).

## Verification
The accompanying self-contained `checker.py` computes the eigenvalue formula with exact rational arithmetic, checks strict signs at the rational bracket endpoints in dimensions \(2\) through \(16\) for alphabets of sizes \(2,3,5\), and compares the Fourier spectrum to direct matrix-character multiplication on several small products. Execute `python checker.py`; the expected output is `FINITE CHECKS PASS 2074`. These finite tests corroborate the stated computations but do not substitute for the uniform inequalities above.

## Relationship to prior work
Da Costa, Mostajeran and Ortega (2023) study the Gaussian of *intrinsic circle distance* and show negative Fourier eigenvalues for increasingly fine circular samples. Li (2023) extends non-positivity to certain closed Riemannian manifolds. Those results motivate the positive-definiteness question but concern different metric spaces and do not imply this exact finite-Hamming transition. Classical product-group Fourier diagonalization provides the spectrum; the new assertion is that the highest degree loses positivity first at an alphabet-independent root, together with the multiplicity and sharp expansions. Existing Fourier/Krawtchouk treatments of Hamming schemes give general spectral machinery but not the explicit ordering of Gaussian squared-distance modes in the stated bracket. A 2026 applied Gaussian-process discussion notes that Gaussian–Hamming kernels need not be positive definite, without giving the first threshold. No global novelty theorem follows from a literature search; equivalent formulations in older association-scheme sources remain possible.

## Limitations
This result concerns the complete \(r\)-ary product with equally weighted coordinates, integers \(n\ge2\), \(r\ge2\), and the stated first-loss region. It does not classify all subsequent positivity intervals, weighted-coordinate Hamming metrics, restricted subsets, or noninteger alphabet models.

## References
- N. Da Costa, C. Mostajeran, J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (public 2023-02-21), https://arxiv.org/pdf/2302.10623.
- S. Li, *Gaussian kernels on non-simply-connected closed Riemannian manifolds are never positive definite*, arXiv:2303.06558v1 (public 2023-03-12), https://arxiv.org/pdf/2303.06558.
- L. Friedli et al., *Gaussian Process Modeling with Genotype × Environment Kernels for Wheat Performance Prediction*, Journal of Agricultural, Biological and Environmental Statistics (2026-08-23), https://doi.org/10.1007/s13253-026-00749-2; Sect. 3.3 concerns Gaussian–Hamming kernel validity, not the exact threshold.
- Classical finite-group Fourier diagonalization and the Schur multiplier positive-definiteness criterion, used as standard tools.
