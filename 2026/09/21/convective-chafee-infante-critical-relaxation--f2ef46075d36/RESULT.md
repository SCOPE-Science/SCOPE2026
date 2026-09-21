# Transport-renormalized critical relaxation in a convective Chafee–Infante equation

Consider the one-dimensional reaction–convection–diffusion equation
\[
 u_t+\alpha u u_x=\nu u_{xx}+\beta(u-u^3),\qquad 0<x<L,
\]
with homogeneous Dirichlet boundary conditions
\[
 u(0,t)=u(L,t)=0,
\]
where \(\nu,\beta>0\) and \(\alpha\in\mathbb R\).  This is the Chafee–Infante cubic reaction with Burgers transport; equivalently, it is the \(n=1,\gamma=-1\) symmetric-cubic member of the generalized Burgers–Huxley family.

Put
\[
 \kappa=\frac{\pi}{L},\qquad \beta_c=\nu\kappa^2,
 \qquad r=\frac{\alpha}{\nu\kappa}.
\]
For sufficiently regular data, standard one-dimensional parabolic theory gives the global solution used below; the energy identities extend to the usual energy class by approximation.

## 1. Exact global stability boundary

### Theorem 1
The zero equilibrium is globally asymptotically stable exactly for
\[
 \boxed{\beta\le \beta_c=\frac{\nu\pi^2}{L^2}.}
\]
More precisely:

1. if \(0<\beta<\beta_c\), every solution converges exponentially to zero in \(L^2\), with the usual parabolic smoothing giving convergence in stronger norms for positive time;
2. if \(\beta=\beta_c\), every solution still converges to zero and, writing \(Y(t)=\|u(t)\|_2^2\),
   \[
   \boxed{
   Y(t)\le
   \frac{Y(0)}{1+(2\beta_c/L)Y(0)t};
   }
   \]
3. if \(\beta>\beta_c\), the zero equilibrium is linearly unstable.

In particular, the conservative Burgers transport does not move the sharp global Dirichlet stability threshold.

### Proof
Multiplication by \(u\) and integration by parts give
\[
 \frac12\frac{d}{dt}\|u\|_2^2
 =-\nu\|u_x\|_2^2+\beta\|u\|_2^2-\beta\|u\|_4^4,
\]
because
\[
 \int_0^L u^2u_x\,dx=\frac13[u^3]_{0}^{L}=0.
\]
The sharp Dirichlet Poincaré inequality gives
\[
 \|u_x\|_2^2\ge \kappa^2\|u\|_2^2.
\]
Hence
\[
 \frac12Y'\le-(\beta_c-\beta)Y-\beta\|u\|_4^4.
\]
For \(\beta<\beta_c\) this yields exponential decay.  At \(\beta=\beta_c\), Hölder's inequality \(\|u\|_4^4\ge L^{-1}Y^2\) gives
\[
 Y'\le-\frac{2\beta_c}{L}Y^2,
\]
which integrates to the displayed algebraic bound.  For \(\beta>\beta_c\), the linearization is \(v_t=\nu v_{xx}+\beta v\), whose first Dirichlet eigenvalue is \(\beta-\beta_c>0\).  The convection is quadratic and therefore does not enter the linearization. \(\square\)

## 2. Critical center dynamics and the transport correction

Now set \(\beta=\beta_c\).  Define the sine-mode amplitudes
\[
 A_n(t)=\frac{2}{L}\int_0^L u(x,t)\sin(n\kappa x)\,dx,
 \qquad A=A_1.
\]
The linearized operator has a simple zero eigenvalue on \(\sin(\kappa x)\), while all higher modes are strictly stable.  The equation is equivariant under
\[
 (\mathcal Ru)(x)=-u(L-x),
\]
and \(\mathcal R\) sends \(A\) to \(-A\).  Thus the scalar center dynamics is odd.

### Theorem 2
A smooth local center manifold can be parameterized by the first sine amplitude \(A\).  Its expansion through fourth order is
\[
\begin{aligned}
 u={}&A\sin(\kappa x)
 -\frac r6A^2\sin(2\kappa x)
 +\frac{r^2+1}{32}A^3\sin(3\kappa x)\\
 &+A^4\left[
 \frac{r(r^2+9)}{864}\sin(2\kappa x)
 -\frac{r(13r^2+27)}{2160}\sin(4\kappa x)
 \right]+O(A^5)
\end{aligned}
\]
in \(H_0^1(0,L)\), and the reduced equation is
\[
 \boxed{
 A'=-\frac{\beta_c(r^2+9)}{12}A^3
 -\frac{\beta_c(r^2+9)(7r^2-9)}{3456}A^5
 +O(A^7).
 }
\]

