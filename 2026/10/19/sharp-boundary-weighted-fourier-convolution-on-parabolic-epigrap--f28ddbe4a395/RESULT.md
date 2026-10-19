# Sharp boundary-weighted Fourier convolution on parabolic epigraphs

## Finding

For every integer \(d\ge 1\), put
\[
\Omega_d=\{(u,t)\in\mathbb R^d\times\mathbb R:t>|u|^2\},
\quad 2\Omega_d=\{2x:x\in\Omega_d\},
\quad \omega_{2\Omega_d}(z)=\big|(2\Omega_d)\cap(2z-2\Omega_d)\big|.
\]
Here vertical bars on sets denote \((d+1)\)-dimensional Lebesgue volume. For any nonzero \(F,G\in L^2(\Omega_d)\), extend both by zero outside \(\Omega_d\). Then the following boundary-weighted Fourier-side convolution inequality is sharp:
\[
\boxed{\int_{2\Omega_d}\frac{|(F*G)(z)|}{\omega_{2\Omega_d}(z)}\,dz
\le \frac{\pi(d+2)}4\,\|F\|_2\|G\|_2.}
\]
The best constant is exactly \(\pi(d+2)/4\) for each \(d\), and no nonzero pair attains equality. The integral is well defined and finite for every such pair.

Equivalently, the integral Hankel operator on \(L^2(\Omega_d)\),
\[
(H_dF)(x)=\int_{\Omega_d}\frac{F(y)}{\omega_{2\Omega_d}(x+y)}\,dy,
\]
initially defined for nonnegative compactly supported inputs and extended by boundedness, has
\[
\boxed{\|H_d\|=\|H_d\|_{\mathrm{ess}}=\frac{\pi(d+2)}4.}
\]
It has no nonzero norm-attaining vectors; the error of every finite-rank operator approximation is at least \(\pi(d+2)/4\), with equality attained by the zero approximant. The essential norm is the distance to compact operators in the operator norm.

## Assumptions and scope

There is no regularity, sign, symmetry, or compact-support assumption on \(F,G\) beyond membership in \(L^2(\Omega_d)\). Convolution is with unnormalized Euclidean Lebesgue measure: \((F*G)(z)=\int F(x)G(z-x)\,dx\). No factor of \(2\pi\) is implicit. All functions may be complex valued. The epigraph is open, convex, and unbounded. The weight is evaluated at \(z\in 2\Omega_d\), where it is finite and strictly positive. Its measure vanishes at the boundary, which is excluded from the integration region.

## Proof

**1. Exact overlap geometry.** Write \(V_d=\pi^{d/2}/\Gamma(1+d/2)\), the volume of the \(d\)-dimensional Euclidean unit ball. Since \(2\Omega_d=\{(w,s):s>|w|^2/2\}\), set \(H=s-|w|^2/2>0\) for an arbitrary center \(z=(w,s)\in 2\Omega_d\). The pair \(z\pm(a,b)\) lies in \(2\Omega_d\) precisely when
\[
|b-w\cdot a|<H-|a|^2/2,
\qquad |a|^2<2H.
\]
The Jacobian from displacements to points is one. Integrating the permitted vertical interval gives the exact Macbeath overlap volume
\[
\begin{aligned}
\omega_{2\Omega_d}(w,s)
&=2\int_{|a|<\sqrt{2H}}(H-|a|^2/2)\,da\\
&=\frac{2^{d/2+2}V_d}{d+2}\,H^{(d+2)/2}.
\end{aligned}
\tag{1}
\]

