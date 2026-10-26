# Exact narrow-band eigenvalue constants for circular prolate concentration

## Finding
Fix \(\alpha>-\tfrac12\). For each \(c>0\), let \(H_c^{\alpha}\) be the self-adjoint finite Hankel transform on \(L^2(0,1;dx)\) with integral kernel
\[
 K_c^{\alpha}(x,y)=\sqrt{cxy}\,J_{\alpha}(cxy),\qquad 0<x,y<1.
\]
Let \(Q_c^{\alpha}=c(H_c^{\alpha})^2\), with eigenvalues \(\lambda_{\alpha,0}(c)\ge\lambda_{\alpha,1}(c)\ge\cdots\ge0\), repeated with multiplicity. For every fixed integer \(n\ge0\),
\[
 \boxed{\lim_{c\downarrow0}\frac{\lambda_{\alpha,n}(c)}{c^{4n+2\alpha+2}}=
 \left[\frac{1}{2^{\alpha+2n+1}(2n+\alpha+1)n!\,\Gamma(n+\alpha+1)\binom{2n+\alpha}{n}^{2}}\right]^2.}
\]
In particular, every fixed adjacent pair of positive concentration eigenvalues satisfies \(\lambda_{\alpha,n+1}(c)/\lambda_{\alpha,n}(c)\sim (L_{\alpha,n+1}/L_{\alpha,n})^2c^4\), where \(L_{\alpha,n}\) denotes the positive quantity in square brackets.

## Assumptions and scope
The Hilbert space is the real or complex \(L^2(0,1;dx)\); its inner product has Lebesgue normalization, not weighted radial measure. Bessel \(J_{\alpha}\) has its standard series. The generalized binomial coefficient is \(\binom{2n+\alpha}{n}=\Gamma(2n+\alpha+1)/(\Gamma(n+1)\Gamma(n+\alpha+1))\). The asymptotic is for fixed \(\alpha>-\tfrac12\) and fixed \(n\in\{0,1,2,\ldots\}\) as positive \(c\) tends to zero. No uniformity in \(n\) or \(\alpha\) is claimed.

## Proof
**Step 1 (rank-one Bessel series).** Write \(u_k(x)=x^{\alpha+2k+1/2}\) and
\[
 b_k=\frac{(-1)^k}{2^{\alpha+2k}k!\,\Gamma(k+\alpha+1)}.
\]
The Bessel series gives the trace-norm convergent expansion
\[
 H_c^{\alpha}=c^{\alpha+1/2}\sum_{k=0}^{\infty}b_k c^{2k}\,|u_k\rangle\langle u_k|.
\]
Indeed, \(\|u_k\|_2^2=1/[2(\alpha+2k+1)]\), so the series of rank-one trace norms converges absolutely and locally uniformly for bounded \(c\). Here \(|u\rangle\langle u|\) denotes \(f\mapsto\langle f,u\rangle u\).

**Step 2 (separation of every fixed singular mode).** For any integer \(m\ge1\), apply the exterior-power identity (first for finite sums, then in trace norm):
\[
 \bigwedge^m H_c^{\alpha}=c^{m(\alpha+1/2)}
 \sum_{0\le k_1<\cdots<k_m}\left(\prod_{j=1}^m b_{k_j}\right)c^{2\sum_{j=1}^m k_j}
 |u_{k_1}\wedge\cdots\wedge u_{k_m}\rangle
 \langle u_{k_1}\wedge\cdots\wedge u_{k_m}|.
\]
The unique minimizing tuple for \(\sum k_j\) is \((0,1,\ldots,m-1)\). The next possible sum is larger by at least one. Absolute trace-norm convergence therefore implies
\[
 c^{-m(\alpha+1/2)-m(m-1)}\bigwedge^m H_c^{\alpha}
 \longrightarrow \left(\prod_{k=0}^{m-1}b_k\right)|U_m\rangle\langle U_m|
 \quad\text{in trace norm},
\]
where \(U_m=u_0\wedge\cdots\wedge u_{m-1}\). In particular the limit has operator norm \(\prod_{k=0}^{m-1}|b_k|\det G_m\), where \(G_m=(\langle u_j,u_k\rangle)_{0\le j,k<m}\), and \(\det G_0:=1\). The determinant is positive because the monomials are linearly independent. Since the norm of the \(m\)-th exterior power equals the product \(\prod_{j=0}^{m-1}s_j(H_c^{\alpha})\) of the largest singular values, taking successive ratios gives
\[
 s_n(H_c^{\alpha})\sim c^{\alpha+1/2+2n}|b_n|\frac{\det G_{n+1}}{\det G_n}.
\]
The multiplicity convention is thus handled without assumptions about the signs of eigenvalues of \(H_c^{\alpha}\).