The cubic damping coefficient is therefore
\[
 \boxed{
 g=\frac{\beta_c(r^2+9)}{12}
 =\frac{3\beta_c}{4}+\frac{\alpha^2}{12\nu}.
 }
\]
Thus the Burgers term, although invisible in the energy threshold and in the linearization, increases the first nonlinear damping coefficient by the explicit amount \(\alpha^2/(12\nu)\).  The mechanism is a slaved second harmonic: transport creates \(-\frac r6A^2\sin(2\kappa x)\), which feeds back into the critical first mode at cubic order.

### Derivation
Write \(\theta=\kappa x\).  At criticality the equation becomes
\[
 u_t=\beta_c(u_{\theta\theta}+u)-r\beta_c u u_\theta-\beta_c u^3.
\]
Using \(\phi_n=\sin(n\theta)\), the linear eigenvalues are \(\beta_c(1-n^2)\).  Insert
\[
 u=A\phi_1+A^2H_2+A^3H_3+A^4H_4+\cdots
\]
into the invariance equation, impose that each \(H_j\) has zero \(\phi_1\) component, and solve the stable-mode equations successively.  This gives
\[
 H_2=-\frac r6\phi_2,\qquad
 H_3=\frac{r^2+1}{32}\phi_3,
\]
and the displayed \(H_4\).  Projection of the invariance equation onto \(\phi_1\) gives the cubic and quintic coefficients above.  The compact symbolic artifact reproduces these coefficients and verifies the center and stable-mode residuals through the claimed orders.

## 3. Sharp critical slowing and a logarithmic correction

The global estimate in Theorem 1 brings every solution into the local critical neighborhood.  Standard stable-foliation theory then gives the following dichotomy.

### Theorem 3
At \(\beta=\beta_c\), each solution belongs to one of two classes.

- **Strong-stable exceptional class.**  If its local center coordinate is zero, the solution decays exponentially.
- **Nonexceptional class.**  Otherwise the first-mode amplitude is eventually nonzero with a fixed sign, and there is a finite constant \(C=C(u_0)\) such that
  \[
  \boxed{
  \frac1{A(t)^2}
  =\frac{\beta_c(r^2+9)}6\,t
  +\frac{7r^2-9}{288}\log t
  +C+o(1).
  }
  \]
  Consequently,
  \[
  \boxed{
  \sqrt t\,A(t)\longrightarrow
  \sigma\sqrt{\frac6{\beta_c(r^2+9)}},\qquad
  \sigma\in\{-1,+1\},
  }
  \]
  and
  \[
  \boxed{
  \sqrt t\,\|u(t)\|_2
  \longrightarrow
  \sqrt{\frac{3L}{\beta_c(r^2+9)}}.
  }
  \]
  The second harmonic has the sign-independent wake
  \[
  \boxed{
  tA_2(t)\longrightarrow
  -\frac{r}{\beta_c(r^2+9)}.
  }
  \]

The logarithmic coefficient changes sign at
\[
 |r|=\frac3{\sqrt7}.
\]
It vanishes exactly there, is negative for \(r^2<9/7\), and positive for \(r^2>9/7\).

### Proof of the asymptotic formula
Write the reduced equation as
\[
 A'=-gA^3+qA^5+O(A^7),
\]
where
\[
 g=\frac{\beta_c(r^2+9)}{12},\qquad
 q=-\frac{\beta_c(r^2+9)(7r^2-9)}{3456}.
\]
For a nonzero center orbit put \(Z=A^{-2}\).  Then
\[
 Z'=2g-\frac{2q}{Z}+O(Z^{-2}).
\]
First \(Z=2gt+O(\log t)\); substituting this back makes the remaining error integrable and yields
\[
 Z=2gt-\frac qg\log t+C+o(1).
\]
Since \(-q/g=(7r^2-9)/288\), the claimed expression follows.  The norm and second-harmonic limits follow from the center-manifold expansion and \(tA^2\to 1/(2g)\). \(\square\)

## 4. Local supercritical steady branches

