# Temporal off-shell diffusivities form a Hausdorff moment hierarchy
## Finding
Consider the class of causal relaxational linear theories used in Gavassino's off-shell formulation of relativistic hydrodynamics. At zero wave number, write the resummed diffusivity as
\[
\mathfrak D(z,0)=\sum_{n\ge 0}A_n z^n,\qquad z=i\omega.
\]
Let \(S\) denote the positive self-adjoint nonhydrodynamic relaxation operator and let \(U\) map a conserved-density vector to its nonconserved current component. The source representation gives
\[
\mathfrak D(z,0)=U^*(S-z)^{-1}U,
\qquad
A_n=U^*S^{-(n+1)}U.
\]
Because the source assumes \(\operatorname{spec}(S)\subset[1/\tau_g,\infty)\), the operator \(T=S^{-1}\) has spectrum in \([0,\tau_g]\). Hence there is a positive matrix-valued measure \(N\) supported on \([0,\tau_g]\) such that
\[
A_n=\int_{0}^{\tau_g}t^n\,dN(t).
\]
Thus the complete zero-wave-number temporal coefficient sequence is a matrix Hausdorff moment sequence. In particular, for all integers \(n,r\ge0\),
\[
\sum_{j=0}^{r}(-1)^j\binom rj\tau_g^{\,r-j}A_{n+j}\succeq0,
\]
and every block Hankel matrix and its support-shift obey
\[
[A_{i+j}]_{i,j=0}^{m}\succeq0,
\qquad
\tau_g[A_{i+j}]_{i,j=0}^{m}-[A_{i+j+1}]_{i,j=0}^{m}\succeq0.
\]
For any conserved direction \(v\) with nonzero dissipative coupling, define \(a_n=v^*A_nv\). Then
\[
q_n=\frac{a_{n+1}}{a_n}
\]
is nondecreasing and converges to the largest inverse relaxation rate in the spectral support coupled to \(v\). Calling this coupled longest relaxation time \(\tau_c(v)\),
\[
q_n\uparrow\tau_c(v)\le\tau_g.
\]
Equivalently, the finite-order estimates \(a_n/a_{n+1}\) decrease to the coupled nonhydrodynamic gap \(1/\tau_c(v)\).

For the source's one-dimensional Fokker-Planck example, setting \(k=0\) in its exact formula gives
\[
\mathfrak D_{nn}(z,0)
=\mathfrak D\,C(\mathfrak D z)^2,
\qquad
C(x)=\frac{1-\sqrt{1-4x}}{2x}.
\]
Since \(C(x)^2=\sum_{n\ge0}C_{n+1}x^n\), with \(C_j\) the Catalan numbers,
\[
A_n=C_{n+1}\mathfrak D^{n+1},
\qquad
\frac{A_{n+1}}{A_n}
=4\mathfrak D-\frac{6\mathfrak D}{n+3}
\uparrow4\mathfrak D=\tau_g.
\]
Thus finite temporal off-shell coefficients recover the nonhydrodynamic relaxation edge monotonically in this exactly solvable kinetic model.
## Assumptions and scope
The theorem uses exactly the anchor's linear-response assumptions: the nonhydrodynamic relaxation operator is self-adjoint and positive, its spectrum is bounded below by \(1/\tau_g\), and the current coupling is bounded. The moment hierarchy concerns the temporal expansion at \(k=0\). It does not assert analogous positivity for mixed space-time coefficients, where the compressed velocity operator need not commute with the relaxation operator.

The coupled time \(\tau_c(v)\) is the largest point in the support of the scalar spectral measure seen by direction \(v\). It can be strictly smaller than the global \(\tau_g\) if that direction is orthogonal to the globally slowest mode. If the dissipative coupling vanishes in direction \(v\), all \(a_n\) vanish and the ratio statement is inapplicable.
## Proof
Put \(T=S^{-1}\). The spectral theorem gives a projection-valued measure \(E_T\) on \([0,\tau_g]\). With \(M(B)=U^*E_T(B)U\), define the positive matrix measure \(dN(t)=t\,dM(t)\). Then
\[
A_n=U^*T^{n+1}U=\int t^n\,dN(t),
\]
which proves the moment representation.

For the finite-difference constraint, expand the polynomial \((\tau_g-t)^r\):
\[
\sum_{j=0}^{r}(-1)^j\binom rj\tau_g^{\,r-j}A_{n+j}
=\int t^n(\tau_g-t)^r\,dN(t)\succeq0.
\]
For vectors \(x_0,\ldots,x_m\) in the conserved space,
\[
\sum_{i,j}x_i^*A_{i+j}x_j
=\int\left\|\sum_i t^i x_i\right\|_{dN(t)}^2\ge0,
\]
which proves block-Hankel positivity; inserting the nonnegative factor \(\tau_g-t\) proves the shifted support constraint.

