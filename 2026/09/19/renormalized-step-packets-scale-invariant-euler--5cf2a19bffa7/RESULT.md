# Renormalized top-hat asymptotics for finite step packets in scale-invariant 2D Euler

## Statement

Consider the reduced scale-invariant, odd, \(m\)-fold symmetric Euler system on
\(I_m=[0,\pi/m]\), with \(m\ge 4\),
\[
\partial_t g+2G\partial_\theta g=0,\qquad G_{\theta\theta}+4G=g,
\qquad G(t,0)=G(t,\pi/m)=0.
\]
For finite positive step data
\[
g_0(\theta)=\sum_{k=1}^n c_k\mathbf 1_{(a_k,b_k]}(\theta),
\quad
0<a_1<b_1<\cdots<a_n<b_n<\pi/m,
\quad c_k>0,
\]
write the transported endpoints as \(a_k(t),b_k(t)\), and let \(c_*=c_n\) be the height of the outermost step.

The source paper proves that \(b_n(t)\asymp(1+t)^{-1}\) and that every endpoint other than \(b_n\) is integrable in time. These estimates imply the following sharper asymptotic law:
\[
\boxed{\lim_{t\to\infty} c_*t\,b_n(t)=1.}
\]
Moreover, with the renormalized profile
\[
h_t(y):=g\!\left(t,\frac{y}{c_*t}\right),\qquad y\ge0,
\]
extended by zero outside the rescaled sector, one has
\[
\boxed{h_t\longrightarrow c_*\mathbf 1_{(0,1]}\quad\text{in }L^1(0,\infty).}
\]
Thus every finite positive step packet has the same asymptotic top-hat shape after the natural \(t\)-rescaling; only the height of the outermost plateau sets the spatial scale.

Consequently, for every fixed \(p\ge0\),
\[
\boxed{
 t^{p+1}\int_0^{\pi/m}\theta^p g(t,\theta)\,d\theta
 \longrightarrow \frac{1}{(p+1)c_*^p}.
}
\]
In particular,
\[
\boxed{t\|g(t)\|_{L^1(I_m)}\to1,}
\qquad
\boxed{t^2\int_0^{\pi/m}\sin(2\theta)g(t,\theta)\,d\theta\to\frac1{c_*}.}
\]
The leading mass coefficient is therefore universal: it is independent of \(m\), the number of steps, their locations, and all their amplitudes.

For a single step \(g=c\mathbf1_{(a(t),b(t)]}\), the source paper obtains only \(b(t)\asymp t^{-1}\) and \(a(t)/b(t)\lesssim t^{-\gamma}\) for some unspecified \(\gamma>0\). In fact there is a finite constant \(\Lambda\in(0,\infty)\), depending on the initial interval, such that
\[
\boxed{\frac{a(t)}{b(t)^2}\to\Lambda,}
\qquad
\boxed{t^2a(t)\to\frac{\Lambda}{c^2}.}
\]
If \(\kappa_m=\cot(2\pi/m)\), then the outer endpoint has the sharper expansion
\[
\boxed{
\frac1{b(t)}=ct-2\kappa_m\log t+B+o(1)
}
\]
for some finite constant \(B\). For \(m=4\), \(\kappa_m=0\), so the logarithmic correction disappears exactly.

## Proof of the finite-step top-hat law

The source paper's Proposition 2.4 shows that the step topology is preserved, \(b_n(t)\asymp(1+t)^{-1}\), and every endpoint \(x(t)\ne b_n(t)\) satisfies
\[
\int_0^\infty x(t)\,dt<\infty.
\]
All endpoints are nonincreasing because the Green kernel is negative and hence \(G\le0\). A nonnegative nonincreasing integrable function obeys \(t x(t)\to0\): indeed,
\[
\frac t2 x(t)\le \int_{t/2}^t x(s)\,ds\to0.
\]
Therefore
\[
t a_k(t)\to0,\qquad t b_k(t)\to0\ (k<n),\qquad t a_n(t)\to0.
\]
Since \(t b_n(t)\) stays bounded above and below, all those endpoints are \(o(b_n(t))\).

Let \(s_m=\sin(2\pi/m)\). The exact endpoint equation from the source is
\[
b_n'=
\frac{\sin(2(\pi/m-b_n))}{2s_m}
\sum_{k=1}^n c_k\bigl(\cos(2b_k)-\cos(2a_k)\bigr).
\]
For \(k<n\), the corresponding summands are \(o(b_n^2)\). For \(k=n\), since \(a_n/b_n\to0\),
\[
\cos(2b_n)-\cos(2a_n)=-2b_n^2+o(b_n^2).
\]
Also \(\sin(2(\pi/m-b_n))\to s_m\). Hence
\[
 b_n'=-c_*b_n^2+o(b_n^2),
\qquad
 \left(\frac1{b_n}\right)'=c_*+o(1).
\]
Integrating and dividing by \(t\) gives \(c_*tb_n\to1\).

