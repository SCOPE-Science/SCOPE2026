# Irrational sweep-phase law for two-node Verlet spectral deferred correction

## Finding

Consider the velocity-Verlet-preconditioned spectral deferred correction (SDC) method with two Gauss–Legendre nodes, constant stage initialization, and exactly \(k\ge 1\) correction sweeps, applied to the undamped harmonic oscillator \(\ddot x=-\omega^2x\). Let \(h>0\), \(z=h^2\omega^2\), and let \(R_k(z)\in\mathbb R^{2\times2}\) be the one-step matrix on the scaled state \((x,h\dot x)^{\mathsf T}\).

Put
\[
H=\begin{pmatrix}
1/24&1/8-\sqrt3/12\\
1/24&1/24
\end{pmatrix},\qquad
q=\tfrac12(1,1),\qquad
c=\tfrac16(3-\sqrt3,3+\sqrt3)^{\mathsf T}.
\]
For every fixed positive integer \(k\), the exact leading determinant defect is
\[
\boxed{\det R_k(z)-1=a_kz^{k+1}+O_k(z^{k+2}),\qquad
 a_k=(-1)^k qH^kc.}
\]
The eigenvalues of \(H\) are \(re^{\pm i\theta}\), with
\[
r^2=\frac{\sqrt3-1}{288},\qquad
2\cos(2\theta)=\sqrt3-1,\qquad 0<\theta<\frac\pi2.
\]
Furthermore,
\[
\boxed{a_k=(-r)^k\left[\frac12\cos(k\theta)
-\frac{\sqrt{2\sqrt3-3}}6\sin(k\theta)\right].}
\]
The angle \(\theta/\pi\) is irrational. Consequently the set of positive integers \(k\) for which the method is **strictly Schur stable for all sufficiently small positive \(z\)** has natural density \(1/2\), and its complement of locally unstable sweep counts also has density \(1/2\). At most one integer can have \(a_k=0\), and its possible classification does not affect these densities. In particular, neither odd nor even sweep counts eventually guarantee stability in this setting.

For the first four sweep counts, the determinant-defect signs are, respectively, negative, positive, positive, negative. Thus the method is locally stable for one and four sweeps and locally unstable for two and three sweeps, matching the contrasting first four entries for the two-node undamped oscillator in the motivating work.

## Assumptions and scope

The scalar oscillator has \(\omega>0\), exact arithmetic, no friction, and a fixed time step \(h>0\). Its two interior quadrature nodes on the normalized step are \(c_1=(3-\sqrt3)/6\) and \(c_2=(3+\sqrt3)/6\). The initial nodal positions all equal \(x_0\), and the initial nodal velocities all equal \(\dot x_0\), before the first correction sweep. End-point values use the collocation quadrature, not the value at the final interior node. The stability property means that both eigenvalues of the repeated-step matrix \(R_k(z)\) have modulus strictly less than one. In the asymptotic statement, \(k\) is held fixed before \(z\downarrow0\); the small-step threshold may depend on \(k\).

To specify the exact method without implementation conventions, let \(\mathbf1=(1,1,1)^{\mathsf T}\) and let \(Q\) be the \(3\times3\) matrix of integrals of the two Lagrange cardinal polynomials from zero to \(c_i\), with an initial all-zero row and column. It is
\[
Q=\begin{pmatrix}0&0&0\\0&1/4&1/4-\sqrt3/6\\0&1/4+\sqrt3/6&1/4\end{pmatrix}.
\]
Let \(E\) and \(I\) be the strictly lower and lower triangular cumulative substep integration matrices, respectively: \(E_{ij}=c_{j+1}-c_j\) for \(j<i\), \(I_{ij}=c_j-c_{j-1}\) for \(1\le j\le i\), and zero otherwise, using \(c_0=0\). Set \(T=(E+I)/2\) and \(X_{\mathrm{vv}}=ET+(E\circ E)/2\), with \(\circ\) the entrywise product. The nodal position stages are defined by
\[
X^{(0)}=\mathbf1 x_0,\qquad
(I+zX_{\mathrm{vv}})X^{(j+1)}
=\mathbf1 x_0+Q\mathbf1(h\dot x_0)-z(Q^2-X_{\mathrm{vv}})X^{(j)}.
\]
Because \(X_{\mathrm{vv}}\) is strictly lower triangular, every sweep is defined for all \(z\). With \(q_3=(0,1/2,1/2)\), the endpoint is
\[
x_1=x_0+h\dot x_0-zq_3QX^{(k)},\qquad
h\dot x_1=h\dot x_0-zq_3X^{(k)}.
\]
This formulation is the undamped, position-dependent-force specialization of the published Verlet-SDC iteration.

