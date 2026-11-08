# A dimension-seven/eight reversal in sharp Grassmannian fourth moments

## Finding

Let \(n\ge5\) be an integer, let \(P\) be the orthogonal projector onto a Haar-uniform unoriented two-plane in \(\mathbb R^n\), and let \(A\) be a nonzero real symmetric trace-free \(n\times n\) matrix. Put
\[
F_A(P)=\operatorname{tr}(AP),\qquad S_2=\operatorname{tr}(A^2),\qquad S_4=\operatorname{tr}(A^4),\qquad \rho(A)=S_4/S_2^2.
\]
The fourth-moment quotient has the exact formula
\[
K_n(A):=\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}
=\frac{3n(n-1)(n+2)}{(n-2)^2(n+1)(n+4)(n+6)}
\left[n^2+2n+8+2(n^2-6n-8)\rho(A)\right].\tag{1}
\]
Set
\[
b_n=\begin{cases}1/n,&n\text{ even},\\(n^2+3)/(n(n^2-1)),&n\text{ odd},\end{cases}\qquad
u_n=\frac{n^2-3n+3}{n(n-1)},\tag{2}
\]
and denote the right side of (1), with \(\rho(A)\) replaced by \(t\), by \(k_n(t)\). The sharp endpoint interval is
\[
\boxed{\begin{array}{ll}
k_n(u_n)\le K_n(A)\le k_n(b_n),&5\le n\le7,\\
k_n(b_n)\le K_n(A)\le k_n(u_n),&n\ge8.
\end{array}}\tag{3}
\]
All values in either interval occur. Every equality case is as follows, up to multiplying \(A\) by a nonzero scalar and orthogonal conjugation:

* At \(\rho(A)=u_n\), the spectrum is \((n-1,-1,\ldots,-1)\).
* At \(\rho(A)=b_n\), the spectrum has two levels, with multiplicities \(k=\lfloor n/2\rfloor\) and \(n-k\), proportional to \((n-k)\) and \(-k\), respectively. When \(n\) is even these are equally numerous opposite eigenvalues.

Thus the maximum changes from the balanced spectrum to the single-outlier spectrum precisely between dimensions seven and eight; the minimum changes in the opposite direction. This is a strict change because \(n^2-6n-8\ne0\) for every integer \(n\ge5\).

There are exact nonnegative spectral deficit identities. Let
\[
C_n=\frac{6n(n-1)(n+2)|n^2-6n-8|}{(n-2)^2(n+1)(n+4)(n+6)}>0.
\]
For \(5\le n\le7\) the lower and upper deficits are, respectively, \(C_n(u_n-\rho(A))\) and \(C_n(\rho(A)-b_n)\). For \(n\ge8\), they are \(C_n(\rho(A)-b_n)\) and \(C_n(u_n-\rho(A))\).

The real normed space \(X_n=\{F_A:\operatorname{tr}A=0,\ A=A^{\mathsf T}\}\subset L^4(\operatorname{Gr}(2,n))\) has dimension \(n(n+1)/2-1\). Its exact Euclidean Banach--Mazur distance is
\[
\boxed{d_{\mathrm{BM}}(X_n,\ell_2^{\,n(n+1)/2-1})=\left(\frac{K_{n,\max}}{K_{n,\min}}\right)^{1/4}.}\tag{4}
\]
Here \(K_{n,\min},K_{n,\max}\) are the endpoints in (3); the invariant \(L^2\) Euclidean structure is optimal among *all* Euclidean structures, not only invariant ones.

## Assumptions and scope

All matrices and functions are real. The Grassmannian measure is Haar-invariant probability, not unnormalized volume. The exponent is exactly four. The trace-free hypothesis ensures \(\mathbb EF_A=0\). The map \(A\mapsto F_A\) is injective on trace-free symmetric matrices because its second moment is strictly positive there. No result is claimed for different ranks of the random projector, other exponents, complex matrices, or non-Haar measures.

## Proof

