# Exponential collapse of the zero-free radial band in thin-annulus Bergman kernels

## Finding

Let \(A_r=\{z\in\mathbb C:r<|z|<1\}\) for \(0<r<1\), and let \(K_r(z,w)\) be its ordinary area-normalized Bergman kernel. The established annulus zero classification gives a unique number \(x_r\in(\sqrt r,1)\) such that \(K_r(z,w)=0\) for some \(z\in A_r\) exactly when \(|w|<r/x_r\) or \(|w|>x_r\). Thus the central zero-free radial band is \(r/x_r\le |w|\le x_r\). Its width \(\Delta(r)=x_r-r/x_r\) satisfies the **sharp nonperturbative thin-annulus law**

\[
\boxed{\displaystyle
\Delta(r)\sim\frac{4\sqrt r}{\pi}\log\frac1r\,
\exp\!\left(-\frac{\pi^2}{\log(1/r)}\right)}
\qquad(r\uparrow1).
\]

Equivalently, with \(L=2\log(1/r)\),
\[
\lim_{L\downarrow0}\frac{\pi\Delta(e^{-L/2})}{2L e^{-L/4}}e^{2\pi^2/L}=1.
\]

The amplitude, exponential rate, and the sharp coefficient \(4/\pi\) are all specified. This result quantifies, rather than re-proves, the previously known annulus zero-fibre classification.

## Assumptions and scope

The kernel uses Euclidean area measure \(dA\), so its reproducing identity is \(f(z)=\int_{A_r} f(w)\overline{K_r(z,w)}\,dA(w)\). The position variable is \(z\), the fixed evaluation point is \(w\), and a zero is within the open annulus in both variables. All limits hold as \(r\) tends to \(1\) from below. The previously established exact radial zero classification is used only to identify \(\Delta\) as the full zero-free band; the quantitative asymptotic is proved below from the exact kernel series.

## Proof

**1. Kernel series and scalar roots.** Write \(q=r^2=e^{-L}\), and put \(t=z\overline w\). Orthogonality of the Laurent monomials \(z^n\) in \(A_r\) gives
\[
\pi tK_r(z,w)=\frac1L+\sum_{n\in\mathbb Z\setminus\{0\}}
\frac{n t^n}{1-q^n}=:H_r(t).
\]
The normalizations follow directly from \(\|z^{-1}\|_{L^2(A_r)}^2=\pi L\) and, for \(n\ne-1\), \(\|z^n\|^2=\pi(1-r^{2n+2})/(n+1)\). All series converge normally when \(q<|t|<1\). Setting \(t=-x\) for \(q<x<1\) and summing geometric series yields
\[
H_r(-x)=\frac1L-\sum_{m\ge0}\left[
\frac{xq^m}{(1+xq^m)^2}
+\frac{q^{m+1}/x}{(1+q^{m+1}/x)^2}
\right]. \tag{1}
\]
Existing exact annulus results identify precisely two simple scalar roots, at \(-x_r\) and \(-q/x_r\), with \(\sqrt r<x_r<1\). Consequently a fixed \(|w|=s\) has a kernel zero in the first branch exactly if \(s>x_r\), and in the other branch exactly if \(s<r/x_r\). This gives the zero-free band stated above; see Gustafsson--Sebbar, Theorem 6.1, for the qualitative classification.

**2. Exact Poisson duality.** Define \(g(y)=e^{-y}/(1+e^{-y})^2=1/(4\cosh^2(y/2))\). Put \(x=e^{-Lv}\) for \(0<v<1\). Equation (1), using the evenness of \(g\), becomes
\[
H_r(-e^{-Lv})=\frac1L-\sum_{m\in\mathbb Z}g(L(m+v)).
\]
With the substitution \(s=e^y\), the beta integral gives \(\widehat g(\omega)=\int_0^\infty s^{-i\omega}(1+s)^{-2}\,ds=\Gamma(1-i\omega)\Gamma(1+i\omega)\). The gamma reflection identity therefore gives
\[
\widehat g(\omega)=\int_{\mathbb R}g(y)e^{-i\omega y}\,dy
=\frac{\pi\omega}{\sinh(\pi\omega)},\qquad
\widehat g(0)=1.
\]
Poisson summation applies to this smooth exponentially decaying function and gives the **exact** absolutely convergent Fourier identity
\[
H_r(-e^{-Lv})=-\frac{4\pi^2}{L^2}\sum_{k=1}^{\infty}
\frac{k\cos(2\pi kv)}{\sinh(2\pi^2k/L)}.\tag{2}
\]
This identity holds for every \(L>0\), uniformly with derivatives in \(v\).

