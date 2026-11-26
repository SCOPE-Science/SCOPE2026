# Exact eventual maximizing layer of the affine Johnson-slice projection

## Finding

For the uniform measure on the slice of all \(k\)-subsets of \([n]\), let \(P_{n,k}\) be the \(L^2\)-orthogonal projector onto the restrictions of affine coordinate functions. Put \(\Lambda_{n,k}=\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}=\|P_{n,k}\|_{\ell^1\to\ell^1}\). **For all sufficiently large integers \(n\), the only layers maximizing \(\Lambda_{n,k}\) over \(1\le k<n\) are \(k_*(n)\) and \(n-k_*(n)\), where**
\[
k_*(n)=\left\lceil\frac{\sqrt{32n+1}-1}{8}\right\rceil.
\]
Equivalently, \(k_*(n)\) is the least integer \(k\ge1\) with \(n\le 2k^2+\lfloor k/2\rfloor\). The maximal norm is
\[
1+\frac{2n(k_*-1)}{n-k_*}\,\frac{\binom{n-k_*}{k_*}}{\binom n{k_*}}.
\]
In particular there are eventually no ties between two different smaller widths. The cutoff describes the discrete optimizer, not just its known leading scale \(\sqrt{n/2}\).

## Assumptions and scope

Use the full finite slices, unweighted counting coordinates for the endpoint norms, and uniform probability measure for the orthogonal projectors. The range is the space of functions \(S\mapsto a+\sum_{i\in S}b_i\). The theorem does not specify the first value of \(n\) for which the formula always holds and does not treat other Johnson projectors or nonuniform measures.

## Proof

**Exact kernel.** Center the coordinate indicators by \(k/n\). Their covariance on the sum-zero subspace is scalar \(k(n-k)/[n(n-1)]\): the diagonal entries are \((k/n)(1-k/n)\), all off-diagonal entries are equal, and the matrix kills the all-ones vector. Adding the constant component gives the probability-normalized kernel
\[
K(S,U)=1+\frac{n(n-1)}{k(n-k)}\left(|S\cap U|-\frac{k^2}{n}\right).
\]
For uniform \(U\) and fixed \(S\), \(J=|S\cap U|\) has masses \(\binom{k}{j}\binom{n-k}{k-j}/\binom nk\). Transitivity makes all absolute row sums equal to \(\mathbb E|K(S,U)|\), and symmetry gives the same absolute column sums. Complementation identifies widths \(k\) and \(n-k\), so it suffices to optimize \(1\le k\le n/2\).

**Localization used below.** The degree-one-only projector has all-width asymptotics with the same three regimes and the same unique sparse peak [1, Proof, “All scaling regimes” and “Unique maximum of the crossover”]. Its norm and the affine projector norm differ by at most one, uniformly in \(n,k\), because the constant projector has norm one. Here is the localization argument directly. Put \(\mu=k^2/n\) and \(\sigma^2=k^2(n-k)^2/[n^2(n-1)]\). Then \(K=1+\sqrt{n-1}(J-\mu)/\sigma\), with \(\mathbb E K^2=n\), giving uniform integrability for the normalized absolute kernels. If \(k/\sqrt n\to0\), use \(\mathbb E|J-\mu|\le 2\mu\) to get a zero limit. If \(k/\sqrt n\to c>0\) finite, the factorial moments \((k)_r^2/(n)_r\) yield the Poisson law of mean \(t=c^2\). The normalized norm tends to \(F(t)=2e^{-t}t^{m+1/2}/m!\), \(m=\lfloor t\rfloor\), by the Poisson mass recursion for the mean absolute deviation. If \(k/\sqrt n\to\infty\), the standardized overlap has the standard normal limit, hence the normalized norm tends to \(\sqrt{2/\pi}\). For the central limit theorem here, all four expected cell counts in the hypergeometric cross table tend to infinity: for \(k\le n/2\) the minimum is \(k^2/n\), and the standard deviation is comparable to \(\sqrt{k^2/n}\). Equivalently, expanding the logarithm of the adjacent mass ratio \((k-j)^2/[(j+1)(n-2k+j+1)]\) on bounded standardized windows gives the Gaussian density ratio; normalization and variance tightness give the limit.

