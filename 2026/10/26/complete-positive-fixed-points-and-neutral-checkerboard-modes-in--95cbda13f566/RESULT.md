# Complete positive fixed points and neutral checkerboard modes in a degenerate diffusion update

## Finding

For the reaction-free nonstandard diffusion update of Zinihi–Ehrhardt–Sidi Ammi [1], with the coordinatewise mirror-ghost realization of homogeneous Neumann boundaries specified below and exponent \(p>2\), **every strictly positive discrete stationary state is constant on each coordinate-parity class**. On any rectangular two-dimensional grid with at least two intervals in each direction, the entire positive fixed-point set is exactly
\[
\mathcal F_{+}=\bigl\{u_{ij}=c_{i\bmod 2,j\bmod 2}: c_{00},c_{01},c_{10},c_{11}>0\bigr\}.
\]
This classification holds for every positive diffusion coefficient and every positive generalized timestep ratio. In one dimension the exact analogue has two, rather than four, arbitrary positive parity-class values.

In particular, \(u_{ij}=a\) at nodes with even \(i+j\) and \(u_{ij}=b\) at nodes with odd \(i+j\), for any distinct positive \(a,b\), is stationary even though all axial edges have nonzero jumps. On the \((N+1)\times(N+1)\) grid of \([0,1]^2\), with \(h=1/N\) and \(N\ge2\), its nearest-neighbor edge-gradient energy is exactly
\[
\mathcal E_{h,p}(u):=h^2\!\sum_{\{v,w\}\in E_h}\!\left|\frac{u_v-u_w}{h}\right|^p
=2\left(1+\frac1N\right)N^p|a-b|^p.
\]
For fixed \(a\ne b\), this energy diverges as \(h\to0\), although the numerical state remains unchanged at every iteration. The continuous reaction-free Neumann \(p\)-heat equation on a connected domain admits only spatially constant weak equilibria.

There is also an exact local degeneracy: **when \(p>3\), the Jacobian of the full numerical update at every state in \(\mathcal F_+\) is the identity matrix**, including at nonconstant checkerboards. This is a one-step linear-neutrality statement, not a claim of nonlinear attraction or divergence.

## Assumptions and scope

Let \(d=2\), with indices \(0\le i\le N_x\), \(0\le j\le N_y\), integers \(N_x,N_y\ge2\), equal positive spacing \(h\), exponent \(p>2\), and \(\tau=\lambda\phi(k)/h^2>0\). Set the reaction function \(f\equiv0\). Extend grid values by coordinatewise even reflection: \(u_{-1,j}=u_{1,j}\), \(u_{N_x+1,j}=u_{N_x-1,j}\), \(u_{i,-1}=u_{i,1}\), and \(u_{i,N_y+1}=u_{i,N_y-1}\), with successive reflection at corners. Coefficients and the products below are extended by the same rule, equivalently by evaluating the centered-gradient magnitude on the reflected array.

Define the centered differences and coefficient by
\[
G_hu_{ij}=\left(\frac{u_{i+1,j}-u_{i-1,j}}{2h},\frac{u_{i,j+1}-u_{i,j-1}}{2h}\right),
\qquad q_{ij}(u)=|G_hu_{ij}|^{p-2},\qquad w_{ij}(u)=u_{ij}q_{ij}(u).
\]
At zero gradient the coefficient is exactly zero, since \(p>2\). The numerical update is the explicit rational map
\[
(T_\tau u)_{ij}=
\frac{u_{ij}+\tau\bigl(w_{i-1,j}+w_{i+1,j}+w_{i,j-1}+w_{i,j+1}\bigr)}{1+4\tau q_{ij}}.
\tag{A}
\]
This is equation (6) of [1] specialized to zero reaction and given an explicit complete second-order mirror-ghost closure. Every denominator is positive on the nonnegative coefficient domain.

