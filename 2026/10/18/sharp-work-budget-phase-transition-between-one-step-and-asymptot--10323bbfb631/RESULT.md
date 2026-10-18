# Sharp work-budget phase transition between one-step and asymptotic randomized two-row Kaczmarz

## Finding

Fix a real consistent two-equation linear system with independent unit row vectors \(a_1,a_2\in\mathbb R^2\). Write their absolute coherence as \(r=|a_1^{\mathsf T}a_2|\in(0,1)\). An independent, identically distributed update draws a mask from \(\varnothing,\{1\},\{2\},\{1,2\}\). The empty mask does nothing; a singleton enforces its equation by an exact orthogonal Kaczmarz projection; the two-row mask enforces both equations exactly. Assign work costs \(0,1,1,w\), respectively, where \(w>2\); prescribe the exact expected work \(0<c\le1\) per update.

Let \(p_0,p_1,p_2,t\) be the four respective mask probabilities, so that \(p_1+p_2+wt=c\). Put \(s=p_1+p_2\) and \(d=p_1-p_2\). The exact worst-initial-error one-step expected squared-error ratio is
\[
R=p_0+\frac{s+\sqrt{r^2s^2+(1-r^2)d^2}}2.
\]
The exact asymptotic worst-initial-error mean-square rate per independent draw is
\[
Q=\limsup_{k\to\infty}\left(\sup_{e_0\ne0}\frac{\mathbb E\|e_k\|_2^2}{\|e_0\|_2^2}\right)^{1/k}
=p_0+\frac{s+\sqrt{r^4s^2+(1-r^4)d^2}}2.
\]
Both objectives have a complete, sharp global phase diagram across all admissible mask distributions. Define
\[
r_{\rm one}=1-\frac2w,\qquad r_{\rm long}=\sqrt{1-\frac2w}.
\]
For the one-step objective, the unique minimizing law when \(r<r_{\rm one}\) selects each singleton with probability \(c/2\) and otherwise skips; when \(r>r_{\rm one}\) it selects both rows with probability \(c/w\) and otherwise skips. Exactly at \(r=r_{\rm one}\), every law with \(p_1=p_2=(c-wt)/2\) and \(0\le t\le c/w\) is optimal. For the asymptotic objective the identical classification holds with \(r_{\rm one}\) replaced by \(r_{\rm long}\). All stated uniqueness assertions concern the law on the four masks, not a random-seed representation of it.

Since \(0<r_{\rm one}<r_{\rm long}<1\), the exact optimizers **strictly disagree** throughout the open coherence interval
\[
1-\frac2w<r<\sqrt{1-\frac2w}.
\]
In that interval the optimal one-step law is batch-or-skip, whereas the optimal asymptotic law is balanced-singletons-or-skip. In the concrete case \(w=4\), \(c=1\), \(r=3/5\), the best one-step rate is \(3/4\) (batch-or-skip) versus \(4/5\) (balanced singletons), while the best asymptotic rate is \(17/25\) (balanced singletons) versus \(3/4\) (batch-or-skip). Thus minimizing the exact one-step expected loss can select a provably inferior long-run sampling law even in a consistent rank-two linear system and at precisely the same expected work.

## Assumptions and scope

All arithmetic and projections are exact. The two row vectors are real, normalized, linearly independent and fixed. The right-hand side is consistent. At each integer time \(k\ge0\), the mask is independently redrawn from one fixed distribution, without dependence on the current error. Empty draws are explicit idle updates introduced only to enforce an equal *expected* work budget across different block sizes; no claim is made about a method requiring nonempty batches, hard per-update work limits, or wall-clock runtime. The cost \(w>2\) represents a coupled two-row solve with overhead; actual implementation costs can differ. Rates are per attempted draw, so no conversion to physical time is assumed. Probability endpoints are included: a mask probability may vanish.

The error \(e_k=x_k-x_\star\) is deterministic initially, and all expectations are over mask draws. The norm is Euclidean. The one-step performance \(R\) maximizes over nonzero initial errors; the long-run \(Q\) takes a supremum over nonzero initial errors separately for each \(k\) before the \(k\)-th root and limsup. These are two genuinely different statistical objectives.

## Proof

