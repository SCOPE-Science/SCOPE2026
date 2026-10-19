# Simultaneous supercritical period-four births and full-network attraction in Huygens stars

## Finding

For any integer \(d\ge2\), the \(d\)-leaf star quotient is the \(d\)-torus map \(G_h(z)=z+h(I_d+\mathbf1\mathbf1^{\mathsf T})\sin z\pmod{2\pi}\). Its invariant diagonal \(z=x\mathbf1\) evolves by \(F_\alpha(x)=x+\alpha\sin x\pmod{2\pi}\), with \(\alpha=(d+1)h\). Define
\[
\alpha_*=\sqrt{\pi^2+2},\qquad \varepsilon=\alpha^2-\alpha_*^2.
\]
At \(\alpha=\alpha_*\), each of the two distinct antipodal prime-two orbits has an eigenvalue \(-1\) for the two-step map. Each undergoes a **supercritical flip**, producing one **full-torus attracting** diagonal prime-four orbit for all sufficiently small \(\varepsilon>0\) (the smallness requirement can depend on \(d\)). There are **no nearby prime-four orbits, diagonal or otherwise**, for small \(\varepsilon<0\).

For \(\sigma\in\{+,-\}\), let
\[
x_+(\alpha)=\arcsin(\pi/\alpha),\qquad
x_-(\alpha)=\pi-\arcsin(\pi/\alpha),\qquad
B_\pm=\frac{(2\pm\sqrt2)(5\pi^2+2)}{2}>0.
\]
The four-cycle has two points near \(x_\sigma(\alpha)\), located at
\[
x_\sigma(\alpha)\pm\sqrt{\frac{\varepsilon}{B_\sigma}}+O(\varepsilon),
\]
and its other two points lie near \(x_\sigma(\alpha)+\pi\). Its four-step multiplier is
\[
\mu_{4,\sigma}=1-4\varepsilon+O(\varepsilon^{3/2}).
\]
The ratio of the two local half-splittings, positive branch divided by negative branch, tends exactly to \(\sqrt2-1\). The remaining \(d-1\) four-step Floquet multipliers are each \(\bigl(1-2/(d+1)^2\bigr)^2+O_d(\sqrt\varepsilon)\), strictly inside the unit circle. The two newly created orbits are distinct and interchanged by global phase reflection.

## Assumptions and scope

The family is the \(d\)-leaf positively unit-weight Huygens star for every fixed integer \(d\ge2\); the associated edge-quotient coupling matrix is \(I_d+\mathbf1\mathbf1^{\mathsf T}\). The single-edge two-oscillator case obeys the same scalar diagonal formula but has no transverse modes. All statements concern a sufficiently small real parameter neighborhood of \(\alpha_*\), always with \(\alpha>\pi\). The term **locally** means in fixed sufficiently small disjoint neighborhoods of the four diagonal parent period-two points at criticality, in the **entire** \(d\)-torus. The orbits are prime-four for the full map \(G_h\); all Floquet multipliers refer to \(G_h^4\). No claim is made about the full global period-four spectrum.

## Proof

