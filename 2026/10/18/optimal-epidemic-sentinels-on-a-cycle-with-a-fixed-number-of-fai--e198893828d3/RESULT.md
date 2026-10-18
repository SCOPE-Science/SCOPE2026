# Optimal epidemic sentinels on a cycle with a fixed number of failed contacts

## Finding

**Theorem (complete placement classification).** Let \(C_n\) be a simple undirected cycle with \(n\ge3\). Exactly \(m\) of its \(n\) edges fail, chosen uniformly from all \(\binom nm\) subsets, where \(0\le m\le n\). One outbreak source is chosen uniformly from the \(n\) vertices, independently of the failures. The outbreak comprises its entire surviving-edge connected component. A predetermined set of \(k\) distinct perfect sentinels, \(1\le k\le n\), detects the outbreak if and only if that component contains a sentinel.

When \(m\le1\), every placement detects surely. Suppose \(m\ge2\), and set \(L=n-m+1\). Write the clockwise edge counts between consecutive sentinels as positive integers \(\ell_1,\ldots,\ell_k\) with total \(n\). Then:

- If \(n<kL\), a sentinel set is optimal **if and only if** all its gaps belong to \(\{\lfloor n/k\rfloor,\lceil n/k\rceil\}\).
- If \(n\ge kL\), a sentinel set is optimal **if and only if** every gap satisfies \(\ell_i\ge L\).

At the boundary \(n=kL\), both descriptions give the same all-\(L\) arrangement. For \(m\ge2\) and \(k\ge2\), a genuinely non-balanced optimal gap vector exists exactly when \(n\ge kL+2\). The second regime therefore contains a sharp *flat placement plateau* after the disruption budget is sufficiently severe.

For example, with \(n=10\), \(m=8\), and \(k=2\), the complete optimal set of unoriented gap pairs is \((3,7)\), \((4,6)\), \((5,5)\). All detect with probability \(13/45\). The placement \((1,9)\) detects with probability \(11/45\), while \((2,8)\) detects with probability \(127/450\). This is a distinction between *eventual detection* and detection delay: no time variable is introduced.

## Assumptions and scope

Every one of the \(\binom nm\) subsets of exactly \(m\) failed edges has the same probability. Transmission is deterministic along the remaining edges; failures are negatively dependent because their count is fixed. The single source is uniform over vertices and independent of the failed edges. Sentinels are perfect, do not remove edges, and cannot fail. The graph has no shortcuts and no directed or heterogeneous contacts. No independent-bond assumption is made.

Write \(B(s)=\binom{n-s}{m}/\binom nm\) for \(0\le s\le n\), taking an inadmissible binomial coefficient to be zero. It is the probability that a fixed set of \(s\) edges contains no failed edge. Define

\[
f(\ell)=\sum_{r=1}^{\ell-1}\bigl(1-B(r)-B(\ell-r)+B(\ell)\bigr),\qquad 1\le\ell\le n.
\]

If \(S\) is the sentinel set and \(Q(S)\) is the non-detection probability, then

\[
Q(S)=\frac1n\sum_{i=1}^k f(\ell_i).
\]

The objective is to minimize \(Q(S)\) among all \(k\)-element vertex subsets. All quantifiers and the exact sampling mechanism are as stated above.

## Proof

**1. Gap decomposition.** A source located at an interior point of an arc of \(\ell\) edges, \(r\) edges from its left sentinel and \(\ell-r\) from its right sentinel, avoids all sentinels exactly when both its subarcs contain at least one failed edge. Leaving this arc would require traversing one of the endpoint sentinels, so other sentinels are irrelevant to the event. Inclusion-exclusion on the two disjoint subarcs gives

\[
\Pr(\text{miss}\mid r,\ell)=1-B(r)-B(\ell-r)+B(\ell).
\]

Summing over all non-sentinel sources in each arc and dividing by \(n\) proves the claimed objective. A source that is itself a sentinel is always detected.

**2. Exact discrete curvature.** From the preceding expression,

\[
f(\ell)=(\ell-1)(1+B(\ell))-2\sum_{r=1}^{\ell-1}B(r).
\]

Consequently the first forward difference is

\[
f(\ell+1)-f(\ell)=1+\ell B(\ell+1)-(\ell+1)B(\ell).
\]

For \(1\le\ell\le n-2\), the second difference is

\[
\begin{aligned}
f(\ell+2)-2f(\ell+1)+f(\ell)
&=(\ell+1)\bigl[B(\ell)-2B(\ell+1)+B(\ell+2)\bigr]\\
&=(\ell+1)\frac{\binom{n-\ell-2}{m-2}}{\binom nm}.
\end{aligned}
\]

