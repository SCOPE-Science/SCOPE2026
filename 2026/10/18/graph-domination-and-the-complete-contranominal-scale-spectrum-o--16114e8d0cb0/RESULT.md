# Graph domination and the complete contranominal-scale spectrum of complementary incidence lattices

## Finding
For every finite simple undirected graph \(G=(V,E)\) with \(n=|V|\ge 1\), define the **complementary edge–vertex context** \(\mathbb K_G=(E,V,I)\) by
\[
eIv\quad\Longleftrightarrow\quad v\notin e.
\]
A reduced contranominal scale of order \(k\ge1\) is a pair of \(k\)-element sets of distinct objects and attributes whose restricted incidence matrix has precisely a zero diagonal and ones elsewhere, up to simultaneous relabeling. Let \(s_k(G)\) be the number of such pairs, counting each unordered pair of selected object and attribute sets once. With \(s_0(G)=1\), define \(S_G(z)=\sum_{k=0}^{n}s_k(G)z^k\).

**Theorem.** For every such graph,
\[
\boxed{S_G(z)=\sum_{A\subseteq V}z^{|A|}\prod_{v\in A}|N_G(v)\cap(V\setminus A)|.}\tag{1}
\]
In particular, the maximum nonzero exponent is \(n-\gamma(G)\), where \(\gamma(G)\) is the ordinary domination number, counting a vertex as dominating itself. Consequently, the largest Boolean lattice that order-embeds in the concept lattice \(\mathfrak B(G)\) is \(\mathbf2^{n-\gamma(G)}\), in the sense of Boolean sub**orders**, and
\[
|\mathfrak B(G)|\ge 2^{n-\gamma(G)}.\tag{2}
\]
The decision problem whether \(\mathfrak B(G)\) contains a Boolean suborder with at least \(2^k\) elements is NP-complete, with \(k\) part of the input.

The exact scale polynomial is multiplicative under disjoint unions. For \(m\ge1\) and \(n\ge2\), respectively,
\[
S_{K_{1,m}}(z)=(1+z)^m+mz,
\qquad
S_{K_n}(z)=\sum_{k=0}^{n-1}\binom nk(n-k)^kz^k.\tag{3}
\]
If \(G\) has a universal vertex and at least two vertices, then equality in (2) holds if and only if \(G\) is a star (for the two-vertex case \(K_2=K_{1,1}\)).

For paths \(P_n\), \(n\ge1\), and cycles \(C_n\), \(n\ge3\), the entire polynomial has a uniform four-state transfer matrix. Order the binary states as \((0,0),(0,1),(1,0),(1,1)\) and set
\[
T(z)=\begin{pmatrix}0&z&0&0\\0&0&1&1\\z&2z&0&0\\0&0&1&1\end{pmatrix}.
\]
Then, with \(a=(1,1,0,0)\) and \(b=(1,0,1,0)^\top\),
\[
\boxed{S_{P_n}(z)=aT(z)^n b,\qquad S_{C_n}(z)=\operatorname{tr}(T(z)^n).}\tag{4}
\]
Since \(T^4=T^3+2zT^2+z^2T\), each sequence obeys the third-order recurrence \(F_{n+3}=F_{n+2}+2zF_{n+1}+z^2F_n\) whenever all displayed terms lie in its stated domain. Both polynomials have degree \(\lfloor2n/3\rfloor\). For the random graph \(G\sim G(n,p)\) with independent edge probability \(p\),
\[
\boxed{\mathbb E[S_G(z)]=\sum_{k=0}^{n-1}\binom nk((n-k)p)^k z^k.}\tag{5}
\]
This last equality concerns expectations, not concentration or individual instances.

## Assumptions and scope
Graphs are finite, simple, undirected and may have isolates or disconnected components. Here \(N_G(v)\) is the open neighbor set. The concept lattice has the standard derivation-based order; a Boolean **suborder** means an order-embedded copy of a Boolean lattice, not necessarily a sublattice whose joins and meets coincide with ambient lattice operations. Scales count selected sets of object edges and attribute vertices, **not** the number of distinct Boolean suborders. The polynomial's constant term is defined to be one by the empty selection convention, even if the context has no objects.

## Proof
**Step 1: exact scale count.** Let \(A\subseteq V\) be the chosen attributes and let \(D=V\setminus A\). In a contranominal matrix, each selected object must fail incidence with precisely one of the selected attributes. The object is an edge, so its two endpoints must contain that unique attribute \(v\in A\), and its other endpoint must belong to \(D\). Conversely, choosing for each \(v\in A\) any edge joining \(v\) to \(D\) gives the required matrix: for different \(v\), the selected edges are automatically distinct, and each selected edge is incident with exactly one chosen attribute. There are precisely \(\prod_{v\in A}|N_G(v)\cap D|\) such selections, with canonical matching between absent incidences and attributes. This proves (1) without overcounting permutations.

A factor in this product is positive exactly when every vertex outside \(D\) has a neighbor in \(D\); since each vertex in \(D\) dominates itself, this is precisely the condition that \(D\) be a dominating set. Hence the largest possible \(|A|\) equals \(n-\gamma(G)\). The classical contranominal-scale criterion for Boolean suborders of concept lattices [1,2] transfers this maximum to the stated Boolean rank. An embedded copy of \(\mathbf2^{n-\gamma(G)}\) contains \(2^{n-\gamma(G)}\) distinct elements, proving (2). Given \(G,k\), a scale (or dominating set of size at most \(n-k\)) is a polynomially verifiable certificate. Dominating-set decision reduces by \((G,t)\mapsto(G,n-t)\), proving NP-completeness. This is a reduction from the established NP-complete domination problem, not a new complexity result about domination itself.

