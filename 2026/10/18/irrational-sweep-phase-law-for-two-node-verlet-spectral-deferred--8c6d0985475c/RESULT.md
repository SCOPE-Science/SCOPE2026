# Irrational sweep-phase law for two-node Verlet spectral deferred correction

## Finding

Consider velocity-Verlet-preconditioned spectral deferred correction (SDC) with two Gauss–Legendre nodes, constant stage initialization and exactly \(k\ge1\) correction sweeps, applied to the undamped oscillator \(\ddot x=-\omega^2x\). Write \(z=h^2\omega^2\), and let \(R_k(z)\) be the one-step matrix on \((x,h\dot x)^{\mathsf T}\). Put
\[
H=\begin{pmatrix}1/24&1/8-\sqrt3/12\\1/24&1/24\end{pmatrix},\qquad
q=\tfrac12(1,1),\qquad c=\tfrac16(3-\sqrt3,3+\sqrt3)^{\mathsf T}.
\]
For each fixed positive integer \(k\),
\[
\det R_k(z)-1=a_k z^{k+1}+O_k(z^{k+2}),\qquad a_k=(-1)^k qH^kc.
\]
The eigenvalues of \(H\) are \(re^{\pm i\theta}\), where
\[
r^2=\frac{\sqrt3-1}{288},\qquad 2\cos(2\theta)=\sqrt3-1,\qquad 0<\theta<\frac\pi2.
\]
The coefficients satisfy
\[
a_k=(-r)^k\left[\tfrac12\cos(k\theta)-\tfrac{\sqrt{2\sqrt3-3}}6\sin(k\theta)\right].
\]
The angle \(\theta/\pi\) is irrational. The sweep counts giving strict Schur stability for all sufficiently small positive \(z\) have natural density \(1/2\); the sweep counts giving instability for all sufficiently small positive \(z\) also have density \(1/2\). Neither parity eventually guarantees stability. For \(k=1,2,3,4\), the signs of the defect are respectively negative, positive, positive, negative, so precisely one and four sweeps are locally stable among those four counts.

## Assumptions and exact method

Take \(\omega,h>0\) and exact arithmetic. Use the initial node \(c_0=0\) and interior nodes \(c_1,c_2\) given by \(c\) above. Both positions and velocities are initialized by their constant initial values. The step output uses collocation quadrature, not the last interior stage. The limit \(z\downarrow0\) is taken at fixed \(k\); its stability threshold need not be uniform in \(k\).

Write \(\mathbf1=(1,1,1)^{\mathsf T}\) and \(\mathrm{Id}_3\) for the identity matrix. Let
\[
Q=\begin{pmatrix}0&0&0\\0&1/4&1/4-\sqrt3/6\\0&1/4+\sqrt3/6&1/4\end{pmatrix}.
\]
This is the integral matrix of the two interior cardinal polynomials on the normalized step, with an added zero row and column for stage 0. Define cumulative substep quadratures with indices \(0,1,2\): \(E_{ij}=c_{j+1}-c_j\) for \(j<i\), and \(B_{ij}=c_j-c_{j-1}\) for \(1\le j\le i\), with other entries zero. Put \(T=(E+B)/2\) and \(X_{\rm vv}=ET+(E\circ E)/2\), where \(\circ\) is entrywise multiplication. The sweep and endpoint formulas, with \(q_3=(0,1/2,1/2)\), are
\[
X^{(0)}=\mathbf1 x_0,\qquad
(\mathrm{Id}_3+zX_{\rm vv})X^{(j+1)}=\mathbf1 x_0+Q\mathbf1(h\dot x_0)-z(Q^2-X_{\rm vv})X^{(j)},
\]
\[
x_1=x_0+h\dot x_0-zq_3QX^{(k)},\qquad h\dot x_1=h\dot x_0-zq_3X^{(k)}.
\]
The strictly lower triangular \(X_{\rm vv}\) makes each sweep well defined for all \(z\). These are the undamped position-dependent-force specialization of the published iteration.

## Proof

**Compression and collocation.** In the lower-right block the only potentially nonzero entry of \(X_{\rm vv}\) is its subdiagonal, \((c_2-c_1)c_1/2+(c_2-c_1)^2/2\). Subtracting it from the corresponding block of \(Q^2\) gives \(H\). The error subspace with first coordinate zero is invariant because both matrices have first row zero. The exact collocation stages and endpoint matrix are
\[
X^*=(\mathrm{Id}_3+zQ^2)^{-1}(\mathbf1 x_0+Q\mathbf1(h\dot x_0)),\qquad
R_* = \frac1{z^2+12z+144}\begin{pmatrix}
z^2-60z+144&12(12-z)\\12z(z-12)&z^2-60z+144
\end{pmatrix}.
\]
Direct multiplication gives \(\det R_*=1\), and expansion gives \(\operatorname{tr}R_*=2-z+O(z^2)\), \((R_*)_{21}=-z+O(z^2)\), and \((R_*)_{11}=1+O(z)\).

