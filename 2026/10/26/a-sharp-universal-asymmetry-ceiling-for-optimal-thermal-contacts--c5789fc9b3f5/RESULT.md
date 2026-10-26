# A sharp universal asymmetry ceiling for optimal thermal contacts in an unequal-mass Langevin dimer

## Finding

Two freely translating masses connected by one Hooke spring exchange heat between independent classical Langevin thermostats. When the sum of their physical friction coefficients is prescribed, the steady heat current has one strictly interior global maximizer for *every* positive mass ratio. Surprisingly, the maximizing **fraction** depends only on the mass ratio, not on the connecting spring constant, total friction, or two bath temperatures.

More precisely, let the masses be \(m_1,m_2>0\), the connecting spring stiffness be \(k>0\), the bath temperatures satisfy \(T_1>T_2>0\), and the positive friction coefficients satisfy \(\gamma_1+\gamma_2=G>0\). Put \(r=m_2/m_1\) and \(p=\gamma_1/G\). There is a unique maximizer \(p_*(r)\in(0,1)\). It is the unique root in that interval of
\[
P_r(p)=r^3p^2(1-2p)+2r^2p^2(p-1)+2rp(p-1)^2+(1-p)^2(1-2p)=0.
\]
It obeys \(p_*(1)=1/2\), \(p_*(r)<1/2\) when \(r>1\), and \(p_*(r)>1/2\) when \(0<r<1\). Under exchange of the masses, \(p_*(1/r)=1-p_*(r)\).

The asymmetry has the following **sharp universal ceiling**:
\[
\boxed{\left|p_*(r)-\frac12\right|\le\frac{\sqrt7}{28}.}
\]
Equality holds if and only if
\[
\boxed{r\in\left\{\frac{16+5\sqrt7}{9},\frac{16-5\sqrt7}{9}\right\}.}
\]
Thus no possible positive mass ratio requires more than \(0.09449111825\ldots\) of the total damping budget to be transferred away from the balanced allocation to maximize the stationary heat flux. At \(r=(16+5\sqrt7)/9\), the exact optimum is \(p_*=1/2-\sqrt7/28\); at the reciprocal ratio it is \(1/2+\sqrt7/28\).

## Assumptions and scope

The motion obeys the Itô stochastic differential equations
\[
\begin{aligned}
 dx_1&=v_1\,dt,& m_1\,dv_1&=(-k(x_1-x_2)-\gamma_1v_1)\,dt+\sqrt{2\gamma_1T_1}\,dW_1,\\
 dx_2&=v_2\,dt,& m_2\,dv_2&=(+k(x_1-x_2)-\gamma_2v_2)\,dt+\sqrt{2\gamma_2T_2}\,dW_2,
\end{aligned}
\]
where \(W_1,W_2\) are independent standard Brownian motions; Boltzmann's constant is set to one. The system has no individual onsite pins, no mechanical driving, and no nonlinear forces. The center-of-mass coordinate is not stationary, but the relative displacement \(y=x_1-x_2\) together with the velocities has a unique stationary Gaussian law. All expectations below refer to this stationary law.

The directional energy current from bath 1 to bath 2 equals \(J=k\mathbb E[yv_2]\), because \(\mathbb E[yv_1]=\mathbb E[yv_2]\) in stationarity. As \(T_1>T_2\), \(J>0\). Only the friction split \(0<p<1\) is optimized, with \(m_1,m_2,k,G,T_1,T_2\) fixed. The limit allocations \(p=0\) and \(p=1\) have zero heat current (interpreted as limits of the positive-friction model).

## Proof

**1. Stability.** On the stationary variables \((y,v_1,v_2)\), the deterministic drift matrix is
\[
 A=\begin{pmatrix}0&1&-1\\-k/m_1&-\gamma_1/m_1&0\\k/m_2&0&-\gamma_2/m_2\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^3+a_2\lambda^2+a_1\lambda+a_0\), where
