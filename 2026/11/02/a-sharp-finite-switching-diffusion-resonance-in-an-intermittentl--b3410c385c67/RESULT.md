# A sharp finite-switching diffusion resonance in an intermittently motile chiral swimmer

## Finding

An intermittently swimming particle can explore space fastest at a **finite** chirality-switching rate even though its stationary fraction of time spent swimming is independent of that rate. In the exactly specified two-state model below, the existence of such a finite optimum has a sharp asymmetry threshold, and its location diverges with an exact inverse-distance law at the threshold.

Fix rotational diffusivity \(D_R>0\), angular-speed magnitude \(\Omega>D_R\), propulsion speed \(v>0\), a relative deactivation factor \(r\ge1\), and a kinetic scale \(\lambda>0\). The particle is motile in state \(+\), with planar velocity \(v(\cos\Theta_t,\sin\Theta_t)\), and has zero propulsion in state \(-\). Its state switches \(+\to-\) at rate \(r\lambda\) and \(-\to+\) at rate \(\lambda\). Its angular velocity is \(+\Omega\) when motile and \(-\Omega\) when resting, with independent rotational Brownian noise of diffusivity \(D_R\). Optional independent translational Brownian diffusion has coefficient \(D_T\ge0\).

Write \(x=\lambda/D_R\), \(y=\Omega/D_R>1\), and
\[
U=1+y^2+(r+1)x,\qquad V=y(r-1)x,\qquad
F_{r,y}(x)=\frac{(1+x)U+y^2(r-1)x}{U^2+V^2}.
\]
Then the exact long-time diffusion coefficient is
\[
\boxed{D_{\mathrm{eff}}(\lambda)=D_T+\frac{v^2}{2D_R(r+1)}F_{r,y}(x).}
\]
Define the sharp asymmetry threshold
\[
\boxed{r_c(y)=\frac{y^2+2y-1}{1+y^2}>1.}
\]
If \(1\le r\le r_c(y)\), the effective diffusivity is strictly increasing in \(\lambda\) and has no finite maximizer. If \(r>r_c(y)\), it strictly increases to one **unique global maximum** at a finite \(\lambda_*=D_R x_*\), then strictly decreases. With
\[
\begin{aligned}
a_0&=(1+y^2)^2(y^2-1),\\
a_1&=-2(1+y^2)\big((r+1)+(r-3)y^2\big),\\
a_2&=4y^2-\big((r+1)+(r-1)y^2\big)^2<0,
\end{aligned}
\]
the unique optimum is the positive root
\[
\boxed{x_*=\frac{2a_0}{\sqrt{a_1^2-4a_2a_0}-a_1}.}
\]
At the threshold, the optimum escapes to infinity at the sharp rate
\[
\boxed{x_*(r,y)\sim\frac{y-1}{r-r_c(y)}\quad\text{as }r\downarrow r_c(y)\text{ from above}.}
\]
For the natural exact check \(y=2\), \(r=2\), the optimum is \(x_*=5/3\), where the active contribution is \(v^2/(20D_R)\), as compared with \(v^2/(30D_R)\) for vanishing switching and \(v^2/(26D_R)\) in the infinitely rapid switching limit.

## Assumptions and scope

Let \(S_t\in\{+,-\}\) be the stationary two-state continuous-time Markov chain with generator
\[
Q=\begin{pmatrix}-r\lambda&r\lambda\\\lambda&-\lambda\end{pmatrix},
\qquad \pi=\left(\frac1{r+1},\frac r{r+1}\right).
\]
Take independent standard scalar Brownian motion \(B_t\), optional independent planar Brownian motion \(W_t\), and initial \(\Theta_0\) uniform on \([0,2\pi)\), independent of \(S_0\). With \(\sigma_+=1\), \(\sigma_-=-1\), define
\[
 d\Theta_t=\Omega\sigma_{S_t}\,dt+\sqrt{2D_R}\,dB_t,\qquad
 d\mathbf R_t=v\mathbf1_{\{S_t=+\}}(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2D_T}\,dW_t.
\]
The diffusion coefficient means the scalar isotropic limit \(\lim_{t\to\infty}\mathbb E|\mathbf R_t-\mathbf R_0|^2/(4t)\). For any prescribed initial angular/state distribution, the same limit holds because \(D_R>0\) gives exponential orientational-memory decay and the switching chain is irreducible for \(\lambda>0\). Here the stationary preparation makes the Green--Kubo derivation immediate. The \(\lambda\downarrow0\) endpoint is the limiting stationary mixture, not a unique stationary law at exactly zero switching. The theorem holds for all real \(D_R,v>0\), \(D_T\ge0\), \(\Omega>D_R\), \(r\ge1\), and \(\lambda>0\); it does not assert the same threshold outside these inequalities.

## Proof

Write \(C(t)=\mathbb E[\mathbf V_0\cdot\mathbf V_t]\) for the stationary propulsion-velocity correlation, where \(\mathbf V_t=v\mathbf1_{\{S_t=+\}}(\cos\Theta_t,\sin\Theta_t)\). Conditioning on the switching path and using Brownian increments gives
\[
C(t)=\frac{v^2}{r+1}\operatorname{Re}\left[e^{tM}\right]_{++},\qquad
M=\begin{pmatrix}-D_R-r\lambda+i\Omega&r\lambda\\\lambda&-D_R-\lambda-i\Omega\end{pmatrix}.
\]
The real part of the generator for angular correlations is exponentially stable because the symmetric Markov generator is dissipative in its stationary weighted inner product and \(D_R>0\). Consequently the Green--Kubo integral converges absolutely. Stationarity and Fubini's theorem imply
\[
D_{\mathrm{eff}}-D_T=\frac12\int_0^\infty C(t)\,dt
=\frac{v^2}{2(r+1)}\operatorname{Re}\big[(-M)^{-1}\big]_{++}.
\]
A direct inverse gives
\[
\big[(-M)^{-1}\big]_{++}=\frac{D_R+\lambda+i\Omega}{D_R^2+\Omega^2+D_R(r+1)\lambda+i\Omega(r-1)\lambda}.
\]
Taking the real part and scaling by \(D_R\) gives the stated expression for \(D_{\mathrm{eff}}\).

