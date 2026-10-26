# One-source-failure discounted hitting domination on cycles

## Finding

For every simple cycle \(C_n\), integer \(n\geq3\), fidelity \(0<\lambda<1\), and required support \(0<\tau\leq1\), consider source sets that remain feasible after **any one source loses its pinned status**. A failed source remains an ordinary vertex of the cycle; the graph itself does not change. Let \(a=\operatorname{arcosh}(1/\lambda)\), and define for all integers \(g\geq1\)
\[
\psi_\lambda(g)=\begin{cases}
1/\cosh(ag/2),&g\text{ even},\\
\cosh(a/2)/\cosh(ag/2),&g\text{ odd}.
\end{cases}
\]
Set \(B=\min\{n,\max\{g\geq1:\psi_\lambda(g)\geq\tau\}\}\). This maximum exists because \(\psi_\lambda(1)=1\) and the sequence decreases strictly to zero.

**Theorem.** If \(B=1\), no nonempty source set remains feasible after arbitrary loss of one source. If \(2\leq B\leq n\), the minimum resilient source-set size is exactly
\[
\boxed{\delta^{\mathrm{1fail}}_{\lambda,\tau}(C_n)=\left\lceil\frac{2n}{B}\right\rceil.}
\]
For \(k=\lceil 2n/B\rceil\), the **entire family of labelled optimal source sets** consists of the \(k\)-element subsets whose positive cyclic source-to-source edge gaps \(g_1,\ldots,g_k\) satisfy
\[
\sum_{i=1}^kg_i=n,\qquad g_i+g_{i+1}\leq B\quad(1\leq i\leq k),
\]
with cyclic indices. In particular, their exact number is
\[
\boxed{N_{n,B}=\frac{n}{k}[z^n]\,\operatorname{tr}\!\bigl(M_B(z)^k\bigr),\quad
(M_B(z))_{u,v}=\begin{cases}z^v,&u+v\leq B,\\0,&u+v>B,\end{cases}\quad 1\leq u,v<B.}
\]
The scalar coefficient expression is an integer because it counts labelled vertex subsets.

The first two nontrivial phase censuses are explicit. If \(B=3\), then
\[
N_{n,3}=\begin{cases}3,&n\equiv0\pmod3,\\n,&n\equiv1\pmod3,\\n(n+1)/6,&n\equiv2\pmod3.\end{cases}
\]
If \(B=4\), then
\[
N_{n,4}=\begin{cases}
6,&n\equiv0\pmod4,\\
2,&n\equiv2\pmod4,\\
n\lfloor(n+3)/4\rfloor,&n\text{ odd}.
\end{cases}
\]
The even-gap phase \(B=4\) is an intermediate gap constraint between the familiar radius-one and radius-two fault-tolerant distance-domination conditions. For sufficiently large cycles, it is not obtained by substituting an integer radius.

## Assumptions and scope

The graph is the labelled, unweighted, undirected simple cycle on vertices \(0,\ldots,n-1\), with edges between consecutive residues. For a nonempty source set \(S\), the homogeneous discounted support is \(h_v^S=\mathbb E_v[\lambda^{T_S}]\), where \(T_S\) is the first hitting time of \(S\) by simple random walk. Thus \(h_v^S=1\) for \(v\in S\) and \(h_v^S=\lambda(h_{v-1}^S+h_{v+1}^S)/2\) otherwise. The empty source set has support zero. A source set is resilient when \(\min_v h_v^{S\setminus\{s\}}\geq\tau\) for **every** \(s\in S\). Only one failure, not simultaneous multiple failures, is considered. There is no source-specific weighting or post-failure relocation.

## Proof

**1. Exact gap criterion.** Between consecutive sources at graph distance \(g\) along the cycle, the non-source support solves the tridiagonal boundary problem \(u_0=u_g=1\), \(u_j=\lambda(u_{j-1}+u_{j+1})/2\) for \(1\leq j<g\). Its unique solution is
\[
u_j=\frac{\cosh(a(j-g/2))}{\cosh(ag/2)}.
\]
The minimum over the segment is attained in its middle and is exactly \(\psi_\lambda(g)\). The same boundary problem applies when there is just one source, because the two ends of the unique cyclic gap refer to that same source vertex. The gap values are strictly decreasing with \(g\geq1\); this transfer calculation and the monotonicity also appear as Lemmas 5.1 and 5.5 of Allagan–Pereyra–Massey (2026). Therefore a nonempty source set on \(C_n\) reaches the floor \(\tau\) if and only if all cyclic gaps have size at most \(B\). This is an ingredient from prior work, not asserted as a new theorem.

**2. Deleting one source.** If \(S\) has just one source, deleting it leaves empty support, so it cannot be resilient. If \(|S|=k\geq2\), write its positive cyclic gaps as \(g_1,\ldots,g_k\). Deleting source \(i\) merges precisely its incoming and outgoing gaps into a single gap of length \(g_{i-1}+g_i\); all other source gaps stay unchanged. When \(k=2\) the resulting single gap has length \(g_1+g_2=n\), and the same argument applies. By the gap criterion, resilience is **equivalent** to \(g_{i-1}+g_i\leq B\) for all indices. Because each positive gap belongs to such a pair, these inequalities also imply that every unmerged gap is admissible. If \(B=1\), at least one merged gap has length at least two, making resilience impossible for every nonempty \(S\).

**3. Cardinality lower bound and construction.** Summing all \(k\) adjacent-gap inequalities gives \(2n\leq kB\). Hence \(k\geq\lceil2n/B\rceil\). For \(B\geq2\), put \(k=\lceil2n/B\rceil\); then \(2\leq k\leq n\).

