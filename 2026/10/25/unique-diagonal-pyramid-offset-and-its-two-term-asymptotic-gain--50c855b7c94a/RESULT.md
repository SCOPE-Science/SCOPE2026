# Unique diagonal pyramid offset and its two-term asymptotic gain in the cube

## Finding
For each integer \(n\ge 3\), put \(Q_n=[0,1]^n\) and \(H_s=Q_n\cap\{x_1+\cdots+x_n=s\}\), \(0<s<n\). Let \(W_n(s)\) be the \(n\)-dimensional Euclidean volume of the pyramid with apex \(0\) and entire base \(H_s\). Write \(f_n\) for the density of the sum of \(n\) independent uniform random variables on \([0,1]\). Then
\[
W_n(s)=\frac{s}{n}f_n(s)=\frac{s}{n!}\sum_{k=0}^{\lfloor s\rfloor}(-1)^k\binom nk(s-k)^{n-1}.
\]
There exists **exactly one** maximizer \(s_n\in(0,n)\), and it lies strictly beyond the central section: \(n/2<s_n<n\). It is uniquely characterized by
\[
 \frac{f_n'(s_n)}{f_n(s_n)}=-\frac1{s_n}.
\]
For the central diagonal pyramid volume \(c_n=W_n(n/2)=f_n(n/2)/2\), the sharp diagonal-family optimizer satisfies, as integer \(n\to\infty\),
\[
 \boxed{\ s_n=\frac n2+\frac16+\frac{2}{45n}+O(n^{-2})\ },\qquad
 \boxed{\ \frac{W_n(s_n)}{c_n}=1+\frac1{6n}+\frac7{120n^2}+O(n^{-3})\ }.
\]
The unrestricted maximal pyramid volume \(M_n\) therefore satisfies \(M_n\ge W_n(s_n)>c_n\) for \(n\ge3\). No assertion is made that diagonal pyramids optimize \(M_n\) for \(n\ge4\).

For a concrete finite-dimensional benchmark, \(s_4=2+t_4\), where \(t_4\) is the **unique** root in \((0,1)\) of \(3t^3-6t+1=0\). Numerically \(s_4=2.169083656929\ldots\), and \(W_4(s_4)=0.347321469689\ldots>c_4=1/3\).

## Assumptions and scope
All ambient volumes are ordinary Euclidean Lebesgue volumes. The hyperplane \(H_s\) is orthogonal to the body diagonal \((1,\ldots,1)\), its base is the **whole cube section**, its apex is the cube vertex \(0\), and \(n\) ranges over integers \(n\ge3\). The restriction to diagonal-parallel sections is essential: globally optimal cube pyramids are not classified here. Reflection \(x\mapsto(1,\ldots,1)-x\) sends the unique maximizing apex-zero configuration to the corresponding unique opposite-vertex configuration.

## Proof
**1. Volume and density.** By coarea for the sum map \(x\mapsto x_1+\cdots+x_n\), the \((n-1)\)-area of \(H_s\) is \(\sqrt n\,f_n(s)\). The perpendicular altitude of vertex \(0\) above its base hyperplane is \(s/\sqrt n\); the pyramid-volume formula yields \(W_n(s)=s f_n(s)/n\). The alternating inclusion-exclusion expression follows by differentiating the distribution of a sum of uniforms.

**2. Exactly one optimizer.** The indicator density of one uniform interval is log-concave (in the extended sense). By the convolution preservation theorem for log-concave densities, \(f_n\) is positive and log-concave on \((0,n)\). Hence \(\log W_n(s)=\log s+\log f_n(s)-\log n\) is **strictly concave**, because \(\log s\) is strictly concave. The function is positive inside and vanishes at the two endpoints, so it has exactly one maximizer. Symmetry \(f_n(s)=f_n(n-s)\) and differentiability for \(n\ge3\) imply \(f_n'(n/2)=0\) and \(W_n'(n/2)=f_n(n/2)/n>0\), placing the maximizer strictly to the right of the center. Differentiating \(\log W_n\) proves the stationary equation.

**3. Uniform local Fourier expansion.** With \(u\) in any fixed bounded real interval, Fourier inversion gives
\[
f_n\!\left(\frac n2+u\right)=\frac{1}{2\pi}\int_{\mathbb R}e^{-itu}\left(\frac{\sin(t/2)}{t/2}\right)^n\,dt.
\]
After \(t=z/\sqrt n\), the analytic Taylor expansion at zero is
\[
\log\!\left(\frac{\sin(t/2)}{t/2}\right)
=-\frac{t^2}{24}-\frac{t^4}{2880}-\frac{t^6}{181440}+O(t^8).
\]
Expanding the product \(e^{-izu/\sqrt n}\) with this logarithm, pairing odd powers in \(z\), and integrating against the Gaussian \(e^{-z^2/24}\) (variance \(12\)) yields
\[
f_n\!\left(\frac n2+u\right)=\sqrt{\frac6{\pi n}}\left[1+\frac{-6u^2-3/20}{n}
+\frac{18u^4+(9/2)u^2-13/1120}{n^2}+O(n^{-3})\right].
\]
This expansion and its first \(u\)-derivative are uniform on fixed compact intervals. For completeness, split the transformed integral at \(|z|=n^{1/12}\), expand the analytic logarithm with its Taylor remainder on the inner part, and use Gaussian domination there. On the complementary part, the strict inequality \(|\sin(t/2)/(t/2)|<1\) for \(t\ne0\), together with the bound \(\min(1,2/|t|)\), makes the Fourier tails exponentially small in a positive power of \(n\). The additional factor \(t\) needed for differentiation obeys the same estimate. Taylor terms through absolute order \(n^{-2}\) integrate to the displayed coefficients; their omitted even moments are \(O(n^{-3})\) inside the brackets. Thus the stated remainder is justified, rather than inferred from pointwise Gaussian convergence.

Divide the expansion by its value at \(u=0\), then take logarithms. Uniformly for bounded \(u\),
\[
\log\frac{f_n(n/2+u)}{f_n(n/2)}
=-\frac{6u^2}{n}+\frac{18u^2}{5n^2}+O(n^{-3}),
\]
with first derivative in \(u\) satisfying the differentiated expansion.

**4. Drift and sharp gain.** For \(s=n/2+u\), the derivative of the log pyramid volume becomes
\[
\frac{d}{du}\log W_n(n/2+u)
=\frac{2-12u}{n}+\frac{16u}{5n^2}+O(n^{-3}).
\]
It is positive at \(u=0\) and negative at \(u=1\) for large \(n\), so strict concavity puts its only zero in \((0,1)\). Its expansion first forces \(u=1/6+O(n^{-1})\); equating the coefficients of \(n^{-2}\) then gives \(u=1/6+2/(45n)+O(n^{-2})\).

More explicitly, for bounded \(u\),
\[
\frac{W_n(n/2+u)}{c_n}
=1+\frac{2u-6u^2}{n}
+\frac{18u^4-12u^3+(18/5)u^2}{n^2}+O(n^{-3}).
\]
The first correction has its unique maximum at \(u=1/6\); its derivative vanishes there, so substituting the refined optimizing offset does not change the \(n^{-2}\) value. The coefficient at \(u=1/6\) equals \(7/120\), completing both asymptotics.

**5. Dimension four.** For \(2\le s\le3\), setting \(t=s-2\) gives \(f_4(2+t)=2/3-t^2+t^3/2\). The derivative of \(W_4(2+t)\) is \((3t^3-6t+1)/6\). Strict log-concavity supplies uniqueness of its zero in \((0,1)\), and the exact formula and numerical benchmark follow.

## Verification
Run `python3 checker.py` using only Python's standard library. The checker verifies 440 exact rational cardinal-spline/inclusion-exclusion evaluations for dimensions 3 through 12, the cubic critical equation in dimension four, and five independent large-dimension numerical checks of both asymptotic predictions. Output ends in `DIAGONAL_PYRAMID_CHECK_OK`. The finite tests independently corroborate the Fourier/concavity argument, but the global uniqueness and asymptotic orders follow from the analytic proof, not from enumeration.

## Relationship to prior work
Nikolov's October 2026 paper introduces the unrestricted maxima, explicitly states the diagonal pyramid formula and shows its derivative is positive at the central section. **Those ingredients are prior work**. The contribution here is the unique optimizer within the full noncentral diagonal section family, its explicit one-dimensional characterization, the second-order offset and relative-volume expansions, and the exact dimension-four diagonal benchmark. Nikolov does not claim that the offset-maximized diagonal pyramids solve the unrestricted problem in all dimensions. The general forward formula for cube slice volumes is classical and is not claimed as new.

Ambrus–Gárgyán treat the central Laplace–Pólya integral and its decay; their central-section expansion does not optimize the size-biased offset. Brandenburg–De Loera–Luo–Meroni develop piecewise formulas and critical-point tools for cube slices and slabs; their optimization concerns sections and moments, not an apex-distance-weighted pyramid section in growing dimension. Pournin studies section extrema at fixed offsets with varying orientations. No stronger implication covering both uniqueness and the stated two-term asymptotics was identified in the inspected works. Priority in older unindexed literature remains a genuine residual risk.

## Limitations
No global maximizer among arbitrary hyperplane directions is asserted for dimensions \(n\ge4\), and no asymptotic for the **unrestricted** maximal pyramid volume is established. Error constants in the expansions are absolute in this fixed diagonal family; they do not apply uniformly to variable directions. The general fact that the diagonal section derivative is nonzero at the center was already known; only the additional claims above are proposed as new.

## References
1. N. Nikolov, *Maximal volumes of pyramids in the unit cube*, arXiv:2610.14047v1 (first public 2026-10-04). https://arxiv.org/html/2610.14047v1
2. G. Ambrus and B. Gárgyán, *Estimates on the decay of the Laplace–Pólya integral*, arXiv:2412.12835v1 (2024), *Bull. London Math. Soc.* 57 (2025), 3360–3379. https://arxiv.org/abs/2412.12835
3. M.-C. Brandenburg, J. A. De Loera, Y. Luo, and C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643v1 (2026). https://arxiv.org/abs/2603.25643
4. L. Pournin, *Local extrema for hypercube sections*, arXiv:2203.15054v2 (2023). https://arxiv.org/abs/2203.15054
