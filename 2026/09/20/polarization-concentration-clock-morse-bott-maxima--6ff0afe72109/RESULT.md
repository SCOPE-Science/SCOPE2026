# A concentration clock and Morse-Bott selection for cell-polarization localization

## Context

Niethammer, Röger and Velázquez, *Localization properties of a free boundary problem for cell polarization* (arXiv:2609.20609v1), derive a slow-time, zero-membrane-diffusion limit for small-mass localization and characterize subsequential limiting measures. Their Section 4 computes limiting weights for finitely many isolated asymptotically homogeneous maxima, including isolated nondegenerate maxima. This record extracts an explicit temporal concentration law from the same reduced dynamics and extends the geometric selection rule to Morse-Bott maximum sets.

Throughout, `g` is time independent, `g_max=max_Gamma g`, the slow-time reduced solution has unit mass, and
\[
h(x):=\frac{g_{\max}-g(x)}{g_{\max}},\qquad
\alpha_*:=\frac{1-g_{\max}}{g_{\max}},\qquad
\varphi(t):=g_{\max}(\alpha(t)-\alpha_*).
\]
Let
\[
A(t):=\int_0^t\varphi(\tau)\,d\tau,\qquad B(t):=t+A(t),\qquad
\omega(t):=\frac{A(t)}{B(t)},
\]
and
\[
G(s):=\int_\Gamma (s-h)_+\,d\sigma.
\]

## The concentration clock

The source representation formula gives the exact identity
\[
\boxed{u(x,t)=\big[u_0(x)+B(t)(\omega(t)-h(x))\big]_+.}
\]
Assume the limiting maximum set has surface measure zero, as in Theorem 3.6 of the source. Then
\[
\boxed{B(t)G(\omega(t))\to1,\qquad tG(\omega(t))\to1.}
\]
Thus the small-level geometry of `h` supplies an intrinsic clock for the localization dynamics.

### Proof

Write `q=B(omega-h)`. Since `u_0>=0`, pointwise
\[
0\le [u_0+q]_+-q_+\le u_0.
\]
The source proves `alpha(t)\downarrow alpha_*`, so `varphi(t)\to0` and hence `A(t)=o(t)`. At every point with `h(x)>0`,
\[
q(x,t)=A(t)-(t+A(t))h(x)\to-\infty.
\]
On `{h=0}` no pointwise decay is needed because that set has surface measure zero. Dominated convergence and unit mass give
\[
1-B(t)G(\omega(t))
=\int_\Gamma\big([u_0+q]_+-q_+\big)d\sigma\to0.
\]
Since `B(t)/t\to1`, the second limit follows.

## Regular-variation consequence

If for some `C>0`, `p>1`,
\[
G(s)\sim C s^p\qquad(s\downarrow0),
\]
then
\[
\boxed{\omega(t)\sim C^{-1/p}t^{-1/p}.}
\]
Moreover, `A=t\omega/(1-\omega)`, so
\[
A(t)\sim C^{-1/p}t^{1-1/p}.
\]
The source proves that `varphi=A'` has a nonnegative decreasing representative. A monotone-density argument therefore gives
\[
\boxed{\varphi(t)\sim\left(1-\frac1p\right)C^{-1/p}t^{-1/p},}
\]
and hence
\[
\boxed{\alpha(t)-\alpha_*\sim
\frac{1-1/p}{g_{\max}}C^{-1/p}t^{-1/p}.}
\]

The exact representation also gives
\[
\{h<\omega(t)\}\subset\{u(\cdot,t)>0\}
\subset\left\{h<\omega(t)+\frac{\|u_0\|_\infty}{B(t)}\right\}.
\]
Since `B(t)^{-1}=o(\omega(t))` when `p>1`, support thickness is controlled asymptotically by the level set `h\lesssim\omega(t)`.

