# Sharp sketch-distortion attraction cone and correction breakdown for two-mode Jacobi–Davidson

## Finding
Consider the exactly solved **single-vector, one-vector-restarted** sketched Jacobi–Davidson correction for a real diagonal matrix with two distinct eigenvalues. If the sketch preserves every Euclidean squared norm within a factor \(1\pm\epsilon\), the largest open projective cone in which the correction is guaranteed to exist and converge to a designated eigenvector, **uniformly over every admissible fixed or changing sketch**, is exactly
\[
|t|<\rho_\epsilon:=\sqrt{\frac{1-\epsilon}{1+\epsilon}},\qquad 0\le\epsilon<1.
\]
The exact worst-case next-step slope at current absolute slope \(r\in(0,\rho_\epsilon)\) is
\[
F_\epsilon(r)=r^2\frac{r+\tau_\epsilon}{1-\tau_\epsilon r},\qquad
\tau_\epsilon=\frac{\epsilon}{\sqrt{1-\epsilon^2}};
\]
this maximum is attained by a sketch whose extremal singular directions depend on \(r\). It satisfies \(F_\epsilon(r)<r\), with the sharp transition at \(r=\rho_\epsilon\). At the boundary, a diagonal admissible sketch makes the projected correction equation inconsistent; outside it, the same sketch drives the iterate to the *other* eigenvector. For \(\epsilon>0\), the sharp possible leading local error term is quadratic, with coefficient magnitude \(\tau_\epsilon\); an unsketched correction has cubic local order.

## Assumptions and scope
Let \(A=\operatorname{diag}(\lambda_1,\lambda_2)\) with distinct real eigenvalues. The sought eigendirection is the first coordinate axis. Work in the real plane. Let \(S\) be a sketch, possibly square, with symmetric positive-definite Gram matrix \(H=S^\mathsf{T}S\) satisfying
\[
(1-\epsilon)I\preceq H\preceq(1+\epsilon)I,\qquad 0\le\epsilon<1.
\]
Every such \(H\) has a real square-root sketch \(S\). Write \(H=\begin{psmallmatrix}a&c\\c&b\end{psmallmatrix}\), with \(a,b>0\), \(ab-c^2>0\), and write the current nonvertical projective vector \(u=(1,t)^\mathsf{T}\). Put \(Q=u^\mathsf{T}Hu=a+2ct+bt^2\), define the sketched Rayleigh shift and the \(H\)-orthogonal rank-one projector by
\[
\theta=\frac{u^\mathsf{T}HAu}{Q},\qquad P=I-\frac{uu^\mathsf{T}H}{Q}.
\]
The unique exact correction, when it exists, is required to satisfy \(u^\mathsf{T}Hw=0\) and
\[
P(A-\theta I)P w=-(A-\theta I)u.
\]
The next one-dimensional iterate is the projective line through \(u+w\). This is a **one-vector restarted correction dynamics**, not the unrestarted two-dimensional subspace-expansion algorithm, which reaches the full plane after one expansion. No probability distribution for \(S\), finite-precision claim, or inexact correction is assumed. Statements about adaptive sketches require the displayed embedding inequality independently at every step.

## Proof
**1. The exact scalar reduction.** Put \(d=ab-c^2>0\) and
\[
v=(-(c+bt),\ a+ct)^\mathsf{T}.
\]
A direct multiplication gives \(Hv=d(-t,1)^\mathsf{T}\) and \(u^\mathsf{T}Hv=0\). The projected residual is \(H\)-orthogonal to \(u\) by the definition of \(\theta\), and every admissible correction has the form \(w=\alpha v\). Direct substitution, without assuming that \(A-\theta I\) is invertible, gives
\[
v^\mathsf{T}H(A-\theta I)u=(\lambda_2-\lambda_1)dt,
\qquad
v^\mathsf{T}H(A-\theta I)v=(\lambda_2-\lambda_1)d(a-bt^2).
\]
Because the eigenvalues differ and \(d>0\), the scalar projected equation has a unique solution precisely when \(a-bt^2\ne0\); its coefficient is \(\alpha=-t/(a-bt^2)\). At equality with \(t\ne0\), its zero left-hand-side coefficient and nonzero right-hand-side coefficient make it inconsistent. For a nonsingular correction with \(a+ct\ne0\),
\[
 u+w=\frac{1}{a-bt^2}\binom{a+ct}{-t^2(c+bt)},\qquad
 t_+=-t^2\frac{c+bt}{a+ct}.
\]
The formula is valid even if \(\theta\) coincides with an eigenvalue and ordinary inverse iteration is undefined. In the proved safe cone, the denominator of the slope ratio and the correction equation are both nonzero.

