# Three-phase two-cycle bifurcation and sharp stability in synchronized Huygens stars

## Finding
Let \(d\ge2\) be an integer, \(h>0\), \(c=(d+1)h\), and \(c_*=\sqrt{\pi^2+2}\). For the unit-weight, \(d\)-leaf discrete Huygens star
\[
G_h(z)=z+h(I_d+\mathbf 1\mathbf 1^{\mathsf T})\sin z\pmod {2\pi},\qquad z\in\mathbb T^d,
\]
its invariant diagonal \(\Delta=\{(t,\ldots,t):t\in\mathbb T\}\) has the following **complete classification of primitive period-two orbits** for \(0<c\le c_*\):

1. \(0<c\le2\): none.
2. \(2<c<\pi\): exactly one, \(\{\pi-s,\pi+s\}\) with unique \(s\in(0,\pi/2)\) solving \(c\sin s=2s\). It is a hyperbolic attracting two-cycle for the **full \(d\)-torus map**.
3. \(c=\pi\): exactly one, \(\{\pi/2,3\pi/2\}\), with all \(d\) two-step multipliers equal to \(1\).
4. \(\pi<c\le c_*\): exactly three: the continued symmetric orbit \(\{\pi-s,\pi+s\}\), where \(s\in(\pi/2,\pi)\), and two opposite-phase orbits \(\{t_\pm,t_\pm+\pi\}\), where \(t_-=\arcsin(\pi/c)\), \(t_+=\pi-\arcsin(\pi/c)\). The symmetric orbit is hyperbolically repelling; the opposite-phase orbits are hyperbolically attracting for \(\pi<c<c_*\). At \(c=c_*\), both opposite-phase orbits have one two-step multiplier \(-1\), while the other \(d-1\) multipliers remain strictly between \(0\) and \(1\).

The exact nontrivial two-step Floquet spectra are:
\[
\begin{array}{ll}
\text{symmetric orbit:}&(1-c\cos s)^2,\quad (1-\frac{c}{d+1}\cos s)^2\text{ with multiplicity }d-1;\\
\text{each opposite-phase orbit:}&1+\pi^2-c^2,\quad 1-\frac{c^2-\pi^2}{(d+1)^2}\text{ with multiplicity }d-1.
\end{array}
\]
Near the symmetry-breaking parameter \(c=\pi\), the two new representatives obey
\[
t_\pm=\frac\pi2\pm\sqrt{\frac{2(c-\pi)}{\pi}}+O((c-\pi)^{3/2}),
\]
with signs assigned by the two roots. The two attracting periodic states beyond \(\pi\) are genuine basins of attraction in the ambient phase-difference torus, not merely in the diagonal.

## Assumptions and scope
The sine function is taken componentwise and the unit-weight star is oriented from the central oscillator to each leaf. The diagonal is invariant because \((I_d+\mathbf1\mathbf1^{\mathsf T})\mathbf1=(d+1)\mathbf1\). Thus the restricted map is the standard zero-drift sine circle map \(f_c(t)=t+c\sin t\pmod{2\pi}\). A periodic orbit is primitive of period two if its first return is exactly two steps and it is not fixed. The classification counts **only those two-cycles lying in \(\Delta\)**; it makes no assertion that the full torus lacks off-diagonal periodic orbits.

## Proof
**(1) No wrapping in the stated parameter range.** On \([0,\pi]\), \(f_c(t)>t\) in the interior. For \(c\le2\), \(f_c(t)\le\pi+2<2\pi\). When \(2<c\le c_*\), the interior maximum occurs at \(t_c=\arccos(-1/c)\le2\pi/3\), giving \(f_c(t)\le2\pi/3+c_*<2\pi\). Reflection \(f_c(2\pi-t)=2\pi-f_c(t)\) shows that \([0,2\pi]\) maps into itself. Therefore no reduction modulo \(2\pi\) is needed to classify cycles in this range; the endpoints represent the same fixed point.

**(2) Exhaustion of primitive two-cycles.** Any nonfixed two-cycle must have one representative \(x\in(0,\pi)\) and its successor \(y\in(\pi,2\pi)\): in the upper half \(f_c(t)<t\), and in the lower half \(f_c(t)>t\), excluding a two-cycle confined to one half. From \(y=x+c\sin x\) and \(x=y+c\sin y\), adding yields \(\sin y=-\sin x\). With \(x\in(0,\pi)\), \(y\in(\pi,2\pi)\), this forces exactly either \(y=2\pi-x\) or \(y=x+\pi\). In the first case \(x=\pi-s\) and \(c\sin s=2s\). Since \(2s/\sin s\) is strictly increasing from \(2\) to infinity on \((0,\pi)\), this branch exists uniquely exactly when \(c>2\); it crosses \(s=\pi/2\) at \(c=\pi\). In the second case \(c\sin x=\pi\): zero, one, or two solutions according as \(c<\pi\), \(c=\pi\), or \(c>\pi\). At \(c=\pi\) that solution coincides with the symmetric branch. This proves that the list is exhaustive, including threshold counts.

