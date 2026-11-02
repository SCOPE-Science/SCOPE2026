# Universal first period response on a quadratic chameleon Hopf sheet

## Finding

Consider the real quadratic flow
\[
\dot x=y,\qquad
\dot y=-x+yz,\qquad
\dot z=\alpha-bz-5xy+xz.
\]
For each fixed \(b>0\), the unique equilibrium \(E_{\alpha,b}=(0,0,\alpha/b)\) undergoes a **nondegenerate subcritical Hopf bifurcation** as \(\alpha\) passes through zero. With the normalized complex eigenvectors specified below, its first Lyapunov coefficient is exactly
\[
\ell_1(b)=\frac5{b^2+4}>0.
\]
For every fixed \(b>0\), there exists \(\varepsilon_b>0\) such that for \(-\varepsilon_b<\alpha<0\) the flow has a unique (up to phase) nonconstant periodic orbit sufficiently near \(E_{\alpha,b}\). This orbit is radially repelling and transversely attracting (one positive and one negative nontrivial Floquet exponent); the equilibrium is locally asymptotically stable. Define its \(x\)-half-amplitude as \(A_b(\alpha)=(\max_t x(t)-\min_t x(t))/2\). Then
\[
A_b(\alpha)=\sqrt{\frac{2(b^2+4)}{5b}}\sqrt{-\alpha}+O_b(|\alpha|),
\qquad
T_b(\alpha)=2\pi\left(1+\frac{\alpha}4\right)+O_b(\alpha^2).
\]
The exact first period derivative \(\lim_{\alpha\uparrow0}(T_b(\alpha)-2\pi)/\alpha=\pi/2\) is therefore **independent of \(b\)**, even though the cycle's amplitude and Hopf coefficient depend on \(b\).

## Assumptions and scope

All variables are real, \(b\) is held fixed and strictly positive, and \(\alpha\) varies in a sufficiently small neighborhood of zero depending on \(b\). The flow is considered locally in a neighborhood of its unique equilibrium; neither global completeness nor a global attractor classification is needed. Big-O constants may depend on \(b\). The limit cycle is unique only among sufficiently small cycles near this equilibrium, not among all cycles of the vector field. The characteristic frequency at Hopf is one radian per unit physical time.

We use the standard multilinear Hopf convention \(f(w)=Aw+\tfrac12B(w,w)\) at criticality, \(Aq=iq\), \(A^*p=-ip\), and \(\langle p,q\rangle=\overline p^{\mathsf T}q=1\). In this convention \(\ell_1=\tfrac12\operatorname{Re}G_{21}\), where \(G_{21}\) is the cubic normal-form coefficient defined in the proof. Its numerical value need not equal focus coefficients defined using different scaling conventions.

## Proof

**Equilibrium and eigenvalue crossing.** The equilibrium equations give \(y=x=0\) and \(z=\alpha/b\). At this equilibrium,
\[
Df(E_{\alpha,b})=
\begin{pmatrix}0&1&0\\-1&\alpha/b&0\\\alpha/b&0&-b\end{pmatrix},
\qquad
\det(\lambda I-Df)=(\lambda+b)(\lambda^2-\alpha\lambda/b+1).
\]
At \(\alpha=0\) the eigenvalues are \(i,-i,-b\), with \(d\operatorname{Re}\lambda/d\alpha=1/(2b)>0\). Thus the imaginary pair is simple, and the Hopf transversality condition holds for every \(b>0\).

**Exact cubic normal form.** At the critical equilibrium let
\[
A=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&-b\end{pmatrix},\quad
q=(1,i,0)^{\mathsf T},\quad p=\tfrac12(1,i,0)^{\mathsf T}.
\]
The only nonzero components of the symmetric quadratic derivative are
\[
B_2(u,v)=u_2v_3+u_3v_2,
\qquad B_3(u,v)=-5(u_1v_2+u_2v_1)+u_1v_3+u_3v_1.
\]
In particular,
\[
B(q,\bar q)=0,\qquad B(q,q)=(0,0,-10i)^{\mathsf T},\qquad
h_{20}=(2iI-A)^{-1}B(q,q)=(0,0,-10i/(b+2i))^{\mathsf T}.
\]
There are no cubic derivatives. The standard nonresonant Hopf reduction therefore gives
\[
G_{21}=\langle p,B(\bar q,h_{20})\rangle
=\frac{5i}{b+2i}
=\frac{10+5bi}{b^2+4},
\qquad
\ell_1=\frac12\operatorname{Re}G_{21}=\frac5{b^2+4}>0.
\]
The vanishing of \(B(q,\bar q)\) eliminates the other quadratic interaction term. The analytic Hopf theorem gives a unique small periodic branch for \(\alpha<0\). Its radial exponent has leading value \(-\alpha/b>0\), while the other nontrivial exponent tends to \(-b\). This proves its saddle-cycle character and the lack of a generalized Hopf degeneracy along the positive \(b\)-axis.

