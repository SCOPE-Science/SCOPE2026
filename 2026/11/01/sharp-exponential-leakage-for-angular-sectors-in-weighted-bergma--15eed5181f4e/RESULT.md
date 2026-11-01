# Sharp exponential leakage for angular sectors in weighted Bergman spaces

## Finding

For every fixed angular interval \(0<a<b<\pi\), there is a unique frequency which optimizes the weighted analytic Bergman \(L^2\)-mass inside the scale-invariant sector \(\Omega_{a,b}=\{z\in\mathbb H:a<\arg z<b\}\). The optimal leakage has an explicit *sharp exponential rate and prefactor*, and the maximizing frequency has an explicit bounded-order drift as the Bergman weight grows.

Write
\[
C_\lambda(a,b)=\sup_{0\ne f\in A^2_\lambda(\mathbb H)}
\frac{\int_{\Omega_{a,b}} |f(z)|^2(\operatorname{Im}z)^\lambda\,dA(z)}
{\int_{\mathbb H}|f(z)|^2(\operatorname{Im}z)^\lambda\,dA(z)},\qquad \lambda>-1.
\]
Define, using natural logarithms,
\[
\begin{aligned}
\tau_*&=\frac{\log\sin b-\log\sin a}{b-a},&
\theta_*&=\operatorname{arccot}\tau_*\in(a,b),\\
u&=\cot a-\tau_*,&v&=\tau_*-\cot b,\\
\ell&=\theta_*-a,&r&=b-\theta_*,\\
\Delta&=\log\frac{\sin\theta_*}{\sin a}-\tau_*\ell,&
d_*&=\frac{1}{2(b-a)}\log\frac{ru}{\ell v},\\
K&=\frac{1}{\sin\theta_*\sqrt{2\pi}}
\left(\frac{e^{2d_*\ell}}{u}+\frac{e^{-2d_*r}}{v}\right).
\end{aligned}
\]
All of \(u,v,\ell,r,\Delta,K\) are strictly positive. With the frequency normalization specified below, the unique maximizing frequency \(\xi_\lambda\) satisfies
\[
\boxed{\xi_\lambda=\frac{\lambda\tau_*}{2}+d_*+o(1)},\qquad
\boxed{1-C_\lambda(a,b)\sim K\lambda^{-1/2}e^{-\lambda\Delta}}
\quad(\lambda\to\infty).
\]
For every fixed \(\lambda>-1\), \(0<C_\lambda(a,b)<1\), the maximizing frequency is nondegenerate, and the supremum over nonzero holomorphic functions is not attained. In the symmetric example \(a=\pi/3\), \(b=2\pi/3\), one has \(\xi_\lambda=0\) for every \(\lambda>-1\) and
\[
1-C_\lambda(\pi/3,2\pi/3)\sim
\sqrt{\frac{6}{\pi\lambda}}\left(\frac{\sqrt3}{2}\right)^\lambda.
\]

## Assumptions and scope

Here \(\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}\), and \(A^2_\lambda(\mathbb H)\) denotes the holomorphic functions integrable against \((\operatorname{Im}z)^\lambda dA(z)\), \(\lambda>-1\). Any positive normalization of area measure cancels from the ratio. The interval endpoints are fixed strictly in \((0,\pi)\) as \(\lambda\to\infty\). There is no uniform assertion as either endpoint approaches \(0\), \(\pi\), or the other endpoint. The frequency \(\xi\) is normalized by the established Mellin spectral representation with angular density \(e^{-2\xi\theta}\sin^\lambda\theta\,d\theta\).

## Proof

**1. Exact sharp reduction (previously established representation).** The hyperbolic/angular Toeplitz diagonalization gives a unitary equivalence between the positive localization form for the indicator of \(\Omega_{a,b}\) and multiplication on \(L^2(\mathbb R,d\xi)\) by
\[
F_\lambda(\xi)=\frac{\int_a^b e^{-2\xi\theta}\sin^\lambda\theta\,d\theta}{\int_0^\pi e^{-2\xi\theta}\sin^\lambda\theta\,d\theta}.
\]
This formula follows already from Grudsky–Karapetyants–Vasilevski and Rozenblum–Vasilevski; it is not a novelty claim here. Thus \(C_\lambda(a,b)=\sup_{\xi\in\mathbb R}F_\lambda(\xi)\). Since the denominator is finite for \(\lambda>-1\), \(F_\lambda\) is smooth and positive. It tends to zero as \(\xi\to\pm\infty\), since the tilted angular mass escapes to the respective endpoint outside \((a,b)\); hence it has at least one maximizer.

