# Threshold-specific single-vaccine placement on a path

## Finding

For every integer \(n\ge3\), transmission probability \(0<p<1\), and one perfectly vaccinated vertex of the path \(P_n\), the complete family of optimal vaccination locations for *every* outbreak-size tail threshold is determined below. This classification differs fundamentally from optimizing expected outbreak size; the first conflict occurs on the five-vertex path.

Number the path vertices consecutively. Vaccinate vertex \(m+1\), where \(0\le m\le M=n-1\). The remaining paths have \(m\) and \(M-m\) vertices (zero length is allowed). Choose one initially infected vertex uniformly among the \(M\) unvaccinated vertices. Each infectious vertex transmits once to each susceptible neighbor, independently with probability \(p\), and is then removed permanently; protection is perfect. Let \(C_m\) be the final number of infected vertices **including** the source.

For an integer \(s\ge2\), put
\[
G_s(j)=\begin{cases}
0,&0\le j<s,\\
p^{s-1}\left[s+(j-s)\bigl(s-(s-1)p\bigr)\right],&j\ge s.
\end{cases}
\]
Then the exact final-size upper tail is
\[
\Pr(C_m\ge s)=\frac{G_s(m)+G_s(M-m)}{M}.
\]
For \(s=1\), the tail is one, and for \(s>M\), it is zero, independently of placement. For \(2\le s\le M\), the complete set of tail-minimizing left-side lengths is
\[
\mathcal T_s=\begin{cases}
\{s-1,M-s+1\},&M\ge 2s-1,\\
\{M-s+1,M-s+2,\ldots,s-1\},&s\le M\le2s-2.
\end{cases}
\]
In contrast, the complete set of **mean-size** minimizing left lengths is
\[
\mathcal E=\left\{\left\lfloor\frac M2\right\rfloor,\left\lceil\frac M2\right\rceil\right\}.
\]
All optimizer descriptions hold simultaneously for every \(p\in(0,1)\). For \(n\ge5\), the tail-minimizers at \(s=2\) are \(m=1,M-1\), disjoint from \(\mathcal E\). At the threshold \(s=\lceil M/2\rceil+1\), central vaccination gives zero probability, but either \(s=2\) optimizer has positive probability. Consequently **no single vaccination location first-order stochastically minimizes final outbreak size** for \(n\ge5\). The cutoff \(n=5\) is sharp.

## Assumptions and scope

This is the independent-edge, one-infectious-period Reed–Frost process on a finite simple path, not a continuous-time Markovian SIR model. The potential transmission outcomes on different edges are independent. The source is chosen *after vaccination*, uniformly among unvaccinated vertices. One vertex is vaccinated in advance. There are no multiple introductions, imperfect protection, correlated transmissions, or recovery-time heterogeneity. The source counts as one infection.

The parameter \(p\) is a *per-edge eventual transmission probability*, not a reproduction number. Every theorem here applies to all integers \(n\ge3\), all integers \(s\ge1\), and all \(0<p<1\), with the cases \(s=1\) and \(s>M\) as separately stated.

## Proof

**Step 1 (path percolation reduction).** Independently declare each susceptible-to-infectious contact edge open with probability \(p\). Because each newly infected vertex has exactly one opportunity to infect every still-susceptible neighbor, the final infected set from a fixed source equals its open-edge connected component. Deleting the vaccinated vertex leaves two independent path pieces; conditioning on the uniformly selected source gives the sum of their source-weighted component probabilities divided by \(M\).

**Step 2 (exact upper-tail weight).** On a path with \(j\ge s\) vertices, let \(G_s(j)\) be the expected sum of the sizes of all open-edge components having at least \(s\) vertices. For each length \(1\le\ell< s\), the expected number of open-edge components of exactly \(\ell\) vertices is
\[
 p^{\ell-1}\left[(j-\ell-1)(1-p)^2+2(1-p)\right],
\]
since such a component either has both ends inside the path or touches exactly one endpoint. There is no whole-path component of length \(\ell<s\) when \(j\ge s\). Therefore
\[
G_s(j)=j-\sum_{\ell=1}^{s-1}\ell p^{\ell-1}\left[(j-\ell-1)(1-p)^2+2(1-p)\right].
\]
The finite geometric derivative identity
\[
(1-p)^2\sum_{\ell=1}^{s-1}\ell p^{\ell-1}=1-sp^{s-1}+(s-1)p^s
\]
shows this is affine in \(j\), with slope \(p^{s-1}[s-(s-1)p]\). At \(j=s\), its value is \(s p^{s-1}\), the event that all \(s-1\) edges are open. These determine precisely the displayed \(G_s(j)\). If \(j<s\), it is zero by definition.

**Step 3 (all tail optimizers).** Put \(a=s-(s-1)p>0\). When both remaining pieces have at least \(s\) vertices, the numerator of the upper tail equals
\[
p^{s-1}\left[aM-2s(s-1)(1-p)\right],
\]
independent of their individual lengths. With exactly one piece shorter than \(s\), the numerator decreases strictly as the smaller length increases, so among such placements it is least when that length is \(s-1\). Comparing this one-short placement against every two-long placement gives the **strict, exact** excess
\[
 (s-1)p^s>0
\]
in the unnormalized tail numerator. If \(M\ge2s-1\), both pieces cannot be shorter than \(s\), giving exactly the two stated minimizers. If \(s\le M\le2s-2\), both pieces can be shorter than \(s\), yielding tail zero precisely for the displayed integer interval. The remaining threshold cases are immediate.