For the isolated asymptotically homogeneous maxima treated in Section 4 of the source, if the dominant homogeneity degree is `m_*` and `G(s)\sim Cs^{1+2/m_*}`, then
\[
\omega(t)\sim C^{-m_*/(m_*+2)}t^{-m_*/(m_*+2)},
\]
\[
\alpha(t)-\alpha_*\sim
\frac{2}{(m_*+2)g_{\max}}C^{-m_*/(m_*+2)}t^{-m_*/(m_*+2)}.
\]
For `h\asymp |x|^{m_*}`, support radius is of order `t^{-1/(m_*+2)}` and cap height `B(t)\omega(t)=A(t)` is of order `t^{2/(m_*+2)}`. In particular, isolated nondegenerate maxima have threshold rate `t^{-1/2}` and support radius `t^{-1/4}`.

## Morse-Bott maximum sets

Assume `Gamma` is a smooth two-dimensional membrane and `M={h=0}` is a finite disjoint union of compact embedded Morse-Bott components. For a component `M_j` of dimension `d_j in {0,1}`, put `q_j=2-d_j` and let `H_j^perp` be the positive normal Hessian of `h`.

Tubular coordinates give
\[
\int_{\operatorname{tube}(M_j)}(s-h)_+d\sigma
\sim K_{q_j}s^{1+q_j/2}
\int_{M_j}\frac{d\operatorname{vol}_{M_j}}{\sqrt{\det H_j^\perp}},
\]
where
\[
K_q=\frac{2^{1+q/2}\operatorname{Vol}(B_q)}{q+2},\qquad
K_1=\frac{4\sqrt2}{3},\quad K_2=\pi.
\]
Thus the highest-dimensional maximum components dominate. If any maximum curve is present, isolated maxima are lower order.

For maximum curves,
\[
C_{\rm curve}=\frac{4\sqrt2}{3}\int_M\kappa^{-1/2}\,d\ell,
\]
where `kappa` is the scalar normal Hessian. Then
\[
\boxed{\omega(t)\sim(C_{\rm curve}t)^{-2/3},}
\]
\[
\boxed{\alpha(t)-\alpha_*\sim
\frac{1}{3g_{\max}}C_{\rm curve}^{-2/3}t^{-2/3},}
\]
and normal support thickness is of order `t^{-1/3}`.

For isolated nondegenerate maxima,
\[
C_{\rm point}=\pi\sum_j(\det H_j)^{-1/2},
\]
so
\[
\omega(t)\sim(C_{\rm point}t)^{-1/2},\qquad
\alpha(t)-\alpha_*\sim\frac{C_{\rm point}^{-1/2}}{2g_{\max}}t^{-1/2},
\]
with support radius of order `t^{-1/4}`. The coefficient `pi/sqrt(det H_j)` agrees with the source's isolated-maxima coefficient; the new content is the temporal clock and its consequences for relaxation and support scales.

## Limit-measure selection for Morse-Bott maxima

Let
\[
\nu_s:=\frac{(s-h)_+\,d\sigma}{G(s)}.
\]
The same tubular calculation shows that `nu_s` converges weakly to a probability measure carried by maximum components of smallest normal codimension, with density
\[
\boxed{d\nu\propto (\det H^\perp)^{-1/2}d\operatorname{vol}_M.}
\]
Hence, if maximum curves are present, limiting mass is distributed along them with density proportional to `kappa^{-1/2}`, while isolated maxima receive zero limiting mass.

Theorems 3.6 and 3.12 of arXiv:2609.20609v1 characterize subsequential limit measures by normalized positive-part caps. Since `nu_s` has a unique Morse-Bott limit, every subsequential limit is the same measure. Thus the weak limit is unique, for both the infinite-cytosolic-diffusion and finite-diffusion slow-time limit problems, under the stated Morse-Bott geometry. The explicit temporal clock is proved only for the spatially uniform multiplier in the infinite-diffusion reduced problem.

## Verification example

