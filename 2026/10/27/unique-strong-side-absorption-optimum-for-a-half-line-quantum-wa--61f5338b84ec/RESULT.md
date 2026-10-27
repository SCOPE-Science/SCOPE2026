# Unique strong-side absorption optimum for a half-line quantum walk

## Finding

For the semi-infinite tight-binding quantum walk with one Lindblad boundary absorber, initialized at any fixed lattice site \(m\ge 2\), **the eventual absorption probability has exactly one maximizer** \(\eta_m\) over all positive dimensionless loss rates \(\eta\). It lies strictly on the strong-absorption side of the boundary-mode transition:

\[
1<\eta_m<\sqrt3.
\]

The absorption probability is strictly increasing for \(0<\eta<\eta_m\) and strictly decreasing for \(\eta>\eta_m\). As the initial site recedes,

\[
\eta_m=1+\frac{3}{4m^3}+\frac{9}{8m^4}+O(m^{-5}),
\qquad
P_m(\eta_m)-P_m(1)=\frac{3}{16\pi m^6}+O(m^{-7}).
\]

There is a strict **finite-distance failure of weak–strong reciprocal symmetry**. For every \(m\ge2\) and \(\eta>1\),

\[
P_m(\eta)-P_m(\eta^{-1})
=\frac{2\eta(\eta^2-1)}{\pi}\int_0^1
\frac{q^{2m-2}(1-q^2)^2}{(1+\eta^2q^2)(\eta^2+q^2)}\,dq>0.
\]

For fixed \(\eta>1\), the difference is asymptotic to \(2\eta(\eta^2-1)/[\pi(1+\eta^2)^2m^3]\). For example, numerical roots of the exact stationarity equation are \(\eta_2=1.128036558506\ldots\), \(\eta_3=1.035875451023\ldots\), and \(\eta_4=1.014695527529\ldots\). These examples are not used to establish uniqueness.

## Assumptions and scope

Let \(\mathcal H=\ell^2(\{1,2,\ldots\})\), let \(\Omega>0\) and \(\kappa>0\), and put

\[
H_+=\Omega I-\frac{\Omega}{2}\sum_{s\ge1}(|s\rangle\langle s+1|+|s+1\rangle\langle s|),\qquad
L=\sqrt\kappa\,|\emptyset\rangle\langle1|,\qquad \eta=\kappa/\Omega.
\]

Initially the walker occupies the basis state \(|m\rangle\) for a fixed integer \(m\ge2\). The surviving sector evolves through \(H_{\rm eff}=H_+-i\kappa|1\rangle\langle1|/2\). Define

\[
P_m(\eta)=\lim_{t\to\infty}\left(1-\|e^{-iH_{\rm eff}t}|m\rangle\|^2\right).
\]

The exact integral representation established by Riberi, arXiv:2605.08056, is an input, not a new contribution:

\[
P_m(\eta)=B(\eta)+C_m(\eta),\quad
B(\eta)=\frac{2\eta}{\pi}\int_0^\pi
\frac{\sin k}{1+\eta^2+2\eta\sin k}\,dk,\quad
C_m(\eta)=\frac{2\eta}{\pi}\int_0^1
\frac{q^{2m-2}(1-q^2)}{1+\eta^2q^2}\,dq.
\]

Every assertion here concerns **total eventual absorption**, not mean absorption time, finite-time survival, or a finite lattice. The case \(m=1\) is excluded because its optimization behavior is different. The source's dimensionless hopping/loss normalization is retained throughout.

## Proof

**1. Derivatives and the weak-coupling side.** Differentiation under the absolutely integrable kernels gives

\[
B'(\eta)=\frac{2(1-\eta^2)}\pi\int_0^\pi
\frac{\sin k}{(1+\eta^2+2\eta\sin k)^2}\,dk,
\]

\[
C_m'(\eta)=\frac2\pi\int_0^1
\frac{q^{2m-2}(1-q^2)(1-\eta^2q^2)}{(1+\eta^2q^2)^2}\,dq.
\]

Both are strictly positive for \(0<\eta<1\), while \(B'(1)=0<C_m'(1)\). Hence an optimizer cannot lie at or below one.

**2. Strict concavity through the candidate interval.** A second derivative yields

\[
B''(\eta)=\frac4\pi\int_0^\pi
\frac{\sin k[\eta(\eta^2-3)-2\sin k]}{(1+\eta^2+2\eta\sin k)^3}\,dk<0,
\qquad1\le\eta\le\sqrt3,
\]

