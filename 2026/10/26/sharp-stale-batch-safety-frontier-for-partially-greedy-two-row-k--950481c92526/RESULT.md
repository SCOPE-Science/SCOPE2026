# Sharp stale-batch safety frontier for partially greedy two-row Kaczmarz

## Finding

For a consistent, nonsingular, two-equation real linear system with unit row normals of absolute inner product \(c\in[0,1)\), consider \(K\geq1\) independent row decisions taken from **one shared residual snapshot**. Each chosen row contributes its entire relaxed Kaczmarz correction, with no division by \(K\); all contributions are added after the snapshot. Each decision follows a mixture of uniform and maximum-residual selection, with greedy probability \(\theta\in[0,1]\). If the per-worker relaxation is \(\beta\), then the expected squared Euclidean error decreases strictly from **every** nonzero error if and only if
\[
0<\beta<\beta_{\mathrm{safe}}(K,\theta,c)
:=\frac{4}{K+1+(K-1)\sqrt{\theta^2+(1-\theta^2)c^2}}.
\]
The endpoint is sharp: at equality a nonzero error has exactly zero expected one-batch decrease; above it a nonzero error has **positive expected one-batch increase**. Inside the interval, every trajectory using fresh independent draws at successive batches converges to the solution geometrically in mean square.

In particular, \(K=2\), \(\beta=1\) is geometrically mean-square convergent for **every** \(\theta<1\), yet at \(\theta=1\) each batch with a uniquely maximal residual is an exact orthogonal reflection and preserves its squared error. For Lebesgue-almost every nonzero initial error, the fully greedy two-worker method stays on its initial error sphere forever. Thus an arbitrarily small uniform-exploration component restores strict convergence in this model. This is a sharp statement about a shared-snapshot batch, not a stability theorem for arbitrary lock-free asynchronous schedules.

## Assumptions and scope

Let \(u_1,u_2\in\mathbb R^2\) be linearly independent unit vectors and let \(c=|u_1^{\mathsf T}u_2|\). The consistent system \(u_i^{\mathsf T}x=b_i\) has a unique solution \(x_*\). At a batch boundary write \(e=x-x_*\) and \(r_i=u_i^{\mathsf T}e\). If \(|r_1|\ne|r_2|\), each of \(K\) workers independently selects the larger-residual row with probability \((1+\theta)/2\), and the smaller-residual row with probability \((1-\theta)/2\). Equivalently this is a convex mixture: probability \(\theta\) of selecting the maximal row plus probability \(1-\theta\) of selecting a uniformly random row. At a tie, selection is uniform. All selected indices are conditionally independent with replacement.

Each worker computes the correction using the **same** pre-batch error \(e\), and the batch update is
\[
e^+=e-\beta\sum_{j=1}^{K}r_{I_j}u_{I_j}.
\]
The shared-snapshot assumption is essential: a live reread or a sequentially refreshed residual defines a different method. Here \(\theta\) is the greediness mixture parameter and \(\beta\) is the per-worker projection relaxation. The linear system can be translated to a homogeneous system without affecting the argument. Row signs can be flipped to make \(u_1^{\mathsf T}u_2=c\geq0\), with the corresponding residual signs flipped.

## Proof

**Exact conditional second moment.** Fix a nonzero error and order the rows so that \(|r_1|\geq|r_2|\). Put \(p=(1+\theta)/2\), \(q=(1-\theta)/2\), except that ties use \(p=q=1/2\). Define
\[
A=p r_1^2+q r_2^2,
\qquad
B=\|p r_1u_1+q r_2u_2\|_2^2.
\]
Writing \(g_j=r_{I_j}u_{I_j}\), the draws have \(\mathbb E\langle e,g_j\rangle=A\), \(\mathbb E\|g_j\|_2^2=A\), and \(\mathbb Eg_j=p r_1u_1+q r_2u_2\). Independence therefore yields the **identity**
\[
\mathbb E[\|e^+\|_2^2\mid e]-\|e\|_2^2
=-K\beta\{2A-\beta[A+(K-1)B]\}.\tag{1}
\]
Since the rows are linearly independent, \(A>0\) whenever \(e\ne0\).