## Proof

**1. Exact two-node compression.** Direct integration of the cardinal polynomials produces the displayed \(Q\). Evaluating the cumulative-substep matrices and the velocity-Verlet position matrix gives
\[
\bigl(Q^2-X_{\mathrm{vv}}\bigr)_{\{1,2\}\times\{1,2\}}=H.
\]
The first row of both \(Q^2\) and \(X_{\mathrm{vv}}\) vanishes, so the two-dimensional subspace of nodal vectors with first coordinate zero is invariant under this difference and under the stage-error propagation operator.

**2. Comparison with the collocation limit.** The exact collocation position stages are
\[
X^*(z)=(I+zQ^2)^{-1}(\mathbf1 x_0+Q\mathbf1(h\dot x_0)).
\]
The resulting two-stage Gauss–Legendre Runge–Kutta endpoint matrix is
\[
R_*(z)=\frac1{z^2+12z+144}
\begin{pmatrix}
z^2-60z+144&12(12-z)\\
12z(z-12)&z^2-60z+144
\end{pmatrix}.
\]
Its determinant equals one identically, a direct algebraic expression of symplecticity. As \(z\downarrow0\), its trace is \(2-z+O(z^2)\), and its lower-left entry is \(-z+O(z^2)\).

Subtracting the exact stage equation from the sweep equation shows that the stage error \(\Delta^{(j)}=X^{(j)}-X^*\) obeys
\[
\Delta^{(j+1)}=-z(I+zX_{\mathrm{vv}})^{-1}
(Q^2-X_{\mathrm{vv}})\Delta^{(j)}.
\]
The initial error has a zero first nodal coordinate. In the column multiplying \(h\dot x_0\), it is \(-Q\mathbf1+O(z)\); in the column multiplying \(x_0\), it is \(O(z)\). Hence the velocity-input column of \(\Delta^{(k)}\), restricted to its final two coordinates, is
\[
(-1)^{k+1}z^kH^kc+O_k(z^{k+1}),
\]
while the position-input column is \(O_k(z^{k+1})\). Subtracting the endpoint maps and expanding their determinants around \(\det R_*=1\) proves
\[
\det R_k(z)-1=(-1)^kqH^kc\,z^{k+1}+O_k(z^{k+2}).
\]
The remainder is analytic for each fixed \(k\), since the Verlet sweep inverse is a finite polynomial in \(z\).

**3. Irrational rotation.** Direct calculation yields \(\operatorname{tr}H=1/12\), \(\det H=(\sqrt3-1)/288\), and \((\operatorname{tr}H)^2-4\det H=(3-2\sqrt3)/144<0\). Writing its conjugate eigenvalues as \(re^{\pm i\theta}\) gives the stated \(r\) and \(2\cos(2\theta)=\sqrt3-1\). If \(\theta/\pi\) were rational, \(e^{2i\theta}\) would be a root of unity, so all algebraic conjugates of \(e^{2i\theta}+e^{-2i\theta}\) would be real and lie in \([-2,2]\). But the algebraic conjugate of \(\sqrt3-1\) is \(-\sqrt3-1<-2\), a contradiction.

Since \(H\) has two distinct conjugate eigenvalues, the scalar sequence \(qH^kc\) is a real sinusoid times \(r^k\). Its value at \(k=0\) is \(1/2\), and its value at \(k=1\) is \(1/24-\sqrt3/72\), yielding the displayed sinusoidal formula. The amplitude is nonzero. The sign of \(a_k\) is therefore the sign of a nonzero sinusoid sampled at the irrational rotation angle \(\theta+\pi\). Irrational circle rotations are equidistributed, and exactly half a circle corresponds to each strict sign. Thus the positive and negative sign sets each have natural density \(1/2\). If two different indices gave zero, their phase difference would be an integer multiple of \(\pi\), contradicting irrationality, so there is at most one exceptional zero.

