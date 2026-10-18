# Two competing rotation reversals under one-coordinate resetting of a harmonic Brownian gyrator

## Finding

The stationary signed-area transport of a planar, two-thermostat harmonic diffusion responds to random resets in two distinctly measurable ways. Resetting only the first coordinate yields exact formulas for the continuous trajectory's signed twice-area rate and for the signed twice-area rate of the complete jump trajectory. The two rates undergo rotation reversals in *disjoint* ranges of bath-temperature ratios. At equal bath temperatures and every positive reset rate, their signs are opposite, even though their common nonreset limit vanishes.

Set \(\Delta=ab-c^2>0\),
\[
D(r)=2(a+b)\Delta+r(3ab+b^2-c^2)+br^2>0.
\]
For the model defined below, the stationary expected continuous signed twice-area rate is
\[
J_{\mathrm{flow}}(r)=\frac{c}{D(r)}\left[T_y r^2+2\bigl((a+b)T_y-bT_x\bigr)r+4\Delta(T_y-T_x)\right],
\]
while the complete trajectory including reset chords has rate
\[
J_{\mathrm{all}}(r)=-\frac{2c}{D(r)}\left[2\Delta(T_x-T_y)+br(2T_x-T_y)\right].
\]
The reset contribution is
\[
J_{\mathrm{jump}}=J_{\mathrm{all}}-J_{\mathrm{flow}}
=-\frac{cr(2bT_x+2aT_y+T_y r)}{D(r)}<0.
\]
Here the sign convention is counterclockwise-positive, and \(c>0\); reversing the sign of \(c\) reverses all rate signs.

The exact all-parameter sign classification is as follows.

1. For \(T_y<T_x\), \(J_{\mathrm{flow}}\) changes sign exactly once, negative to positive, at
   \[
   r_f=\frac{-h+\sqrt{h^2+4T_y\Delta(T_x-T_y)}}{T_y},\qquad h=(a+b)T_y-bT_x,
   \]
   whereas \(J_{\mathrm{all}}<0\) for all \(r>0\).
2. For \(T_y=T_x\), \(J_{\mathrm{flow}}>0\), \(J_{\mathrm{all}}<0\), and
   \[
   \frac{J_{\mathrm{all}}}{J_{\mathrm{flow}}}=-\frac{2b}{2a+r}
   \]
   for every \(r>0\).
3. For \(T_x<T_y<2T_x\), \(J_{\mathrm{flow}}>0\) for all \(r>0\), whereas \(J_{\mathrm{all}}\) changes sign exactly once, positive to negative, at
   \[
   r_a=\frac{2\Delta(T_y-T_x)}{b(2T_x-T_y)}.
   \]
4. For \(T_y\ge2T_x\), both signed-area rates are strictly positive at every \(r>0\).

For every fixed admissible parameter set,
\[
\lim_{r\to\infty}J_{\mathrm{flow}}(r)=\frac{cT_y}{b},\quad
\lim_{r\to\infty}J_{\mathrm{jump}}(r)=-\frac{cT_y}{b},\quad
\lim_{r\to\infty}J_{\mathrm{all}}(r)=0.
\]
Thus the persistent finite continuous signed-area rate at rapid resetting is canceled exactly at leading order by the area swept out along the reset chords.

## Assumptions and scope

Let \(a,b,c,T_x,T_y,r\) be finite real constants satisfying \(a>0\), \(b>0\), \(c>0\), \(ab>c^2\), \(T_x>0\), \(T_y>0\), \(r>0\). Between Poisson reset times of intensity \(r\), independent of the Brownian motions, the real-valued coordinates solve
\[
\begin{aligned}
dX_t&=-(aX_t+cY_t)\,dt+\sqrt{2T_x}\,dW^{(x)}_t,\\
dY_t&=-(cX_t+bY_t)\,dt+\sqrt{2T_y}\,dW^{(y)}_t.
\end{aligned}
\]
At each reset, the state \((X,Y)\) is replaced instantaneously by \((0,Y)\); in particular the second coordinate is not reset. The positive-definite spring matrix is \(K=\bigl(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\bigr)\). The diffusion and reset process has a unique stationary law with finite second moments.

