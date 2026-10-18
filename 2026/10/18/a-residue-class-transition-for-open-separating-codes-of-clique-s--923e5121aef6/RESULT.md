# A residue-class transition for open-separating codes of clique subdivisions

## Finding

For every integer \(n\ge 3\), let \(H_n=S(K_n)\) be the graph obtained by subdividing each edge of the complete graph exactly once. Thus, \(H_n\) is the bipartite incidence graph between the \(n\) vertices and the \(\binom n2\) edges of \(K_n\). A vertex set \(C\subseteq V(H_n)\) is an **open-separating dominating code** (OD-code, also called an OSD-code) when \(N[v]\cap C\ne\varnothing\) for every vertex \(v\), and the sets \(N(v)\cap C\) are pairwise different for *all* vertices \(v\). An **open-separating total-dominating code** (OTD-code, also called an OLD-set) additionally requires \(N(v)\cap C\ne\varnothing\) for every \(v\).

For \(s\ge0\), put
\[
W_s(z)=\sum_{F\subseteq E(K_s):\,([s],F)\text{ has no components of orders }1\text{ or }2}z^{|F|},
\]
with \(W_0(z)=1\) and \(W_1(z)=W_2(z)=0\). Here a component of order two in a simple graph is necessarily an isolated edge. These polynomials have the explicit inclusion-exclusion representation
\[
W_s(z)=\sum_{\substack{i,j\ge0\\i+2j\le s}}
(-1)^{i+j}\frac{s!}{i!\,2^j j!\,(s-i-2j)!}
 z^j(1+z)^{\binom{s-i-2j}{2}}.
\]

**Theorem (complete code census and residue-class transition).** The cardinality polynomials of OD-codes and OTD-codes in \(H_n\) are, respectively,
\[
\boxed{P_{\rm OD}(H_n;z)=(z^n+nz^{n-1})W_n(z)
+\bigl(nz^n+n(n-1)z^{n-1}\bigr)W_{n-1}(z)}
\]
and
\[
\boxed{P_{\rm OTD}(H_n;z)=(z^n+nz^{n-1})W_n(z).}
\]
Consequently their minimum cardinalities are
\[
\boxed{\gamma_{\rm OD}(H_n)=2n-1-\left\lfloor\frac n3\right\rfloor-\mathbf{1}_{\{3\nmid n\}},\qquad
\gamma_{\rm OTD}(H_n)=2n-1-\left\lfloor\frac n3\right\rfloor.}
\]
In particular, \(\gamma_{\rm OTD}(H_n)-\gamma_{\rm OD}(H_n)\) equals zero exactly when \(3\mid n\), and equals one otherwise.

The theorem also classifies every minimum code. Define the labeled-tree-forest count
\[
B_s=s!\,[u^s t^{\lfloor s/3\rfloor}]
\exp\left(t\sum_{r\ge3}\frac{r^{r-2}}{r!}u^r\right).
\]
For \(s=2\) this equals zero. The exact number of minimum OD-codes is
\[
\boxed{\begin{cases}
nB_n+n(n-1)B_{n-1},&3\mid n,\\
n(n-1)B_{n-1},&3\nmid n.
\end{cases}}
\]
The number of minimum OTD-codes is always \(nB_n\). The coefficient formula for \(B_s\) is finite: at the displayed degree, only terms with \(3\le r\le s\) contribute.

## Assumptions and scope

All graphs are finite, simple, and undirected. In \(H_n\) call the inherited vertices **original vertices** and write them as \([n]\); denote the subdivision vertex of edge \(ij\) by \(e_{ij}\). For any code \(C\), let \(A=C\cap[n]\) and let \(F=\{ij:e_{ij}\in C\}\). The subgraph \(([n],F)\) is spanning and may have isolated vertices. Code size is \(|C|=|A|+|F|\). The OTD condition is the stronger *total* domination condition; the OD condition alone permits one empty open-neighborhood signature if the corresponding vertex belongs to \(C\).

## Proof

**Step 1: original-vertex rigidity.** For each subdivision vertex \(e_{ij}\), its open signature is \(N(e_{ij})\cap C=A\cap\{i,j\}\). If two original vertices \(i,j\) are omitted from \(A\) and \(A\ne\varnothing\), choose \(k\in A\). Then \(e_{ik}\) and \(e_{jk}\) have identical signature \(\{k\}\), contradicting open separation. If \(A=\varnothing\), all subdivision-vertex signatures are empty, again contradicting separation because \(n\ge3\). Hence \(|A|\ge n-1\). Conversely, if \(|A|\ge n-1\), all subdivision signatures are nonempty and pairwise distinct: with one omitted index, the signatures are either a different selected singleton (for an edge using the omitted index) or the edge's selected endpoint pair.

**Step 2: the exact selected-edge condition.** For an original vertex \(i\), its open signature is \(\{e_{ij}:ij\in F\}\). For distinct \(i,j\), these signatures coincide only in two cases: both are empty, or each is the same singleton \(\{e_{ij}\}\). Indeed, if two edges were incident with \(i\), they could not both be incident with a different vertex \(j\). Thus, the original-vertex signatures are pairwise distinct if and only if \(([n],F)\) has at most one isolated vertex and has no isolated-edge component. Every nonempty original signature is supported on subdivision vertices, whereas every subdivision signature is nonempty and supported on original vertices, so signatures from the two sides cannot coincide. All subdivision vertices are dominated because \(|A|\ge n-1\). Original vertices incident with \(F\) are dominated; an isolated original vertex has empty open signature and is dominated in the closed sense precisely when it belongs to \(A\). We conclude that \(C\) is an OD-code exactly when \(|A|\ge n-1\), \(([n],F)\) has no isolated edge component, and it has either no isolated vertices or exactly one isolated vertex lying in \(A\). For OTD-codes the isolated-vertex exception is forbidden.

