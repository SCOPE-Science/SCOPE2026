# Exact default-parameter local stability ceiling for Adan
## Finding

Consider the deterministic scalar quadratic
\[
f(x)=\frac{h}{2}x^2,
\qquad h>0.
\]
Use Adan with no weight decay, no gradient clipping, and constant base learning rate \(\eta>0\). In the paper's coefficient convention, the default moving-average weights are
\[
\beta_1=0.02,
\qquad
\beta_2=0.08,
\qquad
\beta_3=0.01.
\]
These correspond to decay coefficients \((0.98,0.92,0.99)\) in common implementations.

Write the paper-form first-moment and gradient-difference recurrences as
\[
m_k=(1-\beta_1)m_{k-1}+\beta_1 g_k,
\]
\[
v_k=(1-\beta_2)v_{k-1}+\beta_2(g_k-g_{k-1}),
\]
with
\[
g_k=h x_k.
\]
The Adan search direction is
\[
d_k=m_k+(1-\beta_2)v_k.
\]
The squared adaptive state is driven by a square of the Nesterov-corrected gradient. Consequently its innovation has zero first derivative at the minimizer, so its linearized eigenvalue is simply
\[
1-\beta_3=0.99.
\]

Let
\[
s=\frac{\eta h}{\varepsilon}.
\]
After the bias-correction factors have converged to one, the asymptotic local dynamics of \((x,m,v)\), together with one lagged iterate needed by the gradient difference, have characteristic polynomial
\[
P_s(r)
=
r^3
+
\left(
\frac{117}{1250}s-rac{29}{10}
\right)r^2
+
\left(
\frac{1751}{625}-\frac{5129}{31250}s
\right)r
+
\left(
\frac{1127}{15625}s-rac{1127}{1250}
\right).
\]
One apparent fourth state is algebraically redundant, leaving this cubic for the optimization block.

The minimizer is asymptotically locally exponentially stable exactly when
\[
0<s<\frac{19800}{859}.
\]
Numerically,
\[
\frac{19800}{859}
\approx
23.049.
\]
At the upper boundary,
\[
P_s(-1)=0,
\]
so the instability begins through an exact period-doubling root \(-1\).

For comparison, suppress the gradient-difference EMA while keeping the same first-moment coefficient \(\beta_1=0.02\). The resulting normalized momentum recurrence has exact scalar stability ceiling
\[
s<198.
\]
Thus the default Adan gradient-difference channel reduces the epsilon-floor local stability ceiling by the factor
\[
\frac{198}{19800/859}
=
\frac{859}{100}
=
8.59.
\]
This does not contradict Adan's empirical tolerance of large learning rates: away from the optimum, its adaptive squared-moment denominator can be much larger than \(\varepsilon\). The result isolates the final local regime after that adaptive state has decayed toward its floor.

## Assumptions and scope

The theorem uses the paper-form Adan coefficients and the deterministic scalar quadratic. Weight decay, clipping, restart logic, and stochastic gradients are disabled.

The actual implementation uses bias corrections. The claim is asymptotic local stability because those correction factors converge to one. The stated cubic is the limiting Jacobian polynomial.

The squared adaptive state is not ignored: its first-order eigenvalue is \(0.99\). Its innovation is quadratic in the local state, so it does not alter the first-order optimization cubic.

The theorem is about local stability of the minimizer. It does not claim that trajectories starting far from the minimizer immediately use denominator \(\varepsilon\).

## Proof