On \(m<t<m+1\) the function \(F\) peaks at \(a=m+1/2\). Consecutive peak heights satisfy
\[
\log\frac{F(a+1)}{F(a)}=(a+1)\log(a+1)-a\log a-1-\log(a+1/2).
\]
The right-hand side increases strictly to zero, since its derivative is \(\int_0^1(a+x)^{-1}dx-(a+1/2)^{-1}>0\). Thus the unique global peak is \(F(1/2)=\sqrt{2/e}>\sqrt{2/\pi}\). Taking integer widths nearest \(\sqrt{n/2}\) gives that lower limit for the normalized maximum. The three regime limits on subsequences of \(k/\sqrt n\) then force every sequence of smaller maximizing widths to satisfy \(k/\sqrt{n/2}\to1\).

**Exact comparison within the sparse window.** Write \(s_n=\sqrt{n/2}\) and restrict to the integer interval \(I_n=[s_n/2,5s_n/4]\cap\mathbb Z\); every smaller maximizing width is in \(I_n\) for all sufficiently large \(n\). For all such \(n\) and all \(k\in I_n\), \(k\ge2\) and the zero of the affine kernel, as a function of overlap, is \(k(k-1)/(n-1)\in(0,1)\). Only the overlap \(J=0\) contributes to the negative part of the kernel. Since \(\mathbb E K=1\),
\[
\Lambda_{n,k}=1+2n A_{n,k},\qquad
A_{n,k}=\frac{k-1}{n-k}\frac{(n-k)!^2}{n!\,(n-2k)!}.
\]
For adjacent \(k,k+1\in I_n\), the sign of \(A_{n,k+1}-A_{n,k}\) is the sign of
\[
k(n-2k)(n-2k-1)-(k-1)(n-k)(n-k-1)
=n^2-(2k^2+2k+1)n+3k^3+2k^2+k.
\]
As a polynomial in \(n\) the discriminant is \(\Delta=4k^4-4k^3+1\). For \(k\ge2\),
\[
(2k^2-k-1)^2<\Delta<(2k^2-k)^2.
\]
The smaller root is less than \((3k+2)/2<n\) throughout this window for all sufficiently large \(n\). The larger root lies strictly between \(2k^2+k/2\) and \(2k^2+(k+1)/2\), so it is not integral and its floor is \(2k^2+\lfloor k/2\rfloor\). Thus the norm strictly increases across this adjacent step if \(n>2k^2+\lfloor k/2\rfloor\), and strictly decreases otherwise. The thresholds increase strictly with \(k\), and their crossing width \(k_*\) lies in the interior of \(I_n\) for large \(n\) because \(k_*\sim s_n\). There is one maximizer in that interval and none outside it by localization. For integral \(n\), the threshold condition is equivalent to \(n\le 2k^2+k/2\). Solving the quadratic gives the ceiling formula. The norm follows by substitution into the sparse formula, and complementation gives the second maximizing layer.

## Verification and prior coverage

The finite exact-rational checker `check_eventual_width.py` compares the threshold prediction with the full cross-slice norm computation on a bounded range and checks both sides of exact threshold transitions. It does not prove eventual localization or certify the first valid \(n\).

[1] *The sharp worst-slice endpoint norm of the first Johnson spectral projection*, https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-the-sharp-worst-slice-endpoint-norm-of-the-first-johnson-spectra--2367a878c8dc/RESULT.md. This treats the nonconstant degree-one projector and gives the leading optimizer scale, explicitly not a finite optimizer or finite uniqueness. The norm-one comparison transfers the three asymptotic regimes, not the adjacent finite-width comparisons; the constant shift inside the absolute value matters for the latter.

[2] Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (2014), Johnson harmonic decomposition.

[3] N. Elezović, *The mean absolute deviation of the classical discrete distributions: collapse identities, complete asymptotic expansions, and enveloping series*, arXiv:2608.06232, §3 Theorem 3.1 (centered hypergeometric mean absolute deviation).
