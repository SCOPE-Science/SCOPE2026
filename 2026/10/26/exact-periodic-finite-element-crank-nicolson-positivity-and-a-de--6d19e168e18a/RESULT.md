# Exact periodic finite-element Crank–Nicolson positivity and a decreasing mesh-size threshold

## Finding
Let \(n\ge3\) equally spaced nodes discretize a periodic interval by continuous piecewise-linear elements, and let \(h>0\) be each element's length. The consistent-mass, unit-diffusivity Crank–Nicolson heat step is
\[
P_n(r)=(M+\tau K/2)^{-1}(M-\tau K/2),\qquad r=\tau/h^2\ge0.
\]
For \(n=3\), every entry is nonnegative exactly for \(0\le r\le1\). For every \(n\ge4\), **the complete positivity set** is
\[
\boxed{\quad \{0\}\ \cup\ [1/3,\rho_n]\quad}.
\]
The finite-size upper thresholds are unique and strictly decrease with the number of nodes:
\[
\rho_3=1,\qquad \rho_4=\frac{1+\sqrt3}{3},\qquad
\rho_n\searrow\rho_\infty=\frac{5+\sqrt{33}}{12}=0.895380220544836\ldots .
\]
For an exact finite-size formula, let \(q_n\in(0,1)\) be the unique solution of
\[
(1-q_n)\{8(1+q_n^n)+4(q_n+q_n^{n-1})\}
 =6(1+q_n)(1-q_n^n).
\]
Then
\[
\rho_n=\frac13+\frac{2q_n}{(1-q_n)^2}.
\]
When \(n\ge4\) and \(0<r<1/3\), a coefficient connecting nodes two positions apart is strictly negative. When \(r>\rho_n\), the diagonal is strictly negative. Between these two boundaries every off-diagonal coefficient is nonnegative (strictly positive when \(r>1/3\)); positivity at \(r=0\) is the identity-step exception.

## Assumptions and scope
All assertions concern exact real arithmetic and the entrywise order on the nodal update matrix. The spatial domain is a circle of circumference \(nh\); diffusion coefficient is exactly one, the mesh is uniform, no forcing is added, the periodic degrees of freedom are not Dirichlet-eliminated, and the spatial mass matrix is **consistent**, not lumped. The graph of spatial neighbors is the simple cycle for every \(n\ge3\), including the triangle when \(n=3\). No time-step accuracy or floating-point positivity statement is made.

Let \(S\) denote cyclic shift on \(\mathbb R^n\), with \(S^n=I\). Standard element assembly gives
\[
M=\frac h6(4I+S+S^{-1}),\qquad K=\frac1h(2I-S-S^{-1}).
\]
In particular, if \(A=(6/h)(M+\tau K/2)\) and \(H=(6/h)M\), then
\[
H=4I+S+S^{-1},\quad
A=aI+b(S+S^{-1}),\quad a=4+6r,\quad b=1-3r,
\]
and
\[
P_n(r)=2A^{-1}H-I.
\]
The matrix \(A\) is positive definite for every \(r\ge0\), since both \(M\) and \(K\) are symmetric positive (semi)definite, respectively.

## Proof
**1. The small-step obstruction and its sharp boundary.** The case \(r=0\) gives \(P_n(0)=I\). For \(r=1/3\), \(b=0\), \(A=6I\), and hence \(P_n(1/3)=H/3-I\). Its diagonal entries are \(1/3\), neighboring entries are \(1/3\), and all other entries vanish, so it is nonnegative.

For \(0<r<1/3\), \(b>0\). Set
\[
\Delta=\sqrt{a^2-4b^2}>0,\qquad
\zeta=-\frac{2b}{a+\Delta}\in(-1,0).
\]
The inverse \(G=A^{-1}\) has the cyclic Green-function entries
\[
G_{0j}=\frac{\zeta^j+\zeta^{n-j}}{\Delta(1-\zeta^n)},
\qquad 0\le j\le n-1.\tag{1}
\]
One proof is to periodize the absolutely summable infinite-lattice Green function \(\zeta^{|j|}/\Delta\), whose tridiagonal recurrence has characteristic root \(\zeta\); uniqueness of the inverse on the finite cycle identifies the sum. When \(n\ge4\), \(G_{02}>0\): for even \(n\), its numerator is a sum of positive even powers; for odd \(n\ge5\), it is \(|\zeta|^2-|\zeta|^{n-2}>0\). All denominators are positive. From the row-two equation \(aG_{02}+b(G_{01}+G_{03})=0\),
\[
(P_n(r))_{02}
=2\{4G_{02}+G_{01}+G_{03}\}
=-\frac{36r}{b}G_{02}<0.
\]
Therefore the lower threshold is necessary for every \(n\ge4\).

