# Roman domination weight polynomials of thin and thick spiders with arbitrary heads

## Finding

Let \(H\) be an arbitrary finite simple graph with \(r\) vertices and Roman domination polynomial \(R_H(z)\). For each \(n\ge 2\), form a **thin spider** from a clique \(C=\{c_1,\ldots,c_n\}\), an independent set \(S=\{s_1,\ldots,s_n\}\), and \(H\): each core vertex is adjacent to every vertex of \(H\), no foot is adjacent to \(H\), and \(s_i\) is adjacent to \(c_i\) alone. In a **thick spider**, instead \(s_i\) is adjacent to all core vertices other than \(c_i\). The edges within \(H\) are arbitrary.

Set
\[
Q=1+z+z^2,\quad B=1+z,\quad D=z(1+z)^2,\quad X=z^2Q,\quad E=BQ,\quad T=R_H(z).
\]
Then the weight polynomial of the thin spider is exactly
\[
\boxed{R_{\mathrm{thin}_n(H)}(z)=Q^r\big((X+D)^n-D^n\big)+(T-z^r)D^n+z^r(2z^2+z^3)^n.}
\]
For the thick spider put
\[
K_n(z)=B^n\big((z+z^2)^n-z^n-nz^{n+1}\big)+nz^{n+2}B^{n-1}+z^{2n}.
\]
Its weight polynomial is exactly
\[
\boxed{R_{\mathrm{thick}_n(H)}(z)=Q^r\big(Q^{2n}-E^n-nz^2E^{n-1}\big)+(T-z^r)D^n+z^rK_n(z).}
\]
Consequently, for either spider type, **the full weight distribution depends on its head only through the head's order and Roman polynomial**. These explicit transformations, together with the union and join rules below, give a finite exact coefficient-computing recursion for every \(P_4\)-sparse graph from its standard decomposition. The known algorithms for finding the minimum weight and the general existence of bounded-clique-width counting algorithms are not claimed as new.

## Assumptions and scope

A **Roman dominating function** of a finite simple graph \(G\) is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex carrying \(0\) is adjacent to at least one vertex carrying \(2\). Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\); the polynomial is \(R_G(z)=\sum_{f\text{ Roman dominating}} z^{w(f)}\), with labels and vertices distinguished. For the empty graph use \(R_\varnothing(z)=1\); a singleton has \(R_{K_1}(z)=z+z^2\). All identities hold in \(\mathbb Z[z]\), including when \(H\) is empty or disconnected. Here the two kinds of *spider* are the clique-and-feet graphs of the standard \(P_4\)-sparse decomposition, not trees with multiple arms.

For two vertex-disjoint graphs \(G\) and \(J\), of orders \(a\) and \(b\), respectively, the rules are
\[
R_{G\sqcup J}(z)=R_G(z)R_J(z),
\]
\[
\begin{split}
R_{G\vee J}(z)={}&z^{a+b}+(R_G(z)-z^a)(1+z)^b\\
&+(R_J(z)-z^b)(1+z)^a\\
&+\big(Q^a-(1+z)^a\big)\big(Q^b-(1+z)^b\big).
\end{split}
\]
The notation \(G\vee J\) means adding every cross edge between \(G\) and \(J\).

## Proof

**Union and join.** A labeling on a disjoint union is Roman dominating if and only if its restrictions to both components are. For a join, classify labelings by which side contains at least one label \(2\). If neither side has one, the only Roman labeling is all ones, of weight \(a+b\). If only \(G\) contains a \(2\), the \(G\)-restriction must itself be Roman dominating, and every vertex of \(J\) can independently carry \(0\) or \(1\); the contribution is \((R_G-z^a)B^b\). Interchanging sides gives the next term. If both contain a \(2\), every zero sees a two across the join, so arbitrary labelings containing a two on each side contribute \((Q^a-B^a)(Q^b-B^b)\). This proves the join identity, also when either input is empty.

**Thin spiders.** Partition Roman labelings into three mutually exclusive classes. (i) At least one core vertex has label \(2\). Then every head vertex (including any zero) is defended by that core vertex. For each index \(i\), either \(c_i=2\) and \(s_i\in\{0,1,2\}\), contributing \(X=z^2Q\), or \(c_i\in\{0,1\}\) and the sole neighbor of the foot is not two, forcing \(s_i\in\{1,2\}\), contributing \(D=(1+z)(z+z^2)\). Excluding the choice with no core two and freely labeling the head gives \(Q^r((X+D)^n-D^n)\). (ii) No core two but at least one head two. Every foot must have positive label and every core is free to carry zero or one because a head two defends it. The head restriction must itself be Roman dominating because its zero vertices have no core two. The contribution is \((T-z^r)D^n\): the only Roman labeling of \(H\) containing no two is the all-one labeling of weight \(r\). (iii) Neither core nor head contains a two. Every head vertex must be one. Each core-foot pair must be one of \((0,2),(1,1),(1,2)\), contributing \(2z^2+z^3\). Adding the disjoint contributions gives the displayed thin identity.

