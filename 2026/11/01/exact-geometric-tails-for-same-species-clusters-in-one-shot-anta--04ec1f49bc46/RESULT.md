# Exact geometric tails for same-species clusters in one-shot antagonistic adsorption

## Finding

Consider the one-attempt, two-species antagonistic adsorption process on the integer line. Each site independently receives one attempted species, \(A\) with probability \(p\in(0,1)\) and \(B\) with probability \(q=1-p\), at an independent uniform arrival time in \([0,1]\). An attempt succeeds unless an already occupied neighboring site bears the opposite species. Write \(\eta_i(t)\in\{A,B,\varnothing\}\) for the state at time \(t\in(0,1]\).

Define
\[
\gamma=\sqrt{pq},\qquad H_p(t)=1-\cosh(\gamma t)+\sqrt{\frac p q}\sinh(\gamma t).
\]
For every integer \(k\ge2\), the probability of \(k\) specified consecutive sites all being occupied by \(A\) is exactly
\[
Q_k(t):=\Pr\bigl(\eta_0(t)=\cdots=\eta_{k-1}(t)=A\bigr)
=H_p(t)^2(pt)^{k-2}.
\]
The intensity per lattice site of **maximal** \(A\)-clusters of length exactly \(k\ge2\) is
\[
\boxed{\lambda_k(t)=H_p(t)^2(1-pt)^2(pt)^{k-2}.}
\]
In particular, conditional on choosing a typical \(A\)-cluster of length at least two by cluster count, its length \(L\) has the *exact*, time-dependent geometric law
\[
\Pr(L=k\mid L\ge2)=(1-pt)(pt)^{k-2},\qquad k=2,3,\ldots.
\]
The distribution of all cluster sizes, including singleton clusters, is specified by
\[
\lambda_1(t)=\rho_A(t)-(2-pt)H_p(t)^2,
\quad
\rho_A(t)=p\int_0^t\left[\cosh(\gamma u)-\sqrt{\frac q p}\sinh(\gamma u)\right]^2du.
\]
The total intensity of \(A\)-clusters of size at least two is \((1-pt)H_p(t)^2\), and their occupied-site density is \((2-pt)H_p(t)^2\). All identities hold for every \(0<p<1\) and \(0<t\le1\); there is no asymptotic-size restriction.

## Assumptions and scope

The substrate is \(\mathbb Z\) with nearest-neighbor edges. The single, irrevocable attempted color at each site and its continuous arrival time are independent across sites. Occupied sites never change color, and a rejected attempt is not retried. The infinite-volume process is almost surely well defined: a dependency path of length \(m\) starting from a fixed site requires \(m+1\) strictly decreasing independent arrival times, with probability at most \(1/(m+1)!\) for any specified path. There are at most \(2^m\) such paths, and the resulting probabilities are summable. The process is an equivariant factor of i.i.d. marks and therefore is stationary and ergodic under spatial shifts.

A maximal \(A\)-cluster of length \(k\) begins at site \(0\) when sites \(0,\ldots,k-1\) are all \(A\) and neither site \(-1\) nor site \(k\) is \(A\). Its probability \(\lambda_k(t)\) is, by the ergodic theorem, the almost-sure limiting number of length-\(k\) clusters divided by interval length. For \(p<1\), an infinite contiguous \(A\)-cluster has probability zero, since it would require infinitely many consecutive \(A\) proposals. The conditional distribution above uses cluster-count (Palm) weighting, not size-biased selection of a typical occupied site.

The endpoints \(p=0,1\) are omitted from the conditional law when the conditioning event has zero probability; the formulas for finite all-\(A\) cylinders extend by continuity when meaningful.

## Proof

**1. A one-sided boundary calculation.** Run the same process on a half-line with its endpoint initially unoccupied. Let \(a(t)\) and \(b(t)\) be the respective probabilities that this endpoint is occupied by \(A\) or \(B\) at time \(t\). Conditional on an \(A\)-proposal at endpoint time \(u\), the sole neighbor has evolved, before time \(u\), independently of that endpoint. Its state has the same law as the endpoint of a half-line shifted one site. Consequently, for almost every \(t\),
\[
a'(t)=p[1-b(t)],\qquad b'(t)=q[1-a(t)],\qquad a(0)=b(0)=0.
\]
Solving this two-dimensional linear initial-value problem yields
\[
a(t)=1-\cosh(\gamma t)+\frac{p}{\gamma}\sinh(\gamma t)=H_p(t),
\]
\[
1-b(t)=\cosh(\gamma t)-\frac q\gamma\sinh(\gamma t).
\]
The right-hand sides are nonnegative because they represent event probabilities; the solution also directly satisfies the ODE and initial conditions.

**2. Factorization of contiguous cylinders.** Suppose the attempted species at each of \(0,\ldots,k-1\), \(k\ge2\), is \(A\), and every one of their attempt times lies in \([0,t]\). This is necessary for the whole block to be occupied by \(A\) at time \(t\). Every interior site \(1,\ldots,k-2\) is then accepted automatically: neither neighbor could ever carry \(B\), whether that neighbor's own \(A\)-attempt succeeds or fails.

An endpoint's \(A\)-attempt can fail only because the adjacent site **outside** the block was previously occupied by \(B\). Until the endpoint attempts deposition, it remains empty, so the exterior evolves as a one-sided half-line with a vacant boundary. For a boundary attempt at time \(u\), the probability of no blocking exterior \(B\) is \(1-b(u)\). The left and right exteriors, and all interior marked proposals, are independent. Integrating independently over the two endpoint proposal times gives \(a(t)^2\); the \(k-2\) interior proposals each contribute \(pt\). Thus
\[
Q_k(t)=(pt)^{k-2}a(t)^2=H_p(t)^2(pt)^{k-2}.
\]
This argument is valid for \(k=2\): there are then no interior sites, and the two exteriors are still disjoint.

