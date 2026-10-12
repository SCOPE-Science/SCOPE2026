# Exact reset budget and terminal-rate window of MPG-NGD on scalar quadratics
## Finding

Consider Algorithm 2 (MPG-NGD) on the unconstrained scalar quadratic
\[
f(x)=\frac L2x^2,
\qquad
L>0,
\qquad
C=\mathbb R.
\]
Assume the algorithm has not already reached \(x=0\).

Its adaptive stepsize rule collapses exactly to
\[
\lambda_k=
\begin{cases}
2\eta_1/L,&\lambda_{k-1}>2\eta_0/L,\\
(1+\varepsilon_{k-1})\lambda_{k-1},&\lambda_{k-1}\le2\eta_0/L.
\end{cases}
\]
Thus the curvature test is a threshold-reset controller with

\[
\tau=\frac{2\eta_0}{L}
\]
as the reset threshold and
\[
r=\frac{2\eta_1}{L}
\]
as the reset value.

Let
\[
P=\prod_{j=0}^{\infty}(1+\varepsilon_j).
\]
Because
\[
\sum_{j=0}^{\infty}\varepsilon_j<\infty,
\]
the product \(P\) is finite. If \(N\) is the total number of reset events, then
\[
N\le
\left\lceil
\frac{\log P}{\log(\eta_0/\eta_1)}
\right\rceil.
\]

If at least one reset occurs and the trajectory does not terminate finitely, then after the last reset the stepsizes increase monotonically and converge to
\[
\lambda_\infty\in
\left(
\frac{2\eta_1}{L},
\frac{2\eta_0}{L}
\right].
\]
Every point of that interval is realizable by a positive summable expansion tail.

The scalar iterates satisfy
\[
x_{k+1}=(1-L\lambda_k)x_k,
\]
so
\[
\lim_{k\to\infty}
\frac{|x_{k+1}|}{|x_k|}
=
|1-L\lambda_\infty|.
\]

In the strongly convex parameter regime used in the source theorem,
\[
\eta_0\le\frac12,
\]
every nonterminating trajectory that has reset has asymptotic factor in
\[
\left[
1-2\eta_0,
1-2\eta_1
\right).
\]
Every factor in this interval is attainable.

For the numerical choice repeatedly used in the source,
\[
(\eta_0,\eta_1)=(0.5,0.49),
\]
one reset forces
\[
0\le
\lim_{k\to\infty}
\frac{|x_{k+1}|}{|x_k|}
<
0.02.
\]
A suitable positive summable tail can even make
\[
\lambda_\infty=\frac1L,
\]
so that the limiting one-step factor is zero.

There is a complementary slow branch: if no reset ever occurs, then sufficiently small initial stepsizes can lead to limits arbitrarily close to zero and hence asymptotic error factors arbitrarily close to one. Therefore rapid scalar self-tuning is conditional on entering the reset mechanism.

## Assumptions and scope

The objective is the scalar strongly convex quadratic
\[
f(x)=\frac L2x^2.
\]
The constraint set is all of \(\mathbb R\), so the projected step equals the ordinary gradient step.

The algorithmic parameters satisfy the source conditions
\[
0<\eta_1<\eta_0<1
\]
and
\[
\varepsilon_k>0,
\qquad
\sum_{k=0}^{\infty}\varepsilon_k<\infty.
\]

The recurrence is stated only while the iteration is nonterminal. If an iterate reaches \(x=0\), the optimization problem is already solved.

The reset-count bound is independent of the initial iterate and depends on the expansion sequence only through its total multiplicative budget \(P\).

## Proof

For the scalar quadratic,
\[
f'(x)=Lx.
\]
At a nonterminal iteration let
\[
d_k=x_k-x_{k-1}\ne0.
\]
The curvature quantity used in the MPG-NGD test is
\[
f(x_k)-f(x_{k-1})-f'(x_{k-1})d_k.
\]
Direct expansion gives
\[
f(x_k)-f(x_{k-1})-f'(x_{k-1})d_k
=
\frac L2d_k^2.
\]

Hence the source condition
\[
f(x_k)-f(x_{k-1})-f'(x_{k-1})d_k
>
\frac{\eta_0}{\lambda_{k-1}}d_k^2
\]
is equivalent to
\[
\lambda_{k-1}>
\frac{2\eta_0}{L}.
\]

When the test is true, the source update becomes
\[
\lambda_k
=
\eta_1
\frac{d_k^2}
{(L/2)d_k^2}
=
\frac{2\eta_1}{L}.
\]
When the test is false,
\[
\lambda_k=(1+\varepsilon_{k-1})\lambda_{k-1}.
\]
This proves the exact threshold-reset recursion.

Now set
\[
\tau=\frac{2\eta_0}{L},
\qquad
r=\frac{2\eta_1}{L}.
\]
Because \(\eta_1<\eta_0\),
\[
r<\tau.
\]