**Moment calculation.** Choose the two orthonormal columns \(u,v\) of a Haar Stiefel frame sequentially: \(u\) is uniform on the sphere \(\mathbb S^{n-1}\), and conditional on \(u\), the vector \(v\) is uniform on the sphere in \(u^\perp\). Write \(Q=I-uu^{\mathsf T}\) and
\[
x=u^{\mathsf T}Au,\quad y=u^{\mathsf T}A^2u,\quad z=u^{\mathsf T}A^3u,\quad w=u^{\mathsf T}A^4u.
\]
The conditional quadratic-form traces \(t_j=\operatorname{tr}((QAQ)^j)\) are
\[
\begin{aligned}
t_1&=-x,\\
t_2&=S_2-2y+x^2,\\
t_3&=S_3-3z+3xy-x^3,\\
t_4&=S_4-4w+4xz+2y^2-4x^2y+x^4,
\end{aligned}\tag{5}
\]
where \(S_3=\operatorname{tr}(A^3)\). For a uniform vector on a sphere of dimension \(d-1\), the first four moments of the quadratic form with trace power sums \(t_j\) equal
\[
\frac{t_1}{d},\quad\frac{t_1^2+2t_2}{d(d+2)},\quad
\frac{t_1^3+6t_1t_2+8t_3}{d(d+2)(d+4)},\quad
\frac{t_1^4+12t_1^2t_2+12t_2^2+32t_1t_3+48t_4}{d(d+2)(d+4)(d+6)}.\tag{6}
\]
Apply (6) with \(d=n-1\) to \(v^{\mathsf T}Av\), expand \((x+v^{\mathsf T}Av)^4\), and then average over \(u\) using spherical quadratic-form moments. The relevant unconditional identities include
\[
\begin{aligned}
\mathbb E x^4&=\frac{12S_2^2+48S_4}{n(n+2)(n+4)(n+6)},&
\mathbb E(x^2y)&=\frac{2S_2^2+8S_4}{n(n+2)(n+4)},\\
\mathbb E y^2&=\frac{S_2^2+2S_4}{n(n+2)},&
\mathbb E(xz)&=\frac{2S_4}{n(n+2)},\\
\mathbb E x^2&=\frac{2S_2}{n(n+2)},&
\mathbb E y&=\frac{S_2}{n},\quad \mathbb E w=\frac{S_4}{n}.
\end{aligned}\tag{7}
\]
Terms involving \(S_3\mathbb Ex\) vanish. Substitution yields the exact two moment identities
\[
\boxed{\mathbb EF_A^2=\frac{4(n-2)S_2}{n(n-1)(n+2)},\qquad
\mathbb EF_A^4=\frac{48[(n^2+2n+8)S_2^2+2(n^2-6n-8)S_4]}{n(n-1)(n+1)(n+2)(n+4)(n+6)}.}\tag{8}
\]
Division gives (1).

**Spectral extremum lemma (proved here).** For any real numbers \(a_1,\ldots,a_n\) satisfying \(\sum a_i=0\), \(\sum a_i^2>0\), and \(n\ge4\),
\[
b_n\le \frac{\sum a_i^4}{(\sum a_i^2)^2}\le u_n.\tag{9}
\]
All extremizers have precisely two distinct coordinate values. Indeed, on the compact zero-sum unit sphere a critical point of \(\sum a_i^4\) satisfies \(4a_i^3-2\lambda a_i-\mu=0\), so there are at most three distinct coordinates. If there were three distinct values \(a,b,c\), then their sum would be zero (the cubic has no quadratic term). Vary one chosen coordinate of each value along the circle of triples with fixed sum zero and fixed squared sum; by the identity \(a^4+b^4+c^4=\frac12(a^2+b^2+c^2)^2\), their fourth-power sum is unchanged. Because \(n\ge4\), at least one other coordinate stays fixed. For a generic nearby variation there are four distinct coordinates, contradicting the same cubic stationarity condition at another global extremum. Thus no global extremum has three distinct values. Two-level zero-sum vectors with multiplicities \(k\) and \(n-k\) are proportional to \(((n-k)\text{ repeated }k,\ -k\text{ repeated }n-k)\), with fourth ratio
\[
\frac{n}{k(n-k)}-\frac3n.\tag{10}
\]
This is maximal exactly at \(k=1\) or \(n-1\) and minimal at the balanced integers \(k=\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\). Formula (9), including all equality cases, follows.

