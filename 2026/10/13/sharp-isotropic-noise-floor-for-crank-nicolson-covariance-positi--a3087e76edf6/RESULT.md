# Sharp isotropic-noise floor for Crank–Nicolson covariance positivity

## Finding
Consider the continuous-time differential Lyapunov equation
\[
\dot P=-DP-PD+\nu I_2,
\qquad D=\operatorname{diag}(a,b),
\qquad a,b>0,
\quad a\ne b,
\quad\nu\ge0.
\]
The initial covariance is any real symmetric matrix satisfying
\[
P\succeq0,
\qquad\operatorname{tr}P=\tau>0.
\]
The exact flow preserves the positive-semidefinite cone. Let \(P^+\) be the result of one **direct** Crank–Nicolson (trapezoidal) time step of length \(h\). Assume
\[
0<ha<1,
\qquad 0<hb<1.
\]
Thus the scalar diagonal-mode damping factors themselves are nonnegative and cannot explain any loss of covariance positivity.

Set
\[
x=ha,\quad y=hb,\quad r=1-x,\quad\ell=1-y,
\quad z=\frac{2-x-y}{2+x+y},
\]
\[
k=z^2(1+x)(1+y),
\qquad E=k-r\ell
=\frac{2(x-y)^2(x+y)}{(2+x+y)^2}>0.
\]
Then the sharp criterion for **every** covariance of trace \(\tau\) to remain positive semidefinite is
\[
\boxed{
\frac{h\nu}{\tau}
\ge
s_*(x,y)
:=\frac{E}{r+\ell+2\sqrt{k}}.
}
\]
Below this exact diffusion threshold a rank-one covariance loses positive semidefiniteness in a single step; at equality some rank-one input becomes a singular output; above it every trace-\(\tau\) covariance produces a positive-definite output.

At the threshold an extremal rank-one input has squared first modal component
\[
\boxed{
t_*=\frac12-\frac{s_*(r-\ell)}{2E}\in(0,1).
}
\]
Consequently the same direction witnesses failure for every smaller diffusion level. In particular, with zero forcing, a rank-one input with squared components \(1/2,1/2\) loses positive semidefiniteness for **every** allowed \(h>0\) when the decay rates differ.

The sharp physical noise strength has the small-step asymptotic
\[
\boxed{
\nu_*(h)=\frac{\tau h^2(a-b)^2(a+b)}8+O(h^3).
}
\]
The covariance scale \(\tau\) matters linearly: normalizing the input trace to one simply fixes a reference variance against which the process-noise strength is measured.

An exact rational witness is
\[
h=1,
\qquad a=\frac14,
\qquad b=\frac45,
\qquad \tau=1.
\]
Here
\[
E=\frac{2541}{37210},
\qquad s_*=\frac{42}{1159},
\qquad t_*=\frac{74}{209}.
\]
At \(\nu=0\), the pure covariance with equal modal weights evolves numerically as
\[
P=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}
\longmapsto
P^+=\begin{pmatrix}
3/10&19/122\\19/122&1/18
\end{pmatrix},
\quad
\det P^+=-\frac{847}{111630}<0.
\]
Although the exact covariance flow is positive semidefinite for all \(t\ge0\), the unmodified second-order direct step violates the covariance cone.

## Assumptions and scope
The statement concerns real symmetric \(2\times2\) covariances, diagonal stable drift, nonnegative **isotropic** diffusion, and direct time stepping of the matrix differential equation in exact arithmetic. The initial covariance may be singular. The positive trace \(\tau\) is fixed, rather than requiring one fixed diffusion rate to protect arbitrarily scaled initial covariances.

The bound \(0<ha,hb<1\) isolates the matrix-cone defect from scalar Crank–Nicolson sign changes. The rates are distinct; at equal rates the direct step is a nonnegative scalar multiple of the old covariance plus a nonnegative multiple of the identity and requires no positive noise floor.

The condition controls one step from any covariance with the specified trace. After one step, the trace generally changes, so repeated-step unconditional guarantees require recomputing the normalized noise ratio or tracking the trace. The result does not claim a global constant-noise bound for arbitrarily long propagation.

