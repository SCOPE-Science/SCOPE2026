# Paired-domination polynomial and large-set threshold for complete prisms

## Finding

**Theorem.** Let \(n\ge2\), and let \(H_n=K_n\square K_2\) be the graph consisting of two labeled copies of \(K_n\), with corresponding vertices joined by a perfect matching. Let \(p_{n,k}\) count vertex subsets of size \(2k\) that dominate \(H_n\) and induce a subgraph admitting a perfect matching. Then, for \(1\le k\le n\),

\[
p_{n,k}=\binom{2n}{2k}-\left(2+2^{2k-1}\right)\binom n{2k}+2\mathbf 1_{\{2\mid n\}}\mathbf 1_{\{2k=n\}}.
\]

The paired-domination polynomial \(P_n(z)=\sum_{k=1}^n p_{n,k}z^{2k}\) is therefore

\[
P_n(z)=\frac{(1+z)^{2n}+(1-z)^{2n}}2-(1+z)^n-(1-z)^n+\frac32-\frac{(1+2z)^n+(1-2z)^n}{4}+2\mathbf1_{\{2\mid n\}}z^n.
\]

In particular, every vertex set of **even** cardinality strictly greater than \(n\) is paired dominating. The degree threshold is sharp among even cardinalities: when \(n\) is even there are non-paired-dominating sets of size \(n\), and when \(n\) is odd there are such sets of size \(n-1\). The minimum paired-domination number is \(2\) for every \(n\ge2\), with exactly \(4\) minimum sets at \(n=2\) and exactly \(n\) at every \(n\ge3\). All sets are counted as vertex subsets, not as choices of matchings.

## Assumptions and scope

All graphs are finite, simple, and undirected. Write the two clique layers as \(\{u_i:i\in[n]\}\) and \(\{v_i:i\in[n]\}\), where \([n]=\{1,\dots,n\}\). The edge set comprises every pair of different vertices within each layer and precisely the matching edges \(u_iv_i\) between layers. A paired-dominating set \(S\) is a dominating vertex subset for which \(H_n[S]\) admits a perfect matching. A perfect matching always consists of actual edges but need not be an induced matching; different perfect matchings of one \(S\) contribute only once.

For a given \(S\), define \(A=\{i:u_i\in S\}\), \(B=\{i:v_i\in S\}\), \(a=|A|\), \(b=|B|\), and \(r=|A\cap B|\). We use the convention \(\binom np=0\) for \(p>n\). The indicators in the formulas are ordinary zero/one integers.

## Proof

**Step 1: exact structural classification.** We claim that \(S\) is paired dominating if and only if one of the following mutually exclusive alternatives holds:

1. \(a,b\ge2\) and \(a,b\) are both even;
2. \(a,b\) are both odd and \(r\ge1\);
3. \(n\) is even and \((a,b)=(n,0)\) or \((0,n)\).

For sufficiency in case 1, each selected clique has even order at least two, so match selected vertices within each clique in pairs. Each clique contains a selected vertex, which dominates every vertex in its layer. Case 2 admits a matching using one vertical edge \(u_iv_i\) for any \(i\in A\cap B\); the remaining vertices in each layer form even cliques and can be matched internally. Each unselected vertex is adjacent to a selected vertex in its own clique, and every selected vertex is incident to its matched edge, so domination holds. In case 3, the entire chosen clique is even and admits an internal perfect matching, while every opposite-layer vertex is adjacent to its selected matching mate.

Conversely, a paired-dominating set induces a perfect matching, so \(a+b\) is even. If one layer is empty, domination of vertices in that layer forces every vertex of the opposite layer to be selected, and a perfect matching exists precisely when \(n\) is even, giving case 3. If both layers are nonempty, every unselected vertex has a neighbor selected in its own layer; the assumed perfect matching supplies a selected neighbor to each selected vertex. Since \(a+b\) is even, \(a,b\) have the same parity. If both are even, both are at least two, and we are in case 1. If both are odd, an internal matching alone cannot cover both cliques; at least one crossing edge \(u_iv_i\) is necessary. Such an edge exists among selected vertices exactly when \(i\in A\cap B\), giving case 2. This proves necessity and exhaustiveness.

**Step 2: enumerate the complement.** Fix an even cardinality \(s=2k\), \(2\le s\le2n\). There are \(\binom{2n}s\) total subsets. By Step 1, a set of size \(s\) fails to be paired dominating precisely if either it occupies only one clique without occupying that clique in full, or it has odd positive selections in both layers that use disjoint matching indices. The first kind comprises \(2\binom ns\) sets except that, when \(n\) is even and \(s=n\), the two full-clique subsets are actually valid. Therefore the first-kind failure count is \(2\binom ns-2\mathbf1_{\{2\mid n\}}\mathbf1_{\{s=n\}}\).

