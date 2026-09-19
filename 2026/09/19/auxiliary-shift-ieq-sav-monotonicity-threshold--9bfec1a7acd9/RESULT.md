# Auxiliary-energy shifts control IEQ/SAV Allen–Cahn monotonicity reversals

## Statement

Consider the Allen–Cahn equation
\[
u_t=\Delta u-\varepsilon^{-2}f(u),\qquad
f(u)=u^3-u,\qquad
F(u)=\tfrac14(u^2-1)^2,
\]
under periodic or homogeneous Neumann boundary conditions.  Li and Wang, arXiv:2609.19023v1, show that the first-order IEQ and SAV schemes can lose the exact flow's pointwise monotone direction for sufficiently large time steps.  On the spatially homogeneous invariant class, their formulas admit a sharper description.

Let \(V=|\Omega|\), let \(c=C_{\rm IEQ}>0\), and normalize the SAV shift by
\[
\widehat c:=\frac{\varepsilon^2 C_0}{V}.
\]
If \(\widehat c=c\), then the homogeneous IEQ and SAV recurrences are exactly conjugate for every time step: with
\[
q^n=\frac{\varepsilon}{\sqrt V}\,r^n,
\]
consistent IEQ and SAV initializations produce the same phase sequence \(u^n\) and the same scaled auxiliary sequence for all \(n\).

For a homogeneous initial value \(u_0\in(0,1)\), write
\[
x=\frac{\tau}{\varepsilon^2},\qquad A=(1-u_0^2)^2.
\]
The common first phase iterate is
\[
\boxed{
 u^1(c)=u_0+
 \frac{x u_0(1-u_0^2)(A+4c)}
 {A+4c+2x u_0^2A}.
}
\]
It is strictly increasing in the otherwise arbitrary positive shift \(c\).  The exact overshoot threshold is
\[
\boxed{
\tau_*(c)=
\varepsilon^2\frac{A+4c}
{u_0\big((1-u_0)A+4(1+u_0)c\big)}.
}
\]
Moreover,
\[
\boxed{
\frac{d\tau_*}{dc}
=-\frac{8\varepsilon^2A}
{\big((1-u_0)A+4(1+u_0)c\big)^2}<0,
}
\]
and
\[
\boxed{
\lim_{c\downarrow0}\tau_*(c)=\frac{\varepsilon^2}{u_0(1-u_0)},\qquad
\lim_{c\to\infty}\tau_*(c)=\frac{\varepsilon^2}{u_0(1+u_0)}.
}
\]
Thus increasing the energy shift strictly lowers the time step at which the source paper's overshoot-and-reversal mechanism begins.

There is an exact shift-controlled sign bifurcation.  If
\[
\frac1{u_0(1+u_0)}<x<\frac1{u_0(1-u_0)},
\]
then the unique critical normalized shift is
\[
\boxed{
 c_{\rm crit}(x)=
 \frac{A\bigl(1-xu_0(1-u_0)\bigr)}
 {4\bigl(xu_0(1+u_0)-1\bigr)}>0.
}
\]
For \(0<c<c_{\rm crit}\), the first iterate satisfies \(0<u^1<1\) and the second increment is positive.  At \(c=c_{\rm crit}\), \(u^1=u^2=1\).  For \(c>c_{\rm crit}\), \(u^1>1\) and the second increment is negative.  Hence, at fixed physical equation, initial state and time step, changing only the auxiliary energy shift can switch the discrete phase trajectory from the correct second-step direction to the wrong one.

## Exact IEQ/SAV conjugacy on homogeneous states

