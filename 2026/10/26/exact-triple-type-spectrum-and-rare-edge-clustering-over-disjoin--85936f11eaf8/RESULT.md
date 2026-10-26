# Exact triple-type spectrum and rare-edge clustering over disjoint maximal cliques in Henson graphs

## Finding
Fix integers \(r\geq3\), \(k\geq3\), and \(b\geq1\). Let \(\mathbb H_{r+1}\) be the countable universal homogeneous graph omitting \(K_{r+1}\). Individually name all vertices of an induced disjoint union of \(b\) copies of \(K_r\). Write \(T_{r,k}(b)\) for the number of complete types of ordered, pairwise distinct \(k\)-tuples of new vertices, all outside the named parameter graph. Every possible adjacency among the new vertices is counted as a distinct type.

Put \(a=2^r-1\), and define
\[
\begin{aligned}
B_0&=a^k,\\
B_1&=a^k-ra^{k-2},\\
B_2&=a^k-2ra^{k-2}+ra^{k-3}.
\end{aligned}
\]
For every fixed \(r,k\), the complete type count has the **three-term, strictly ordered exponential spectrum**
\[
\boxed{T_{r,k}(b)=B_0^b+\binom{k}{2}B_1^b+3\binom{k}{3}B_2^b+O_{r,k}((B_2-1)^b).}
\]
In fact there is an exact finite expression \(T_{r,k}(b)=\sum_H c_r(H)^b\), over all labelled \(K_{r+1}\)-free graphs \(H\) on the tuple coordinates; the nonnegative integer bases \(c_r(H)\) are explicitly computable by testing the \(2^{rk}\) possible neighbourhood matrices of a single parameter clique. The first three bases correspond, respectively, to the edgeless tuple graph, any one-edge tuple graph, and any graph with exactly two incident edges (a three-vertex path). All other permitted tuple graphs have bases at most \(B_2-1\).

For \(k=3\), **all four exponential terms are explicit**. With
\[
B_\triangle=a^3-3ra+2r-13\binom r2,
\]
one has, for every \(b\ge1\),
\[
\boxed{T_{r,3}(b)=a^{3b}+3(a^3-ra)^b+3(a^3-2ra+r)^b+B_\triangle^b.}
\]
For example, at \(r=3\), the four bases are \(343,322,304,247\); hence the number of ordered injective triple types in the universal \(K_4\)-free graph over \(b\) named disjoint triangles is exactly \(343^b+3\cdot322^b+3\cdot304^b+247^b\).

When a complete type is chosen uniformly from these finitely many \(k\)-types, its internal tuple graph is asymptotically edgeless:
\[
\boxed{\Pr(H=\overline{K}_k)=1-\binom k2(B_1/B_0)^b+O_{r,k}((B_2/B_0)^b).}
\]
More strongly, conditional on having at least two internal edges, the tuple graph is asymptotically a three-vertex path plus isolated vertices:
\[
\boxed{\lim_{b\to\infty}\Pr(H\cong P_3\sqcup(k-3)K_1\mid |E(H)|\ge2)=1.}
\]
This **rare-edge clustering** is strictly stronger than the observation that the expected number of internal edges tends to zero: two incident edges dominate two disjoint edges exponentially, even though both patterns contain precisely two edges.

## Assumptions and scope
Graphs are undirected, irreflexive and simple. The parameter graph \(bK_r\) is induced (there are no edges between its distinct clique components). The tuple coordinates are ordered, distinct from one another, and outside the named parameters. Complete types are in the ordinary graph language over these individually named parameters. They are determined by the finite induced adjacency pattern because \(\mathbb H_{r+1}\) is ultrahomogeneous, and every \(K_{r+1}\)-free finite extension occurs.

The integers \(r\ge3\) and \(k\ge3\) are fixed when \(b\to\infty\). The result concerns this explicit parameter family, not arbitrary parameter graphs. The restriction \(r\ge3\) excludes the triangle-free case, for which broader all-arity parameter counting principles are already available; the restriction \(k\ge3\) likewise excludes earlier pair-type statements.

