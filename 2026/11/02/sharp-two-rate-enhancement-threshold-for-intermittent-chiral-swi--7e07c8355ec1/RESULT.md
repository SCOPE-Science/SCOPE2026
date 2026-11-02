# Sharp two-rate enhancement threshold for intermittent chiral swimmers

## Finding

Consider a planar particle that travels at speed \(v>0\) in its mobile state \(M\), with mobile angular diffusion \(a>0\) and angular velocity \(\omega\in\mathbb R\). In the immobile state \(S\), its position remains fixed and its continuous heading undergoes angular diffusion \(d>0\), with zero angular drift. Its Markov transition rates are \(M\to S\) at \(\beta\ge0\) and \(S\to M\) at \(\gamma>0\). The stationary per-coordinate positional diffusivity is
\[
D(\beta,\gamma)=\frac{v^2}{2}\frac{\gamma}{\beta+\gamma}\frac{a+\beta d/(\gamma+d)}{[a+\beta d/(\gamma+d)]^2+\omega^2}.
\]
This exact diffusivity is a specialization of known finite-duration reorientation formulas, not claimed as a new expression in itself.

The new classification concerns global optimization over **both** switching rates and the existence of improvement relative to never stopping. Put
\[
D_0=\frac{v^2a}{2(a^2+\omega^2)},\qquad c=d-a,\qquad
\mathcal F(z)=\frac{v^2d}{2}\frac{z}{(z+c)(z^2+\omega^2)}\quad(z\ge a).
\]
Then the exact sharp global supremum is
\[
\sup_{\beta\ge0,\,\gamma>0} D(\beta,\gamma)=\max_{z\ge a}\mathcal F(z).
\]
It is strictly greater than \(D_0\) **if and only if**
\[
\boxed{\quad d>a\quad\text{and}\quad
 |\omega|>a\sqrt{\frac{d+a}{d-a}}.\quad}
\]
If these strict inequalities fail, \(D_0\) is the global maximum and any choice \(\beta=0\) achieves it. If they hold, there is a unique \(z_*>a\) satisfying
\[
\boxed{2z_*^3+(d-a)z_*^2=(d-a)\omega^2,}
\]
and the sharp optimal value is \(\mathcal F(z_*)>D_0\). **No finite positive switching-rate pair attains this enhanced supremum**; the limit \(\gamma\to\infty\), \(\beta/\gamma\to(z_*-a)/d\) attains it asymptotically.

For fixed \(\gamma>0\), put \(b=d/(\gamma+d)\) and \(c_\gamma=b\gamma-a\). The unique maximizing stopping rate is \(\beta=0\), except if
\[
c_\gamma>0\quad\text{and}\quad c_\gamma\omega^2>a^2(c_\gamma+2a),
\]
when it is \(\beta_*=(z_\gamma-a)/b>0\), with the unique root \(z_\gamma>a\) of
\[
2z_\gamma^3+c_\gamma z_\gamma^2=c_\gamma\omega^2.
\]
In the enhanced joint regime, as \(|\omega|\to\infty\) for fixed \(a,d\) with \(d>a\),
\[
z_*\sim\left(\frac{d-a}{2}\right)^{1/3}|\omega|^{2/3},\qquad
\sup D\sim\frac{v^2d}{2\omega^2},\qquad
\frac{\sup D}{D_0}\longrightarrow\frac da.
\]
The first limit also gives the asymptotically optimal switching-rate ratio \(\beta/\gamma\sim z_*/d\). Thus the exact enhancement criterion is controlled jointly by the relative angular mixing rates and the chiral rotation, and the best protocol is a singular rapid-switching limit.

## Assumptions and scope

The two-state continuous-time chain is independent of the Brownian angular noise. In state \(M\), \(d\theta=\omega\,dt+\sqrt{2a}\,dW_t\) and \(dX_t=v(\cos\theta_t,\sin\theta_t)dt\). In state \(S\), \(d\theta=\sqrt{2d}\,dW_t\) and \(dX_t=0\). The same heading is retained at each state transition. Start the switching chain at its stationary law, with the heading uniform on the circle and independent of the chain. Define \(D=\lim_{t\to\infty}\mathbb E|X_t-X_0|^2/(4t)\), so that ordinary planar Brownian motion with covariance \(2Dt I_2\) has diffusivity \(D\). All equalities concerning the supremum allow \(\beta=0\); the nonattainment statement applies in the strict enhancement regime.

## Proof

**1. Stationary correlation and its integral.** The mobile-state equilibrium probability is \(p_M=\gamma/(\beta+\gamma)\). For the first angular harmonic, the backward generator acting on functions with state components \((M,S)\) is
\[
A=\begin{pmatrix}i\omega-a-\beta&\beta\\\gamma&-\gamma-d\end{pmatrix}.
\]
Because \(a,d>0\), this matrix has strictly left-half-plane spectrum for any \(\beta\ge0,\gamma>0\). The stationary velocity autocorrelation is
\[
C(t)=v^2p_M\operatorname{Re}(e^{At})_{MM}\quad(t\ge0).
\]
Consequently, by integrating the integrable correlation and applying the Green--Kubo identity, the per-coordinate diffusivity equals \((v^2p_M/2)\operatorname{Re}(-A^{-1})_{MM}\). Exact inversion gives
\[
(-A^{-1})_{MM}=\frac{1}{a+\beta d/(\gamma+d)-i\omega},
\]
which proves the displayed \(D(\beta,\gamma)\). Exponential decay of the stationary velocity correlation also justifies the long-time limit. Equivalently, this identity is recovered from the finite-duration-tumble formulas of Olsen and Löwen for exponential resting times and zero resting torque, with an extra factor of one half because of the coordinatewise normalization used here.