**Sharp extremum of the interference ratio.** For \(p,q>0\), set \(z=(\sqrt p\,r_1,\sqrt q\,r_2)^{\mathsf T}\). Then
\[
\frac BA
=\frac{z^{\mathsf T}H z}{z^{\mathsf T}z},
\qquad
H=\begin{pmatrix}
p&c\sqrt{pq}\\c\sqrt{pq}&q
\end{pmatrix}.
\]
Thus
\[
\frac BA\leq R(\theta,c)
:=\lambda_{\max}(H)
=\frac{1+\sqrt{\theta^2+(1-\theta^2)c^2}}2.\tag{2}
\]
This Rayleigh bound is **attainable within the greedy-ordering constraint**. Indeed, for \(0<c<1\) and \(0\leq\theta<1\), choose \(r_1>0\) and
\[
\frac{r_2}{r_1}
=\frac{\sqrt{\theta^2+(1-\theta^2)c^2}-\theta}{c(1-\theta)}.\tag{3}
\]
The ratio belongs to \((0,1]\): squaring nonnegative sides reduces the upper bound to \(2\theta(1-\theta)c(1-c)\geq0\). It is the positive top-eigenvector ratio for \(H\). For \(\theta=0\), the ratio is one and uniform tie-breaking agrees with the stipulated probabilities. For \(c=0\), the extremum \(R=(1+\theta)/2\) is attained by \(r_2=0\); for \(\theta=1\), it is attained by any uniquely dominant first-row residual, as then \(B=A\). Each specified residual pair is realizable by a unique \(e\) because the two rows are independent. Consequently, (2) is an **exact maximum**, not merely an upper estimate.

**Necessary and sufficient frontier.** Substituting the attained maximum \(R\) into (1), strict negativity from every nonzero error is equivalent to
\[
0<\beta<\frac{2}{1+(K-1)R}
=\frac{4}{K+1+(K-1)\sqrt{\theta^2+(1-\theta^2)c^2}}.
\]
At the endpoint the maximizing residual gives equality, and for every larger positive relaxation the same residual gives strict expansion. At zero relaxation there is no decrease; negative relaxation strictly increases the error by (1). These observations establish the complete strict-contraction classification.

**Uniform geometric mean-square convergence in the safe interval.** As the larger residual has sampling weight at least \(1/2\),
\[
A\geq\tfrac12(r_1^2+r_2^2)
\geq\tfrac{1-c}{2}\|e\|_2^2,
\]
where the second bound is the smallest-eigenvalue bound for \(u_1u_1^{\mathsf T}+u_2u_2^{\mathsf T}\). For \(0<\beta<\beta_{\mathrm{safe}}\), (1) and (2) consequently give
\[
\mathbb E[\|e^+\|_2^2\mid e]
\leq (1-\delta)\|e\|_2^2,
\quad
\delta=\frac{K\beta(1-c)}{2}
\bigl[2-\beta(1+(K-1)R)\bigr]>0.
\]
The exact expectation identity ensures \(0<\delta\leq1\). Iterating conditional expectations across fresh batches yields \(\mathbb E\|e_n\|_2^2\leq(1-\delta)^n\|e_0\|_2^2\).

**Pure-greedy reflection obstruction.** For \(K=2,\theta=1,\beta=1\), whenever one residual is strictly largest, both workers select the same row \(i\), giving
\[
e^+=(I-2u_iu_i^{\mathsf T})e.
\]
The matrix is an orthogonal Householder reflection. The tie set is the union of the two lines \((u_1-u_2)^{\mathsf T}e=0\) and \((u_1+u_2)^{\mathsf T}e=0\). Every composition of finitely many such reflections has an invertible orthogonal matrix, so the set of initial errors hitting a tie at some finite batch is contained in a countable union of reflected lines and has Lebesgue measure zero. From all other nonzero starts, every batch preserves \(\|e_n\|_2\), precluding convergence. On the other hand, for \(K=2\) and \(\theta<1\), the square root in the safety frontier is strictly below one because \(c<1\). Hence \(\beta_{\mathrm{safe}}>1\), proving geometric mean-square convergence at \(\beta=1\).

