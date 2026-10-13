# Closed Bessel form and exact high-intensity limit for gain-one pair-coherent teleportation
## Finding
For the gain-one coherent-state teleportation fidelity of Gábris and Agarwal's pair-coherent resource, with \(\zeta\ge0\), the published double series sums exactly to \[\mathcal F_{\rm av}(\zeta,1)=\frac{e^{\zeta}I_0(\zeta)}{2I_0(2\zeta)}.\] Moreover, as \(\zeta\to\infty\), \[\mathcal F_{\rm av}(\zeta,1)=\frac1{\sqrt2}\left(1+\frac1{16\zeta}+\frac{25}{512\zeta^2}+O(\zeta^{-3})\right).\] Hence the large-intensity fidelity tends exactly to \(1/\sqrt2\) from above; in particular it eventually exceeds \(2/3\), sharpening the source's qualitative statement that the gain-one fidelity approaches a limit above \(1/2\).

The source gives, at gain \(g=1\),
\[
\mathcal F_{\rm av}(\zeta,1)=\frac{1}{2I_0(2\zeta)}\sum_{m,n\ge0}\frac{(\zeta/2)^{m+n}(m+n)!}{(m!n!)^2}.
\]
The exact reduction above turns that two-index sum into one standard modified-Bessel quotient and fixes the high-intensity plateau exactly.

## Assumptions and scope
The parameter is real with \(\zeta\ge0\). The statement concerns the source's coherent-state input and fixed gain \(g=1\); it does not optimize over gain, alter the Bell measurement, or assert anything about noisy preparation of the pair-coherent resource. \(I_0\) denotes the modified Bessel function of the first kind.

## Proof
Put \(k=m+n\). For each \(k\ge0\), Vandermonde's identity gives
\[
\sum_{m=0}^k\frac{k!}{(m!)^2((k-m)!)^2}
=\frac1{k!}\sum_{m=0}^k\binom{k}{m}^2
=\frac1{k!}\binom{2k}{k}.
\]
Therefore the published double sum is
\[
\sum_{k=0}^\infty \left(\frac\zeta2\right)^k\frac1{k!}\binom{2k}{k}
=\sum_{k=0}^\infty\frac{(1/2)_k}{(k!)^2}(2\zeta)^k
={}_1F_1\!\left(\frac12;1;2\zeta\right).
\]
Euler's integral for \({}_1F_1\) with \(a=1/2\), \(b=1\), followed by \(t=(1+\cos\theta)/2\), yields
\[
{}_1F_1\!\left(\frac12;1;2\zeta\right)
=\frac1\pi\int_0^1\frac{e^{2\zeta t}}{\sqrt{t(1-t)}}\,dt
=e^{\zeta}\frac1\pi\int_0^\pi e^{\zeta\cos\theta}\,d\theta
=e^{\zeta}I_0(\zeta).
\]
Substitution proves the closed form.

For positive real \(x\), the standard large-argument expansion is
\[
I_0(x)=\frac{e^x}{\sqrt{2\pi x}}\left(1+\frac1{8x}+\frac9{128x^2}+\frac{225}{3072x^3}+O(x^{-4})\right).
\]
Applying it at \(x=\zeta\) and \(x=2\zeta\), then dividing the two series, gives
\[
\frac{e^{\zeta}I_0(\zeta)}{2I_0(2\zeta)}
=\frac1{\sqrt2}\left(1+\frac1{16\zeta}+\frac{25}{512\zeta^2}+\frac{491}{8192\zeta^3}+O(\zeta^{-4})\right).
\]
The displayed finding follows, and the positive first correction implies approach from above for all sufficiently large \(\zeta\).

## Verification
`verify.py` independently evaluates the original double sum and the closed Bessel quotient using high-precision decimal series at several positive values of \(\zeta\). It also checks the displayed asymptotic approximation at increasing \(\zeta\), and reproduces the source's reported value near \(\zeta=1.2357\). The computation is a replay check, not a substitute for the analytic summation and asymptotic proof.

## Relationship to prior work
Gábris and Agarwal derive the double-series formula and report numerically that at unit gain the fidelity is input-amplitude independent, has a maximum about \(0.75884\), and appears to approach a limit above \(1/2\). Their displayed formula is the premise here; the exact Bessel quotient and exact limiting value \(1/\sqrt2\) are the added statement.

Earlier work of Wu, Li, Wang, and Xu studies teleportation with pair-coherent states under a different protocol and phase damping. Its accessible bibliographic and abstract material does not state this gain-one Gábris--Agarwal double series or its Bessel reduction. Generic modified-Bessel asymptotics are standard and are used here only after the exact source-specific summation.

## Limitations
The claim does not prove uniqueness of the finite-\(\zeta\) fidelity maximum and does not optimize the gain. It does not compare all possible pair-coherent teleportation protocols. A residual literature risk is that the same special-function reduction may occur in an unindexed calculation using different notation.

## References
1. A. Gábris and G. S. Agarwal, “Quantum teleportation with pair-coherent states,” arXiv:quant-ph/0607162, first public 2006-07-24; DOI 10.1142/S0219749907002475.
2. MaRDI item Q5292229 / zbMATH-linked metadata for the same work, listing MSC 81P68 and 81R30.
3. R.-K. Wu, S.-B. Li, Q.-M. Wang, and J. Xu, “Application of pair coherent states in quantum information processes,” DOI 10.1142/S0217984904007426.
4. NIST Digital Library of Mathematical Functions, §10.40, large-argument asymptotic expansions for modified Bessel functions.
