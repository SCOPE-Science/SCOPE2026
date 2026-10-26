# No real sampling sequences in supercritical fractional Paley–Wiener spaces

## Finding

For every bandwidth \(a>0\) and exponent \(s>\frac12\) outside the critical values \(\frac32,\frac52,\frac72,\ldots\), set \(m=\lfloor s-\frac12\rfloor\). In the fractional Paley–Wiener reproducing-kernel Hilbert space \(PW_a^s\) defined in [1], there is no countable real sequence \(\Lambda\subset\mathbb R\) and no constants \(0<A\le B<\infty\) for which

\[
 A\|f\|_{PW_a^s}^{2}\le \sum_{\lambda\in\Lambda}|f(\lambda)|^{2}\le B\|f\|_{PW_a^s}^{2}
\]

holds for every \(f\in PW_a^s\). Thus real point evaluations do not form a stable sampling system in any of these supercritical noncritical spaces.

## Assumptions and scope

The parameter satisfies \(s>\frac12\) and \(s-\frac12\notin\mathbb N\). With \(m=\lfloor s-\frac12\rfloor\), this is equivalent to

\[
 m+\frac12<s<m+\frac32.
\]

The space is the one in [1, Sections 3 and 5], whose Fourier representation subtracts the Taylor polynomial \(P_m(iz\xi)=\sum_{k=0}^{m}(iz\xi)^k/k!\). Sampling means the two-sided frame inequality above, with the sum over the proposed real sampling sequence. The theorem concerns real point samples of \(f\) itself; it does not rule out samples of the fractional Laplacian, complex sampling points, or other measurement functionals.

## Proof

Write

\[
 R_m(t)=e^{-it}-\sum_{k=0}^{m}\frac{(-it)^k}{k!},\qquad
 u_\lambda(\xi)=R_m(\lambda\xi)|\xi|^{-s},\quad -a\le\xi\le a.
\]

By the reproducing-kernel formula for \(PW_a^s\) in [1, Corollary 3.6], applying the isometry from the weighted Fourier model to \(L^2([-a,a])\) sends the sampling kernels, up to a fixed nonzero scalar, to \(u_\lambda\). Hence a real sampling sequence would make \(\{u_\lambda:\lambda\in\Lambda\}\) a frame for the infinite-dimensional Hilbert space \(H=L^2([-a,a])\), and in particular a Bessel sequence.

First, Taylor's theorem gives

\[
 R_m(t)=\frac{(-it)^{m+1}}{(m+1)!}+O(|t|^{m+2})\quad(t\to0).
\]

At infinity, \(R_m(t)=O(|t|^m)\) (and is bounded when \(m=0\)). Since \(m+\frac12<s<m+\frac32\), the constant

\[
 C_{s,m}=\int_{\mathbb R}|R_m(t)|^2|t|^{-2s}\,dt
\]

is finite and strictly positive: near zero the integrand is of order \(|t|^{2m+2-2s}\), whose exponent is greater than \(-1\); at infinity it is bounded by a constant times \(|t|^{2m-2s}\), whose exponent is less than \(-1\). The change of variables \(t=\lambda\xi\) therefore yields

\[
 \|u_\lambda\|_2^2
 =|\lambda|^{2s-1}\int_{-a|\lambda|}^{a|\lambda|}|R_m(t)|^2|t|^{-2s}\,dt
 \sim C_{s,m}|\lambda|^{2s-1}\quad(|\lambda|\to\infty).
\]

Because \(s>\frac12\), these norms diverge as \(|\lambda|\to\infty\). Every vector in a Bessel sequence has norm bounded by the square root of the Bessel bound, so all sampling locations in a putative frame must be bounded.

On bounded sets of parameters, \(\lambda\mapsto u_\lambda\) is continuous in \(H\): the Taylor remainder near \(\xi=0\) is bounded by a constant times \(|\xi|^{m+1-s}\), which is square-integrable because \(s<m+\frac32\). If a bounded sequence of sampling locations had a nonzero accumulation point \(\lambda_*\), a subsequence of its frame vectors would converge in \(H\) to \(u_{\lambda_*}\ne0\). A Bessel sequence cannot have a subsequence converging to a nonzero vector, since its inner products with that limit vector would fail to be square-summable. Thus, if the set is infinite, its only possible accumulation point is zero, so for each \(\varepsilon>0\) only finitely many locations satisfy \( |\lambda|\ge\varepsilon\). If the set is finite, its frame operator is already finite-rank and cannot be a frame operator on \(H\).

For the remaining infinite case, set

\[
 v(\xi)=\frac{(-i)^{m+1}}{(m+1)!}\,\xi^{m+1}|\xi|^{-s}.
\]

This is a nonzero vector in \(H\), and the Taylor expansion gives

\[
 u_\lambda=\lambda^{m+1}v+O_H(|\lambda|^{m+2})\quad(\lambda\to0).
\]

Consequently, for all sufficiently small nonzero \(\lambda\), \(|\langle u_\lambda,v\rangle|\ge c|\lambda|^{m+1}\) for some \(c>0\). The Bessel inequality applied to \(v\) implies \(\sum_{\lambda\in\Lambda}|\lambda|^{2m+2}<\infty\) on the tail. The same Taylor expansion gives \(\|u_\lambda\|_2^2\asymp |\lambda|^{2m+2}\) near zero, so \(\sum_{\lambda\in\Lambda}\|u_\lambda\|_2^2<\infty\). The associated frame operator is therefore trace-class, hence compact. But a frame operator on an infinite-dimensional Hilbert space is bounded below by \(A I\) for some \(A>0\), and no compact operator can have that property. This contradiction proves the claim.

## Verification

The proof uses the exact kernel representation in [1, Corollary 3.6], Taylor expansion with an explicit first nonzero term, and the change of variables \(t=\lambda\xi\). The two integrability checks are exactly \(2m+2-2s>-1\) at zero and \(2m-2s<-1\) at infinity. The compactness contradiction is an infinite-dimensional argument, not a finite enumeration or numerical extrapolation. No external computational certificate is required.

## Relationship to prior work

Monguzzi, Peloso, and Salvatori [1, Section 5] explicitly investigate real sampling in \(PW_a^s\) and prove nonexistence for \(0<s<\frac12\), using a fixed-window exponential-frame criterion. Their reproducing kernels for \(s>\frac12\) instead contain the parameter-dependent Taylor subtraction \(P_m(-i\lambda\xi)\). The fixed-window criterion does not directly cover that family. The argument here treats the supercritical range by proving that Bessel boundedness forces the sampling locations to remain bounded, that any accumulation can occur only at zero, and that the resulting frame operator would be compact. The primary paper's Section 5 does not state this supercritical conclusion.

## Limitations

The critical exponents \(s=\frac32,\frac52,\ldots\) are excluded from the space setup used in [1] and are not treated here. The result is only about real point evaluations of \(f\); it does not classify complex sampling sets or alternative measurements. It also does not contradict the orthogonal reconstruction formula using samples of \(\Delta^{s/2}f\), which is a different measurement system.

## References

[1] A. Monguzzi, M. M. Peloso, and M. Salvatori, “Fractional Paley–Wiener and Bernstein spaces,” arXiv:2002.12015v1, first public version 27 February 2020; *Collectanea Mathematica* 72 (2021), 615–643. DOI: 10.1007/s13348-020-00303-4. Open text: https://arxiv.org/abs/2002.12015 and https://doi.org/10.1007/s13348-020-00303-4.