In \(d=1\), use \(0\le i\le N\), \(N\ge2\), centered gradient \((u_{i+1}-u_{i-1})/(2h)\), reflecting endpoint ghosts, and equation (7) of [1]: replace the four neighbor terms and central factor \(4\) in (A) with two terms and factor \(2\), respectively. Statements concern strictly positive real grid data; positivity is used in the reverse fixed-point implication.

## Proof

**1. Exact reduction to a reflecting harmonic problem.** For a fixed point \(T_\tau u=u\), multiply (A) by its positive denominator, subtract \(u_{ij}\), and divide by \(\tau>0\). The resulting identity is
\[
4w_{ij}=w_{i-1,j}+w_{i+1,j}+w_{i,j-1}+w_{i,j+1}.
\tag{B}
\]
At the boundary, the quantities \(w\) inherit even reflection because the magnitude of a centered gradient is preserved by coordinate reflection, while \(u\) itself is reflected. Thus (B) is precisely the five-point reflecting discrete Neumann harmonic equation. There is no differentiability assumption in this step.

**2. A reflecting harmonic array is constant.** Let \(M\) be the maximum of \(w\) on the finite grid and choose a maximizing node. Equation (B) says its value equals the arithmetic mean of four reflected neighboring values, all at most \(M\); hence every corresponding neighbor has value \(M\). By repeating along interior horizontal and vertical nearest-neighbor edges, and using connectedness of the rectangular grid, every node has value \(M\). Consequently \(w_{ij}=M\) for every node. The same argument with two neighbors works in one dimension.

**3. The corner pins the harmonic constant to zero.** Reflection gives \(G_hu_{00}=(0,0)\), hence \(q_{00}=0\) for \(p>2\), and \(w_{00}=u_{00}q_{00}=0\). Since \(w\) is constant, \(w\equiv0\). Because all \(u_{ij}>0\), every \(q_{ij}=0\), so every centered gradient is zero:
\[
u_{i+1,j}=u_{i-1,j},\qquad u_{i,j+1}=u_{i,j-1}
\]
wherever the two displayed indices belong to the grid (the boundary equalities are automatic by mirror reflection).

**4. Exhaustive parity classification.** The first recurrence forces values to be constant separately on even and odd \(i\) for each fixed \(j\). The second forces the resulting two values to be constant separately on even and odd \(j\). Hence the array is determined by exactly four positive constants \(c_{00},c_{01},c_{10},c_{11}\), and no other strictly positive fixed points exist. Conversely, any such array has every centered difference zero, so \(q\equiv w\equiv0\) and (A) returns the unchanged array. In one dimension the same argument gives exactly two arbitrary positive parity-class values. For \(N_x,N_y\ge2\), all four parity classes occur.

**5. Edge energy and continuum contrast.** A checkerboard with values \(a\ne b\) has \(N(N+1)\) horizontal edges and the same number of vertical edges; each contributes \(h^{2-p}|a-b|^p\). Substituting \(h=1/N\) proves the displayed identity. By contrast, if a weak stationary state of the continuous Neumann equation solves \(-\operatorname{div}(|\nabla u|^{p-2}\nabla u)=0\), testing its weak form by \(u\) modulo its mean yields \(\int_\Omega|\nabla u|^p=0\), so \(u\) is constant on a connected domain.

**6. Identity Jacobian for \(p>3\).** In finite dimensions, \(z\mapsto |z|^{p-2}\) is differentiable at \(z=0\) with derivative zero when \(p>3\). At a parity-class state \(u_*\), every \(G_hu_*=0\). Thus \(Dq(u_*)=0\) and \(Dw(u_*)=0\). Differentiating (A), whose denominator is \(1\) there, gives \(DT_\tau(u_*)=I\) exactly. No assertion of differentiability of \(q\) at the origin is made for \(2<p\le3\).

## Verification