**Thick spiders.** Make the same partition. (i) At least one core two. The head has no restriction, contributing \(Q^r\). Every zero on a core is automatically defended by a different core carrying two. A zero at foot \(s_i\), however, requires a core two at an index different from \(i\). Starting from all \(Q^{2n}\) core-foot labelings, subtract those with no core two, giving the subtraction \(E^n\) because a non-two core carries zero or one while its foot is unrestricted. The only other forbidden assignments have exactly one core two at \(i\) and \(s_i=0\), contributing \(nz^2E^{n-1}\). Thus class (i) gives \(Q^r(Q^{2n}-E^n-nz^2E^{n-1})\). (ii) No core two but at least one head two gives \((T-z^r)D^n\), just as before. (iii) No two in head or core. The head is all ones; every foot must be positive. Let \(t\) count the feet carrying two. If \(t\ge2\), every core is free to be zero or one; the contribution is \(B^n((z+z^2)^n-z^n-nz^{n+1})\). If \(t=1\), the one foot two is nonadjacent to its matching core, so this core must be one, and all other cores are free; the contribution is \(nz^{n+2}B^{n-1}\). If \(t=0\), every core must be one, giving \(z^{2n}\). These are all possibilities, proving the thick identity.

**Composition and head substitution.** The classical decomposition theorem for \(P_4\)-sparse graphs states that a nontrivial graph is disconnected, or its complement is disconnected, or it is a thin/thick spider with a smaller recursively decomposable head. Thus the displayed union, join, and spider formulas, started at the empty graph and isolated vertex, recursively determine every coefficient. In the spider formulas, only \(r\) and \(R_H\) occur. Consequently two heads of the same order with the same Roman weight polynomial have identical weight polynomials under either spider operation, regardless of their distinct internal edges. No numerical sampling is required in the proof.

**Extremal consistency check.** Substituting the empty head gives minimum nonzero degree \(n+1\) with coefficient \(n\) for the thin spider, and minimum degree \(3\) with coefficient \(n\) for the thick spider (\(n\ge2\)). The minimum degrees agree with previously published Roman-domination results; the full-coefficient formulas are the claim here.

## Verification

The accompanying standalone `verification.py` builds graphs independently from labelled edge lists and enumerates every map to \(\{0,1,2\}\), testing its zeros against neighboring twos. It compares the complete coefficient vector against the recurrence in exact integer arithmetic. Across 264 instances with both spider types, arbitrary test heads and nested join/union compositions of up to eleven vertices, it checked 8,244,702 labelled functions. All coefficient checks passed. Sixteen additional headless-spider minimum-degree/count tests for \(2\le n\le9\) passed. Run `python verification.py`; the expected output is embedded as `verification_output.txt`. These tests are corroboration, not the logical basis of the unrestricted theorem.

## Relationship to prior work

Das and Santra's 2026 preprint on Roman domination of \(P_4\)-tidy graphs gives exact minimum-weight computations and explicitly discusses thin/thick spiders and heads. Its spider minimum formulas and known structural decompositions are prior work; its examined treatment does not provide the full weight-polynomial identities above. Abu-Khzam, Fernau and Mann's 2023 Roman census studies **minimal** Roman dominating functions; minimality under the pointwise ordering is a stricter combinatorial condition than the all-functions polynomial counted here. General weighted counting results for bounded clique-width cover the *possibility* of polynomial-time computation; they do not supply the explicit universal two-statistic head-substitution formulas, which are the mathematical contribution. Previous complete-multipartite and chain-graph Roman polynomials likewise concern different graph families. The general join identity follows directly from elementary label classification and is stated as a tool, not claimed in isolation as novel.

## Limitations

All statements concern ordinary Roman domination on finite simple graphs; variants such as Roman \(\{2\}\) domination, total Roman domination, and domination by selected sets are not covered. The recursive computation presupposes a valid \(P_4\)-sparse decomposition, whose existence is a published result, not proved anew here. The proof provides explicit polynomial identities, not a claim of optimal implementation complexity. No independent review has been performed. Some unindexed or inaccessible specialized literature could predate this particular polynomial presentation; absolute bibliographic priority is not established.

## References

- G. K. Das and K. Santra, *Roman Domination on Circular-Convex, Triad-Convex Bipartite Graphs and \(P_4\)-Tidy Graphs*, arXiv:2609.19240v1 (first publicly dated July 21, 2026). Sections on spider decomposition and Roman domination.
- F. N. Abu-Khzam, H. Fernau and A. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, MFCS 2023, DOI:10.4230/LIPIcs.MFCS.2023.6.
- T. Kotek and J. A. Makowsky, *Efficient Computation of Generalized Ising Polynomials on Graphs with Fixed Clique-Width*, arXiv:1505.06617. General expressive-power and algorithmic context, not an explicit spider formula.
- B. Jamison and S. Olariu, *Recognizing \(P_4\)-sparse graphs in linear time*, SIAM Journal on Computing (1992), DOI:10.1137/0221027. Structural decomposition context.
