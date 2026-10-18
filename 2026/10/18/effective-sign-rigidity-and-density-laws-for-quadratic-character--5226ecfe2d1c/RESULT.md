# Effective sign rigidity and density laws for quadratic-character binomial transforms

## Finding
Let \(p\) be any odd prime, and let \(\chi_p(k)=(\frac{k}{p})\) be the Legendre symbol, with value zero when \(p\mid k\). Define the ordinary binomial transform
\[
T_p(n)=\sum_{k=0}^{n}\chi_p(k)\binom{n}{k},\qquad n\in\mathbb Z_{\ge0}.
\]
For \(p\ge5\), define the explicit cutoff
\[
N_p=1+\left\lfloor\frac{p^2}{6}\log\left(\frac{p(p-3)}{2}\right)\right\rfloor.
\]
For every \(n\ge N_p\), the signs follow exactly a trigonometric residue-class law:
\[
\operatorname{sgn}T_p(n)=
\begin{cases}
\operatorname{sgn}\cos(n\pi/p),&p\equiv1\pmod4,\\
\operatorname{sgn}\sin(n\pi/p),&p\equiv3\pmod4.
\end{cases}
\]
When \(p=3\), the sine formula holds for *every* \(n\ge0\). Consequently the sets of nonnegative indices with positive, negative and zero transform values have natural densities respectively
\[
\begin{cases}
(\tfrac12,\tfrac12,0),&p\equiv1\pmod4,\\
(\tfrac{p-1}{2p},\tfrac{p-1}{2p},\tfrac1p),&p\equiv3\pmod4.
\end{cases}
\]
If \(p\equiv3\pmod4\), then \(T_p(n)=0\) holds exactly, without a cutoff, whenever \(p\mid n\). For all \(n\ge N_p\), these are the only zeros. For \(p\equiv1\pmod4\), no zeros occur beyond the cutoff.

## Assumptions and scope
The prime \(p\) is odd and fixed, while the index \(n\) ranges over all nonnegative integers. The Legendre symbol is extended periodically to all integers and is zero at multiples of \(p\). The sign of zero is zero. The formula concerns the *ordinary* transform using \(\binom nk\), not a centered transform using \(\binom{2n}{n+k}\), nor a Legendre symbol applied to the binomial coefficient itself. Statements for small indices not covered by \(N_p\) are not asserted except the exact divisibility zeros. Logarithms are natural logarithms.

## Proof
**Fourier decomposition.** Put \(\zeta=e^{2\pi i/p}\), \(u=\pi/p\), and \(\tau_p=\sum_{j=1}^{p-1}\chi_p(j)\zeta^j\). The classical evaluation of the quadratic Gauss sum, with this choice of the positive exponential, is
\[
\tau_p=\begin{cases}\sqrt p,&p\equiv1\pmod4,\\i\sqrt p,&p\equiv3\pmod4.\end{cases}
\]
For every integer \(k\), the change of variable in the complete character sum gives
\(\sum_{j=1}^{p-1}\chi_p(j)\zeta^{jk}=\chi_p(k)\tau_p\); this remains true when \(p\mid k\) because both sides vanish. Hence by the binomial theorem,
\[
T_p(n)=\tau_p^{-1}\sum_{j=1}^{p-1}\chi_p(j)(1+\zeta^j)^n.
\]
For \(1\le j\le(p-1)/2\) put \(a_j=2\cos(ju)\), which is positive. Pair \(j\) with \(p-j\); note \(1+\zeta^j=a_j e^{iju}\), its partner is \(a_j e^{-iju}\), and \(\chi_p(p-j)=(-1)^{(p-1)/2}\chi_p(j)\). The precise real identities become
\[
T_p(n)=\frac2{\sqrt p}\sum_{j=1}^{(p-1)/2}\chi_p(j)a_j^n
\begin{cases}\cos(nju),&p\equiv1\pmod4,\\\sin(nju),&p\equiv3\pmod4.
\end{cases}
\tag{1}
\]
In particular the first term in this expansion has positive coefficient \(\chi_p(1)=1\).

**Quantitative leading-frequency domination.** Assume \(p\ge5\) and write \(a=\cos u\), \(b=\cos(2u)\), so \(0<b<a<1\). For \(j\ge2\), \(a_j\le2b\). Since \(\sin t\ge2t/\pi\) for \(0\le t\le\pi/2\),
\[
a-b=2\sin(3u/2)\sin(u/2)\ge\frac6{p^2}.
\]
As \(a\le1\), we have \((a-b)/a\ge6/p^2\), and therefore
\[
\frac ba=1-\frac{a-b}{a}\le\exp(-6/p^2).
\tag{2}
\]
For integer \(n\), the cosine \(\cos(nu)\) is never zero because \(p\) is odd. Its magnitude is at least \(\sin(\pi/(2p))\ge1/p\). If \(\sin(nu)\ne0\), its magnitude is at least \(\sin(\pi/p)\ge2/p\), hence also at least \(1/p\). These inequalities follow by reducing \(n\) modulo \(2p\) and applying the same sine bound.

