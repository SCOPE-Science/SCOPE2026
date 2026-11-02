# Sharp critical Gabor bounds and a universal conditioning barrier for positive Cauchy mixtures

## Finding
Let \(\nu\) be a nonzero finite positive Borel measure with compact support contained in \((0,\infty)\). Set
\[
 g_\nu(t)=\int_{(0,\infty)}\frac{d\nu(w)}{t-iw},\qquad t\in\mathbb R.
\]
For every \(\alpha>0\), the critical-density Gabor system
\[
 \mathcal G_\alpha(g_\nu)=\left\{e^{2\pi i nt/\alpha}g_\nu(t-\alpha m):m,n\in\mathbb Z\right\}
\]
is a frame for \(L^2(\mathbb R)\), with **optimal** lower and upper squared frame bounds
\[
 \boxed{A_{\alpha,\nu}=\frac{4\pi^2}{\alpha}
 \left(\int\frac{d\nu(w)}{1+e^{2\pi w/\alpha}}\right)^2},
 \qquad
 \boxed{B_{\alpha,\nu}=\frac{4\pi^2}{\alpha}
 \left(\int\frac{d\nu(w)}{1-e^{-2\pi w/\alpha}}\right)^2}.
\]
Furthermore, the optimal frame-operator condition number satisfies the **sharp universal bound**
\[
 \boxed{\frac{B_{\alpha,\nu}}{A_{\alpha,\nu}}\ge17+12\sqrt2}.
\]
Equality holds if and only if \(\nu=c\delta_{w_*}\) for some \(c>0\), where
\[
 \boxed{w_*=\frac{\alpha}{2\pi}\log(1+\sqrt2)}.
\]
Thus mixing different positive Cauchy poles cannot improve the best possible conditioning at critical rectangular density.

## Assumptions and scope
The measure is positive, nonzero, finite and supported in an interval \([w_0,w_1]\) with \(0<w_0\le w_1<\infty\). The window is the unnormalized Cauchy transform above; multiplying \(\nu\) by a positive constant multiplies both optimal bounds by its square and leaves their ratio unchanged. The Fourier convention is \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-2\pi it\xi}\,dt\). The frame coefficients and their squared bounds are defined by
\[
 A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}
 \big|\langle f,e^{2\pi int/\alpha}g_\nu(\cdot-\alpha m)\rangle\big|^2
 \le B\|f\|_2^2
 \quad\text{for all }f\in L^2(\mathbb R).
\]
Optimal means the greatest admissible \(A\) and the least admissible \(B\). No assertion is made for signed or complex measures, poles outside the indicated positive imaginary ray, noncritical densities, or measures approaching the singular endpoint \(w=0\) without further integrability hypotheses.

## Proof
**1. Exact critical Zak symbol.** Since \(\|(\cdot-iw)^{-1}\|_2=\sqrt{\pi/w}\) and \(w\ge w_0>0\), the Bochner integral defining \(g_\nu\) belongs to \(L^2\). Distributional Fourier transformation yields, almost everywhere,
\[
 \widehat {g_\nu}(\xi)=2\pi i\,\mathbf1_{\{\xi<0\}}
 \int e^{2\pi w\xi}\,d\nu(w).
\]
For \(0<t<\alpha\) and \(0<\omega<1/\alpha\), define \(Z_\alpha f(t,\omega)=\sum_{k\in\mathbb Z} f(t-\alpha k)e^{2\pi i\alpha k\omega}\) in the standard \(L^2\)-Zak sense. Fourier-periodization and a uniformly convergent geometric series (uniformity follows from \(w\ge w_0\)) give
\[
 Z_\alpha g_\nu(t,\omega)=\frac{2\pi i}{\alpha}
 e^{2\pi it(\omega-1/\alpha)}
 F_{\alpha\omega}(e^{-2\pi it/\alpha}),
\]
where, writing \(u=\alpha\omega\in(0,1)\),
\[
 q_w=e^{-2\pi w/\alpha}\in(0,1),\qquad
 c_u(w)=q_w^{\,1-u}>0,\qquad
 F_u(z)=\int\frac{c_u(w)}{1-q_w z}\,d\nu(w).
\]
At critical lattice product one, Zak diagonalization identifies the Gabor frame operator with multiplication by
\[
 \Lambda(u,\theta)=\frac{4\pi^2}{\alpha}|F_u(e^{i\theta})|^2.
\]
Here \(u\in(0,1)\), \(\theta\in(0,2\pi)\); the harmless sign of \(\theta\) has no effect on the modulus. The compact support assumption makes \(F_u(e^{i\theta})\) continuous on the closed rectangle \([0,1]\times[0,2\pi]\). Consequently, its squared essential minimum and maximum are the sharp squared frame bounds.

