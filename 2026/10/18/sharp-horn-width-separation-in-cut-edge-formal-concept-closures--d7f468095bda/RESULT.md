# Sharp Horn-width separation in cut-edge formal concept closures

## Finding
For each integer \(n\ge4\), let \(E=\binom{[n]}{2}\), let the objects be the distinct cuts \(\delta(S)\subseteq E\), and let an object be incident to an edge precisely when that edge crosses its cut. Let \(c_n\) be the attribute-closure operator of this finite formal context. Define \(i_n\) (respectively, \(d_n\)) as the smallest possible maximum premise size in a sound and complete implicational basis using repeated forward chaining (respectively, one simultaneous application of all rules).

The exact sharp widths are
\[
 i_n=3,\qquad d_n=2\left\lfloor\frac{n-2}{2}\right\rfloor+1=\begin{cases}n-1,&n\text{ even},\\n-2,&n\text{ odd}.\end{cases}
\]
In particular, the iterative optimum is constant, but the direct optimum grows linearly with the number of vertices. An explicit ternary iterative basis and exact one-pass lower-bound witnesses are given below.

## Assumptions and scope
Let \(V=[n]\), with \(n\ge4\), and \(E\) the unordered pairs of distinct elements of \(V\). For \(S\subseteq V\), write \(\delta(S)=\{\{u,v\}\in E:|\{u,v\}\cap S|=1\}\). Since \(\delta(S)=\delta(V\setminus S)\), treat equal cuts as one object, including the empty cut. The formal context has object set \(\{\delta(S):S\subseteq V\}\), attribute set \(E\), and relation \(C I e\) when \(e\in C\).

For \(F\subseteq E\), put
\[
 c_n(F)=\bigcap_{F\subseteq C,\,C\text{ a cut}} C,
\]
interpreting the intersection of no cuts as \(E\). A Horn rule \(A\to B\) has finite premise \(A\subseteq E\) and conclusion \(B\subseteq E\), and is *sound* when \(B\subseteq c_n(A)\). A basis generates \(c_n\) when the common rule-closed hull is \(c_n(F)\) for every \(F\). Its iterative width is the largest \(|A|\) among its rules. For a *direct* (single-pass) basis, \(c_n(F)=F\cup\bigcup_{A\subseteq F}(B:A\to B\text{ is a rule})\) holds for every \(F\). The relevant optimum takes the minimum maximum width over all sound complete bases of the specified kind; empty or unit conclusions are allowed, so the bounds do not depend on requiring singleton conclusions.

## Proof
**1. Closure normal form.** A cut contains every edge of \(F\) if and only if the graph \(([n],F)\) is bipartite, since its two color classes then determine the cut. If \(F\) is nonbipartite, no such cut exists and \(c_n(F)=E\). If \(F\) is bipartite, independently choose the orientation of the unique bipartition in each nontrivial connected component. For an edge \(uv\), both orientations of its endpoints are forced to differ in every such coloring precisely when \(u,v\) belong to the same connected component and have opposite bipartition colors. Thus \(c_n(F)\) is the disjoint union of the complete bipartite graphs across the two classes of every connected component of \(([n],F)\); isolated vertices contribute nothing. Equivalently, an unpresent edge \(uv\) is forced by a consistent \(F\) exactly when \(F\) contains an odd-length \(u\)-to-\(v\) path.

**2. Ternary rules suffice for iteration.** Put in the basis each rule
\[
 \{ab,bc,cd\}\longrightarrow\{ad\}
\]
for four pairwise distinct vertices \(a,b,c,d\), and each rule
\[
 \{ab,bc,ca\}\longrightarrow E
\]
for three pairwise distinct vertices \(a,b,c\). Here \(ab\) denotes the unordered edge \(\{a,b\}\). The first rule is sound because a cut separating each successive pair along a three-edge path must separate its endpoints. The second is sound because no cut can cross every edge of a triangle.

Starting from bipartite \(F\), any forced edge has endpoints connected by an odd simple path of length \(2k+1\). Induct on \(k\): if the length exceeds one, a three-edge initial segment can be replaced by the edge joining its endpoints, shortening the path by two. The first family therefore derives every forced edge. Starting from nonbipartite \(F\), take an odd cycle; if its length is at least five, the same shortcut replaces three consecutive edges by one and produces a shorter odd cycle. Repeating yields a triangle, activating a rule of the second family and deriving all \(E\). Every rule is sound, so no unforced edge can be derived. This proves \(i_n\le3\).

For the reverse inequality, take precisely the three successive edges of a four-vertex path. They force the edge between its endpoints, but every subset of this three-edge premise of cardinality at most two is closed: its graph consists of isolated edges and/or a length-two path, each already a complete bipartite component. Therefore no sound rule of arity at most two can add any edge on its first firing; nor can any later rule fire to enlarge the set. Hence \(i_n\ge3\).

