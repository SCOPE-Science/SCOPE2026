# A unique resetting-induced torque reversal in a two-bath Brownian gyrator

## Finding

Consider the two-temperature overdamped Brownian gyrator in a strictly confining, coupled harmonic well, subject to Poisson interventions that multiply **only its first coordinate** by a fixed factor. The stationary mean **conservative potential torque** reverses sign at a unique positive intervention rate if and only if the intervened coordinate has the hotter bath. This assertion includes a sharp, explicitly invertible threshold at every positive rate and every partial-reset strength strictly below one.

Define \(\delta=ab-c^2>0\), \(p=r(1-\theta)\), \(h=1+\theta\), and \(q=D_x/D_y\). The unique temperature-ratio boundary is

\[
q_*(p)=1+\frac{2p(a+b\theta)+hp^2}{4\delta+2bp}.
\]

For every \(p>0\), \(q_*(p)>1\), and \(q_*(p)\) increases strictly from one to infinity as \(p\) increases. With the orientation convention below,

\[
\operatorname{sgn}\!\left(\frac{M(r)}c\right)=\operatorname{sgn}\big(q-q_*(r(1-\theta))\big).
\]

Consequently, if \(q>1\), there is exactly one stall/reversal rate \(r_*>0\), with \(M(r)/c>0\) for \(0\le r<r_*\), \(M(r_*)=0\), and \(M(r)/c<0\) for \(r>r_*\). It is given explicitly by

\[
\begin{aligned}
B&=bq-a-bh,\\
p_*&=\frac{B+\sqrt{B^2+4h\delta(q-1)}}{h},\\
r_*&=\frac{p_*}{1-\theta}.
\end{aligned}
\]

If \(q\le1\), the sign is strictly negative for every positive resetting rate and no positive reversal occurs. No assumption that the stationary law is Gaussian is required.

## Assumptions and scope

Let \(a,b,D_x,D_y>0\), \(c\in\mathbb R\setminus\{0\}\), \(ab>c^2\), \(0\le\theta<1\), and \(r>0\). Between events the coordinates follow independent thermal noises and symmetric coupled restoring drifts,

\[
\begin{split}
dX_t&=-(aX_t+cY_t)\,dt+\sqrt{2D_x}\,dW_t^x,\\
dY_t&=-(cX_t+bY_t)\,dt+\sqrt{2D_y}\,dW_t^y.
\end{split}
\]

At independent Poisson times of rate \(r\), replace \((X,Y)\mapsto(\theta X,Y)\). The potential is \(U(x,y)=(a x^2+2cxy+b y^2)/2\). The observable is **only** the torque exerted on the confining potential,

\[
M(r)=\mathbb E_{\mathrm{stat}}[X\,\partial_yU-Y\,\partial_xU]
=c(u-v)+(b-a)w,
\]

where \(u=\mathbb E[X^2]\), \(v=\mathbb E[Y^2]\), and \(w=\mathbb E[XY]\) refer to the unique stationary law. A different sign convention multiplies all torque signs by minus one. The notation does not include the intervention device's forces, work, or impulsive angular-momentum transfer; torque sign alone is not a thermodynamic efficiency claim or a claim about local probability-current winding.

## Proof

**Stationarity.** Let \(K=\bigl(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\bigr)\), whose smallest eigenvalue \(\kappa>0\) exists by positive definiteness. For \(V=x^2+y^2\), the infinitesimal generator of the diffusion-and-jump process gives

\[
\mathcal LV=-2(x,y)K(x,y)^\top+2(D_x+D_y)+r(\theta^2-1)x^2
\le-2\kappa V+2(D_x+D_y).
\]

The resulting Foster--Lyapunov bound gives an invariant probability with finite quadratic moments. More explicitly, couple two copies with the same Brownian drivers and intervention times: between jumps their difference contracts in Euclidean norm by at least \(e^{-\kappa t}\), while the map \((x,y)\mapsto(\theta x,y)\) cannot increase that norm. Hence the Markov semigroup contracts quadratic Wasserstein distance, ruling out more than one invariant probability. The drift and jumps preserve zero as the mean; stationary linear moment equations, whose coefficient matrix is positive definite after symmetrization or directly invertible, make the stationary mean zero.

