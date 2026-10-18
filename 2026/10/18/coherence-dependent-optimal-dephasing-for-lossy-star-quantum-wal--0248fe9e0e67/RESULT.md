# Coherence-dependent optimal dephasing for lossy star quantum walks

## Finding

For a star with \(m\ge 2\) leaves, homogeneous hopping \(J>0\), loss from the central vertex at rate \(\kappa>0\), and uniform site-projector dephasing at rate \(\gamma>0\), let an arbitrary initial density matrix be supported on the leaves. Write \(s=\sum_{i,j=1}^{m}\rho_{ij}(0)=m\langle b|\rho(0)|b\rangle\), with \(|b\rangle=m^{-1/2}\sum_{j=1}^{m}|j\rangle\). Then \(0\le s\le m\), eventual absorption is certain, and the unconditional mean absorption time is exactly

\[
\tau_\gamma=\frac{m+1}{\kappa}+\frac{\kappa}{4J^2}+\frac{\gamma}{2J^2}+\frac{m-s}{\gamma}.
\]

If \(s<m\), this mean has the unique global minimizer

\[
\gamma_*=J\sqrt{2(m-s)},\qquad
\tau_{\min}=\frac{m+1}{\kappa}+\frac{\kappa}{4J^2}+\frac{\sqrt{2(m-s)}}{J}.
\]

In particular, the optimal dephasing is independent of the positive trap-loss rate. For \(s=m\), the mean grows strictly with positive dephasing; its infimum on \(\gamma>0\) is \((m+1)/\kappa+\kappa/(4J^2)\), but at exactly zero dephasing its value is \(2/\kappa+\kappa/(4mJ^2)\). Thus the mean absorption time has a finite, strictly positive jump in the zero-dephasing limit from a bright initial state. At zero dephasing and \(s<m\), a positive dark population survives indefinitely and the unconditional mean is infinite.

## Assumptions and scope

The one-particle Hilbert space has orthonormal basis \(|0\rangle,|1\rangle,\dots,|m\rangle\), with central site \(0\). Let \(P_j=|j\rangle\langle j|\). With \(J,\kappa>0\), the Hamiltonian and trace-decreasing master equation are

\[
H=J\sum_{j=1}^{m}(|0\rangle\langle j|+|j\rangle\langle0|),
\]
\[
\frac{d\rho}{dt}=-i[H,\rho]
+\gamma\sum_{j=0}^{m}\left(P_j\rho P_j-\frac12\{P_j,\rho\}\right)
-\frac{\kappa}{2}\{P_0,\rho\}.
\]

The dephasing convention is explicit: every off-diagonal matrix entry incurs decay rate \(\gamma\) from the dephasing term alone, whereas the site populations are unchanged by that term. The initial \(\rho(0)\) is any positive semidefinite unit-trace density matrix supported on the leaf subspace. The mean is \(\tau_\gamma=\int_0^\infty \operatorname{tr}\rho(t)\,dt\), with \(+\infty\) allowed at \(\gamma=0\). No additional onsite energies, disorder, or site-dependent noise are assumed.

## Proof

**Decay and integrability for positive dephasing.** On the full complex operator space, the Hilbert–Schmidt real part of the generator obeys

\[
-\operatorname{Re}\langle X,\mathcal L X\rangle
=\gamma\sum_{i\ne j}|X_{ij}|^2
+\frac\kappa2\left(2|X_{00}|^2+\sum_{j=1}^m(|X_{0j}|^2+|X_{j0}|^2)\right).
\]

Consequently each eigenvalue has nonpositive real part. A hypothetical eigenvector whose eigenvalue has zero real part must be diagonal and have zero center entry. For such a diagonal \(X\), all diagonal entries of \(-i[H,X]\) vanish; thus an imaginary-axis eigenvalue must be zero, and the hub–leaf entries of the commutator force every remaining leaf diagonal entry to vanish. There is no nonzero eigenvector on the imaginary axis. In this finite-dimensional generator all eigenvalues have strictly negative real part, so all density-matrix entries decay exponentially and the following integrals exist.

**Four-variable closure.** Define four real variables

\[
x(t)=\rho_{00}(t),\quad p(t)=\sum_{j=1}^m\rho_{jj}(t),\quad
B(t)=\sum_{i,j=1}^m\rho_{ij}(t),\quad
\eta(t)=\operatorname{Im}\sum_{j=1}^m\rho_{0j}(t).
\]

Directly taking entries of the stated master equation yields, without symmetry assumptions on the initial density matrix,

\[
\begin{aligned}
\dot x&=-2J\eta-\kappa x,\\
\dot p&=2J\eta,\\
\dot B&=2mJ\eta-\gamma(B-p),\\
\dot\eta&=-J(B-mx)-(\gamma+\kappa/2)\eta.
\end{aligned}
\]

At time zero, \((x,p,B,\eta)=(0,1,s,0)\). All four tend to zero exponentially for \(\gamma>0\). Integrating the second, first, third, and fourth equations in that order yields