Suppose reset events occur at indices
\[
j_1<j_2<\cdots<j_N.
\]
After every reset,
\[
\lambda_{j_q}=r.
\]
For any two consecutive resets \(j_q<j_{q+1}\), all intervening steps are expansion steps. Therefore
\[
\lambda_{j_{q+1}-1}
=
r
\prod_{i=j_q}^{j_{q+1}-2}(1+\varepsilon_i)
>
\tau.
\]
Thus
\[
\prod_{i=j_q}^{j_{q+1}-2}(1+\varepsilon_i)
>
\frac{\tau}{r}
=
\frac{\eta_0}{\eta_1}.
\]
The corresponding factor blocks are disjoint. Multiplying over the \(N-1\) gaps between resets gives
\[
P>
\left(\frac{\eta_0}{\eta_1}\right)^{N-1}.
\]
Hence
\[
N-1<
\frac{\log P}{\log(\eta_0/\eta_1)},
\]
which yields the stated integer bound.

After the last reset \(j_N\), no later iterate can have a stepsize exceeding \(\tau\), otherwise another reset would occur at the next iteration. Therefore
\[
\lambda_k
=
r\prod_{i=j_N}^{k-1}(1+\varepsilon_i)
\]
is increasing and bounded above by \(\tau\). It converges to
\[
\lambda_\infty
=
r\prod_{i=j_N}^{\infty}(1+\varepsilon_i)
\le\tau.
\]
Because every remaining \(\varepsilon_i\) is positive,
\[
\lambda_\infty>r.
\]

Conversely, choose any
\[
\bar\lambda\in(r,\tau].
\]
Set
\[
Q=\frac{\bar\lambda}{r}\in
\left(
1,
\frac{\eta_0}{\eta_1}
\right].
\]
Choose a positive summable sequence by
\[
1+\varepsilon_m
=
\exp\!\left(
\frac{\log Q}{2^{m+1}}
\right),
\qquad
m=0,1,2,\ldots.
\]
Then
\[
\prod_{m=0}^{\infty}(1+\varepsilon_m)=Q,
\]
and all partial products are at most \(Q\). Starting immediately after a reset, this realizes
\[
\lambda_\infty=\bar\lambda
\]
without causing another reset.

Finally, on \(C=\mathbb R\),
\[
x_{k+1}
=
x_k-\lambda_kLx_k
=
(1-L\lambda_k)x_k.
\]
Thus, for a nonterminating trajectory,
\[
\frac{|x_{k+1}|}{|x_k|}
=
|1-L\lambda_k|
\longrightarrow
|1-L\lambda_\infty|.
\]

If
\[
\eta_0\le\frac12,
\]
then every post-reset limit obeys
\[
0<L\lambda_\infty\le1.
\]
Therefore
\[
|1-L\lambda_\infty|
=
1-L\lambda_\infty
\in
\left[
1-2\eta_0,
1-2\eta_1
\right).
\]

If no reset occurs, then
\[
\lambda_k
=
\lambda_0
\prod_{i=0}^{k-1}(1+\varepsilon_i)
\]
and
\[
\lambda_\infty=\lambda_0P\le\tau.
\]
Taking \(\lambda_0\) arbitrarily small makes \(\lambda_\infty\) arbitrarily small, hence makes the asymptotic factor arbitrarily close to one.

## Verification

The standalone script `artifacts/verify_mpg_quadratic.py` checks the exact reduction of the source curvature expression, replays the threshold-reset recursion, verifies the reset-count inequality on representative summable expansion sequences, and confirms the predicted asymptotic ratios.

The universal statements in the finding are proved analytically above; finite computation is used only as supporting evidence.

## Relationship to prior work

The primary manuscript introduces MPG-NGD as a parameter-free projected-gradient method with a stepsize sequence that is eventually nondecreasing and convergent to a positive limit. Its Algorithm 2 uses the same function-value curvature expression analyzed here, and its Lemmas 4.1--4.2 prove eventual monotonicity abstractly.

The scalar calculation gives substantially more information: the curvature rule becomes an exact two-state controller, the total number of resets is bounded by the finite multiplicative expansion budget, and the entire post-reset terminal-rate window can be described and realized exactly.

The manuscript also reproduces the earlier PG-NGD rule based on gradient differences. On the same scalar quadratic that earlier rule has a related threshold structure, but with a different normalization. The present result concerns the modified function-value rule and its factor-two curvature scale.

A later inexact adaptive proximal-gradient manuscript by the same author uses a different composite and inexact-proximal framework. Its public description establishes adaptive stepsize convergence properties but does not state the MPG-NGD scalar reset budget or terminal-rate interval.

Targeted searches by the method name, paper title, scalar-quadratic specialization, reset terminology, terminal stepsize, and the parameters \(\eta_0,\eta_1\) did not locate the exact classification above.

## Limitations

The finding is exact for one-dimensional unconstrained quadratics. It does not claim that multidimensional MPG-NGD has a scalar threshold-reset recursion.

The terminal-rate window is an asymptotic statement after at least one reset. A trajectory that never resets can remain arbitrarily conservative.

The zero limiting factor at
\[
\lambda_\infty=1/L
\]
means that the ratio of successive errors tends to zero; it does not assert finite termination unless some finite iterate has exactly that stepsize.

## References

1. P. T. Hoai, N. D. Hoang, F. Lara, *A Modified Projected Gradient Algorithm for Solving Quasiconvex Programming with Applications*, Optimization Online, first public 4 March 2026, repository record 33877.
2. P. T. Hoai, *New inexact adaptive proximal gradient algorithms for nonconvex composite optimization problems*, Optimization Online, first public 31 August 2026, repository record 36519.
