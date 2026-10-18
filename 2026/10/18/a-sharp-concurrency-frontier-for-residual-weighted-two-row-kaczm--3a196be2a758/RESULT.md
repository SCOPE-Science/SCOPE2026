# A sharp concurrency frontier for residual-weighted two-row Kaczmarz

## Finding
For a consistent orthonormal two-row linear system, suppose that \(T\ge1\) workers independently select rows using probabilities proportional to the **squared residuals at one common frozen snapshot**, and commit unaveraged, simultaneous relaxed row corrections with a common coefficient \(\beta>0\). The exact worst-direction conditional squared-error factor is
\[
R_T(\beta)=\max\!\left\{(1-\beta T)^2,\;1-\beta T+\frac{\beta^2T(T+1)}4\right\}.
\]
Its unique globally minimax relaxation and the corresponding sharp factor are
\[
(\beta_T^*,R_T^*)=\begin{cases}
\left(\dfrac2{T+1},\dfrac1{T+1}\right),&1\le T\le3,\\[5pt]
\left(\dfrac4{3T-1},\dfrac{(T+1)^2}{(3T-1)^2}\right),&T\ge3.
\end{cases}
\]
The two formulas agree at \(T=3\). Thus \(R_T^*\to1/9\) as concurrency grows. For fixed uniform row sampling, in contrast, the sharp factor is \(1/(T+1)\to0\). For \(T\ge4\) the optimally tuned squared-residual sampler is strictly worse than optimally tuned uniform sampling in this worst-direction criterion. Finally, the adaptive batch contracts squared error uniformly in every direction if and only if \(0<\beta<2/T\).

## Assumptions and scope
Consider \(Ax=b\) with \(A\in\mathbb R^{2\times2}\) orthogonal and a consistent right-hand side. By applying the orthogonal coordinates of \(A\), translate the unique solution to the origin and write the current error \(e=(u,v)\ne0\). Let \(T\) be any positive integer. Conditional on this \(e\), every worker independently chooses equation \(1\) with probability \(z=u^2/(u^2+v^2)\), and equation \(2\) otherwise. Every worker computes its individual row-projection correction from the same \(e\), rather than from updates already made by other workers. All corrections are then **added**, without averaging or sequential residual refresh; a worker choosing equation \(i\) contributes \(-\beta e_i\) in that coordinate. This is a synchronous stale-snapshot model, not a guarantee for arbitrary asynchronous schedules. The optimization is over fixed \(\beta>0\), minimizing the worst conditional *one-batch* squared-error ratio over all nonzero \(e\).

## Proof
Let \(N\sim\operatorname{Binomial}(T,z)\) count the workers selecting the first equation. The post-batch error is exactly
\[
e'=((1-\beta N)u,\;(1-\beta(T-N))v).
\]
With \(\|e\|_2^2=u^2+v^2\), the binomial moment identity \(\mathbb EN=Tz\) and \(\mathbb EN^2=Tz(1-z)+T^2z^2\) yield
\[
\frac{\mathbb E[\|e'\|_2^2\mid e]}{\|e\|_2^2}
=(1-\beta T)^2+z(1-z)\,\beta T[4-\beta(3T-1)]. \tag{1}
\]
Since \(z(1-z)\) fills \([0,1/4]\), expression (1) is affine on that interval. Hence its largest value occurs either at \(z=0\) or \(z=1\) (an axis error), yielding \(A(\beta)=(1-\beta T)^2\), or at \(z=1/2\) (balanced errors), yielding \(B(\beta)=1-\beta T+\beta^2T(T+1)/4\). These are realizable, so \(R_T=\max\{A,B\}\) is exact, not only a bound.

The branches satisfy
\[
A(\beta)-B(\beta)=\beta T\left[\frac{\beta(3T-1)}4-1\right].
\]
Thus \(B\) dominates below \(\beta_c=4/(3T-1)\), while \(A\) dominates above \(\beta_c\). The strictly convex branch \(B\) has its unique minimum at \(\beta_b=2/(T+1)\), and \(A\) is strictly increasing on \([\beta_c,\infty)\), because \(\beta_c>1/T\). If \(T<3\), then \(\beta_b<\beta_c\), so the unique minimax point is \(\beta_b\) with \(R_T^*=1/(T+1)\). If \(T>3\), then \(\beta_c<\beta_b\): \(B\) decreases up to the crossing and \(A\) increases thereafter, so the unique minimax point is \(\beta_c\) with \(R_T^*=((T+1)/(3T-1))^2\). Both choices coincide at \(T=3\). The limit is \(1/9\).

Uniform contraction is equivalent to \(A<1\) and \(B<1\), respectively \(0<\beta<2/T\) and \(0<\beta<4/(T+1)\). The first is the binding restriction for every \(T\ge1\). For comparison, if both rows are sampled independently with constant probability \(1/2\), then each coordinate's count is binomial with parameter \(1/2\), giving the direction-independent factor \(B(\beta)\). Its unique minimum is \(1/(T+1)\) at \(\beta_b\). For \(T\ge4\), the strict inequality \(((T+1)/(3T-1))^2>1/(T+1)\) follows by direct factoring or monotonicity. The conditional bound also gives \(\mathbb E\|e_k\|_2^2\le (R_T^*)^k\|e_0\|_2^2\) for repeated freshly sampled batches; this inequality is not asserted to be attained at every horizon.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. Run `python verify.py` to check exact rational binomial moment expansions, endpoint reductions, predicted minimax parameters against extensive rational step grids, and the uniform-sampling comparator. This finite verification supports but does not replace the preceding proof for all integer \(T\) and real \(\beta>0\).

## Relationship to prior work
Coleman [1] experimentally identifies a sampling-aggressiveness versus concurrency cliff for asynchronous randomized Kaczmarz, motivating a mathematically controlled frozen-snapshot benchmark. Moorman, Tu, Molitor, and Needell [2] analyze parallel Kaczmarz with averaged updates and a fixed row-sampling distribution. Our sampling probabilities are recomputed from the current squared residual, and the unaveraged corrections are accumulated from a shared snapshot; the state-dependent minimax envelope here does not follow from their fixed-distribution result. Steinerberger [3] analyzes residual-weighted sequential row selection; the repeated-choice collisions that control this batch optimum do not arise from a single sequential update. This theorem does not claim to invent parallel averaging, residual-weighted selection, or their standard moment identities.

## Limitations
The result is restricted to orthogonal two-row consistent systems, conditionally independent with-replacement draws, exact arithmetic, and a common frozen snapshot. It is a sharp worst-direction squared-error **one-batch** result, not an optimal runtime or iteration-count theorem for real multicore schedulers. The comparison counts batches rather than total row evaluations; uniform sampling can be cheaper in this worst-case batch sense without dominating adaptive selection at every starting error. Other averaging, duplicate suppression, or concurrency-control designs are outside scope. Equivalent formulas in earlier specialized minibatch stochastic-coordinate literature cannot be categorically ruled out.

## References
[1] Evan Coleman, *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz*, arXiv:2607.08313v1, first public 2026-07-09. https://arxiv.org/abs/2607.08313

[2] J. D. Moorman, T. K. Tu, D. Molitor, and D. Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126v1, 2020. https://arxiv.org/abs/2002.04126

[3] Stefan Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910v3, 2020. https://arxiv.org/abs/2007.02910
