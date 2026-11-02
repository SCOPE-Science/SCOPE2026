# Geometric-mean dissipation crossover in a four-direction active harmonic trap

## Finding
For a thermally diffusing planar particle propelled along four Cartesian directions with reversible but direction-dependent Poisson reorientations, the steady entropy production in a rotated anisotropic harmonic trap has a sharp alignment reversal. Let the distinct trap relaxation rates satisfy \(0<k_1<k_2\), let the distinct orientation-correlation decay rates satisfy \(0<\gamma_1<\gamma_2\), and let \(\theta\) be the angle from the propulsion axes to the trap's principal axes. Under the even-orientation time-reversal convention described below, put
\[
A=\frac{\gamma_1}{k_1+\gamma_1}+\frac{\gamma_2}{k_2+\gamma_2},\qquad
B=\frac{\gamma_2}{k_1+\gamma_2}+\frac{\gamma_1}{k_2+\gamma_1}.
\]
The exact stationary total entropy-production rate is
\[
\boxed{\Pi(\theta)=\frac{v^2}{2D}(A\cos^2\theta+B\sin^2\theta).}
\]
The alignment contrast has the factorization
\[
\boxed{A-B=\frac{(\gamma_1-\gamma_2)(k_1-k_2)(\gamma_1\gamma_2-k_1k_2)}{(k_1+\gamma_1)(k_1+\gamma_2)(k_2+\gamma_1)(k_2+\gamma_2)}.}
\]
Thus aligned principal axes \(\theta=0\) minimize dissipation over \(0\leq\theta\leq\pi/2\) if \(\gamma_1\gamma_2<k_1k_2\), while crossed axes \(\theta=\pi/2\) minimize it if \(\gamma_1\gamma_2>k_1k_2\). The minimizer is unique within that closed angle interval outside the equality case. At the nondegenerate transition
\[
\boxed{\gamma_1\gamma_2=k_1k_2,\qquad \Pi(\theta)=\frac{v^2}{2D}\quad\hbox{for every }\theta.}
\]
The crossing therefore produces an exact orientation-blind dissipation rate although both the confinement and the reorientation dynamics remain anisotropic.

## Assumptions and scope
Let \(X_t\in\mathbb R^2\) obey the Itô stochastic differential equation
\[
dX_t=(-K_\theta X_t+vN_t)\,dt+\sqrt{2D}\,dW_t,
\quad K_\theta=R_\theta\begin{pmatrix}k_1&0\\0&k_2\end{pmatrix}R_\theta^\top,
\]
where \(R_\theta\) is the rotation matrix, \(W_t\) is standard planar Brownian motion, \(v>0\), \(D>0\), and \(0<k_1<k_2\). The stationary internal state \(N_t\) takes values in \(\{e_1,-e_1,e_2,-e_2\}\) and is independent of \(W_t\). Each \(\pm e_i\) state flips to its same-axis opposite at rate \(a_i>0\) and jumps to each of the two perpendicular states at rate \(b/2\), with \(b>0\). These rates are symmetric between each pair of connected states; all four stationary state probabilities are \(1/4\). Define \(\gamma_i=2a_i+b\), and impose \(0<\gamma_1<\gamma_2\) (equivalently \(a_1<a_2\)). Every such parameter set has a unique stationary joint probability law with finite moments.

Entropy production is the steady total (diffusive plus internal-jump) path-irreversibility rate **with the orientation states taken as even under time reversal**, with the thermal diffusion coefficient \(D\) setting the translational thermodynamic scale and symmetric internal transition rates carrying zero medium affinity. This is the standard stationary entropy-balance convention for this kinetic model; different parity or energetic bookkeeping conventions for active propulsion need not give the same thermodynamic quantity.

## Proof
**1. Directional relaxation and the stationary cross moment.** The symmetric four-state jump generator \(Q\) satisfies \(QN_i=-\gamma_iN_i\) as an identity on the states, while reversibility gives \(\mathbb E[N]=0\) and \(\mathbb E[NN^\top]=I/2\). The confining drift is stable and the forcing bounded, ensuring the joint invariant law and its requisite moments. Define the \(2\times2\) matrix \(M=\mathbb E[XN^\top]\) in stationarity. The generator applied to the four products \(X_iN_j\), using noise independence, gives the Sylvester equation
\[
K_\theta M+M\Gamma=\frac v2 I,
\qquad\Gamma=\operatorname{diag}(\gamma_1,\gamma_2).
\]
Since both matrices have positive spectrum, the solution is unique. Its \(j\)-th column is \(\frac v2(K_\theta+\gamma_j I)^{-1}e_j\).

