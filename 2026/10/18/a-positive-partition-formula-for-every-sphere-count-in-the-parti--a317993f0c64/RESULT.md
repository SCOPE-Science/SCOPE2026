# A positive partition formula for every sphere count in the partition-transfer clique complex

## Finding

For each integer \(n\ge1\), the **partition-transfer graph** \(G_n\) has as vertices the partitions of \(n\). Distinct partitions are adjacent if one is obtained from the other by moving one cell between rows of a Ferrers diagram and reordering the resulting parts. Let \(K_n=\operatorname{Cl}(G_n)\), its clique complex.

Write a partition in distinct-size blocks as
\[
\lambda=(d_1^{m_1},\ldots,d_t^{m_t}),\qquad d_1>\cdots>d_t\ge1,\quad m_j\ge1.
\]
Define the **nonnegative partition weight**
\[
w(\lambda)=
\begin{cases}
0,&t\le2,\\
\displaystyle\binom{t-2}{2}+\sum_{j=2}^{t-1}\mathbf1_{\{m_j\ge2\}},&t\ge3.
\end{cases}
\]
Then for **every** \(n\ge1\), the Euler characteristic and sphere multiplicity are
\[
\boxed{\quad\chi(K_n)=1+\sum_{\lambda\vdash n}w(\lambda),\qquad
K_n\simeq\bigvee^{\sum_{\lambda\vdash n}w(\lambda)}S^2.\quad}
\]
The homotopy-equivalence step invokes the established all-parameter theorem in [1], which proves \(K_n\simeq\bigvee^{\chi(K_n)-1}S^2\). The **new** assertion is the explicit, positive integer-partition formula for this formerly implicitly defined multiplicity, together with the following uniform consequence:
\[
\boxed{\quad b_n=0\ \text{for}\ 1\le n\le7,\qquad b_{n+1}\ge b_n+1\ \text{for every}\ n\ge7.\quad}
\]
Consequently every \(K_n\) with \(n\ge8\) is noncontractible, and its number of spheres increases strictly with \(n\).

An equivalent **formal generating-function identity** makes the result usable without enumerating cliques. Put
\[
P(q)=\prod_{j\ge1}(1-q^j)^{-1},\qquad
P_{<k}(q)=\prod_{1\le j<k}(1-q^j)^{-1},\qquad
P_{>k}(q)=\prod_{j>k}(1-q^j)^{-1}.
\]
Then
\[
\boxed{\begin{aligned}
\sum_{n\ge1}b_nq^n={}&P(q)\left(1-\frac{q}{1-q}+\frac{q^3}{(1-q)(1-q^2)}\right)-1\\
&-\sum_{k\ge1}q^k\bigl(P_{<k}(q)-1\bigr)\bigl(P_{>k}(q)-1\bigr).
\end{aligned}}
\]
All products and sums are interpreted coefficientwise in the ring of integer formal power series.

## Assumptions and scope

The graph has *unordered* integer partitions, each counted once, not compositions or labeled rows. A transfer must yield a **different** partition; apparent exchanges that merely permute parts are not edges. The topological statement concerns the finite abstract clique complex at each \(n\), ordinary integral homotopy type, and nonnegative integral sphere multiplicities. The positive partition formula and its growth law are proved for all positive integers, not just the tested range. The previously published sphere-wedge theorem [1] is cited rather than reproved. Primary MSC2020: 55U10 (homotopy and homology of combinatorially defined simplicial complexes).

## Proof

**1. Height filtration.** For a partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\), write
\(h(\lambda)=\sum_{r=1}^{\ell}r\lambda_r\).
Moving a Ferrers cell from its removable row to a distinct addable row changes \(h\) by the difference of their row indices. Along every genuine edge this change is nonzero [1, Section 2]; the assertion also follows directly from the block calculation below. Thus every clique of \(G_n\) has a unique vertex of greatest height. If \(N_-(\lambda)\) denotes the neighbors with *smaller* height and \(L_\lambda=\operatorname{Cl}(G_n[N_-(\lambda)])\), summing alternating clique signs by their unique largest-height vertex gives
\[
\chi(K_n)=\sum_{\lambda\vdash n}\bigl(1-\chi(L_\lambda)\bigr).
\]
We use \(\chi(\varnothing)=0\), so a vertex with no lower neighbors contributes one.