**Exact closed moment system.** Applying the generator to \(x^2,y^2,xy\) gives, at stationarity,

\[
\begin{split}
(2a+hp)u+2cw&=2D_x,\\
2bv+2cw&=2D_y,\\
c(u+v)+(a+b+p)w&=0.
\end{split}
\tag{1}
\]

Here \(r(\theta^2-1)=-hp\) supplies the first diagonal loss, and \(r(\theta-1)=-p\) supplies the mixed-moment loss. For the matrix in (1), a direct determinant calculation gives

\[
\begin{split}
\Delta&=4(a+b)\delta
+2p\bigl((h+2)ab+hb^2-hc^2\bigr)+2bhp^2\\
&=4(a+b)\delta+2p\bigl(2ab+h\delta+hb^2\bigr)+2bhp^2>0.
\end{split}
\tag{2}
\]

Thus (1) uniquely determines these moments for every admissible parameter. In particular, solving the last equation and substituting into the two diagonal equations, or using Cramer's rule, gives the exact cross moment

\[
w=-\frac{2c}{\Delta}\bigl(2aD_y+2bD_x+hpD_y\bigr).
\tag{3}
\]

Substitution into \(M=c(u-v)+(b-a)w\) and cancellation yield the exact identity

\[
\boxed{M(r)=\frac{2c}{\Delta}\left[4\delta(D_x-D_y)+2p\bigl(bD_x-(a+bh)D_y\bigr)-hD_y p^2\right].}
\tag{4}
\]

For transparency, the corresponding diagonal numerators can be reconstructed from (1), for example

\[
\begin{split}
\Delta u &=4\Bigl[\bigl(b(a+b+p)-c^2\bigr)D_x+c^2D_y\Bigr],\\
\Delta v &=2\Bigl[2c^2D_x+\bigl(2a(a+b)-2c^2+(ah+2a+bh)p+hp^2\bigr)D_y\Bigr].
\end{split}
\tag{5}
\]

Equations (3)--(5), with the positive determinant (2), are exact identities, not perturbative expansions.

**The sharp boundary.** Divide the bracket in (4) by \(D_y>0\), set \(q=D_x/D_y\), and factor it as

\[
(4\delta+2bp)\left[q-1-\frac{2p(a+b\theta)+hp^2}{4\delta+2bp}\right].
\tag{6}
\]

All factors outside the final square bracket have strictly positive sign after dividing \(M\) by \(c\), so (6) proves the stated sign criterion. Put \(A=a+b\theta>0\). A single differentiation shows

\[
\frac{d}{dp}\bigl(q_*(p)-1\bigr)
=\frac{8\delta(A+hp)+2bhp^2}{(4\delta+2bp)^2}>0.
\tag{7}
\]

The limiting boundary values are \(q_*(0)=1\) and \(q_*(p)\to\infty\) as \(p\to\infty\). Thus every \(q>1\) intersects the boundary exactly once, whereas \(q\le1\) never intersects it at positive \(p\). Solving the quadratic equation \(q=q_*(p)\) gives precisely the formula for \(p_*\) above; its second root is strictly negative when \(q>1\).

The endpoint torque identities follow directly from (2) and (4):

\[
M(0)=\frac{2c(D_x-D_y)}{a+b},\qquad
\lim_{r\to\infty}M(r)=-\frac{cD_y}{b}.
\tag{8}
\]

The first identity also follows by solving the ordinary coupled Ornstein--Uhlenbeck model without resets. Since \(0\le\theta<1\), \(p\to\infty\) with \(r\to\infty\), making the second limit legitimate. This completes the proof.

## Verification

The supplied standalone Python 3 script `verify.py` uses only standard-library exact rational arithmetic. It reconstructs all three stationary moments by independent Cramer determinants, compares both the determinant and torque formulas against (2) and (4), verifies the temperature-ratio sign test for 347 randomly sampled admissible rational systems, checks exact points on three stall curves and strict signs on both sides, checks several monotonic threshold grids, and confirms one explicit reversal example. It outputs `PASS: 347 exact rational parameter checks; stall and sign examples verified.` The code runs from this package; the proof is the algebra and inequalities above, **not** finite sampling.

