# Exact geometric cluster tails and snapshot calibration in antagonistic one-shot adsorption

## Finding

Consider the one-dimensional, two-species antagonistic random sequential adsorption process with **one attempted deposition per site** described below. Let \(0<p<1\) be the probability of proposing species A, let \(b=1-p\), and observe the process at \(0<t\leq1\). Define
\[
 g=\sqrt{pb},\qquad
 f_A(u)=\cosh(gu)-\frac{b}{g}\sinh(gu),\qquad
 J_A(t)=\int_0^t f_A(u)\,du.
\]
In particular,
\[
 J_A(t)=\frac{\sinh(gt)}{g}-\frac{b}{g^2}\bigl(\cosh(gt)-1\bigr)>0.
\]
Let \(P_m^A(t)\) be the probability that \(m\) specified consecutive sites are all occupied by A by time \(t\). **For every integer \(m\geq2\)**,
\[
 \boxed{P_m^A(t)=p^m t^{m-2}J_A(t)^2.}\tag{1}
\]
The previously established one-point probability is
\[
 P_1^A(t)=p\int_0^t f_A(u)^2\,du.\tag{2}
\]
Let \(d_m^A(t)\) be the expected number per lattice site of **maximal consecutive A-clusters of length exactly \(m\)**. Then for every \(m\geq2\),
\[
 \boxed{d_m^A(t)=p^m t^{m-2}J_A(t)^2(1-pt)^2,}\tag{3}
\]
while
\[
 d_1^A(t)=P_1^A(t)-p^2J_A(t)^2(2-pt).\tag{4}
\]
Thus the cluster-size distribution conditional on a cluster having at least two sites, sampled by **cluster left endpoints** rather than by a uniformly sampled occupied site, is exactly geometric:
\[
 \boxed{\Pr\{L_A=m\mid L_A\geq2\}=(1-pt)(pt)^{m-2},\quad m\geq2.}\tag{5}
\]
All these statements hold at every observation time, including the final frozen state \(t=1\). Species B satisfies the same statements with \(p\) replaced by \(b\).

There is also an **exact inverse calibration law**. Define the ratios of consecutive cluster intensities, for any \(m\geq2\),
\[
 R_A=\frac{d_{m+1}^A(t)}{d_m^A(t)},\qquad
 R_B=\frac{d_{m+1}^B(t)}{d_m^B(t)}.
\]
Then
\[
 \boxed{R_A=pt,\quad R_B=bt,\quad t=R_A+R_B,\quad
 p=\frac{R_A}{R_A+R_B}.}\tag{6}
\]
Consequently, the two species' cluster-tail ratios identify both the deposition progress \(t\) and proposal bias \(p\) from an infinite spatial snapshot under the specified model. Spatial ergodicity makes the corresponding observed frequencies consistent as the observation window grows. As a further spatial-dependence consequence, the nearest-neighbor A-occupation indicators have strictly **positive covariance** for all \(0<p<1\) and \(0<t\leq1\).

## Assumptions and scope

Every site \(i\in\mathbb Z\) independently receives one proposal time \(T_i\sim\mathrm{Unif}[0,1]\) and one mark \(Y_i\in\{A,B\}\) with \(\Pr(Y_i=A)=p\) and \(\Pr(Y_i=B)=b\). Initially all sites are vacant. At time \(T_i\), its marked species occupies site \(i\) precisely when neither neighbor is already occupied by the opposite species. Rejected sites never attempt again. Occupation is irreversible. Time \(t\in(0,1]\) denotes the fraction of sites whose proposal times have passed in expectation, not a rescaled Poisson attempt rate.

This infinite-volume process is well defined almost surely by the standard priority or graphical construction: a proposed arrival's decision has a finite backward dependency cone almost surely, because an influence path extending \(k\) consecutive edges requires a strictly decreasing sequence of \(k+1\) independent continuous proposal times, whose probability is \(1/(k+1)!\). Countable union and factorial decay rule out infinite backward influence paths. The occupation field at fixed \(t\) is a translation-equivariant measurable function of the iid marks and priorities and is therefore stationary and ergodic.