**1. Two parent prime-two cycles on the invariant diagonal.** As \(I_d+\mathbf1\mathbf1^{\mathsf T}\) acts by \(d+1\) on \(\mathbf1\), the diagonal restriction of the full map is exactly \(F_\alpha\). For every \(\alpha>\pi\), write \(u=\arcsin(\pi/\alpha)\in(0,\pi/2)\). Since \(\alpha\sin u=\alpha\sin(\pi-u)=\pi\), both
\[
\{u,u+\pi\},\qquad\{\pi-u,2\pi-u\}
\]
are distinct prime-two orbits, because \(F_\alpha(x_\sigma)=x_\sigma+\pi\), \(F_\alpha(x_\sigma+\pi)=x_\sigma\). Smooth real lifts can be chosen near these orbits. Define \(g_\sigma=F_\alpha^2\) in such a lift. Put \(t_\sigma=\alpha\cos x_\sigma=\sigma\sqrt{\alpha^2-\pi^2}\) (\(\sigma=+1\) or \(-1\)). The derivative is
\[
g_\sigma'(x_\sigma)=(1+t_\sigma)(1-t_\sigma)=1+\pi^2-\alpha^2=-1-\varepsilon.
\]
Therefore both parent cycles cross the flip multiplier at exactly the same \(\alpha_*\), transversely since \(\partial_\alpha g_\sigma'(x_\sigma)=-2\alpha_*\ne0\).

**2. Exact nondegeneracy coefficient.** The chain rule, with \(F'(x_\sigma)=1+t_\sigma\), \(F''(x_\sigma)=-\pi\), \(F'''(x_\sigma)=-t_\sigma\), and with the opposite corresponding signs at \(x_\sigma+\pi\), yields
\[
\begin{aligned}
g_\sigma''(x_\sigma)&=\pi(3t_\sigma+t_\sigma^2),\\
g_\sigma'''(x_\sigma)&=4t_\sigma^2+3t_\sigma^3+t_\sigma^4-3\pi^2(1+t_\sigma).
\end{aligned}
\]
The standard scalar flip normal-form invariant is
\[
B_\sigma=\left(\frac{g_\sigma''(x_\sigma)}2\right)^2
+\frac{g_\sigma'''(x_\sigma)}6
\quad\text{evaluated at }\alpha=\alpha_*.
\]
Inserting \(t_\sigma=\sigma\sqrt2\) and simplifying gives the two **strictly positive** values
\[
B_\pm=\frac{(2\pm\sqrt2)(5\pi^2+2)}2.
\]
This sign is not implied merely by the parent multiplier crossing.

**3. Diagonal creation, uniqueness, amplitude and longitudinal stability.** Set \(y=x-x_\sigma(\alpha)\). Smooth Taylor expansion of the **recentered** return \(\widetilde g_\sigma(y):=g_\sigma(x_\sigma+y)-x_\sigma\) gives
\[
\widetilde g_\sigma(y)=-(1+\varepsilon)y+a_\sigma y^2+b_\sigma y^3+O(y^4),
\]
where coefficients depend smoothly on \(\varepsilon\) and \(a_\sigma(0)^2+b_\sigma(0)=B_\sigma\). Composition of this recentered return yields
\[
\widetilde g_\sigma^2(y)-y
=2\varepsilon y-2B_\sigma y^3
+O(\varepsilon^2|y|+|\varepsilon|y^2+|y|^4).
\]
Because \(y=0\) is always the parent fixed point of \(g_\sigma\), divide the expression by \(y\), extending smoothly to zero. The resulting smooth function has \(y\)-second derivative \(-4B_\sigma+o(1)<0\) uniformly near the origin, value \(2\varepsilon+O(\varepsilon^2)\) and first derivative \(O(\varepsilon)\) at zero. Consequently its unique local maximum is at \(y=O(\varepsilon)\) and equals \(2\varepsilon+O(\varepsilon^2)\). For a sufficiently small fixed neighborhood its two endpoint values are negative. Strict concavity gives exactly two nonzero roots if \(\varepsilon>0\), and none if \(\varepsilon<0\). Rescale \(y=\sqrt\varepsilon z\); the two zeros satisfy \(z=\pm B_\sigma^{-1/2}+O(\sqrt\varepsilon)\). Since the recentered map has a unique local fixed point by its derivative \(-1+o(1)\), the new points form one prime-two orbit of \(g_\sigma\), hence one prime-four orbit of \(F_\alpha\).

Differentiating the squared-return expansion at the new roots gives
\[
(F_\alpha^4)'=1+2\varepsilon-6B_\sigma\frac{\varepsilon}{B_\sigma}+O(\varepsilon^{3/2})
=1-4\varepsilon+O(\varepsilon^{3/2}),
\]
strictly inside the unit circle for small positive \(\varepsilon\). The two parental prime-two orbits are disjoint at the crossing and remain so nearby, hence the two born four-cycles are distinct. The sinusoidal oddness \(F_\alpha(-x)=-F_\alpha(x)\pmod{2\pi}\) interchanges them. Finally,
\[
\sqrt{\frac{B_-}{B_+}}=
\sqrt{\frac{2-\sqrt2}{2+\sqrt2}}=\sqrt2-1,
\]
proving the amplitude ratio.

