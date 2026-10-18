# Sharp covariance tails and geometric reconstruction for positive-volume Cantor expanding maps

## Finding
For a natural polynomial-gap family of positive-volume, invariant Cantor sets in \(C^1\) expanding circle maps, the signed position observable has an exact positive correlation sequence, a sharp two-term polynomial correction to its exponential decay, and a uniquely recoverable underlying Cantor geometry from its complete correlation spectrum.

Take parameters \(0<b<1\), \(p>1\), and
\[
0<c<\min\{2b,\,2(1-b)/\zeta(p)\}.
\]
Put \(L=2-2b-c\zeta(p)>0\), \(Q=2b+c\operatorname{Li}_{p}(1/4)\), and \(R=c\operatorname{Li}_{p-1}(1/4)\). Define
\[
A=\frac{L(4+Q)}{24},\qquad J=\frac{4-2Q+3R}{3(4+Q)}.
\]
If \(C_n\) is the lag-\(n\) covariance of the signed position under the Cantor-supported physical probability, then for all integers \(n\ge0\)
\[
C_n=\sum_{j\ge0}d_jd_{j+n}>0,
\quad d_j=2^{-j-2}\left(L+\sum_{k\ge j}\beta_k+\beta_j\right),
\quad\beta_0=2b,\quad \beta_j=cj^{-p}\ (j\ge1).
\]
As \(n\to\infty\),
\[
\boxed{\quad 2^nC_n=A\left[1+\frac{c}{L(p-1)}n^{1-p}+\frac{c}{L}\left(\frac32-J\right)n^{-p}+O(n^{-p-1})\right].\quad}
\]
In particular \(2^nC_n\to A>0\) from above at the sharp relative rate \(n^{1-p}\), with a strictly positive coefficient.

Furthermore, the *entire* sequence \((C_n)_{n\ge0}\) uniquely determines every removed gap length and location of the centered Cantor set in \([-1,1]\), hence the induced shift-conjugate dynamics on that set. This inverse claim does not determine the map on its complementary gaps.

## Assumptions and scope
Begin with \([-1,1]\); remove the central open interval \((-b,b)\). At each level \(j\ge1\), remove a centered open gap of length \(c/(j^p2^j)\) from every surviving level-\(j\) interval. All binary-cylinder intervals of the same level have equal lengths. The hypotheses are exactly a specialization of the summability, decreasing-gap, and adjacent-level ratio assumptions in Catsigeras and Valenzuela Gómez, Sections 5.2–5.3. Their associated degree-three \(C^1\) expanding circle map \(f\) preserves the residual fat Cantor set \(K\) and its normalized Lebesgue restriction \(\mu=m|_K/L\), which is a fair Bernoulli physical probability under its binary itinerary. We use those established dynamical properties as premises, not as new results.

Use the measurable signed-position chart \(X(x)=x\) on \([-1,1]\), identifying the two endpoints as one circle point. This chart has a jump across its chosen cut, but belongs to \(L^2(\mu)\); its value at the glued endpoint has no effect on integrals. Let \(C_n=\int_K X(x)X(f^nx)\,d\mu(x)-(\int_K X\,d\mu)^2\). All assertions concern this particular bounded measurable observable and this measure, not all continuous circle observables or arbitrary expanding maps.

## Proof
**Cylinder displacement.** Write \(\beta_0=2b\), \(\beta_j=cj^{-p}\) for \(j\ge1\), and \(S_j=\sum_{k\ge j}\beta_k\). The length of each level-\(j\) retained interval is
\[
I_j=2^{-j}(L+S_j).
\]
Indeed the union of its descendants has Lebesgue mass \(L/2^j\), while its future gaps have total length \(2^{-j}S_j\). The middle gap of this interval has length \(g_j=2^{-j}\beta_j\); the centers of the two children differ from the parent center by
\[
d_j=(I_j+g_j)/4=2^{-j-2}(L+S_j+\beta_j).
\]
As \(I_j\to0\), a point determined by itinerary signs \(\varepsilon_j\in\{-1,1\}\) has the uniformly convergent expansion \(X=\sum_{j\ge0}d_j\varepsilon_j\). The signs are independent, symmetric Rademacher variables by the established fair Bernoulli conjugacy. Thus \(\int X\,d\mu=0\) and independence gives exactly \(C_n=\sum_{j\ge0}d_jd_{j+n}\), including \(n=0\).