**2. A sharp joint bound and its attainability as a supremum.** Put \(z=a+\beta d/(\gamma+d)\ge a\). If \(\beta>0\), the mobile fraction satisfies the strict inequality
\[
\frac{\gamma}{\beta+\gamma}
=\frac{\gamma d}{\gamma(d+z-a)+d(z-a)}
<\frac{d}{d+z-a}.
\]
It follows that \(D(\beta,\gamma)<\mathcal F(z)\). For \(\beta=0\), equality holds at \(z=a\). Conversely, choose any fixed \(z>a\), let \(\gamma\to\infty\), and set \(\beta=(\gamma+d)(z-a)/d\). Then \(z\) stays fixed and the mobile fraction tends to \(d/(d+z-a)\), so \(D\to\mathcal F(z)\). Therefore \(\sup_{\beta,\gamma}D=\max_{z\ge a}\mathcal F(z)\); the maximum in \(z\) exists because \(\mathcal F(z)>0\) and tends to zero as \(z\to\infty\). In the strictly enhanced regime its maximizer has \(z>a\), and all finite \(\beta>0\) satisfy the strict bound, proving nonattainment.

**3. Exact maximizer and threshold.** For any constant \(c>-a\), consider \(f_c(z)=z/[(z+c)(z^2+\omega^2)]\) on \(z\ge a\). Its derivative has the sign of
\[
g_c(z)=c(\omega^2-z^2)-2z^3.
\]
If \(c\le0\), then \(-a<c\le0\), and for \(z\ge a\), \(g_c(z)\le(-c)z^2-2z^3<0\). If \(c>0\), then \(g_c'(z)=-2cz-6z^2<0\) for every \(z>0\), so there is at most one turning point in the domain and it is a strict global maximum when present. The turning point lies strictly above \(a\) precisely when \(g_c(a)>0\), namely
\[
c\omega^2>a^2(c+2a).
\]
Taking \(c=d-a\) gives the claimed necessary and sufficient joint condition, the cubic equation, and the boundary equality cases. Repeating with \(c_\gamma=b\gamma-a\) gives the fixed-\(\gamma\) classification because \(z=a+b\beta\) increases strictly with \(\beta\).

**4. Strong-chirality asymptotics.** For \(d>a\), set \(c=d-a>0\). The unique root of \(2z^3+cz^2=c\omega^2\) obeys \(z\sim(c\omega^2/2)^{1/3}\) as \(|\omega|\to\infty\), since \(z\to\infty\) but \(z/|\omega|\to0\). Substitution in \(\mathcal F\) gives \(\sup D\sim v^2d/(2\omega^2)\), while \(D_0\sim v^2a/(2\omega^2)\). The optimizer's fast-switching ratio follows from the construction in Step 2.

## Verification

A standalone checker, `verify.py`, independently evaluates the complex-harmonic generator resolvent, numerically integrates matrix-exponential velocity correlations, symbolically reconstructs the derivative polynomial, compares optimizers with direct constrained numerical optimization, tests rigorous supremum bounds and their fast-switching approach, and checks the two-thirds scaling and strict phase boundary. All 160 reported checks passed. They support algebra and normalization; the proof above, rather than finite sampling, establishes the universal statements.

## Relationship to prior work

Peruani and Chaudhuri's stop-and-go models (arXiv:2306.05647, first posted 9 June 2023) distinguish how angular memory behaves during active and inactive periods. In particular, their model 4 derives diffusivity for nonchiral motion that randomizes the heading during stops. Olsen and Löwen (arXiv:2405.14326, first posted 23 May 2024) derive the general chiral diffusivity with finite-duration reorientations and examine enhancement diagrams. Their Eqs. (30), (53)--(55) include the exact diffusivity above as a specialization. The present result does **not** claim a new Green--Kubo identity or a new diffusion formula. The assessed additional theorem is a complete sharp joint two-rate enhancement criterion, classification of boundary and interior optima, nonattainment by any finite pair in the enhanced regime, and the universal optimized high-chirality scaling.

Perez Ipiña and collaborators (Nature Physics 2019; arXiv:1912.11835) demonstrate optimal stop frequency in a distinct three-state bacteria/surface-adhesion model. They do not establish the stated global two-rate sharp threshold for this two-state Brownian-angle model. This theorem concerns diffusivity, not search success, biological fitness, or parameter-inference identifiability.

## Limitations

The model assumes exponential mobile and stop sojourns, no angular drift during pauses, independent Gaussian angular fluctuations, no translational Brownian noise, and unlimited ability to increase both switching rates. The enhanced joint supremum is a singular limit and should not be described as physically attained at finite switching rates. A switching-rate cost, minimal dwell time, non-exponential waits, or nonzero stop torque can change the phase diagram. The long-time diffusivity is not the finite-time exploration area or a hitting-time optimum. The broader exact diffusion formula is already published; novelty priority for the **additional optimization classification** still requires independent expert and exhaustive bibliographic review.

## References

1. F. Peruani and D. Chaudhuri, *Active stop and go motion: a strategy to improve spatial exploration and survival*, arXiv:2306.05647v1 (9 June 2023); revised preprint arXiv:2306.05647v2 (2025). https://arxiv.org/abs/2306.05647
2. K. Stølevik Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326v1 (23 May 2024), Sec. V and Eqs. (30), (53)--(55); v2 (16 October 2024). https://arxiv.org/html/2405.14326v2
3. E. Perez Ipiña, S. Otte, R. Pontier-Bres, D. Czerucka, and F. Peruani, *Bacteria display optimal transport near surfaces*, Nature Physics 15 (2019), 610--615. https://doi.org/10.1038/s41567-019-0460-5 ; https://arxiv.org/abs/1912.11835