**2. Sharp uniform one-step bound.** Let \(r=|t|\), \(\phi=\arctan r\), and \(\beta=\arcsin\epsilon\). Since \(\|(H-I)u\|\le\epsilon\|u\|\), the oriented angle of the positive vector \(Hu\) with \(u\) changes by at most \(\beta\). To prove the angular bound, view \(Hu\) as a point of the closed Euclidean disk of radius \(\epsilon\|u\|\) about \(u\); for \(\epsilon<1\), the largest possible angular deviation is the angle of a tangent ray from the origin, with sine \(\epsilon\). For \(r<\rho_\epsilon\), the first coordinate of \(Hu\) is positive, and the absolute ratio of its second and first coordinates is bounded sharply by
\[
\tan(\phi+\beta)=\frac{r+\tau_\epsilon}{1-\tau_\epsilon r}.
\]
Combining this with the exact projective map yields \(|t_+|\le F_\epsilon(r)\). For every \(r\) in the stated interval the bound is attained: take unit vectors \(e=u/\|u\|\) and \(n\) obtained by rotating \(e\) toward increasing polar angle, and choose \(H=I+E\), where in the orthonormal basis \((e,n)\),
\[
[E]_{(e,n)}=\begin{pmatrix}-\epsilon^2&\epsilon\sqrt{1-\epsilon^2}\\ \epsilon\sqrt{1-\epsilon^2}&\epsilon^2\end{pmatrix}.
\]
This matrix has eigenvalues \(\pm\epsilon\), so \(H\) is admissible, while \(He\) forms angle exactly \(\beta\) with \(e\). For negative slopes reflect both axes. At \(\epsilon=0\), take \(H=I\), which also realizes equality.

**3. Exact attraction radius.** Elementary algebra gives
\[
\frac{F_\epsilon(r)}r=\frac{r(r+\tau_\epsilon)}{1-\tau_\epsilon r}<1
\quad\Longleftrightarrow\quad
r<\sqrt{1+\tau_\epsilon^2}-\tau_\epsilon
=\rho_\epsilon.
\]
In this range \(\phi<\pi/4-\beta/2\). Moreover, since \(a\ge 1-\epsilon\) and \(b\le1+\epsilon\), \(a-bt^2>0\) whenever \(r<\rho_\epsilon\), proving unique solvability. Also \(a+ct=(Hu)_1>0\) by the angular bound. The function \(F_\epsilon(r)/r\) is strictly increasing for \(0<r<\rho_\epsilon\). Even if \(H\) changes arbitrarily from step to step subject to the same embedding distortion, the sequence satisfies
\[
|t_{k+1}|\le F_\epsilon(|t_k|)\le q_0|t_k|,
\qquad
q_0=\frac{F_\epsilon(|t_0|)}{|t_0|}<1,
\]
for each nonzero starting slope inside the cone. Thus \(t_k\to0\), and the asymptotic bound is quadratic. When the initial slope is exactly zero, it remains zero.

**4. Sharp boundary and exterior failure.** The diagonal admissible metric
\[
H_*=\operatorname{diag}(1-\epsilon,1+\epsilon)
\]
makes the correction inconsistent at \(|t|=\rho_\epsilon\), because \(a-bt^2=0\) while the projected residual is nonzero. Away from this boundary its exact map is
\[
 t_+=-\frac{1+\epsilon}{1-\epsilon}t^3.
\]
For any finite \(|t|>\rho_\epsilon\), the magnitude increases strictly and diverges under iteration, so its projective direction converges to the other eigenvector. This establishes that no larger interval about the first eigendirection has uniform solvability and target attraction.