**3. Optimal one-pass upper bound.** Let \(D=2\lfloor(n-2)/2\rfloor+1\), the largest odd integer not exceeding \(n-1\). Include every singleton-conclusion sound rule \(A\to\{e\}\) with \(|A|\le D\). This is a direct basis. Indeed, if \(F\) is bipartite, any \(e\in c_n(F)\setminus F\) has an odd simple path in \(F\), whose length is an odd number at most \(n-1\), hence at most \(D\). The edges of that path form the required premise \(A\).

If \(F\) is nonbipartite, choose a shortest odd cycle. Its length is at most \(n\). Unless \(n\) is odd and this cycle is Hamiltonian, its length is at most \(D\), so its edges form a premise implying every \(e\in E\). In the exceptional case, \(n\) is odd, the shortest odd cycle has all \(n\) vertices, and \(D=n-2\). Every edge \(e\notin F\) is a chord of that Hamiltonian odd cycle. Its endpoints partition the cycle into two arcs of opposite parity; the odd arc has length at most \(n-2=D\) because the endpoints are not consecutive on the cycle. The edges of that arc imply \(e\). Edges already belonging to \(F\) require no implication. This proves \(d_n\le D\).

**4. Optimal one-pass lower bound.** Choose an odd cycle on exactly \(D\) vertices and at least one vertex \(w\) outside that cycle; such a vertex exists because \(D\le n-1\). Let \(F\) comprise exactly the \(D\) cycle edges, and let \(e\) connect \(w\) to any cycle vertex. Since \(F\) is nonbipartite, \(e\in c_n(F)\), but \(e\notin F\). Any proper subset \(A\subsetneq F\) is a bipartite forest, with \(w\) in an isolated component, so \(e\notin c_n(A)\). In a sound direct basis, some rule deriving \(e\) in one pass from \(F\) must consequently have its premise equal to all \(F\), of cardinality \(D\). Hence \(d_n\ge D\), proving both exact formulas.

**5. Closed-set classification, as a known enumerative context.** The normal form also shows that, apart from the inconsistent top set \(E\), closed attribute sets correspond bijectively to set partitions of \([n]\) whose blocks of size at least two carry unordered nontrivial bipartitions. The weight of a block of size \(s\) is \(w_1=1\), and \(w_s=2^{s-1}-1\) for \(s\ge2\). The number of closed sets is therefore
\[
 1+\sum_{\pi\in\Pi_n}\prod_{B\in\pi}w_{|B|}.
\]
The exponential generating function of the sum without the initial \(1\) is \(\exp((e^{2x}-2e^x+2x+1)/2)\). This sequence and generating function are *already recorded* as OEIS A307389, with related primary enumeration in Nijholt–Sieben–Swift; no originality claim is made for this enumeration.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. The checker independently enumerates every cut and every possible edge premise for \(n=4,5,6\), compares the Galois closure against the bipartite-component rule, checks repeated application of all ternary rules, and exhaustively tests the claimed one-pass upper width. It checks the lower-bound odd-cycle witness through \(n=9\), and the closed-set count for \(n=4,5,6\). Its successful terminating output is `VERIFY_OK`. The computation is finite corroboration; Steps 1–4 above prove the unbounded statements.

## Relationship to prior work
The distinction between iterative and direct implicational bases is established, including in Adaricheva–Ninesling (2018). Rawson et al. (2023) describe general hypergraph intersection structures via concept lattices. These general results do not supply this cut-edge instance's exact width function or the ternary-versus-growing-width separation.

The auxiliary closed-set count is **not new**: its coefficient sequence exactly matches OEIS A307389, and the same EGF occurs in the tagged-polydiagonal enumeration of Nijholt–Sieben–Swift (2022). The numerical count is included only to locate the example in known enumerative mathematics. The genuinely assessed assertion is the sharp pair \((i_n,d_n)\) for this specified closure operator, with explicit matching bases and lower-bound witnesses.

## Limitations
The result concerns complete-graph edge attributes with all binary cuts as objects, not arbitrary host graphs or hypergraph cuts. It determines the minimum maximum premise width, not the minimum number of rules. Equivalent Horn presentations using parity constraints or signed-partition terminology could have appeared elsewhere; publication priority is not independently certified. Computational checks cover bounded sizes and are not infinite proofs. The known closed-set enumeration is expressly excluded from the novel contribution.

## References
- K. Adaricheva and T. Ninesling, *Direct and Binary Direct Bases for One-set Updates of a Closure System*, first arXiv version 19 October 2018, https://arxiv.org/abs/1810.08684.
- M. G. Rawson, A. Myers, R. Green, M. Robinson and C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, first arXiv version 21 July 2023, https://arxiv.org/abs/2307.11681.
- E. Nijholt, N. Sieben and J. W. Swift, *Invariant Synchrony and Anti-Synchrony Subspaces of Weighted Networks*, arXiv v1 31 May 2022, https://arxiv.org/abs/2206.00094; tagged-partition enumeration, Section 7.
- OEIS A307389, https://oeis.org/A307389, matching coefficient sequence and EGF (recorded in 2019).
