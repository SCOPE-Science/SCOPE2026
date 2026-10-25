# Transversely unstable period-doubling cycles in the discrete Huygens triangle

## Finding

Consider the edge-difference quotient of three identical repulsively coupled phase oscillators. Let
\[
\mathcal Z=\left\{z\in(\mathbb R/2\pi\mathbb Z)^3:\ z_1+z_2+z_3\equiv0\pmod{2\pi}\right\},\qquad
G_h(z)=z+h(3I-\mathbf1\mathbf1^{\mathsf T})\sin z\pmod{2\pi},
\]
with \(h>0\). The two uniform twisted fixed points are \(z_*=\pm(2\pi/3)\mathbf1\). Both eigenvalues of their derivative on \(\mathcal Z\) equal \(1-3h/2\); they reach \(-1\) simultaneously at \(h_*=4/3\).

**Theorem.** There exists \(\varepsilon>0\) such that, for every \(h\in(h_*,h_*+\varepsilon)\), on each of the three reflection-fixed lines through each twisted fixed point, exactly one sufficiently nearby nonconstant primitive period-two orbit exists. These six orbits are pairwise distinct. Each is an attracting two-cycle *within its reflection-fixed line* but a **hyperbolic saddle on the two-dimensional quotient**. For \(\delta=h-h_*>0\), its two return multipliers satisfy
\[
\mu_{\parallel}=1-6\delta+O(\delta^2),\qquad
\mu_{\perp}=1+\frac{63}{10}\delta^2+O(\delta^3).
\]
For \(h\le h_*\) sufficiently close to \(h_*\), there is no nonconstant period-two orbit sufficiently close to either twist *within those reflection-fixed lines*.

## Assumptions and scope

All trigonometric functions act coordinatewise. The quotient \(\mathcal Z\) is a two-torus, and the theorem concerns prime-period-two orbits of \(G_h\) on this quotient, not a statement about absolute phase for a chosen lift of the oscillator network. Neighbourhoods of the two twists are chosen disjoint, and all computations use their local real lifts. A reflection-fixed line consists of configurations whose two nondistinguished edge coordinates agree. The assertion of uniqueness applies separately on each such line, not to all two-cycles in the entire two-torus.

## Proof

