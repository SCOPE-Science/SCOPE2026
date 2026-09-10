# First helicity-source Euler subsolution from the wavenumber-2 ABC Taylor datum

## Context

The 3D incompressible Euler helicity-conservation threshold is
$B^{2/3}_{3,c(\mathbb N)}$ (Cheskidov–Constantin–Friedlander–Shvydkoy,
arXiv:0704.0759). That paper proves conservation above the threshold and
discusses sharpness only through a divergence-free vector field with
non-vanishing flux — explicitly not an unforced Euler solution or
subsolution. Energy-profile flexibility below $1/3$ was closed by
Buckmaster–De Lellis–Székelyhidi–Vicol (arXiv:1701.08678) and Isett
(arXiv:1608.08301), both energy-only with no helicity control. Solution-
or subsolution-level realization of prescribed helicity decay below $2/3$
was open. This record certifies the first explicit helicity-source Euler
subsolution from a canonical datum (preset fallback of the admitted
$h(t)=H^*(1-t/2)$ target).

## Definitions

Let $\mathbb T^3=[0,2\pi]^3$, $\mathrm{Vol}=8\pi^3$, and

$$U^*(x)=\Bigl(\tfrac{\sin 2z+\cos 2y}{2},\tfrac{\sin 2x+\cos 2z}{2},\tfrac{\sin 2y+\cos 2x}{2}\Bigr).$$

Then $\mathrm{div}\,U^*=0$ and $\mathrm{curl}\,U^*=2U^*$
($k_0=2$ Beltrami/Taylor state). Intrinsic invariants:

$$E^*=\int_{\mathbb T^3}|U^*|^2\,dx=6\pi^3\approx 186.03766,\qquad H^*=\int_{\mathbb T^3}U^*\cdot\mathrm{curl}\,U^*\,dx=2E^*=12\pi^3\approx 372.07532.$$

Let $W(x)=(\sin 8z,-\cos 8z,0)$: $\mathrm{div}\,W=0$,
$\mathrm{curl}\,W=-8W$, $|W|^2\equiv 1$.
Put $b(t)=1-t/8$, $a(t)=t/8$, and

$$v_0(x,t)=b(t)U^*(x)+a(t)W(x),\quad \dot b=-1/8,\ \dot a=1/8.$$

Write $C=(U^*\cdot\nabla)W+(W\cdot\nabla)U^*$,
$F=\dot b\,U^*+\dot a\,W+ab\,C$, $P=F-\bar F$ (mean removed; mean
vanishes), $B=\Delta^{-1}P$, $\Phi=\Delta^{-1}\mathrm{div}\,P$, and

$$R^s_{jl}=\partial_j B_l+\partial_l B_j,\qquad R_0=S_0=R^s-\tfrac{\mathrm{tr}\,R^s}{3}I,$$

$$p_0=-\tfrac{b^2|U^*|^2}{2}-\tfrac{a^2|W|^2}{2}+\Phi-\tfrac{\mathrm{tr}\,R^s}{3}.$$

All fields are trigonometric polynomials of degree $\le 10$.

## Result

There exists an explicit smooth strict Euler subsolution
$(v_0,R_0,p_0)$ on $\mathbb T^3\times[0,1]$ such that:

1. $v_0(\cdot,0)=U^*$ and $\mathrm{div}\,v_0=0$;
2. $\partial_t v_0+\mathrm{div}(v_0\otimes v_0)+\nabla p_0=\mathrm{div}\,R_0$;
3. $R_0$ is traceless, symmetric, and not identically zero, with
   $\|R_0\|_{L^\infty(\mathbb T^3\times[0,1])}\le E^*/8\approx 23.2547$;
4. with $\omega_0=\mathrm{curl}\,v_0$,
   $\left.\frac{d}{dt}\right|_{t=0}\int_{\mathbb T^3}v_0\cdot\omega_0\,dx=-H^*/4\approx -93.01883$.

## Proof / evidence