The source IEQ scheme is
\[
\frac{u^{n+1}-u^n}{\tau}
=-\varepsilon^{-2}q^{n+1}\frac{f(u^n)}{Q_n},
\qquad
q^{n+1}-q^n
=\frac12\frac{f(u^n)}{Q_n}(u^{n+1}-u^n),
\]
where
\[
Q_n=\sqrt{F(u^n)+c}.
\]
For a homogeneous phase, the source SAV scheme has
\[
S_n=\left(\frac{V}{\varepsilon^2}F(u^n)+C_0\right)^{1/2}
=\frac{\sqrt V}{\varepsilon}Q_n
\]
when \(C_0=Vc/\varepsilon^2\).  Its phase equation contains the ratio \(r^{n+1}/S_n\), while its scalar update reduces to
\[
r^{n+1}-r^n
=\frac{V}{2\varepsilon^2S_n}f(u^n)(u^{n+1}-u^n).
\]
Substituting \(r^n=(\sqrt V/\varepsilon)q^n\) gives exactly the IEQ auxiliary update and the same phase equation.  Consistent initial data satisfy the same scaling, so induction proves the conjugacy for all iterates.

In particular, the two threshold formulas reported separately in arXiv:2609.19023v1 collapse to one formula after replacing the SAV constant by \(\widehat c=\varepsilon^2C_0/V\).

## Shift dependence of the first phase update

Eliminating \(q^1\) from the homogeneous IEQ equations gives the source paper's first-step expression.  Since
\[
Q_0^2=\frac14A+c,
\]
it can be written as the boxed rational formula above.  Differentiation yields
\[
\frac{\partial u^1}{\partial c}
=
\frac{8x^2u_0^3(1-u_0^2)A}
{\big(A+4c+2xu_0^2A\big)^2}>0.
\]
Thus the shift monotonically increases the phase advance at every fixed positive time step.  Its two endpoint limits are
\[
\lim_{c\downarrow0}u^1(c)
=u_0+\frac{x u_0(1-u_0^2)}{1+2xu_0^2},
\]
while
\[
\lim_{c\to\infty}u^1(c)
=u_0+xu_0(1-u_0^2),
\]
the explicit-Euler first step for the homogeneous Allen–Cahn reaction ODE.  Thus larger auxiliary shifts continuously weaken the first-step quadratization feedback toward explicit Euler.

Solving \(u^1(c)>1\) gives exactly \(\tau>\tau_*(c)\).  The threshold is therefore an if-and-only-if condition for first-step overshoot on this homogeneous class, not merely a sufficient large-step estimate.

## Complete second-increment phase diagram

The source paper proves that the second IEQ scaling factor is positive:
\[
\vartheta_2=
\frac{2q^1Q_1}
{2Q_1^2+(\tau/\varepsilon^2)(u^1-(u^1)^3)^2}>0,
\]
and analogously for SAV.  Therefore
\[
\operatorname{sgn}(u^2-u^1)
=\operatorname{sgn}\big(u^1(1-(u^1)^2)\big).
\]
Because \(u^1>u_0>0\), the second increment is positive exactly when \(u^1<1\), zero when \(u^1=1\), and negative exactly when \(u^1>1\).

Consequently:

- if \(x\le 1/[u_0(1+u_0)]\), no finite positive shift triggers a first-step overshoot, so the second increment is nonnegative;
- if \(1/[u_0(1+u_0)]<x<1/[u_0(1-u_0)]\), the unique \(c_{\rm crit}(x)\) above switches the sign of the second increment;
- if \(x\ge1/[u_0(1-u_0)]\), every positive shift produces a first-step overshoot and hence a negative second increment.

This is a complete shift/time-step phase diagram for the source paper's homogeneous IEQ/SAV reversal mechanism.

## Example

Take
\[
u_0=\frac12,\qquad \varepsilon=1,\qquad \tau=2.
\]
Then
\[
\frac{1}{u_0(1+u_0)}=\frac43<2<4=\frac{1}{u_0(1-u_0)},
\]
and
\[
 c_{\rm crit}=\frac{9}{64}=0.140625.
\]
For \(c=0.05\), direct recurrence evaluation gives
\[
u^1=0.931603773584906,\qquad
u^2-u^1=+0.207453418199297.
\]
At \(c=9/64\),
\[
u^1=u^2=1.
\]
For \(c=0.5\),
\[
u^1=1.115000000000000,\qquad
u^2-u^1=-0.434127937674123.
\]
The original Allen–Cahn ODE is identical in all three cases; only the auxiliary shift changes.

