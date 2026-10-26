# Exact stationary kurtosis and the chirality-reversal threshold in a trapped active Brownian swimmer

## Finding
Consider a planar active Brownian swimmer in an isotropic harmonic trap whose angular drift reverses sign at independent Poisson times. Its stationary Cartesian excess kurtosis admits an exact rational formula and a complete sign classification. In particular, the sign of the large-angular-speed kurtosis changes precisely when the chirality-switching rate equals one quarter of the trap relaxation rate. Above this rate there is exactly one kurtosis zero for every rotational diffusivity; below it, a genuine negative–positive–negative reentrant sequence occurs for sufficiently strong rotational diffusion.

In dimensionless parameters \(d\geq0\), \(g>0\), \(w>0\), write \(u=w^2\), \(a=1+d+2g\), and
\[
\begin{aligned}
L_1&=(1+d)a+u,\\
L_2&=u+d^2+2dg+6d+6g+9,\\
L_3&=u+4d^2+2dg+4d+g+1,\\
A&=(7d+3)a^2(d+2g+3)(2d+g+1),\\
B&=-a(10d^2-7dg-2d-14g^2-27g-10),\\
P(u)&=A+Bu+(1-4g)u^2.
\end{aligned}
\]
The normalized excess kurtosis of either stationary Cartesian coordinate is
\[
\boxed{\mathcal K(d,g,w)=-\frac{3P(w^2)}{2a^2L_2L_3}.}
\]
All denominators here are strictly positive. Therefore:

1. If \(g>1/4\), there is exactly one positive zero, located at
   \[
   u_* = \frac{B+\sqrt{B^2+4(4g-1)A}}{2(4g-1)},
   \]
   with \(\mathcal K<0\) for \(0<w<\sqrt{u_*}\) and \(\mathcal K>0\) for \(w>\sqrt{u_*}\).
2. If \(g=1/4\), a positive zero exists exactly when \(B<0\), in which case \(u_*=-A/B\) and the sign changes from negative to positive. Otherwise \(\mathcal K<0\) at every finite positive \(w\).
3. If \(0<g<1/4\), two distinct positive zeros exist exactly when \(B<0\) and \(\Delta=B^2-4(1-4g)A>0\). Between these zeros \(\mathcal K>0\), and outside them \(\mathcal K<0\). If \(B<0\) and \(\Delta=0\), the kurtosis touches zero at one positive \(u\) but never becomes positive. In all other cases it is negative throughout.

For every fixed \(0<g<1/4\), sufficiently large \(d\) produces two positive zeros satisfying
\[
\frac{u_-}{d^2}\longrightarrow\frac75,
\qquad
\frac{u_+}{d^3}\longrightarrow\frac{10}{1-4g}
\qquad(d\to\infty).
\]
At fixed \(d\) and \(g\), the exact high-chirality limit is
\[
\boxed{\lim_{w\to\infty}\mathcal K(d,g,w)=\frac{3(4g-1)}{2(1+d+2g)^2}.}
\]
These results distinguish chirality *reversal* (flipping angular velocity) from propulsion-direction reversal (flipping the active velocity), which defines a different stochastic process.

## Assumptions and scope
The dimensional dynamics are
\[
\mathrm d Z_t=(-\kappa Z_t+v e^{i\theta_t})\,\mathrm dt,\qquad
\mathrm d\theta_t=\omega\sigma_t\,\mathrm dt+\sqrt{2D}\,\mathrm dW_t.
\]
Here \(Z_t\in\mathbb C\), \(\kappa,v,\omega,\gamma>0\), \(D\geq0\), \(W_t\) is standard Brownian motion, and the independent, symmetric two-state Markov chain \(\sigma_t\in\{-1,1\}\) flips sign at rate \(\gamma\) from either state. There is no translational Brownian noise. Work in dimensionless time \(\tau=\kappa t\) and dimensionless position \(z=(\kappa/v)Z\), with \(d=D/\kappa\), \(g=\gamma/\kappa\), and \(w=\omega/\kappa\).

Take the stationary rotationally invariant law, which exists by the exponentially stable position convolution. In that law \(\theta\) is uniform modulo \(2\pi\), chirality is symmetric, and \(|z|\leq1\) almost surely. The Cartesian excess kurtosis is well-defined because the second moment is strictly positive. The statements concern this stationary law and the specified linear trap, not transient motion, nonlinear confinement, or higher spatial dimensions.

## Proof
**Stationary construction and symmetries.** In rescaled time the bounded stationary convolution is
\[
z_0=\int_{-\infty}^0 e^s e^{i\theta_s}\,\mathrm ds.
\]
Its absolute value is at most one. The stationary angular process with positive switching rate and positive angular speed has a uniform angular marginal and is rotation invariant jointly with the convolution. Thus \(\mathbb E[z]=0\) and \(\mathbb E[(\operatorname{Re}z)^2]=\mathbb E[|z|^2]/2\), while \(\mathbb E[(\operatorname{Re}z)^4]=3\mathbb E[|z|^4]/8\).