Let \(\mu=\beta-\beta_c>0\) be small, with \(\nu,L,\alpha\) fixed.  The parameter-dependent center reduction has the form
\[
 A'=\mu A-gA^3+\text{higher-order terms},
\]
with \(g=\beta_c(r^2+9)/12\) at \(\mu=0\).  Hence two symmetry-related locally asymptotically stable equilibria bifurcate from zero:
\[
 \boxed{
 A_\pm=\pm\sqrt{\frac{12\mu}{\beta_c(r^2+9)}}+O(\mu^{3/2}).
 }
\]
Their profiles satisfy
\[
 \boxed{
 u_\pm(x)=A_\pm\sin(\kappa x)
 -\frac r6A_\pm^2\sin(2\kappa x)+O(\mu^{3/2})
 }
\]
in \(H_0^1\), with \(u_-(x)=-u_+(L-x)\).  The second harmonic records the broken pointwise sign symmetry caused by transport even though the combined reflection-sign symmetry remains.

## Relation to prior literature

Chafee and Infante established the classical bifurcation structure of the unadvected cubic reaction–diffusion problem.  Henry's monograph supplies the general invariant-manifold framework for semilinear parabolic equations.  The generalized Burgers–Huxley equation has an extensive traveling-wave, well-posedness, attractor, numerical, and integrability literature, including Wang–Zhu–Lu (1990), Mohan–Khan (2021), and Li–Wang–Wu (2026).  Bortolan–Pires (2023) studies robustness of Chafee–Infante attractors under Lipschitz perturbations.

The established threshold and generic center-manifold methodology are not claimed as new.  Targeted searches for the convective Chafee–Infante / symmetric cubic Burgers–Huxley problem did not locate the combination proved here: exact transport-independence of the sharp global Dirichlet threshold together with the explicit transport-renormalized cubic and quintic center coefficients, the resulting logarithmic critical correction, and the second-harmonic asymptotic.  Originality is therefore asserted only **to the best of our knowledge**.

The most important residual priority risk is older model-specific literature whose complete theorem-level text was not fully inspected, especially the 1974 Chafee–Infante paper, the 1990 Wang–Zhu–Lu generalized Burgers–Huxley paper, and the 2021 Mohan–Khan well-posedness/attractor study.  The available bibliographic, abstract, and related-source material was checked; none of the inspected material states the explicit critical coefficients or asymptotics above.

## Reproducibility

`artifacts/verify_normal_form.py` symbolically reconstructs the center-manifold coefficients at criticality using sine projection.  With SymPy 1.14.0 it produces the exact output stored in `artifacts/VERIFIED_OUTPUT.txt`.  The symbolic calculation corroborates the algebra; the theorems are established analytically above.

## Limitations

- The sharp algebraic and logarithmic asymptotics are stated for the nonexceptional class; the strong-stable exceptional class decays exponentially instead.
- The supercritical steady-branch statement is local near \(\beta=\beta_c\); no global branch classification is claimed.
- Homogeneous Dirichlet data are essential to the exact convection cancellation used in the global energy argument.
- The \(n=1,\gamma=-1\) generalized Burgers–Huxley interpretation is a symmetric-cubic mathematical extension; many physical Burgers–Huxley studies use a different \(\gamma\) range.
- Originality is to the best of our knowledge and retains the literature risks stated above.

## References

1. N. Chafee and E. F. Infante, *A bifurcation problem for a nonlinear partial differential equation of parabolic type*, Applicable Analysis 4 (1974), 17–37. https://doi.org/10.1080/00036817408839081
2. D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Lecture Notes in Mathematics 840, Springer (1981). https://doi.org/10.1007/BFb0089647
3. X. Y. Wang, Z. S. Zhu and Y. K. Lu, *Solitary wave solutions of the generalised Burgers–Huxley equation*, Journal of Physics A 23 (1990), 271–274. https://doi.org/10.1088/0305-4470/23/3/011
4. M. T. Mohan and A. Khan, *On the generalized Burgers–Huxley equation: Existence, uniqueness, regularity, global attractors and numerical studies*, Discrete and Continuous Dynamical Systems B 26 (2021), 3943–3988. https://doi.org/10.3934/dcdsb.2020270
5. M. C. Bortolan and L. Pires, *Topological equivalence of global attractors for Lipschitz perturbations of the Chafee–Infante equation*, Discrete and Continuous Dynamical Systems B 28 (2023), 4519–4531. https://doi.org/10.3934/dcdsb.2023027
6. C. Li, S. Wang and X. Wu, *The integrability of the generalized Burgers–Huxley equation*, Journal of Applied Analysis and Computation 16 (2026), 1594–1607. https://doi.org/10.11948/20250123
