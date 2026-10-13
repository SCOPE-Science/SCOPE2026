# A sharp all-moment clock for Gaussian iterative double sketching

## Finding

The Gaussian nested-sketch construction in Wang, Ouyang, and Xu's iterative double sketching (IDS) has an exact unconditional moment-integrability threshold that advances by two inverse-chi-square powers with each optimization step.

For any integer \(r\ge1\), any finite integer \(T\ge0\), any step size \(\mu>0\), and any integer sequence
\[
r<m_0\le\cdots\le m_{T-1}<N
\]
when \(T\ge1\), run the published Algorithm 1 with its Gaussian construction (7) on
\[
A=e_1\in\mathbb R^{N\times1},\qquad y=e_2\in\mathbb R^N.
\]
The unique least-squares minimizer is \(x_*=0\), and the prediction-error square is exactly \(|x_t-x_*|^2\).

Every iterate \(x_t\), for \(0\le t\le T\), is finite almost surely. Nevertheless, for **every real** \(p>0\), its moment exists if and only if
\[
\boxed{\mathbb E|x_t|^p<\infty\quad\Longleftrightarrow\quad r>p(2t+1).}
\]
In particular,
\[
\boxed{\mathbb E\|A(x_t-x_*)\|_2^2<\infty\quad\Longleftrightarrow\quad r>4t+2.}
\]
Equality is on the divergent side. The boundary holds for *every* finite sequence of strictly oversized but not full gradient sketches and every fixed \(\mu>0\).

An explicit one-step mean-square formula is available. Write
\[
q=\frac{\mu r}{m_0},\qquad k=m_0-r.
\]
For \(r>6\),
\[
\boxed{
\mathbb E x_1^2=
\frac1{r-2}
+\frac{q(q-2)k}{(r-2)(r-4)}
+\frac{q^2k(k+2)}{(r-2)(r-4)(r-6)}.
}
\]
For \(r\le6\), this expectation is infinite. For example, a width of \(r=5\) yields a finite initialization mean-square error but infinite mean-square error after one update; at \(r=10\), the first update has finite mean-square error but the second does not.

The phenomenon is an exact **moment clock**: almost-surely nonsingular Gaussian sketches do not ensure integrability of the subsequent fixed-inverse iterative trajectory. Increasing a finite gradient sketch size changes constants but not the critical Hessian sketch width.

## Assumptions and scope

The object is the mathematical **Gaussian variant of Algorithm 1** of Wang, Ouyang, and Xu, with its nested sketching matrices defined in their equation (7), not their later iteration-efficient structured implementation.

Use \(N\ge2\), \(1\le r<N\), and, if \(T\ge1\), finite sketch sizes \(r<m_0\le\cdots\le m_{T-1}<N\). The last strict inequality keeps each gradient step within the paper's Gaussian sketching case: the source instead substitutes an exact gradient when a sketch size reaches \(N\). All quantities \(r,T,N,m_j,\mu\) are fixed before sampling. No optimization regularizer or safeguards are applied.

Let \(C\in\mathbb R^{N\times N}\) have independent standard normal entries, and let \(C_s\) be its first \(s\) rows. Define
\[
\widetilde S=\frac{C_r}{\sqrt r},\qquad S_j=\frac{C_{m_j}}{\sqrt{m_j}}.
\]
The initialization and update are exactly
\[
x_0=(A^{\mathsf T}\widetilde S^{\mathsf T}\widetilde SA)^{-1}
 A^{\mathsf T}\widetilde S^{\mathsf T}\widetilde Sy,
\]
\[
x_{j+1}=x_j-
\mu(A^{\mathsf T}\widetilde S^{\mathsf T}\widetilde SA)^{-1}
 A^{\mathsf T}S_j^{\mathsf T}S_j(Ax_j-y).
\]
The least-squares objective \(\|Ax-y\|_2^2/2\) is strongly convex with scalar Hessian \(1\), although its minimum objective value is nonzero because \(y\) is orthogonal to the column space of \(A\).

## Proof