**2. Reduction to a one-dimensional Carleman majorant.** The change of variables \((u,h)\mapsto(u,|u|^2+h)\), with \(h>0\), preserves Lebesgue measure. In these coordinates, for inputs \((u,h),(v,k)\in\Omega_d\),
\[
H(x+y)=h+k+\tfrac12|u-v|^2.
\]
Consequently \(H_d\) has the positive translation-invariant horizontal kernel
\[
K_{h+k}(u-v)=\frac{d+2}{2^{d/2+2}V_d}
\left(h+k+\tfrac12|u-v|^2\right)^{-(d+2)/2}.
\]
By a radial beta integral, for every \(A>0\),
\[
\int_{\mathbb R^d}\left(A+|u|^2/2\right)^{-(d+2)/2}\,du
=\frac{2^{d/2}V_d}{A},
\qquad \|K_A\|_{L^1(\mathbb R^d)}=\frac{d+2}{4A}.
\tag{2}
\]
For an input \(F\) and \(g(k)=\|F(\cdot,k)\|_{L^2(\mathbb R^d)}\), Minkowski's integral inequality and Young's convolution inequality give, for almost every \(h>0\),
\[
\|(H_d F)(\cdot,h)\|_{L^2_u}
\le \frac{d+2}{4}\int_0^\infty\frac{g(k)}{h+k}\,dk.
\]
Thus
\[
\|H_dF\|_2\le\frac{d+2}{4}\,\|Cg\|_{L^2(0,\infty)},
\quad (Cg)(h)=\int_0^\infty\frac{g(k)}{h+k}\,dk.
\tag{3}
\]

**3. Sharp Carleman bound and strict nonattainment.** The unitary logarithmic change \((Ug)(s)=e^{s/2}g(e^s)\) maps \(C\) to convolution by
\[
j(s)=\frac1{2\cosh(s/2)}.
\]
Its Fourier transform, in the convention \(\widehat j(\xi)=\int e^{-i\xi s}j(s)\,ds\), is \(\pi/\cosh(\pi\xi)\). Plancherel therefore yields \(\|C\|=\pi\). Since the multiplier has modulus strictly below \(\pi\) except at the single frequency \(\xi=0\), the inequality \(\|Cg\|_2<\pi\|g\|_2\) holds for every nonzero \(g\in L^2(0,\infty)\). Equation (3) proves \(\|H_d\|\le\pi(d+2)/4\), with strict inequality on every nonzero vector.

**4. Sharpness, not merely an upper bound.** Define the unit-norm logarithmic plateau
\[
g_L(h)=(2L)^{-1/2}h^{-1/2}\mathbf 1_{(e^{-L},e^L)}(h),\qquad L>0.
\]
Its Carleman Rayleigh quotient is
\[
\langle Cg_L,g_L\rangle
=\int_{-2L}^{2L}\left(1-\frac{|s|}{2L}\right)
\frac{ds}{2\cosh(s/2)}\longrightarrow\pi.
\tag{4}
\]
Choose a nonnegative \(\phi\in C_c^\infty(\mathbb R^d)\) of \(L^2\)-norm one, put \(\phi_R(u)=R^{-d/2}\phi(u/R)\), and define \(F_{R,L}(u,h)=\phi_R(u)g_L(h)\). For every fixed \(A>0\),
\[
\lim_{R\to\infty}\langle K_A*\phi_R,\phi_R\rangle
=\|K_A\|_1=\frac{d+2}{4A},
\]
by strong continuity of translations on \(L^2(\mathbb R^d)\) and dominated convergence. Inserting this into the double integral over \(h,k\), again using the integrable majorant from (2), gives
\[
\lim_{R\to\infty}\langle H_dF_{R,L},F_{R,L}\rangle
=\frac{d+2}{4}\langle Cg_L,g_L\rangle.
\]
Taking \(L\to\infty\) and using (4) proves the matching lower bound. Because \(F_{R,L}\ge0\), the same sequence proves sharpness of the absolute convolution integral through Tonelli and \(\int_{2\Omega_d}(F*F)/\omega=\langle H_dF,F\rangle\).

