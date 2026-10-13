# Cardinality enumerator of connected forcing sets of sunlet graphs
## Finding
For every integer \(n\ge 3\), let \(L_n=C_n\odot K_1\) be the sunlet graph. Label the cycle vertices \(v_0,\ldots,v_{n-1}\), with indices modulo \(n\), and let \(\ell_i\) be the pendant leaf adjacent to \(v_i\). A set \(S\subseteq V(L_n)\) is a connected forcing set exactly in the following three situations.

First, every cycle vertex lies in \(S\), and the leaves in \(S\) are arbitrary. Second, exactly one cycle vertex \(v_i\) is omitted; every selected leaf has its support in \(S\), at least one of the two boundary leaves \(\ell_{i-1}\) and \(\ell_{i+1}\) is selected, and every other leaf supported on a selected cycle vertex is arbitrary. Third, when \(n\ge4\), exactly two consecutive cycle vertices \(v_i,v_{i+1}\) are omitted; every selected leaf has its support in \(S\), both boundary leaves \(\ell_{i-1}\) and \(\ell_{i+2}\) are selected, and every other leaf supported on a selected cycle vertex is arbitrary.

Define
\[
z_c(L_n;j)=\big|\{S\subseteq V(L_n): |S|=j,\ S\text{ is a connected forcing set}\}\big|
\]
and
\[
\Phi_n(x)=\sum_j z_c(L_n;j)x^j.
\]
Then
\[
\Phi_3(x)=x^3(1+x)^3+3x^2\big((1+x)^2-1\big),
\]
while for every \(n\ge4\),
\[
\Phi_n(x)=x^n(1+x)^n+n x^{n-1}\big((1+x)^2-1\big)(1+x)^{n-3}+n x^n(1+x)^{n-4}.
\]
In particular,
\[
Z_c(L_n)=n,
\]
the number of minimum connected forcing sets is \(7\) when \(n=3\) and \(3n+1\) when \(n\ge4\), and the total number of connected forcing sets is \(17\) when \(n=3\) and
\[
2^{n-4}(7n+16)
\]
when \(n\ge4\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The ordinary zero forcing color-change rule is used: a blue vertex with exactly one white neighbor forces that neighbor blue. A connected forcing set is an initial blue set whose induced subgraph is connected and whose zero forcing process colors every vertex. The result concerns the standard sunlet \(C_n\odot K_1\) for every integer \(n\ge3\).

The polynomial \(\Phi_n(x)\) is defined here solely as the cardinality enumerator of connected forcing sets; no claim is made that this notation is standard. The coefficient definition above is the operative definition.

## Proof
Let \(S\) be a connected forcing set. Since \(n\ge3\), a one-vertex set cannot force \(L_n\). Therefore, whenever a leaf \(\ell_i\) belongs to \(S\), its support \(v_i\) also belongs to \(S\); otherwise \(\ell_i\) would be isolated in the induced subgraph \(L_n[S]\). Hence every selected leaf is supported on a selected cycle vertex.

Let \(C=S\cap\{v_0,\ldots,v_{n-1}\}\). If all cycle vertices are in \(C\), then \(S\) is connected, and every unselected leaf is the unique white neighbor of its blue support after all cycle vertices are already blue. Thus every choice of leaves gives a connected forcing set. This is the first family.

Suppose now that at least one cycle vertex is omitted. Connectivity of \(L_n[S]\) implies that \(C\) is a consecutive path on the cycle. Equivalently, the omitted cycle vertices form one consecutive block. Let the length of that omitted block be \(t\ge1\). At either end of the selected path, the boundary cycle vertex has one white cycle neighbor in the omitted block. It can initiate a force into that block exactly when its own pendant leaf is already blue; if its leaf is white, it has two white neighbors and cannot force.

If \(t=1\), a force from either boundary colors the unique omitted cycle vertex. That newly colored vertex then has only its own leaf white and can force it. Thus it is necessary and sufficient that at least one of the two boundary leaves be selected. All other leaves supported on selected cycle vertices are irrelevant to the ability to force and may be chosen arbitrarily. This gives the second family.

If \(t=2\) and \(n\ge4\), one force from only one side is insufficient: the newly colored omitted cycle vertex would still have two white neighbors, namely its own leaf and the other omitted cycle vertex. Hence both boundary cycle vertices must be able to force inward, which is equivalent to selecting both boundary leaves. After the two inward forces, each newly colored cycle vertex can force its own leaf. This gives the third family. When \(n=3\), a two-vertex omitted block leaves only one selected cycle vertex, so two distinct boundary launches are impossible and no third-family set exists.

If \(t\ge3\), even after both possible boundary forces occur, each newly colored end vertex of the omitted block still has two white neighbors: its own leaf and the next omitted cycle vertex. No further force can enter the block, so the process stalls. Thus no other connected forcing set exists.

It remains to count the three disjoint families. The first contributes
\[
x^n(1+x)^n.
\]
For the second, there are \(n\) choices of the omitted cycle vertex. The \(n-1\) selected cycle vertices contribute \(x^{n-1}\). Among the two boundary leaves at least one must be selected, giving \((1+x)^2-1\), while the other \(n-3\) eligible leaves are arbitrary. Hence the contribution is
\[
n x^{n-1}\big((1+x)^2-1\big)(1+x)^{n-3}.
\]
For \(n\ge4\), the third family has \(n\) choices of the consecutive omitted pair, \(n-2\) selected cycle vertices, two mandatory boundary leaves, and \(n-4\) other eligible leaves. Its contribution is
\[
n x^n(1+x)^{n-4}.
\]
For \(n=3\) this family is absent. Adding the contributions proves the stated formulas. The least exponent is \(n\), giving \(Z_c(L_n)=n\). Extracting the coefficient of \(x^n\) gives \(7\) for \(n=3\) and \(3n+1\) for \(n\ge4\). Evaluating at \(x=1\) gives the total counts.

## Verification
The accompanying checker constructs \(L_n\), enumerates every vertex subset for \(3\le n\le9\), independently tests induced connectivity and the zero forcing process, compares the result with the three-family criterion above, and compares every coefficient with the closed formula. It checks \(349{,}504\) subsets in total. The replay result is:

`VERIFY_OK n_range=3..9 subset_checks=349504 criterion_checks=349504 coefficient_checks=91 min_counts=7_then_3n_plus_1 total_counts=17_then_2^(n-4)(7n+16) max_order=18`

This finite computation is a stress test, not the proof for arbitrary \(n\); the proof is the structural argument above.

## Relationship to prior work
The zero forcing process was introduced by the AIM Minimum Rank--Special Graphs Work Group. Connected forcing was subsequently introduced as the restriction in which the initial forcing set is connected.

Brimkov's 2016 work on connected zero forcing proves general structural lemmas for unicyclic graphs and gives a formula and linear-time method for the minimum connected forcing number. In particular, its cycle-segment lemmas are consistent with the fact proved here that a connected forcing set of a sunlet can omit only a short consecutive block of cycle vertices. That work does not give the cardinality distribution of all connected forcing sets of a sunlet, nor does its minimum-number theorem account for the arbitrary leaf choices that create the higher-degree terms of \(\Phi_n(x)\).

Brimkov, Davila, and Schuerger later introduced the notation \(z_c(G;i)\) for counting connected forcing sets of a given size. Their 2025 paper gives complete enumeration results for trees and treats several graph operations, while explicitly listing unicyclic graph families among future directions. Its corona results assume a nontrivial or isolate-free attached graph and therefore do not specialize to \(C_n\odot K_1\). The present result supplies an exact all-size enumeration for a basic unicyclic family.

A 2026 Rice dissertation passage records the scalar equality \(Z_c(L_n)=n\) for sunlet graphs and elsewhere notes qualitatively that certain forcing-set counts for sunlets have polynomial behavior. The scalar equality is therefore not claimed as new. The full dissertation was not retrievable through the access path used for this review; indexed passages did not expose an all-size connected-forcing enumerator. This access limitation is retained as a residual literature risk.

## Limitations
The theorem is specific to the standard one-leaf-per-cycle-vertex sunlet. It does not cover partial sunlets, multiple leaves at a support, longer pendant paths, or arbitrary unicyclic graphs. The formula counts connected forcing sets only; it does not count forcing chronologies or propagation times.

The literature comparison found no prior all-size formula for this family, but one plausible recent dissertation could not be inspected in full. The indexed material from that dissertation was checked and is described above; unseen passages remain a residual originality risk.

## References
1. AIM Minimum Rank--Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. Available online 26 November 2007.
2. B. Brimkov and R. Davila, “Characterizations of the Connected Forcing Number of a Graph,” arXiv:1604.00740 (2016).
3. B. Brimkov, “Complexity and Computation of Connected Zero Forcing,” arXiv:1607.00658 (2016); later *Discrete Applied Mathematics* 229 (2017), 31–45.
4. B. Brimkov, R. Davila, and H. Schuerger, “Connected forcing density and related problems,” arXiv:2507.11194 (2025).
5. B. Brimkov, *Graph Coloring, Zero Forcing, and Related*, Rice University dissertation (2026), indexed passages including Proposition 5.2 on sunlet connected forcing number.