Write the first two columns of \(C\) as independent standard Gaussian coordinates \(g_i=C_{i1}\), \(h_i=C_{i2}\), for \(1\le i\le N\). Put
\[
a=\sum_{i=1}^{r}g_i^2,\qquad b=\sum_{i=1}^{r}g_i h_i,
\]
\[
c_j=\sum_{i=r+1}^{m_j}g_i^2,
\qquad
 d_j=\sum_{i=r+1}^{m_j}g_i h_i,
\qquad q_j=\frac{\mu r}{m_j}>0.
\]
Here \(a\) has a chi-square law with \(r\) degrees of freedom, and \(c_j>0\) almost surely because \(m_j>r\). The nested Gaussian construction preserves all correlations among \(c_j,d_j\).

The published recurrence specializes *exactly* to
\[
\boxed{
 x_0=\frac ba,\qquad
 x_{j+1}=
 \left(1-q_j-\frac{q_jc_j}{a}\right)x_j+
 \frac{q_j(b+d_j)}a.
}
\]
Define \(Z=b/\sqrt a\), which is independent of \(a\) and of all Gaussian coordinates with indices above \(r\), and is standard normal. Indeed, conditionally on the first \(r\) values \(g_i\), the variable \(b\) is centered normal with variance \(a\), so the conditional law of \(Z\) is constant; this also proves independence from the first \(r\) values \(g_i\).

Put \(u=1/a\). Collect the contribution involving \(Z\) to write
\[
x_t=a^{-1/2}P_t(u)Z+R_t(u),
\]
where \(R_t\) is a random polynomial in \(u\) whose coefficients depend only on Gaussian coordinates with index above \(r\), and therefore are independent of \(a,Z\). Initially \(P_0=1\), \(R_0=0\); recurrence substitution shows
\[
P_{j+1}(u)=(1-q_j-q_j c_j u)P_j(u)+q_j,
\]
\[
R_{j+1}(u)=(1-q_j-q_jc_j u)R_j(u)+q_j u d_j.
\]
Thus \(P_t\) is a polynomial of degree exactly \(t\) with nonzero leading coefficient
\[
(-1)^t\prod_{j=0}^{t-1}q_jc_j,
\]
while \(R_t\) has degree at most \(t\). The coefficients of both polynomials have finite moments of all positive orders because they are polynomials in finitely many Gaussian variables.

Fix \(p>0\). Since \(a\) is independent of all coefficients and of \(Z\), upper bounds from the displayed decomposition and elementary finite-sum \(p\)-power bounds show
\[
\mathbb E|x_t|^p<\infty
\quad\text{if}\quad
\mathbb E a^{-p(t+1/2)}<\infty.
\]
For the converse, condition on a positive-probability compact event involving only extra-row Gaussian values where \(c_j\) stay bounded away from zero and all polynomial coefficients are bounded, and also condition on \(1\le|Z|\le2\). On this event the first term dominates as \(a\downarrow0\): its nonzero leading coefficient gives \(|x_t|\ge C a^{-t-1/2}\) for sufficiently small \(a\), with a deterministic \(C>0\). The event is independent of \(a\). Consequently the moment diverges whenever \(\mathbb E a^{-p(t+1/2)}\) does.

The chi-square density behaves as a positive constant times \(a^{r/2-1}\) near zero; hence
\[
\mathbb E a^{-s}<\infty\quad\Longleftrightarrow\quad r>2s.
\]
Take \(s=p(t+1/2)\), proving the all-moment equivalence, including strictness at equality. The same recurrence shows all finite iterates are well defined on the full-measure event \(a>0\).