**Step 4 (expected-size optimizers).** For an open-edge path with \(j\) vertices, the source-weighted expected cluster size is
\[
H(j)=\sum_{u,v=1}^{j}\Pr(u\leftrightarrow v)
=j+2\sum_{d=1}^{j-1}(j-d)p^d,
\]
where \(H(0)=0\). Consequently \(\mathbb E C_m=[H(m)+H(M-m)]/M\). Its forward difference satisfies
\[
H(j+1)-H(j)=1+2\sum_{d=1}^{j}p^d,
\]
which is strictly increasing in \(j\). Transferring one vertex from a larger component to a smaller component strictly lowers the sum unless the two lengths already differ by at most one. This proves the exact mean-minimizer set \(\mathcal E\).

**Step 5 (sharp conflict and first-order dominance failure).** For \(M\ge4\), threshold \(s=2\) uniquely favors \(m=1\) or \(m=M-1\). At either central mean minimizer, both component lengths are at least two, and the probability of two or more infections exceeds that of either near-end optimizer by exactly \(p^2/M\). But at \(s=\lceil M/2\rceil+1\), a central placement makes both components shorter than \(s\), so its upper tail is zero; a near-end placement has a component of size \(M-1\ge s\) and a strictly positive tail. Hence no position minimizes all upper tails. For \(n=3,4\), the finite optimizer descriptions above admit a common placement, proving sharpness.

**Exact example.** At \(n=5\) and \(p=1/2\), central vaccination \(m=2\) gives mean size \(3/2\), probability of at least two infections \(1/2\), and probability of at least three infections zero. Vaccination at \(m=1\) or \(m=3\) gives respectively \(13/8\), \(7/16\), and \(3/16\). The two risk orderings cross despite a fixed transmission probability.

## Verification

The accompanying `VERIFY.py` computes all bond configurations on each path with at most ten vertices using `fractions.Fraction`, independently builds source-weighted outbreak-size distributions, and compares them with the stated formulas. It also enumerates all single-vaccine placements for all \(2\le M\le10\), all integer thresholds through \(M+2\), and \(p\in\{1/4,1/2,3/4\}\), checking exact optimizer sets and the five-vertex example. Execution returned `VERIFICATION_OK 529 exact-rational assertions`. The finite checks corroborate, but are not substitutes for, the general proof.

## Relationship to prior work

Holme (2017), arXiv:1708.06456, studies expected final outbreak size, vaccination and early sentinel monitoring on *all graphs through seven vertices* using a continuous-time SIR model. It does not establish the threshold-by-threshold vaccination optimum for Reed–Frost on paths of arbitrary length. The anticipated centrality of balanced deletion is consistent with its mean-based studies, and is not independently claimed as a general-purpose vaccination discovery.

Chatterjee and Zehmakan (2023), arXiv:2305.16458, study node vaccination with heterogeneous contacts and a **different** degree-normalized transition mechanism; they assess final mortality and centrality heuristics rather than these exact Reed–Frost upper-tail objectives. Clusella et al. (2016), arXiv:1604.00073, investigate network fragmentation and largest-component/mean component-size proxies: their surrogate objectives do not imply the stochastic threshold classification above. Yuan et al. (2015), PLOS ONE 10:e0115826, determine vaccine allocation across two well-mixed noninteracting populations by optimizing mean outbreak size under a continuous-time SIR master equation; their full-text methods and allocation/results sections do not provide path-deletion upper-tail optimizers. Classical bond-percolation cluster identities are treated as known ingredients. The contribution assessed here is the complete finite-path tail-optimum phase diagram and sharp incompatibility with the mean objective.

## Limitations

There is no claim of priority over inaccessible or unpublished related work, nor of extension to general trees, cycles, time-correlated contacts, different source laws, infection-duration variation, or multiperiod intervention. Exact small-graph rankings from other models are not equivalent to this all-size Reed–Frost classification. The result concerns mathematical risk criteria, not a prescriptive vaccination recommendation. Independent validation has not been performed.

## References

- P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs* (first arXiv submission 2017-08-22), arXiv:1708.06456, https://arxiv.org/abs/1708.06456.
- S. Chatterjee and A. N. Zehmakan, *Effective Vaccination Strategies in Network-based SIR Model* (first arXiv submission 2023-05-25), arXiv:2305.16458, https://arxiv.org/abs/2305.16458.
- P. Clusella, P. Grassberger, F. J. Pérez-Reche, and A. Politi, *Immunization and targeted destruction of networks using explosive percolation* (first arXiv submission 2016-03-31), arXiv:1604.00073, https://arxiv.org/abs/1604.00073.
- E. C. Yuan, D. L. Alderson, S. Stromberg, and J. M. Carlson, *Optimal vaccination in a stochastic epidemic model of two non-interacting populations* (2014), arXiv:1407.3215, https://arxiv.org/abs/1407.3215. The open-access published full text was inspected (PLOS ONE, DOI: 10.1371/journal.pone.0115826): its continuous-time, two-well-mixed-population mean-burden optimization does not imply a fixed single vaccinated vertex on a path or the whole family of threshold-optimal placements.