As one transparent example, take \(a=b=2\), \(c=1\), \(D_x=3\), \(D_y=1\), and \(\theta=1/2\). Then \(q=3\), \(\delta=3\), and the unique stall is

\[
r_*=\frac{4(1+\sqrt{37})}{3}.
\]

The torque divided by \(c\) is positive at \(r=1\) and negative at \(r=30\). The inequality (7), not these two sample values, proves there is only one reversal.

## Relationship to prior work

Filliger and Reimann (2007) introduced the harmonic two-bath Brownian gyrator and its no-reset torque; (8) recovers that baseline. Work on partial-coordinate resetting in coupled systems, notably Olsen and Löwen (2024), derives a general moment hierarchy under a **spatial homogeneity** assumption on the free marginal propagator; their equation (4) requires translation covariance in the non-reset coordinate. A strictly confining, symmetrically coupled harmonic well does not satisfy this assumption, and that paper does not present the stationary torque phase boundary derived here.

Abdoli, Olsen, and Löwen (2024) examine resetting in shear-driven diffusion; their unconfined one-coordinate resetting problem is not stationary, and their drift and noise mechanism differ from the positive-definite two-bath trap here. Abdoli and collaborators (2021, 2025) study magnetic or shear **loads** that reverse potential torque by changing continuous dynamics, not a coordinate-only Poisson jump. These precedents establish that torque reversal can occur through other mechanisms; they do not constitute this specific partial-reset rate/temperature classification. The one-dimensional partial-reset thermodynamic work literature concerns a different observable and does not establish an angle-dependent gyrator torque law in the material that could be inspected. This is a targeted comparison, not a claim to exhaust all literature.

## Limitations

Only the stationary mean conservative **potential** torque is classified. The full nonlocal stationary density and its spatial current, the instantaneous reset device's work, total entropy production, and engine efficiency are not covered. The result assumes a symmetric positive-definite harmonic drift, independent white-noise heat baths with \(D_x,D_y>0\), and one coordinate multiplied by a nonnegative factor strictly below one. The high-rate limit at fixed \(\theta<1\) is not uniform as \(\theta\uparrow1\). A vanishing cold-bath diffusivity, a noncontractive reset factor, magnetic Lorentz forces, anisotropic mobility, or nonharmonic potentials are outside the claim. Generic jump-diffusion moment closure may independently imply pieces of the forward calculation; literature-priority risk therefore remains for an unlocated specialized study. Independent external validation has not been performed.

## References

1. R. Filliger and P. Reimann, "The Brownian gyrator: a minimal heat engine on the nano-scale," 2007, arXiv:0710.3735, https://arxiv.org/abs/0710.3735 (first public version 2007-10-19).
2. K. S. Olsen and H. Löwen, "Dynamics of inertial particles under velocity resetting," 2024, arXiv:2401.12685, https://arxiv.org/html/2401.12685v1 (especially Sec. 2, equations (1)--(5)).
3. I. Abdoli, K. S. Olsen, and H. Löwen, "Shear-Driven Diffusion with Stochastic Resetting," 2024, arXiv:2410.10333, https://arxiv.org/html/2410.10333v1 (especially Secs. II--IV and Appendix C).
4. I. Abdoli and collaborators, "Brownian magneto-gyrator as a tunable microengine," 2021, arXiv:2110.05284, https://arxiv.org/html/2110.05284v1.
5. I. Abdoli and collaborators, "Enhanced Efficiency in Shear-Loaded Brownian Gyrators," 2025, arXiv:2502.19222, https://arxiv.org/html/2502.19222v1 (Secs. II--III).
6. K. S. Olsen and D. Gupta, "Thermodynamic work of partial resetting," 2024, arXiv:2401.11919, https://arxiv.org/abs/2401.11919 (abstract inspected; full text not verified).