If \(B=2r\) is even, \(n\leq kr\). Since \(k\leq n\), choose \(k\) positive integers not exceeding \(r\) whose sum is \(n\). Every adjacent sum is at most \(2r=B\).

If \(B=2r+1\) is odd, first suppose \(n\leq kr\), and use the same construction. Otherwise write \(n=kr+t\) with \(t>0\). The definition of \(k\) yields \(2n\leq k(2r+1)\), so \(t\leq\lfloor k/2\rfloor\). Choose \(t\) nonconsecutive positions on a cyclic list of length \(k\), assign those gaps length \(r+1\), and assign every other gap length \(r\). This list has sum \(n\) and adjacent sums at most \(2r+1=B\). Reading either gap list around the labelled cycle constructs a resilient set with exactly \(k\) sources. This establishes the sharp minimum and the exhaustive gap classification.

**4. Exact labelled census.** Every admissible cyclic gap list uses values \(1,\ldots,B-1\). A closed walk of length \(k\) on these gap values, using transition weight \(z^v\) when consecutive gap values \(u,v\) satisfy \(u+v\leq B\), has total weight \(z^{\sum g_i}\). Thus \([z^n]\operatorname{tr}(M_B(z)^k)\) counts the admissible ordered \(k\)-tuples of gaps summing to \(n\). There are \(n\) choices for the labelled starting source; a given labelled \(k\)-source set appears exactly \(k\) times under this rooted description. Dividing by \(k\) gives \(N_{n,B}\), with no symmetry or orbit-size assumption.

**5. Explicit phase counts.** When \(B=3\), every gap is one or two, and twos must be nonadjacent. An optimum has \(k=\lceil2n/3\rceil\) gaps, of which exactly \(n-k\) are twos. The standard cyclic nonadjacency count gives \(\frac{k}{2k-n}\binom{2k-n}{n-k}\) ordered gap lists; applying the labelled-root factor \(n/k\) reduces to the three displayed residue formulas.

When \(B=4\), put \(k=\lceil n/2\rceil\) and \(d_i=4-g_i-g_{i+1}\geq0\). Summing gives \(\sum_i d_i=4k-2n\). For even \(n\), this is zero, so \(g_{i+1}=4-g_i\) throughout: if \(k\) is odd only the all-two list is possible (two labelled sets), whereas if \(k\) is even the all-two list and the two alternating one/three lists are possible (six labelled sets). For odd \(n\), the slack sum is two. If \(k\) is odd, every choice of nonnegative slacks summing to two (one two or two ones) determines a unique valid gap list with each gap in \(\{1,2,3\}\), giving \(k+\binom{k}{2}\) lists. If \(k\) is even, consistency of \(g_{i+1}=4-d_i-g_i\) requires one unit slack in each parity class of indices; there are \((k/2)^2\) such assignments and exactly two valid gap lists for each, giving \(k^2/2\) lists. Multiplication by \(n/k\) gives the stated odd-order formula. These arguments include \(k=2\) and \(n=3\).

## Verification

The standalone script `verify_resilience_exact.py` independently reconstructs the simple random walk's rational hitting equations and tests every single-source deletion over all relevant labelled subsets for \(3\leq n\leq8\), fidelities \(\lambda=2/5,3/5\), and each critical admissible gap threshold \(1\leq B\leq n\). It performed 6,688 exact rational feasibility comparisons, checked the merged-gap characterization, the infeasibility boundary, and every minimum cardinality. The script `verify_cycle_transfer.py` independently computes cyclic transfer coefficients and enumerates labelled minimum sets for \(3\leq n\leq13\) and \(2\leq B\leq n\), validating all 77 cases, including the explicit \(B=3\) counts. Both returned `VERIFY_OK` when executed from their packaged paths.

Finite verification checks implementation and small boundaries; the proof of the infinite formulas is the preceding gap-merge inequality, constructive gap placement, and rooted cyclic enumeration.

## Relationship to prior work

Allagan, Pereyra, and Massey introduced discounted hitting domination in September 2026 and established the general hitting-potential model and exact two-boundary gap profile. Their Lemma 5.5 supplies the admissible-gap cutoff \(B\) used here. They develop results for spiders, complete graphs, and general optimization; the inspected full text does not state the cycle one-failure formula, the adjacent-gap classification, or the exact labelled transfer census. The ordinary no-failure cycle gap rule follows immediately from their published lemma and is **not** claimed as new.

When \(B\) is an odd integer of the form \(2r+1\), the resilient condition specializes to classical twofold distance-\(r\) domination on a cycle, so such cardinality specializations are related to pre-existing multiple-domination theory. In particular, the \(B=3\) case coincides with double domination in closed neighborhoods. The discounted model also has **even** cutoff values, especially \(B=4\), which are not recovered by a single integer-radius double-domination substitution. The contribution here is the all-fidelity exact one-failure theorem, its exhaustive optimal-set description, and the uniform labelled counting formula, with both parity phases treated together. A distinct previously indexed fault-tolerant first-hitting formula is a residual historical-priority risk.

## Limitations

The result concerns unweighted simple cycles, homogeneous \(0<\lambda<1\), strictly positive thresholds, and loss of pinned status at exactly one source. Removing a source vertex or incident edges is a different stochastic model; simultaneous failures of two or more pinned sources are not settled. The classification is mathematically proved but has not received an independent external audit. Broad historical novelty beyond inspected sources is not certified.

## References

1. J. D. Allagan, K. Pereyra, and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (first public version 2026-09-25), especially Sections 2, 5, 6, and 7.
2. T. Pramanik, *Minimum 2-Tuple Dominating Set of an Interval Graph*, International Journal of Combinatorics (2011), DOI:10.1155/2011/389369, for standard double-domination terminology (not an assertion of cycle priority).
