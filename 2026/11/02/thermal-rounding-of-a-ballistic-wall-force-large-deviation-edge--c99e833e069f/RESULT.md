# Thermal rounding of a ballistic wall-force large-deviation edge

## Finding

The long-time large deviations of the *difference* between the two wall impulses in a hard one-dimensional box are independent of the box width, even though each wall's mean contact and fluctuation laws depend on confinement. In a thermally diffusing run-and-tumble gas, the scaled cumulant generating function of the right-minus-left regulator is

\[
\Lambda_D(q)=Dq^2-\lambda+\sqrt{\lambda^2+v^2q^2}.
\]

For zero translational diffusivity, the force-imbalance rate function ends at a ballistic current \(|j|=v\), with value \(\lambda\). Any positive translational diffusivity removes that compact support. The small-diffusivity resolution of the ballistic boundary is a singular two-thirds-width, one-third-height layer:

\[
I_D(v+\delta_D s)=\lambda+E_D\Phi(s)+o(E_D),\qquad
\delta_D=\left(\frac{\lambda^2D^2}{v}\right)^{1/3},\quad
E_D=\left(\frac{\lambda^4D}{v^2}\right)^{1/3},
\]

uniformly for \(s\) in compact subsets of \(\mathbb R\), where

\[
\Phi(s)=\sup_{z>0}\left(sz-z^2-\frac1{2z}\right).
\]

The unique maximizer \(z_s>0\) obeys \(2z_s-(2z_s^2)^{-1}=s\). In particular,

\[
I_D(v)=\lambda-\frac{3}{2^{4/3}}\left(\frac{\lambda^4D}{v^2}\right)^{1/3}+o(D^{1/3}).
\]

The result applies symmetrically near \(j=-v\). The newly identified component is the *thermal rounding and its exact scaling profile* for the signed wall-impulse observable, not the known free telegraph cumulant formula or the previously established second-cumulant wall sum rule.

## Assumptions and scope

Fix \(L,v,\lambda>0\) and \(D\ge0\). Let \((\sigma_t)_{t\ge0}\) take values \(\pm1\), flipping at independent Poisson times of rate \(\lambda\). The initial sign is stationary, with equal probabilities, and independent of standard Brownian motion \(W\). For any initial position \(X_0\in[0,L]\), the two-sided, normal-reflection Skorokhod equation is

\[
X_T=X_0+v\int_0^T\sigma_t\,dt+\sqrt{2D}W_T+U_T-R_T,\qquad0\le X_T\le L,
\]

where \(U\) and \(R\) are continuous nondecreasing regulators increasing only at the left and right walls. At \(D=0\), this is the standard outward-sticking run-and-tumble reflection. Define the signed *kinematic* impulse and time-averaged current by

\[
S_T=R_T-U_T,\qquad J_T=S_T/T.
\]

If the overdamped mobility is \(\mu>0\), the signed physical impulse is \(S_T/\mu\); its scaled generating function is obtained by replacing \(q\) by \(q/\mu\). Long-time and small-\(D\) limits are taken in that order. The assertions concern the net difference, not the marginal force at either wall.

A good speed-\(T\) large-deviation principle means that for every closed \(F\) and open \(G\), the usual upper and lower exponential probability bounds hold with rate \(I_D\). For \(D>0\), \(I_D\) is finite, strictly convex and smooth on \(\mathbb R\). For \(D=0\), it is finite on the whole closed interval \([-v,v]\), including its endpoints, and infinite outside.

## Proof

**1. Bounded-reflection identity.** Write the free displacement \(A_T=v\int_0^T\sigma_t\,dt+\sqrt{2D}W_T\). The reflection equation gives

\[
S_T=A_T-(X_T-X_0),\qquad |S_T-A_T|\le L.
\]

Consequently for every \(q\in\mathbb R\) and finite \(T>0\),

\[
e^{-|q|L}\,\mathbb E e^{qA_T}
\le\mathbb E e^{qS_T}
\le e^{|q|L}\,\mathbb E e^{qA_T}.
\]