On the unit sphere take
\[
h(x,y,z)=\frac{z^2}{2}.
\]
The maximum set is the equator, its normal Hessian is one, and its length is `2pi`. Direct integration gives exactly, for small `s`,
\[
G(s)=\frac{8\pi\sqrt2}{3}s^{3/2}.
\]
Thus
\[
C_{\rm curve}=\frac{8\pi\sqrt2}{3},\qquad
\omega(t)t^{2/3}\to C_{\rm curve}^{-2/3}=0.192417365779563\ldots.
\]
For constant unit-mass initial density, the verifier solves the exact mass constraint. At `t=10^6` it gives
\[
\omega(t)t^{2/3}=0.191619148248,\qquad tG(\omega(t))=0.993783909805,
\]
and a finite-difference multiplier estimate gives
\[
\varphi(t)t^{2/3}=0.064138714065,
\]
against the predicted value `C_curve^{-2/3}/3=0.064139121927...`.

## Originality boundary

General Morse-Bott quadratic-normal asymptotics are established prior art and are not claimed as new. Ievlev, arXiv:2608.02626, explicitly treats Morse-Bott and stratified minimum-set asymptotics, building on classical Laplace/tubular methods. The new claim is source-specific: the exact concentration-clock identity for this slow-time cell-polarization dynamics, the resulting temporal rates, and the combination of the source's cap-measure characterization with Morse-Bott maximum geometry to obtain continuous-manifold selection and uniqueness of the limiting measure.

Earlier cell-polarization papers arXiv:2006.16155, arXiv:2202.06289 and arXiv:2402.03034 focus respectively on derivation/stability and free-boundary qualitative behavior; arXiv:2605.03553 studies small-mass shapes of stationary positivity regions. The present source arXiv:2609.20609v1 treats long-time localization on the slow scale, but its Section 4 examples assume finitely many isolated maxima and do not state a temporal localization rate.

## Limitations

The concentration-clock and multiplier-rate statements apply to the infinite-cytosolic-diffusion slow-time reduced system with time-independent signal and the source's measure-zero limiting-support hypothesis. They do not establish the same temporal power laws for the finite-diffusion reduced system, whose multiplier is spatially dependent. Morse-Bott formulas assume clean quadratic normal behavior and compact smooth maximum components; singular, intersecting, boundary, or flatter maximum sets may have different powers. The result concerns the reduced small-mass dynamics, not a quantitative convergence rate for the original unscaled bulk-surface PDE at fixed positive mass.

## References

- B. Niethammer, M. Röger, J.J.L. Velázquez, *Localization properties of a free boundary problem for cell polarization*, arXiv:2609.20609v1 (2026), https://arxiv.org/abs/2609.20609v1
- P. Ievlev, *Laplace Asymptotics near Stratified Minimum Sets*, arXiv:2608.02626v1 (2026), https://arxiv.org/abs/2608.02626v1
- A. Logioti, B. Niethammer, M. Röger, J.J.L. Velázquez, *A parabolic free boundary problem arising in a model of cell polarization*, arXiv:2006.16155 (2020), https://arxiv.org/abs/2006.16155
- A. Logioti, B. Niethammer, M. Röger, J.J.L. Velázquez, *Qualitative properties of solutions to a mass-conserving free boundary problem modeling cell polarization*, arXiv:2202.06289 (2022), https://arxiv.org/abs/2202.06289
- A. Logioti, B. Niethammer, M. Röger, J.J.L. Velázquez, *Interface behavior for the solutions of a mass conserving free boundary problem modelling cell polarization*, arXiv:2402.03034v1 (2024), https://arxiv.org/abs/2402.03034v1
- S. Flores Sepúlveda, B. Niethammer, J.J.L. Velázquez, *On the shape of the positivity region for a free boundary problem describing cell polarization*, arXiv:2605.03553v1 (2026), https://arxiv.org/abs/2605.03553v1