**Step 2: structural formulas.** For disjoint components, crossing-edge choices factor vertex by vertex and hence \(S_{G\sqcup H}=S_G S_H\). In a complete graph every outside vertex has \(n-k\) chosen-side neighbors, giving the second formula in (3). For the star, when the hub belongs to \(D\), every selected leaf has one crossing edge, contributing \((1+z)^m\); if the hub belongs to \(A\), the only admissible \(A\) is the singleton hub, and the hub has \(m\) crossing-edge choices. This proves the first formula in (3).

For any graph with universal vertex \(u\), the spoke edges form a star spanning all vertices. Each subset of the other \(n-1\) attribute vertices missing at least one leaf is a closed intent in the full context: some set of spoke objects witnesses its exact closure; the top intent is all of \(V\). These \(2^{n-1}\) intents remain distinct when extra edges are added. If there is an edge \(e\) between two noncentral vertices, then the object intent \(e'=V\setminus e\) is closed and proper, contains \(u\), and is different from all previously constructed intents (only the top one contained \(u\)). Hence any additional nonspoke edge forces strict inequality. For a star, the closed intents consist exactly of every proper subset of the leaves together with \(V\), giving \(2^{n-1}\) in total. This proves the sharp equality characterization.

**Step 3: path/cycle transfer.** Label each vertex \(i\) by \(x_i=0\) if it lies in \(A\), and by \(x_i=1\) if it lies in \(D\). The weight of vertex \(i\) in (1) is \(1\) when \(x_i=1\), and \(z(x_{i-1}+x_{i+1})\) when \(x_i=0\). Thus a transition \((a,b)\to(b,c)\) receives weight \(1\) for \(b=1\) and weight \(z(a+c)\) for \(b=0\). This is exactly the displayed matrix. For a path the boundary labels are \(x_0=x_{n+1}=0\), hence its initial states are \((0,0),(0,1)\) and its terminal states are \((0,0),(1,0)\), giving \(aT^nb\). Cyclic boundary conditions close the state sequence, giving the trace. Direct multiplication (or determinant) gives \(\det(\lambda I-T)=\lambda(\lambda^3-\lambda^2-2z\lambda-z^2)\), and Cayley–Hamilton gives the recurrence. In a path or cycle, one dominating vertex covers at most three vertices, so \(\gamma\ge\lceil n/3\rceil\). Taking every third vertex (with appropriate endpoint adjustment) achieves equality in both graph families. The degree of (1) is therefore \(n-\lceil n/3\rceil=\lfloor2n/3\rfloor\).

**Step 4: random-graph expectation.** For fixed \(A\) with \(|A|=k\), the \(k(n-k)\) cut edges are independent Bernoulli variables. The \(k\) factors \(|N_G(v)\cap D|\), indexed by distinct \(v\in A\), involve disjoint collections of such edges. Their product has expectation \(((n-k)p)^k\). Summing over all \(\binom nk\) sets proves (5), with \(k=n\) giving zero for \(n\ge1\).

## Verification
The accompanying executable `verify.py` reconstructs the actual formal context for all \(1,099\) labeled simple graphs on up to five vertices, independently enumerates reduced contranominal submatrices, computes dominating-set weights, checks the Boolean-rank identity, enumerates all closed intents, and verifies the universal-vertex equality case. It independently checks the path/cycle transfer for sizes through \(11\), plus the complete/star formulas through \(8\), and the transfer-matrix polynomial identity. Its successful output is:

```text
VERIFY_OK labeled_graphs= 1099 submatrix_witnesses= 44672 concept_totals= 15765 path_cycle_profiles= 20 max_n=11 complete_star_max_n=8 transfer_matrix_identity=PASS
```

These finite checks corroborate but do not replace the general proofs above.

## Relationship to prior work
The general contranominal-scale characterization of Boolean suborders of concept lattices is prior mathematics, developed and discussed in [1,2]. General graph/hypergraph incidence and concept-lattice connections appear in [3]. The graph domination number and its NP-completeness are standard pre-existing graph theory. The contribution here is the exact graph-specific complement-incidence correspondence, its complete weighted scale polynomial, sharp star equality, uniform transfer and expected coefficients. A general theorem can have unrecognized graph-specific corollaries: the claimed originality is subject to that residual possibility and to literature under alternative graph-context terminology.

## Limitations
Only finite simple undirected graphs and the specified nonincidence context are covered. No equality between the number of scales and the number of embedded Boolean suborders is asserted. No statement about Boolean sublattices, arbitrary hypergraph contexts, or typical random-graph concentration is claimed. The novelty comparison cannot certify absolute historical priority; no independent mathematical audit has been performed.

## References
[1] M. Koyda and G. Stumme, *Boolean Substructures in Formal Concept Analysis*, arXiv:2104.07159, initially posted 2021-04-14. https://arxiv.org/abs/2104.07159

[2] A. Albano and B. Chornomaz, *Why concept lattices are large: Extremal theory for number of minimal generators and formal concepts*, CEUR-WS Vol. 1466, paper06, 2015. https://ceur-ws.org/Vol-1466/paper06.pdf

[3] Rawson et al., *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681 (2023). https://arxiv.org/abs/2307.11681
