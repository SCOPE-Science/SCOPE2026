# The full filtration-entropy spectrum of the polynomial algebra

## Result

Let \(k\) be a field and let \(A=k[x]\). As \(\mathcal F\) ranges over all finite-dimensional exhaustive algebra filtrations in the sense used for filtered algebraic entropy,
\[
\boxed{\{h_{\rm alg}(k[x],\mathcal F)\}=[0,\infty].}
\]
Here the right-hand side is the extended nonnegative real interval, so it includes \(+\infty\).

For \(\lambda\in(0,\infty)\), put \(a=e^\lambda\) and
\[
f_\lambda(n)=n+\lfloor a^n-1\rfloor\qquad(n\ge1),
\]
then define
\[
V_0=0,\qquad V_n=\operatorname{span}_k\{1,x,\ldots,x^{f_\lambda(n)}\}.
\]
This filtration has entropy exactly \(\lambda\). The standard degree filtration has entropy \(0\). Replacing \(a^n\) by \(e^{n^2}\) gives entropy \(+\infty\).

## Proof

For \(m,n\ge1\),
\[
(a^n-1)+(a^m-1)\le a^{n+m}-1
\]
because the difference is \((a^n-1)(a^m-1)\). Together with
\(\lfloor u\rfloor+\lfloor v\rfloor\le\lfloor u+v\rfloor\), this gives
\[
f_\lambda(n)+f_\lambda(m)\le f_\lambda(n+m).
\]
Hence \(V_nV_m\subseteq V_{n+m}\). The spaces are finite dimensional, increasing and exhaustive.

For \(n\ge2\),
\[
\dim(V_n/V_{n-1})=f_\lambda(n)-f_\lambda(n-1).
\]
The floor error is bounded, so
\[
(a-1)a^{n-1}\le f_\lambda(n)-f_\lambda(n-1)
\le (a-1)a^{n-1}+2.
\]
Therefore
\[
\lim_{n\to\infty}\frac{\log\dim(V_n/V_{n-1})}{n}=\log a=\lambda.
\]
The standard degree filtration has one-dimensional successive quotients and therefore entropy zero.

For the infinite value, set
\[
f_\infty(n)=n+\lfloor e^{n^2}-1\rfloor.
\]
The same multiplicativity argument applies because
\[
(e^{n^2}-1)+(e^{m^2}-1)\le e^{(n+m)^2}-1.
\]
Its successive quotient dimensions grow on the order of \(e^{n^2}\), so the entropy is \(+\infty\). This proves the complete spectrum.

## Prior boundary

Filtration dependence itself is prior work. An earlier published record on 18 September 2026 already showed that every infinite-dimensional affine algebra admits accelerated positive-entropy filtrations, gave exact values \(\log b\) on \(k[x]\) for integer bases \(b\ge2\), and supplied the growth-detection and linear-control consequences. Those results are inputs and are not claimed here.

The contribution retained here is only the exact classification of all entropy values realized by finite-dimensional filtrations on the single algebra \(k[x]\).

## Limitations

This result concerns this filtration-based entropy, not unrelated notions with the same name. It does not assert that arbitrary filtrations are natural for intrinsic growth questions. The construction is elementary, so an equivalent prescribed-reindexing observation may exist under different terminology.

## References

1. W. Bock, C. Gil Canto, D. Martín Barquero, C. Martín González, I. Ruiz Campos and A. Sebandal, *Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs*, Results in Mathematics 79 (2024), Article 180, https://doi.org/10.1007/s00025-024-02198-0
2. J. Schwarz and A. Sebandal, *Growth functions of algebras and an application to Leavitt path algebras*, arXiv:2609.18144 (2026).
3. *Accelerated filtrations break arbitrary-filtration entropy-growth implications*, 18 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-accelerated-filtrations-break-growth-entropy-dichotomy--3c11c354c506
