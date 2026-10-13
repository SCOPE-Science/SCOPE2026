# A fractional-power mean-square rate law for randomized subspace Nesterov acceleration

## Finding
Fix an integer \(d\ge 2\). For the strongly convex quadratic
\[
f_\kappa(x)=\tfrac12\left(\kappa x_1^2+\sum_{j=2}^{d}x_j^2\right),\qquad 0<\kappa<1,
\]
apply the strongly convex randomized-subspace Nesterov algorithm with independent uniformly chosen singleton-coordinate sketches, the admissible constants \(L=1\), \(\ell=\omega=d\), and initialization \(x_0=z_0=e_1\). Write \(t=\sqrt\kappa\), \(\theta=t/d\), and let \(r_d(t)\) be the spectral radius of the explicit three-dimensional second-moment transfer matrix defined below.

There exists \(\kappa_d>0\) such that for every fixed \(0<\kappa<\kappa_d\) the exact asymptotic expected-objective contraction exists and equals \(r_d(\sqrt\kappa)\):
\[
\lim_{k\to\infty}\frac{\mathbb E f_\kappa(x_{k+1})}{\mathbb E f_\kappa(x_k)}=r_d(\sqrt\kappa).
\]
Its singular low-curvature expansion is
\[
\boxed{r_d(\sqrt\kappa)=1-\frac2d\kappa^{1/2}
+\left(\frac{2(d-1)}{d^4}\right)^{1/3}\kappa^{2/3}
+O_d(\kappa^{5/6}).}
\]
The positive \(\kappa^{2/3}\) correction comes from a three-cycle in the covariance dynamics; it is absent from a first-moment or scalar-rate calculation. In dimension two its coefficient is exactly \(1/2\). The leading contraction deficit is twice that in the method's published general \((1-\theta)^k\) upper bound, for this family only.

## Assumptions and scope
The sketch is \(P_k=\sqrt d\,e_{J_k}\), where \(J_k\) is independent uniform on \(\{1,\ldots,d\}\) at each step. The normalization satisfies \(\mathbb E[P_kP_k^{\mathsf T}]=I\), \(\mathbb E[(P_kP_k^{\mathsf T})^2]=dI\), and, for the Hessian \(H=\operatorname{diag}(\kappa,1,\ldots,1)\), \(\mathbb E[P_kP_k^{\mathsf T}HP_kP_k^{\mathsf T}]=dH\preceq dI\); these verify the sketch and smoothness constants directly. The underlying matrix smoothness is bounded by the identity, and the sketch moment constants \(\ell=\omega=d\) are admissible. The source's strongly convex update is
\[
\begin{aligned}
y_k&=(x_k+\theta z_k)/(1+\theta),\\
x_{k+1}&=y_k-(L\ell)^{-1}P_kP_k^{\mathsf T}\nabla f_\kappa(y_k),\\
z_{k+1}&=(1-\theta)z_k+\theta y_k-(\theta/\kappa)P_kP_k^{\mathsf T}\nabla f_\kappa(y_k),
\end{aligned}
\]
with \(\theta=\sqrt{\kappa/(L\omega\ell)}=t/d\). All quantities are real and updates use exact arithmetic. Only the first coordinate can be nonzero from the stated initial condition. The theorem is about the expectation at fixed \(\kappa\) as \(k\to\infty\), followed by \(\kappa\downarrow0\); it makes no uniform-in-\(k\) claim when \(\kappa\) varies.

## Proof
**1. Exact conditional updates.** Put \(a_k=(x_k)_1\), \(b_k=(z_k)_1\) and \(u_k=(a_k,b_k)^{\mathsf T}\). In the event \(J_k\ne1\), no projected gradient acts on the active coordinate. In the event \(J_k=1\), \((L\ell)^{-1}P_kP_k^{\mathsf T}\nabla f_\kappa\) equals \(\kappa\) times the active coordinate. Direct substitution gives
\[
u_{k+1}=K_{I_k}u_k,\qquad
K_0=\frac1{1+\theta}\begin{pmatrix}1&\theta\\\theta&1\end{pmatrix},
\]
\[
K_1=\begin{pmatrix}
(1-t^2)/(1+\theta)&(1-t^2)\theta/(1+\theta)\\
-(d-1)\theta/(1+\theta)&1-\theta-(d-1)\theta^2/(1+\theta)
\end{pmatrix},
\]
where \(\Pr(I_k=1)=1/d\) independently at every step. These are the original sketched-accelerated updates, not a substitute coordinate-descent scheme.

**2. Exact covariance transfer.** For \(K=\begin{pmatrix}a&b\\c&e\end{pmatrix}\), define
\[
\mathcal S(K)=\begin{pmatrix}
a^2&2ab&b^2\\ ac&ae+bc&be\\c^2&2ce&e^2
\end{pmatrix}.
\]
With \(w_k=(\mathbb E a_k^2,\mathbb E a_kb_k,\mathbb E b_k^2)^{\mathsf T}\), independence implies
\[
w_{k+1}=M_d(t)w_k,\qquad M_d(t)=\frac{d-1}{d}\mathcal S(K_0)+\frac1d\mathcal S(K_1),\qquad w_0=(1,1,1)^{\mathsf T}.
\]
In particular \(\mathbb E f_\kappa(x_k)=\frac\kappa2\,(M_d(t)^kw_0)_1\). This identity is valid for every \(k\ge0\) and \(0<\kappa<1\), without an asymptotic approximation.

