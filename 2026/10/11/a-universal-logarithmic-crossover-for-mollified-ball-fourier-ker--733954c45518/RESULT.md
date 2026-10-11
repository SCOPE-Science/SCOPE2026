# A universal logarithmic crossover for mollified-ball Fourier kernels

## Finding

Fix an integer \(d\ge2\). Use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-ix\cdot\xi}\,dx,\qquad
\mathcal F^{-1}g(x)=(2\pi)^{-d}\int_{\mathbb R^d}g(\xi)e^{ix\cdot\xi}\,d\xi.
\]
Let \(\eta\ge0\) be supported in \((-1/2,1/2)\), belong to \(C_c^\infty(\mathbb R)\), and have integral one. For \(0<\delta<1/2\) define
\[
h_{\delta,\eta}(\xi)=\int_{\mathbb R}\eta(u)\,\mathbf1_{\{|\xi|\le1+\delta u\}}\,du,
\qquad K_{\delta,\eta}=\mathcal F^{-1}h_{\delta,\eta}.
\]
Put \(p_c=2d/(d+1)\), \(L_\delta=\log(1/\delta)\), and for any real \(\lambda\) put \(p_{\delta,\lambda}=p_c-\lambda/L_\delta\). Define
\[
\begin{split}
 C_d={}&|S^{d-1}|\left((2\pi)^{-d/2}\sqrt{2/\pi}\right)^{p_c}
 \frac{\Gamma((p_c+1)/2)}{\sqrt\pi\,\Gamma((p_c+2)/2)},\\
 \Phi_d(\lambda)={}&\int_0^1\exp\!\left(\frac{d+1}{2}\lambda t\right)dt
 =\begin{cases}\dfrac{e^{(d+1)\lambda/2}-1}{(d+1)\lambda/2},&\lambda\ne0,\\ 1,&\lambda=0.\end{cases}
\end{split}
\]
Then the **exact critical-window law** is
\[
\boxed{\displaystyle
\lim_{\delta\downarrow0}\frac{\|K_{\delta,\eta}\|_{L^{p_{\delta,\lambda}}(\mathbb R^d)}^{p_{\delta,\lambda}}}{\log(1/\delta)}
 =C_d\Phi_d(\lambda).}
\]
This is uniform over \(\lambda\) in every compact real interval **and** uniform over normalized nonnegative profiles \(\eta\) supported in \((-1/2,1/2)\) with a fixed bound on \(\|\eta\|_{W^{2,1}(\mathbb R)}\), whenever this profile class is nonempty. In particular the profile may vary with \(\delta\). The complete crossover curve is independent of the smoothing profile.

## Assumptions and scope

The dimension \(d\) is fixed, not allowed to grow with \(\delta\). The exponent is positive and at least one for sufficiently small \(\delta\), uniformly for bounded \(\lambda\). The profile is a radial *boundary-coordinate mollifier*: it averages indicators of balls whose radii lie within \(\delta/2\) of one. The theorem concerns \(L^p\) norms of the convolution kernel, **not** \(L^p\)-operator norms of the Fourier multiplier. The latter are generally larger at the endpoint.

The statement includes both sides of the critical index: negative \(\lambda\) corresponds to \(p_{\delta,\lambda}>p_c\), positive \(\lambda\) to \(p_{\delta,\lambda}<p_c\). Its assertion is a joint limit; it does not give an exact asymptotic for an exponent kept strictly away from \(p_c\).

## Proof

