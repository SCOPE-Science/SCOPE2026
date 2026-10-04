# Exact two-by-two determinant law and marginal indistinguishability for Adafactor
## Finding

Let
\[
V=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix},
\qquad
a,b,c,d\ge0,
\qquad
S=a+b+c+d>0.
\]
Adafactor's factored second-moment reconstruction is
\[
\mathcal P(V)
=
\frac{(V\mathbf 1)(\mathbf 1^\top V)}{S}.
\]

In two dimensions its error is exactly
\[
\mathcal P(V)-V
=
\frac{\det V}{S}
\begin{bmatrix}
-1&1\\
1&-1
\end{bmatrix}.
\]
Therefore
\[
\mathcal P(V)=V
\]
if and only if
\[
\det V=0,
\]
equivalently \(V\) has rank at most one.

There is no finite constant \(C\) for which
\[
C^{-1}V_{ij}
\le
\mathcal P(V)_{ij}
\le
CV_{ij}
\]
holds for every positive coordinate of every nonnegative \(2\times2\) matrix.

For underestimation, take
\[
D_M=
\begin{bmatrix}
1&0\\
0&M
\end{bmatrix}.
\]
Then
\[
\mathcal P(D_M)_{11}
=
\frac{1}{1+M},
\]
so the ratio to the true entry tends to zero as \(M\to\infty\).

For overestimation, take
\[
V_\varepsilon=
\begin{bmatrix}
\varepsilon&1-\varepsilon\\
1-\varepsilon&\varepsilon
\end{bmatrix},
\qquad
0<\varepsilon<1.
\]
All row and column sums equal one, hence
\[
\mathcal P(V_\varepsilon)
=
\frac12
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix},
\]
and
\[
\frac{\mathcal P(V_\varepsilon)_{11}}
{(V_\varepsilon)_{11}}
=
\frac{1}{2\varepsilon}
\longrightarrow\infty.
\]

The obstruction is information-theoretic, not specific to the generalized-KL choice. Define
\[
W_\varepsilon=
\begin{bmatrix}
1-\varepsilon&\varepsilon\\
\varepsilon&1-\varepsilon
\end{bmatrix}.
\]
The matrices \(V_\varepsilon\) and \(W_\varepsilon\) have identical row and column sums. Any deterministic reconstruction based only on those marginals must output the same target estimate \(h\) for both. If \(h\) were within a factor \(C\) of both true \((1,1)\) entries, then
\[
\frac{1-\varepsilon}{\varepsilon}
\le
C^2.
\]
No finite \(C\) can satisfy this for all positive \(\varepsilon\).

The same loss of information persists dynamically. Fix
\[
\beta\in(0,1).
\]
Let the first squared-gradient matrix be \(V_\varepsilon\) in one history and \(W_\varepsilon\) in the other. On the second step use exactly the same current squared-gradient matrix \(C\), with
\[
C_{11}=c>0.
\]
The two first-step matrices have identical marginals, so the Adafactor row and column states agree after step one. Because the second gradient is common, those compressed states remain identical after step two.

A full bias-corrected exponential second moment at the target coordinate equals
\[
\frac{\beta\varepsilon+c}{1+\beta}
\]
in the first history and
\[
\frac{\beta(1-\varepsilon)+c}{1+\beta}
\]
in the second. Their ratio is
\[
\frac{\beta(1-\varepsilon)+c}
{\beta\varepsilon+c}.
\]
Taking
\[
c=\varepsilon^2
\]
makes this ratio diverge as \(\varepsilon\to0\). Thus identical compressed state and identical current gradient can hide arbitrarily different full-memory adaptive denominators.

## Assumptions and scope

The theorem isolates Adafactor's factored second-moment reconstruction. It does not assert divergence or poor performance of the complete optimizer.

The static formulas permit nonnegative matrices. The indistinguishable pair is strictly positive for \(0<\varepsilon<1\).

The dynamic statement uses the original exponential second-moment convention with zero initialization and bias correction. It concerns the factored state before optional update clipping, relative parameter scaling, or other safeguards.