For a labelled graph \(H\) on \([k]\), define \(c_r(H)\) precisely as follows. Choose subsets \(S_1,\ldots,S_k\subseteq[r]\), join the tuple vertices according to \(H\), join the \(r\) parameter vertices into a clique, and join tuple vertex \(i\) to the parameter vertices in \(S_i\). Count the choices for which the resulting \((k+r)\)-vertex graph is \(K_{r+1}\)-free. If \(H\) already contains \(K_{r+1}\), set \(c_r(H)=0\).

## Proof
**1. Complete types factor through parameter cliques.** Every nonalgebraic injective tuple type is uniquely specified by the labelled internal graph \(H\) and the neighbourhood subsets \(S_i^{(t)}\subseteq[r]\) for each parameter clique \(t\in[b]\). Henson universality and homogeneity say such data yield exactly one complete type if and only if the resulting finite graph is \(K_{r+1}\)-free. A clique cannot use vertices from two different parameter clique components because those components are mutually nonadjacent. Thus the global forbidden-clique test factors separately over the \(b\) components, yielding the exact identity
\[
T_{r,k}(b)=\sum_{\substack{H\text{ labelled on }[k]\\H\text{ is }K_{r+1}\text{-free}}}c_r(H)^b.
\]
More explicitly, a neighbourhood family \((S_i)\) contributes to \(c_r(H)\) precisely when for every nonempty clique \(C\) in \(H\) of size \(s\le r\),
\[
\left|\bigcap_{i\in C}S_i\right|\le r-s.
\]
In particular, each \(S_i\) is a proper subset of \([r]\).

**2. The three largest bases.** Let \(a=2^r-1\). For the edgeless \(H\), the \(k\) proper neighbourhood subsets may be chosen independently, giving \(B_0=a^k\). A single internal edge \(ij\) creates one extra forbidden event: \(|S_i\cap S_j|\ge r-1\). Since both subsets are proper, this occurs exactly when both are the same \((r-1)\)-subset of \([r]\), in \(r\) choices. Thus the one-edge base is \(B_1=a^k-ra^{k-2}\).

For two edges sharing a tuple vertex, say \(ij\) and \(i\ell\), their respective forbidden events each number \(ra^{k-2}\), and their intersection occurs exactly when the three corresponding subsets are identical co-singletons, in \(ra^{k-3}\) choices. Inclusion–exclusion gives \(B_2=a^k-2ra^{k-2}+ra^{k-3}\). Two disjoint edges, possible only for \(k\ge4\), instead give
\[
B_{\mathrm{disjoint}}=a^k-2ra^{k-2}+r^2a^{k-4},
\]
which is strictly smaller, because
\[
B_2-B_{\mathrm{disjoint}}=ra^{k-4}(a-r)>0.
\]
Here \(a>r\) for \(r\ge3\).

Adding any edge \(ij\) to a \(K_{r+1}\)-free internal graph \(H\) strictly decreases \(c_r(H)\), provided the augmented graph stays \(K_{r+1}\)-free. Indeed, choose \(S_i=S_j=[r]\setminus\{v\}\), for any \(v\in[r]\), and assign the empty subset to every other tuple coordinate. This assignment is allowed for \(H\) (the endpoints are nonadjacent there), but creates \(K_{r+1}\) after the new edge is added. Every other assignment accepted after the edge addition was already accepted before it. Consequently every graph with at least three edges has a base strictly below the base of any two-edge subgraph, while any graph with exactly two disjoint edges has base smaller than \(B_2\). Since bases are integers, all graphs other than the three listed shapes have bases at most \(B_2-1\). The inequalities \(B_0>B_1>B_2>0\) follow from the explicit formulas and the admissibility of the all-empty assignment. There are \(1\), \(\binom k2\), and \(3\binom k3\) labelled internal graphs of the three respective shapes. This proves the three-term expansion, with an error bounded by at most \(2^{\binom k2}(B_2-1)^b\).