**2. Full entropy balance, including reorientation.** Write \(\rho_s(x)\) for the stationary spatial density conditional on internal label \(s\), with its probability weight incorporated, \(F_s(x)=-K_\theta x+v n_s\), and \(J_s=F_s\rho_s-D\nabla\rho_s\). The standard entropy balance for a diffusion coupled to a symmetric finite-state jump chain reads
\[
0=\frac{dS}{dt}=\Pi-\Phi,\quad
\Pi=\sum_s\int\frac{|J_s|^2}{D\rho_s}\,dx
+\sum_{s<t}q_{st}\int(\rho_s-\rho_t)\log\frac{\rho_s}{\rho_t}\,dx,
\quad\Phi=\frac1D\sum_s\int F_s\cdot J_s\,dx.
\]
Both displayed contributions to \(\Pi\) are nonnegative. The jump contribution belongs to total entropy production, not to the medium affinity: \(q_{st}=q_{ts}\). In the stationary total density, \(\nabla\cdot\sum_sJ_s=0\). Integration by parts with the quadratic potential \(\frac12x^\top K_\theta x\) cancels its contribution to \(\Phi\). Also \(\int\nabla\rho_s\,dx=0\). Consequently,
\[
\Pi=\Phi=\frac vD\mathbb E[N\cdot(-K_\theta X+vN)]
=\frac{v^2}{D}-\frac vD\operatorname{tr}(K_\theta M).
\]
Using the cross-moment solution yields
\[
\Pi=\frac{v^2}{2D}\sum_{j=1}^2 \gamma_j e_j^\top(K_\theta+\gamma_jI)^{-1}e_j.
\]
No Gaussian assumption about the joint stationary distribution is needed.

**3. Angular formula.** The spectral projectors of \(K_\theta\) give
\[
e_1^\top(K_\theta+\gamma I)^{-1}e_1
=\frac{\cos^2\theta}{k_1+\gamma}+\frac{\sin^2\theta}{k_2+\gamma},
\]
with the cosines and sines interchanged for \(e_2\). Substitution gives the claimed expression for \(\Pi(\theta)\).

**4. Sharp crossover.** Putting the fractions over a common strictly positive denominator gives the displayed factorization of \(A-B\). Because both \(\gamma_1-\gamma_2\) and \(k_1-k_2\) are negative, its sign is the sign of \(\gamma_1\gamma_2-k_1k_2\). Meanwhile \(\Pi'(\theta)=\frac{v^2}{2D}(B-A)\sin(2\theta)\), strictly of one sign for \(0<\theta<\pi/2\) if the determinant products differ. This proves the unique endpoints and the reversal. At equality,
\[
A-1=\frac{\gamma_1\gamma_2-k_1k_2}{(k_1+\gamma_1)(k_2+\gamma_2)}=0,
\]
so \(A=B=1\) and the universal flat value follows. The strict eigenvalue inequalities exclude the separate trivial angle-flat cases of isotropic confinement or isotropic reorientation.

## Verification
The accompanying executable `verify.py` uses Python 3 standard-library arithmetic only. It independently obtains the entropy flux by solving the full \(8\times8\) linear equations for the four state-conditioned position means, without using the closed spectral formula; 500 deterministic parameter instances agree with the theorem. Another 300 exact rational choices verify both factorized identities, and 19 further deterministic tests probe the flat threshold and alignment signs, for 1,119 successful assertions. Algebraic and finite numerical checks corroborate the direct generator-and-entropy proof and do not replace the universal analytical arguments. Reproduce with `python3 verify.py`.

## Relationship to prior work
Loewe, Kozhukhov, and Shendruk (2023, arXiv:2305.03663) introduce four-direction anisotropic tumble-turn kinetics in free space, without the present pair-dependent U-turn rates, rotated anisotropic confinement, or entropy-optimization statement. Paoluzzi, Puglisi, and Angelani (2024, arXiv:2404.16955), especially Sec. VI, derive a general steady-state entropy-flux formula and the exact expression for isotropically confined particles with constant tumbling rate; the entropy-balance method and isotropic expression are prior work. Garcia-Millan and Pruessner (2020, arXiv:2012.02900) discuss field-theoretic entropy production and harmonic confinement in one spatial dimension. The result claimed here is the exact two-anisotropy angle dependence, its determinant-product alignment reversal, and its nondegenerate universal flat manifold, not the general entropy balance or harmonic moment closure.

## Limitations
The exact result is for a symmetric four-direction internal jump graph, identical propulsion speed in each direction, common isotropic translational thermal diffusion, a positive quadratic trap, constant rates, and ideal stationary ensemble values. Correlated jump asymmetries, odd-under-time-reversal orientation conventions, noisy inference, and interacting particles lie outside the claim. The novelty assessment compares accessible primary literature and indexed mathematical records but is not an exhaustive publication-priority certification; a stronger general theorem for anisotropic colored propulsion and linear drift might subsume this special case. No independent scientific audit has been carried out.

## References
1. B. Loewe, T. Kozhukhov, T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, arXiv:2305.03663 (first public 2023-05-05), Soft Matter 20 (2024), 1133–1150, DOI 10.1039/D3SM00589E.
2. M. Paoluzzi, A. Puglisi, L. Angelani, *Entropy production of run-and-tumble particles*, arXiv:2404.16955 (first public 2024-04-25), Entropy 26 (2024), 443, DOI 10.3390/e26060443.
3. R. Garcia-Millan, G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900 (first public 2020-12-04).