To optimize, let \(P=(1+x)U+y^2(r-1)x\) and \(H=U^2+V^2>0\). Exact polynomial differentiation and factorization give
\[
P'H-PH'=r\,[a_0+a_1x+a_2x^2].
\]
For \(y>1\) we have \(a_0>0\). The quantity \(K(r)=(r+1)+(r-1)y^2\) is increasing for \(r\ge1\), and \(K(r_c)=2y\). Thus \(a_2\ge0\) exactly when \(r\le r_c\). Moreover \((r+1)+(r-3)y^2\) increases in \(r\), and at \(r_c\) it is \(-2y(y-1)<0\). Hence \(a_1>0\) whenever \(r\le r_c\). All derivative coefficients are then nonnegative, with \(a_0>0\), proving strict increase.

If \(r>r_c\), then \(a_2<0\) while \(a_0>0\), so the quadratic derivative numerator has exactly one positive and one negative real root. It is positive before its positive root and negative thereafter; therefore the positive root is the unique global maximizer. The quadratic formula, rationalized to avoid cancellation, yields the stated \(x_*\).

Finally, as \(r\downarrow r_c\) from above,
\[
a_1\longrightarrow4y(1+y^2)(y-1),\qquad
 a_2=-4y(1+y^2)(r-r_c)+O((r-r_c)^2).
\]
Since the positive root tends to infinity, its dominant balance \(a_1x_*+a_2x_*^2=0\) proves the claimed sharp asymptotic. Substitution of \(y=r=2\) yields
\[
D_{\mathrm{eff}}-D_T=\frac{v^2}{D_R}\frac{3x^2+12x+5}{6(13x^2+30x+25)},\qquad
\frac{d}{dx}\left(\frac{3x^2+12x+5}{6(13x^2+30x+25)}\right)
=-\frac{(3x-5)(11x+15)}{3(13x^2+30x+25)^2},
\]
which verifies the exact example and all its boundary values.

## Verification

The accompanying `verify.py` independently integrates the two-state matrix-exponential velocity correlation rather than using the displayed rational inverse, and checks agreement with the closed formula for an array of positive parameters. It also symbolically reproduces the differentiated-polynomial identity and exact rational example, probes monotone and unimodal parameter regimes, and checks the near-threshold inverse-distance limit. Execute `python verify.py` with `numpy`, `scipy`, and `sympy` installed. The recorded run passed 1,478 checks. These numerical experiments test but cannot replace the proof for infinitely many real parameter values.

## Relationship to prior work

Weber, Sokolov and Schimansky-Geier (2012) studied asymmetric dichotomous angular driving **at constant swimming speed**, deriving effective diffusion and nonmonotone effects; neither generic nonmonotonicity nor the Green--Kubo method is claimed here as novel. Nourhani, Ebbens, Gibbs and Lammert (2016) analyzed chiral reversals in constant-speed rotating self-propellers. Das and Basu (2023) also treated constant-speed chirality-reversing active Brownian particles. Jamali (2020 preprint, revised 2025) studied a two-speed active/passive particle with angular Brownian motion **independent** of the motility state; the 2021 bacterial-motility work analyzed speed fluctuations and chirality without this coupled two-state kinetic mechanism. The specific result assessed here is the correlation-induced, occupancy-preserving on/off *rate-asymmetry phase boundary*, uniqueness of a finite optimum, and its sharp escape asymptotic. Searching for related models does not certify historical priority.

## Limitations

The result concerns long-time diffusion, not finite-time search performance, survival probabilities, or interacting particles. It assumes fixed opposite angular velocities in the two propulsion states, constant \(D_R>0\), Poisson switching, and the restricted sector \(\Omega>D_R\), \(r\ge1\). The 2012 constant-speed asymmetric angular-driving study was available as abstract/metadata but its complete text was not accessible here, leaving a residual historical-priority risk. No independent validation is claimed.

## References

1. C. Weber, I. M. Sokolov and L. Schimansky-Geier, *Active particles forced by an asymmetric dichotomous angle drive*, Physical Review E 85, 052101 (2012), arXiv:1205.3419, https://doi.org/10.1103/PhysRevE.85.052101 (first publicly submitted 2012-05-15).
2. A. Nourhani, S. J. Ebbens, J. G. Gibbs and P. E. Lammert, *Spiral diffusion of rotating self-propellers with stochastic perturbation*, Physical Review E 94, 030601 (2016), arXiv:1607.00587, https://doi.org/10.1103/PhysRevE.94.030601 (first publicly submitted 2016-07-03).
3. S. Das and U. Basu, *Chirality Reversing Active Brownian Motion in Two Dimensions*, Journal of Statistical Mechanics 063205 (2023), arXiv:2301.11194, https://arxiv.org/abs/2301.11194.
4. T. Jamali, *Active-Passive Brownian Particle in Two Dimensions*, arXiv:2012.14155 (first submitted 2020-12-28; revised version inspected), https://arxiv.org/abs/2012.14155.
5. *Statistics of pathogenic bacteria in the search of host cells*, Nature Communications (2021), https://doi.org/10.1038/s41467-021-22156-6.