## Interpretation

At the continuous level, the constants added inside IEQ/SAV square roots do not change the Allen–Cahn gradient flow when the auxiliary variable remains exactly tied to its defining energy quantity.  The discrete auxiliary update breaks this exact shift invariance.  On the homogeneous class, that loss is strong enough to alter the sign of a phase increment.

This should not be read as a general recommendation to minimize the auxiliary constant in every IEQ/SAV computation.  Other analyses have already observed that auxiliary shifts can affect numerical accuracy, and in other models a larger shift can improve conditioning or error constants.  The present result is narrower: for the specific first-order Allen–Cahn IEQ/SAV recurrences analyzed in arXiv:2609.19023v1, the shift has an exact and monotone effect on the source's pointwise-monotonicity failure threshold.

## Originality boundary

The following are prior art and are not claimed as new: IEQ and SAV themselves; their continuous equivalence to the underlying gradient flow with consistent auxiliary initialization; the need for a positive shift in classical square-root formulations; the fact that discretized auxiliary variables need not remain exactly consistent with their continuous definitions; and the broader fact that SAV accuracy can depend on a potential shift.  In particular, Liu (2019) discusses the practical difficulty of choosing the positive constant, Jiang et al. (2022) analyze discrete auxiliary-variable consistency and relaxation, Shen and Yang (2020) survey IEQ/SAV in a unified setting, and Russo--Ducceschi--Bilbao (2026) report strong potential-shift dependence for SAV discretizations of nonlinear string models.

The claim here is restricted to the source-specific Allen–Cahn result: exact homogeneous IEQ/SAV conjugacy after the normalization \(C_{\rm IEQ}=\varepsilon^2C_0/|\Omega|\), the strict closed-form dependence of the overshoot threshold on that normalized shift, and the resulting exact shift-controlled sign bifurcation of the second phase increment.  No checked source was found to state this phase diagram.

## Limitations

The exact IEQ/SAV conjugacy is specific to spatially homogeneous states.  Away from that invariant class, IEQ uses a pointwise auxiliary field while SAV uses a global scalar auxiliary variable, so the schemes are genuinely different.  The sign bifurcation concerns the first two steps from consistent homogeneous initialization; it is not a global-in-time stability theorem, a convergence theorem, or an assertion that one shift is universally optimal.  The persistence results in arXiv:2609.19023v1 imply that strict homogeneous reversals can survive sufficiently small nonhomogeneous perturbations for each fixed scheme, but the present calculation does not derive a uniform perturbation radius as the shift varies.

## Reproducibility

`artifacts/verify_auxiliary_shift.py` evaluates the exact homogeneous IEQ and SAV recurrences, verifies their scaled conjugacy, checks the critical-shift example, and records the monotone threshold law.  `artifacts/verification_output.txt` is the corresponding deterministic output.

## References

1. P. Li and D. Wang, *Pointwise Monotonicity of the Allen–Cahn Flow and Dynamical Limitations of Energy-Stable Schemes*, arXiv:2609.19023v1. https://arxiv.org/abs/2609.19023
2. J. Shen and X. Yang, *The IEQ and SAV approaches and their extensions for a class of highly nonlinear gradient flow systems*, Contemporary Mathematics 754 (2020), 217–245. https://doi.org/10.1090/conm/754/15147
3. Z. Liu, *Efficient invariant energy quadratization and scalar auxiliary variable approaches without bounded below restriction for phase field models*, arXiv:1906.03621. https://arxiv.org/abs/1906.03621
4. M. Jiang, Z. Zhang, and J. Zhao, *Improving the accuracy and consistency of the scalar auxiliary variable (SAV) method with relaxation*, Journal of Computational Physics 456 (2022), 110954. https://doi.org/10.1016/j.jcp.2022.110954
5. R. Russo, M. Ducceschi, and S. Bilbao, *Numerical convergence of the scalar auxiliary variable method applied to nonlinear stiff string models*, Nonlinear Dynamics 114 (2026), article 857. https://doi.org/10.1007/s11071-026-12708-0