**1. Projection representation and feasible polytope.** Let \(u_i\) be a unit vector orthogonal to \(a_i\), and set \(P_i=u_i u_i^{\mathsf T}\). The singleton error maps are \(P_1,P_2\), the empty error map is \(I_2\), and the two-row error map is zero. In the plane \(|u_1^{\mathsf T}u_2|=r\). Expected work imposes
\[
p_0=1-c+(w-1)t,\quad s=c-wt,\quad0\le t\le c/w,\quad |d|\le s,
\]
with \(p_1=(s+d)/2\) and \(p_2=(s-d)/2\). Since \(0<c\le1\) and \(w>2\), these conditions are sufficient for a valid probability distribution.

**2. Exact one-step worst-case ratio.** For any deterministic initial error \(e\),
\[
\mathbb E\|e_1\|_2^2=e^{\mathsf T}(p_0I_2+p_1P_1+p_2P_2)e.
\]
The two nonnegative eigenvalues of \(p_1P_1+p_2P_2\) have sum \(s\) and squared difference \(d^2+4p_1p_2r^2=r^2s^2+(1-r^2)d^2\). Its top eigenvalue gives the displayed formula for \(R\), including every boundary case.

**3. Exact long-run mean-square rate.** On real symmetric \(2\times2\) matrices define the covariance propagation operator
\[
\mathcal M(H)=p_0H+p_1P_1HP_1+p_2P_2HP_2.
\]
For rank-one orthogonal projectors, \(P_iHP_i=\operatorname{tr}(P_iH)P_i\). The two-dimensional subspace spanned by \(P_1,P_2\) is invariant, and \(\mathcal M\) has coefficient matrix
\[
T=\begin{pmatrix}p_0+p_1&r^2p_1\\r^2p_2&p_0+p_2\end{pmatrix}.
\]
On its one-dimensional Frobenius-orthogonal complement \(\mathcal M\) acts as multiplication by \(p_0\). The larger eigenvalue of \(T\) is
\[
\lambda_+=p_0+\frac{s+\sqrt{r^4s^2+(1-r^4)d^2}}2\ge p_0.
\]
Because \(\mathcal M\) preserves the positive-semidefinite cone and is Frobenius-self-adjoint, this eigenvalue governs the exponential growth/decay of \(\operatorname{tr}(\mathcal M^k(I_2))\): if \(s>0\), a top eigenmatrix is a nonzero nonnegative linear combination of \(P_1,P_2\) and has strictly positive Frobenius pairing with \(I_2\). This remains true if one singleton probability is zero, by the explicit triangular form of \(T\). If \(s=0\), \(\mathcal M=p_0\operatorname{Id}\) and the statement is immediate. For every \(k\),
\[
\sup_{e\ne0}\frac{\mathbb E\|e_k\|_2^2}{\|e\|_2^2}
=\lambda_{\max}(\mathcal M^k(I_2)).
\]
Since \(\mathcal M^k(I_2)\succeq0\) and its largest eigenvalue lies between half its trace and its trace, taking \(k\)-th roots proves \(Q=\lambda_+\) in all cases. Thus no finite simulation or unproved interchange of limits is used.

**4. Optimization of all distributions.** For fixed \(t\) (hence fixed \(s\)), the factors \(1-r^2\) and \(1-r^4\) are strictly positive. Both \(R\) and \(Q\) are uniquely minimized at \(d=0\) whenever \(s>0\). If \(s=0\), then \(d=0\) necessarily. Substituting \(p_1=p_2=(c-wt)/2\) gives the two affine functions
\[
R_{\rm bal}(t)=1-\frac{c(1-r)}2+t\left(\frac{w(1-r)}2-1\right),
\]
\[
Q_{\rm bal}(t)=1-\frac{c(1-r^2)}2+t\left(\frac{w(1-r^2)}2-1\right).
\]
The signs of their slopes change exactly at \(r_{\rm one}=1-2/w\) and \(r_{\rm long}=\sqrt{1-2/w}\), respectively. Minimizing each affine function on the closed interval \([0,c/w]\) yields the full phase diagram and uniqueness statements, including the equality regimes. The inequality \(0<1-2/w<\sqrt{1-2/w}<1\) proves that the strict-disagreement interval is nonempty for every \(w>2\).