**Exact moment recursion.** Define, for integers \(p,q\geq0\) and \(s\in\{0,1\}\),
\[
M_{pq}^{(s)}=\mathbb E\big[z^p\overline z^{\,q}e^{i(q-p)\theta}\sigma^s\big].
\]
Set \(k=q-p\) and \(c=p+q+dk^2\). Applying the stationary Markov generator to these bounded observables gives
\[
\begin{aligned}
cM_{pq}^{(0)}-ikwM_{pq}^{(1)}&=pM_{p-1,q}^{(0)}+qM_{p,q-1}^{(0)},\\
(c+2g)M_{pq}^{(1)}-ikwM_{pq}^{(0)}&=pM_{p-1,q}^{(1)}+qM_{p,q-1}^{(1)}.
\end{aligned}
\]
A term with a negative index is omitted, and \(M_{00}^{(0)}=1\), \(M_{00}^{(1)}=0\). For \(p+q>0\) the determinant is
\[
c(c+2g)+k^2w^2>0,
\]
so this triangular system uniquely computes every mixed moment of bounded order. Iterating to \((p,q)=(1,1)\) and \((2,2)\) yields the exact identities
\[
\mathbb E|z|^2=\frac{a}{L_1},\qquad
\mathbb E|z|^4=\frac{2a^2L_2L_3-P(u)}{L_1^2L_2L_3}.
\]
Consequently
\[
\mathcal K=\frac{\mathbb E[(\operatorname{Re}z)^4]}{\mathbb E[(\operatorname{Re}z)^2]^2}-3
=\frac32\frac{\mathbb E|z|^4}{(\mathbb E|z|^2)^2}-3
=-\frac{3P(u)}{2a^2L_2L_3}.
\]
The exact rational identities are independently replayable with the attached symbolic checker `verify.py`.

**Root classification.** Since \(A>0\), the polynomial \(P\) is positive at \(u=0\). For \(g>1/4\), its leading coefficient is negative and the product of its two roots is negative, so it has exactly one positive root, as displayed. At \(g=1/4\), it is linear. For \(0<g<1/4\), the leading coefficient is positive and both roots are positive and distinct precisely when their sum is positive (\(B<0\)) and their discriminant is strictly positive. Equality in the discriminant gives a double root. The signs of \(\mathcal K\) are opposite those of \(P\), proving the full classification.

**Asymptotic reentrance.** At fixed \(0<g<1/4\), as \(d\to\infty\), direct expansion gives
\[
A=14d^5+O(d^4),\qquad B=-10d^3+O(d^2),\qquad
\Delta=100d^6+O(d^5)>0.
\]
Therefore two positive roots exist eventually. Their sum is \(-B/(1-4g)\) and their product is \(A/(1-4g)\); comparison of orders gives the two asymptotic formulas. Finally \(L_2L_3\sim u^2\) proves the high-frequency limit.

## Verification
Run `python verify.py` with Python 3 and SymPy. It rebuilds the Markov-generator recurrences, simplifies their second and fourth stationary moments exactly, and checks the claimed kurtosis polynomial as an identity in all three parameters. Exact-rational sign checks verify a reentrant example \((d,g)=(10,1/10)\) at \(w=0,30,200\) (the \(w=0\) value is only a continuous boundary test) and a single-crossing example \((d,g)=(0,1)\) at \(w=5,10\). An independent event-driven numerical check for \((d,g,w)=(0,1,10)\), using 150,000 independent paths over 20 relaxation times, gave sample excess kurtosis about \(0.213\), against the exact stationary value about \(0.205\); finite sampling does not constitute the proof.

## Relationship to prior work
Das and Basu (2023) introduced chirality-reversing active Brownian motion and investigated its unconfined displacement laws and time regimes. The present result adds isotropic harmonic confinement and determines an exact stationary fourth-moment sign diagram. Chaudhuri and Dhar (2020) computed trapped nonchiral active Brownian moments. Pattanayak and collaborators (2025, 2026) analyze non-switching chiral or torque-driven particles in harmonic traps and report kurtosis crossovers, including reentrant phenomena. Therefore neither reentrance *per se* nor the non-switching-chirality limit is claimed as new. The mathematical distinction is the positive-rate Markov switching of the angular drift and its \(g=1/4\) threshold.

## Limitations
The classifications concern a stationary **Cartesian** kurtosis, not a global distribution-shape theorem or a thermodynamic phase transition. The position support is compact; positive excess kurtosis is relative to a Gaussian baseline, not evidence of power-law tails. Finite simulation does not prove exact identities. The full text of one closely related 2025 constant-chirality paper could not be examined; its accessible abstract and later full-length account identify a non-switching model, but this leaves a residual literature-equivalence risk. Higher moments, translational noise, anisotropic traps, and nonlinear forces are not covered. Independent mathematical review has not been performed.

## References
1. S. Das and U. Basu, *Chirality Reversing Active Brownian Motion in Two Dimensions*, arXiv:2301.11194v1 (first public 2023-01-26), https://arxiv.org/abs/2301.11194.
2. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234v2 (2020), https://arxiv.org/abs/2005.14234.
3. A. Pattanayak, A. Shee, D. Chaudhuri, and A. Chaudhuri, *Impact of chirality on active Brownian particle: Exact moments in two and three dimensions*, arXiv:2404.09650 (2024), https://arxiv.org/abs/2404.09650.
4. A. Pattanayak, A. Shee, D. Chaudhuri, and A. Chaudhuri, *Chirality, confinement and dimensionality govern re-entrant transitions in active matter*, arXiv:2509.03448 (2025), https://arxiv.org/abs/2509.03448.
5. A. Pattanayak, A. Shee, A. Chaudhuri, and D. Chaudhuri, *Exact dynamics and dimensional effects in torque-driven trapped active Brownian particles*, arXiv:2603.26967v2 (2026), https://arxiv.org/abs/2603.26967.
