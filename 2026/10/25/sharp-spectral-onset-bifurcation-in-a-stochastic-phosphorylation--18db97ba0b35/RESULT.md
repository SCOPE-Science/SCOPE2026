# Sharp spectral-onset bifurcation in a stochastic phosphorylation ring with an independent switch

## Finding

An eight-state phosphorylation network with an independent switching degree of freedom has **two distinct mechanisms for the onset of nonzero-frequency spectral dominance**. In particular, the zero-frequency curvature test previously available for this model is sometimes a sufficient but *not a necessary* condition for positive oscillation efficiency. There is a unique universal directionality threshold separating a continuous emergence of the dominant frequency from a jump to a strictly positive dominant frequency.

Write \(a=k_++k_-\), \(b=k_+-k_-\), \(c=a^2+b^2\), \(d=a^2-b^2\), \(E=3b^2-a^2\), and \(\theta=|b|/a\). Assume \(k_+,k_-,r>0\). Let \(\eta(r)=1-G(0)/\max_{\omega\ge0}G(\omega)\), with the exact stationary power spectrum \(G\) in the assumptions below.

If \(\theta\le 1/\sqrt3\), then \(\eta(r)=0\) for every \(r>0\). If \(\theta>1/\sqrt3\), define
\[
 A_r=4ar+c,\qquad
 B_r=4ar(E-4r^2)-2cd,\qquad
 C_r=16ar^3E-c^3,
\]
\[
 H(r)=C_r+\frac{\max\{B_r,0\}^2}{4A_r}.
\]
Then \(H\) is strictly increasing, has exactly one positive zero \(r_*\), and the following classification is *necessary and sufficient*:
\[
 \eta(r)=0\quad(0<r\le r_*),\qquad
 \eta(r)>0\quad(r>r_*).
\]

Define the zero-frequency-curvature threshold
\[
 r_0=\left(\frac{c^3}{16aE}\right)^{1/3}.
\]
Let \(z_c\in(1/3,1)\) be the unique solution of
\[
 h(z)=2^{2/3}(3z-1)^{2/3}-\frac{(1+z)^2}{3z-1}-2(1-z)=0,
\]
with \(z_c=0.910181756256864\ldots\) and \(\theta_c=\sqrt{z_c}=0.954034462824517\ldots\). The transition falls into three regimes.

* If \(1/\sqrt3<\theta<\theta_c\), then \(r_*=r_0\). Just above threshold, every global maximizing frequency tends to zero, with \(\omega_{\max}(r)\asymp(r-r_*)^{1/2}\), while \(\eta(r)\asymp(r-r_*)^2\).
* If \(\theta=\theta_c\), then still \(r_*=r_0\), but the degenerate continuous transition has \(\omega_{\max}(r)\asymp(r-r_*)^{1/4}\) and \(\eta(r)\asymp(r-r_*)^{3/2}\).
* If \(\theta_c<\theta<1\), then \(r_*<r_0\). At \(r_*\) two *different* frequencies, zero and \(\omega_*=\sqrt{B_{r_*}/(2A_{r_*})}>0\), tie for the global spectral maximum. For \(r\downarrow r_*\) from above, the positive-frequency global maximizer converges to \(\omega_*\) rather than zero, and \(\eta(r)\asymp r-r_*\). The value \(r_*\) is equivalently specified by \(B_{r_*}>0\), \(C_{r_*}<0\), and \(B_{r_*}^2+4A_{r_*}C_{r_*}=0\).

The appearance of a *finite-frequency* global maximum below the zero-frequency-curvature threshold is a genuine spectral first-order onset in this explicit Markov system; no singular thermodynamic or large-system limit is involved.

## Assumptions and scope

Consider independent stationary continuous-time Markov chains \(X_t\in\{U,T,ST,S\}\) and \(Y_t\in\{0,1\}\). The first chain makes nearest-neighbor clockwise transitions around its four-cycle at rate \(k_+\) and counterclockwise transitions at rate \(k_-\); the second switches in either direction at rate \(r\). All three rates are strictly positive. The eight-state generator is \(Q_X\otimes I_2+I_4\otimes Q_Y\). Its invariant distribution is uniform.