Indeed, the bracket is the probability that the first \(\ell\) specified edges survive and the next two specified edges fail; the remaining \(m-2\) failures can be chosen freely among \(n-\ell-2\) edges. For \(m\ge2\), curvature is strictly positive for \(1\le\ell\le n-m\) and exactly zero for larger available indices. Thus the marginal increments of \(f\) strictly increase until \(L=n-m+1\), then equal \(1\) thereafter. In particular the increment at each \(\ell<L\) is strictly below \(1\): since \(B(\ell)>0\) and \(B(\ell+1)\le B(\ell)\), the displayed first difference is at most \(1-B(\ell)<1\).

**3. Optimization.** If \(n<kL\), any gap vector contains a gap shorter than \(L\). If two gaps differ by at least two, transferring one edge from a longest gap to a shortest gap strictly decreases the sum of their \(f\)-values by the strictly ordered marginal increments. Therefore every optimum has gaps differing by at most one. Such balanced gaps exist, and repeated exchanges strictly improve every other vector.

If \(n\ge kL\), vectors with every gap at least \(L\) exist. For every \(\ell\ge L\), the function \(f(\ell)\) is affine of slope \(1\); all such vectors therefore have the same objective. If any gap is shorter than \(L\), the total length condition implies some other gap exceeds \(L\). Moving one edge from that longer gap to the short gap strictly decreases the objective, since its marginal removal cost is \(1\) and the short gap's marginal addition cost is below \(1\). Hence exactly the stated vectors are optimal. The case \(m\le1\) is immediate because deleting at most one edge leaves a cycle connected.

Finally, in the flat regime all gaps of length at least \(L\) are optimal. Such a vector is non-balanced exactly when one gap exceeds another by at least two. This is possible for \(k\ge2\) if and only if \(n-kL\ge2\), by placing two excess edges on one gap, and proves the sharp onset of non-balanced optima.

## Verification

The standalone `verify_cycle_sentinels.py` independently enumerates every selection of \(m\) failed edges and all choices of \(k\) sentinels on each cycle of sizes \(3\le n\le9\). The direct calculation identifies graph components by breadth-first traversal; it does not use the gap probability formula. It then checks the gap formula and the exact optimizer classification for each of 9,151 parameter-and-placement cases. The program further checks exact second-difference certificates and the ten-vertex example. The checks completed successfully with rational arithmetic using only the Python standard library.

Run `python verify_cycle_sentinels.py` from the directory containing that file. The finite checks supplement, but do not substitute for, the unrestricted proof above.

## Relationship to prior work

Moore and Newman (2000) developed bond-percolation and epidemic-cluster calculations on small-world networks, including local cycles; their random-bond and infinite-network objectives do not determine optimum sentinel gaps under exactly \(m\) failed edges. Holme (2017) analyzed influence, vaccination, and sentinel surveillance on all small connected graphs under a continuous-time SIR dynamics, optimizing expected discovery time, not the present event of eventual detection under a fixed cardinality of failed edges. Bai and collaborators (2017) used empirical and simulated temporal networks to optimize surveillance lead time; this is not an all-size finite-cycle combinatorial classification. More generally, sensor-placement and reliability literature contains results for different observability and fault models; none of the inspected results establishes the exact gap-saturation criterion in this theorem.

## Limitations

This result does not assert corresponding placement classifications for independent rather than fixed-count edge failures, directed cycles, nonuniform sources, faulty sentinels, nonuniform edge risk, general graphs, or time-to-detection metrics. Its optimum is for an artificial but interpretable uniform fixed-disruption model, not a calibrated epidemiological forecast. No independent peer assessment or bibliographic completeness claim is made.

## References

1. C. Moore and M. E. J. Newman, “Exact solution of site and bond percolation on small-world networks,” arXiv:cond-mat/0001393v1 (public 2000-01-26), https://arxiv.org/abs/cond-mat/0001393; *Physical Review E* 62 (2000), 7059–7064, https://doi.org/10.1103/PhysRevE.62.7059.
2. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” arXiv:1708.06456 (2017), https://arxiv.org/abs/1708.06456; *Physical Review E* 96, 062305, https://doi.org/10.1103/PhysRevE.96.062305.
3. Y. Bai, B. Yang, L. Lin, J. L. Herrera, Z. Du, and P. Holme, “Optimizing sentinel surveillance in temporal network epidemiology,” *Scientific Reports* 7 (2017), 4804, https://doi.org/10.1038/s41598-017-03868-6.