Fix \(v\) and let \(d\nu_v(t)=v^*dN(t)v\). Then \(a_n=\int t^n d\nu_v(t)\). Cauchy-Schwarz gives
\[
a_{n+1}^2\le a_na_{n+2},
\]
so \(q_n=a_{n+1}/a_n\) is nondecreasing. It is also bounded above by the essential supremum \(\tau_c(v)\) of the support. Standard concentration of the tilted measures \(t^n d\nu_v/a_n\) near their right endpoint gives \(q_n\to\tau_c(v)\). A direct proof is obtained by choosing any \(b<\tau_c(v)\): the positive mass on \((b,\tau_c(v)]\) eventually dominates the mass on \([0,b]\), forcing \(\liminf q_n\ge b\); then let \(b\uparrow\tau_c(v)\).

For the Fokker-Planck model, the anchor's exact formula at \(k=0\) reduces with \(q=\sqrt{1-4\mathfrak Dz}\) to
\[
\mathfrak D_{nn}(z,0)=\frac{1-q}{z(1+q)}=\frac{4\mathfrak D}{(1+q)^2}.
\]
The Catalan generating function satisfies \(C(x)=2/(1+\sqrt{1-4x})\), proving \(\mathfrak D_{nn}=\mathfrak D C(\mathfrak Dz)^2\). The identity \(C(x)^2=\sum_{n\ge0}C_{n+1}x^n\) gives the coefficient formula. Finally,
\[
\frac{C_{n+2}}{C_{n+1}}=\frac{2(2n+3)}{n+3}=4-\frac{6}{n+3},
\]
so the ratio converges monotonically to \(4\mathfrak D\), which is exactly the relaxation time stated by the anchor for this example.
## Verification
The operator argument is infinite-dimensional and analytic; no finite experiment is used as a substitute for it. The accompanying checker verifies the Catalan coefficient identity and ratio law exactly with rational arithmetic through multiple orders, tests scalar Hausdorff finite differences for discrete relaxation spectra, and checks the monotonicity and support bounds for representative positive measures.

As a source-level consistency check, the formula gives \(A_0=\mathfrak D\) and \(A_1=2\mathfrak D^2\), matching the anchor's explicitly printed first temporal off-shell coefficient. It also recovers \(\tau_g=4\mathfrak D\), matching the causal-diamond edge of the Fokker-Planck example.
## Relationship to prior work
Gavassino derives the resolvent formula, the causal-diamond convergence domain, absolute bounds on each mixed gradient coefficient, and positivity of the resummed diffusivity inside the diamond. The paper emphasizes that all-order off-shell coefficients encode nonhydrodynamic information, but it does not state the Hausdorff finite-difference hierarchy, block-Hankel constraints, adjacent-ratio gap bounds, or the Catalan coefficient law above.

Matrix-valued Herglotz and Stieltjes theory supplies general spectral-representation machinery for positive operator-valued resolvents. Linear viscoelasticity also has a mature relaxation-spectrum language. Those broader theories explain why moment methods are natural, but the literature inspected did not state the present consequence for the off-shell relativistic-hydrodynamic diffusivity coefficients or the monotone finite-order recovery of the coupled nonhydrodynamic gap. The finding is therefore an application and sharpening of the anchor's new hydrodynamic representation, not a claim that moment theory itself is new.
## Limitations
The result is restricted to \(k=0\) temporal coefficients. It does not show that the finite-order ratio reaches the global gap when the measured current direction fails to couple to the globally slowest mode. It does not solve the inverse moment problem from noisy experimental coefficients, and it does not establish optimal statistical confidence bounds under measurement error. Very recent or differently indexed work could contain an equivalent hydrodynamic specialization; this remains the principal originality risk.
## References
1. L. Gavassino, *The causal diamond of relativistic hydrodynamics*, arXiv:2610.02416v1 (2026), first public 2026-10-01, https://arxiv.org/abs/2610.02416.
2. F. Gesztesy and E. Tsekanovskii, *On Matrix-Valued Herglotz Functions*, Mathematische Nachrichten 218 (2000), 61–138, DOI: 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D.
3. J. Song and N. Holten-Andersen, *Non-Maxwellian viscoelastic stress relaxations in soft matter*, Soft Matter 19 (2023), 7885–7906, DOI: 10.1039/D3SM00736G.