\[
\int_0^\infty\eta\,dt=-\frac1{2J},\qquad
\int_0^\infty x\,dt=\frac1\kappa,
\]
\[
\int_0^\infty(B-p)\,dt=\frac{s-m}{\gamma},\qquad
\int_0^\infty B\,dt=\frac m\kappa+\frac{\gamma+\kappa/2}{2J^2}.
\]

Because \(\operatorname{tr}\rho=x+p\), substitution proves the exact formula. Completing the square,

\[
\frac\gamma{2J^2}+\frac{m-s}\gamma
-\frac{\sqrt{2(m-s)}}J
=\left(\frac{\sqrt\gamma}{\sqrt2 J}-\frac{\sqrt{m-s}}{\sqrt\gamma}\right)^2\ge0,
\]

with equality at exactly the stated \(\gamma_*\) when \(s<m\). For \(s=m\), the last inverse-noise term vanishes and the positive-noise mean increases linearly.

**Exactly zero dephasing.** Decompose the leaf space into its one-dimensional bright direction \(|b\rangle\) and the orthogonal dark space. The Hamiltonian couples the hub only to the bright direction, with strength \(\sqrt m J\); every dark vector is stationary and invisible to the trap. Its initial weight is \(1-s/m\). If this weight is positive, the surviving trace is bounded below by it at every time and the unconditional mean diverges. If \(s=m\), positivity and unit trace force \(\rho(0)=|b\rangle\langle b|\); direct integration of the lossy two-state equations with coupling \(\sqrt mJ\) gives \(2/\kappa+\kappa/(4mJ^2)\). Subtracting it from the positive-noise limit gives \((m-1)/\kappa+\kappa(m-1)/(4mJ^2)>0\).

## Verification

A self-contained script, `verification.py`, independently constructs the full \((m+1)^2\)-dimensional Lindblad superoperator, integrates it by matrix inversion, and compares its mean with the formula for multiple graph sizes, hopping values, trap rates, positive dephasing rates, localized inputs, bright inputs, random coherent leaf states, and mixed states. It also checks the predicted positive-noise optimum by numerical minimization and the strict zero-noise discontinuity algebraically. Executing `python verification.py` with NumPy and SciPy completed 326 checks; the largest absolute mean-time discrepancy was \(2.096\times10^{-13}\), and the largest scaled discrepancy was \(7.130\times10^{-15}\). The dimension-free argument above, not finite sampling, proves the claims.

## Relationship to prior work

Yalouz and Pouthier (2018, 2022) investigated trapping and energy-defect optimization in coherent extended-star excitonic networks. Their trap-coupled dark/bright structure motivates the present finite star, but their source models do not supply the asserted homogeneous-dephasing mean-time optimizer. Pepe, Pouthier, and Yalouz (2023) studied a dephased extended star with a peripheral uniform initial state and optimized energy defects using a 50% absorption-time measure, together with strong-dephasing random-walk approximations. That study does not assert an exact all-rate mean-absorption formula for arbitrary initial mixed leaf states or the dependence of its optimal dephasing on bright overlap. Alterman, Berman, and Strauch (2023) derived exact transport optimization formulas on an all-to-all coupled network; the leaf–leaf hoppings and dynamical objective distinguish that graph from the present hub-only star. Bressanini, Benedetti, and Paris (2022) studied the classicalization of quantum walks under several dephasing models, including stars, without the lossy-hub mean-time objective. These works supply prior models and methods, not claimed as new here.

## Limitations

The result is exact only for a one-particle, equal-hopping star with uniform site-basis dephasing, a single central absorber, and no other loss. It does not optimize spectral gaps, finite-time absorption quantiles, or general multi-excitation transport, and does not establish robustness to unequal hopping or nonuniform noise. The zero-noise limit is singular in the mean and must not be interchanged with the infinite-time integration. Possible implicit formulations within general graph-resolvent or quantum transport literature require further independent scrutiny; independent validation has not occurred.

## References

1. S. Yalouz and V. Pouthier, “Continuous-time quantum walk on an extended star graph: Trapping and superradiance transition,” *Physical Review E* 97, 022304 (2018), doi:10.1103/PhysRevE.97.022304. Public date: 2018-02-08.
2. S. Yalouz and V. Pouthier, “The extended star graph as a light-harvesting-complex prototype: excitonic absorption speedup by peripheral energy defect tuning,” arXiv:2210.17524 (2022).
3. G. Bressanini, C. Benedetti, and M. G. A. Paris, “Decoherence and classicalization of continuous-time quantum walks on graphs,” arXiv:2204.01836 (2022).
4. L. Pepe, V. Pouthier, and S. Yalouz, “Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing,” arXiv:2308.15857 (2023).
5. S. Alterman, J. Berman, and F. Strauch, “Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network,” arXiv:2309.00164 (2023).