**3. Cluster intensities.** Translation invariance and inclusion-exclusion at the two exterior sites imply
\[
\lambda_k(t)=Q_k(t)-2Q_{k+1}(t)+Q_{k+2}(t),\qquad k\ge2.
\]
Substitution proves the stated formula. Since \(0<pt<1\),
\[
\sum_{k\ge2}\lambda_k(t)=(1-pt)H_p(t)^2,
\quad
\sum_{k\ge2}k\lambda_k(t)=(2-pt)H_p(t)^2.
\]
Dividing the individual intensities by their sum proves the geometric conditional law. Its conditional mean is \(2+pt/(1-pt)\).

**4. Singleton intensity.** A site attempts \(A\) at time \(u\) with density \(p\). Before that time, its two neighboring exterior half-lines are independent; each fails to contain an occupied \(B\) neighbor with probability \(1-b(u)\). Consequently
\[
Q_1(t)=\rho_A(t)=p\int_0^t[1-b(u)]^2\,du.
\]
As for the other cluster counts, inclusion-exclusion gives \(\lambda_1=Q_1-2Q_2+Q_3\), yielding the displayed formula. This proves the complete cluster-size intensity distribution.

## Verification

The accompanying standalone `verify_runs.py` performs exhaustive, rational-arithmetic checks of the probability of a marked all-\(A\) interval on finite paths, enumerating every active-site subset, relative arrival order and proposed-color assignment for path lengths three through seven. It compares the independently enumerated probabilities against exact finite-half-line polynomial recurrences at both terminal and intermediate times and for three distinct rational color biases. The script also bounds the convergence of finite-half-line probabilities to \(H_p(t)\) and checks the cluster-intensity summations numerically. It reports 360 passed assertions and 1,146,639 enumerated configurations, including 270 exact finite-path comparisons.

For a finite half-line of \(m\) sites, let \(a_m(t),b_m(t)\) be the endpoint occupation probabilities. These satisfy the polynomial recurrences
\[
a_1(t)=pt,\quad b_1(t)=qt,\quad
a_m(t)=pt-p\int_0^t b_{m-1}(u)du,\quad
b_m(t)=qt-q\int_0^t a_{m-1}(u)du.
\]
For a finite path with \(\ell\) sites to the left and \(r\) sites to the right of a designated \(k\)-site block, the exact all-\(A\) probability is \((pt)^{k-2}a_{\ell+1}(t)a_{r+1}(t)\). A finite-half-line approximation error satisfies \(|a_m(t)-H_p(t)|\le t^{m+1}/(m+1)!\) because any influence from beyond the truncated boundary requires a strictly decreasing chain of \(m+1\) attempt times. The checker verifies that bound at specified finite parameters; the proof establishes it for all valid parameters.

The finite enumeration and numerical checks are tests, not substitutes for the infinite-volume arguments above.

## Relationship to prior work

Do Amaral and dos Santos (2023) define the identical one-attempt antagonistic \(AB\) adsorption model and calculate its single-site type densities at arbitrary times and biases [1]. Their one-site formula agrees with \(\rho_A(t)\) here. Their full treatment does not state a same-color contiguous-cylinder law or the maximal-cluster size distribution; a marginal density alone does not determine either joint quantity. The half-line decomposition in their work is closely related to the one used above, so the derivation is a direct structural extension rather than a new adsorption process.

The related one-species nearest-neighbor exclusion process analyzed by the same authors (2022) [2] excludes *any* adjacent occupied pair, whereas this model permits adjacent particles of the same species; therefore its pair correlation formulas cannot imply the positive-length same-species cluster law here. Martins, Dickman and Ziff (2022) [3] analyze the repeated-proposal antagonistic model, principally in two dimensions; in its one-dimensional discussion they derive or estimate coverage, but the model allows a site to be revisited after unsuccessful deposition and is not the one-attempt process. Penrose and Sudbury (2005) [4] give general deposition methods and nearest-neighbor exclusion correlations for a different blocking mechanism; those constructions help contextualize rigorous finite/infinite dependence but do not specialize to this species-dependent permission rule.

The specific contribution here is the complete time-and-bias-dependent **cluster-length intensity classification**, particularly its geometric tail beginning at length two. The general adsorption and half-line methods are not claimed as new.

## Limitations

The results require exactly one attempt per site, i.i.d. proposal colors and times, the one-dimensional nearest-neighbor graph, and irreversible two-species exclusion of *opposite* colors only. They do not apply directly to repeated-attempt models, other substrates or interactions beyond nearest neighbors. The conditional geometric law begins at length two; singleton clusters carry a distinct intensity. The theorem gives marginal cluster-size intensities, not independence of different clusters, a complete spatial Markov property, or a central limit theorem for cluster counts. No claim of independent external mathematical validation or exhaustive historical priority is made.

## References

[1] C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786, first posted 2023-06-16. https://arxiv.org/abs/2306.09786

[2] C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627, first posted 2022-10-11. https://arxiv.org/abs/2210.05627

[3] P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622, first posted 2022-11-09. https://arxiv.org/abs/2211.04622

[4] M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519, first posted 2005-03-24. https://arxiv.org/abs/math/0503519
