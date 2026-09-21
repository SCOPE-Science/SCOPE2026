# Ikeda critical delay stability and sharp relaxation law

Consider the zero-phase Ikeda delay equation
\[
\dot x(t)=\mu\sin x(t-h)-x(t),\qquad \mu>0,\quad h\ge0,
\]
with continuous initial history on \([-h,0]\) (and the ordinary differential equation interpretation when \(h=0\)).

## Theorem

For every fixed delay \(h\ge0\), the zero equilibrium is globally asymptotically stable if and only if
\[
\boxed{\mu\le1.}
\]

More precisely:

1. If \(0<\mu<1\), zero is globally exponentially stable. A Halanay rate is the unique \(\eta>0\) satisfying
   \[
   \eta+\mu e^{\eta h}=1
   \]
   when \(h>0\); for \(h=0\), one may take \(\eta=1-\mu\).

2. At the nonhyperbolic endpoint \(\mu=1\), the functional
   \[
   V(x_t)=\frac12x(t)^2+\frac12\int_{t-h}^{t}x(s)^2\,ds
   \]
   satisfies the exact identity
   \[
   \boxed{
   \dot V=
   -\frac12\bigl(x(t)-\sin x(t-h)\bigr)^2
   -\frac12\bigl(x(t-h)^2-\sin^2x(t-h)\bigr).
   }
   \]
   Hence zero remains globally asymptotically stable at equality.