**Step 3: enumerate all codes.** If \(([n],F)\) has no isolated vertices and no isolated-edge component, then \(F\) contributes \(W_n(z)\) and \(A\) contributes \(z^n+nz^{n-1}\). If it has exactly one isolated vertex \(y\), choosing \(y\) gives \(n W_{n-1}(z)\) possibilities for \(F\) by cardinality. For each such \(F\), \(A\) is either all \(n\) originals or all but one of the other \(n-1\) originals; the contribution is \(z^n+(n-1)z^{n-1}\). This proves both polynomial identities and the exact difference \(P_{\rm OD}-P_{\rm OTD}=nz^{n-1}(z+n-1)W_{n-1}\).

For completeness, fix a prescribed set of \(i\) isolated vertices and \(j\) disjoint isolated-edge components in a graph on \(s\) labeled vertices. This forces exactly \(j\) present edges and forbids all edges incident to those components except their own internal edges; the remaining \(s-i-2j\) vertices may have any edges. Its generating weight is \(z^j(1+z)^{\binom{s-i-2j}{2}}\). The number of such prescriptions is \(s!/(i!2^j j!(s-i-2j)!)\). Inclusion-exclusion over forbidden singleton and isolated-edge components gives the asserted \(W_s(z)\). Distinct forbidden-component events can be jointly realized only when their prescribed vertex sets are disjoint, so no terms are omitted.

**Step 4: minima and their exact multiplicities.** A graph on \(s\) labeled vertices with all components of order at least three and \(c\) components has at least \(s-c\) edges, with equality precisely for a forest of trees. Since \(c\le\lfloor s/3\rfloor\), its least possible edge count is \(d_s=s-\lfloor s/3\rfloor\), attained by forests with \(\lfloor s/3\rfloor\) components of sizes at least three. Cayley's labeled tree count \(r^{r-2}\) gives exactly \(B_s\) such forests via the exponential formula. For OD-codes, \(F\) has minimum either \(d_n\) edges with no isolates, or \(d_{n-1}\) edges with one isolate. Direct floor arithmetic yields \(d_n=d_{n-1}\) when \(3\mid n\), and \(d_n=d_{n-1}+1\) otherwise. Any minimum code uses exactly \(n-1\) original vertices, since this choice is feasible with every eligible minimum edge set, and selecting the last original would increase its cardinality. Therefore the exact minima and counts are as stated: no-isolate forests give \(nB_n\) choices; one-isolate forests give \(n(n-1)B_{n-1}\) choices, as the omitted original vertex must differ from the isolated one. For OTD-codes only the former contribution occurs. This completes the proof for every \(n\ge3\).

## Verification

The standalone file `verify.py` tests the definitions directly on graph adjacencies and compares its generated code-cardinality histogram with the inclusion-exclusion formulas. It exhaustively examines every vertex subset for \(3\le n\le6\), totaling 2,131,008 candidate subsets, and independently tests the stronger OTD condition. It also checks polynomial coefficients, minima, and minimum-code counts symbolically for \(3\le n\le11\), using an independent recurrence for restricted labeled tree forests. The executable produces `VERIFICATION_OK direct_candidates 2131008 symbolic_orders 9`; its recorded output is in `verification_output.txt`. These are finite sanity checks, not a replacement for the proof.

## Relationship to prior work

Chakraborty and Wagler introduced the open-separating dominating code notion in their 2024 preprint and conference paper, and established the general bound \(\gamma_{\rm OTD}(G)-1\le\gamma_{\rm OD}(G)\le\gamma_{\rm OTD}(G)\) for graphs without isolated vertices. Their full-length paper studies general structure and examples including cliques, matchings, half-graphs, fans, and spiders; its section on code families does not state the present clique-subdivision enumerator or residue-class dichotomy. The present graph is also known as the incidence graph of the edges of a clique or the central graph of a clique, and its OD and OTD codes have been compared under these aliases.

Earlier literature on open-neighborhood locating-dominating sets uses a total-domination requirement and thus corresponds to OTD rather than OD. The generic hypergraph covering reformulation in the foundational paper encodes all codes in any graph, but it does not give this infinite-family polynomial, the restricted graph-species bijection, or the exact mod-three separation of its two minima. These are mathematical comparisons, not a claim of exhaustive bibliographic priority.

## Limitations

The theorem covers the full one-subdivision of complete graphs and does not assert an analogous formula for arbitrary base graphs or repeated subdivisions. No all-orders computational enumeration is claimed; unbounded validity is established by the explicit proof. The finite verifier covers only the ranges stated. A related broad dissertation was not accessible for full-text comparison, leaving some literature-priority uncertainty. Independent external evaluation has not been performed.

## References

1. D. Chakraborty and A. K. Wagler, *On open-separating dominating codes in graphs*, arXiv:2402.03015, first publicly submitted 5 February 2024, https://arxiv.org/abs/2402.03015 (the later full-length revision uses OD/OTD abbreviations).
2. D. Chakraborty and A. K. Wagler, *Open-Separating Dominating Codes in Graphs*, International Symposium on Combinatorial Optimization, 2024, DOI: 10.1007/978-3-031-60924-4_11, https://link.springer.com/chapter/10.1007/978-3-031-60924-4_11.
3. M. Chellali, N. J. Rad, S. J. Seo, and P. J. Slater, *On open neighborhood locating-dominating in graphs*, Electronic Journal of Graph Theory and Applications **2** (2014), 87–98, DOI: 10.5614/ejgta.2014.2.2.1.
