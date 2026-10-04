# Unique rotational lossless tangent fractional plank cover of a circular annulus

## Finding
Let \(D=\{x\in\mathbb R^2:\|x\|\le1\}\), fix \(a\in(0,1)\), and put \(H=1-a\). For \(\theta\in[0,2\pi)\), write \(e_\theta=(\cos\theta,\sin\theta)\), and for \(h\in(0,H]\) define the outward tangent plank
\[
P_{\theta,h}=\{x\in\mathbb R^2:a\le\langle x,e_\theta\rangle\le a+h\}.
\]
Consider rotationally invariant fractional mixtures
\[
d\mu(\theta,h)=\frac{d\theta}{2\pi}\,d\nu(h),
\]
where \(\nu\) is a positive sigma-finite Borel measure on \((0,H]\) with finite first width moment. Let \(\Gamma(t)=\nu([t,H])\). Requiring the covering multiplicity to equal \(1\) at every point of \(D\setminus aD\) uniquely forces
\[
\Gamma(t)=\Gamma_a(t):=\frac{2(a+t)}{\sqrt{t(t+2a)}}\qquad(0<t\le H).
\]
Equivalently,
\[
d\nu(t)=\frac{2a^2}{[t(t+2a)]^{3/2}}\,dt+\frac{2}{\sqrt{1-a^2}}\,\delta_H.
\]
This mixture has multiplicity \(0\) on \(aD\), multiplicity \(1\) on \(D\setminus aD\), and total fractional plank width
\[
W_a=\int_{(0,H]}h\,d\nu(h)=2\sqrt{1-a^2}.
\]
At \(a=1/2\), the tail is \(\Gamma_{1/2}(t)=(2t+1)/\sqrt{t(t+1)}\) and \(W_{1/2}=\sqrt3\).

## Assumptions and scope
A fractional mixture is a positive measure on the plank parameters; its multiplicity at \(x\) is \(M(x)=\int\mathbf 1_P(x)\,d\mu(P)\), and its total width is \(\int w(P)\,d\mu(P)\). The inner disk \(aD\) is closed, so the target annulus \(D\setminus aD\) has \(a<\|x\|\le1\). The theorem classifies only rotationally invariant mixtures of planks whose inner boundary is tangent to \(aD\) and whose multiplicity is exactly lossless, namely \(M=1\), on the whole target annulus. It does not assert global optimality among arbitrary fractional plank covers.

## Proof
For a point \(x\) with \(\|x\|=d>a\), rotational invariance lets us take \(x=de_0\). A plank with direction \(\theta\) can contain \(x\) only when \(d\cos\theta\ge a\). With \(\alpha=\arccos(a/d)\), the covering multiplicity therefore is
\[
M(d)=\frac1\pi\int_0^\alpha \Gamma(d\cos\theta-a)\,d\theta.
\]
Put \(s=d-a\) and \(t=d\cos\theta-a\). Then
\[
\pi M(d)=\int_0^s\frac{\Gamma(t)}{\sqrt{(s-t)(s+t+2a)}}\,dt.
\]
Set \(y=s(s+2a)\), \(z=t(t+2a)\), and
\[
F(z)=\frac{\Gamma(\sqrt{a^2+z}-a)}{2\sqrt{a^2+z}}.
\]
The lossless condition \(M(d)=1\) becomes the Abel equation
\[
\int_0^y\frac{F(z)}{\sqrt{y-z}}\,dz=\pi
\qquad(0<y\le1-a^2).
\]
Applying the same Abel kernel once more and using Tonelli's theorem gives, for every \(Y\in(0,1-a^2]\),
\[
\begin{aligned}
2\pi\sqrt Y
&=\int_0^Y\frac{\pi}{\sqrt{Y-y}}\,dy\\
&=\int_0^Y F(z)\left[\int_z^Y\frac{dy}{\sqrt{(y-z)(Y-y)}}\right]dz\\
&=\pi\int_0^Y F(z)\,dz.
\end{aligned}
\]
The bracketed beta integral equals \(\pi\). Hence \(\int_0^YF(z)\,dz=2\sqrt Y\), so \(F(Y)=Y^{-1/2}\) almost everywhere. Since a tail is right-continuous and the target expression is continuous away from \(0\), the equality holds for every positive argument. Undoing the substitution yields
\[
\Gamma(t)=\frac{2(a+t)}{\sqrt{t(t+2a)}}.
\]
Conversely this tail makes \(F(z)=z^{-1/2}\), so the first Abel integral is the beta integral \(\int_0^y[z(y-z)]^{-1/2}dz=\pi\); hence \(M(d)=1\) for every \(a<d\le1\).

