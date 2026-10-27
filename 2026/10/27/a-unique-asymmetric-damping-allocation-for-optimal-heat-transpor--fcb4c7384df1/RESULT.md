# A unique asymmetric damping allocation for optimal heat transport through a harmonic dimer

## Finding

For a classical underdamped harmonic dimer with fixed positive trap stiffnesses \(u,v\), interparticle spring constant \(k\), a fixed total bath friction \(G\), equal unit particle masses, and unequal bath temperatures \(T_1>T_2>0\), consider the stationary heat current from bath 1 into bath 2 while allocating the friction budget \(\gamma_1+\gamma_2=G\), with both frictions strictly positive.

Write \(p=\gamma_1/G\), \(a=u+k\), \(b=v+k\), and \(\Delta T=T_1-T_2\). The exact stationary current is

\[
J(p)=\frac{k^2G\Delta T}{(a-b)^2+\frac{k^2}{p(1-p)}+G^2\left(a(1-p)+bp\right)}.
\]

It has **exactly one global maximizer** \(p_*\in(0,1)\), characterized by

\[
\frac{k^2(2p_*-1)}{p_*^2(1-p_*)^2}=G^2(u-v).
\]

The optimizer is balanced, \(p_*=1/2\), exactly when \(u=v\). For \(u>v\), one has \(p_*>1/2\), so the stiffer oscillator receives the larger friction allocation, and conversely if \(u<v\). As the total friction grows without bound, the smaller *optimized* friction converges to the nonzero finite constant

\[
\lim_{G\to\infty}\min(\gamma_{1,*},\gamma_{2,*})
=\frac{k}{\sqrt{|u-v|}},\qquad u\ne v.
\]

In that regime,

\[
J_{\max}(G)\sim\frac{k^2\Delta T}{G\,[\min(u,v)+k]},\quad
\frac{J_{\max}(G)}{J_{\mathrm{balanced}}(G)}\longrightarrow
\frac{u+v+2k}{2[\min(u,v)+k]}.
\]

Thus the optimal asymmetry yields a strictly larger asymptotic current than equal division whenever the trap stiffnesses differ. For \(G\downarrow0\), the optimizer instead approaches equal division with the expansion

\[
p_*=\frac12+\frac{G^2(u-v)}{32k^2}+O(G^4).
\]

## Assumptions and scope

Let \(u,v,k,G>0\), \(T_1>T_2>0\), and let \(W_1,W_2\) be independent standard Brownian motions. For each \(p\in(0,1)\), set \(g=Gp\), \(h=G(1-p)\), and consider the Itô equations

\[
\begin{aligned}
\mathrm d x_1&=v_1\,\mathrm dt, &\mathrm d x_2&=v_2\,\mathrm dt,\\
\mathrm d v_1&=\big[-(u+k)x_1+kx_2-gv_1\big]\,\mathrm dt+\sqrt{2gT_1}\,\mathrm dW_1,\\
\mathrm d v_2&=\big[kx_1-(v+k)x_2-hv_2\big]\,\mathrm dt+\sqrt{2hT_2}\,\mathrm dW_2.
\end{aligned}
\]

The masses and Boltzmann constant are normalized to one, so stiffnesses have units of inverse time squared and friction coefficients have units of inverse time. All displayed asymptotics vary \(G\), holding \(u,v,k,T_1,T_2\) fixed. The observed heat current is the stationary reservoir input into oscillator 1, \(J=g(T_1-\mathbb E[v_1^2])\), equivalently the negative input from reservoir 2.

## Proof

**Existence of a stationary state.** The deterministic mechanical energy is

\[
E=\tfrac12(v_1^2+v_2^2)+\tfrac12(ux_1^2+vx_2^2+k(x_1-x_2)^2).
\]

Its derivative along the deterministic drift is \(\dot E=-gv_1^2-hv_2^2\le0\). The largest invariant set on which this derivative is zero has both velocities zero and then, since the position stiffness matrix is strictly positive definite, both positions zero. For the finite-dimensional linear drift this implies Hurwitz stability. Consequently the Ornstein--Uhlenbeck process has a unique centered invariant Gaussian law with finite moments, determined by its Lyapunov equation.

**Exact current.** Put \(a=u+k\), \(b=v+k\), \(C=\mathbb E[x_1v_2]\), and \(W=\mathbb E[v_1v_2]\) at stationarity. Taking expectations in the Itô derivatives of \(x_1^2,x_2^2,x_1x_2,v_1^2,v_2^2\) gives

\[
\mathbb E[x_1v_1]=\mathbb E[x_2v_2]=0,\quad
\mathbb E[x_2v_1]=-C,\quad
\mathbb E[v_1^2]=T_1-\frac{kC}{g},\quad
\mathbb E[v_2^2]=T_2+\frac{kC}{h}.
\]

The derivative of \(v_1v_2\) gives \(W=(b-a)C/(g+h)\). The derivatives of \(x_1v_1\) and \(x_2v_2\) give

\[
\mathbb E[v_1^2]=a\mathbb E[x_1^2]-k\mathbb E[x_1x_2],\quad
\mathbb E[v_2^2]=b\mathbb E[x_2^2]-k\mathbb E[x_1x_2].
\]

Finally, stationarity of \(x_1v_2\) and \(x_2v_1\) gives

\[
W+k\mathbb E[x_1^2]-b\mathbb E[x_1x_2]-hC=0,\qquad
W-a\mathbb E[x_1x_2]+k\mathbb E[x_2^2]+gC=0.
\]