Define the continuous time contribution, per unit time in the stationary law, as
\[
J_{\mathrm{flow}}=\mathbb E_{\mathrm{stat}}[X(-cX-bY)-Y(-aX-cY)],
\]
and the full jump-inclusive rate by the expected long-run time average of the Itô semimartingale signed-area integral
\[
J_{\mathrm{all}}=\lim_{t\to\infty}\frac1t
\mathbb E\int_{(0,t]}\left(X_{s-}\,dY_s-Y_{s-}\,dX_s\right).
\]
The jump at a reset is the straight chord from \((X,Y)\) to \((0,Y)\). Its signed twice-area contribution is \(XY\). Brownian components are independent, so there is no mixed continuous quadratic-covariation correction. These are *un-normalized signed twice-area rates*, not the mean polar angular velocity or the probability-current curl.

## Proof

**Existence and uniqueness.** Couple any two copies using the same Brownian motions and reset times. Their difference obeys \(\dot z=-Kz\) between jumps and is multiplied by the orthogonal projection \(P=\operatorname{diag}(0,1)\) at jumps. If \(\lambda_{\min}(K)>0\), then \(\|z(t)\|\le e^{-\lambda_{\min}(K)t}\|z(0)\|\). The generator also yields
\[
\mathcal L(X^2+Y^2)=-2(X,Y)K(X,Y)^{\mathsf T}+2(T_x+T_y)-rX^2,
\]
which bounds second moments and gives tight time-averaged laws. This establishes the stationary law, and the contraction proves uniqueness and convergence for initial states with finite second moments. Consequently the long-run expected area rates equal the stationary generator averages and Poisson-reset compensation terms.

**Exact stationary covariance.** Write
\(u=\mathbb E[X^2]\), \(v=\mathbb E[XY]\), and \(w=\mathbb E[Y^2]\) in stationarity. Apply the diffusion-plus-reset generator respectively to \(X^2\), \(XY\), and \(Y^2\). The three linear equations are
\[
\begin{aligned}
(2a+r)u+2cv&=2T_x,\\
cu+(a+b+r)v+cw&=0,\\
2cv+2bw&=2T_y.
\end{aligned}
\]
Their explicit solution is
\[
\begin{aligned}
u&=\frac{2[(ab+b^2+br-c^2)T_x+c^2T_y]}{D(r)},\\
v&=-\frac{c[2bT_x+(2a+r)T_y]}{D(r)},\\
w&=\frac{2c^2T_x+[2a^2+2ab+3ar+br-2c^2+r^2]T_y}{D(r)}.
\end{aligned}
\]
The denominator equals the positive quadratic displayed in the finding; positivity follows from \(a,b,r,\Delta>0\), since \(3ab+b^2-c^2=2ab+b^2+\Delta>0\).

**Continuous and jump areas.** By the definition and the drift equations,
\[
J_{\mathrm{flow}}=c(w-u)+(a-b)v.
\]
A Poisson reset changes only \(X\), by \(\Delta X=-X\). Hence the compensator of its signed-area jump is \(-Y\Delta X=XY\), contributing \(J_{\mathrm{jump}}=rv\). Substitute the displayed covariance entries and collect powers of \(r\) to obtain all three exact rational expressions in the finding.