**2. Exact structure of the lower-neighbor graph.** The removable corner of the \(j\)-th distinct-size block is in its last row, and the addable corner of the \(k\)-th block is in its first row. An additional addable corner creates a new bottom row. A *downward* (height-decreasing) admissible transfer has precisely one of the two forms
\[
(j,k),\quad 1\le k<j\le t,\qquad\text{or}\qquad(j,j),\quad m_j\ge2.
\]
All these transfers are admissible and distinct. Transfers with \(k>j\), including the new-bottom-row choice, have increasing height. When \(k=j\), the transfer decreases height exactly if the block contains at least two rows; a singleton-block diagonal transfer is not admissible. The gap-one transfer obstruction occurs only when \(k=j+1\), outside the decreasing set. These assertions also agree with the complete local transfer classification in [2, Lemma 3.1].

Let \(B_\lambda^-\) be the simple bipartite graph with left vertices \(c_1,\ldots,c_t\), right vertices \(a_1,\ldots,a_t\), and edges corresponding to precisely these decreasing pairs. The graph induced by the lower neighbors of \(\lambda\) is the **line graph** \(L(B_\lambda^-)\). Indeed the conjugate partition changes under a transfer by subtracting a basis vector at its removable column and adding one at its addable column. For two *distinct* admissible transfers, their resulting partitions differ by a single genuine transfer exactly when the original transfers have the same removable corner or the same addable corner. With both corners different, the four signed basis terms cannot reduce to one positive and one negative unit (cross coincidences reinforce the same sign). This also specializes [2, Theorem 4.2].

**3. Euler characteristic of the descending link.** For any finite simple bipartite graph \(B\), every clique of size at least two in \(L(B)\) is a collection of edges incident at one common vertex of \(B\); that center is unique. Writing \(V_+(B)\) for nonisolated vertices gives
\[
\chi(\operatorname{Cl}(L(B)))=|V_+(B)|-|E(B)|.
\]
To verify this identity directly, singletons contribute \(|E(B)|\); cliques of size at least two contribute \(\sum_{v\in V_+(B)}\sum_{r=2}^{\deg v}(-1)^{r-1}\binom{\deg v}{r}=\sum_v(1-\deg v)\), yielding the identity.

Let \(\rho_j=\mathbf1_{\{m_j\ge2\}}\). From the triangular edge set of \(B_\lambda^-\),
\[
|E(B_\lambda^-)|=\frac{t(t-1)}2+\sum_{j=1}^t\rho_j.
\]
For \(t\ge2\), the nonisolated left vertices are \(c_2,\ldots,c_t\), plus \(c_1\) if \(\rho_1=1\). The nonisolated right vertices are \(a_1,\ldots,a_{t-1}\), plus \(a_t\) if \(\rho_t=1\). Therefore
\[
\begin{aligned}
1-\chi(L_\lambda)
&=1-\bigl(2(t-1)+\rho_1+\rho_t\bigr)
 +\frac{t(t-1)}2+\sum_{j=1}^t\rho_j\\
&=\frac{(t-2)(t-3)}2+\sum_{j=2}^{t-1}\rho_j.
\end{aligned}
\]
For \(t=2\), the displayed value is zero. For \(t\ge3\), it is exactly \(w(\lambda)\). If \(t=1\), the lower-neighbor graph is empty when \(m_1=1\) and has one vertex when \(m_1\ge2\); thus its Euler contribution is respectively one and zero. The only partition with \(t=m_1=1\) is \((n)\). Summing the height contributions proves
\(\chi(K_n)=1+\sum_{\lambda\vdash n}w(\lambda)\).
Applying the homotopy theorem of [1] gives the claimed full integral sphere-wedge multiplicity.

**4. Positivity, threshold, and strict growth.** A positive weight requires either at least four distinct sizes, whose minimum total size is \(1+2+3+4=10\), or three distinct sizes with a repeated *interior* size, whose minimum partition is \((3,2,2,1)\) of size eight. Hence \(b_n=0\) for \(n\le7\). For any \(n\ge8\), the partition \((n-5,2,2,1)\) has weight one, so \(b_n\ge1\).

The map \(\lambda\mapsto\lambda\cup\{1\}\) injects partitions of \(n\) into partitions of \(n+1\) and never decreases \(w\): if the original partition has a part of size one, only its smallest-block multiplicity changes and \(w\) stays fixed; otherwise a new smallest size is introduced, and an old smallest repeated block may become an interior contribution, while the nonnegative binomial term cannot decrease. When \(n\ge7\), the source partition \((n-4,2,2)\) has weight zero, whereas its image \((n-4,2,2,1)\) has weight one. Summing the resulting inequalities over all source partitions, with all remaining target partitions contributing nonnegative weights, yields \(b_{n+1}\ge b_n+1\).

