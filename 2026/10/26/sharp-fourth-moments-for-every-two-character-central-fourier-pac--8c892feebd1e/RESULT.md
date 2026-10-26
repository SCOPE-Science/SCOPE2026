# Sharp fourth moments for every two-character central Fourier packet on \(SU(2)\)

## Finding
For any integers \(0\le n<m\), let \(\chi_j\) be the unnormalized irreducible character of highest weight \(j\) of \(SU(2)\), normalized by \(\|\chi_j\|_{L^2(SU(2))}=1\) under Haar probability measure. The sharp norm of the two-dimensional central Fourier packet is
\[
K_{n,m}=\max_{|a|^2+|b|^2=1}\|a\chi_n+b\chi_m\|_4^4.
\]
Write \(A=n+1\), \(B=m+1\), and \(k=m-n\).

**Opposite character parity (odd \(k\)).** If \(B<3A\), then
\[
K_{n,m}=B+\frac{(3A-B)^2}{5A-B},\qquad
u=\frac{3A-B}{5A-B},
\]
and precisely the extremizers are \((a,b)=\zeta(\sqrt{u},\pm\sqrt{1-u})\) for \(|\zeta|=1\). If \(B\ge3A\), then \(K_{n,m}=B\), and precisely the extremizers are \((a,b)=(0,\zeta)\) for \(|\zeta|=1\).

**Equal character parity (even \(k\)).** Put \(H=\max\{0,A-k/2\}\). The polynomial
\[
p(t)=A+(3A-B)t+3(H-A)t^2-2At^3-Ht^4
\]
has exactly one positive real root \(t_*\), counted with multiplicity. The exact sharp constant is
\[
K_{n,m}=\frac{At_*^4+4Ht_*^3+6At_*^2+4At_*+B}{(1+t_*^2)^2}>B,
\]
and precisely the extremizers are
\[
(a,b)=\frac{\zeta}{\sqrt{1+t_*^2}}(t_*,1),\qquad |\zeta|=1.
\]
Consequently, at arbitrarily large separation, same-parity character packets always benefit from nonzero mixing, whereas opposite-parity packets cease mixing sharply when \(B\ge3A\).

## Assumptions and scope
Characters are traces of the \((j+1)\)-dimensional irreducible representations, not divided by dimension. Haar measure has total mass one. A central Fourier packet is restricted to the stated two distinct irreducible characters, without additional matrix coefficients. Coefficients may be arbitrary complex numbers and \(K_{n,m}\) denotes the fourth power of the \(\ell^2\to L^4\) operator norm. The equality descriptions refer to unit-energy coefficient pairs; multiplying by any common nonzero complex scalar gives all nonzero maximizers of the homogeneous inequality.

## Proof
The Clebsch–Gordan product identity and Schur orthogonality imply
\[
\chi_r\chi_s=\sum_{j=|r-s|,\ |r-s|+2,\ldots,r+s}\chi_j,
\qquad \int_{SU(2)}\chi_r\chi_s\,dg=\delta_{rs}.
\]
In particular, \(\int\chi_n^4=A\), \(\int\chi_m^4=B\), and \(\int\chi_n^2\chi_m^2=A\). Comparing the step-two character lists in the fusion products also gives
\[
\int\chi_n^3\chi_m=H,\qquad
\int\chi_n\chi_m^3=J,
\]
where \(H=J=0\) when \(k\) is odd; when \(k\) is even, \(H=\max\{0,A-k/2\}\) and \(J=A\). Indeed, \(\chi_n^2\) contains each of \(\chi_0,\chi_2,\ldots,\chi_{2n}\) once, while \(\chi_n\chi_m\) contains each of \(\chi_k,\chi_{k+2},\ldots,\chi_{m+n}\) once. The common-term count is \(H\) for even \(k\), and zero for odd \(k\). The analogous overlap with \(\chi_m^2\) consists of \(n+1\) terms for even \(k\).

For \(a,b\in\mathbb C\), let \(x=\operatorname{Re}(a\overline b)\). The characters are real-valued, and direct expansion of \(|a\chi_n+b\chi_m|^4\) gives the **exact identity**
\[
\int|a\chi_n+b\chi_m|^4
=A|a|^4+B|b|^4+2A|ab|^2+4Ax^2+4H|a|^2x+4J|b|^2x.
\]
This determines the complex phase optimization, not merely real-coefficient bounds.