3. At \(\mu=1\), define
   \[
   Q(t)=x(t)+\int_{t-h}^{t}x(s)\,ds .
   \]
   Then
   \[
   \boxed{Q'(t)=\sin x(t-h)-x(t-h).}
   \]
   The characteristic equation is
   \[
   \lambda+1-e^{-\lambda h}=0.
   \]
   Its only root in the closed right half-plane is the simple root \(\lambda=0\). In the center coordinate
   \[
   u=\frac{Q}{1+h},
   \]
   standard retarded-equation center-manifold reduction gives
   \[
   \boxed{
   \dot u=-\frac{1}{6(1+h)}u^3+O(u^5).
   }
   \]
   Consequently, for every critical solution whose eventual local history is not on the strong-stable manifold,
   \[
   \boxed{
   \sqrt t\,x(t)\longrightarrow
   \sigma\sqrt{3(1+h)},\qquad \sigma\in\{-1,+1\}.
   }
   \]
   Histories on the strong-stable manifold decay exponentially. For \(h=0\), every nonzero solution has the displayed algebraic asymptotic.

4. If \(\mu>1\), zero is unstable.

Thus the transition at \(\mu=1\) is not a loss of attraction at the endpoint itself: exponential attraction for \(\mu<1\) changes to generic \(t^{-1/2}\) attraction at \(\mu=1\), and instability begins for \(\mu>1\).

## Proof

### Subcritical regime

For \(x(t)\ne0\),
\[
D^+|x(t)|
\le -|x(t)|+\mu|x(t-h)|
\le -|x(t)|+\mu\sup_{s\in[t-h,t]}|x(s)|.
\]
Halanay's inequality gives global exponential decay when \(\mu<1\), with the rate stated above.

### Critical global stability

Set \(y=x(t-h)\). Direct differentiation gives
\[
\begin{aligned}
\dot V
&=x(t)(\sin y-x(t))
 +\frac12\bigl(x(t)^2-y^2\bigr)\\
&=x(t)\sin y-\frac12x(t)^2-\frac12y^2\\
&=-\frac12(x(t)-\sin y)^2-\frac12(y^2-\sin^2y).
\end{aligned}
\]
Since \(|\sin y|\le |y|\), this is nonpositive. Equality requires both
\(x(t)=\sin y\) and \(y^2=\sin^2y\). For real \(y\), the second equality forces
\(y=0\), and then \(x(t)=0\).

The functional bounds the current value, so every critical solution is bounded. The equation then bounds \(\dot x\), making positive-time history segments precompact in \(C([-h,0])\). The largest invariant subset of the zero-dissipation set is the zero history: a complete trajectory remaining in that set would have \(x(t)=x(t-h)=0\) for every \(t\). The LaSalle invariance principle for retarded functional differential equations therefore yields \(x_t\to0\) in \(C([-h,0])\). Lyapunov stability follows directly from
\[
V(x_0)\le \frac{1+h}{2}\|x_0\|_\infty^2
\]
and monotonicity of \(V\). Hence zero is globally asymptotically stable at \(\mu=1\).

### Critical spectrum and relaxation

Differentiating \(Q\) along the critical equation gives
\[
Q'=\dot x+x(t)-x(t-h)=\sin x(t-h)-x(t-h).
\]
For a characteristic root with \(\Re\lambda\ge0\),
\[
|\lambda+1|=|e^{-\lambda h}|\le1,
\]
while
\[
|\lambda+1|\ge \Re(\lambda+1)=1+\Re\lambda\ge1.
\]
Equality throughout forces \(\lambda=0\). Moreover
\[
\frac{d}{d\lambda}\bigl(\lambda+1-e^{-\lambda h}\bigr)\Big|_{\lambda=0}=1+h,
\]
so this root is simple and the remaining spectrum is strictly stable.

The equation is odd. A local one-dimensional center manifold can therefore be chosen odd, and in the normalized center coordinate \(u=Q/(1+h)\) its delayed value satisfies
\[
x(t-h)=u+O(u^3).
\]
Using
\[
\sin\xi-\xi=-\frac{\xi^3}{6}+O(\xi^5)
\]
in the exact \(Q\)-identity gives
\[
u'=-\frac{1}{6(1+h)}u^3+O(u^5).
\]
For a nonzero center component,
\[
\frac{d}{dt}u^{-2}
=\frac{1}{3(1+h)}+o(1),
\]
hence
\[
u(t)\sim \sigma\sqrt{\frac{3(1+h)}{t}}.
\]
The stable foliation contributes only exponentially decaying terms relative to this center motion, and \(x(t)=u(t)+O(u(t)^3)\), proving the asymptotic formula. Initial histories on the strong-stable manifold have no center component and decay exponentially.

### Supercritical instability

The linearization has characteristic equation
\[
g(\lambda)=\lambda+1-\mu e^{-\lambda h}=0.
\]
For \(\mu>1\), \(g(0)=1-\mu<0\), whereas \(g(\lambda)\to+\infty\) as real \(\lambda\to+\infty\). Thus a positive real characteristic root exists, so zero is unstable.

## Relation to prior work

The Ikeda equation was introduced as a nonlinear-optical delay model and has a long literature on equilibrium multiplicity, periodic solutions, multistability and chaos. Nardone, Mandel and Kapral (1986) studied stability boundaries of steady and periodic solutions. Kubyshkin and Moriakova (2018) analyzed equilibrium and periodic-solution bifurcations, and their 2020 follow-up treated special cases including the zero-phase, \(\mu=1\) degeneracy through a singular large-delay normal-form construction.

Those local and singular-perturbation results are the closest checked prior work. The strict subcritical stability and supercritical linear instability are not claimed here as new. The contribution of this record is the endpoint package: an explicit delay-independent Lyapunov--Krasovskii identity proving global attraction at exactly \(\mu=1\), together with the all-fixed-delay center observable and sharp generic critical relaxation coefficient \(\sqrt{3(1+h)}\). To the best of our knowledge, this package is not stated in the checked Ikeda literature. The 2020 normal form is a significant residual-coverage risk because it studies the same local degeneracy and may implicitly encode the cubic zero-mode coefficient in a different singular scaling.

## Limitations

The result is restricted to zero phase shift. It does not classify the nonzero equilibria, periodic attractors or chaotic dynamics for \(\mu>1\). The \(t^{-1/2}\) law is generic at the critical point but excludes histories on the strong-stable manifold when \(h>0\). The center asymptotic invokes standard smooth invariant-manifold and stable-foliation theory for retarded functional differential equations. Originality is asserted only to the best of our knowledge; older broad absolute-stability results for scalar delay equations and the 2020 Ikeda normal-form paper remain the most plausible sources of equivalent implicit statements.

## References

- P. Nardone, P. Mandel, R. Kapral, *Analysis of a delay-differential equation in optical bistability*, Phys. Rev. A 33 (1986), 2465. https://doi.org/10.1103/PhysRevA.33.2465
- E. P. Kubyshkin, A. R. Moriakova, *Features of Bifurcations of Periodic Solutions of the Ikeda Equation*, Russian Journal of Nonlinear Dynamics 14 (2018), 301--324. https://doi.org/10.20537/nd180302
- E. P. Kubyshkin, A. R. Moriakova, *Analysis of Special Cases in the Study of Bifurcations of Periodic Solutions of the Ikeda Equation*, Russian Journal of Nonlinear Dynamics 16 (2020), 437--451. https://doi.org/10.20537/nd200303
- J. K. Hale, S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Springer, 1993. https://doi.org/10.1007/978-1-4612-4342-7