A coordinatewise positive floor can impose problem-dependent finite distortion bounds. Such a floor does not restore information discarded by row-column compression.

## Proof

The row sums are
\[
a+b,\qquad c+d,
\]
and the column sums are
\[
a+c,\qquad b+d.
\]
Thus
\[
\mathcal P(V)_{11}
=
\frac{(a+b)(a+c)}{S}.
\]
Subtracting \(a\),
\[
\mathcal P(V)_{11}-a
=
\frac{bc-ad}{S}
=
-\frac{\det V}{S}.
\]
Similarly,
\[
\mathcal P(V)_{12}-b
=
\frac{ad-bc}{S}
=
\frac{\det V}{S}.
\]
The remaining two entries follow by the same expansion, proving the checkerboard formula.

The exactness criterion follows immediately. A nonzero \(2\times2\) matrix has rank one exactly when its determinant vanishes.

The two explicit families prove unbounded underestimation and overestimation by direct substitution.

For the marginal-only lower bound, identical marginals force a common estimate \(h\). A factor-\(C\) approximation to both target entries requires
\[
\frac{1-\varepsilon}{C}
\le
h
\le
C\varepsilon,
\]
hence
\[
\frac{1-\varepsilon}{\varepsilon}
\le
C^2.
\]
This fails for sufficiently small \(\varepsilon\).

For the dynamic statement, after two steps the uncorrected full exponential moment is
\[
(1-\beta)(\beta A+C),
\]
where \(A\) is the first squared-gradient matrix. Dividing by
\[
1-\beta^2=(1-\beta)(1+\beta)
\]
gives
\[
\widehat V_2
=
\frac{\beta A+C}{1+\beta}.
\]
Substitution of \(A=V_\varepsilon\) and \(A=W_\varepsilon\) gives the claimed ratio. Since row and column summation are linear and the first-step marginals coincide, Adafactor's compressed states coincide throughout the two-step comparison.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to check the determinant identity, the two distortion families, the same-marginal pair, and the two-step exponentially smoothed construction.

The finite checks are algebraic transcription guards. The universal impossibility statement is proved symbolically above.

## Relationship to prior work

Shazeer and Stern introduced Adafactor's central memory-saving construction: moving averages of row and column sums replace the full matrix of squared-gradient moments, and the reconstructed matrix is their normalized outer product. They derive this as a generalized-KL-optimal nonnegative rank-one approximation and note that rank-one second-moment matrices are recovered exactly.

The defining paper also introduces update clipping because inaccurate or stale second moments can produce undesirably large updates. The inspected source does not state the two-dimensional determinant error identity, a coordinatewise constant-factor impossibility theorem, or the same-marginal dynamic construction above.

Hong and Lin later proved convergence guarantees for Adafactor in smooth nonconvex optimization. Their analysis treats the factored state as a nonlinear adaptive step and controls it using regularization, clipping, and proxy step sizes. The inspected paper does not claim that the factored matrix is a uniform coordinatewise multiplicative approximation to the full second moment.

The result here is complementary: generalized-KL optimality and global convergence do not imply coordinatewise fidelity. The obstruction already occurs in the smallest nontrivial matrix dimension.

## Limitations

The impossibility result is worst-case. Practical second-moment matrices may have structure that makes row-column factorization substantially more accurate.

Update clipping can limit the norm-level effect of a badly scaled factored denominator.

A positive second-moment floor changes quantitative distortion bounds.

The theorem concerns coordinatewise second-moment fidelity. It does not compare generalized-KL loss, Frobenius error, or end-to-end training loss.

## References

1. Noam Shazeer and Mitchell Stern, “Adafactor: Adaptive Learning Rates with Sublinear Memory Cost,” arXiv:1804.04235v1, 2018.
2. Yusu Hong and Junhong Lin, “Theoretical Investigation of Adafactor for Non-Convex Smooth Optimization,” Advances in Neural Information Processing Systems 38, 2025.