Dividing logarithms by \(T\) proves equality of all existing free and wall scaled cumulant generating functions. More strongly, \(S_T/T\) and \(A_T/T\) are *deterministically exponentially equivalent* at speed \(T\), since their difference is at most \(L/T\). Thus every good LDP for the free current transfers to the wall current unchanged, without an eigenproblem for its two boundary contacts. This general observation also holds for any integrable autonomous propulsion path \(V_t\) independent of the Brownian noise, whenever the relevant free-current LDP exists.

**2. Exact telegraph tilted eigenvalue.** In the stationary initial sign law, the finite-time moment generating function factorizes exactly:

\[
\mathbb E e^{qA_T}
=e^{Dq^2T-\lambda T}
\left[\cosh(T\omega_q)+\frac{\lambda}{\omega_q}\sinh(T\omega_q)\right],
\qquad \omega_q=\sqrt{\lambda^2+v^2q^2}.
\]

Indeed, the tilted two-state generator is

\[
\begin{pmatrix}-\lambda+vq&\lambda\\\lambda&-\lambda-vq\end{pmatrix},
\]

whose eigenvalues are \(-\lambda\pm\omega_q\); Brownian independence adds \(Dq^2\). The factor multiplying the dominant exponential is strictly positive for every real \(q\). Combining this with Step 1 gives

\[
\lim_{T\to\infty}T^{-1}\log\mathbb E e^{qS_T}
=\Lambda_D(q)=Dq^2-\lambda+\omega_q.
\]

Neither \(X_0\) nor \(L\) appears in the limit.

