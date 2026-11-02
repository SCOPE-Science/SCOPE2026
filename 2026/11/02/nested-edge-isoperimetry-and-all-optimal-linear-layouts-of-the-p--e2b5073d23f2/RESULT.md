# Nested edge-isoperimetry and all optimal linear layouts of the Pappus graph

## Finding

Let \(G\) be the 18-vertex Pappus graph with vertices \(0,\ldots,17\), cycle edges \(\{i,i+1\}\) modulo 18 and additional LCF chords with signed offsets \((5,7,-7,7,-7,-5)^3\). For each integer \(0\leq k\leq18\), put
\[
 b_k=\min_{S\subseteq V(G),\ |S|=k}|\partial_G S|,
 \qquad m_k=\#\{S\subseteq V(G):|S|=k,\ |\partial_G S|=b_k\}.
\]
The complete edge-isoperimetric profile and numbers of minimizers are:

| \(k\) | \(b_k\) | \(m_k\) |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 3 | 18 |
| 2 | 4 | 27 |
| 3 | 5 | 54 |
| 4 | 6 | 126 |
| 5 | 7 | 324 |
| 6 | 6 | 18 |
| 7 | 7 | 108 |
| 8 | 8 | 540 |
| 9 | 7 | 54 |
| 10 | 8 | 540 |
| 11 | 7 | 108 |
| 12 | 6 | 18 |
| 13 | 7 | 324 |
| 14 | 6 | 126 |
| 15 | 5 | 54 |
| 16 | 4 | 27 |
| 17 | 3 | 18 |
| 18 | 0 | 1 |

All eighteen initial segments of the Hamiltonian order \((0,1,\ldots,17)\) attain the corresponding \(b_k\): the Pappus graph is *nested edge-isoperimetric* (also called \(\sigma\)-good). Consequently its minimum linear-arrangement value and cutwidth are, respectively,
\[
\operatorname{MinLA}(G)=99,\qquad \operatorname{cw}(G)=8.
\]
There are **exactly \(31{,}850{,}496\) distinct vertex permutations** attaining the minimum linear-arrangement value 99. These are precisely the permutations for which *every* initial segment is an edge-isoperimetric minimizer.

## Assumptions and scope

The graph is the 18-vertex **point-line incidence (Levi) graph** of the Pappus \((9_3)\) configuration, not the distinct nine-vertex point-collinearity graph. Vertices are individually labelled; optimal orders are counted as permutations, with no identification under rotations, reversal, or graph automorphisms. An edge cut \(\partial_G S\) consists of all edges with exactly one endpoint in \(S\). The minimum linear arrangement is \(\min_\pi\sum_{uv\in E(G)}|\pi(u)-\pi(v)|\), and cutwidth is \(\min_\pi\max_{1\leq k<18}|\partial_G\{\pi^{-1}(1),\ldots,\pi^{-1}(k)\}|\).

## Proof

**Step 1: complete edge-boundary enumeration.** Represent each subset by its 18-bit mask \(M\) and write \(B(M)=|\partial_GM|\). Let \(A_v\) be the 18-bit neighbourhood mask of vertex \(v\). Since the Pappus graph is cubic, for any present vertex \(v\in M\), setting \(N=M\setminus\{v\}\) yields the exact identity
\[
 B(M)=B(N)+3-2|N\cap A_v|,\qquad B(\varnothing)=0.
\]
Indeed the three incident edges contribute three additional outgoing edges minus twice the number of former outgoing edges that become internal. Starting at zero, this recurrence calculates the exact boundary size of **every** one of the \(2^{18}=262{,}144\) subsets. Grouping by cardinality and taking minima, while counting ties, yields the complete displayed \((b_k,m_k)\) table. The short standalone `verify_lcf.py` exhausts every mask using this recurrence and asserts the entire table. The independently written `verify_incidence.py` reconstructs the Pappus point-line incidence graph and directly scans all 27 edges for each mask, obtaining the same table without using the recurrence. The latter checks an explicit isomorphism between the two independently specified graphs.

**Step 2: simultaneous nested minima.** Directly counting the boundary along prefixes of the explicit cyclic LCF order \(0,1,\ldots,17\) gives exactly
\[
 (0,3,4,5,6,7,6,7,8,7,8,7,6,7,6,5,4,3,0),
\]
which equals \((b_0,\ldots,b_{18})\). Thus one order simultaneously realizes every cardinality-constrained minimum.

