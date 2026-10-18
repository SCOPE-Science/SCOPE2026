# Packing-domatic coloring polynomials reconstruct independent-set profiles in diameter-two graphs

## Finding

Let \(G\) be any finite connected simple graph of order \(n\ge2\), with \(\operatorname{diam}(G)\le2\). For integers \(1\le k\le n\) and \(t\ge1\), define \(F_{G,k}(t)\) to be the number of maps \(f:V(G)\to\{1,\ldots,t\}\) that are packing \(k\)-domatic colorings. **Each map is counted once, regardless of how many witnessing partitions it admits.**

Let \(i_s(G)\) count independent sets of size \(s\) (including the empty set) and \(m_s(G)\) count inclusion-maximal independent sets of size \(s\). Set \(i_s=m_s=0\) for out-of-range indices and \(m_0=0\). Write \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\), with \((x)_{\underline0}=1\), and let \((q)_{\underline r}=0\) for integers \(0\le q<r\).

**Theorem (complete counting law).** For every \(1\le k\le n\) and \(t\ge1\),
\[
\boxed{F_{G,k}(t)=\sum_{r=k}^{n}i_{n-r}(G)(t-1)_{\underline r}
 +m_{n-k+1}(G)(t-1)_{\underline{k-1}}.}
\]
This is a polynomial identity in the integer variable \(t\), expressed in the falling-factorial basis. It counts the entire family of feasible maps, not just optimal ones.

**Recovery.** The coefficients of \((t-1)_{\underline r}\) in \(F_{G,1}(t)\) recover \(i_{n-r}(G)\) for \(1\le r\le n\). Since a connected nontrivial graph has \(i_n=0\), this recovers the independence polynomial. For each \(2\le k\le n\), the coefficient of \((t-1)_{\underline{k-1}}\) in \(F_{G,k}(t)\) equals \(m_{n-k+1}(G)\). Since \(m_0=m_n=0\), all maximal-independent-set cardinality counts are recovered as well.

**Exact optima.** Let \(\alpha=\alpha(G)\) and \(\tau=n-\alpha\). Write \(\chi_{\rho,k}(G)\) for the smallest permitted value of \(t\), and \(N_k(G)=F_{G,k}(\chi_{\rho,k}(G))\) for the number of optimal maps. Then
\[
(\chi_{\rho,k}(G),N_k(G))=
\begin{cases}
(\tau+1,\ m_{\alpha}(G)\tau!), &1\le k\le\tau+1,\\
(k,\ m_{n-k+1}(G)(k-1)!), & k>\tau+1\ \text{and}\ m_{n-k+1}(G)>0,\\
(k+1,\ i_{n-k}(G)k!),& k>\tau+1\ \text{and}\ m_{n-k+1}(G)=0.
\end{cases}
\]
The first line specializes, when \(k=1\), to the already known diameter-two packing chromatic number \(n-\alpha(G)+1\); **that numerical specialization is not a novelty claim**.

## Assumptions and scope

Graphs are finite, undirected, connected, loopless, simple and have at least two vertices. Distance is graph-geodesic distance. A packing coloring \(f:V(G)\to\{1,\ldots,t\}\) requires that distinct vertices sharing color \(j\) are at distance greater than \(j\). It is packing \(k\)-domatic when there is a partition \(V(G)=A_1\sqcup\cdots\sqcup A_k\) into \(k\) nonempty blocks such that, for each vertex \(v\) and each block \(A_h\), some \(w\in A_h\) satisfies \(d_G(v,w)\le f(w)\). The sets \(A_h\) are broadcast dominating relative to \(f\); the blocks are not coloring classes. Colors may be unused. The counting polynomial counts labeled vertex-color maps, not color permutations or witness partitions. No condition of minimum degree beyond connectedness is imposed. For \(k>n\), no nonempty partition is possible, so only \(1\le k\le n\) is considered.

## Proof

**Lemma (unique obstruction to a broadcast partition).** Fix a packing map \(f\). Let \(I=f^{-1}(1)\) and \(r=n-|I|\). Then \(I\) is independent and the \(r\) vertices outside \(I\) receive pairwise distinct colors at least \(2\), because any two distinct vertices of \(G\) are at distance at most \(2\). Each outside vertex, by itself, broadcasts to all vertices of \(G\). Hence if \(r\ge k\), distribute the \(r\) such vertices among \(k\) nonempty blocks, and place all vertices of \(I\) arbitrarily: every block is broadcast dominating.

Conversely, suppose the map has a witnessing partition and \(r<k\). At least one block \(B\) contains no vertex outside \(I\); its members all have color \(1\). For each \(u\in I\setminus B\), every vertex of \(B\) has distance at least \(2\) from \(u\), contradicting broadcasting at radius \(1\). Thus \(B=I\) (in particular, \(I\ne\varnothing\)). This block must dominate every vertex, since it is broadcast dominating with only radius-one sources; equivalently, \(I\) is an inclusion-maximal independent set. There can be at most one such rootless block, since two disjoint rootless blocks would both equal nonempty \(I\). Thus \(k-r=1\), or \(r=k-1\). Conversely, if \(r=k-1\) and \(I\) is inclusion-maximal independent, \(I\) is a dominating block and each of the \(r\) other singleton vertices broadcasts to all of \(G\). These \(k\) blocks witness feasibility. The lemma follows, including the boundary \(I=\varnothing\), where only \(r\ge k\) can apply.