**3. Global rate functions and boundaries.** For \(D>0\), \(\Lambda_D\) is differentiable on \(\mathbb R\) and steep: \(\Lambda_D'(q)\to\pm\infty\) as \(q\to\pm\infty\). The Gärtner–Ellis theorem and Step 1 give the full good LDP with

\[
I_D(j)=\sup_{q\in\mathbb R}\{qj-\Lambda_D(q)\}.
\]

Since \(\Lambda_D''(q)=2D+v^2\lambda^2/(\lambda^2+v^2q^2)^{3/2}>0\), its optimizer is the unique real solution of

\[
j=2Dq+\frac{v^2q}{\sqrt{\lambda^2+v^2q^2}}.
\]

For \(D=0\), this Legendre transform is

\[
I_0(j)=
\begin{cases}
\lambda\left[1-\sqrt{1-(j/v)^2}\right],&|j|\le v,\\
+\infty,&|j|>v.
\end{cases}
\]

The differentiable Gärtner–Ellis theorem gives the lower bound for every exposed current \(|j|<v\) and the upper bound everywhere; the support bound \(|S_T/T|\le v+L/T\) ensures exponential tightness. At \(j=v\) and \(j=-v\), starting with the corresponding sign and experiencing no orientation flips during \([0,T]\) has probability \(e^{-\lambda T}/2\). On those events the signed wall-current differs from \(\pm v\) by at most \(L/T\). Therefore every neighborhood of either endpoint has the required lower-bound exponent \(-\lambda=-I_0(\pm v)\). This completes the full LDP including endpoints.

**4. Uniform small-noise boundary layer.** Put

\[
E_D=\left(\frac{\lambda^4D}{v^2}\right)^{1/3},\quad
\delta_D=\left(\frac{\lambda^2D^2}{v}\right)^{1/3},\quad
Q_D=\left(\frac{\lambda^2}{vD}\right)^{1/3}.
\]

These are chosen so that \(DQ_D^2=E_D\), \(\delta_DQ_D=E_D\), and \(\lambda^2/(vQ_D)=E_D\). For \(j_D=v+\delta_Ds\), the strictly increasing optimizer equation in Step 3, with \(q=Q_Dz\), becomes

\[
s=2z-\frac{1}{2z^2}+O(D^{2/3})
\]

uniformly whenever \(z\) lies in a compact positive interval. Since \(z\mapsto2z-1/(2z^2)\) increases continuously from \(-\infty\) to \(+\infty\), each real \(s\) has a unique positive solution \(z_s\), and the exact optimizer satisfies \(q_D=Q_D(z_s+o(1))\). On compact \(s\)-sets, these solutions stay in one compact positive interval, giving uniform convergence of the optimizer ratios.

For large positive \(q\), the elementary square-root expansion gives

\[
\sqrt{\lambda^2+v^2q^2}
=vq+\frac{\lambda^2}{2vq}+O(q^{-3}).
\]

The maximization identity, the above scaling relations and \(q_D\asymp D^{-1/3}\) yield uniformly on compact \(s\)-sets

\[
I_D(j_D)
=\lambda+E_D\left(sz_s-z_s^2-\frac1{2z_s}\right)+o(E_D).
\]

This is the stated \(\Phi(s)\). At \(s=0\), \(z_0=4^{-1/3}\) and \(\Phi(0)=-3/2^{4/3}\), proving the explicit one-third-power deficit. Symmetry gives the negative edge. The proof requires taking \(T\to\infty\) first; it supplies no joint \(T,D\) scaling theorem.

**5. Independent particles.** For any fixed integer \(N\ge1\) of independent copies, the total signed impulse \(S_T^{(N)}\) has scaled generating function \(N\Lambda_D(q)\) and current rate function \(I_D^{(N)}(j)=N I_D(j/N)\). The derivation is exact because independent moment-generating functions multiply.

## Verification

The attached standalone `verify.py` needs only Python's standard library. Execute `python verify.py`. It checks the two-state eigenvalue and its derivative, unique optimizer and symmetry of the rate function, its singular edge profile at different small diffusivities, and pathwise reflection identities on independently simulated exact event-driven zero-diffusion trajectories. It completed 1,607 checks. These finite calculations test consistency and are **not** the proof of the long-time or uniform asymptotic assertions; Steps 1–5 establish those assertions analytically.

For example, at \(v=\lambda=1\) and \(D=10^{-4}\), numerical Legendre inversion gives \(I_D(1)=0.9447894935901964\); the leading formula gives \(0.9447395275203943\). At \(D=10^{-6}\), these are \(0.9880949920944957\) and \(0.9880944921102385\), respectively.

## Relationship to prior work

Li, Eichhorn and Dabelow (2026) derive finite-box **mean** ideal-active-gas pressure laws and an exact one-dimensional stationary model; these motivate considering force *fluctuations* and very rare net imbalances, but their gas law alone does not give this small-thermal-diffusivity large-deviation edge. The stationary run-and-tumble wall occupation model and its mean pressure are established by Angelani and Bressloff. Bressloff (2023), in particular, gives a full joint occupation-time transform for the two wall contacts in the zero-diffusion model. Consequently the zero-diffusion force statistics are in principle recoverable from that earlier work and are **not independently claimed to be novel**.

General large-deviation frameworks for reflected diffusions and reflected jump-diffusions are established by Mallmin, du Buisson and Touchette (2021) and Popovic and Zoroddu (2022). These supply important prior general methods but do not present the particular telegraph-plus-translational-diffusion wall-regulator imbalance or its \(D^{1/3}\) rate-height and \(D^{2/3}\) current-width rounding profile. The main claim is this combined *physical observable and singular edge classification*, not a new general large-deviation principle or a new telegraph tilted matrix.

## Limitations

The two-wall difference is distinguished from each wall's force. No joint distribution of the individual wall impulses is asserted. The box is a fixed finite interval, walls are hard and normal reflecting, the orientation dynamics are independent of the position and Brownian noise, and particles (when present) are noninteracting. No statement covers moving/soft walls, orientation-changing interactions with the wall, externally feedback-controlled propulsion, or finite-time thermodynamic work. The small-diffusion expansion holds only after first taking long observation time. A stronger, as-yet-unlocated physical application of the general reflected-process large-deviation theory could overlap with the result; independent publication-priority validation remains outstanding.

## References

- S. Li, R. Eichhorn, L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287v1 (first posted 2026-10-01), https://arxiv.org/abs/2610.01287.
- L. Angelani, *Confined run-and-tumble swimmers in one dimension*, arXiv:2206.03123, https://arxiv.org/abs/2206.03123.
- P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158 (2023), https://arxiv.org/abs/2302.01158.
- E. Mallmin, J. du Buisson, H. Touchette, *Large deviations of currents in diffusions with reflective boundaries*, J. Phys. A 54 (2021) 295001, arXiv:2102.04846, https://arxiv.org/abs/2102.04846.
- L. Popovic, G. Zoroddu, *Large Deviations for Additive Functionals of Reflected Jump-Diffusions*, SIAM J. Appl. Math. 82 (2022) 2008–2035, arXiv:2012.13223, https://arxiv.org/abs/2012.13223.