For \(n=3\), direct decomposition into the constant mode and its orthogonal complement gives diagonal entry \((1-r)/(1+3r)\) and each off-diagonal entry \(2r/(1+3r)\). This proves the separate interval \([0,1]\).

**2. Above the lower threshold only the diagonal matters.** For \(r>1/3\) put \(c=3r-1>0\). Then \(A=aI-c(S+S^{-1})\) and \(a=2c+6>2c\). It is an irreducible, strictly diagonally dominant Stieltjes matrix, so \(A^{-1}\) is strictly entrywise positive. Since \(H\) is entrywise nonnegative with positive diagonal, the off-diagonal entries of \(P_n(r)=2A^{-1}H-I\) are strictly positive. The diagonal entries coincide by periodic translation symmetry.

The Fourier modes with angles \(\theta_k=2\pi k/n\) give the eigenvalues of \(P_n(r)\) as
\[
\phi_k(r)=\frac{m_k-3r\kappa_k}{m_k+3r\kappa_k},\quad
m_k=4+2\cos\theta_k>0,\quad
\kappa_k=2-2\cos\theta_k\ge0.
\]
Thus the common diagonal is
\[
f_n(r)=\frac1n\sum_{k=0}^{n-1}\phi_k(r),\quad
f_n'(r)=-\frac6n\sum_{k=1}^{n-1}
\frac{m_k\kappa_k}{(m_k+3r\kappa_k)^2}<0.
\]
We have \(f_n(1/3)=1/3\) and \(\lim_{r\to\infty}f_n(r)=2/n-1<0\). There is exactly one \(\rho_n>1/3\) with \(f_n(\rho_n)=0\). This establishes the complete positivity sets.

**3. Closed cyclic root law and its monotone limiting threshold.** With \(r>1/3\), write
\[
q=\frac{2c}{a+\Delta}\in(0,1),\quad
\Delta=\sqrt{a^2-4c^2},\quad
c=\frac{6q}{(1-q)^2},\quad
\Delta=\frac{6(1+q)}{1-q}.
\]
The positive cyclic Green function is now obtained from (1) with \(\zeta=q\):
\[
G_{00}=\frac{1+q^n}{\Delta(1-q^n)},\qquad
G_{01}=\frac{q+q^{n-1}}{\Delta(1-q^n)}.
\]
Therefore
\[
f_n(r)=8G_{00}+4G_{01}-1
=\frac{8(1+q^n)+4(q+q^{n-1})}{\Delta(1-q^n)}-1.
\]
Setting this equal to zero and using the explicit \(\Delta\) gives precisely the finite-size equation in the Finding section. Uniqueness follows from strict monotonicity of \(f_n\) and of the map \(q\mapsto 1/3+2q/(1-q)^2\).

For fixed \(q\in(0,1)\), the infinite-lattice return coefficient is
\[
f_\infty(r)=\frac{8+4q}{\Delta}-1
=\frac{1-5q-2q^2}{3(1+q)}.
\]
Moreover, the **exact finite-size correction** is
\[
f_n(r)-f_\infty(r)
=\frac{4q^{n-1}(1+4q+q^2)}{\Delta(1-q^n)}>0.
\]
It strictly decreases with \(n\), since \(q^{n-1}/(1-q^n)\) does. Hence \(f_n(r)\) strictly decreases with \(n\) at every fixed \(r>1/3\), so its unique zeros satisfy \(\rho_{n+1}<\rho_n\). Uniform convergence on each compact positive-\(q\) interval, or a direct root-bracketing argument, gives convergence to the unique zero of \(f_\infty\), namely \(q_\infty=(\sqrt{33}-5)/4\), and substitution yields
\[
\rho_\infty=\frac13+\frac{2q_\infty}{(1-q_\infty)^2}
=\frac{5+\sqrt{33}}{12}.
\]
For \(n=4\), evaluation of the four Fourier modes gives
\[
f_4(r)=-\frac{9r^2-6r-2}{(3r+2)(6r+1)},
\]
so \(\rho_4=(1+\sqrt3)/3\); the separate triangle formula above gives \(\rho_3=1\). This completes the proof.