**2. Strict monotonicity of the Zak modulus.** For \(0<q,r<1\) and \(x=\cos\theta\in[-1,1]\), put
\[
 D_q(x)=1-2qx+q^2>0,\qquad
 K_{q,r}(x)=\Re\frac{1}{(1-qe^{i\theta})(1-re^{-i\theta})}.
\]
Direct multiplication and partial fractions give the two identities
\[
 K_{q,r}(x)=\frac{1-(q+r)x+qr}{D_q(x)D_r(x)}>0,
\]
\[
 K_{q,r}(x)=\frac{1}{1-qr}
 \left(\frac{1-qx}{D_q(x)}+\frac{1-rx}{D_r(x)}-1\right).
\]
The first numerator is at least \((1-q)(1-r)>0\). Also,
\[
 \frac{d}{dx}\frac{1-qx}{D_q(x)}
 =\frac{q(1-q^2)}{D_q(x)^2}>0.
\]
It follows that \(K_{q,r}\) is strictly increasing in \(x\). Since
\[
 |F_u(e^{i\theta})|^2
 =\iint c_u(w)c_u(v)K_{q_w,q_v}(\cos\theta)\,d\nu(w)d\nu(v),
\]
the squared modulus is strictly increasing in \(x=\cos\theta\). For fixed \(x\), it is also strictly increasing in \(u\), since \(c_u(w)=e^{-2\pi w(1-u)/\alpha}\) strictly increases in \(u\), and each \(K_{q_w,q_v}(x)>0\). Thus its global minimum is at \((u,x)=(0,-1)\) and its global maximum at \((1,1)\). These boundary values are limits of interior values, hence are **essential** extrema, not merely formal boundary evaluations.

At those corners,
\[
 F_0(-1)=\int\frac{q_w}{1+q_w}\,d\nu(w)
 =\int\frac{d\nu(w)}{1+e^{2\pi w/\alpha}},
\]
\[
 F_1(1)=\int\frac{1}{1-q_w}\,d\nu(w)
 =\int\frac{d\nu(w)}{1-e^{-2\pi w/\alpha}}.
\]
Both are finite and strictly positive. Multiplying their squares by \(4\pi^2/\alpha\) proves the two optimal frame bounds and frame invertibility.

**3. Universal optimal conditioning and equality.** Let \(R_w=e^{2\pi w/\alpha}>1\), and put \(\ell(w)=(R_w+1)^{-1}\), \(h(w)=R_w/(R_w-1)\). Then
\[
 \sqrt{B_{\alpha,\nu}/A_{\alpha,\nu}}=
 \frac{\int h\,d\nu}{\int\ell\,d\nu}
 =\int \frac{R_w(R_w+1)}{R_w-1}\,d\mu(w),
\]
where \(d\mu=\ell\,d\nu/\int\ell\,d\nu\) is a probability measure. For \(R>1\), define \(r(R)=R(R+1)/(R-1)\). Differentiating gives
\[
 r'(R)=\frac{R^2-2R-1}{(R-1)^2}.
\]
The unique global minimum is \(R_*=1+\sqrt2\), at which \(r(R_*)=3+2\sqrt2\). Averaging yields \(\sqrt{B/A}\ge3+2\sqrt2\), hence \(B/A\ge(3+2\sqrt2)^2=17+12\sqrt2\). Since the minimizer is unique and \(\ell>0\), equality forces \(\nu\) to be supported on \(\{w_*\}\); positivity implies \(\nu=c\delta_{w_*}\), \(c>0\). Conversely this measure attains equality. This proves sharpness and the complete equality classification.