**Step 3 (Jacobi Gram determinant).** Under \(t=x^2\), the monomials \(u_k\) have Gram entries
\[
 \langle u_j,u_k\rangle=\frac12\int_0^1 t^{\alpha+j+k}\,dt=\frac{1}{2(\alpha+j+k+1)}.
\]
By Gram-Schmidt, \(\det G_{n+1}/\det G_n\) is the squared norm \(h_{\alpha,n}\) of the monic polynomial of degree \(n\) orthogonal for the measure \(\tfrac12 t^\alpha\,dt\) on \([0,1]\). The shifted Jacobi polynomial \(P_n^{(0,\alpha)}(2t-1)\) has squared norm \(1/(2n+\alpha+1)\) in \(t^\alpha dt\) and leading coefficient \(\binom{2n+\alpha}{n}\). Therefore
\[
 h_{\alpha,n}=\frac{1}{2(2n+\alpha+1)\binom{2n+\alpha}{n}^2}.
\]
Substitute \(|b_n|\) and \(h_{\alpha,n}\) into Step 2.

**Step 4 (positive concentration eigenvalues).** The nonnegative eigenvalues of \(Q_c^{\alpha}=c(H_c^{\alpha})^2\) are \(\lambda_{\alpha,n}(c)=c\,s_n(H_c^{\alpha})^2\). Squaring Step 2 and inserting Step 3 yields the displayed limit. The constant is strictly positive, hence the adjacent-mode ratio follows.

## Verification
The companion `check.py` uses high-precision orthogonal-polynomial Gram-Schmidt and a truncated Bessel rank-one series to check twelve finite ratios for \(\alpha\in\{0,\tfrac12\}\), \(c\in\{0.2,0.4\}\), and \(n\in\{0,1,2\}\), plus the shifted Jacobi norm identity. Run `python check.py` with Python 3 and the `mpmath` package installed. These numerical experiments corroborate, but do not replace, the exterior-power convergence proof for all fixed \(n\).

## Relationship to prior work
Boulsane and Karoui (2017) define the same \(H_c^{\alpha}\) and \(Q_c^{\alpha}\) operators and give comparison estimates and index-decay bounds for their eigenvalues. Boulsane (2020) studies non-asymptotic bounds and large-bandwidth spectral distribution, while Boulsane (2022) studies circular-prolate series in Hankel Sobolev spaces. The statement here instead supplies an exact coefficient for **every fixed index** in the **small-bandwidth** regime. Such constants do not follow by substituting \(c\downarrow0\) into estimates aimed at \(n\to\infty\) or large \(c\). The 1964 foundational circular-prolate article of Slepian remains a historical-priority comparison risk because its full text was not available for the present comparison; no claim of exhaustive literature coverage is made.

## Limitations
No estimate uniform as \(n\to\infty\), no large-bandwidth eigenvalue law, and no independently validated priority claim is asserted. The constants depend on the specific kernel and Lebesgue normalization above. The convergence argument does not give an explicit uniform error bound in the two-variable \((n,c)\) regime. A prior exact formula in inaccessible historical literature remains a possible priority risk.

## References
1. M. Boulsane and A. Karoui, *The finite Hankel transform operator: Some explicit and local estimates of the eigenfunctions and eigenvalues decay rates*, arXiv:1701.04622v1 (first public 2017-01-17), https://arxiv.org/abs/1701.04622.
2. M. Boulsane, *Non-asymptotic behavior and the distribution of the spectrum of the finite Hankel transform operator*, arXiv:2002.00170v1 (first public 2020-02-01), https://arxiv.org/abs/2002.00170.
3. M. Boulsane, *Approximation in Hankel Sobolev Space by Circular prolate spheroidal series*, arXiv:2206.04319v1 (first public 2022-06-09), https://arxiv.org/abs/2206.04319.
4. D. Slepian, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty—IV: Extensions to Many Dimensions; Generalized Prolate Spheroidal Functions*, Bell System Technical Journal (1964), https://doi.org/10.1002/j.1538-7305.1964.tb01037.x. Full article not inspected.
