# Exact spike-and-reset law for NIPG on scalar strongly convex quadratics
## Finding

Consider Algorithm 3.1 NIPG\(\ell\), \(\ell\in\{1,2\}\), in its exact proximal specialization on
\[
F(x)=\frac a2x^2,\qquad a>0,\qquad g\equiv0.
\]
Let \(0<c_1<c_0\le1/2\), let \(t_k>0\) be the adaptive stepsize, and suppose \(x_k\ne0\). Then the complete scalar dynamics are
\[
x_{k+1}=(1-a t_k)x_k,
\]
\[
A_1(x_k,x_{k+1})=A_2(x_k,x_{k+1})=a|x_{k+1}-x_k|^2,
\]
and
\[
\frac{F(x_{k+1})}{F(x_k)}=(1-a t_k)^2.
\]
Consequently, whenever the post-step curvature test fires, equivalently whenever
\[
a t_k>c_0,
\]
the next stepsize is reset exactly to
\[
t_{k+1}=\frac{c_1}a.
\]

On an expansion step, \(a t_k\le c_0\) and
\[
t_{k+1}=(1+\gamma'_k)t_k.
\]
The sharp uniform scalar objective-safety cap for such an expansion is
\[
\gamma'_k\le\frac2{c_0}-1.
\]
Indeed, this condition forces \(a t_{k+1}\le2\), so the next quadratic objective value cannot exceed the current one. Conversely, at the boundary state \(a t_k=c_0\), any larger expansion factor gives \(a t_{k+1}>2\) and therefore a strict objective increase.

The source initialization makes the transient obstruction particularly explicit. Choose
\[
t_{-1}=t_0=\frac{c_0}a,\qquad x_0\ne0.
\]
Because the curvature test is strict, equality sends the first iteration to the expansion branch and, since \(t_0/t_{-1}=1\), one has \(\gamma'_0=\gamma_0\). Thus
\[
\frac{F(x_1)}{F(x_0)}=(1-c_0)^2<1,
\]
but
\[
\frac{F(x_2)}{F(x_1)}=\bigl[1-c_0(1+\gamma_0)\bigr]^2.
\]
For every prescribed \(M>0\), an admissible summable positive sequence can be chosen with
\[
\gamma_0>\frac{1+\sqrt M}{c_0}-1,
\]
which makes \(F(x_2)/F(x_1)>M\). Since \(\gamma_0>0\) also implies \(a t_1>c_0\), the next curvature test resets
\[
t_2=\frac{c_1}a.
\]
So the method permits arbitrarily large finite transient amplification even after an initially decreasing step, but on this model it repairs the offending stepsize exactly one update later.

## Assumptions and scope

The claim uses exact proximal subproblems, so the inexactness variables are \(v^k=0\) and \(\varepsilon_k=0\). This is explicitly allowed by the source framework. The smooth term is the one-dimensional globally strongly convex quadratic \(f(x)=a x^2/2\), and the nonsmooth term is identically zero. Both source curvature choices \(A_1\) and \(A_2\) therefore coincide.

The unbounded-amplification statement ranges over algorithmically admissible input sequences \((\gamma_k)\): positive and summable, with no source-imposed upper bound on the initial term. It is a finite-transient statement and does not contradict the source's eventual descent or convergence theorems.

## Proof

For \(g\equiv0\), the exact proximal step is the identity proximal map applied after the forward gradient step. Since \(\nabla f(x)=a x\),
\[
x_{k+1}=x_k-t_k a x_k=(1-a t_k)x_k.
\]
Writing \(\Delta_k=x_{k+1}-x_k=-a t_kx_k\), the two source curvature quantities satisfy
\[
A_1(x_k,x_{k+1})=|a(x_k-x_{k+1})(x_k-x_{k+1})|=a|\Delta_k|^2,
\]
and
\[
A_2(x_k,x_{k+1})=|a(x_k-x_{k+1})|\,|x_k-x_{k+1}|=a|\Delta_k|^2.
\]
When \(x_k\ne0\), one has \(\Delta_k\ne0\), so the Step 3 test
\[
A_\ell(x_k,x_{k+1})>\frac{c_0}{t_k}|\Delta_k|^2
\]
is equivalent to \(a t_k>c_0\). In that case the source update gives
\[
t_{k+1}=c_1\frac{|\Delta_k|^2}{A_\ell(x_k,x_{k+1})}=\frac{c_1}a.
\]
If instead \(a t_k\le c_0\), the algorithm takes the expansion branch and sets \(t_{k+1}=(1+\gamma'_k)t_k\), with the source's ratio-dependent truncation included in \(\gamma'_k\).

For the quadratic objective,
\[
\frac{F(x_{k+1})}{F(x_k)}=(1-a t_k)^2.
\]
A positive stepsize is objective-nonincreasing exactly when \(0<a t_k\le2\). Therefore, if \(a t_k\le c_0\), the uniform condition
\[
1+\gamma'_k\le\frac2{c_0}
\]
ensures \(a t_{k+1}\le2\). Sharpness follows by taking the boundary state \(a t_k=c_0\): any larger expansion makes \(a t_{k+1}>2\), and the next objective ratio exceeds one.

Finally initialize \(t_{-1}=t_0=c_0/a\). The strict inequality in the curvature test fails at equality, while \(t_0/t_{-1}=1\) prevents the ratio-dependent truncation. Hence \(t_1=(1+\gamma_0)c_0/a\). The two displayed objective ratios follow immediately. A positive summable sequence may have an arbitrarily large first term—for example, choose the desired \(\gamma_0\) and then \(\gamma_k=2^{-k}\) for \(k\ge1\). This proves unbounded second-step amplification. Because \(a t_1=c_0(1+\gamma_0)>c_0\), Step 3 at the next nonstationary iterate sets \(t_2=c_1/a\), proving the exact reset.

## Verification

The standalone script `artifacts/verify_nipg_spike.py` uses exact rational arithmetic. It checks both curvature formulas, the strict-test equality branch, the exact reset, representative large spike factors, and the sharp expansion-safety threshold. The script is a finite consistency check; the all-parameter statement is proved algebraically above.

## Relationship to prior work

The 2026 NIPG paper defines the inexact adaptive method, explicitly includes exact proximal steps as a special case, and uses the post-step curvature test and expansion rule analyzed here. Its convergence and objective-descent guarantees begin only from a finite iteration \(k_\ell^*\); it does not state a finite-transient amplification bound.

The immediate 2024 predecessor develops NPG1, whose exact update is recovered by NIPG2 up to a parameter-range change. That paper likewise proves objective descent only from a fixed iteration and explains that summability of the expansion sequence eventually controls the stepsizes. Its full text does not state the scalar spike-and-reset law, the unbounded transient factor, or the sharp scalar expansion-safety cap above.

Targeted database searches for NIPG, NPG1, adaptive proximal-gradient overshoot, post-hoc curvature checks, scalar quadratics, transient objective amplification, and summable expansion sequences returned nearby records about other algorithms, including Polyak steps, Nesterov acceleration, CG-based steps, and gradient-mapping accumulation. Those recurrence laws do not imply the present NIPG formula.

## Limitations

The exact law is for the scalar quadratic with exact proximal subproblems. Inexact residuals, nonsmooth nonzero regularizers, multidimensional anisotropic quadratics, and other adaptive proximal-gradient schemes can have different transient behavior.

The unbounded factor uses the absence of an upper bound on an admissible \(\gamma_0\). Practical implementations may deliberately choose small expansion sequences. The structural point is therefore not that large spikes are inevitable, but that the stated theoretical input conditions and post-hoc curvature test alone do not preclude them.

## References

1. P. T. Hoai, N. D. Hao, J.-C. Yao, *New inexact adaptive proximal gradient algorithms for nonconvex composite optimization problems*, Optimization Online, published 2026-08-31, record 36519.
2. P. T. Hoai, N. P. D. Thai, *Composite optimization problems via novel proximal gradient algorithms and applications*, Optimization Online, first published 2024-06-15, record 26741.