The observable is the number of phosphorylated sites, \(f(X,Y)=n_P(X)+Y\), with \(n_P(U)=0\), \(n_P(ST)=2\), and \(n_P(T)=n_P(S)=1\). The stationary two-sided power spectral density, with the Fourier convention \(G(\omega)=\int_{-\infty}^{\infty}\mathrm{Cov}(f(X_0,Y_0),f(X_t,Y_t))e^{-i\omega t}\,dt\), is
\[
 G(\omega)=\frac{a(c+\omega^2)}{\omega^4+2d\omega^2+c^2}+\frac{r}{4r^2+\omega^2}.
\]
This spectral formula and the model originate with Jia, arXiv:2610.23310v1, equations (31)--(33). The claimed contribution is the sharp global spectral-peak classification, not this pre-existing spectrum.

## Proof

**1. Reduction to a concave quadratic.** Put \(x=\omega^2\ge0\) and \(P(x)=x^2+2dx+c^2\). Since \(a>0\), \(d=4k_+k_->0\), and \(c>0\), all denominators below are positive. Elementary subtraction gives
\[
 G(\sqrt{x})-G(0)=\frac{ax(E-x)}{cP(x)}-\frac{x}{4r(x+4r^2)}
 =\frac{x\bigl(C_r+B_rx-A_rx^2\bigr)}{4rc(x+4r^2)P(x)}.
\]
This identity is exact, with no asymptotic approximation. If \(E\le0\), both terms of the first difference are nonpositive and the second is strictly negative for every \(x>0\), so zero frequency is the unique global maximizer. If \(E>0\), the difference is strictly negative for \(x\ge E\). Consequently its sign can be positive only on \(0<x<E\) and there is positive efficiency precisely when the concave quadratic \(F_r(x)=C_r+B_rx-A_rx^2\) is strictly positive for some \(x>0\).

**2. Exact uniqueness of the onset.** Since \(A_r>0\), the unique maximizing point of \(F_r\) on \([0,\infty)\) is \(x_v=\max\{B_r,0\}/(2A_r)\), and the corresponding maximum is \(H(r)\) above. Whenever \(B_r>0\), the inequalities \(B_r<4arE\) and \(A_r>4ar\) show \(x_v<E/2\). Thus every optimizer lies in \([0,E)\). For fixed \(x<E\),
\[
 \frac{\partial F_r(x)}{\partial r}=4a(x+12r^2)(E-x)>0.
\]
The maximum \(H(r)\) is therefore strictly increasing in \(r>0\): evaluate the larger-rate quadratic at the smaller-rate maximizer. As \(r\downarrow0\), \(H(r)\to-c^3<0\), while \(H(r)\ge F_r(0)=16ar^3E-c^3\to+\infty\). Its unique positive zero is \(r_*\). At that zero, the quadratic is nonpositive, so \(G(\sqrt{x})\le G(0)\) even if it touches zero at an interior point. For larger rates some \(x>0\) has \(F_r(x)>0\); for smaller rates none does. This proves the exact efficiency criterion.

**3. The universal directionality boundary.** The constant coefficient \(C_r\) changes sign exactly at \(r_0\). At \(r=r_0\), the maximum \(H(r_0)\) vanishes if \(B_{r_0}\le0\), and is positive if \(B_{r_0}>0\). With \(z=b^2/a^2\) and \(1/3<z<1\), direct substitution and factorization give
\[
 B_{r_0}=a^4(1+z)h(z).
\]
Here the displayed \(h\) is continuous, diverges to minus infinity as \(z\downarrow1/3\), and has \(h(1)=2^{4/3}-2>0\). Moreover,
\[
 h'(z)=2^{5/3}(3z-1)^{-1/3}+\frac{(1+z)(5-3z)}{(3z-1)^2}+2>0.
\]
There is exactly one \(z_c\in(1/3,1)\). It follows that \(r_*=r_0\) for \(\theta\le\theta_c\), whereas \(r_*<r_0\) for \(\theta>\theta_c\). In the latter case \(C_{r_*}<0\); since \(H(r_*)=0\), necessarily \(B_{r_*}>0\) and the quadratic touches zero at the strictly positive double root \(x_*=B_{r_*}/(2A_{r_*})\). Hence \(G(\sqrt{x_*})=G(0)\), and these are the only nonnegative-frequency global maximizers at the transition.