The accompanying standard-library Python file `check.py` evaluates the stated source-type map with exact rational arithmetic at \(p=4\) and \(p=6\). It tests parity-class fixed states for multiple rectangular grids, positive steps, and arbitrary positive class values; finite random-array fixed-point equivalence against parity classes; the exact edge-energy count for integer exponents; and quadratic vanishing of the update defect near checkerboards for \(p=4\). Execution returned `EXACT_CHECKS_PASSED 982`. In particular, at \(N=4\), \(p=4\), \(a=1\), \(b=2\), the exact edge energy is \(640\).

These finitely many rational checks are regression tests only. The all-grid, all-real-exponent, all-positive-step fixed-point classification and the \(p>3\) Jacobian statement are established by the proof above, not by enumeration.

## Relationship to prior work

Zinihi, Ehrhardt, and Sidi Ammi [1], first publicly released July 1, 2026, provide the nonlinear two-level flux formula (equations (5)–(7)) and prove positivity and preservation of *constant* equilibria (Theorems 1–2). Their investigated statements do not classify all discrete positive stationary states or the derivative at nonconstant states. The finding here is explicitly conditional on the standard coordinatewise Neumann mirror completion and zero reaction; it does not revisit the truth of the source's positivity theorem.

Odd–even decoupling of centered derivatives is a well-established phenomenon. Reiss [2, Introduction] describes this mechanism for collocated-grid Navier–Stokes discretizations, including the two-step difference composition. The generic parity warning and its numerical remedies are **not claimed as new**. The present classification additionally exploits the source-specific **product** \(u|G_hu|^{p-2}\), Neumann harmonic equation, the corner coefficient zero, and strict positivity to characterize *every* fixed point of (A), derive the exact positive high-energy stationary family, and identify the neutral Jacobian regime.

Andreianov, Boyer, and Hubert [3] analyze different, admissible locally conservative finite-volume discretizations of stationary \(p\)-Laplacian equations with homogeneous **Dirichlet** data, uniquely minimizing a strictly convex discrete energy (Theorem 2.12). This is a useful structural contrast, not an instance of (A). Their nonadmissible finite-volume variants do not supply a stationary-state classification for the 2026 two-time-level reaction-free Neumann map.

## Limitations

The result is about a *specified* reflected-grid completion of the update (A); the source displays corner-ghost equalities but does not present all side ghost assignments explicitly. Other boundary treatments can change the set of equilibria. The proof assumes nonzero mesh spacing, \(\tau>0\), strictly positive grid data, \(p>2\), and zero reaction. It does not classify equilibria with zeros, singular diffusion exponents \(1<p<2\), or nonzero reaction. The identity-Jacobian conclusion requires \(p>3\) and does not establish nonlinear orbital stability. The edge energy is a defined nearest-neighbor diagnostic, not a claim about discrete energy monotonicity of the update. High-frequency exact stationary checkerboards do not contradict convergence assertions made under smooth-data and mesh-timestep assumptions.

The broader historical priority of this exact scheme-specific fixed-point classification remains open to independent verification; older centered-gradient work could contain an equivalent statement under another formulation.

## References

[1] A. Zinihi, M. Ehrhardt, M. R. Sidi Ammi, *A Nonstandard Finite Difference Scheme for a Nonlinear Parabolic Equation with p-Laplacian-Type Diffusion*, arXiv:2607.00489, first public 2026-07-01. https://arxiv.org/abs/2607.00489

[2] J. Reiss, *A family of energy stable, skew-symmetric finite difference schemes on collocated grids*, arXiv:1402.0998 (2014), particularly §1–2. https://arxiv.org/abs/1402.0998

[3] B. Andreianov, F. Boyer, F. Hubert, *Finite volume schemes for the p-Laplacian on Cartesian meshes*, ESAIM: Mathematical Modelling and Numerical Analysis 38 (2004), 931–959, doi:10.1051/m2an:2004045. https://doi.org/10.1051/m2an:2004045