\[
 a_2=\frac{\gamma_1}{m_1}+\frac{\gamma_2}{m_2},\quad
 a_1=k\left(\frac1{m_1}+\frac1{m_2}\right)+\frac{\gamma_1\gamma_2}{m_1m_2},\quad
 a_0=\frac{k(\gamma_1+\gamma_2)}{m_1m_2}.
\]
A direct dissipation argument proves Hurwitz stability: the positive quadratic mechanical energy \(\frac12ky^2+\frac12m_1v_1^2+\frac12m_2v_2^2\) has derivative \(-\gamma_1v_1^2-\gamma_2v_2^2\), and the only invariant set with both velocities zero is the origin (since nonzero \(y\) would immediately accelerate the masses). The standard invariance principle, or its finite-dimensional linear equivalent, therefore gives exponential decay. Thus the finite-dimensional deterministic semigroup decays exponentially, and the stated Gaussian covariance exists uniquely.

**2. Exact heat current.** Write
\[
 c=\mathbb E[yv_1]=\mathbb E[yv_2],\quad z=\mathbb E[v_1v_2],\quad q_i=\mathbb E[v_i^2],\quad s=\mathbb E[y^2].
\]
Stationarity of the second moments gives
\[
 z=\frac{k(m_1-m_2)}{\gamma_1m_2+\gamma_2m_1}c,\quad
 q_1=\frac{T_1}{m_1}-\frac{k}{\gamma_1}c,\quad
 q_2=\frac{T_2}{m_2}+\frac{k}{\gamma_2}c,
\]
and, from the two \(yv_i\) equations,
\[
 ks=m_1(q_1-z)-\gamma_1c=m_2(q_2-z)+\gamma_2c.
\]
Solving this scalar identity for \(c\) yields
\[
\boxed{J=(T_1-T_2)\frac{k\gamma_1\gamma_2(\gamma_1m_2+\gamma_2m_1)}{(\gamma_1+\gamma_2)\bigl[\gamma_1\gamma_2(\gamma_1m_2+\gamma_2m_1)+k(\gamma_1m_2^2+\gamma_2m_1^2)\bigr]}.}
\]
Every factor in its denominator is positive.

**3. Reduction to a geometric one-variable problem.** Put
\[
 F_r(p)=\frac{p(1-p)[1+(r-1)p]}{1+(r^2-1)p},\qquad R=\frac{F_r(p)}{m_1}.
\]
The current is
\[
 J=(T_1-T_2)\frac{kG R}{G^2R+k}.
\]
For fixed positive \(G,k,T_1-T_2\), this is a strictly increasing function of \(R>0\). Therefore exactly the maximizers of \(F_r\) maximize the current. This proves all claimed parameter independences.

**4. Unique optimizer.** For every \(r>0\), \(F_r(p)>0\) on \((0,1)\) and vanishes at its endpoints. Its logarithmic second derivative is
\[
 (\log F_r)''=-\frac1{p^2}-\frac1{(1-p)^2}-\frac{(r-1)^2}{[1+(r-1)p]^2}+\frac{(r^2-1)^2}{[1+(r^2-1)p]^2}.
\]
When \(r>1\), the final positive term is smaller than \(1/p^2\); when \(0<r<1\), it is smaller than \(1/(1-p)^2\). For \(r=1\) it vanishes. Hence \(\log F_r\) is strictly concave, and the unique critical point of \(F_r\) is its unique global maximum. Differentiating gives precisely the polynomial \(P_r(p)\) displayed in the Finding. Moreover
\[
 F_r'(1/2)=-\frac{r(r-1)}{(1+r^2)^2},
\]
so the signs relative to \(1/2\) follow. Replacing \((r,p)\) by \((1/r,1-p)\) changes \(F_r\) by only the positive factor \(r\), proving reflection symmetry.