Under the rescaling \(y=c_*t\theta\), all endpoints except the rightmost one converge to \(0\), while
\[
c_*t b_n(t)\to1.
\]
The rescaled support therefore consists of an outer interval converging to \((0,1]\), with height \(c_*\), plus finitely many inner intervals whose total rescaled length tends to zero. This proves
\[
h_t\to c_*\mathbf1_{(0,1]}
\]
in \(L^1(0,\infty)\).

The moment formula follows by change of variables:
\[
(c_*t)^{p+1}\int\theta^p g(t,\theta)\,d\theta
=\int y^p h_t(y)\,dy
\to c_*\int_0^1 y^p\,dy=\frac{c_*}{p+1}.
\]
The sine moment uses \(\sin(2\theta)=2\theta+O(\theta^3)\) and \(\sup\operatorname{supp}g=O(t^{-1})\).

## Single-step refinement

For one interval the exact endpoint system is
\[
 a'=-\frac{c}{2s_m}\sin(2a)
 \bigl[\cos(2(\pi/m-b))-\cos(2(\pi/m-a))\bigr],
\]
\[
 b'=\frac{c}{2s_m}\sin(2(\pi/m-b))
 \bigl[\cos(2b)-\cos(2a)\bigr].
\]
The source already proves \(b\asymp t^{-1}\) and \(a=O(t^{-1-\gamma})\), so \(a\in L^1\) and \(b^2\in L^1\).

Set
\[
R(t)=\frac{\tan a(t)}{\tan^2 b(t)}.
\]
Direct differentiation gives
\[
\frac{R'}R=
\frac{2c\sin(b-a)}{\sin(2b)}
\left[
-\sin(b-a)+
\frac{\sin(2(\pi/m-b))}{s_m}\sin(a+b)
\right].
\]
The bracket is \(O(a+b^2)\) as \((a,b)\to(0,0)\), while the prefactor is bounded. Hence
\[
\left|\frac{R'}R\right|\le C(a+b^2)
\]
for all sufficiently large times. The right-hand side is integrable, so \(\log R(t)\) converges and \(R(t)\to\Lambda\in(0,\infty)\). Since \(\tan x\sim x\), this yields \(a/b^2\to\Lambda\). Together with \(tb\to1/c\), it gives \(t^2a\to\Lambda/c^2\).

Substituting \(a=\Lambda b^2+o(b^2)\) into the exact \(b\)-equation gives
\[
\left(\frac1b\right)'
=c-2c\cot(2\pi/m)b+O(b^2).
\]
Writing \(u=1/b\) and using \(u\sim ct\), first gives \(u=ct+O(\log t)\). Then
\[
\frac{d}{dt}\left(u-ct+2\cot(2\pi/m)\log t\right)
=O\!\left(\frac{\log t}{t^2}\right),
\]
which is integrable. The claimed finite constant \(B\) follows.

## Interpretation

The source paper uses finite step packets as building blocks for a dense-orbit construction and needs only coarse decay estimates. The sharpened picture is more rigid: every finite packet has a universal renormalized top-hat attractor, its sector mass satisfies the exact clock \(\|g(t)\|_1\sim t^{-1}\), and in the one-step problem the fast endpoint is not merely polynomially separated from the slow one but satisfies \(a\sim\Lambda b^2\). The first geometry-dependent correction to the slow edge is logarithmic and is controlled solely by \(\cot(2\pi/m)\).

## Limitations

The top-hat theorem is for finite positive step data in the \(m\ge4\) sector considered by the source paper. It does not assert a renormalized attractor for arbitrary \(L^\infty\) data, for the dense-orbit data constructed from infinitely many steps, or for sign-changing sector data. The logarithmic denominator correction and \(a/b^2\) limit are proved here only for a single interval; interactions among multiple inner endpoints can affect subleading corrections for general finite step packets.

## References

1. I. Suleiman, *Dense orbits for scale-invariant rotationally symmetric solutions of the 2D Euler equations*, arXiv:2609.20674v1 (2026). https://arxiv.org/abs/2609.20674
2. T. M. Elgindi, R. W. Murray, A. R. Said, *On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications*, Ann. Sci. Éc. Norm. Supér. 58 (2025), 943–970. https://doi.org/10.24033/asens.2621
3. T. M. Elgindi, I. Jeong, *Symmetries and critical phenomena in fluids*, Comm. Pure Appl. Math. 73 (2020), 257–316.
4. D. Cao, J. Fan, G. Qin, *Gradient growth and relaxation to jump profiles for 3-fold symmetric scale-invariant Euler flows*, arXiv:2608.16755 (2026).

## Reproducibility

`artifacts/verify_step_packet_asymptotics.py` checks the exact differentiated ratio, the one-step asymptotic expansion, and a representative numerical trajectory. `artifacts/verification_output.txt` records the resulting dimensionless clocks. These checks support the algebra and asymptotics but are not independent validation.