**Counting.** For each independent set \(I\) of size \(n-r\), the remaining \(r\) labeled vertices can receive distinct colors from \(\{2,\ldots,t\}\) in exactly \((t-1)_{\underline r}\) ways. The lemma partitions admissible maps into the disjoint cases \(r\ge k\) (arbitrary independent \(I\)) and \(r=k-1\) (maximal independent \(I\)); their sum is precisely the boxed formula. Multiplicity of witnessing partitions plays no role because \(I=f^{-1}(1)\) is unique.

**Recovery.** Falling factorials of distinct degrees are linearly independent. In \(F_{G,1}\), the coefficient of degree-index \(r\ge1\) is \(i_{n-r}\), since \(m_n=0\). In \(F_{G,k}\) for \(k\ge2\), the index \(k-1\) appears only in the extra maximal-independent-set term because the other sum begins at \(r=k\). This gives the two stated profiles.

**Optima and their multiplicities.** An independent set has at most \(\alpha\) vertices, so \(r\ge\tau\) in every packing map. If \(k\le\tau+1\), the smallest possible palette is \(t=\tau+1\): select a largest independent set for color \(1\) and injectively color its \(\tau\) remaining vertices; feasibility follows either from \(r\ge k\) or from maximality with \(r=k-1\). Conversely, any map with fewer colors cannot color \(\tau\) high-color vertices distinctly. At this palette, all feasible maps arise from a largest independent set, and number \(m_\alpha\tau!\).

If \(k>\tau+1\), then any feasible map has at least \(k-1\) high-color vertices, so \(t\ge k\). At \(t=k\), feasibility forces exactly \(r=k-1\), with a maximal independent color-one set of order \(n-k+1\); hence such maps exist exactly when \(m_{n-k+1}>0\), and their number is \(m_{n-k+1}(k-1)!\). Otherwise \(t=k+1\) is sufficient: choose any independent set of size \(n-k\), which exists since \(n-k<\alpha\), and injectively give its \(k\) complementary vertices the \(k\) high colors. There are exactly \(i_{n-k}k!\) such maps at this palette. This completes all branches of the optimum formula.

**Illustrative boundary.** For the complete multipartite graph with parts of orders \(2,4,8\), all maximal independent sets are complete parts, so only their sizes \(2,4,8\) occur. Here \(n=14\), \(\tau=6\); the exact chromatic sequence has both plateaus and two-step increases: \(\chi_{\rho,7}=7\), \(\chi_{\rho,8}=9\), \(\chi_{\rho,10}=11=\chi_{\rho,11}\), and \(\chi_{\rho,12}=13=\chi_{\rho,13}\). Thus the maximal-independent-set spectrum, not just the independence number, controls the higher domatic levels.

## Verification

The standalone Python 3 checker `verify_full.py` independently constructs labeled graphs of diameter at most two, enumerates every allowed vertex coloring from palettes of sizes \(1\) through \(n+1\), tests the packing constraint via all-pairs graph distances, and tests the existence of a broadcasting partition using exhaustive set partitions. It independently enumerates independent and maximal independent sets for the predicted counts. The direct check does not use the lemma to decide whether a coloring is admissible. It confirmed exactly \(1,594\) graph-palette-partition-count comparisons on \(65\) labeled graphs (all qualifying orders \(2,3,4\), and a deterministic sample of \(34\) graphs of order \(5\)), considering \(440,702\) raw color assignments before packing filtering. Execute `python3 verify_full.py`; `verification_output.txt` records the actual result. This finite corroboration does not prove the theorem for general order; the argument above does.

## Relationship to prior work

Brešar, Ferme and Hu (2026; arXiv:2610.03477, first submitted 2026-10-02) introduced packing \(k\)-domatic colorings and determined several minimum-value regimes on paths and cycles; their available abstract also states global results for \(k=2,3\). Their complete preprint was not accessible for full-text comparison, so exact overlap within it cannot be ruled out. The present statement addresses the *number of all color maps at every palette size* and the reconstruction of both independent-set profiles on arbitrary graphs of diameter at most two, not solely chromatic minima.

Goddard, Hedetniemi, Hedetniemi, Harris and Rall (2008) introduced broadcast/packing coloring, and Brešar and Mesarič Štesl (2022, Proposition 7.1 citing Goddard et al.) record \(\chi_\rho(G)=n-\alpha(G)+1\) for graphs of diameter two. That numeric equality is prior work and follows here only as a specialization. The inspected 2022 Section 7 concerns packing coloring games and does not introduce the \(k\)-domatic partitions or derive the all-level counting identity.

## Limitations

The polynomial is an exact identity, but it may not be computationally easy to evaluate for arbitrary input graphs, since its coefficients include independent-set counts. The result is limited to finite connected graphs of diameter at most two and the ordinary sequence of packing radii equal to their color labels. All counts distinguish vertex labels and numeric color labels, but not witness partitions. The motivating preprint's abstract was available, whereas its complete text was not, leaving a material literature-overlap risk; historical terminology may hide equivalent results. The proof is mathematical, not an external formal or independent audit.

## References

1. B. Brešar, J. Ferme and W. Hu, *Partitioning an \(S\)-packing coloring into broadcast dominating sets*, arXiv:2610.03477 (2026), first submitted 2026-10-02. https://arxiv.org/abs/2610.03477
2. B. Brešar and D. Mesarič Štesl, *The Competition-Independence Game with Prevention*, Filomat 36(18) (2022), 6197–6213. https://doi.org/10.2298/FIL2218197B
3. W. Goddard, S. M. Hedetniemi, S. T. Hedetniemi, J. M. Harris and D. F. Rall, *Broadcast Chromatic Numbers of Graphs*, Ars Combinatoria 86 (2008), 33–49. https://combinatorialpress.com/ars-articles/volume-086-ars-articles/broadcast-chromatic-numbers-of-graphs/