Apply (9) to the eigenvalues of \(A\). In (1) the slope in \(\rho\) has the sign of \(n^2-6n-8\), negative for integers \(5\le n\le7\) and positive for integers \(n\ge8\). This gives (3), all equality patterns and all exact deficits. Connectedness of the nonzero trace-free symmetric unit sphere and continuity of (1) imply that the full closed interval is attained.

**Optimal Euclidean distortion.** The \(L^4\) norm on \(X_n\) is invariant under \(A\mapsto UAU^{\mathsf T}\), \(U\in O(n)\). Suppose any positive definite quadratic form \(H\) gives a Euclidean norm with two comparison constants. Average the inequalities for this quadratic form over \(O(n)\). The resulting average \(\overline H\) has no larger distortion and is \(O(n)\)-invariant. On the real trace-free symmetric matrices the only invariant positive quadratic forms are multiples of \(\operatorname{tr}(A^2)\) (equivalently, the conjugation representation is irreducible). Hence the \(L^2\) norm is an optimal Euclidean norm, and its optimal comparison ratio is exactly (4).

## Verification

Run `python verify_grassmann.py` with SymPy installed. The script symbolically reduces the two-step spherical integration for an indeterminate dimension \(n\), proves the rational polynomial moment identities, checks the \(L^2\) normalization, and independently verifies the fourth-moment coefficients by exact Dirichlet integration for several dimensions and three nontrivial spectral patterns. It also checks the strict transition and endpoint ordering for many integer dimensions. Finite checks are supporting evidence; equations (5)–(10) provide the dimension-uniform proof.

For example, the exact sharp normalized fourth-moment intervals are \([203/99,7756/2673]\) at \(n=5\), \([1971/715,80163/28600]\) at \(n=7\), and \([25/9,65/21]\) at \(n=8\). The equality patterns switch their roles across the latter two dimensions.

## Relationship to prior work

Ehler, Gräf and Király (2015) give a zonal-polynomial formula for all trace moments of rotationally invariant projection ensembles and explicitly evaluate the first three. Their general theorem permits computation of the fourth moment, but does not give the simplified formula (8), the optimization over all trace-free \(A\), the extremizer reversal at dimensions seven/eight, or the Euclidean distortion (4). Grinberg and Rubin (2004) develop a different Grassmannian Radon-transform theory rather than sharp fourth moments. Bodmann, Ehler and Gräf (2017) study moment reconstruction from projections, not this sharp spectral norm classification. These theories provide context and methods rather than a stated sharp result. The dimension-four case is not included; the first genuinely varying family here starts at \(n=5\).

## Limitations

The dimension-uniform calculation is proved only for *rank-two real orthogonal projections* and exponent four. The bounds do not claim a new general integration formula superseding zonal-polynomial methods, nor optimal quantitative distance-to-orbit estimates beyond the exact spectral deficit. A hidden equivalent extremal inequality in older literature remains a bibliographic risk. No independent external validation has been performed.

## References

1. M. Ehler, M. Gräf, F. J. Király, *Phase retrieval using random cubatures and fusion frames of positive semidefinite matrices*, arXiv:1505.05003v1 (first public version 19 May 2015), especially Section 7 and Theorems 7.2–7.3. https://arxiv.org/abs/1505.05003
2. E. L. Grinberg, B. Rubin, *Radon inversion on Grassmannians via Gårding–Gindikin fractional integrals*, Ann. Math. 159 (2004), 783–817. https://doi.org/10.4007/annals.2004.159.783
3. B. G. Bodmann, M. Ehler, M. Gräf, *From Low- to High-Dimensional Moments Without Magic*, J. Theoret. Probab. 31 (2018), 2167–2193 (first published 14 September 2017). https://doi.org/10.1007/s10959-017-0785-x
