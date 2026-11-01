# Extremal forests and exact counts for total domination in triangular graphs

## Finding

For every integer \(n\ge 4\), let \(J(n,2)\) be the Johnson graph whose vertices are the two-element subsets of \([n]\), with distinct vertices adjacent when their subsets intersect. Let \(T(n)\) count its minimum-cardinality total dominating sets, where all elements of \([n]\) are labelled and sets are not identified under automorphisms. Their common cardinality is
\[
\gamma_t(J(n,2))=\left\lceil\frac{2(n-1)}3\right\rceil.
\]
The exact numbers of minimum sets are, for the indicated positive integers \(k\),
\[
\begin{aligned}
T(3k)&=\frac{(3k)!}{2^k k!}\left(1+\frac{25}{6}k(k-1)+\frac{16}{9}k(k-1)(k-2)\right) &&(k\ge 2),\\
T(3k+1)&=\frac{(3k+1)!}{2^k k!} &&(k\ge1),\\
T(3k+2)&=\frac{4k}{3}\frac{(3k+2)!}{2^k k!} &&(k\ge1).
\end{aligned}
\]

More strongly, interpret a selected vertex \(\{i,j\}\) of \(J(n,2)\) as an edge \(ij\) of a graph \(H\) on the labelled set \([n]\). The minimum total dominating sets correspond **exactly** to the following forests. Every unspecified nontrivial component is a three-vertex path \(P_3\), and a tree of order four or five can have any tree shape.

* If \(n=3k\), either \(H\) consists of \(k\) components \(P_3\), or it has one isolated vertex and either one tree of order five with \(k-2\) copies of \(P_3\), or two trees of order four with \(k-3\) copies of \(P_3\). A family with a negative number of copies is absent.
* If \(n=3k+1\), then \(H\) consists of one isolated vertex and \(k\) copies of \(P_3\).
* If \(n=3k+2\), then \(H\) consists of one isolated vertex, one tree of order four, and \(k-1\) copies of \(P_3\).

## Assumptions and scope

Graphs are finite, simple, undirected and labelled. A total dominating set \(D\) of a graph \(G\) satisfies: every vertex of \(G\), including each vertex of \(D\), has a **distinct adjacent vertex in \(D\)**. Thus a selected edge of \(H\) must meet another selected edge. Trees described above are **selected-edge subgraphs**, not necessarily induced subgraphs of the ambient complete graph. The theorem holds for every integer \(n\ge4\); no asymptotic or probabilistic assumption is used.

## Proof

**1. Exact selected-edge criterion.** The Johnson graph \(J(n,2)\) is the line graph of the complete graph on \([n]\). Given \(D\subseteq V(J(n,2))\), form \(H=([n],D)\), and let \(s\) be its number of nonisolated vertices. Every selected edge of \(H\) has a neighbour in \(D\) precisely when \(H\) has no component isomorphic to \(K_2\). Every unselected edge \(ij\) of the complete graph has a selected incident edge precisely when at least one of its endpoints belongs to the support of \(H\). Consequently,
\[
D\text{ is total dominating}\quad\Longleftrightarrow\quad
s\ge n-1\text{ and }H\text{ has no component }K_2.
\]
To see the converse without ambiguity, if a pair \(ij\) is selected, the absence of a \(K_2\)-component gives an adjacent selected edge distinct from \(ij\); if it is unselected, an endpoint incident with a selected edge supplies its adjacent selected edge.

**2. Sharp lower bound.** Every nontrivial connected component of such an \(H\) has \(v_i\ge3\) vertices and \(e_i\ge v_i-1\ge2\) edges. Therefore
\[
v_i\le e_i+1\le \tfrac32e_i.
\]
Summing gives \(n-1\le s\le\tfrac32 |D|\), whence \(|D|\ge\lceil 2(n-1)/3\rceil\). This is attained by \(k\) disjoint \(P_3\)'s when \(n=3k\), by \(k\) such paths and one isolated vertex when \(n=3k+1\), and by one order-four tree, \(k-1\) such paths and one isolated vertex when \(n=3k+2\). Each construction meets the criterion from step 1.