**3. A singular three-cycle.** Taylor expansion of the displayed rational matrices at \(t=0\), with \(d\) held fixed, yields
\[
M_d(t)=(1-2t/d)I+tN_1+t^2N_2+O_d(t^3),
\]
\[
N_1=\begin{pmatrix}0&2/d&0\\0&0&1/d\\0&0&0\end{pmatrix},\qquad
N_2=\frac1{d^2}\begin{pmatrix}-(2d-3)&-4&1\\0&-(d-2)&-2\\d-1&0&1\end{pmatrix}.
\]
At \(t=0\) the three covariance eigenvalues coalesce. The nonzero \((1,2)\) and \((2,3)\) entries of \(tN_1\) form a length-two Jordan chain, closed by the positive \((3,1)\) entry of \(t^2N_2\). Thus, putting \(\lambda=1-2t/d+t^{4/3}z\), the characteristic determinant satisfies, locally uniformly for bounded complex \(z\),
\[
 t^{-4}\det\bigl(\lambda I-M_d(t)\bigr)
 =z^3-\frac{2(d-1)}{d^4}+O_d(t^{1/3}).
\]
This follows by multiplying the three cycle entries \((2t/d)(t/d)((d-1)t^2/d^2)\): their product is \(2(d-1)t^4/d^4\). All other determinant terms are higher order at that scale. Let \(C_d=[2(d-1)/d^4]^{1/3}>0\). The three distinct roots of the limit polynomial and elementary continuity of simple polynomial roots imply
\[
\lambda_j(t)=1-2t/d+C_d\zeta_jt^{4/3}+O_d(t^{5/3}),\qquad\zeta_j^3=1.
\]
For sufficiently small positive \(t\), the real branch \(\zeta=1\) has strictly greater modulus than either nonreal branch because their real corrections are \(-C_dt^{4/3}/2\). This proves the claimed spectral-radius expansion.

**4. The spectral radius is the observed error rate.** It remains to rule out cancellation of the dominant mode by the specified initial data or the first-coordinate observation. Normalize a dominant real right eigenvector \(v(t)\) and left eigenvector \(h(t)\) so their first entries are one. The same three-cycle equations give
\[
\begin{aligned}
v_2(t)&=(dC_d/2)t^{1/3}+o(t^{1/3}), &v_3(t)&=(d^2C_d^2/2)t^{2/3}+o(t^{2/3}),\\
h_2(t)&=2(dC_d)^{-1}t^{-1/3}+o(t^{-1/3}), &h_3(t)&=2(d^2C_d^2)^{-1}t^{-2/3}+o(t^{-2/3}).
\end{aligned}
\]
All displayed leading coefficients are positive. Hence \((e_1^{\mathsf T}v)(h^{\mathsf T}w_0)/(h^{\mathsf T}v)>0\) for small positive \(t\), and \(h^{\mathsf T}v\to3\). The remaining two eigenvalues have smaller modulus. Spectral decomposition therefore gives \((M_d(t)^kw_0)_1=B_d(t)\lambda_+(t)^k+o(\lambda_+(t)^k)\), with \(B_d(t)>0\) for each sufficiently small fixed \(t>0\). The ratio of successive expected objectives tends to \(\lambda_+(t)=r_d(t)\). Substituting \(t=\sqrt\kappa\) finishes the proof.

## Verification
The accompanying standalone `verify.py` independently reconstructs the two conditional state matrices, tests exact-rational second-moment identities against complete enumeration of selection strings through five iterations, and numerically checks the predicted fractional-order eigenvalue separation in several dimensions and at several small positive parameters. Execute `python verify.py` with the listed dependencies. Its successful output is `VERIFY_OK exact_finite_identities=168 spectral_cases=12`. The universal cubic-root asymptotic and the noncancellation argument are analytical; the finite checks cannot establish them alone.

## Relationship to prior work
Omiya, Poirion, and Takeda, *Randomized Subspace Nesterov Accelerated Gradient*, arXiv:2605.00740v1 (first publicly submitted 2026-05-01), introduce and analyze the strongly convex sketched three-sequence method. Their general upper bound involves \((1-\theta)^k\) and their coordinate examples use subspace sketching; the result here concerns the exact expected-objective rate for a specified low-curvature eigendirection, obtained from a full covariance recurrence. Generic accelerated randomized coordinate-descent results, including Fercoq and Richtárik's APPROX framework, establish broader complexity guarantees for related but not identical updates; those do not directly imply the present cubic-root covariance-eigenvalue expansion. A literature search does not establish uniqueness; see the accompanying review for remaining equivalence risks.

## Limitations
The result requires a fixed finite dimension, a diagonal positive-definite quadratic, uniform independent singleton-coordinate sketches, and exact implementation of the stated strongly convex update. Only initial data supported on the lowest-curvature coordinate are covered by the identified observable rate. The asymptotic expansion holds for sufficiently small positive \(\kappa\), with constants depending on \(d\); no explicit optimal range for \(\kappa_d\) is asserted. The relative cost of the extra state and possible finite-precision effects are not quantified. The observed rate does not imply a better worst-case universal guarantee or a global rate comparison for other initializations.

## References
1. G. Omiya, P.-L. Poirion, A. Takeda, *Randomized Subspace Nesterov Accelerated Gradient*, arXiv:2605.00740v1 (2026-05-01), https://arxiv.org/abs/2605.00740 (Algorithm 2, strongly convex convergence theorem, coordinate sketch discussion, and appendices).
2. O. Fercoq and P. Richtárik, *Accelerated, Parallel, and Proximal Coordinate Descent*, SIAM Journal on Optimization 25 (2015), 1997–2023; preprint arXiv:1312.5799. General accelerated coordinate benchmark, different update rule.