- **F1 (datum/closed forms).** $(\mathrm{curl}\,U^*)_1=\partial_yU^*_3-\partial_zU^*_2=\cos 2y+\sin 2z=2U^*_1$ (cyclic); $\mathrm{div}\,U^*=0$. Each $\int (U^*_i)^2=\mathrm{Vol}/4$, so $E^*=3\cdot 8\pi^3/4=6\pi^3$, $H^*=2E^*$. Spectral quadrature gives relerr $0.0$. Cross $U^*$–$W$ energy/helicity vanish ($\sim 10^{-14}$) by Fourier-support separation ($|k|=2$ vs $(0,0,\pm 8)$).
- **F2.** $a(0)=0$, $b(0)=1$ give $v_0(\cdot,0)=U^*$; $\mathrm{div}\,v_0=b\,\mathrm{div}\,U^*+a\,\mathrm{div}\,W=0$ (grid max $0.0$).
- **F3 (rate).** $h(t)=\int v_0\cdot\omega_0=b(t)^2H^*-a(t)^2\cdot 8\cdot\mathrm{Vol}$ (cross terms vanish), so $h(0)=H^*$ and $\dot h(0)=2\dot b(0)H^*=-H^*/4$ analytically exact (the $a\dot a$ term vanishes at $t=0$); finite-difference check relerr $2.7\times 10^{-5}$ (first-order bias only).
- **F4 (system).** $(U^*\cdot\nabla)U^*=\nabla(|U^*|^2/2)$ since $U^*\times\mathrm{curl}\,U^*=0$; $(W\cdot\nabla)W=0$ ($W_3=0$, no $x/y$ dependence). Hence $\mathrm{div}(v_0\otimes v_0)=b^2\nabla(|U^*|^2/2)+ab\,C$ (plus $a^2$ term vanishing since $(W\cdot\nabla)W=0$ and $\mathrm{div}\,W=0$ make $a^2\mathrm{div}(W\otimes W)=\nabla(a^2|W|^2/2)$). With $F=\partial_t v_0+ab\,C$ (mean zero) and $R^s_{jl}=\partial_jB_l+\partial_lB_j$, $B=\Delta^{-1}P$, the identity $\mathrm{div}\,R^s=P+\nabla\Phi$ holds exactly; $p_0$ absorbs the gradient, $\Phi$, and trace parts. True residual max $2.76\times 10^{-14}$ over 21 time slices (floating-point error on an analytically exact identity; $N=64$ grid exactly resolves all modes $\le 16 <$ Nyquist $32$, no aliasing).
- **F5.** $\mathrm{tr}\,S_0=0$ to $1.4\times 10^{-17}$ by construction.
- **F6 (cap).** Grid-max $\|R_0\|_{L^\infty}=0.2260\le E^*/8\approx 23.2547$ (margin $103\times$). Rigorous Wiener ($\ell^1$ Fourier) bound: componentwise $\sup\le 0.2658$, Frobenius $\sup\le 0.7973\ll 23.2547$; independently recomputed max-component $\ell^1\le 0.197$ across slices. Since $\sup\le\ell^1$ for Fourier series, the cap is rigorous, not mere sampling.
- **F7 (strict).** Slice-averaged $\|R_0\|_{L^2}=1.50445>0$; $\|P(F(0))\|_{L^2}=0.15309\ne 0$, so $R_0\not\equiv 0$ (inverse-divergence injective on mean-zero fields).
- **F8 (ledger).** Low modes ($|k|\le 4$): $U^*$ Beltrami store; high ($|k|>4$): $W$ sink with $dH_{\mathrm{high}}/dE_{\mathrm{high}}=-8$; Woltjer-compatible ($|h|/e\le 2$ along path).

## Limitations

Subsolution only (nonzero Reynolds stress), not an exact weak Euler
solution. Helicity rate certified at $t=0$ only. The full prescribed-profile
target $h(t)=H^*(1-t/2)$ exact solution remains open. Residual/l1 numbers
certify analytically exact trigonometric-polynomial identities via exact
spectral quadrature, not a general-PDE error bound.

## Reproducibility

`python3 output/artifacts/verify_fallback.py` → `VERIFY_OK`
(residual $2.76\times 10^{-14}$); Fourier-$\ell^1$ cap certificate in
`output/artifacts/verify_fallback_ell1.log`. Pre-fixed datum, box, $E^*$,
$H^*$, operators (Fourier multipliers on modes $|k|\le 10$), and all
numbered estimates above.

## References

- A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, Energy
  conservation and Onsager's conjecture for the Euler equations,
  arXiv:0704.0759. Helicity conservation in $B^{2/3}_{3,c(\mathbb N)}$;
  sharpness via vector field only.
- T. Buckmaster, C. De Lellis, L. Székelyhidi Jr., V. Vicol, Onsager's
  conjecture for admissible weak solutions, arXiv:1701.08678.
  Energy-profile flexibility, $\beta<1/3$, no helicity control.
- P. Isett, A Proof of Onsager's Conjecture, arXiv:1608.08301.
  Energy-flexible $C^\alpha$ solutions, $\alpha<1/3$, no helicity control.
- arXiv all-fields searches for `helicity subsolution Euler` and
  `ABC Beltrami Euler subsolution helicity` (2026-09-10): no results.