A maximal A-cluster of length \(m\) begins at \(i\) if the sites \(i,\ldots,i+m-1\) are occupied A and neither site \(i-1\) nor site \(i+m\) is occupied A. These exterior sites may be vacant or occupied B; no assumptions are made about more distant sites.

## Proof

**1. One-sided exclusion probability.** Hold an exterior ghost site vacant and evolve an independent half-line. Let \(f_A(u)\) be the probability that the boundary site has not become occupied B by time \(u\); define \(f_B(u)\) by exchanging A and B. The boundary site can first become occupied B in the infinitesimal interval around \(u\) only when its own mark is B, its proposal time lies there, and the next site has not become occupied A. Conditional on the boundary proposal occurring at \(u\), that boundary site is vacant at all earlier times, so the next site's A-exclusion probability equals \(f_B(u)\) by translation of the half-line problem. It follows that
\[
 f_A'(u)=-b f_B(u),\qquad f_B'(u)=-p f_A(u),\qquad
 f_A(0)=f_B(0)=1.\tag{7}
\]
Solving this two-by-two linear initial-value problem gives
\[
 f_A(u)=\cosh(gu)-\frac b g\sinh(gu),\qquad
 f_B(u)=\cosh(gu)-\frac p g\sinh(gu).\tag{8}
\]
These are probabilities. For \(0<p<1\) and \(u\in(0,1]\), both lie strictly between zero and one. In particular, the derivative in (7) is strictly negative. Integrating (8) establishes the stated positive expression for \(J_A\).

**2. A single occupied A.** Conditional on a site having the A mark and proposal time \(u\), acceptance requires no previously accepted B on either side. Until its proposal this site remains vacant, so the two half-lines are independent, and each contributes \(f_A(u)\). Integrating the site proposal time over \([0,t]\) proves (2). This coincides with the known one-point density expression in the motivating source.

**3. Consecutive A block.** Fix \(m\geq2\). All \(m\) sites can be occupied A only if they have A marks and all their proposal times are at most \(t\). Under those conditions every interior site, if any, necessarily accepts: both its neighbors have A marks and can never be occupied B. Only the two endpoints can be blocked, each by a B particle immediately outside the block. Given the endpoint proposal times \(u,v\), the left and right exterior regions are independent up to their respective decisions, and their success probabilities are \(f_A(u)\) and \(f_A(v)\). The \(m-2\) interior proposal times contribute \(t^{m-2}\), the A marks contribute \(p^m\), and integration over the two endpoint proposal times gives
\[
 P_m^A(t)=p^m t^{m-2}\int_0^t f_A(u)\,du\int_0^t f_A(v)\,dv.
\]
This proves (1), including \(m=2\), where there are no interior sites.

**4. Maximal cluster law.** By translation invariance and inclusion-exclusion at the two exterior sites,
\[
 d_m^A=P_m^A-2P_{m+1}^A+P_{m+2}^A.\tag{9}
\]
For \(m\geq2\), substitution of (1) immediately gives (3). For \(m=1\), substitute (2) along with the \(m=2,3\) cases of (1) to obtain (4). Since \(0<pt<1\), the sum of the intensities for \(m\geq2\) is
\[
 \sum_{m=2}^{\infty}d_m^A=p^2J_A(t)^2(1-pt)>0.
\]
Normalizing (3) by this sum yields (5). The same argument applies after interchanging A and B.

**5. Identifiability and correlation.** Dividing consecutive instances of (3) gives \(R_A=pt\), and interchanging species yields \(R_B=bt\). Because \(p+b=1\) and \(t>0\), these equations uniquely determine \(p,t\), proving (6). Stationary ergodicity implies almost-sure convergence of the empirical counts of each finite cluster pattern divided by the observation length to the corresponding positive intensities, so the empirical ratios recover the same parameters in the infinite-window limit.

