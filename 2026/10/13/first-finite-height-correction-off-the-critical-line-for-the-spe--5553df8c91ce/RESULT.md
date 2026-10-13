# First finite-height correction off the critical line for the special-value weighted zeta density
## Finding
Fix \(\sigma\in(1/2,1)\) and put
\[
\alpha_\sigma=\frac{\sigma}{2\sigma+1}.
\]
Let \(\phi\) be a real even Schwartz function such that \(\operatorname{supp}\widehat\phi\subset(-\alpha,\alpha)\) for some \(0<\alpha<\alpha_\sigma\). Write
\[
I_\sigma(T)=\int_T^{2T}|\zeta(\sigma+it)|^2\,dt
\]
and
\[
\mathcal D_{\sigma,T}(\phi)=\frac{1}{I_\sigma(T)}\int_T^{2T}|\zeta(\sigma+it)|^2D_T(\zeta_t,\phi)\,dt,
\]
where \(D_T(\zeta_t,\phi)\) is the one-level density with ordinates scaled by \(\log T/(2\pi)\). Then
\[
\mathcal D_{\sigma,T}(\phi)
=\widehat\phi(0)+\frac{\widehat\phi(0)}{\log T}
\left(\log\frac{2}{\pi}-1+2\frac{\zeta'}{\zeta}\left(\sigma+\frac12\right)\right)
+o_\sigma\!\left(\frac1{\log T}\right).
\]
Consequently the coefficient of \(1/\log T\) is nonuniform at the critical transition:
\[
\log\frac{2}{\pi}-1+2\frac{\zeta'}{\zeta}\left(\sigma+\frac12\right)
=-\frac{2}{\sigma-1/2}+O(1)
\qquad(\sigma\downarrow1/2).
\]

## Assumptions and scope
The statement is for fixed \(\sigma\in(1/2,1)\), not for a \(\sigma\) that varies with \(T\). The Fourier support is strictly inside the source paper's unconditional range \((-\alpha_\sigma,\alpha_\sigma)\). Real even \(\phi\) is imposed only to keep the paired prime-power terms symmetric. No Riemann hypothesis is assumed.

The result refines the leading unitary law for this weighted continuous family; it does not enlarge the Fourier-support range and it does not claim a second correction term.

## Proof
Let \(L=\log T\). Start from the exact Weil explicit formula used by Sugiyama and Suriajaya, before the source absorbs the prime powers of exponent at least three and the constant archimedean terms into an \(O(1/L)\) remainder.

For the archimedean term, Stirling's formula gives, uniformly for \(t\in[T,2T]\),
\[
\frac{1}{2\pi}\int_{\mathbb R}\phi\!\left(\frac{L}{2\pi}(r-t)\right)\Omega(r)\,dr
=\frac{\widehat\phi(0)}{L}\left(\log t-\log(2\pi)\right)+o\!\left(\frac1L\right)
\]
after weighted averaging. The classical off-critical second moment, equivalently the \(m=1\) case of the Selberg estimate used in the source, yields
\[
\frac{1}{I_\sigma(T)}\int_T^{2T}|\zeta(\sigma+it)|^2\log t\,dt
=\log T+\int_1^2\log u\,du+o(1).
\]
Since \(\int_1^2\log u\,du=2\log2-1\), the archimedean contribution is
\[
\widehat\phi(0)+\frac{\widehat\phi(0)}{L}\left(\log\frac{2}{\pi}-1\right)+o\!\left(\frac1L\right).
\]
The two pole-evaluation terms in the exact explicit formula are \(o(1/L)\) for compactly supported \(\widehat\phi\), by the usual Paley--Wiener integration-by-parts bound in the real direction.

For every prime power \(q=p^k\le T^\alpha\), Theorem 2.4 of the source gives
\[
\frac{I_q(\sigma,T)}{I_\sigma(T)}
=q^{-\sigma}+O_\sigma\!\left(q^{\sigma-1}T^{1-2\sigma}\right)
+O_\sigma\!\left(qT^{-\sigma}L^2\right)
+O_\sigma\!\left(q^\sigma T^{-\sigma/2}L^2\right).
\]
Insert this into the full prime-power part of the explicit formula. Using \(\Lambda(p^k)=\log p\), the three summed errors, including the outer factor \(1/L\), are bounded respectively by
\[
O_\sigma\!\left(\frac{T^{1-2\sigma+\alpha(\sigma-1/2)}}{L}\right),\qquad
O_\sigma\!\left(T^{-\sigma+3\alpha/2}L\right),\qquad
O_\sigma\!\left(T^{-\sigma/2+\alpha(\sigma+1/2)}L\right).
\]
All are \(o(1/L)\) when \(\alpha<\alpha_\sigma\): the third inequality is exactly the restrictive one, while \(\alpha_\sigma<2\sigma/3\) controls the second and \(\alpha<2\) controls the first.

Thus the prime-power contribution equals
\[
-\frac{2}{L}\sum_{q=p^k}\frac{\Lambda(q)}{q^{\sigma+1/2}}
\widehat\phi\!\left(\frac{\log q}{L}\right)+o\!\left(\frac1L\right).
\]
Because \(\sigma+1/2>1\), the series \(\sum_q\Lambda(q)q^{-\sigma-1/2}\) converges absolutely. Dominated convergence therefore replaces the Fourier factor by \(\widehat\phi(0)\), and
\[
-\sum_{q=p^k}\frac{\Lambda(q)}{q^{\sigma+1/2}}
=\frac{\zeta'}{\zeta}\left(\sigma+\frac12\right).
\]
The prime-power correction is hence
\[
\frac{2\widehat\phi(0)}{L}\frac{\zeta'}{\zeta}\left(\sigma+\frac12\right)+o\!\left(\frac1L\right).
\]
Adding it to the archimedean term proves the formula. Finally, the Laurent expansion \(\zeta'/\zeta(1+\varepsilon)=-1/\varepsilon+O(1)\) gives the stated divergence as \(\sigma\downarrow1/2\).

## Verification
The proof is analytic and infinite; the accompanying program is not a proof of the asymptotic theorem. It checks the exact identity
\[
-\frac{\zeta'}{\zeta}(s)=\sum_p\frac{\log p}{p^s-1},\qquad s>1,
\]
against large finite prime cutoffs at several values of \(s=\sigma+1/2\), verifies \(\int_1^2\log u\,du=2\log2-1\), and evaluates the displayed coefficient numerically. The remaining finite-tail discrepancy decreases with the cutoff, as expected from absolute convergence.

## Relationship to prior work
Sugiyama and Suriajaya prove, for the same continuous family and the same support threshold, the leading off-critical formula
\[
\mathcal D_{\sigma,T}(\phi)=\widehat\phi(0)+O_\sigma\!\left(\frac1{\log T}\right).
\]
Their proof explicitly truncates the exact prime-power formula to the first two prime powers and absorbs the archimedean constant and higher prime powers into an \(O(1/\log T)\) term. The present statement instead retains all prime powers and the constant term from the gamma factor, identifying the complete first coefficient.

Bettin and Fazzari study the distinct critical-line weights \(|\zeta(1/2+it)|^{2k}\), with \(k=1,2\), and do not imply this fixed off-critical \(\sigma>1/2\) coefficient. The divergence of the coefficient as \(\sigma\downarrow1/2\) quantitatively exhibits why the fixed-\(\sigma\) expansion is not uniform at the phase transition identified by Sugiyama and Suriajaya.

## Limitations
The little-oh term is asserted only for each fixed \(\sigma>1/2\) and fixed strict support margin \(\alpha<\alpha_\sigma\). No uniform estimate as \(\sigma\downarrow1/2\) is proved. The result does not determine the next term, relax the support restriction, or address the critical-line expansion itself.

## References
1. Shingo Sugiyama and Ade Irma Suriajaya, *One-level density of zeros of the Riemann zeta function weighted by its special values*, arXiv:2610.05227v1, first public 2026-10-04.
2. Sandro Bettin and Alessandro Fazzari, *A weighted one-level density of the non-trivial zeros of the Riemann zeta-function*, arXiv:2208.08421v1; *Mathematische Zeitschrift* 307 (2024), article 32, DOI 10.1007/s00209-024-03496-7.