**5. Generating series.** For a partition with \(t\ge1\) distinct sizes, one has \(\binom{t-1}{2}=1-t+\binom t2\) (with the ordinary polynomial interpretation at \(t=1,2\)). Summing this baseline over all nonempty partitions is
\[
P(q)\left(1-\sum_{j\ge1}q^j+\sum_{1\le i<j}q^{i+j}\right)-1.
\]
Here marking a present distinct size \(j\) multiplies the partition Euler product by \(q^j\), and marking two distinct sizes \(i,j\) multiplies it by \(q^{i+j}\). To get the actual contribution for \(t\ge3\), subtract one for each *interior* distinct part size occurring exactly once. Fixing such a marked size \(k\) gives precisely
\(q^k(P_{<k}(q)-1)(P_{>k}(q)-1)\): exactly one copy of size \(k\), plus at least one smaller and one larger part, with unrestricted further multiplicities. Finally
\(\sum_{j\ge1}q^j=q/(1-q)\) and \(\sum_{i<j}q^{i+j}=q^3/((1-q)(1-q^2))\).
The announced formal generating-function identity follows. Its coefficients agree term-by-term with the positive weight formula, since \(\binom{t-1}{2}-\#\{\text{singleton interior blocks}\}=\binom{t-2}{2}+\#\{\text{repeated interior blocks}\}\) for \(t\ge3\), and vanish for \(t=1,2\).

## Verification

The standalone, dependency-free program `verify_partition_graph.py` separately (a) constructs transfer graphs from distinct integer partitions without using the theorem's block presentation, (b) enumerates **every clique** and its alternating Euler sum for \(1\le n\le15\), (c) checks the height-descending-link Euler contribution partition by partition for the same range, (d) compares the direct positive partition statistic with the independent published \(1\le n\le25\) Euler table in [3], and (e) expands both sides of the formal generating-function identity through degree 35 and checks the strict growth inequalities on that range. Its output ends with `PASS`. This is finite corroboration; the proof for all \(n\) is the preceding symbolic argument. As further coefficients, it obtains \(b_{26}=4480\), \(b_{30}=13653\), and \(b_{35}=48227\).

## Relationship to prior work

The all-parameter wedge-of-two-spheres theorem and the identification \(b_n=\chi(K_n)-1\) are due to [1] and are **not new claims**. The local line-graph description of the full neighborhood of a partition is in [2]. The numerical study [3] gives clique-count and nerve-count methods, publishes the sequence through \(n=25\), explicitly does not give a closed formula for the Euler characteristic, and poses finding formulas or structural reductions as Problem 6.1 and studying monotonicity as Problem 6.5. The present argument combines a descending-height decomposition with an explicitly counted triangular *subgraph* of the admissibility graph; it yields a direct nonnegative multiplicity statistic, a formal generating series, and a strict all-parameter growth law. A later conceptual synthesis [4] was checked at the accessible abstract level; its full text could not be inspected, so undiscovered equivalent formulas remain a literature risk.

## Limitations

The theorem determines the ordinary nonequivariant integral homotopy type only by combining the new Euler characteristic computation with the previously published sphere-wedge theorem [1]; it does not reconstruct that theorem's full higher-homotopy proof. No assertion is made about equivariant homology, shellability, persistent homology, or a closed elementary asymptotic. The generating function is an infinite Euler-product expression rather than a finite rational function. Checks through finite \(n\) are corroboration, not an all-parameter certificate. Unindexed literature or inaccessible portions of the latest synthesis [4] could contain overlapping results; absence of a retrieved equivalent is not proof of historical uniqueness.

## References

[1] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (first posted 2026-03-15), especially Sections 2, 3, 7, and 8. https://arxiv.org/abs/2603.14370

[2] F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (first posted 2026-03-19), especially Lemmas 3.1–3.2 and Theorem 4.2. https://arxiv.org/abs/2603.18696

[3] F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph: Euler characteristic, clique counts, and sequence data*, arXiv:2603.26656 (first posted 2026-03-27), Sections 3, 5 and Problems 6.1 and 6.5. https://arxiv.org/abs/2603.26656

[4] F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773 (first posted 2026-06-18); accessible abstract only. https://arxiv.org/abs/2606.20773