**4. Transfer of sign to step stability.** For every fixed \(k\ge1\), the endpoint matrix has \(\operatorname{tr}R_k(z)=2-z+O(z^2)\) and \(\det R_k(z)=1+a_kz^{k+1}+O_k(z^{k+2})\). The real quadratic Schur conditions are
\[
1-\det R_k>0,\quad 1-\operatorname{tr}R_k+\det R_k>0,\quad 1+\operatorname{tr}R_k+\det R_k>0.
\]
The latter two have leading terms \(z\) and \(4\), respectively, and are positive for all sufficiently small \(z>0\). If \(a_k<0\), the first is also positive, proving strict stability; if \(a_k>0\), the determinant exceeds one, proving instability. The at-most-one exceptional index has no effect on the natural densities. This establishes the claim.

## Verification

The standalone `verify.py` reconstructs the Gauss–Legendre integration matrix by symbolic integration; constructs both cumulative Verlet matrices; checks the exact compressed matrix, its trace, determinant and angle identity; and verifies the complete Gauss collocation endpoint matrix and its unit determinant. It then verifies the determinant-defect coefficients symbolically for the first six sweeps and independently recomputes the first nine step matrices by high-precision forward substitution through the original sweep equations. The direct step determinants agree in sign and leading asymptotic scale with the theorem. Execute with `python verify.py` using SymPy and mpmath. The arithmetical irrationality and density arguments are mathematical proofs, not finite tests.

## Relationship to prior work

Akramov, Götschel, Minion, Ruprecht and Speck (2023/2024) define this velocity-Verlet SDC scheme and investigate oscillator stability. Their Table 1 records differing two-node limits for the first four sweep counts, and the text explicitly leaves the reason for the observed odd/even behavior unexplained. The exact infinite-sweep-count local stability density and its irrational compression phase are not stated there. The earlier Boris-SDC work of Winkel, Speck and Ruprecht develops related Lorentz-force correction sweeps but does not supply this exact two-node scalar oscillator density law in the accessible material. The present result uses, rather than reclaims, the standard SDC formulas and classical irrational-rotation equidistribution.

A separate first-order, implicit-Euler-preconditioned, three-node Gauss–Lobatto SDC calculation also exhibits an irrational-phase density law in a stiff negative-real-axis limit. That statement concerns a different solver, node set, asymptotic regime and stability multiplier. It does not yield the velocity-Verlet compression or the oscillator determinant defect proved here.

## Limitations

The theorem applies only to the two-node Gauss–Legendre velocity-Verlet-preconditioned method with repeated-constant stage initialization, a scalar undamped harmonic oscillator, fixed finite sweep count, and sufficiently small positive squared frequency-step parameter. It does **not** establish a uniform stability interval over all sweep counts, an exact finite-step stability boundary, or comparable density for more Gauss nodes, other initial stage strategies, damping, nonlinear forces, or alternative preconditioners. The asymptotic half-density is over the integer number of correction sweeps, not over randomly chosen timesteps. Converged Gauss collocation has determinant one and neutral Hamiltonian stability; the finite-sweep strict contraction or expansion approaches that neutral limit as the correction iteration converges.

## References

1. I. Akramov, S. Götschel, M. Minion, D. Ruprecht and R. Speck, *Spectral deferred correction methods for second-order problems*, first public preprint 12 October 2023, arXiv:2310.08352; *SIAM Journal on Scientific Computing* 46 (2024), DOI: 10.1137/23M1592596. In particular, the position-stage sweep, oscillator stability matrix, Section 3 and Table 1.
2. M. Winkel, R. Speck and D. Ruprecht, *A high-order Boris integrator*, arXiv:1409.5677, *Journal of Computational Physics* 295 (2015), 456–474 (background on second-order SDC in Lorentz-force problems).
3. Classical two-stage Gauss–Legendre Runge–Kutta symplecticity and irrational circle-rotation equidistribution are used in their standard finite-dimensional forms; both facts are also verified directly where needed by the displayed formulas.