Finally, write \(K_A(t)=\int_0^t f_A(u)^2\,du\). Equations (1) and (2) imply
\[
 \operatorname{Cov}(\mathbf1_{\{0\text{ occupied A}\}},
 \mathbf1_{\{1\text{ occupied A}\}})
 =p^2\left[J_A(t)^2-K_A(t)^2\right]>0.\tag{10}
\]
The strict inequality follows from \(0<f_A(u)<1\) for every \(u>0\), hence \(0<K_A(t)<J_A(t)\) for every \(t>0\). This completes the proof.

## Verification

The self-contained Python 3 script `verify.py` recomputes the half-line differential identities, independently integrates the published one-point density, checks the full geometric cluster law and parameter reconstruction on a parameter grid, and computes finite-chain probabilities by a dynamic program that averages over **all** proposal orders, independent species marks, and proposal-time activity. The finite-chain dynamic program does not assume the infinite-volume half-line formulas. On execution it passed 1,854 assertions, including five finite-chain comparisons with buffers of four sites on each side. These finite computations support the proof but are not used to infer its universal quantifiers.

To reproduce: run `python verify.py` with Python 3.10 or later in a directory containing this result and that script; no third-party packages are needed.

## Relationship to prior work

The model, its single-attempt rule, and its exact one-point species densities are due to do Amaral and dos Santos [1]. Formula (2), or equivalently the single-site density, is **prior work and not claimed as new**. The present result identifies an exact hierarchy of *consecutive same-species block probabilities*, the resulting complete finite cluster-size intensity law and its geometric tail, the positive adjacent same-species covariance, and inverse calibration from the two cluster tails. None of these joint-cluster statements follows from the one-point density alone.

The same authors separately studied one-species nearest-neighbor-excluding adsorption and its pair correlations [2]. That process forbids adjacent occupied sites irrespective of species and therefore cannot imply (1)–(6) in this two-species antagonistic process. Martins, Dickman, and Ziff [3] studied a different antagonistic protocol allowing repeated proposals at sites and concentrated primarily on two-dimensional percolation and coverage. Its hypotheses do not identify the one-attempt cluster law here. General cooperative adsorption and cluster-hierarchy methods are established; [4] and [5] provide earlier related context. An equivalent specialization in this broader literature remains a priority risk.

## Limitations

The results require iid uniform proposal times, iid species marks, one proposal per site, nearest-neighbor antagonism, an initially vacant infinite line, and perfect observations. The geometric statement concerns **clusters of length at least two sampled by left endpoints**, not the size-biased length of the cluster containing a randomly selected A particle. Singleton-cluster intensities are different and are given separately in (4). The inverse calibration assumes that both species and sufficiently many finite clusters are observable; no finite-sample error bounds are established. The result does not apply unchanged to repeated attempts, longer-range exclusions, finite lattices without boundary corrections, or higher-dimensional clusters.

## References

1. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786v1, first posted 2023-06-16; Journal of Physics A 56, 475204 (2023). https://arxiv.org/abs/2306.09786
2. C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627 (first posted 2022-10-11). https://arxiv.org/abs/2210.05627
3. P. H. L. Martins, R. Dickman, and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (2022); Physical Review E 107, 024104 (2023). https://arxiv.org/abs/2211.04622
4. J. W. Evans, D. K. Hoffman, and D. R. Burgess, *Competing irreversible cooperative reactions on polymer chains*, Journal of Chemical Physics 80, 936–943 (1984), doi:10.1063/1.446751.
5. J. W. Evans and R. S. Nord, *Cluster-size distributions for irreversible cooperative filling of lattices. II. Exact one-dimensional results for noncoalescing clusters*, Physical Review A 31, 3831 (1985).