For the explicit one-update formula, set \(c=c_0\), \(d=d_0\), \(q=q_0\). Then
\[
x_1=\frac Z{\sqrt a}\left(1-\frac{qc}a\right)+\frac{qd}a.
\]
Here \(c\) has chi-square distribution with \(k=m_0-r\) degrees of freedom and, conditionally on the extra-row \(g_i\), \(d\) is centered Gaussian with variance \(c\). The random variables \(Z,a,(c,d)\) are independent across the stated blocks. Therefore
\[
\mathbb E x_1^2
=\mathbb E(a^{-1})-2q\mathbb E(c)\mathbb E(a^{-2})
+q^2\mathbb E(c^2)\mathbb E(a^{-3})
+q^2\mathbb E(d^2)\mathbb E(a^{-2}).
\]
Using \(\mathbb E c=k\), \(\mathbb E c^2=k(k+2)\), \(\mathbb E d^2=k\), and
\[
\mathbb E a^{-s}=\prod_{i=1}^{s}\frac1{r-2i}
\quad(s=1,2,3;\ r>6),
\]
produces the displayed formula.

## Verification

The standalone `verify.py` checks the exact nested Gaussian scalar recurrence against the source matrix-gradient expression for many deterministic random inputs and schedules; it separately reconstructs the \(Z\)-polynomial and remainder decomposition and their leading coefficients. It checks the one-step second-moment formula with exact rational arithmetic, chi-square thresholds for representative moments, and the small-\(a\) leading power. These finite computations confirm transcription and algebra only; the all-time and all-moment statements are proved above.

## Relationship to prior work

Wang, Ouyang, and Xu introduced IDS with source-initialized sketched least squares, a fixed sketched Hessian, and nested gradient sketches. Their Theorem 3.1 derives a high-dimensional limiting **conditional prediction-error** formula in a regime with growing sketch width, while their finite-sample results for their iteration-efficient sketch family are embedding and high-probability statements. They do not state this sharp finite-width, unconditional integrability clock.

Lacotte and Pilanci study fixed and refreshed Hessian sketches and derive exact expected rates involving inverse moments for refreshed, independent-sketch IHS; the source initialization and nested gradient-noise correlations treated here are different. Pilanci and Wainwright's original IHS theory supplies high-probability subspace-embedding guarantees. Neither theorem implies the all-positive-moment, all-finite-iteration threshold for source-initialized Gaussian IDS without additionally analyzing its correlated initial projection and repeated fixed random inverse.

The distinction is between near-certain *existence* of the sketched inverse and finiteness of its **unconditional moments**. The clock uses the same Gaussian distribution and initialization printed in the IDS paper, not an altered algorithm.

## Limitations

The exact threshold concerns one deliberately transparent but nontrivial scalar, strongly convex, overdetermined least-squares instance and **Gaussian** nested sketches with finite \(r<m_j<N\). It does not assert that this threshold is necessary on every instance or for other sketch distributions.

The mathematical update is in exact arithmetic with no regularization, clipping, early stopping, or safeguarding of very small sketch singular values. The source's structured iteration-efficient sketching implementation is not covered. High-probability and conditional-error bounds may remain valid even when unconditional moments diverge.

The limiting result is a moment-existence statement, not an almost-sure convergence or a statement about practical floating-point overflow; every finite iterate remains finite almost surely.

## References

1. Rui Wang, Yanyan Ouyang, and Wangli Xu, “Iterative Double Sketching for Faster Least-Squares Optimization,” Proceedings of Machine Learning Research, vol. 162, pp. 22935–22963, ICML, 17–23 July 2022. Source Algorithm 1, Gaussian equation (7), Theorem 3.1, and appendix. https://proceedings.mlr.press/v162/wang22t.html ; https://proceedings.mlr.press/v162/wang22t/wang22t.pdf .
2. Jonathan Lacotte and Mert Pilanci, “Faster Least Squares Optimization,” arXiv:1911.02675v1, 6 November 2019. https://arxiv.org/abs/1911.02675 .
3. Mert Pilanci and Martin J. Wainwright, “Iterative Hessian Sketch: Fast and Accurate Solution Approximation for Constrained Least-Squares,” arXiv:1411.0347v1, 3 November 2014. https://arxiv.org/abs/1411.0347 .
4. Jonathan Lacotte, Sifan Liu, Edgar Dobriban, and Mert Pilanci, “Optimal Iterative Sketching with the Subsampled Randomized Hadamard Transform,” arXiv:2002.00864v1, 3 February 2020. https://arxiv.org/abs/2002.00864 .