Normalize the two linear momentum states by \(h\):
\[
p_k=\frac{m_k}{h},
\qquad
q_k=\frac{v_k}{h}.
\]
For a modal solution proportional to \(r^k\), the first-moment recurrence gives
\[
\frac{p_k}{x_k}
=
\frac{\beta_1 r}{r-1+\beta_1},
\]
while the gradient-difference recurrence gives
\[
\frac{q_k}{x_k}
=
\frac{\beta_2(r-1)}{r-1+\beta_2}.
\]
Near the minimizer the adaptive denominator tends to \(\varepsilon\), so the parameter update is
\[
x_{k+1}
=
x_k-s\left[p_k+(1-\beta_2)q_k\right].
\]
Eliminating \(p_k\) and \(q_k\) yields
\[
(r-1)(r-1+\beta_1)(r-1+\beta_2)
+
s\left[
\beta_1r(r-1+\beta_2)
+(1-\beta_2)\beta_2(r-1)(r-1+\beta_1)
\right]
=0.
\]
Substituting
\[
\beta_1=\frac1{50},
\qquad
\beta_2=\frac2{25}
\]
and expanding gives the displayed cubic.

For a monic real cubic
\[
r^3+a r^2+b r+c,
\]
Schur stability is equivalent to
\[
|c|<1,
\qquad
1+a+b+c>0,
\qquad
1-a+b-c>0,
\qquad
1-b+ac-c^2>0.
\]
For the present coefficients these conditions simplify to
\[
\frac{59425-2254s}{31250}>0,
\]
\[
\frac{3075+2254s}{31250}>0,
\]
\[
\frac{s}{625}>0,
\]
\[
\frac{6(19800-859s)}{15625}>0,
\]
and
\[
\frac{1512434s^2+613525s+153750}{976562500}>0.
\]
For \(s>0\), the quadratic condition and the second displayed condition are automatic. The bound
\[
s<\frac{19800}{859}
\]
is stricter than
\[
s<\frac{59425}{2254}.
\]
Hence it is the exact stability ceiling. The active Jury condition is equality at \(r=-1\), proving sharpness.

If the gradient-difference channel is removed, the normalized first-moment decay is \(0.98\) and its current-gradient weight is \(0.02\). The standard second-order Jury calculation gives
\[
s<\frac{2(1+0.98)}{0.02}=198.
\]

## Verification

The accompanying `verify.py` reconstructs the cubic with exact rational arithmetic, evaluates all four cubic Schur conditions, verifies the exact \(-1\) boundary root, and checks roots immediately on both sides of the threshold.

The computation is an algebraic transcription guard. The exact interval follows from the symbolic elimination and Schur inequalities above.

## Relationship to prior work

Xie, Zhou, Li, Lin, and Yan introduced Adan to combine an efficient Nesterov momentum estimate with adaptive first- and second-order gradient moments. Their theory proves stochastic nonconvex complexity bounds and emphasizes that Adan tolerates comparatively large learning rates. The inspected source gives the momentum, gradient-difference, squared-moment, and proximal updates but does not state a deterministic scalar local Schur boundary.

The default implementation convention uses decay coefficients \((0.98,0.92,0.99)\), which are complements of the paper's current-sample coefficients \((0.02,0.08,0.01)\). Public implementation notes explicitly warn about this convention difference. The present calculation fixes the paper convention before deriving the polynomial.

Focused searches for Adan quadratic stability, local Jacobians, gradient-difference characteristic polynomials, and exact stepsize frontiers did not identify a covering result.

## Limitations

The result is local and deterministic. It does not characterize the nonlinear attractor if the minimizer is locally unstable.

The exact rational ceiling uses the paper's default three coefficients. Other coefficient choices produce a different cubic Schur region.

The result disables weight decay, clipping, and restart logic in order to isolate Adan's Nesterov-momentum mechanism.

The denominator floor matters only asymptotically near a deterministic minimizer. In practical stochastic training, persistent gradient noise can keep the adaptive denominator above this floor.

## References

1. Xingyu Xie, Pan Zhou, Huan Li, Zhouchen Lin, and Shuicheng Yan, “Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models,” arXiv:2208.06677v1, 2022.
2. Public Adan implementation documentation using decay coefficients \((0.98,0.92,0.99)\) and documenting their relation to the paper convention.