**3. The exact triangle term.** For \(k=3\), the only remaining internal graph is a triangle. There are three forbidden edge events among proper neighbourhood subsets. Inclusion–exclusion over these pair events leaves
\[
a^3-3ra+2r
\]
assignments. A triangle additionally forbids a common neighbourhood of size at least \(r-2\). Among assignments already avoiding all pair events, such a common neighbourhood has exactly \(r-2\) elements. Choose that common core in \(\binom r2\) ways. Each of the three subset labels then uses zero or one of the two remaining elements; to avoid pair events each remaining element can be used by at most one label. There are exactly \(1+6+6=13\) such assignments. The common core is uniquely determined, so subtraction gives \(B_\triangle=a^3-3ra+2r-13\binom r2\). Summing the four labelled internal-graph classes proves the exact triple formula.

**4. Rarity and clustering.** Divide the three-term expansion by \(B_0^b\). As \(B_1/B_0<1\), the edgeless probability tends to one. Its first correction is \(\binom k2(B_1/B_0)^b\); the next error is \(O((B_2/B_0)^b)\), since \(B_1^2/B_0<B_2\), equivalently \(r(a-r)>0\). Meanwhile types with exactly two incident edges contribute \(3\binom k3 B_2^b\), and all other types with at least two edges contribute at most \(2^{\binom k2}(B_2-1)^b\). Their ratio tends to zero, proving the conditional path concentration. The strict preference for incident over disjoint pairs of edges follows from the explicit positive difference of their bases.

## Verification
Run `python3 verify.py` in a directory containing this result and `verify.py`. The standard-library checker compares direct forbidden-clique tests with a separately implemented common-neighbour criterion over 294,912 local assignments in 79 small labelled graph profiles. It performs 4,800 additional direct graph checks over two distinct parameter cliques, checks the exact triple expression for nine parameter pairs, and separately checks larger forbidden clique thresholds. The accompanying `verification-output.txt` contains the recorded `ALL_TESTS_PASS` result. These finite computations are supporting checks and do not substitute for the proof for unbounded \(r,k,b\).

## Relationship to prior work
Henson established the existence, universality, and homogeneity of the countable \(K_p\)-free graphs; in particular, his Theorem 2.3 supplies the finite-extension framework. Conant's 2014 work on Henson graph types (especially Proposition 3.4) likewise treats consistency and optimal realizations of relational types, but concerns dividing and forking rather than these exact parameter-dependent high-arity type counts. His later free-amalgamation work provides a more general structural framework, not the asserted exponential bases.

Finite-parameter one-type counts in Henson graphs can already be expressed through clique-free subset enumerators, and general formulae for the triangle-free graph's higher-arity types and for some four-clique-free pair spectra have also been obtained. These prior principles are acknowledged and are not the present claim. The new scope requires \(K_{r+1}\)-free with \(r\ge3\), injective tuple arity \(k\ge3\), a repeated maximal-clique parameter family, and the explicit triple spectrum and all-arity three-leading-base/conditional-clustering theorems. The relevant published and indexed mathematical searches inspected to date did not reveal a result covering those combined statements. Unindexed treatments of Henson type spectra or an implicit extraction from broader enumeration methods remain originality risks.

## Limitations
No claim is made for tuple coordinates equal to each other or to parameters, for varying \(r,k\) in the asymptotic estimates, or for arbitrary finite parameter graphs. The finite spectral sum can have many terms outside the three leading bases; the error bound does not classify those lower bases. The convergence statements use the uniform distribution over complete types, not over random realizations of the countable graph. The proof does not address independence under other probability measures.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* **38** (1971), 69–83, Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570, first posted 2014-01-08; *Notre Dame Journal of Formal Logic* **58** (2017), 555–566. https://arxiv.org/html/1401.1570v1
3. G. Conant, “An axiomatic approach to free amalgamation,” arXiv:1505.00762, first posted 2015-05-04; *Journal of Symbolic Logic* **82** (2017), 648–671. https://arxiv.org/abs/1505.00762
4. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” publicly accessible research record (one-type formula and complexity, not a higher-arity spectrum). https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650/RESULT.md