## Verification
The standalone `checker.py` confirms the rational kernel identities and strict monotonicity on extensive rational grids, checks sampled Zak multipliers at three lattice widths, and tests the sharp numerical barrier. Its tests are supplemental: the universal measure-valued theorem and equality conditions follow from the identities and monotonicity proved above. Run with `python3 checker.py`; no third-party packages are required.

The normalization can also be checked independently by integrating the multiplier. Fourier orthogonality in the angular Zak coordinate gives
\[
 \int_0^1\int_0^{2\pi}\Lambda(u,\theta)\,\frac{d\theta}{2\pi}\,du
 =2\pi\iint\frac{d\nu(w)d\nu(v)}{w+v}=\|g_\nu\|_2^2.
\]
The final identity follows by contour integration of the Cauchy kernels, and verifies the factor \(4\pi^2/\alpha\).

For the single-pole case \(\nu=c\delta_w\), the two bound formulas specialize to the previously published one-Cauchy-kernel critical frame constants. For a two-pole example \(\nu=\delta_{\alpha\log2/(2\pi)}+\delta_{\alpha\log3/(2\pi)}\), the exact results are
\[
 A_{\alpha,\nu}=\frac{4\pi^2}{\alpha}\left(\frac13+\frac14\right)^2
 =\frac{49\pi^2}{36\alpha},\qquad
 B_{\alpha,\nu}=\frac{4\pi^2}{\alpha}\left(2+\frac32\right)^2
 =\frac{49\pi^2}{\alpha}.
\]
Thus \(B/A=36\), strictly above \(17+12\sqrt2\), providing a transparent exact benchmark.

## Relationship to prior work
Belov, Kulikov and Lyubarskii (2021 preprint; 2022 journal) establish the frame property of finite positive-pole Herglotz windows at all lattice products at most one and give an explicit rational Zak-type function for general finite pole sets. Their principal results concern frame existence and frame sets rather than optimal constants for arbitrary positive mixtures or a universal conditioning minimizer. Belov, Kulikov and Lyubarskii (December 2022) calculate the **single Cauchy pole** Zak transform and its sharp critical-lattice bounds; the present formula agrees with that case. The new point here is the strict two-variable positivity/monotonicity lemma for all positive pole mixtures, its extension to non-atomic compactly supported positive measures, and the universal, equality-rigid best possible frame condition number. The already known one-pole formula and the general critical Zak diagonalization are not claimed as new.

## Limitations
The condition-number obstruction is restricted to positive Cauchy mixtures whose poles lie on the positive imaginary ray; cancellations from complex or signed weights need not obey it. No assertion is made about optimal frame bounds at oversampled lattices, irregular lattices, or other time-frequency windows. The proof is analytical and does not assert independent external validation or priority over all potentially inaccessible literature. The exact extremal constants are approached in the Zak domain as boundary values; they do not imply existence of extremizing nonzero \(L^2\) vectors.

## References
1. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959v1 (first public March 16, 2021), especially Theorem 1.1 and the rational Zak-type function in Section 1.5; published in *Inventiones mathematicae* 231 (2023), 431–466, DOI:10.1007/s00222-022-01151-8.
2. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915v1 (December 17, 2022), especially the critical-lattice Zak formula and single-pole optimal bounds on page 2.
3. The standard critical-density Zak frame-operator diagonalization is reviewed in reference 2, Section 1, and reference 1, Section 1.2.