**Sharp tail.** Set \(B_j=L+S_j+\beta_j\), so \(d_j=2^{-j-2}B_j\). Then
\[
2^nC_n=\frac1{16}\sum_{j\ge0}4^{-j}B_j B_{n+j}.
\]
Using absolutely convergent geometric series and interchanging the positive sums yields
\[
W_0=\sum_{j\ge0}4^{-j}B_j=\frac{8+2Q}{3},\qquad
W_1=\sum_{j\ge0}j4^{-j}B_j=\frac{8-4Q+6R}{9}.
\]
For fixed \(j\), the Hurwitz-zeta/Euler–Maclaurin tail of \(c\sum_{k\ge n+j}k^{-p}\), together with the one extra \(\beta_{n+j}\), gives
\[
B_{n+j}=L+\frac{c}{p-1}n^{1-p}+c(3/2-j)n^{-p}+O_p(c(1+j)^2n^{-p-1}).
\]
For a uniform summed error, apply this bound first to \(0\le j\le n/2\); the remaining terms are exponentially small since \(B_j\) is bounded and \(\sum_{j>n/2}4^{-j}\) decays exponentially. Consequently the error after summation is \(O(n^{-p-1})\). Inserting \(W_0,W_1\) and \(A=LW_0/16\), \(J=W_1/W_0\) gives exactly the displayed expansion. Since \(c,L,p-1,A\) are positive, its first correction is nonzero and therefore sharp.

**Spectral recovery and rigidity.** Let \(D(z)=\sum_{j\ge0}d_jz^j\). By construction \(\sum_{j\ge0}d_j=1\), \(d_0=(1+b)/2\), and \(\sum_{j\ge1}d_j=(1-b)/2\). Hence for every \(|z|\le1\),
\[
|D(z)|\ge d_0-\sum_{j\ge1}d_j=b>0.
\]
Define \(F(t)=C_0+2\sum_{n\ge1}C_n\cos(nt)=|D(e^{it})|^2\). Since \(D\) has no zeros in the closed unit disk and \(D(0)>0\), its normalized logarithm is analytic there. With
\[
\ell_k=\frac1{2\pi}\int_0^{2\pi}\log F(t)e^{-ikt}\,dt\quad(k\ge0),
\]
uniqueness of analytic Fourier coefficients gives the constructive inverse
\[
D(z)=\exp\left(\ell_0/2+\sum_{k\ge1}\ell_kz^k\right),\qquad |z|<1.
\]
Thus the correlations determine each coefficient \(d_j\). Reconstruct recursively
\[
I_0=2,\qquad I_j=2-2\sum_{k<j}d_k,\qquad g_j=4d_j-I_j.
\]
The \(2^j\) level-\(j\) gaps each have length \(g_j\), and centered splitting fixes their positions uniquely. Their residual Cantor set and binary itinerary shift are therefore recovered. Standard minimum-phase spectral factorization underlies the inversion step; the crucial family-specific fact is the strict quantitative gap \(b\) enforcing its applicability and the explicit centered-gap reconstruction.

## Verification
An accompanying standard-library Python program checks \(\sum d_j=1\), the two closed weighted-sum identities, the sharp-tail approximation on parameter examples, Rademacher-word covariance by direct exhaustive enumeration, and truncated discrete Fourier logarithm inversion. It prints `VERIFY_OK 88 diagnostics (finite cases only)`. Exact results are established in the proof, not inferred from these finite computations.

## Relationship to prior work
Catsigeras and Valenzuela Gómez (arXiv:2604.04959, Sections 5.2–5.3, Propositions 5.6–5.8) establish the Cantor construction, invariant physical measure, and fair Bernoulli coding, but not the position-covariance series, its explicit polynomial corrections, or the full inverse reconstruction from correlations. Araujo and Santos (arXiv:1707.04311, Section 2.1) discuss predecessor expanding examples and entropy, not this two-point statistic. The Wiener–Khinchin and minimum-phase spectral-factorization principles are older general tools and are *not* claimed to be newly proved; the special geometric and quantified dynamical consequences above are the proposed addition. Prior work on Fourier transforms and pair correlations of Bernoulli convolutions concerns a different observable/problem, rather than the time-lagged signed position in this fat Cantor expanding map. An equivalent historical specialization has not been ruled out by a comprehensive expert bibliography.

## Limitations
The signed coordinate is measurable and discontinuous at the circle chart cut, not globally continuous. The output concerns normalized Lebesgue on the specific centered Cantor support; it is not a claim about correlations for arbitrary observables or the dynamics outside the support. Finite diagnostics are not a proof for all parameters or all times. The original constructions, fair Bernoulli property, Wiener–Khinchin identity and spectral-factorization method remain established prior knowledge. The exact proposed specialization has not been independently audited, and bibliographic priority remains uncertain.

## References
1. E. Catsigeras and F. Valenzuela Gómez, *Entropy formula for \(C^1\) expanding maps*, arXiv:2604.04959, first posted 2026-04-03, Sections 5.2–5.3. https://arxiv.org/abs/2604.04959
2. V. Araujo and F. Santos, *Pesin's Entropy Formula for \(C^1\) non-uniformly expanding maps*, arXiv:1707.04311, Section 2.1. https://arxiv.org/html/1707.04311v4
3. K. Takaya, *Recovery of Phase Using Power Spectrum and Bispectrum*, J. Circuits, Systems and Computers (1997), DOI 10.1142/S021812669700019X, for the classical minimum-phase caveat. https://doi.org/10.1142/S021812669700019X