## Verification

Run \(\texttt{python3 CHECK.py}\) with Python 3 and no third-party dependencies. Its exact-rational enumeration reconstructs all conditional draw outcomes on normalized rational two-row systems, and verifies identity (1) over 2,000 parameter choices. Its additional 5,000 seeded numeric checks cover the maximizing residual ratio, both sides of the sharp frontier, and Householder norm preservation. The implementation is included with this result. The theorem's infinite quantifiers are proved by the displayed identities and eigenvalue argument, not by the finite checks.

For an explicit sharp-boundary instance choose \(K=2\), \(\theta=3/4\), \(c=3/5\). Then
\[
R=\frac12+\frac{3\sqrt2}{10},
\quad
\beta_{\mathrm{safe}}=\frac{100-20\sqrt2}{69},
\quad
r_2/r_1=4\sqrt2-5.
\]
The residual ratio attains the interference maximum. At the endpoint the conditional change in squared error is exactly zero; at \(\beta=11/10\) it is strictly positive (take \(r_1=1\)).

## Relationship to prior work

Coleman (2026), arXiv:2607.08313, empirically studies power-weighted and threshold-greedy asynchronous Kaczmarz with stale residual information, including a dependence of stability on aggressiveness and concurrency. That study does not state the exact two-row, common-snapshot, mixed-greed interference maximum or the reflection obstruction. Moorman, Tu, Molitor, and Needell (2020), arXiv:2002.04126, study sums or averages of independent row corrections computed in parallel, mainly with fixed sampling distributions and coupled probability/weight choices. Their general stochastic-moment viewpoint provides relevant background, but their results do not assert the sharp adaptive-mixing frontier. Gower, Molitor, Moorman, and Needell (2019), arXiv:1909.03604, establish single-sketch adaptive selection rules; here concurrent workers each reuse the same residual and their corrections are added, not sequentially refreshed.

The 2024 survey of Ferreira, Acebrón, and Monteiro (DOI:10.1007/s11075-024-01945-2) distinguishes averaged and parallel Kaczmarz variants. Published related findings on cyclic two-row Kaczmarz overrelaxation, two-coordinate stale Gauss–Seidel, and max-distance residual spikes concern different updates, objectives, or error metrics. The result above concerns only the explicitly defined shared-snapshot batched adaptive mechanism.

## Limitations

The theorem is for exactly two independent normalized equations in the plane, consistent data, exact arithmetic, independent sampling with replacement, a uniform-plus-greedy mixture, and simultaneous additive commits based on one residual snapshot. It does not predict a hardware thread-count cliff for general asynchronously interleaved reads or other adaptive exponent laws. An expected one-step expansion witness above the frontier does not itself prove long-run divergence. The rate bound is sufficient and is not asserted to be the sharp asymptotic rate. The originality comparison is best-knowledge rather than independent bibliographic certification.

## References

1. E. Coleman, *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz*, arXiv:2607.08313, first released 2026-07-09. https://arxiv.org/abs/2607.08313
2. J. D. Moorman, T. K. Tu, D. Molitor, D. Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126, first released 2020-02-10. https://arxiv.org/abs/2002.04126
3. R. M. Gower, D. Molitor, J. D. Moorman, D. Needell, *Adaptive Sketch-and-Project Methods for Solving Linear Systems*, arXiv:1909.03604, first released 2019-09-09. https://arxiv.org/abs/1909.03604
4. I. A. Ferreira, J. A. Acebrón, J. Monteiro, *Survey of a class of iterative row-action methods: The Kaczmarz method*, Numerical Algorithms, DOI:10.1007/s11075-024-01945-2 (2024). https://link.springer.com/article/10.1007/s11075-024-01945-2