The tail is strictly decreasing because
\[
\Gamma_a'(t)=-\frac{2a^2}{[t(t+2a)]^{3/2}}<0.
\]
Thus it is realized by the displayed absolutely continuous density together with an endpoint atom of mass \(\Gamma_a(H)=2/\sqrt{1-a^2}\). The measure is sigma-finite because \(\Gamma_a(t)<\infty\) for every \(t>0\). For \(d<a\), no plank in the family contains a point of radius \(d\); for \(d=a\), only a zero-angular-measure parameter set can meet the point, so the multiplicity on the closed hole is \(0\).

Finally, the layer-cake identity and the elementary antiderivative
\[
\frac{d}{dt}\left(2\sqrt{t(t+2a)}\right)=\Gamma_a(t)
\]
give
\[
W_a=\int_0^H\Gamma_a(t)\,dt
=2\sqrt{H(H+2a)}
=2\sqrt{1-a^2}.
\]
For \(a=1/2\) this is \(\sqrt3\). If \(a\) is in the sufficiently small regime of Bakaev--Yehudayoff's finite-plank theorem, the integer optimum is \(2\), while the displayed fractional family has width \(2\sqrt{1-a^2}\). Hence the integer-to-fractional-optimum ratio is at least \(1/\sqrt{1-a^2}\), with expansion \(1+a^2/2+O(a^4)\).

## Verification
The analytic proof is self-contained. The accompanying checker `artifacts/verify_fractional_annulus.py` independently evaluates the derivative of the tail, the layer-cake antiderivative, the transformed Abel integrand on a parameter grid, the exact cost identity, and the \(a=1/2\) specialization. It was replayed from that packaged path and returned a passing result. These finite arithmetic checks support, but do not replace, the Abel inversion proof.

## Relationship to prior work
Bakaev and Yehudayoff exhibit the same outward-tangent fractional ansatz only for the hole radius \(a=1/2\). They write its radial multiplicity as an Abel integral and state that a tail can be chosen to make the multiplicity equal to \(1\), using the construction to explain why fractional relaxations cannot prove their integer theorem. Their paper does not display the tail, its width measure, its total width, a uniqueness statement, or an all-radius formula. The finding above solves that Abel equation explicitly, proves uniqueness inside the stated rotationally invariant lossless ansatz, and extends it to every \(a\in(0,1)\).

The earlier annulus-by-strips paper of Zhang and Ding studies finite strip coverings and does not formulate a fractional or Abel construction. The 2025 plank survey records the annulus problem in its finite-covering form and predates the 2026 lossless fractional construction. The subject is naturally classified as MSC2020 52C15, packing and covering in two dimensions; Zhang and Ding's annulus paper explicitly uses 52C15, and the MSC2020 database retains that description.

## Limitations
The number \(2\sqrt{1-a^2}\) is proved to be the cost of the unique rotationally invariant outward-tangent mixture with exact multiplicity \(1\); it is not asserted to be the unrestricted fractional covering optimum. The measure has infinite total plank mass near zero width although its first width moment is finite. The theorem concerns the open inner boundary \(a<\|x\|\), exactly as in \(D\setminus aD\) for a closed inner disk. No finite discretization with exactly the same pointwise multiplicity is claimed.

## References
1. Egor Bakaev and Amir Yehudayoff, *Area stability of plank covers*, arXiv:2609.30409v1, first public 2026-09-24.
2. Yuqin Zhang and Ren Ding, *A Note about Bezdek's Conjecture on Covering an Annulus by Strips*, Electronic Journal of Combinatorics 15 (2008), #N19, DOI 10.37236/894.
3. William Verreault, *Plank theorems and their applications: A survey*, Bulletin of the London Mathematical Society 58 (2026), e70230, DOI 10.1112/blms.70230; first published 2025-11-09.
4. Mathematics Subject Classification 2020, entry 52C15: packing and covering in two dimensions.