**Defect.** The stage error \(\Delta^{(j)}=X^{(j)}-X^*\) propagates by \(-z(\mathrm{Id}_3+zX_{\rm vv})^{-1}(Q^2-X_{\rm vv})\). Initially it has first coordinate zero; restricted to the other two coordinates, its velocity-input column is \(-c+O(z)\) and its position-input column is \(O(z)\). Thus after \(k\) sweeps these columns are \((-1)^{k+1}z^kH^kc+O_k(z^{k+1})\) and \(O_k(z^{k+1})\), respectively. Applying the endpoint functionals introduces a further factor of \(z\); the bottom-right endpoint error is \((-1)^kz^{k+1}qH^kc+O_k(z^{k+2})\). The entire first error column is \(O_k(z^{k+2})\), and the other second-column error is multiplied by \((R_*)_{21}=O(z)\) in the determinant expansion. This proves the claimed coefficient and preserves the trace expansion \(2-z+O(z^2)\) for \(k\ge1\).

**Phase.** The trace and determinant of \(H\) are \(1/12\) and \((\sqrt3-1)/288\); the discriminant is \((3-2\sqrt3)/144<0\). They give the stated \(r,\theta\). The two scalar initial values of \(qH^kc\), namely \(1/2\) and \((3-\sqrt3)/72\), determine the displayed sinusoid by the Cayley–Hamilton recurrence. That recurrence gives \(qH^kc=(9-5\sqrt3)/1728,(5-3\sqrt3)/6912,(27-16\sqrt3)/248832\) for \(k=2,3,4\), respectively. Also no coefficient is zero: the conjugation \(\sqrt3\mapsto-\sqrt3\) makes every entry of \(H\) and \(c\) positive, so the conjugate of \(qH^kc\) is strictly positive.

If \(\theta/\pi\) were rational then \(e^{2i\theta}\) would be a root of unity. All conjugates of its sum with its inverse would lie in \([-2,2]\), whereas \(\sqrt3-1\) has conjugate \(-\sqrt3-1<-2\). Thus the sampling of the nonzero sinusoid by the rotation \(\theta+\pi\) is equidistributed on the circle. Each sign occupies a half-circle. The same holds within either parity subsequence since the doubled rotation is still irrational.

**Stability.** For the characteristic polynomial of the real step matrix the Schur inequalities are \(1-\det R_k>0\) and \(1\pm\operatorname{tr}R_k+\det R_k>0\). The latter two have leading terms \(4\) and \(z\), both positive for sufficiently small positive \(z\). Therefore the defect sign distinguishes strict stability from determinant greater than one, which implies instability. Equidistribution gives the two densities.

## Reproducibility

The accompanying `verify.py` reconstructs the quadrature by symbolic integration, checks the compression and the collocation endpoint, verifies the coefficient for the first six sweeps symbolically, and compares with high-precision step matrices for the first nine sweeps. It can be run with Python, SymPy and mpmath. These finite checks are diagnostics; the all-\(k\) result and the density follow from the proof.

## Relationship to prior work and limitations

Akramov et al. give the scheme and oscillator stability analysis; their Table 1 gives differing finite two-node stability limits for the first four sweeps. Those entries are not an all-sweep local stability law. A related half-density phase law for three-node Gauss–Lobatto SDC with implicit-Euler preconditioning instead treats a scalar negative-real-axis stiff limit. It does not give the Verlet compression, determinant coefficients, or oscillator small-step stability law here. The conclusion here is local in \(z\) at fixed sweep count, for a scalar undamped oscillator and this specific initialization, preconditioner and output. It gives neither a uniform step interval nor a finite-step boundary, and does not address other node sets, damping, nonlinear forces or other preconditioners. The converged collocation endpoint has unit determinant, in contrast to the finite-sweep strict contraction or expansion in the small-step regime.

## References

1. I. Akramov, S. Götschel, M. Minion, D. Ruprecht and R. Speck, *Spectral deferred correction methods for second-order problems*, arXiv:2310.08352 (2023), SIAM J. Sci. Comput. 46 (2024), DOI: 10.1137/23M1592596, especially Sections 2–3 and Table 1.
2. M. Winkel, R. Speck and D. Ruprecht, *A high-order Boris integrator*, arXiv:1409.5677, J. Comput. Phys. 295 (2015), 456–474, for related second-order SDC background.
3. *Half-density stiff instability of convergent three-node deferred correction*, Resultary, `2026/10/18/SCOPE-half-density-stiff-instability-of-convergent-three-node-deferred--124d0f71bd59`, for the distinct negative-real-axis result.