The matrix \(K=3I-\mathbf1\mathbf1^{\mathsf T}\) acts as \(3I\) on the tangent plane \(E=\{u\in\mathbb R^3:\sum u_i=0\}\). At \(z_*=(2\pi/3)\mathbf1\), the derivative is \(I+hK\cos(2\pi/3)=(1-3h/2)I\) on \(E\). The other fixed point and its local branches follow by the exact symmetry \(z\mapsto-z\). Cyclic coordinate permutations give the three reflection axes. It therefore suffices to analyze
\[
z(a)=\left(\alpha+2a,\alpha-a,\alpha-a\right),\qquad\alpha=2\pi/3.
\]
Because \(3\alpha=2\pi\), these are valid points of \(\mathcal Z\). The map preserves this line and acts there as \(a\mapsto f_h(a)=a+h\Delta(a)\), where
\[
\Delta(a)=\sin(\alpha+2a)-\sin(\alpha-a).
\]
A small nonconstant two-cycle has points \(a=m+d\) and \(b=m-d\), with \(d\ne0\). The two equations \(f_h(a)=b\), \(f_h(b)=a\) are equivalent to
\[
\Delta(m+d)+\Delta(m-d)=0,\qquad
h[\Delta(m+d)-\Delta(m-d)]=-4d. \tag{1}
\]
Since \(\Delta'(0)=-3/2\), the analytic implicit-function theorem applied to the first equation gives a unique analytic even function \(m=m(d)\) near zero, with \(m(0)=0\). The second equation then uniquely specifies the even analytic function
\[
h(d)=-\frac{4d}{\Delta(m(d)+d)-\Delta(m(d)-d)},
\]
whose removable value at zero is \(h(0)=4/3\). The Taylor expansion
\[
\Delta(t)=-\frac32t-\frac{3\sqrt3}{4}t^2+\frac34t^3+\frac{5\sqrt3}{16}t^4-\frac{11}{80}t^5-\frac{7\sqrt3}{160}t^6+O(t^7)
\]
inserted into (1) yields
\[
m(d)=-\frac{\sqrt3}{2}d^2-\frac{11\sqrt3}{12}d^4+O(d^6),\qquad
h(d)=\frac43+\frac83d^2+\frac{392}{45}d^4+O(d^6). \tag{2}
\]
Thus \(h(d)>4/3\) and is strictly increasing for sufficiently small \(d>0\). For every sufficiently small positive \(\delta=h-4/3\), there is exactly one \(d>0\) and consequently one unordered two-cycle on the line. Its amplitude is \(d=\sqrt{3\delta/8}+O(\delta^{3/2})\). Conversely no sufficiently nearby nontrivial two-cycle on that line exists at \(h\le4/3\).

For stability, at \(z(a)\) the derivative of \(G_h\) on \(E\) has two invariant, independent directions \(v=(2,-1,-1)\) and \(w=(0,1,-1)\), with eigenvalues
\[
T_h(a)=1+h\bigl[2\cos(\alpha+2a)+\cos(\alpha-a)\bigr],\qquad
S_h(a)=1+3h\cos(\alpha-a).
\]
The two eigenvalues of the second return derivative are exactly
\[
\mu_{\parallel}=T_h(m+d)T_h(m-d),\qquad
\mu_{\perp}=S_h(m+d)S_h(m-d).
\]
Substitution of (2), using Taylor expansions through fourth order, gives
\[
\mu_{\parallel}=1-16d^2-\frac{848}{15}d^4+O(d^6),\qquad
\mu_{\perp}=1+\frac{224}{5}d^4+O(d^6). \tag{3}
\]
Since \(d^2=(3/8)\delta+O(\delta^2)\), (3) yields the stated expansions. Thus \(0<\mu_{\parallel}<1<\mu_{\perp}\) for all sufficiently small \(\delta>0\), proving that the two-cycle is a hyperbolic saddle on \(\mathcal Z\) despite being attracting on its symmetry line.

The three coordinate choices of the distinguished site give distinct branches, since different reflection-fixed lines meet near the twist only at the twist itself; the cycles are nonconstant. Negating the phases transports these three branches to the other twist, and the disjoint twist neighbourhoods make all six distinct. This completes the proof.

## Verification

The standalone `verify.py` uses exact symbolic Taylor expansions to check the coefficients in (2) and (3) and high-precision root solving to check seven parameter values. It also evaluates the original three-coordinate map at both points of each candidate two-cycle and computes both return multipliers. Run it with `python verify.py` after installing the dependency stated in `requirements.txt`. The existence, uniqueness, and signs over a nonempty open parameter interval are established by the analytic argument, not by finite numerical tests.

## Relationship to prior work

Buescu and Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings* (arXiv:2610.19953v1, publicly posted 14 October 2026), identify the twisted equilibria, their fixed-point multipliers and the threshold \(4/3\) for their linear sink property on the triangle. Their global convergence theorem is confined to the strictly smaller Lyapunov interval. The period-two branches, their precise transverse instability and the quartic-order cancellation in the transverse return multiplier are not stated in its examined sections. Earlier three-oscillator Lyapunov work and the recent network Morse–Smale criterion concern small-step dynamics. Generic equivariant-map period-doubling theory provides context, but the explicit coefficient and sign here arise from the specific sine interaction.

## Limitations

This is a local result for \(h\) just above \(4/3\), restricted to the three reflection-invariant families through each twist. It does not exclude other symmetry-breaking period-two orbits, classify higher periods, or describe distant supercritical parameters. Multipliers refer to the common-phase quotient; the original phase map has an additional neutral common-phase direction. Claims of global bibliographic priority are not made, and no independent audit has been performed.

## References

1. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (14 October 2026), https://arxiv.org/html/2610.19953v1.
2. J. Buescu and H. M. Oliveira, *Lyapunov functions for Morse–Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (2025), https://arxiv.org/abs/2503.13230.
3. J. Buescu, E. D’Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (2026), https://arxiv.org/abs/2610.10993.
4. P. Chossat and M. Golubitsky, *Iterates of Maps with Symmetry*, SIAM J. Math. Anal. 19 (1988), 1259–1270, https://doi.org/10.1137/0519092 (general context).