Multiplying these equations by \(a\) and \(b\), respectively, and subtracting eliminates \(\mathbb E[x_1x_2]\). Substitution of the preceding moment identities yields the exact identity

\[
k\Delta T=C\left(\frac{(a-b)^2}{g+h}+\frac{k^2(g+h)}{gh}+ah+bg\right).
\]

The stationary energy balance therefore gives \(J=g(T_1-\mathbb E[v_1^2])=kC=h(\mathbb E[v_2^2]-T_2)\), proving the claimed formula after inserting \(g=Gp\), \(h=G(1-p)\). Every denominator term is positive, so \(J>0\).

**Unique optimum and its location.** Maximizing \(J\) is equivalent to minimizing

\[
F(p)=(a-b)^2+k^2\left(\frac1p+\frac1{1-p}\right)+G^2\big[a(1-p)+bp\big].
\]

Direct differentiation gives

\[
F'(p)=k^2\left(-\frac1{p^2}+\frac1{(1-p)^2}\right)+G^2(b-a),\qquad
F''(p)=2k^2\left(\frac1{p^3}+\frac1{(1-p)^3}\right)>0.
\]

As \(p\downarrow0\), \(F'\to-\infty\); as \(p\uparrow1\), \(F'\to+\infty\). Hence it has a unique critical point, necessarily its global minimum; the current tends to zero at both endpoints. Evaluating \(F'(1/2)=G^2(v-u)\) establishes the precise sign of the optimal asymmetry. The critical-point equation is exactly the equation in the Finding.

**Asymptotics and enhancement.** For small \(G\), write \(p_*=1/2+\varepsilon\). Taylor's theorem applied to \(F'=0\) gives \(32k^2\varepsilon=G^2(u-v)+O(\varepsilon^3)\), establishing the stated \(O(G^4)\) remainder (indeed a stronger remainder is available). If \(u>v\), the critical equation implies \(p_*\uparrow1\). Writing \(\delta=1-p_*\), we have

\[
\frac{k^2(1-2\delta)}{(1-\delta)^2\delta^2}=G^2(u-v),
\]

and hence \(G\delta\to k/\sqrt{u-v}\). If \(v>u\), the same argument with the indices interchanged proves \(Gp_*\to k/\sqrt{v-u}\). In either case, the \(G^2\) term of \(F(p_*)\) approaches \(G^2\min(a,b)\) in ratio, while the singular reciprocal term contributes only \(O(G)\). Thus \(J_{\max}\sim k^2\Delta T/[G\min(a,b)]\). Substituting \(p=1/2\) into the exact current and dividing establishes the enhancement factor; it exceeds one strictly if \(u\ne v\). This proves all asserted limits.

## Verification

The standalone Python program `check_heat.py` independently reconstructs the ten scalar equations of the stationary \(4\times4\) covariance Lyapunov system using exact rational arithmetic and checks the heat-current formula against eight parameter sets. It also checks the location and optimality of the unique predicted allocation against comparison grids in six regimes. Its completed execution printed `PASS: 8 exact-rational stationary covariance/current checks, 6 optimality grids`.

The symbolic all-parameter conclusions are established by the analytic derivation above; the finite tests neither establish nor substitute for those proofs. The program uses Python standard-library functionality only.

## Relationship to prior work

Ciliberto, Imparato, Naert, and Tanase (arXiv:1301.4311, first posted 2013-01-18) experimentally and analytically study heat exchange between two thermal reservoirs and an analogous pair of *overdamped* coupled Brownian particles. Their equations (3)--(7) and supplemental treatment establish a heat-current law for that first-order model, not the present second-order inertial system or its fixed-total-friction maximizer.

Barton (2015) treats two dynamically identical classical oscillators and heat flow; that symmetry cannot capture the stiffness-asymmetric optimal friction allocation. The accessible abstract was checked, but its full article was not inspected.

Henkel (2021) analyzes a broader pair-of-oscillators quantum Langevin model, including unequal damping and classical Ohmic limits. In particular its equation (44) gives a general positive-frequency integral representation for heat flow. The relevant full article (model, covariance, and heat-current sections) does **not** give the closed fixed-budget optimization, its strict-uniqueness criterion, or the finite weak-contact limit derived here. That general spectral integral is relevant prior coverage of the forward-model setup and may make the specific formula derivable by further algebra; the asserted distinct contribution is the exact global allocation theorem, not the existence or direction of the current.

## Limitations

The result addresses a two-site, unit-mass, classical, linear **underdamped** Langevin system with independent white-noise baths and positive bare onsite springs. It fixes the sum of the *friction rates*, not a cost-weighted allocation of microscopic bath couplings. The thermal difference changes only the current amplitude, not the optimizer, within this classical model. Its strong-budget limit varies both bath couplings while keeping other physical parameters fixed. General non-Ohmic memory, unequal masses, nonlinear forces, quantum corrections, and finite observation noise are not covered. Priority may depend on non-indexed optimization studies or specialized classical limits of broader oscillator transport results.

## References

1. S. Ciliberto, A. Imparato, A. Naert, M. Tanase, *On the heat flux and entropy produced by thermal fluctuations*, arXiv:1301.4311 (first posted 2013-01-18), https://arxiv.org/abs/1301.4311.
2. G. Barton, *Classical van der Waals heat flow between oscillators and between half-spaces*, J. Phys.: Condens. Matter 27 (2015), 214005; DOI:10.1088/0953-8984/27/21/214005.
3. C. Henkel, *Heat Transfer and Entanglement--Non-Equilibrium Correlation Spectra of Two Quantum Oscillators*, Annalen der Physik 533 (2021), 2100089; DOI:10.1002/andp.202100089.