## Proof
The exact flow is
\[
P(t)=e^{-Dt}P(0)e^{-Dt}
+\nu\int_0^t e^{-Du}I_2e^{-Du}\,du,
\]
which is positive semidefinite when \(P(0)\succeq0\) and \(\nu\ge0\).

For the direct Crank–Nicolson step, the componentwise equations are
\[
\frac{P^+_{ij}-P_{ij}}h
=-\frac{d_i+d_j}{2}(P_{ij}+P^+_{ij})
+\nu\delta_{ij},
\quad (d_1,d_2)=(a,b).
\]
Thus
\[
P^+_{11}=\frac{rP_{11}+h\nu}{1+x},
\quad
P^+_{22}=\frac{\ell P_{22}+h\nu}{1+y},
\quad
P^+_{12}=zP_{12}.
\]
The map is affine in \(P\). Every positive-semidefinite \(P\) with trace \(\tau\) is a convex combination of rank-one matrices of the form \(\tau vv^{\mathsf T}\) with \(\|v\|_2=1\). Since the positive-semidefinite cone is convex, the update preserves positivity for **all** such \(P\) if and only if it does so for all rank-one inputs.

For a rank-one input write
\[
P=\tau\begin{pmatrix}
t&\sigma\sqrt{t(1-t)}\\
\sigma\sqrt{t(1-t)}&1-t
\end{pmatrix},
\qquad0\le t\le1,
\quad\sigma\in\{-1,1\}.
\]
With \(s=h\nu/\tau\), the updated diagonal entries are nonnegative and the normalized determinant satisfies
\[
(1+x)(1+y)\frac{\det P^+}{\tau^2}
=(rt+s)(\ell(1-t)+s)-k t(1-t).
\]
Put
\[
E=k-r\ell
=\frac{2(x-y)^2(x+y)}{(2+x+y)^2}>0.
\]
Then the determinant condition is
\[
F_s(t):=s^2+s[rt+\ell(1-t)]-E t(1-t)\ge0
\qquad\text{for every }t\in[0,1].
\]
Because the updated diagonal entries are positive for \(s>0\) and nonnegative for \(s=0\), this determinant inequality is necessary and sufficient for the updated rank-one covariance to be positive semidefinite.

The quadratic \(F_s\) in \(t\) has coefficient \(E>0\) and critical point
\[
t_s=\frac12-\frac{s(r-\ell)}{2E}.
\]
Completing the square yields
\[
F_s(t)=E(t-t_s)^2
+s^2+\frac{s(r+\ell)}2-\frac E4
-\frac{s^2(r-\ell)^2}{4E}.
\]
The constant term vanishes at
\[
s_*=\frac{E}{r+\ell+2\sqrt{k}},
\quad k=r\ell+E.
\]
Indeed multiplying it by \(4E\) produces
\[
(4k-(r+\ell)^2)s^2
+2E(r+\ell)s-E^2,
\]
which is zero after substituting the displayed \(s_*\). Moreover,
\[
|r-\ell|<r+\ell+2\sqrt{k},
\]
so the corresponding point \(t_*\) lies strictly between zero and one. Therefore
\[
F_{s_*}(t)=E(t-t_*)^2\ge0
\]
for every \(t\in[0,1]\), with equality exactly at the indicated interior rank-one orientation.

For fixed \(t\),
\[
\frac{\partial F_s(t)}{\partial s}
=2s+rt+\ell(1-t)>0
\]
for every \(s\ge0\), because \(r,\ell>0\). Thus \(s>s_*\) makes all determinant inequalities strict, whereas \(0\le s<s_*\) makes \(F_s(t_*)<0\). This proves the sharp if-and-only-if criterion, including both boundary and failure constructions.

In particular,
\[
F_0(1/2)=-E/4<0,
\]
which proves the arbitrarily small-step unforced counterexample. Finally, expanding \(x=ha\) and \(y=hb\) gives
\[
E=\frac12(a-b)^2(a+b)h^3+O(h^4),
\qquad r+\ell+2\sqrt{k}=4+O(h),
\]
so
\[
\nu_*(h)=\frac{\tau s_*}{h}
=\frac{\tau h^2(a-b)^2(a+b)}8+O(h^3).
\]

