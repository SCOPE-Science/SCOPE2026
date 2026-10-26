# Sharp kinetic-energy contractivity of the stiff charged-dust source update

## Finding

The stiff two-stage charged-dust source integrator with rational stability function
\[
R(z)=\frac{1-z}{1-2z+2z^2}
\]
is a contraction **of the entire mass-weighted kinetic-energy norm**, not only of each eigenmode, when its coefficients are frozen and the stated stiff-branch switching criterion is met. The assertion holds for an arbitrary finite number of species, arbitrary positive dust-to-gas mass ratios, arbitrary signed gyrofrequencies, and arbitrary initial relative velocities. On the subspace of zero center-of-mass momentum the contraction is strict if all drag rates are positive. The bound defining the stiff branch is sharp among universal switching constants, including for strictly positive drag.

The underlying matrix result is: if \(A\) is an invertible complex square matrix with \(A+A^*\preceq0\) and \(\sigma_{\min}(A)\ge1/2\), then \(\|R(A)\|_2\le1\). If \(A+A^*\prec0\), the inequality is strict. The coefficient \(1/2\) cannot be reduced uniformly, even for scalar dissipative matrices. Unlike scalar eigenvalue stability, this result applies to nonnormal matrices.

## Assumptions and scope

Fix \(n\ge1\), gas density \(\rho_g>0\), dust densities \(\rho_i>0\), drag rates \(\alpha_i>0\), and real gyrofrequencies \(\Omega_i\). Keep these quantities and the unit magnetic direction constant during a source substep, and neglect external forcing and hydrodynamic transport for that substep. Let \(\epsilon_i=\rho_i/\rho_g\), and let \(\Delta t>0\) denote the complete split-step duration, so that one source half-step has length \(h=\Delta t/2\). Set
\[
r_{\min}=\min_{1\le i\le n}\sqrt{\alpha_i^2+\Omega_i^2}.
\]
The stiff coefficient set is used when \(\Delta t\,r_{\min}\ge1\), equivalently \(h r_{\min}\ge1/2\). Its stage amplification for constant coefficients is exactly \(R(h\mathcal M)\). Here \(\mathcal M\) is the coupled, linear, momentum-conserving gas–dust drag–Lorentz source matrix. The kinetic-energy norm on momenta \(p_g,p_i\in\mathbb R^3\) is
\[
\|p\|_E^2=\frac{\|p_g\|^2}{\rho_g}+\sum_{i=1}^n\frac{\|p_i\|^2}{\rho_i},\qquad E_{\rm kin}=\tfrac12\|p\|_E^2.
\]
Only this linear, frozen-coefficient source map and its exact-arithmetic norm are asserted. The corresponding gas internal-energy correction, state-dependent Picard iterations, forcing and transport are outside the claim.

## Proof

**1. A noncommutative rational contraction identity.** Let \(A\) satisfy the matrix hypotheses and put \(B=A^{-1}\). By congruence,
\[
B+B^*=A^{-*}(A+A^*)A^{-1}\preceq0,
\qquad \|B\|_2\le2.
\]
Define \(D=B^2-2B+2I\) and \(N=B^2-B\). A direct matrix expansion, retaining the order of factors, gives the exact identity
\[
\boxed{D^*D-N^*N=(4I-B^*B)+(B-2I)^*[-(B+B^*)](B-2I).}
\tag{1}
\]
Both terms on the right are positive semidefinite. The zeros of \(z^2-2z+2\) are \(1\pm i\); because the numerical range of \(B\) lies in the closed left half-plane, its spectrum cannot contain these zeros. Hence \(D\) is invertible, and \(R(A)=ND^{-1}\). Equation (1) implies
\[
I-R(A)^*R(A)=D^{-*}(D^*D-N^*N)D^{-1}\succeq0.
\]
If \(A+A^*\prec0\), then \(-(B+B^*)\succ0\), and \(B-2I\) is invertible because \(2\) is outside the left half-plane. Thus the second term of (1) is positive definite, proving strict contraction. The proof uses no normality, eigenbasis or diagonalizability assumption.

**2. Orthogonal relative-coordinate form of the physical generator.** Pass from momentum to mass-weighted velocities \(x_j=\sqrt{\rho_j}\,v_j\), so \(\|p\|_E=\|x\|_2\). On any transverse circular polarization define real star-edge vectors
\[
v_i=\sqrt{\epsilon_i}\,e_g-e_i,\qquad V=[v_1\ \cdots\ v_n],\qquad G=V^*V=I+s s^*,\quad s_i=\sqrt{\epsilon_i}.
\]
The frozen transverse generator is \(M_\pm=VT_\pm V^*\), with \(T_\pm=\operatorname{diag}(-\alpha_i\pm i\Omega_i)\); the sign reflects the choice of polarization and does not affect the argument. The center-of-mass direction is \(\ker V^*\), which is orthogonal to \(\operatorname{ran}V\). Because \(G\succeq I\), the columns of \(Q=VG^{-1/2}\) are orthonormal and the restriction of \(M_\pm\) to relative motion has matrix
\[
M_{\perp,\pm}=Q^*M_\pm Q=G^{1/2}T_\pm G^{1/2}.
\]
Its Hermitian part is \(-G^{1/2}\operatorname{diag}(\alpha_i)G^{1/2}\prec0\). For every \(y\),
\[
\|M_{\perp,\pm}y\|_2
\ge\sigma_{\min}(G^{1/2})^2\min_i|{-\alpha_i\pm i\Omega_i}|\,\|y\|_2
\ge r_{\min}\|y\|_2.
\]
Consequently, \(A=hM_{\perp,\pm}\) satisfies the matrix contraction lemma whenever \(h r_{\min}\ge1/2\). Each transverse polarization contracts strictly. Along the magnetic field the generator is real symmetric negative semidefinite, with strictly negative relative eigenvalues; since \(R(-a)=(1+a)/(1+2a+2a^2)\) lies strictly between zero and one when \(a>0\), the parallel relative subspace also contracts strictly. If the field vanishes, this last argument applies in all three directions.