**5. Rational witness.** At \(w=4,c=1,r=3/5\), choose \(a_1=(1,0)^{\mathsf T}\), \(a_2=(3/5,4/5)^{\mathsf T}\), and a consistent homogeneous right-hand side. The all-singleton law has \(p_1=p_2=1/2\) and \(p_0=t=0\); formulas give \(R=4/5,Q=17/25\). The batch-or-skip law has \(t=1/4,p_0=3/4\) and \(p_1=p_2=0\); its one-step and long-run rates both equal \(3/4\). Each has expected cost exactly one. Both inequalities are strict rational comparisons. More strongly, these two globally optimal (for their respective objectives) laws reverse their worst-initial-error ordering after just two draws. For the balanced singleton law with \(c=1\), \(\mathcal M(I_2)=(P_1+P_2)/2\) and \(\mathcal M((P_1+P_2)/2)=((1+r^2)/2)(P_1+P_2)/2\). Thus for every integer \(k\ge1\), its exact worst-initial-error ratio is \(\frac45(\frac{17}{25})^{k-1}\), whereas the batch-or-skip ratio is \((\frac34)^k\). The singleton ratio is larger for \(k=1\), but smaller for **every** \(k\ge2\), beginning with \(68/125<9/16\).

## Verification

A self-contained standard-library program `verify.py` constructs the exact rational two-row witness, checks the row projector and covariance identities, reproduces the strict phase reversal, verifies the affine optimizers at threshold cases and tests a grid of admissible distributions against the exact one-step and long-run spectral formulas. Run `python3 verify.py` in the same directory. Its finite grid and rational checks corroborate the proof; they do not certify universal quantifiers or literature originality. The analytical argument above is the proof.

## Relationship to prior work

Xie and Yang, *Randomized batch-sampling Kaczmarz methods for solving linear systems*, arXiv:2511.09872 (first publicly posted 2025-11-13), introduce learnable joint batch-sampling distributions and, in Remark 5.2, frame their optimization as difficult. Their Theorem 5.1 concerns bounds rather than the exact cost-constrained two-row distribution classified here. The paper's Example B.3 uses variable-sized **nonempty** batches; the present deliberately extended cost model also permits an explicit no-op, which must not be attributed to their scheme.

The same authors' *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685 (posted 2026-10-03), treats learned batch probabilities and the dual coordinate-descent viewpoint. Only the abstract and metadata were available for comparison; no claim is made that its inaccessible full text lacks a related result. Classical analyses of randomized projections already give ingredients of the two-state recurrence; neither projection identities nor the basic single-coordinate mean-square formula is claimed as new. Mutný, Dereziński and Krause (2020) optimize determinantal block sizes and numerical effort for a different sampler. The proposed contribution here is solely the **joint complete work-budget classification and the nonempty interval where exact one-step and long-run optimal mask laws contradict each other**.

## Limitations

The full two-row batch is an exact solve because the system has two independent equations in two variables. The model therefore does not imply that periodic exact small-system solves are inferior in high-dimensional implementations. The abstract work cost \(w>2\) and idle draws are modeling choices, not hardware benchmarks, and nonempty-only sampling rules are outside the theorem's feasible set. Distribution changes during iterations, finite precision, inconsistent systems, more than two independent rows, objective-function decay rather than squared solution error, and wall-clock optimality are not addressed. In particular, the expected work constraint does not impose a per-draw cost ceiling. The full 2026 manuscript named above was unavailable for a decisive text-level originality comparison; an equivalent older formulation remains possible. No independent audit is asserted.

## References

1. D.-Y. Xie and X. Yang, *Randomized batch-sampling Kaczmarz methods for solving linear systems*, arXiv:2511.09872 (v1 publicly submitted 2025-11-13), https://arxiv.org/abs/2511.09872 . Full accessible HTML version inspected, including Sections 3, 5, and Appendix B.
2. D.-Y. Xie and X. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685 (v1 publicly submitted 2026-10-03), https://arxiv.org/abs/2610.04685 . Abstract available; full text not compared.
3. M. Mutný, M. Dereziński and A. Krause, *Convergence Analysis of Block Coordinate Algorithms with Determinantal Sampling*, AISTATS 2020, https://proceedings.mlr.press/v108/mutny20a.html .
4. T. Strohmer and R. Vershynin, *A Randomized Kaczmarz Algorithm with Exponential Convergence*, Journal of Fourier Analysis and Applications 15 (2009), https://arxiv.org/abs/math/0702226 . Background rate bounds.