**Sign and uniqueness of crossings.** Since \(c/D(r)>0\), the sign of \(J_{\mathrm{flow}}\) equals the sign of
\[
P_f(r)=T_y r^2+2[(a+b)T_y-bT_x]r+4\Delta(T_y-T_x).
\]
If \(T_y<T_x\), this upward-opening quadratic has negative constant and positive leading coefficient, so its two real roots have opposite signs. The positive root is \(r_f\). When \(T_y\ge T_x\), its linear coefficient is strictly positive, while the constant is nonnegative, so \(P_f(r)>0\) for every \(r>0\). Similarly the sign of \(J_{\mathrm{all}}\) is minus the sign of the affine function
\[
P_a(r)=2\Delta(T_x-T_y)+br(2T_x-T_y).
\]
For \(T_y\le T_x\), this is positive for \(r>0\). For \(T_x<T_y<2T_x\), it starts negative and crosses to positive exactly once at \(r_a\). For \(T_y\ge2T_x\), it is strictly negative for all finite \(r>0\). This proves the complete classification. The equal-bath ratio and limits at infinite resetting follow by substitution and comparison of leading polynomial coefficients.

## Verification

Execute `python verification/check.py` with Python 3 and SymPy available. The executable first verifies the generator moment identities, three exact current decompositions, equal-temperature ratio, and small/large resetting limits by exact symbolic simplification. It then independently inverts the rational coefficient matrix at 120 fixed-seed positive-rational parameter sets satisfying \(ab>c^2\), comparing their exact covariances and signed-area rates with the closed forms. All tests passed before release. Symbolic identities, not the finite sample, support the arbitrary-parameter proof.

## Relationship to prior work

Filliger and Reimann introduced the conventional two-temperature harmonic Brownian gyrator and its nonequilibrium rotation without stochastic resetting [1]. Dotsenko and collaborators treated the two-temperature harmonic stationary problem without resets [2]. Meylahn, Sabhapandit and Touchette derived resetting principles and OU time-integral fluctuation results, but their studied OU observable is a one-dimensional temporal area and their resets do not give this partial-coordinate planar signed-area law [3]. Abdoli and Sharma investigated active Brownian particles reset to a line in a Lorentz-force setting, not this symmetric coupled harmonic two-thermostat model [4]. The fractional Brownian gyrator study uses correlated noise but not these Poisson resets [5]. General partial-state reset frameworks may simplify the moment-method derivation; the claimed contribution is the evaluated pair of signed-area rates and the global, mutually exclusive reversal sectors rather than a novel resetting generator or moment-closure principle.

## Limitations

The theorem is restricted to linear overdamped two-coordinate dynamics, a positive-definite symmetric spring matrix, two independent strictly positive-temperature white-noise baths, a fixed positive Poisson reset rate, and resetting the *first coordinate alone to zero*. The two area observables are deliberately distinct. No assertion is made about winding-angle distributions, heat-engine efficiency, entropy production, spatially resolved probability currents, underdamped dynamics, or nonlinear traps. At \(r=0\) the unreset reference model is standard; the theorem concerns strictly positive reset intensity. The covariance-based area rate is not a complete characterization of the stationary distribution.

## References

[1] R. Filliger and P. Reimann, “The Brownian gyrator: a minimal heat engine on the nano-scale,” arXiv:0710.3735, initially public 19 October 2007; *Physical Review Letters* **99**, 230602 (2007). https://arxiv.org/abs/0710.3735

[2] V. Dotsenko, A. Maciołek, O. Vasilyev and G. Oshanin, “Two-temperature Langevin dynamics in a parabolic potential,” arXiv:1302.4056 (2013). https://arxiv.org/abs/1302.4056

[3] J. M. Meylahn, S. Sabhapandit and H. Touchette, “Large deviations for Markov processes with resetting,” arXiv:1510.02431 (2015). https://arxiv.org/abs/1510.02431

[4] I. Abdoli and A. Sharma, “Stochastic resetting of active Brownian particles with Lorentz force,” arXiv:2010.02103 (2020). https://arxiv.org/abs/2010.02103

[5] “Fractional Brownian Gyrator,” arXiv:2204.12145 (2022). https://arxiv.org/abs/2204.12145