For the second kind, choose \(s\) distinct indices in \([n]\) and assign each to exactly one of the two layers. Exactly half of the \(2^s\) assignments put an odd number in the first layer (and hence, since \(s\) is even, an odd number in the second). Therefore the second-kind failure count is \(2^{s-1}\binom ns\). The two failure kinds are disjoint. Subtracting their counts from \(\binom{2n}s\) proves the coefficient formula.

**Step 3: sum coefficients.** Define \(E_n(z)=\frac12((1+z)^n+(1-z)^n)-1\), which enumerates nonempty even subsets in one layer, and \(O_n(z)=\frac12((1+z)^n-(1-z)^n)\), which enumerates odd subsets. Then \(E_n(z)^2+O_n(z)^2\) enumerates both-even-positive and both-odd selection patterns. The bad both-odd patterns are exactly the disjoint ones, enumerated by

\[
Q_n(z)=\frac{(1+2z)^n+(1-2z)^n-2}{4},
\]

because its \(z^{2k}\)-coefficient equals \(2^{2k-1}\binom n{2k}\). Finally the valid one-full-clique sets contribute \(2\mathbf1_{\{2\mid n\}}z^n\). Hence \(P_n(z)=E_n(z)^2+O_n(z)^2-Q_n(z)+2\mathbf1_{\{2\mid n\}}z^n\), which simplifies to the displayed expression.

**Step 4: sharp consequences.** If \(s>n\), both failure counts vanish since \(\binom ns=0\), so every even set of that size is paired dominating. If \(n\) is even, choose one vertex from each matching pair and split the \(n\) choices into two odd-sized groups (possible because \(n\) is even); the two odd cliques have no crossing selected edge, so the resulting size-\(n\) set fails. If \(n\) is odd, choose \(n-1\) distinct matching indices and similarly split them into two odd-sized groups; this fails at even size \(n-1\). At size two, the coefficient identity gives \(p_{n,1}=n\) for \(n\ge3\) and \(p_{2,1}=4\). No set of odd size can admit a perfect matching, so the minimum is two. This completes the proof.

## Verification

The accompanying standalone Python program `verify_paired_prisms.py` builds the graph directly from the adjacency rule. For every \(2\le n\le7\), it enumerates all subsets of each even size, tests domination by the actual adjacency lists, and independently tests whether the induced selected graph has a perfect matching using recursive backtracking. It compares every count against the closed formula. All checks completed successfully. These computations are finite corroboration, not the basis of the infinite argument.

Example coefficient sequences, listed in increasing even degree, are \((4,1)\) for \(n=2\), \((3,15,1)\) for \(n=3\), \((4,62,28,1)\) for \(n=4\), and \((5,160,210,45,1)\) for \(n=5\).

## Relationship to prior work

Carballosa and Wisby (2020) analyze total \(k\)-domination of Cartesian products of complete graphs, including the same underlying Cartesian-product construction, but their results concern a different property requiring multiple selected neighbors, not existence or multiplicity of perfect-matchable dominating vertex subsets. Choudhary, Margulies, and Hicks (2013) establish general inequalities for paired domination in Cartesian products; a minimum-cardinality bound does not yield the entire polynomial or the universal large-even-set threshold. Gorzkowska, Henning, Pilśniak, and Tumidajewicz (2023) study paired-domination stability in prisms, including specific cycle and hypercube prisms, rather than enumeration of all paired-dominating sets of complete prisms. The cited polynomial-framework conference abstract (2016) does not identify its treated graph families; see the limitations below.

## Limitations

The theorem concerns the two-layer complete prism only; it does not count distinct perfect matchings within a valid vertex set and does not extend to arbitrary graph prisms. Search and full-text comparisons conducted for the cited work did not identify the same coefficient formula; this is not a proof of global publication priority. The complete 2016 conference treatment of paired-domination polynomials and the full text of one 2018 ordinary/total domination paper could not be reliably inspected, so coverage of this very specific graph family by those sources remains a residual priority risk. The result does not establish publication priority beyond the examined research sources.

## References

1. W. Carballosa and J. Wisby, *Total \(k\)-domination in Cartesian product of complete graphs*, arXiv:2001.07850, first posted 2020-01-22. https://arxiv.org/abs/2001.07850
2. K. Choudhary, S. Margulies, and I. V. Hicks, *A Note on Total and Paired Domination of Cartesian Product Graphs*, Electron. J. Combin. 20(3) (2013), P25. https://doi.org/10.37236/2535
3. A. Gorzkowska, M. A. Henning, M. Pilśniak, and E. Tumidajewicz, *Total and paired domination stability in prisms*, Discuss. Math. Graph Theory 43 (2023), 1147–1169. https://doi.org/10.7151/dmgt.2421
4. W. Goddard and M. A. Henning, *A note on domination and total domination in prisms*, J. Comb. Optim. 35 (2018), 14–20. https://doi.org/10.1007/s10878-017-0150-0
5. Puttaswamy, A. Alwardi, and S. R. Nayaka, *Introduction to Paired Domination Polynomial of a Graph*, 2016 conference abstract. https://publications.waset.org/abstracts/52964/introduction-to-paired-domination-polynomial-of-a-graph
