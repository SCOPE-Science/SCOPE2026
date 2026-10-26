# A sharp phase-deficit bound for Paley–Wiener symmetrization

## Finding

Let \(W\subset\mathbb R\) be a bounded interval of length \(B>0\), let \(T>0\) satisfy \(0<BT<1\), and define the Paley–Wiener space
\[
PW(W)=\{f\in L^2(\mathbb R):\operatorname{supp}\widehat f\subseteq W\},
\qquad \widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt.
\]
For \(f\in PW(W)\), let \(g\in PW(W)\) be specified by \(\widehat g=|\widehat f|\), and put \(I_T=[-T/2,T/2]\). Then
\[
\boxed{\int_{I_T}(|g(t)|^2-|f(t)|^2)\,dt\ge T\frac{\sin(\pi BT)}{\pi BT}\left(\|\widehat f\|_{L^1(W)}^2-|f(0)|^2\right).}
\]
The coefficient is optimal for every fixed pair \((B,T)\) with \(0<BT<1\). Since \(g(0)=\|\widehat f\|_{L^1(W)}\) and Fourier inversion gives \(f(0)=\int_W\widehat f(\xi)\,d\xi\), the right-hand side measures the exact loss of central peak caused by spectral phase cancellation, multiplied by an explicit time–bandwidth factor.

In particular, if \(A=\|\widehat f\|_{L^1(W)}>0\) and \(u(\xi)=\widehat f(\xi)/|\widehat f(\xi)|\) where \(\widehat f(\xi)\ne0\), then
\[
\inf_{|\zeta|=1}\int_W|\widehat f(\xi)|\,|u(\xi)-\zeta|^2\,d\xi\le \frac{2\pi BT}{T\sin(\pi BT)}\frac{\int_{I_T}(|g|^2-|f|^2)\,dt}{A}.
\]
Thus a small phase-alignment concentration deficit forces the Fourier phase to be close, in the natural \(|\widehat f|\)-weighted square metric, to a constant phase.

## Assumptions and scope

The Fourier transform is normalized with the factor \(2\pi\) in the exponential, so Plancherel has no additional constant. A bounded interval \(W\) of length \(B\) ensures \(\widehat f\in L^1(W)\cap L^2(W)\). The observation set is specifically the centered interval \(I_T\); the theorem is not an operator-level assertion for arbitrary measurable observation sets. The strict condition \(BT<1\) keeps the interval Fourier kernel strictly positive over the full difference interval \(W-W\). No claim is made at \(BT=1\).

## Proof

Write
\[
K_T(\xi)=\int_{-T/2}^{T/2}e^{2\pi i\xi t}\,dt=
\begin{cases}\dfrac{\sin(\pi T\xi)}{\pi\xi},&\xi\ne0,\[4pt]T,&\xi=0.\end{cases}
\]
The quadratic-form identity, justified by \(\widehat f,\widehat g\in L^1(W)\) and Fubini's theorem, gives
\[
\int_{I_T}(|g|^2-|f|^2)\,dt=\iint_{W\times W}K_T(\eta-\omega)\Bigl(|\widehat f(\omega)||\widehat f(\eta)|-\operatorname{Re}(\widehat f(\omega)\overline{\widehat f(\eta)})\Bigr)\,d\omega\,d\eta.
\]
The parenthesized factor is nonnegative because \(\operatorname{Re}(z\overline w)\le |z||w|\). For \(|\xi|\le B\),
\[
K_T(\xi)=T\frac{\sin(\pi T|\xi|)}{\pi T|\xi|}\ge T\frac{\sin(\pi BT)}{\pi BT}>0,
\]
using that \(x\mapsto\sin x/x\) is decreasing on \((0,\pi)\). Therefore the double integral is bounded below by this minimum kernel value times
\[
\iint_{W\times W}\Bigl(|\widehat f(\omega)||\widehat f(\eta)|-\operatorname{Re}(\widehat f(\omega)\overline{\widehat f(\eta)})\Bigr)\,d\omega\,d\eta
=\|\widehat f\|_1^2-\left|\int_W\widehat f(\xi)\,d\xi\right|^2.
\]
Fourier inversion identifies the last integral with \(f(0)\), proving the inequality. The phase-distance consequence follows from
\[
\inf_{|\zeta|=1}\int_W|\widehat f|\,|u-\zeta|^2=2\left(A-|f(0)|\right),\qquad A=\|\widehat f\|_1,
\]
and \(A^2-|f(0)|^2\ge A(A-|f(0)|)\).

To prove optimality, take \(W=[-B/2,B/2]\). For \(0<\varepsilon<B/2\), set \(\widehat f_\varepsilon=(2\varepsilon)^{-1}\) on \([-B/2,-B/2+\varepsilon]\), set \(\widehat f_\varepsilon=-(2\varepsilon)^{-1}\) on \([B/2-\varepsilon,B/2]\), and set it to zero elsewhere. Then \(\|\widehat f_\varepsilon\|_1=1\) and \(f_\varepsilon(0)=0\). The phase-deficit integrand vanishes within each packet; only cross-packet pairs contribute, and their frequency differences tend uniformly to magnitude \(B\) as \(\varepsilon\downarrow0\). Consequently,
\[
\frac{\int_{I_T}(|g_\varepsilon|^2-|f_\varepsilon|^2)\,dt}{\|\widehat f_\varepsilon\|_1^2-|f_\varepsilon(0)|^2}\longrightarrow K_T(B)=T\frac{\sin(\pi BT)}{\pi BT}.
\]
No larger coefficient can hold uniformly over nonzero \(f\).

## Verification

The proof uses only the Fourier quadratic-form identity, positivity and monotonicity of the sinc kernel on \([0,\pi)\), and Fourier inversion for compactly supported \(L^1\) transforms. The optimality sequence is explicit and analytic; it is a limiting construction, not a claim of nonzero equality attainment. The derived phase-distance bound is a consequence of the main sharp inequality, not a separate optimal-constant claim.

## Relationship to prior work

Baeza-Guasch's phase-alignment theorem proves that replacing \(\widehat f\) by \(|\widehat f|\) maximizes concentration on a centered interval when the time–bandwidth product is at most one. The present statement adds an explicit lower bound for the concentration gain in the strict subcritical regime and proves that its coefficient is best possible. A 2026 stability result for the Paley–Wiener concentration problem instead controls distance to translated prolate spheroidal extremizers and the observation set's distance from an interval; it does not state this fixed-Fourier-modulus phase-deficit inequality. The comparison is at the level of the mathematical statements, not their titles.

## Limitations

The lower bound degenerates as \(BT\uparrow1\), and no positive uniform coefficient is asserted at the critical boundary. The result concerns a fixed Fourier modulus and a centered interval; it does not solve the unrestricted Donoho–Stark operator-level concentration problem. The sharpness construction shows optimality of the coefficient as a uniform constant, but does not classify all equality cases.

## References

1. O. Baeza-Guasch, “Phase symmetrization and a no-aliasing concentration principle in Paley–Wiener spaces,” arXiv:2307.04558, first submitted 10 July 2023; full-text statements used: Lemma 2.1, Theorem 2.2, Theorem 1.4, and Section 8.
2. D. Zelent, “Stability of concentration in the Paley–Wiener space,” arXiv:2610.01299, first submitted 1 October 2026; Theorem 1 and its proof are used only to compare the distinct global stability problem.