**5. Convolution inequality and equality exclusion.** Positivity and Tonelli imply
\[
\int_{2\Omega_d}\frac{|F*G|}{\omega_{2\Omega_d}}
\le \int_{\Omega_d}\int_{\Omega_d}
\frac{|F(x)||G(y)|}{\omega_{2\Omega_d}(x+y)}\,dx\,dy
\le\|H_d|F|\|_2\|G\|_2.
\]
The last term is strictly smaller than \(\pi(d+2)\|F\|_2\|G\|_2/4\) when both inputs are nonzero, by step 3; hence there are no nontrivial equality cases.

**6. Essential norm and finite-rank approximation.** Horizontal translations \((T_aF)(u,h)=F(u-a,h)\) commute with \(H_d\). For a fixed \(F\in L^2(\Omega_d)\), \(T_aF\rightharpoonup0\) as \(|a|\to\infty\). A compact operator \(K\) therefore satisfies \(\|KT_aF\|_2\to0\). It follows that
\[
\|H_d-K\|\ge\limsup_{|a|\to\infty}
\frac{\|(H_d-K)T_aF\|_2}{\|F\|_2}
=\frac{\|H_dF\|_2}{\|F\|_2}.
\]
Taking the supremum over nonzero \(F\) and then the infimum over compact \(K\) gives \(\|H_d\|_{\mathrm{ess}}=\|H_d\|\). Finite-rank operators are compact, so every finite-rank approximation has at least this error; the zero operator achieves equality.

## Verification

The attached standard-library checker `check.py` independently integrates the horizontal beta kernels and the exact vertical overlap sections in dimensions \(1\) through \(5\) at several gap values. It also checks the logarithmic Carleman-kernel integral and increasing Rayleigh quotients for several finite plateaus. These are consistency checks of coefficients and endpoint normalization; they neither prove a dimension-uniform identity nor verify the infinite-dimensional norm, nonattainment, or essential-norm argument, which follow from the analytic proof above.

## Relationship to prior work

Bampouras and Perfekt (2026, arXiv:2608.19806) introduce and analyze boundary-weighted Fourier inequalities for convex domains, including the Macbeath overlap weight and associated Hilbert-type kernels. Earlier Bampouras–Perfekt work (arXiv:2409.04184) treats higher-dimensional Paley–Wiener Hankel and Schatten theory; the related Paley–Wiener Nehari paper (arXiv:2504.05986) treats Hardy-type estimates. The Carleman norm \(\pi\) and its Mellin/Fourier diagonalization are classical and are used here, not claimed as new. The new assertion is the exact all-dimensional parabolic-epigraph weight calculation together with sharp convolution constant, nonattainment, and essential-norm classification. No direct implication from the inspected general-domain results yielded this epigraph constant; priority against unindexed domain-specific calculations is not certified.

## Limitations

The domain is the explicit isotropic quadratic epigraph; the theorem does not determine sharp constants for arbitrary convex, bounded, or anisotropic domains, nor does it provide norm-attaining Fourier data. The sharpness construction requires a two-parameter limiting sequence and is not an exact finite-energy maximizer. Finite numerical integration provides consistency only. Literature comparison is bounded by the accessible sources and database indexing; no independent audit or historical-priority certification has been performed.

## References

1. Bampouras and Perfekt, *Boundary-Weighted Fourier Inequalities for Convex Domains* (first public August 20, 2026), arXiv:2608.19806, https://arxiv.org/abs/2608.19806.
2. Bampouras and Perfekt, *Besov spaces and Schatten class Hankel operators for Hardy and Paley–Wiener spaces in higher dimensions*, arXiv:2409.04184, https://arxiv.org/abs/2409.04184.
3. Bampouras, *Nehari's Theorem and Hardy's inequality for Paley-Wiener spaces*, arXiv:2504.05986, https://arxiv.org/abs/2504.05986.
4. Classical Carleman integral operator: Mellin diagonalization of the kernel \(1/(s+t)\), with multiplier \(\pi/\cosh(\pi\xi)\).
