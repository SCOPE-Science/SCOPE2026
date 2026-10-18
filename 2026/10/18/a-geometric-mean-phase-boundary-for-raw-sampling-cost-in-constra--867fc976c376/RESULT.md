# A geometric-mean phase boundary for raw sampling cost in constrained Kaczmarz

## Finding

For the row-constrained stochastic projection method with independently redrawn, squared-row-norm probes and rejection of zero-residual probes, minimizing the usual projected Frobenius residual can be arbitrarily worse for **raw sampling work** than a different legal constraint row, even when the relative sacrifice in Frobenius residual is arbitrarily small. On a three-row diagonal system, the optimal row changes at an exact geometric-mean boundary.

**Theorem.** Let \(s_1>s_2>s_3>0\), let \(A=\operatorname{diag}(s_1,s_2,s_3)\), and set \(b=A\mathbf1\). Choose one pinned equation \(i\in\{1,2,3\}\) and initialize \(x^0=A_{\{i\}}^{\dagger}b_{\{i\}}=e_i\). For every raw sample draw one of the two unpinned rows independently with probabilities proportional to its squared Euclidean norm. Reject a draw when that row currently has zero residual, and otherwise use the exact subspace-constrained Kaczmarz update, corresponding to \(\zeta=1\) in Algorithm 1 of [1]. Let \(T_i\) count **all raw draws, including rejected draws**, until the exact solution is reached.

For the two unpinned rows \(j,k\), writing \(w=s_j^2\) and \(z=s_k^2\), one has, for every integer \(t\ge1\),
\[
\Pr(T_i>t)=\left(\frac{w}{w+z}\right)^t+\left(\frac{z}{w+z}\right)^t,
\qquad
\mathbb ET_i=1+\frac wz+\frac zw.
\]
Exactly two **accepted** updates suffice in all three configurations, almost surely. The squared projected Frobenius residual is
\[
F_i=\|A-AA_{\{i\}}^{\dagger}A_{\{i\}}\|_F^2=\sum_{j\ne i}s_j^2,
\]
uniquely minimized by \(i=1\). In contrast, the unique minimum of \(\mathbb ET_i\) is attained by \(i=3\) when \(s_2^2>s_1s_3\), by \(i=1\) when \(s_2^2<s_1s_3\), and by both endpoint rows at equality. Pinning \(i=2\) is strictly suboptimal for every strictly ordered triple. The same boundary optimizes the nominal matrix-based first-step contraction proxy \(q_i=1-\min\{w,z\}/(w+z)\), which is **not** claimed to be the realized contraction factor of the subsequently rejection-conditioned accepted iterations.

For \(A=\operatorname{diag}(2,1,\varepsilon)\), \(0<\varepsilon<1/2\), the Frobenius-optimal pinning \(i=1\) has \(\mathbb ET_1=1+\varepsilon^{-2}+\varepsilon^2\), while pinning the smallest row \(i=3\) gives \(\mathbb ET_3=21/4\). The ratio diverges as \(\varepsilon\downarrow0\).

**Arbitrarily near-Frobenius-optimal comparison.** For every \(\delta>0\), there is an integer \(n\ge3\) and a family \(A_{n,\varepsilon}=\operatorname{diag}(2,1,\ldots,1,\varepsilon)\), with \(0<\varepsilon<1\), such that pinning the largest row uniquely minimizes \(F_i\), while pinning the smallest row satisfies
\[
\frac{F_{n}}{F_1}=\frac{n+2}{n-2+\varepsilon^2}<1+\delta
\]
for all sufficiently large fixed \(n\), yet the ratio of the expected raw draws under pinning the largest row to that under pinning the smallest row tends to infinity as \(\varepsilon\downarrow0\). Both pinning choices require exactly \(n-1\) accepted updates. No claim is made that pinning the smallest row is optimal among *all* choices for general \(n\).

## Assumptions and scope

All systems are square diagonal real nonsingular systems in exact arithmetic. The right-hand side is chosen so every unpinned coordinate initially has nonzero error. Sampling is independent with **fixed, pre-rejection** row probabilities proportional to squared row norms of the reduced projected matrix. Zero-residual proposals are repeatedly rejected but remain counted as raw draws. Every accepted step uses relaxation parameter \(\zeta=1\), and the process stops immediately on solving every row. The comparison excludes algebraic solve, factorization, residual-scanning, and row-sampling setup costs. The result is about the number of random probes, not wall-clock time or the accepted-iteration count.

## Proof

Fix pinned row \(i\). The orthogonal projector onto its nullspace is the diagonal matrix \(P=I-e_ie_i^{\mathsf T}\). For any unpinned row \(j\), the projected row is \(s_je_j^{\mathsf T}\). The exact Kaczmarz correction sets coordinate \(j\) from zero to one on its first accepted selection and cannot subsequently change it. Thus every row outside the pinned set has to be drawn at least once. Under rejection, each first-ever appearance is accepted and subsequent appearances are rejected. This proves that the number of accepted steps is exactly the number of unpinned rows and that the raw draw count is the coupon-collection stopping time for the fixed sampling probabilities.