\[
C_m''(\eta)=-\frac{4\eta}\pi\int_0^1
\frac{q^{2m}(1-q^2)(3-\eta^2q^2)}{(1+\eta^2q^2)^3}\,dq<0,
\qquad1\le\eta\le\sqrt3.
\]

Thus \(P_m'\) is strictly decreasing on \([1,\sqrt3]\). The following two steps show that it stays negative afterward.

**3. Excluding additional stationary points through twice the hopping rate.** For \(\sqrt3\le\eta\le2\), using \(1+\eta^2+2\eta\sin k\le(1+\eta)^2\) gives

\[
-B'(\eta)\ge\frac{4(\eta-1)}{\pi(\eta+1)^3}
\ge\frac{4(\sqrt3-1)}{\pi(1+\sqrt3)^3}
>\frac{2}{9\sqrt3\pi}.
\]

Only the region \(0<q<1/\eta\) can contribute positively to \(C_m'\). Since \(m\ge2\), discarding factors at most one bounds it by

\[
C_m'(\eta)\le \frac2\pi\int_0^{1/\eta}q^2\,dq
=\frac{2}{3\pi\eta^3}\le\frac{2}{9\sqrt3\pi}.
\]

The second inequality for \(-B'\) uses the fact that \((\eta-1)/(\eta+1)^3\) increases on \([\sqrt3,2]\). Therefore \(P_m'(\eta)<0\) throughout \([\sqrt3,2]\).

**4. Excluding additional stationary points for all greater losses.** An elementary integration gives

\[
C_2'(\eta)=\frac4{\pi\eta^5}
\left[(\eta^2+2)\arctan\eta-\frac{\eta^3}{3}-2\eta\right].
\]

Let \(g(\eta)=\eta^3/3+2\eta-(\eta^2+2)\arctan\eta\). At \(\eta=2\), \(g(2)>0\), since \(\arctan2<10/9\), as follows from \(\arctan2=\pi/4+\arctan(1/3)\), \(\pi<22/7\), and the first three terms of the alternating arctangent expansion. Furthermore,

\[
g'(\eta)=\eta h(\eta),\quad
h(\eta)=\eta+\frac\eta{1+\eta^2}-2\arctan\eta,\quad
h'(\eta)=\frac{\eta^2(\eta^2-1)}{(1+\eta^2)^2}>0
\quad(\eta>1).
\]

The same \(\arctan2<10/9\) bound gives \(h(2)>8/45>0\), so \(g>0\) and \(C_2'<0\) for every \(\eta\ge2\). For general \(m\ge2\), the integrand defining \(C_m'\) equals the integrand of \(C_2'\) multiplied by \(q^{2(m-2)}\). The \(C_2'\) integrand is positive only for \(q<1/\eta\) and negative for \(q>1/\eta\). Since the multiplying function is increasing, comparison with its value \(\eta^{-2(m-2)}\) at this unique sign change yields

\[
C_m'(\eta)\le\eta^{-2(m-2)}C_2'(\eta)<0,\qquad\eta\ge2.
\]

Because \(B'(\eta)<0\) for \(\eta>1\), we obtain \(P_m'<0\) on \([2,\infty)\). Steps 1–4 show that the strictly decreasing derivative on \([1,\sqrt3]\) crosses zero exactly once and that no other stationary point exists anywhere. This proves global and strict uniqueness.

**5. The reciprocal bias.** Substitute \(\eta^{-1}\) into the displayed integral for \(C_m\), use \(B(\eta^{-1})=B(\eta)\), and take the difference:

\[
\frac{2\eta}{\pi}\int_0^1q^{2m-2}(1-q^2)
\left(\frac1{1+\eta^2q^2}-\frac1{\eta^2+q^2}\right)dq.
\]

Simplifying the bracket proves the stated positive reciprocal-bias integral. As \(m\to\infty\), its mass concentrates near \(q=1\). The denominator converges there to \((1+\eta^2)^2\), and the exact beta integral

\[
\int_0^1q^{2m-2}(1-q^2)^2dq
=\frac{8}{(2m-1)(2m+1)(2m+3)}\sim m^{-3}
\]

proves its fixed-\(\eta\) asymptotic.

**6. Sharp optimizer and gain expansions.** Substituting \(z=q^2\) gives

\[
C_m'(1)=\frac1\pi\int_0^1
\frac{z^{m-3/2}(1-z)^2}{(1+z)^2}\,dz
=\frac{1}{2\pi m^3}+\frac{3}{4\pi m^4}+O(m^{-5}).
\]

The expansion follows by Taylor expansion of \((1+z)^{-2}\) around \(z=1\) and the exact beta integrals; the remaining term is bounded by a fourth-order beta moment. Direct substitution in the first second-derivative integral gives

\[
B''(1)=-\frac2{3\pi},\qquad C_m''(1)=O(m^{-2}).
\]

The latter bound follows from \(q^{2m}\) and the factor \(1-q^2\) in the integral. Since \(C_m'\to0\) uniformly on a fixed neighborhood of one while \(B'\) has its isolated negative-slope zero there, uniqueness places \(\eta_m\to1\). The stationarity equation and the uniform negative curvature near one first yield \(\eta_m-1=O(m^{-3})\); Taylor's theorem then gives

\[
\eta_m-1=\frac{3\pi}{2}C_m'(1)+O(m^{-5})
=\frac{3}{4m^3}+\frac{9}{8m^4}+O(m^{-5}).
\]

Finally, expanding \(P_m\) around one through the stationary point, the maximum improvement is

\[
P_m(\eta_m)-P_m(1)=\frac{[C_m'(1)]^2}{2(2/(3\pi))}+O(m^{-7})
=\frac{3}{16\pi m^6}+O(m^{-7}),
\]

where the remainder follows from the displayed derivative bounds. The assertion is an analytic large-distance result, not an extrapolation of computed roots.

## Verification

The standalone `verify.py` independently evaluates the two exact quadratures and their derivatives, locates the unique zeros numerically for selected initial positions, checks the reciprocal-difference identity on 25 parameter pairs, and compares infinite-time quadratures against finite-time non-Hermitian evolution on a 420-site truncation. It performs 129 finite diagnostics and reports passing results. Its finite propagation probabilities approach their infinite-time counterparts from below; no finite truncation is treated as a proof of the infinite-volume formulas. The complete all-distance and all-coupling result is proved in Steps 1–6, not inferred from computation.

## Relationship to prior work

Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk* (first posted as *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056, 2026), derives the half-line Lindblad dynamics and the integral formula for total absorption, identifies the boundary-mode transition at \(\eta=1\), and establishes the asymptotic reciprocal correspondence as the initial site recedes. These are antecedents, not new claims. The present result isolates the exact finite-distance departure: **one unique optimum at \(\eta_m>1\)**, a strict finite-distance reciprocal bias, and sharp cubic and sixth-order distance scales.

Other quantum-walk absorption papers use discrete-time projective absorbing boundaries or finite detector arrays. Those settings do not by themselves determine global optimization of this continuous-time half-line Lindblad absorption probability. Generic Zeno/reflection observations do not provide the uniqueness theorem or its constants.

## Limitations

The analysis fixes an unweighted homogeneous half-line, a single boundary sink, pure localized initial position \(m\ge2\), and time-independent positive rates. It does not characterize optimal finite-time absorption, mean arrival time, mixed initial states, multiple sinks, finite chains, noise, or the boundary-start case \(m=1\). The source's exact half-line absorption integral is assumed; this result establishes new consequences of it. Priority is assessed against inspected relevant sources and may require further independent literature review. Independent scientific audit has not been performed.

## References

1. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk* (earlier title *An Exactly Solvable Absorbing Quantum Walk*), arXiv:2605.08056, first public version 2026-05-08, https://arxiv.org/abs/2605.08056 . Model, resolvent, absorption probability, asymptotic duality; principal formula input.
2. E. Bach, S. Coppersmith, M. P. Goldschen, R. Joynt, and J. Watrous, *One-dimensional quantum walks with absorbing boundaries*, J. Comput. Syst. Sci. 69 (2004), 562–592. Discrete-time absorbing boundary formalism.
3. P. Kuklinski and M. Kon, *Absorption probabilities of quantum walks*, Quantum Information Processing 17 (2018), article 263. Discrete quantum walks and absorption-probability comparisons.
4. S. Stefanutti et al., *Implementation of Leaking Quantum Walks on a Photonic Processor*, arXiv 2026 preprint. Experimental discrete-time lossy quantum-walk setting, not an optimization formula for the present half-line Lindblad dynamics.