**5. Sharp universal asymmetry bound.** The implicit optimizer \(p_*(r)\) depends smoothly on \(r>0\) by strict log-concavity; also \(p_*(r)\to1/2\) as \(r\to0\) or \(r\to\infty\). Write \(P_r(p)\) for the numerator of \(F_r'(p)\). The critical points of \(p_*(r)\) obey \(P_r(p)=\partial_rP_r(p)=0\). Two exact polynomial eliminations give, up to nonzero signs,
\[
\begin{aligned}
 \operatorname{Res}_{p}(P_r,\partial_rP_r)&=-2r^4(r-1)^2(9r^2-32r+9),\\
 \operatorname{Res}_{r}(P_r,\partial_rP_r)&=-p^6(p-1)^4(2p-1)(112p^2-112p+27).
\end{aligned}
\]
For \(r>1\), the only possible interior extremizing mass ratio is \(r_0=(16+5\sqrt7)/9\). Substitution into the stationarity equation gives \(p_*(r_0)=1/2-\sqrt7/28\). Because the optimizer is below \(1/2\) for all \(r>1\) yet approaches \(1/2\) at both ends of \((1,\infty)\), this point is its unique global minimum. Reflection gives the upper extreme at \(1/r_0=(16-5\sqrt7)/9\). This proves the sharp universal bound and precisely its equality cases.

## Verification

The standalone `CHECK.py` verifies the polynomial elimination identities exactly with SymPy, reconstructs the full three-variable stationary covariance matrix, and proves by exact symbolic substitution that its Lyapunov residual vanishes. Independent numerical covariance computations solve the three-dimensional Lyapunov equation for 340 randomly selected positive mass, spring, temperature and friction parameters. A further 163 mass-ratio families compare the scalar optimizer to direct numerical maximization, including both sharp equality ratios. All included tests pass when run with SymPy, NumPy and SciPy. These checks corroborate but do not replace the analytic proof in the previous section.

For a concrete nondegenerate example, \(m_1=1\), \(m_2=(16+5\sqrt7)/9\), \(G=2\), \(k=1\), \(T_1-T_2=1\) yield \(p_*=0.405508881747693\ldots\) and maximal current \(J_*=0.137250432801715\ldots\), compared with \(0.134463205957981\ldots\) under balanced friction.

## Relationship to prior work

Morgado and Duarte Queirós (arXiv:1207.6044; 2012) treat heat conduction between two **equal-mass, equally damped** oscillators, with individual onsite restoring forces and a general white-noise framework. Their explicit equal-friction thermal-conductance calculation is prior evidence for the basic Langevin method, not for an unequal-mass fixed-sum friction optimization. Falasco et al. (arXiv:1505.05088; 2015) derive mode-temperature distributions for uniform harmonic chains with the same friction at each site, rather than a heterogeneous contact allocation. Barton (2015) studies dynamically identical oscillator pairs; its available abstract does not resolve the mass-imbalance optimization. Henkel (2021) establishes a much more general oscillator heat-current spectral formula; that formula covers underlying transport physics but does not supply the present fixed-friction-budget optimizer, the mass-only invariance, or the sharp universal asymmetry ceiling.

Separately, onsite-pinned two-oscillator models need not share the present mass-only friction allocation law: the onsite stiffnesses alter their dynamical constraints. Our free-dimer classification is not a claim about such pinned models.

## Limitations

The theorem requires classical independent Gaussian white-noise baths satisfying fluctuation-dissipation with temperature-independent friction and an **unpinned** connecting Hooke spring. The common translational coordinate is not stationary, although relative displacement and velocities are. The result maximizes steady expected heat current, not transient transport, heat-current fluctuations, finite-time conduction, or thermal-machine efficiency. It does not assert the same mass-only optimizer for onsite-pinned, colored-noise, quantum, nonlinear, or many-mass chains. The literature comparison is not an exhaustive historical priority guarantee; in particular, the complete Barton (2015) paper was not accessible for inspection.

## References

1. W. A. M. Morgado and S. M. Duarte Queirós, *The role of the nature of the noise in the thermal conductance of mechanical systems*, arXiv:1207.6044 (first public 2012-07-25), Phys. Rev. E 86, 041108 (2012). https://ar5iv.labs.arxiv.org/html/1207.6044
2. G. Falasco, M. Baiesi, L. Molinaro, L. Conti and F. Baldovin, *Energy repartition for a harmonic chain with local reservoirs*, arXiv:1505.05088 (2015), Phys. Rev. E 92, 022129 (2015). https://userswww.pd.infn.it/~baiesi/papers/energy_modes_2015.pdf
3. G. Barton, *Classical van der Waals heat flow between oscillators and between half-spaces*, J. Phys.: Condens. Matter 27, 214005 (2015). https://doi.org/10.1088/0953-8984/27/21/214005
4. C. Henkel, *Heat Transfer and Entanglement–Non-Equilibrium Correlation Spectra of Two Quantum Oscillators*, Ann. Phys. 533, 2100089 (2021). https://doi.org/10.1002/andp.202100089