**3. Quantified displacement from the quarter-period.** Write \(v_0=1/4\) and \(E=e^{-2\pi^2/L}\). At \(v_0\), odd Fourier modes vanish. By (2),
\[
H_r(-e^{-Lv_0})=\frac{16\pi^2}{L^2}E^2(1+O(E^2)).\tag{3}
\]
Similarly, differentiation of (2) yields
\[
\left.\frac\partial{\partial v}H_r(-e^{-Lv})\right|_{v=v_0}
=\frac{16\pi^3}{L^2}E(1+O(E^2)).\tag{4}
\]
The remainder estimates follow by \(1/\sinh(ak)=2e^{-ak}(1+O(e^{-2ak}))\) and geometric tail bounds, uniformly for \(a=2\pi^2/L\to\infty\). Around \(v_0\), the derivative stays positive and has the stated leading order throughout any window of size \(O(E)\): the first Fourier harmonic dominates there, and the differentiated higher-harmonic tail is \(O(L^{-2}E^2)\). In particular, (3)--(4) and the intermediate value theorem give a unique root \(v_r\) in that window, satisfying, by the mean value theorem,
\[
v_r-\frac14=-\frac1\pi E(1+o(1)).\tag{5}
\]
This root corresponds to \(x_r=e^{-Lv_r}>e^{-L/4}=\sqrt r\) and hence is the distinguished outer scalar root from the preceding classification.

**4. Band width.** Substituting (5),
\[
\begin{aligned}
\Delta(r)&=x_r-\frac r{x_r}
=e^{-Lv_r}-e^{-L(1/2-v_r)}\\
&=2e^{-L/4}\sinh\!\left(L(1/4-v_r)\right)\\
&=\frac{2L}{\pi}e^{-L/4}E(1+o(1)).
\end{aligned}
\]
Since \(L=2\log(1/r)\), this is exactly the claimed sharp law. \(\square\)

## Verification

The standalone checker `verify_annulus.py` compares the direct Laurent-series evaluation of \(H_r\) with the Poisson-dual Fourier series at high precision; it numerically brackets the scalar root and compares the exact band width with the theorem's leading approximation. The checks are finite consistency tests, not substitutes for Poisson summation, the uniform tail bounds, or the analytic root argument.

## Relationship to prior work

Gustafsson and Sebbar (arXiv:0912.1223v1, Theorem 6.1 and Section 6.3) explicitly prove the full qualitative zero-fibre classification and the existence of a central zero-free band for an annulus. Those facts are **not** asserted as new here. The present statement is the sharp exponentially small asymptotic width, including its leading prefactor and rate, obtained from a direct modular Poisson analysis. The inspected full text in Section 6.3 gives an elliptic integral specification of its boundary but does not provide this thin-annulus rate. The earlier Sebbar--Falliero article on Green-function equilibria and Eisenstein series could not be fully inspected and remains a priority risk.

## Limitations

Only the thin-annulus limit for the ordinary, unweighted Bergman kernel is treated. The result does not establish corresponding rates for general doubly connected domains, weighted kernels, or complex perturbations of the annulus. The qualitative fibre classification is pre-existing. No external independent validation or priority certification has been performed.

## References

1. B. Gustafsson and A. Sebbar, *Critical points of Green's function and geometric function theory*, arXiv:0912.1223v1 (public 2009-12-07), especially Section 6.3 and Theorem 6.1. https://arxiv.org/pdf/0912.1223
2. A. Sebbar and T. Falliero, *Equilibrium point of Green's function for the annulus and Eisenstein series*, *Proc. Amer. Math. Soc.* **135** (2007), DOI:10.1090/S0002-9939-06-08353-5 (relevant earlier source; full text unavailable in this comparison).