**Physical amplitude and period.** Set \(\alpha=-\epsilon^2\), \(\tau=\Omega t\), and expand the periodic solution
\[
x=\epsilon R\cos\tau+O(\epsilon^2),\quad
y=-\epsilon R\sin\tau+O(\epsilon^2),\quad
z=\epsilon^2Z_2(\tau)+O(\epsilon^3),\quad
\Omega=1+\omega_2\epsilon^2+O(\epsilon^4).
\]
The \(z\)-equation at order \(\epsilon^2\) has its unique periodic solution
\[
Z_2'+bZ_2=-1+\frac{5R^2}2\sin2\tau,\qquad
Z_2=-\frac1b+\frac{5R^2}{2(b^2+4)}(b\sin2\tau-2\cos2\tau).
\]
For the forced oscillator \(\ddot x+x=yz\), the fundamental Fourier coefficients of \(y_1Z_2\), with \(y_1=-R\sin\tau\), are
\[
[\sin\tau]:\ \frac Rb-\frac{5R^3}{2(b^2+4)},\qquad
[\cos\tau]:\ -\frac{5bR^3}{4(b^2+4)}.
\]
The sine solvability equation yields \(R^2=2(b^2+4)/(5b)\); the cosine solvability equation gives
\[
2\omega_2R=\frac{5bR^3}{4(b^2+4)}
\quad\Longrightarrow\quad
\omega_2=\frac14.
\]
Consequently \(\Omega=1-\alpha/4+O_b(\alpha^2)\) and \(T=2\pi/\Omega=2\pi(1+\alpha/4)+O_b(\alpha^2)\). The Hopf nondegeneracy proved above and analytic implicit-function reduction justify this regular even-power expansion, not merely a formal series. The \(x\)-half-amplitude is \(R\sqrt{-\alpha}+O_b(|\alpha|)\), as claimed.

## Verification

Run `python verification/verify.py` with Python, SymPy, SciPy, and NumPy. It checks the matrix eigenvector identities, exact quadratic derivative, \(G_{21}\), the \(Z_2\) forcing identity, both Fourier solvability coefficients, and the symbolic frequency cancellation. It also solves the full periodic shooting equations for \(b\in\{1/2,1,2\}\) and \(\alpha\in\{-0.005,-0.0025\}\), checking consistency with the asymptotic amplitude and period. These finite computations corroborate rather than prove the all-parameter or infinite-time statements; the proof is analytical.

## Relationship to prior work

Zhang, Sang, Li, Liu, Fan and Wang introduced the quadratic chameleon family and proved a **qualitative subcritical Hopf result** for the special damping \(b=1\), using \(\mu(z)=\alpha-z\) (their Section 4, Theorem 4.2). Their paper also varied the damping in numerical studies. The present theorem does not claim novelty for the existence or subcritical nature at \(b=1\); it supplies the exact general-\(b\) coefficient and the leading **physical** amplitude and period formulas, with a damping-independent first period slope. The related later paper by Liu and collaborators (2025) treats a different quadratic chameleon vector field with distinct nonlinear couplings and does not imply these formulas. Standard Hopf and Poincaré–Lindstedt methods are established tools; the mathematical claim concerns their exact consequences for this specified family. Searches have not established absolute publication priority.

## Limitations

This is a local two-parameter calculation for fixed \(b>0\), with constants and the allowed \(\alpha\)-window not uniform as \(b\to0\) or \(b\to\infty\). It does not classify all cycles or chaotic attractors, prove their cryptographic properties, or characterize global basins. The originally uploaded preprint displays a month-only draft date preceding its verified October 12, 2023 online upload; that ambiguity and potentially unindexed calculations remain publication-priority risks. Independent mathematical audit has not been performed.

## References

1. X. Zhang, B. Sang, B. Li, J. Liu, L. Fan, N. Wang, “Hidden chaotic mechanisms for a family of chameleon systems,” *Mathematical Modelling and Control* **3** (2023), 400–415, DOI: 10.3934/mmc.2023032. Full author-uploaded preprint: https://www.researchgate.net/publication/374625497_Hidden_chaotic_mechanisms_for_a_family_of_chameleon_systems_Rev (publicly uploaded October 12, 2023).
2. J. Liu et al., “Symmetry, Hopf bifurcation, and offset boosting in a novel chameleon system,” *AIMS Mathematics* **10** (2025), 4915–4937, DOI: 10.3934/math.2025225 (different model).
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004, Section on the first Lyapunov coefficient of a Hopf bifurcation (standard method).