## Verification
The standalone `verify.py` uses only exact rational arithmetic. It checks the displayed rational witness, the closed-form threshold \(42/1159\), the critical orientation \(74/209\), vanishing of the determinant quadratic at equality, and strictly negative determinant both for zero forcing and for subcritical nonzero forcing. It also checks the defining algebraic formula for \(E\) on multiple rational parameter pairs.

All universal quantifiers and the small-step asymptotic are proved analytically above. Rational checks are corroborative, not evidence for an infinite parameter range.

## Relationship to prior work
Positive-semidefinite covariance propagation under a differential Lyapunov equation is classical. Dieci and Eirola studied direct numerical integration of Riccati and Lyapunov matrix differential equations and proved that a standard direct method of order above one cannot universally preserve positive definiteness. Their impossibility theorem is explicitly treated as prior work: no novelty is claimed for the basic observation that direct second-order integration can lose positivity.

Gillis and Diehl developed a positive-definiteness-preserving discretization for differential Lyapunov equations in optimal-control covariance propagation. Their full paper explicitly notes positivity failure under ordinary direct collocation and gives an alternative factor-compatible covariance update. It does not classify a sharp minimal isotropic diffusion strength that rescues the **direct** Crank–Nicolson step for every fixed-trace covariance in a two-mode diagonal system.

Structure-preserving ODE integration, including Lyapunov-function-preserving exponential schemes, supplies broader numerical-analysis context. The 2016 work by Li and Wu lists primary MSC \(65L04\); the present matrix-covariance question is a numerical ODE cone-preservation problem within that category, not an assertion that its different Lyapunov-function invariant is identical to a matrix positive-semidefinite constraint.

The contribution is the exact quantitative replacement for the generic impossibility warning: once the initial total variance is fixed, the smallest isotropic noise that restores positive-semidefinite output is the explicitly computed \(s_*\), with an equality orientation and the sharp second-order small-step scaling. Searches for the equivalent formulations “covariance positivity noise floor,” “trapezoidal Lyapunov PSD isotropic forcing,” and “rank-one Schur-multiplier rescue” did not locate an implication-equivalent statement.

## Limitations
The theorem applies to direct Crank–Nicolson time stepping on a two-mode diagonal stable drift and isotropic additive forcing. It is not a general statement for nonnormal drift, anisotropic diffusion, multiple modes, or higher-order integrators.

The input trace is fixed. No strictly positive finite diffusion level can offset the negative homogeneous contribution uniformly over arbitrary rescalings of the initial covariance; any such assertion would be false. The exact answer for trace \(\tau\) scales linearly with \(\tau\).

The noise floor is a sufficient-and-necessary **one-step** property. It does not guarantee that a fixed \(\nu\) continues to work after repeated steps if the total variance changes. A factorized positivity-preserving covariance integrator can avoid the defect altogether, and may be preferable to adding physical or numerical diffusion.

At zero noise the failure occurs for singular rank-one inputs. A fixed strictly positive-definite input need not fail in one sufficiently small step. The theorem therefore does not replace the general multi-step positive-definite impossibility theorem of Dieci and Eirola.

## References
1. L. Dieci and T. Eirola, “Positive Definiteness in the Numerical Solution of Riccati Differential Equations,” *Numerische Mathematik* 67 (1994), 303–313. DOI 10.1007/s002110050030. Author-hosted full manuscript dated April 13, 1993.
2. J. Gillis and M. Diehl, “A Positive Definiteness Preserving Discretization Method for Lyapunov Differential Equations,” *52nd IEEE Conference on Decision and Control* (2013), 7759–7764. DOI 10.1109/CDC.2013.6761121.
3. Y.-W. Li and X. Wu, “Exponential Integrators Preserving First Integrals or Lyapunov Functions for Conservative or Dissipative Systems,” *SIAM Journal on Scientific Computing* 38 (2016), A1876–A1895. DOI 10.1137/15M1023257. Published online June 29, 2016; primary MSC 65L04.