**4. Critical scaling and jump.** Let \(\delta=r-r_*>0\), \(p=48aEr_*^2>0\), \(A_*=A_{r_*}\), and \(D_*=16r_*^3c^3>0\). In the case \(\theta<\theta_c\), write \(q=-B_{r_*}>0\). Near \((x,\delta)=(0,0)\), the exact difference is \((p\delta x-qx^2+o(\delta x+x^2))/D_*\). The maximizing point satisfies \(x_{\max}\sim p\delta/(2q)\), and the spectral enhancement is \(G_{\max}-G(0)\sim p^2\delta^2/(4qD_*)\). For \(\theta=\theta_c\), \(B_{r_*}=0\), and the leading difference becomes \((p\delta x-A_*x^3)/D_*\); its optimizer obeys \(x_{\max}\sim\sqrt{p\delta/(3A_*)}\), and its enhancement is asymptotic to \(2p\sqrt{p/(3A_*)}\,\delta^{3/2}/(3D_*)\). These claims follow by localization of the global maximum: at criticality, the exact spectral difference is strictly negative away from the stated critical peak, and it tends to zero at infinity.

For \(\theta>\theta_c\), the critical spectrum has two isolated equal global peaks, at \(x=0\) and \(x=x_*>0\). Strict positivity of \(\partial_rF_r(x_*)\) ensures that, for \(\delta>0\), the winning positive peak lies near \(x_*\), and its enhancement is
\[
 G_{\max}-G(0)\sim \frac{x_*\,4a(x_*+12r_*^2)(E-x_*)}{4r_*c(x_*+4r_*^2)P(x_*)}\,\delta.
\]
Since \(G(0)>0\), the corresponding efficiency has the same positive powers of \(\delta\) as the enhancement. Taking square roots of the maximizing \(x\)-values proves all frequency exponents and the finite positive jump.

## Verification

The accompanying `VERIFY.py` reconstructs the eight-state generator independently of the published spectrum and computes its resolvent power spectrum. It also verifies the exact rational difference identity at representative parameters, the strict sign changes at the derived thresholds, the critical bias equation, the double-root crossover, and direct global-frequency maximization. Execute with Python 3 and the `numpy` and `scipy` packages:

```
python VERIFY.py
```

It passed 321 deterministic assertions in the current verification environment. For normalized rates \(a=1\), the computed threshold and curvature threshold are approximately \(r_*=0.669177368444=r_0\) at \(\theta=0.8\); \(r_*=0.631011846509<r_0=0.631041368580\) with jump frequency \(0.122337884777\) at \(\theta=0.96\); and \(r_*=0.629008743128<r_0=0.630024591837\) with jump frequency \(0.302188959758\) at \(\theta=0.99\). Finite calculations are corroboration, not proof of the global classification.

## Relationship to prior work

Chen Jia, *Fundamental Bounds on the Oscillation Efficiency of Markov Networks*, arXiv:2610.23310v1, introduces precisely this eight-state phosphorylation example and obtains its power spectrum in equation (33). Equation (34) of that work gives a **sufficient** positive-efficiency condition, equivalent to \(r>r_0\) in the present notation. That work does not state the necessary-and-sufficient condition \(r>r_*\), the stricter threshold below \(r_0\) at sufficiently high directional bias, the unique universal directionality boundary, or the three distinct onset exponents. Its general spectral-efficiency bounds alone do not supply these transition locations.

Andreas Dechant, *Thermodynamic constraints on the power spectral density in and out of equilibrium*, arXiv:2306.00417 (2023), establishes general spectral and dissipation inequalities, also discussed in Jia's article. These do not specify the present eight-state spectral maximizer or its sharp switching-rate transition. The existing exact spectrum is an essential input; the new result is the complete analysis of its *global* maximum. General rational-spectrum optimization methods remain relevant, and broader priority assessment is still needed.

## Limitations

The classification pertains only to the specified independent four-cycle and two-state switch, strictly positive rates, the three-site phosphorylation-count observable, stationarity, and the stated two-sided spectral normalization. No general conclusion is asserted for coupled switches, nonuniform ring rates, other observables, or higher-dimensional Markov networks. The stochastic system remains finite and irreducible at the jump: this is a change in the maximizing *frequency*, not a singular phase transition of the stationary Markov measure. Exact constants of the near-threshold efficiency and frequency depend on the rates, although the classification boundary in the ratio \(\theta\) is universal.

## References

1. Chen Jia, *Fundamental Bounds on the Oscillation Efficiency of Markov Networks*, arXiv:2610.23310v1, first publicly available 2026-10-16. https://arxiv.org/html/2610.23310v1 (especially equations (31)--(34) and the accompanying End Matter).
2. Andreas Dechant, *Thermodynamic constraints on the power spectral density in and out of equilibrium*, arXiv:2306.00417 (2023). https://arxiv.org/abs/2306.00417.