**5. Local convergence order.** At fixed \(H\), expansion of the exact map at \(t=0\) gives
\[
 t_+=-\frac ca t^2+O(t^3),
\]
and if \(c=0\), it reduces to \(t_+=-(b/a)t^3\). By the angular-disk argument at \(u=(1,0)^\mathsf{T}\), \(\sup_H |c/a|=\tau_\epsilon\), attained by \(H=\begin{psmallmatrix}1-\epsilon^2&\epsilon\sqrt{1-\epsilon^2}\\\epsilon\sqrt{1-\epsilon^2}&1+\epsilon^2\end{psmallmatrix}\). For \(\epsilon>0\), quadratic order is therefore unavoidable in the worst case; for \(\epsilon=0\), the map is exactly \(t_+=-t^3\).

## Verification
A standalone exact-rational program `VERIFY.py` directly constructs the projected correction coefficient, compares it against the derived scalar map for many nonsingular rational test cases, checks the singular boundary and exterior behavior for the distortion \(\epsilon=3/5\), and checks the sharp uniform upper bound on a deterministic finite collection of rational near-isometric matrices. Run `python3 VERIFY.py` with the Python standard library. These checks corroborate the symbolic identities and the example but are not substitutes for the all-parameter angular argument or convergence proof.

## Relationship to prior work
Grigori, Park, and Simunec (arXiv:2609.29651v1, first public September 1, 2026) define the sketched Jacobi–Davidson correction, relate exact solutions to sketched inverse iteration subject to nondegeneracy, and prove general local quadratic convergence; their Remark 11 identifies the quadratic-order loss on normal matrices under sketched shifts. The present result uses their correction equation but analyzes a specifically defined one-vector restarted two-mode model. It determines its exact projective map, sharp **global uniform** attraction cone, sharp embedding-dependent next-step envelope, and precise correction singularity. Those global constants, exact extremizers, and exterior counterexamples do not follow from a local quadratic estimate alone. Classical Rayleigh-quotient iteration and generalized weighted-quotient studies provide important antecedents; this finding does not claim to invent inverse iteration, cubic unsketched order, sketched projection, or the existence of local quadratic errors.

## Limitations
The claim is restricted to real two-dimensional matrices with distinct diagonal eigenvalues, exact arithmetic and projected solves, and a uniform Gram distortion bound. The repeated one-vector reset is a mathematical model and not the unrestarted full two-dimensional Jacobi–Davidson implementation, which would span the plane after one expansion. Sharpness allows an arbitrary admissible sketch, and does not assert that a particular random sketch produces the worst case with substantial probability. No comparison of computational runtime is made. Earlier work on weighted Rayleigh iterations may contain related two-mode calculations; some historical full texts were not accessible for conclusive overlap exclusion.

## References
- L. Grigori, T. Park, I. Simunec, *Randomized Jacobi–Davidson method*, arXiv:2609.29651v1 (September 1, 2026). https://arxiv.org/html/2609.29651v1 . Sections 3–4, particularly equation (4), Theorem 1, Theorem 9 and Remark 11.
- P. B. Geltner, *General Rayleigh Quotient Iteration*, SIAM Journal on Numerical Analysis 18 (1981), 839–843, DOI: 10.1137/0718057 (abstract consulted; full text unavailable).
- S. Batterson, J. Smillie, *The Dynamics of Rayleigh Quotient Iteration*, SIAM Journal on Numerical Analysis 26 (1989), 624–636, DOI: 10.1137/0726037 (abstract consulted).
- B. N. Parlett, *The Rayleigh quotient iteration and some generalizations for nonnormal matrices*, Mathematics of Computation 28 (1974), 679–693, DOI: 10.1090/S0025-5718-1974-0405823-3 (abstract consulted).