Write \(r=|x|\), \(R_u=1+\delta u\), \(\alpha=(d+1)/2\), and \(\beta=(d+1)\pi/4\). The standard radial Fourier transform of a ball gives, exactly,
\[
K_{\delta,\eta}(r)
=(2\pi)^{-d/2}r^{-d/2}
\int\eta(u)R_u^{d/2}J_{d/2}(rR_u)\,du.
\tag{1}
\]
The continuous value at \(r=0\) is understood. The fixed-order Bessel expansion, uniform for \(r\ge1\) and \(1-\delta/2\le R_u\le1+\delta/2\), is
\[
J_{d/2}(rR_u)=\sqrt{\frac2{\pi rR_u}}\cos(rR_u-\beta)
+O_d(r^{-3/2}).
\]
Thus, with \(a_d=(2\pi)^{-d/2}\sqrt{2/\pi}\),
\[
K_{\delta,\eta}(r)
=a_dr^{-\alpha}\operatorname{Re}\!\left[e^{i(r-\beta)}A_{\delta,\eta}(\delta r)\right]
+E_{\delta,\eta}(r),
\tag{2}
\]
where
\[
A_{\delta,\eta}(s)=\int\eta(u)(1+\delta u)^{(d-1)/2}e^{isu}\,du,
\qquad |E_{\delta,\eta}(r)|\le C_dr^{-\alpha-1}.
\tag{3}
\]
All constants here are uniform over the indicated normalized profiles. Two integrations by parts, using their uniformly bounded \(W^{2,1}\) norm, give
\[
|A_{\delta,\eta}(s)|\le C_{d,M}(1+|s|)^{-2},
\quad |A_{\delta,\eta}(s)-1|\le C_d(\delta+|s|),
\tag{4}
\]
where \(M\) bounds \(\|\eta\|_{W^{2,1}}\). The second inequality uses nonnegativity, unit mass, and compact support.

Fix \(\Lambda>0\) and restrict \(|\lambda|\le\Lambda\). For sufficiently small \(\delta\), \(p=p_{\delta,\lambda}\) stays in a compact subset of \((1,\infty)\) on which \((\alpha+1)p>d\). Consequently \(\|E_{\delta,\eta}\|_p^p=O(1)\) over \(r\ge1\), uniformly. Equations (2)--(4) give an \(O(L_\delta)\) bound for the \(p\)-th power of the radial leading-term norm: split \(r\le\delta^{-1}\), where \(|A|\le C\), from \(r\ge\delta^{-1}\), where \((1+\delta r)^{-2}\) is integrable. The inequality
\[
\bigl||v+w|^p-|v|^p\bigr|\le C\bigl(|v|^{p-1}|w|+|w|^p\bigr)
\]
and Hölder then show that replacing \(K\) by the leading term in (2) changes its \(L^p\)-power integral by \(O(L_\delta^{1-1/p}+1)=o(L_\delta)\). The portion \(r<1\) contributes only \(O(1)\), because \(0\le h_{\delta,\eta}\le1\) and its support has bounded measure.

Set \(L=L_\delta\) and choose \(0<\varepsilon<1/2\). On the bulk annulus
\[
e^{\varepsilon L}\le r\le e^{(1-\varepsilon)L},
\]
we have \(\delta r\le e^{-\varepsilon L}\), so (4) gives \(A_{\delta,\eta}(\delta r)=1+o(1)\) uniformly. With \(p=p_c-\lambda/L\),
\[
r^{d-1-\alpha p}\,dr=r^{-1+\alpha\lambda/L}\,dr.
\]
The periodic function \(v_p(r)=|\cos(r-\beta)|^p\) has mean
\[
\overline v_p=\frac1\pi\int_0^\pi|\cos t|^p\,dt
=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)}.
\tag{5}
\]
The zero-mean periodic function \(v_p-\overline v_p\) has a primitive bounded uniformly for \(p\) in the above compact interval. Integration by parts against the monotone weight \(r^{-1+\alpha\lambda/L}\) shows that replacing \(v_p\) by \(\overline v_p\) in the bulk radial integral incurs \(O(1)\), uniformly in \(\delta,\lambda\). Substituting \(t=\log r/L\), the bulk contribution divided by \(L\) therefore tends, uniformly,
\[
|S^{d-1}|a_d^{p_c}\overline v_{p_c}
\int_\varepsilon^{1-\varepsilon}e^{\alpha\lambda t}\,dt.
\tag{6}
\]