The sum of all terms other than \(j=1\) in (1), before its common positive factor \(2/\sqrt p\), has magnitude at most \(\frac{p-3}{2}(2b)^n\). If the leading trigonometric factor is nonzero, the leading term has magnitude at least \((2a)^n/p\). Their ratio is therefore bounded by
\[
\frac{p(p-3)}2\left(\frac ba\right)^n
\le\frac{p(p-3)}2\exp(-6n/p^2)<1
\qquad(n\ge N_p).
\]
The last inequality is strict by the definition of \(N_p\). The remainder cannot reverse or cancel the sign of the first term. This proves both asserted eventual sign formulas at indices where the trigonometric factor is nonzero.

**Forced zeros and the small prime.** Suppose \(p\equiv3\pmod4\) and \(p\mid n\). Pair summands at indices \(k\) and \(n-k\): the binomial coefficients agree, but \(\chi_p(n-k)=\chi_p(-k)=-\chi_p(k)\). Thus \(T_p(n)=0\), including \(n=0\). Conversely the sine term in (1) is nonzero at every integer \(n\) not divisible by \(p\), so the domination bound establishes that no other zeros persist past \(N_p\). When \(p=3\), the expansion (1) consists only of \(j=1\); because \(2\cos(\pi/3)=1\), it reads exactly \(T_3(n)=\frac2{\sqrt3}\sin(n\pi/3)\), giving the claimed sine sign law for every \(n\ge0\).

**Density.** The eventual signs depend only on \(n\bmod2p\). For \(p\equiv1\pmod4\), among these \(2p\) residues cosine is positive for precisely \(p\) and negative for precisely \(p\), never zero. For \(p\equiv3\pmod4\), sine is positive at \(p-1\) residues, negative at \(p-1\) residues, and zero at the two residues \(0,p\). A finite exceptional prefix does not affect natural densities, proving the two triples.

## Verification
The standalone script `verify_signs.py` recomputes Legendre symbols and binomial sums exactly by integer Pascal rows for each odd prime through \(37\), through each prime's cutoff plus three full prime lengths. It checks every sign prediction in the proved range, every forced zero below that range, the exact \(p=3\) formula, and the predicted counts in a full period. The verifier is confirmatory; the proof is uniform and does not rely on finite sampling.

## Relationship to prior work
Dresden and Li's preprint, publicly posted October 9, 2022 (arXiv:2210.04322), develops periodic weights for centered binomial sums and includes a Legendre-weighted identity for even-index Fibonacci numbers. The later full published article, *Journal of Integer Sequences* 26 (2023), article 23.8.7, gives primary MSC 11B39 and Theorems 1 and 2 on centered sums; the original version also gives examples for Kronecker weights. Those centered \(\binom{2n}{n+k}\) identities are not the ordinary \(\binom nk\) transform studied here and do not state its eventual signs or the exact densities for arbitrary odd primes. The Fourier step uses the standard quadratic Gauss evaluation; the quantitative sign bound and residue-class frequency conclusions are additional arguments. General root-of-unity filters for periodic sequences may yield the spectral expression, but not, without further analysis, this explicit stabilization threshold and complete sign-density law.

## Limitations
The cutoff is explicit but not proved optimal. Zeros at smaller indices for primes congruent to one modulo four, or at nonmultiples of the prime for primes congruent to three modulo four, are not classified. The result does not claim a new quadratic Gauss-sum evaluation. Novelty is assessed against the inspected primary literature, mathematical database searches and accessible related records; equivalent work outside those sources may exist. No independent mathematical audit has been performed.

## References
1. G. Dresden and Y. Li, *Periodic Weighted Sums of Binomial Coefficients*, arXiv:2210.04322, first posted 2022-10-09. https://arxiv.org/abs/2210.04322
2. G. Dresden and Y. Li, *Periodic Weighted Sums of Binomial Coefficients*, Journal of Integer Sequences 26 (2023), Article 23.8.7. https://cs.uwaterloo.ca/journals/JIS/VOL26/Dresden/dresden26.pdf
3. B. C. Berndt, R. J. Evans and K. S. Williams, *Gauss and Jacobi Sums*, 1998, quadratic Gauss-sum evaluation (also cited by Dresden and Li).
4. The On-Line Encyclopedia of Integer Sequences, A117611 and A117980, for comparison with the distinct transform applying a Legendre symbol to binomial coefficients. https://oeis.org/A117611 ; https://oeis.org/A117980