**2. Unique nondegenerate maximum.** Put \(w(\theta)=e^{-2\xi\theta}\sin^\lambda\theta\) and \(Z=\int_0^\pi w\). Define the strictly positive integrals
\[
\begin{aligned}
A(\xi)&=\int_a^b\int_0^a(\theta-s)w(\theta)w(s)\,ds\,d\theta,\\
B(\xi)&=\int_a^b\int_b^\pi(s-\theta)w(\theta)w(s)\,ds\,d\theta.
\end{aligned}
\]
Direct differentiation of the quotient gives \(F_\lambda'(\xi)=2(B-A)/Z^2\). In \(A\), the sum \(\theta+s<a+b\), whereas in \(B\) it is \(\theta+s>a+b\), apart from null boundaries. Differentiating the logarithm of their ratio under their positive product measures yields
\[
\frac{d}{d\xi}\log\frac{A(\xi)}{B(\xi)}
=2\big(\mathbb E_B[\theta+s]-\mathbb E_A[\theta+s]\big)>0.
\]
The ratio tends to \(0\) as \(\xi\to-\infty\) and \(+\infty\) as \(\xi\to+\infty\), by the strict separation of the ranges of \(\theta+s\). Therefore \(A=B\) exactly once. The derivative changes strictly from positive to negative there; moreover \(F_\lambda''<0\) at this critical point, because \((A/B)'>0\). Hence the maximizer \(\xi_\lambda\) is unique and nondegenerate. Since multiplication by \(F_\lambda\) on \(L^2(\mathbb R)\) has no eigenfunction supported on its singleton maximum, the original sharp norm ratio is not attained by any nonzero holomorphic function.

**3. Balancing the two exponentially small tails.** For real \(\tau\) define \(h_\tau(\theta)=\log\sin\theta-\tau\theta\). It is strictly concave on \((0,\pi)\), with unique maximum at \(\theta_\tau=\operatorname{arccot}\tau\), where \(-h_\tau''(\theta_\tau)=\sin^{-2}\theta_\tau\). From the definition of \(\tau_*\), \(h_{\tau_*}(a)=h_{\tau_*}(b)\), and strict concavity gives \(\theta_*\in(a,b)\), \(u,v>0\), and \(\Delta=h_{\tau_*}(\theta_*)-h_{\tau_*}(a)>0\).

Set \(\tau=2\xi/\lambda\), so \(w(\theta)=e^{\lambda h_\tau(\theta)}\). Uniform one-sided Watson/Laplace estimates for \(\tau\) in a fixed neighborhood of \(\tau_*\) give
\[
\begin{split}
A(\lambda\tau/2)&\sim
\left(\int_a^b e^{\lambda h_\tau(\theta)}d\theta\right)
\frac{\theta_\tau-a}{\lambda(\cot a-\tau)}e^{\lambda h_\tau(a)},\\
B(\lambda\tau/2)&\sim
\left(\int_a^b e^{\lambda h_\tau(\theta)}d\theta\right)
\frac{b-\theta_\tau}{\lambda(\tau-\cot b)}e^{\lambda h_\tau(b)}.
\end{split}
\]
Indeed, the factors \(\theta-s\) and \(s-\theta\) converge to the displayed distances at the unique interior saddle and the respective endpoint; all other portions are exponentially smaller. Consequently,
\[
\frac{A(\lambda\tau/2)}{B(\lambda\tau/2)}\sim
\frac{(\theta_\tau-a)(\tau-\cot b)}{(b-\theta_\tau)(\cot a-\tau)}
\exp\{\lambda(b-a)(\tau-\tau_*)\},
\]
uniformly near \(\tau_*\). For each fixed \(\varepsilon>0\), this ratio tends to \(0\) at \(\tau_* -\varepsilon\) and to \(+\infty\) at \(\tau_*+\varepsilon\), provided \(\varepsilon\) keeps the saddle inside \((a,b)\). Unique balancing thus forces \(\tau_\lambda=2\xi_\lambda/\lambda\to\tau_*\). Solving the last ratio equation \(A/B=1\) to the next order yields
\[
\lambda(\tau_\lambda-\tau_*)=\frac{\log(ru/(\ell v))}{b-a}+o(1)=2d_*+o(1).
\]

**4. Exact leakage coefficient.** At \(\xi_\lambda=\lambda\tau_*/2+d_*+o(1)\), the angular partition function has central saddle asymptotic
\[
Z=\int_0^\pi e^{\lambda h_{\tau_\lambda}(\theta)}d\theta
\sim e^{\lambda h_{\tau_\lambda}(\theta_{\tau_\lambda})}
\sin\theta_*\sqrt{2\pi/\lambda}.
\]
The two excluded tails are one-sided endpoint Laplace integrals:
\[
\begin{split}
\int_0^a e^{\lambda h_{\tau_\lambda}(\theta)}d\theta
&\sim\frac{e^{\lambda h_{\tau_*}(a)-2d_*a}}{\lambda u},\\
\int_b^\pi e^{\lambda h_{\tau_\lambda}(\theta)}d\theta
&\sim\frac{e^{\lambda h_{\tau_*}(b)-2d_*b}}{\lambda v}.
\end{split}
\]
Here the common factor due to the unspecified \(o(1)\) drift cancels in ratios with \(Z\). Taylor expansion at the moving saddle gives the left and right normalized contributions
\[
\frac{e^{-\lambda\Delta}}{\sqrt{\lambda}\sin\theta_*\sqrt{2\pi}}
\left(\frac{e^{2d_*\ell}}u+\frac{e^{-2d_*r}}v\right)(1+o(1)).
\]
They sum to \(1-C_\lambda(a,b)\). This proves the claimed sharp coefficient, exponent and maximizing-frequency drift. Reflection \(\theta\mapsto\pi-\theta\) proves that the symmetric interval has \(\xi_\lambda=0\) for every \(\lambda>-1\); substitution into the general coefficient gives its displayed specialization.

## Verification

The standalone numerical diagnostic `checks/sector_leakage_check.py` requires Python 3 with SciPy. Execute `python checks/sector_leakage_check.py`; it tests the exactly evaluable symmetric constants and computes unique frequency balancing roots and normalized leakages over four distinct angular intervals at four large weights, with **89 finite checks**. For example, in the asymmetric interval \((a,b)=(0.55,1.90)\), the calculated \(d_*\) is approximately \(0.23161749\), while the finite-weight optimal correction approaches this value; the ratio between observed leakage and \(K\lambda^{-1/2}e^{-\lambda\Delta}\) increases toward \(1\). Numerical experiments do not establish the all-weight uniqueness or the infinite-weight asymptotics; Steps 1–4 above are the proof.

## Relationship to prior work

The Mellin spectral multiplier and the qualitative semiclassical spectral convergence were established by Grudsky, Karapetyants and Vasilevski (2004). Rozenblum and Vasilevski (arXiv:2203.04170, first public 2022-03-08), especially their equations (2.6) and (5.1), provide a modern spectral-theorem derivation of the multiplier. Quiroga-Barranco and Sanchez-Nungaray (arXiv:2404.14582, first public 2024-04-22) derive related quasi-hyperbolic integral representations. The present addition is **not** that diagonalization nor the qualitative limit \(C_\lambda\to1\); it is the unique frequency balancing and sharp \(\lambda^{-1/2}e^{-\lambda\Delta}\) deficit with its geometric constants. The inspected principal results and relevant mathematical passages in these works did not already supply that claim. This literature comparison is not a proof of historical priority.

## Limitations

The angular interval is fixed strictly inside the upper-half-plane angular range. No claim is made for endpoint-dependent sectors, unions of disconnected intervals, general symbols, or a uniform two-parameter limit. Optimal norms are suprema and are not attained by nonzero analytic functions. Older book treatments of angular Toeplitz operators and equivalent semiclassical formulations remain a priority risk; there is no independent mathematical validation.

## References

1. S. Grudsky, A. Karapetyants and N. Vasilevski, *Dynamics of properties of Toeplitz operators on the upper half-plane: Hyperbolic case*, Bol. Soc. Mat. Mexicana 10 (2004), 119–138. Author-hosted full text: https://www.math.cinvestav.mx/~nvasilev/download.php?file=DynHyper.pdf (spectral representation in Section 2; Theorem 5.5).
2. G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited: Spectral theorem approach*, arXiv:2203.04170v1 (2022-03-08), https://arxiv.org/html/2203.04170v1 (equations (2.6), (5.1)).
3. R. Quiroga-Barranco and A. Sanchez-Nungaray, *Toeplitz operators and group-moment coordinates for quasi-elliptic and quasi-hyperbolic symbols*, arXiv:2404.14582v1 (2024-04-22), https://arxiv.org/html/2404.14582v1 (quasi-hyperbolic multiplier theorem).
4. N. L. Vasilevski, *Commutative Algebras of Toeplitz Operators on the Bergman Space*, Operator Theory: Advances and Applications 185, Birkhäuser (2008), Chapter 10; bibliographic relevance noted, full book text not inspected.