For the omitted inner range \(1\le r<e^{\varepsilon L}\) and the upper edge \(e^{(1-\varepsilon)L}\le r\le e^L\), the leading-term integral is \(O_{d,M,\Lambda}(\varepsilon L)\), directly from (3)--(4). For \(r>e^L=\delta^{-1}\), the substitution \(s=\delta r\) and \(|A_{\delta,\eta}(s)|\le C(1+s)^{-2}\) bound the leading-term integral by \(O_{d,M,\Lambda}(1)\). Let \(\delta\downarrow0\), then \(\varepsilon\downarrow0\). The coefficient in (6) is exactly \(C_d\), and the integral over \(0\le t\le1\) is \(\Phi_d(\lambda)\). All bounds were uniform for \(|\lambda|\le\Lambda\) and the normalized profile family, proving the theorem.

## Verification

The Bessel normalization in (1) follows directly from Fourier inversion of \(\mathbf1_{\{|\xi|\le R\}}\). In dimension two, the endpoint constant reduces to
\[
C_2=\frac{2^{1/3}}{\pi^2}\mathrm B\!\left(\frac12,\frac76\right)
=0.2325251309295119\ldots,
\]
matching the independently published leading coefficient for the trapezoidal radial profile at the single endpoint exponent. In dimension three,
\(p_c=3/2\) and \(C_3=0.0797290043956112\ldots\). The attached `verify_crossover.py` recomputes both constants and the exact relation for \(C_2\), and performs finite-parameter checks on the explicit three-dimensional trapezoidal kernel. These checks supplement, but do not replace, the analytic proof. No finite computation establishes the universal limit by itself.

## Relationship to prior work

Carbery and Seeger, *Mollified disc multipliers*, arXiv:2609.32919v1 (first public 2026-09-26), introduce precisely this type of boundary-coordinate smoothing and obtain sharp multiplier-norm estimates, including the planar endpoint \(L^4\) logarithmic growth. They record two-sided growth for the convolution-kernel \(L^{4/3}\) norm; that fixed-exponent result does not determine a transition when the exponent itself changes by \(1/\log(1/\delta)\). The earlier published *Exact leading constant for the endpoint kernel norm of a trapezoidal disc mollifier* supplies the single value \((d,\lambda)=(2,0)\) for one profile. The present claim recovers that value, but its substantive result is the uniform, all-dimensional, all-profile crossover curve for varying exponents. The proof directly controls this joint limit, which cannot be obtained from a fixed-exponent limit alone.

Standard Bessel asymptotics (Stein--Weiss; Watson) supply the oscillatory leading term, not the full variable-exponent, uniform-in-mollifier conclusion. Other work on uniform Bessel \(L^p\) estimates concerns closely related estimates but has not been established to settle this particular joint limit.

## Limitations

This does not yield the sharp \(L^p\) Fourier-multiplier operator norm, and no universal law is asserted when the exponent stays a fixed distance from \(p_c\). The profile-independence requires normalized smoothing profiles with fixed uniform regularity bounds. No dimension-uniform assertion is made. Despite searches and comparison with the principal current source and the closest published endpoint calculation, equivalent treatments under older Bessel-integral or approximation-theoretic terminology cannot be excluded.

## References

1. A. Carbery and A. Seeger, *Mollified disc multipliers*, arXiv:2609.32919v1 (2026), https://arxiv.org/pdf/2609.32919.
2. *Exact leading constant for the endpoint kernel norm of a trapezoidal disc mollifier*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-leading-constant-for-the-endpoint-kernel-norm-of-a-trapezo--1a76f3a9a8a8/RESULT.md.
3. E. M. Stein and G. Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*, Princeton University Press (1971).
4. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, Cambridge University Press (2nd edition, 1944).
5. K. Guo, *A uniform \(L^p\) estimate of Bessel functions and distributions supported on spheres*, Proc. Amer. Math. Soc. 125 (1997), 1329--1340, DOI:10.1090/S0002-9939-97-03667-8.