**4. Full-network attraction and exclusion of nondiagonal daughter orbits.** At every diagonal configuration \(z=x\mathbf1\),
\[
DG_h(z)=I_d+h\cos(x)(I_d+\mathbf1\mathbf1^{\mathsf T}).
\]
The longitudinal eigenvalue is \(1+\alpha\cos x\); the other \(d-1\) eigenvalues are all \(1+\alpha\cos x/(d+1)\). These eigenspaces are parameter-independent, so derivatives along a diagonal periodic orbit commute. At either antipodal parent orbit the two-step transverse multiplier is
\[
\left(1+\frac{t_\sigma}{d+1}\right)
\left(1-\frac{t_\sigma}{d+1}\right)
=1-\frac{\alpha^2-\pi^2}{(d+1)^2}.
\]
At the flip threshold, the transverse multiplier of the **four-step** map is \(q_d=\bigl(1-2/(d+1)^2\bigr)^2\), strictly between zero and one for every \(d\ge2\). Continuity along the newborn diagonal four-cycles gives \(d-1\) transverse four-step multipliers \(q_d+O_d(\sqrt\varepsilon)\). Hence, for each fixed finite \(d\), all of these and the longitudinal multiplier are in the open unit disk for sufficiently small positive \(\varepsilon\): both new four-cycles are attracting in the **full phase torus**, not merely inside the diagonal.

For local completeness, decompose \(z=y\mathbf1+w\) with \(w\perp\mathbf1\), and consider the transverse component of \(G_h^4(z)-z\) near any one of the four critical parent points. Its derivative with respect to \(w\) at criticality is \((q_d-1)I\), invertible. The diagonal \(w=0\) solves this transverse equation for every nearby \(y\) and parameter. By the implicit-function theorem it is the **unique** local transverse solution. Thus every nearby fixed point of \(G_h^4\) lies on the diagonal, so the scalar strict-concavity count in part 3 exhausts **all** local prime-four cycles of the full system on both sides of the threshold.

## Verification

The self-contained `verify.py` uses Python's standard library. It checks the displayed chain-rule derivatives with independently assembled algebraic formulas, tests the full-network transverse multiplier identity for several star sizes, and numerically brackets the four new diagonal roots of \(F_\alpha^4(x)-x\) for several small positive values of \(\varepsilon\), with computed four-step multipliers in \((-1,1)\). These diagnostics are finite and **do not substitute** for the analytic local existence/uniqueness and stability argument above. Run `python3 verify.py` in the extracted package directory.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (2026, arXiv:2610.10993v1, primary MSC2020 37C05) introduce the reciprocal discrete network quotient and prove its Morse–Smale window; they do not classify this strong-step daughter-four bifurcation. Earlier analysis of synchronized Huygens-star diagonal subspaces had already identified the antipodal prime-two cycles and their exact multiplier crossing at \(\alpha_*\), so **their existence, previous stability, and the crossing itself are not new assertions here**. What is established here is the nonzero signed cubic coefficient on **both** branches, the locally exhaustive birth of two *prime-four* orbits across **all star dimensions**, their full-network attraction, amplitude asymptotics and all multipliers. General one-dimensional flip normal-form theory predicts a flip conditional on the sign of a coefficient, not its sign or multiplicity for this network. Oliveira and Melo's 2015 impact-based two-clock study addresses a different physical phase update.

## Limitations

The claim is local to \(\alpha_*\), not a global four-cycle census. It concerns positive unit-weight stars for any fixed finite leaf count; it does not extend to arbitrary weighted graphs or give a leaf-count-uniform parameter neighborhood. Its mathematical validity follows from the local Taylor and concavity proof, but unrecognized coverage in the older standard sine-circle-map literature remains a priority risk. Independent audit and comprehensive bibliographic priority certification have not been performed.

## References

1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public 2026-10-07), https://arxiv.org/abs/2610.10993.
2. H. M. Oliveira and L. V. Melo, *Huygens synchronization of two clocks*, Scientific Reports **5**, 11548 (2015), https://doi.org/10.1038/srep11548.
3. E. W. Weisstein, *Circle Map*, MathWorld, https://mathworld.wolfram.com/CircleMap.html (standard sine-circle-map normalization).
4. Prior analysis: *Three-phase two-cycle bifurcation and sharp stability in synchronized Huygens stars* (previous result describing the parent two-cycles and the first \(-1\) crossing).