For odd \(k\), the last two terms vanish. Given \(|a|\), \(|b|\), maximize \(x^2\) by choosing relative phases \(0\) or \(\pi\). Writing \(u=|a|^2\) and \(1-u=|b|^2\), the optimized fourth moment is
\[
Q(u)=Au^2+B(1-u)^2+6Au(1-u)
=B+2(3A-B)u-(5A-B)u^2.
\]
When \(B<3A\) this strictly concave quadratic has its unique maximizer at the stated interior \(u\), and direct substitution gives the stated \(K_{n,m}\). When \(B\ge3A\), \(Q(u)\le B\) for every \(u\in[0,1]\), strictly if \(u>0\): indeed \(Q(u)-B\) is \(u\) times an affine function whose endpoint values are \(2(3A-B)\le0\) and \(A-B<0\). The equality conditions now follow exactly.

For even \(k\), write \(|a|=t|b|\), \(t\ge0\), and \(x=t|b|^2c\), \(-1\le c\le1\). After dividing by \((|a|^2+|b|^2)^2\), the phase dependence is a convex quadratic with leading term \(4At^2c^2\) and positive linear coefficient \(4Ht^3+4At\) for \(t>0\). Its unique maximum occurs at \(c=1\). At that phase the remaining expression is
\[
F(t)=\frac{At^4+4Ht^3+6At^2+4At+B}{(1+t^2)^2}.
\]
Direct differentiation gives \(F'(t)=4p(t)/(1+t^2)^3\). Since \(A>0\), \(0\le H\le A\), the nonzero coefficients of \(p\), ordered by descending degree, have exactly one sign change (irrespective of the sign of \(3A-B\)). Descartes' rule of signs gives at most one positive root counting multiplicity. As \(p(0)=A>0\) and \(p(t)\to-\infty\) for \(t\to\infty\), there is exactly one, and it is simple. Hence \(F\) rises strictly then falls strictly, and the stated \(t_*\) gives its unique global maximum. Since \(F'(0)=4A>0\) and \(F(0)=B\), this maximum is strictly greater than \(B\); since \(F(t)\to A<B\) at infinity, there is no missing boundary extremizer. This proves both the sharp constant and the complete complex equality family for every pair.

## Verification
The standalone `verify.py` constructs fusion products independently, computes the \(L^4\) fourth moment as the sum of squared character-product coefficients, and compares it against the claimed closed identity for many complex Gaussian-integer coefficient pairs. It symbolically verifies the derivative numerator and checks both parity branches and the positive critical-root formula using deterministic numerical grids. The recorded successful output is `verification_output.txt`. These finite and symbolic checks corroborate the proof; the argument above, including Descartes' rule and the exact fusion multiplicities, establishes all infinitely many pairs.

## Relationship to prior work
Kirilov–de Moraes–Ruzhansky (2019 preprint, 2020 journal) treats partial Fourier series of compact groups and motivates exact questions on small central character packets, but its smoothness and solvability conclusions do not give sharp packet fourth moments or equality cases. Dooley–Gupta (1996) studies norms of noncentral matrix-coefficient polynomials inside a single irreducible block, not the present central pair of distinct characters. A later published result on high-weight **fixed finite packets** establishes a parity-count leading asymptotic, \(K_m(S)=mC(e,o)+O_S(1)\); that statement does not imply this exact all-weights two-character formula, the distance-dependent transition, or all finite-degree maximizing phases. Conversely, for fixed opposite-parity separations the leading term here is consistent with its two-parity limit. The classical Clebsch–Gordan rule itself is not claimed as new.

## Limitations
Only two-dimensional central Fourier spans, \(L^4\), and the group \(SU(2)\) are treated. The algebraic root in the even-gap case is characterized uniquely but not expressed in radicals for every parameter pair. This does not give general sharp norms for three or more characters, noncentral blocks, or other compact groups. A complete exhaustive search of historical orthogonal-polynomial extremal inequalities is unavailable; an equivalent older two-Chebyshev norm formula remains a residual priority risk. No independent scientific audit or comprehensive priority certification has been performed.

## References
1. A. Kirilov, W. A. Almeida de Moraes, and M. Ruzhansky, *Partial Fourier series on compact Lie groups*, arXiv:1909.12824, first submitted 2019-09-27, later published in *Bulletin des Sciences Mathématiques* 160 (2020), article 102853. https://arxiv.org/abs/1909.12824.
2. A. H. Dooley and S. K. Gupta, *On norms of trigonometric polynomials on \(SU(2)\)*, *Pacific Journal of Mathematics* 175 (1996), 491–509. https://msp.org/pjm/1996/175-2/pjm-v175-n2-p09-s.pdf.
3. *High-weight parity localization of central fourth moments on \(SU(2)\)*, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-high-weight-parity-localization-of-central-fourth-moments-on-su--00a2a7bedf04. Comparison concerns the published theorem's leading asymptotic, not its review status.