In dimension three, let \(p=w/(w+z)\). After \(t\ge1\) raw draws, failure occurs exactly when all \(t\) draws were of the first row or all were of the second. These disjoint events have probabilities \(p^t\) and \((1-p)^t\), proving the stated tail. Summing the tail from \(t=0\) yields \(\mathbb ET_i=1+w/z+z/w\). In this formula, the ratio of the larger to the smaller unpinned singular value completely determines the expectation: \(1+r^2+r^{-2}\) strictly increases for \(r>1\). Pinning the middle singular row leaves the extreme pair and therefore always gives the largest expectation. The remaining two ratios are \(r_1=s_2/s_3\) and \(r_3=s_1/s_2\), giving the stated geometric-mean boundary. The proxy \(q_i=r_i^2/(1+r_i^2)\) is strictly increasing in the same imbalance ratio. The Frobenius residual formula is immediate because pinning one diagonal row deletes precisely its coordinate contribution, and therefore selects \(i=1\).

For the higher-dimensional family, pinning the largest row leaves \(n-2\) rows of squared norm \(1\) and one row of squared norm \(\varepsilon^2\), with total raw sampling weight \(W_1=n-2+\varepsilon^2\). The waiting time to draw the smallest row alone is geometric with success probability \(\varepsilon^2/W_1\), so
\[
\mathbb ET_1\ge\frac{n-2+\varepsilon^2}{\varepsilon^2}.
\]
Pinning the smallest row instead leaves one row of squared norm \(4\) and \(n-2\) rows of squared norm \(1\), for a total \(W_n=n+2\). Until collection finishes, at least one unfinished row has weight \(\ge1\); hence the conditional chance that the next raw draw is an undiscovered row is at least \(1/(n+2)\). By summing the expected waiting times between discoveries,
\[
\mathbb ET_n\le(n-1)(n+2).
\]
Their ratio is at least \((n-2+\varepsilon^2)/[\varepsilon^2(n-1)(n+2)]\), which diverges as \(\varepsilon\downarrow0\) for every fixed \(n\). The Frobenius ratio is \((n+2)/(n-2+\varepsilon^2)\), uniformly at most \(1+4/(n-2)\). Choosing \(n>2+4/\delta\) proves the advertised arbitrarily small relative Frobenius sacrifice.

## Verification

The accompanying standalone `checker.py` uses Python standard-library exact rational arithmetic. It independently solves the missing-coupon dynamic-programming equations, enumerates short raw-draw histories, verifies update identities and the selection-boundary inequalities on a broad finite grid, and checks the higher-dimensional inequalities. Running `python3 checker.py` prints `PASS: exact-arithmetic checks = 2475`. Finite checks are supplementary: the statements for all positive parameters and arbitrary \(n\) follow from the preceding proof.

## Relationship to prior work

Sun, Qi, Han, and Xie [1] define the stochastic subspace-constrained algorithm, explicitly redraw until the proposed row residual is nonzero (Algorithm 1, step 2), give squared projected row-norm sampling (Remark 3.1), and adopt a projected Frobenius residual as a tractable constraint-selection surrogate (Section 3.2). Their bound concerns *accepted iteration count*. The present theorem compares the **pre-rejection raw-proposal count** and derives an explicit selection boundary plus a near-surrogate-optimal unbounded-work family; it does not claim novelty for their algorithm, Frobenius criterion, or matrix convergence bound.

Lok and Rebrova [2] established the subspace-constrained Kaczmarz framework and related row-selection ideas, but their basic Algorithm 1 does not repeatedly reject previously satisfied row proposals. Nutini and coauthors [3] established that exploiting orthogonality to avoid unproductive Kaczmarz selections can accelerate sampling; that qualitative principle is not claimed as new. Classical weighted coupon-collection identities, used as a proof ingredient, are also not claimed as new. The contribution assessed here is the exact interaction between **the specific 2026 Frobenius pinning surrogate and its rejected-proposal work measure** on a minimal diagonal family, with a quantitative near-surrogate-optimal separation.

## Limitations

Only diagonal, nonzero-entry, consistent systems and independent fixed-distribution row probes are covered. A practitioner who conditions or renormalizes sampling directly to the as-yet-unfinished rows would eliminate the wasted raw proposals, but that implementation requires an additional adaptive selection mechanism. The result does not contradict the original source's convergence rate stated in accepted iterations. No general singular-matrix, nonorthogonal, approximate arithmetic, adaptive-sampler, total execution-time, or complexity lower bound is asserted. Earlier equivalent derivations of this specialized selection tradeoff may exist.

## References

[1] Y. Sun, H.-D. Qi, D. Han, J. Xie. *On subspace-constrained preconditioning for randomized iterative methods*. arXiv:2605.29304v1 (2026-05-28), Algorithm 1, Remark 3.1, Sections 3.1–3.2. https://arxiv.org/html/2605.29304

[2] J. Lok, E. Rebrova. *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*. arXiv:2309.04889, Algorithm 1, Sections 3.1 and 3.3.2. https://arxiv.org/pdf/2309.04889

[3] J. Nutini et al. *Convergence Rates for Greedy Kaczmarz Algorithms, and Randomized Kaczmarz Rules Using the Orthogonality Graph*. UAI/PMLR (2016), orthogonality-based sampling discussion. https://proceedings.mlr.press/r14/nutini16a.html