**Step 3: sharp linear-arrangement and cutwidth values.** For any vertex order \(\pi\), let \(S_k\) be its first \(k\) vertices. Each graph edge \(uv\) is counted in precisely \(|\pi(u)-\pi(v)|\) of the cuts \(\partial_G S_k\). Therefore
\[
 \sum_{uv\in E(G)}|\pi(u)-\pi(v)|
 =\sum_{k=1}^{17}|\partial_G S_k|
 \geq \sum_{k=1}^{17}b_k=99.
\]
Also \(\max_{1\le k<18}|\partial_GS_k|\geq\max_{1\leq k<18}b_k=8\). Both bounds are attained by the explicit cyclic order. Note that the general arrangement lower bound and its equality criterion are classical [2]; this calculation proves that the Pappus graph satisfies the criterion.

**Step 4: exact number of minimum arrangements.** A permutation has arrangement cost 99 if and only if each of its 17 cut sizes equals the corresponding \(b_k\), since each difference \(|\partial_G S_k|-b_k\) is nonnegative and their sum is zero. Define \(F(\varnothing)=1\), and for each nonempty subset \(S\) put
\[
 F(S)=\begin{cases}
 \displaystyle\sum_{v\in S}F(S\setminus\{v\}),&|\partial_GS|=b_{|S|},\\
 0,&\text{otherwise}.
 \end{cases}
\]
By induction on \(|S|\), \(F(S)\) is the number of permissible optimal-prefix orders of \(S\). Exhaustive integer evaluation over all \(2^{18}\) subsets gives
\[
 F(V(G))=31{,}850{,}496.
\]
A second implementation counts the same chains with a *forward-extension* recurrence on the incidence representation, independently confirming the result. No sampling or extrapolation is used.

## Verification

The standalone standard-library Python programs `verify_lcf.py` and `verify_incidence.py` reconstruct their graphs independently, verify 18 vertices and 27 edges, compute every cut, check the complete minimizer multiplicity profile, and calculate the 31,850,496 optimal orderings. Run them separately with `python verify_lcf.py` and `python verify_incidence.py`. Both completed successfully. The `certificate.json` contains the exact finite graph definitions, expected profiles, explicit incidence isomorphism, and comparison values; the executable programs verify those values independently of the certificate. The exhaustive certificate applies to this finite graph only.

## Relationship to prior work

Horton, Parker and Borie [2] defined \(\sigma\)-good graphs and established the **general** implication linking nested edge-isoperimetric cuts to optimal linear arrangement; that general implication is **not** new. Kfoury and Mirzaei [3] and Eikel, Scheideler and Setzer [4] describe established linear-layout objectives and algorithms for other graph classes. Abiad et al. [5], Appendix A, Table A4, explicitly record a value rounding to \(0.78\) for the Pappus graph's scalar edge-isoperimetric *ratio*. This is consistent with the previously known ratio \(b_9/9=7/9\) and is not asserted to be new. The contributions claimed here are specifically the **complete** constrained boundary profile with all minimizer multiplicities, the explicit Pappus-specific nested witness, the sharp layout values, and the exact count of optimal permutations; they are not implied by the lone isoperimetric ratio or by the general nested-graph theorem. MathWorld [1] supplies a classical identification of the 18-vertex Pappus Levi graph and its LCF representation.

## Limitations

The result concerns one canonical finite graph, not all \((9_3)\) configurations, all cubic symmetric graphs, or every toroidal honeycomb graph. Exact exhaustive enumeration is a proof of the stated finite facts but gives no general family theorem. Although targeted searches and comparisons revealed no duplicate of the complete profile, isoperimetric nesting and exact order count, unindexed computations or historical graph-layout tables may exist; historical priority is not independently certified. The general layout implication is credited to prior work.

## References

1. E. W. Weisstein, *Pappus Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/PappusGraph.html
2. S. B. Horton, R. G. Parker, and R. B. Borie, *On minimum cuts and the linear arrangement problem*, Discrete Applied Mathematics 103 (2000), 127–139, doi:10.1016/S0166-218X(00)00173-6. https://doi.org/10.1016/S0166-218X(00)00173-6
3. A. J. Kfoury and S. Mirzaei, *Efficient Reassembling of Graphs, Part 1: The Linear Case*, arXiv:1509.06434 (first posted 2015-09-22). https://arxiv.org/abs/1509.06434
4. M. Eikel, C. Scheideler, and A. Setzer, *Minimum Linear Arrangement of Series-Parallel Graphs*, arXiv:1410.4395 (first posted 2014-10-16). https://arxiv.org/abs/1410.4395
5. A. Abiad et al., *The edge-isoperimetric number of graphs and their powers*, arXiv:2601.17519 (first posted 2026-01-24), Appendix A, Table A4. https://arxiv.org/abs/2601.17519