**(3) Ambient stability.** On the diagonal at phase \(t\), the Jacobian is \(I_d+h\cos t(I_d+\mathbf1\mathbf1^{\mathsf T})\). Its longitudinal eigenvalue is \(1+c\cos t\); every transverse eigenvalue is \(1+h\cos t\). Because these matrices commute at the two points, multiply corresponding eigenvalues to get the stated spectra. On the symmetric orbit, the two cosines coincide at \(-\cos s\). For \(2<c<\pi\) one has \(s\in(0,\pi/2)\) and \(0<c\cos s=2s\cot s<2\); also \(0<h\cos s<\pi/(d+1)\le\pi/3<2\). Both squared multipliers are strictly below \(1\). For \(c>\pi\), \(\cos s<0\), making both squared multipliers strictly greater than \(1\). At \(c=\pi\), both equal \(1\). On either opposite-phase orbit the cosines have opposite signs and \(c^2\cos^2 t=c^2-\pi^2\). This gives the second spectrum. Both multipliers lie strictly between \(-1\) and \(1\) for \(\pi<c<c_*\), since \(0<c^2-\pi^2<2\) and \(d+1\ge3\). At \(c=c_*\), the longitudinal multiplier equals \(-1\), and the transverse multiplier equals \(1-2/(d+1)^2\in(0,1)\).

**(4) Branch opening.** Put \(c=\pi+\delta\), \(\delta\downarrow0\). The identity \(\sin t=\pi/c=1-\delta/\pi+O(\delta^2)\) and the nondegenerate quadratic maximum of sine at \(\pi/2\) give the claimed square-root splitting with the stated error.

## Verification
The included standalone Python checker verifies the exact pair equations and the longitudinal/transverse Floquet products for \(d\in\{2,3,5,11\}\) and nine parameter values spanning all branches and both boundaries. It reports `CHECK_OK 456`. These are finite tests; all-period and all-dimension assertions follow from the preceding analytic proof, not numerical enumeration. Run `python3 checker.py` with the standard library only.

## Relationship to prior work
Buescu, D'Aniello, and Oliveira, *Morse–Smale dynamics in discrete Huygens networks* (arXiv:2610.10993v1, Sections 2, 4 and 5.2), establish the star quotient matrix and a Morse–Smale diffeomorphism regime \(0<h<1/4\) for the three-leaf star, corresponding to \(c<1\) on its diagonal. Their main results classify fixed points and transversality in this small-step regime; the exact diagonal period-two count, the symmetry-breaking at \(c=\pi\), and the ambient multipliers for \(c>2\) are not stated there. The scalar restriction belongs to the classical sine/Arnold circle-map family; the scalar circle map and qualitative period-doubling phenomenon are not claimed as new. The contribution is the exact exhaustion with the dimension-dependent **ambient** Floquet spectrum and its sharp two-attractor window for this star-network family.

## Limitations
This is a theorem about diagonal two-cycles only, not a global phase portrait or a proof of absence of off-diagonal cycles. Other periods may coexist. The cutoff \(c_*\) is the sharp stability endpoint for the two newly born attracting diagonal cycles, **not** a claim about subsequent cycles or a globally maximal interval of any simpler symbolic dynamics. The formulation does not settle Morse–Smale properties beyond the source's invertibility regime. Classical circle-map literature may contain equivalent scalar branch calculations; searches of accessible papers do not establish absolute novelty. No independent external audit has been performed.

## References
- J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first posted 2026-10-07, https://arxiv.org/html/2610.10993v1.
- J. Buescu, H. M. Oliveira, *Lyapunov functions for Morse–Smale synchronisation diffeomorphisms*, arXiv:2503.13230, https://arxiv.org/abs/2503.13230.
- E. W. Weisstein, *Circle Map*, MathWorld, https://mathworld.wolfram.com/CircleMap.html (background on the scalar family).
- H. Osinga, J. Wiersig, P. Glendinning, U. Feudel, *Multistability and nonsmooth bifurcations in the quasiperiodically forced circle map*, arXiv:nlin/0005032 (different, quasiperiodically forced model).