**3. Equality rigidity.** Fix a minimum total dominating set, put \(h=\lceil2(n-1)/3\rceil\), and write \(\varepsilon=n-s\in\{0,1\}\). Let \(c\) count the nontrivial components of \(H\) and let
\[
\mu=\sum_{i=1}^{c}(e_i-v_i+1)\ge0
\]
be its total cyclomatic excess. Every component has at least three vertices, so
\[
c=s-h+\mu\le\left\lfloor\frac{s}{3}\right\rfloor.
\]
For \(n=3k\), \(h=2k\). If \(\varepsilon=0\), this inequality becomes \(k+\mu\le k\); if \(\varepsilon=1\), it becomes \(k-1+\mu\le k-1\). In either case \(\mu=0\). For \(n=3k+1\), \(h=2k\): \(\varepsilon=0\) would imply \(k+1+\mu\le k\), impossible, while \(\varepsilon=1\) implies \(k+\mu\le k\). For \(n=3k+2\), \(h=2k+1\): \(\varepsilon=0\) likewise implies \(k+1+\mu\le k\), while \(\varepsilon=1\) implies \(k+\mu\le k\). Thus \(\mu=0\) in **all** minimum configurations: every nontrivial component is a tree.

The number of components and their total orders now force the claimed sizes. In the \(3k\) case with no isolated vertex there are \(k\) trees with \(3k\) total vertices, hence all have order three. With one isolated vertex there are \(k-1\) trees using \(3k-1\) vertices, two more than the baseline \(3(k-1)\), giving either one order-five tree or two order-four trees. In the \(3k+1\) case there are \(k\) trees using exactly \(3k\) vertices, so all have order three. In the \(3k+2\) case there are \(k\) trees using \(3k+1\) vertices, so exactly one has order four. Since a three-vertex tree is \(P_3\), this proves the complete classification. Every listed forest satisfies the criterion and has \(h\) edges, so the necessity and sufficiency are both proved.

**4. Counting without symmetry quotient.** On a fixed labelled triple there are three choices for \(P_3\). By Cayley's tree formula, on fixed labelled sets of four and five vertices there are \(4^2=16\) and \(5^3=125\) trees. Partitioning \([n]\) into unordered tree components, and specifying the isolated vertex when present, gives the following disjoint contributions. For \(n=3k\) they are
\[
\frac{n!}{2^kk!},\qquad
\mathbf1_{k\ge2}\frac{125n!}{5!\,2^{k-2}(k-2)!},\qquad
\mathbf1_{k\ge3}\frac{16^2n!}{2(4!)^2\,2^{k-3}(k-3)!}.
\]
For \(n=3k+1\) there is \(n!/(2^kk!)\). For \(n=3k+2\) there is \(16n!/(4!\,2^{k-1}(k-1)!)\). Simplifying produces the three stated formulas.

## Verification

The standalone `verification.cpp` builds the edges of the complete graph on \([n]\), independently enumerates every subset of exactly \(\lceil 2(n-1)/3\rceil\) edges for \(4\le n\le10\), applies the total-domination criterion, verifies the connected-component shapes, and compares each classified count to the exact formulas using integer arithmetic. Its runs return, for \(n=4,5,6,7,8,9,10\), respectively,
\[
T(n)=12,\ 80,\ 840,\ 630,\ 13440,\ 277200,\ 75600.
\]
The exhaustive checks cover all \(8{,}145{,}060\) candidate minimum-sized edge sets for \(n=10\), and every corresponding candidate for the preceding values. This finite replay corroborates the argument but does not replace the universal proof in steps 1–4.

## Relationship to prior work

Cornet, Dravec and Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675 (first publicly submitted 3 October 2026), Theorem 14, establish the exact minimum size \(\gamma_t(J(n,2))=\lceil2(n-1)/3\rceil\). Their relevant proof gives a lower bound and constructions. The new part here is the exhaustive **structure and number** of all minimum sets for each \(n\), not that already established minimum cardinality. The result has the equivalent interpretation as classifying minimum total edge dominating sets of complete graphs.

Pan, Yang, Li and Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431, study the general edge version and focus on complexity and input trees; their accessible abstract does not specify this complete-graph count. A broader historical search found no equivalent formula, but absence from search results does not prove priority.

## Limitations

This result does not enumerate nonminimum total dominating sets, does not quotient by permutations of \([n]\) or Johnson-graph automorphisms, and does not treat \(J(n,r)\) for \(r\ge3\). The original paper's minimum-number theorem is **not** claimed as novel. Bibliographic coverage may be incomplete, particularly for older work formulated in total edge domination terminology. Independent review has not been performed.

## References

1. M. G. Cornet, T. Dravec and P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675 (2026), especially Theorem 14 and its proof. https://arxiv.org/html/2610.04675
2. Z. Pan, Y. Yang, X. Li and S.-J. Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431 (2019). https://arxiv.org/abs/1910.02431
3. A. Cayley, the classical formula counting trees on a labelled \(r\)-element vertex set, \(r^{r-2}\).