The zero-momentum relative space is orthogonal to the three-dimensional center-of-mass space in mass-weighted coordinates. The source update is the identity on the latter because \(R(0)=1\). Thus, for every initial state,
\[
\boxed{E_{\rm kin}^{+}\le E_{\rm kin}^{-},}
\]
with strict inequality whenever its relative component is nonzero. This conclusion is a statement about all initial vectors and all mixtures of possibly nonorthogonal eigenmodes, not merely modal damping.

**3. Sharpness of the universal switching coefficient.** On a scalar imaginary argument \(z=it\), direct expansion yields
\[
|1-2it+2(it)^2|^2-|1-it|^2=t^2(4t^2-1),
\]
which is negative for \(0<|t|<1/2\). Sharpness also holds inside the physical positive-drag family. Choose one dust species with \(\epsilon=1/10\), \(\Omega=1\), \(\alpha=1/1000\), and \(h=1/4\). Its relative transverse mode has \(z=(11/40)(-1/1000+i)\), and exact rational arithmetic gives
\[
|R(z)|^2=\frac{688752048400000000}{655451896588494641}>1.
\]
For any constant \(c<1/2\), select \(t\in(c,1/2)\), take sufficiently small positive \(\epsilon\) and \(\alpha\), set \(h\Omega=t\), and use continuity of \(R\). Then \(h\sqrt{\alpha^2+\Omega^2}>c\) while the relative transverse mode amplifies kinetic energy. Therefore no smaller universal coefficient can replace \(1/2\), even when all physical drag coefficients remain strictly positive.

## Verification

The bundled `check.py` checks the noncommutative identity (1), exact rational physical amplification below the threshold, and random physically admissible multicomponent matrix instances at and beyond the branch threshold in all three velocity components. The results serve as independent finite checks; the universal contraction, strictness and optimality statements follow from the above proof.

## Relationship to prior work

Chen et al., *A Nonlinear General Implicit Runge–Kutta Integrator for Multifluid Charged Dust and Gas*, arXiv:2610.18979 (first posted 2026-10-13), supply the stiff stability function, the branch criterion, and a proof that **each source eigenmode** lies inside its scalar absolute-stability region; see their Appendix A, especially (A3)–(A6). Their Appendix B records the general discrete RK energy residual, but does not establish the present all-vector kinetic-energy contraction inequality. An eigenvalue bound alone does not imply operator-norm contraction for a nonnormal matrix. The contribution here is an exact inverse-singular-value matrix inequality and its mass-weighted application, with a sharp switching constant.

Tedeschi-Prades et al., *General Implicit Runge–Kutta Integrators for Multifluid Gas-Dust Aerodynamic Drag*, arXiv:2511.07562 (2025), address neutral aerodynamic drag and its integration; their setting does not furnish this proof for mixed Lorentz–drag couplings and the non-A-stable stiff coefficient set. Classical scalar RK stability and ordinary algebraic-stability criteria are not substituted for a nonnormal energy argument.

## Limitations

All densities, rates and the field direction must be frozen for the homogeneous source substep; the assertion is not a discrete energy inequality for nonlinear state-dependent Picard stages, fluid transport, external forcing, or the entire coupled MHD solver. The sharp scalar threshold describes a sufficient *uniform* branch condition and does not claim necessity for every individual system. In exact arithmetic the contraction may be arbitrarily close to equality as drag tends to zero. The center-of-mass component is conserved, so strict contraction applies only to nonzero relative motion. This work does not establish historical priority beyond the checked sources; equivalent matrix-function inequalities may occur in operator-theoretic literature.

## References

1. M. Chen, H. Li, C.-C. He, B. D. Wibking, M. R. Krumholz, X.-N. Bai, *A Nonlinear General Implicit Runge–Kutta Integrator for Multifluid Charged Dust and Gas*, arXiv:2610.18979 (2026), https://arxiv.org/abs/2610.18979, Sections II.3–II.7 and Appendices A–B.
2. G. Tedeschi-Prades, T. Birnstiel, K. Dolag, B. Ercolano, *General Implicit Runge–Kutta Integrators for Multifluid Gas-Dust Aerodynamic Drag*, arXiv:2511.07562 (2025), https://arxiv.org/abs/2511.07562, Sections II–III.