## Verification
The standalone standard-library Python script `verify_periodic_cn.py` constructs each consistent-mass Crank–Nicolson matrix by exact-rational Gaussian elimination for \(3\le n\le13\) and eleven prescribed rational step ratios, checking nonnegativity, negative distance-two witnesses, cyclic invariance, row sums, and the Fourier diagonal independently. It re-evaluates all 121 exact-rational matrices, numerically brackets the upper thresholds, checks their strict decrease over the tested sizes, and checks the analytic limiting radical to reported precision. The unbounded-in-\(n\) theorem is proved above, not inferred from those finite tests.

To reproduce: run `python verify_periodic_cn.py` using Python 3 without third-party packages. Its expected final line begins `exact-rational matrices: 121`.

## Relationship to prior work
The detailed 2006 study by Faragó and Horváth analyzes positivity and maximum principles for parabolic Galerkin schemes with **Dirichlet-type boundary data**. Its Theorems 6.4–6.5 give one-dimensional time-step restrictions for that setting, but not a periodic cycle-size-dependent cutoff. Li and Huang's 2012 preprint, Theorem 3.1 and Remark 3.1, provides a sufficient interval for consistent finite elements and \(\theta\)-stepping (in the unit-diffusivity, one-dimensional, uniform case, \(1/3\le r\le2/3\) for Crank–Nicolson). It does not assert the present necessity, finite-size law, or sharp periodic upper endpoint.

Higueras and Roldán (2023) obtain exact mesh-dependent Crank–Nicolson positivity bounds for central finite differences with homogeneous Dirichlet conditions, a different spatial operator and boundary geometry. Two indexed reports on filtered nearest-neighbor-lattice Crank–Nicolson and on finite-state Markov-generator resolvents likewise do not cover unfiltered, consistent-mass finite-element cycles: the former changes the time step by backward-Euler filtering, and the latter requires a Markov generator, whereas \(-M^{-1}K\) has negative off-diagonal entries at distance two for \(n\ge4\). Their abstract mathematical resolvent and periodization techniques are related, but do not imply the two-sided interval or the exact upper root here.

The exact difference between the sufficient \(2/3\) upper bound and the sharp periodic limit \((5+\sqrt{33})/12\) is a practically motivated positivity margin; the exponentially decaying finite-size correction quantifies finite-mesh effects that do not follow from the prior sufficient restrictions.

## Limitations
Only the uniform, periodic, one-dimensional unit-diffusivity consistent-mass \(P_1\) method is classified. Nonuniform meshes, varying diffusivity, sources, reactions, nonperiodic boundaries, different time integrators, rounding errors, and temporal error tolerances are outside the theorem. No claim is made that related general matrix criteria are new; the contribution is the **sharp, complete periodic finite-element classification** and its monotone finite-size limit. Literature indexing is not an exhaustive novelty guarantee, particularly for older studies of positivity on cyclic tridiagonal systems.

## References
1. I. Faragó and R. Horváth, “Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems,” *SIAM Journal on Scientific Computing* 28 (2006), 2313–2336, DOI: 10.1137/050627241. (Author-shared full text examined, especially Sections 6–7.)
2. X. Li and W. Huang, “Maximum principle for the finite element solution of time dependent anisotropic diffusion problems,” arXiv:1209.5657 (first posted 2012-09-25); *Numerical Methods for Partial Differential Equations* 29 (2013), 1963–1985.
3. I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation,” arXiv:2301.01066 (2023), especially Sections 1–3.
4. “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” publicly indexed mathematical report (2026); proof concerns a filtered nearest-neighbor finite-difference lattice, not a consistent finite-element mass matrix.
5. “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains,” publicly indexed mathematical report (2026); proof concerns Markov-generator matrices, not the consistent-mass finite-element generator here.
