# Minimal forts and the complete zero forcing polynomial of fully subdivided complete graphs

## Finding

Let \(n\ge3\), let \(E=\binom{[n]}2\), and put \(m=\binom n2\). Define \(S_n\) by replacing every edge \(e=\{u,v\}\) of \(K_n\) with a path \(u-x_e-v\). Thus \(V(S_n)=[n]\sqcup\{x_e:e\in E\}\), with \(n+m\) vertices. The original vertices and subdivision vertices are distinguished by this construction, including when \(n=3\).

A nonempty vertex set \(F\) is a **fort** when every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **minimal** when it contains no proper nonempty fort. A **zero forcing set** is an initial set of blue vertices from which the rule “a blue vertex with exactly one white neighbor forces that neighbor blue” eventually colors all vertices blue.

**Theorem.** All minimal forts of \(S_n\) are exactly the following three mutually disjoint families:

1. \(\{x_e:e\in E(C)\}\), where \(C\) is an undirected simple cycle of \(K_n\), of length \(3\) through \(n\);
2. the original-vertex set \([n]\);
3. for each \(v\in[n]\), the set \(([n]\setminus\{v\})\cup\{x_{\{v,u\}}:u\in[n]\setminus\{v\}\}\).

Consequently their cardinality polynomial is
\[
\mathcal F_n(z)=\sum_{k=3}^{n}\binom nk\frac{(k-1)!}{2}z^k+z^n+n z^{2n-2}.
\]

Write \(f_{n,j}\) for the number of edge subsets of \(K_n\) that are forests with exactly \(j\) edges, including isolated vertices, and put
\[
\mathcal U_n(y)=\sum_{j=0}^{n-1}f_{n,j}y^j
=n![t^n]\exp\!\left(\sum_{k=1}^{n}\frac{c_k}{k!}y^{k-1}t^k\right),
\qquad c_1=1,\quad c_k=k^{k-2}\quad(k\ge2).
\]
The **complete ordinary zero forcing polynomial** of \(S_n\), counting every forcing seed set by size, is
\[
\boxed{\mathcal Z_n(z)=z^m\mathcal U_n(z^{-1})\big((1+z)^n-1\big)-n z^{m-n+2}.}
\]
This is an ordinary polynomial: the apparent negative exponents cancel against \(z^m\) because every forest has at most \(n-1\) edges.

Its smallest nonzero degree is \(m-n+2=\binom{n-1}{2}+1\). Every minimum forcing set is uniquely of the form
\[
\{v\}\cup\{x_e:e\in E(K_n)\setminus E(T)\},
\]
where \(v\in[n]\), \(T\) is a spanning tree of \(K_n\), and \(T\) is **not** the star with center \(v\). There are exactly
\[
\boxed{n\big(n^{n-2}-1\big)}
\]
minimum forcing sets.

## Assumptions and scope

All graphs are finite, labeled, simple, and undirected. The zero forcing rule is the ordinary, blue-vertex-only color-change rule, not the skew or positive-semidefinite variant. Subdivisions are single subdivisions of *every* edge. The parameter \(n\) is any integer \(n\ge3\). A cycle is an unrooted, unoriented simple cycle on distinct vertices; this convention accounts for division by two in its count. The empty vertex set is excluded from forts, but the edgeless spanning forest is included in \(\mathcal U_n\). The designation of original vertices is the specified subdivision construction; no quotient by graph automorphisms is taken in the enumerators.

## Proof

**1. Forced cut vertices of a fort.** For a fort \(F\), set \(A=F\cap[n]\) and \(B=\{e\in E:x_e\in F\}\). If \(u\in A\) and \(v\notin A\), then \(x_{\{u,v\}}\in F\): otherwise this subdivision vertex lies outside \(F\) with exactly one neighbor inside, namely \(u\). Thus \(B\) contains the entire edge cut \(\delta(A)\) in \(K_n\).

**2. No original vertices.** If \(A=\varnothing\), the fort condition is exactly that the graph \(([n],B)\) has no vertex of degree one. A nonempty graph with this condition contains a cycle: every nontrivial component has minimum positive degree at least two. The subdivision vertices corresponding to any such cycle form a fort. Conversely, any nonempty proper subset of a simple cycle's edges is a forest containing a degree-one vertex, so the cycle fort is minimal. Therefore all minimal forts with \(A=\varnothing\) are the cycle sets in family 1.

**3. One original vertex.** If \(A=\{v\}\), every \(x_{\{v,u\}}\) belongs to \(F\). For each \(u\ne v\), since \(u\notin F\), at least one subdivision vertex for an edge within \([n]\setminus\{v\}\) incident with \(u\) must also belong to \(F\); otherwise \(u\) has precisely its forced cut neighbor in \(F\). Hence deleting \(v\) from \(F\) leaves a nonempty fort: \(v\) then sees \(n-1\ge2\) subdivision neighbors, and every other original vertex sees at least two. This case yields no minimal fort.

**4. Between two and \(n-2\) original vertices.** If \(2\le|A|\le n-2\), the cut subdivisions \(\{x_e:e\in\delta(A)\}\) alone form a fort: every original vertex in either side of the cut has at least two neighbors in that set; all other subdivision vertices see zero original vertices in the set. This is a strict subset of \(F\), since \(A\ne\varnothing\), so \(F\) is not minimal.

**5. Exactly \(n-1\) or \(n\) originals.** Suppose \(A=[n]\setminus\{v\}\). The cut requirement forces all \(n-1\) incident subdivision vertices of \(v\) into \(F\), and these alone with \(A\) form a fort: the omitted original vertex has \(n-1\ge2\) fort-neighbors and an omitted subdivision vertex internal to \(A\) has two. Any extra subdivision vertex is unnecessary. To show minimality, consider any nonempty subset \(F'\) of this displayed fort. If its original part is a nonempty proper subset of \(A\), some omitted internal subdivision vertex \(x_{\{u,w\}}\), with \(u\) retained and \(w\in A\) removed, has exactly one fort-neighbor. If its original part is empty, its remaining subdivisions are a subset of the star centered at \(v\); any nonempty such subset gives an original leaf exactly one fort-neighbor. With all \(A\) retained, every cut subdivision is forced. Thus the displayed fort is inclusion-minimal. Finally \([n]\) alone is a fort (every subdivision vertex sees both endpoints); a proper nonempty subset of originals fails at a cut subdivision vertex. This proves families 2 and 3 and exhausts all cases.

**6. Enumerating minimal forts.** A simple unoriented cycle of length \(k\) in \(K_n\) is specified by choosing its \(k\) vertices and a cyclic order modulo reversal, giving \(\binom nk(k-1)!/2\) choices. Families 2 and 3 contribute one fort of size \(n\) and \(n\) forts of size \(2n-2\). They are disjoint by their counts of original vertices. This proves \(\mathcal F_n\).

**7. From forts to forcing sets.** A seed set is zero forcing if and only if it meets every fort, equivalently every minimal fort. To see this without an extra hypothesis, if the forcing process stalls with nonempty white set \(W\), no blue vertex has exactly one white neighbor, so \(W\) is a fort disjoint from the initial blue set. Conversely, a fort that starts entirely white stays entirely white: no outside vertex can be the first to force a member of the fort. Every nonempty finite fort contains a minimal fort.

Write a candidate initial set as \(S=A\cup\{x_e:e\in B\}\), with \(A\subseteq[n]\), \(B\subseteq E\). It meets all cycle forts if and only if the graph \(([n],E\setminus B)\) is acyclic, that is, a spanning forest of \(K_n\). It meets the all-original fort if and only if \(A\ne\varnothing\). When \(|A|\ge2\), it automatically meets each fort in family 3 because the original portion of that fort contains every original vertex except one. When \(A=\{v\}\), it meets all family-3 forts except possibly the one indexed by \(v\); the latter is met exactly when \(B\) contains at least one edge incident with \(v\). Thus the **necessary-and-sufficient** seed criterion is
\[
A\ne\varnothing,\qquad ([n],E\setminus B)\text{ is a forest},\qquad
|A|\ge2\ \text{or}\ (A=\{v\}\text{ and }B\cap\delta(v)\ne\varnothing).
\]

**8. The full polynomial.** Every spanning forest with \(j\) edges corresponds to a subdivision-vertex selection of size \(m-j\). Independently choose a nonempty subset \(A\) of the originals, giving a factor \((1+z)^n-1\). The only pairs to remove are those with \(A=\{v\}\) and no chosen subdivision vertex incident to \(v\). For such a pair the omitted forest contains the entire \((n-1)\)-edge star at \(v\); as it is a forest, it must be exactly that star. There is precisely one offending pair for each \(v\), each of weight \(1+m-(n-1)=m-n+2\). Removing these \(n\) pairs gives the displayed \(\mathcal Z_n(z)\). The exponential expression for \(\mathcal U_n\) follows by decomposing a labeled forest into unordered tree components: a component on \(k\) specified labeled vertices has \(k^{k-2}\) trees for \(k\ge2\) (Cayley's formula) and contributes \(k-1\) edges. The standard labeled set construction gives the exponential generating function, with the singleton component count \(c_1=1\).

**9. The minimum layer.** Every forest has at most \(n-1\) edges, hence every forcing seed needs at least \(m-n+1\) subdivision vertices and at least one original. Equality at \(m-n+2\) requires one original \(v\) and an omitted forest of exactly \(n-1\) edges, hence a spanning tree \(T\). The singleton proviso excludes exactly the star centered at \(v\). Conversely every remaining pair is forcing by step 7. Cayley's formula gives \(n^{n-2}\) spanning trees on \([n]\), and exactly one of these is the star centered at each fixed \(v\), proving the exact count \(n(n^{n-2}-1)\). The numerical value \(m-n+2\) was established for complete subdivisions of Hamiltonian graphs in earlier work; the complete classification and enumerators here are the assertions assessed separately.

## Verification

The standalone file `verify.py` uses the adjacency list of the subdivided graph and **independently** implements the ordinary forcing rule. It checks all \(2^{n+\binom n2}\) initial vertex subsets for \(n=3,4,5\), comparing the direct forcing outcome against the stated spanning-forest criterion and every coefficient. Separately, it enumerates all forts and their inclusion-minimal elements, matching the three structural families for those same orders. It checks the minimum coefficients and verifies labeled spanning-tree counts via independent Prüfer-code enumeration through \(n=7\). Run `python3 verify.py`; the final output is `VERIFY_OK`.

The directly checked zero-forcing polynomials begin
\[
\begin{aligned}
\mathcal Z_3(z)&=6z^2+18z^3+15z^4+6z^5+z^6,\\
\mathcal Z_4(z)&=60z^4+156z^5+178z^6+116z^7+45z^8+10z^9+z^{10},\\
\mathcal Z_5(z)&=620z^7+1800z^8+2575z^9+2225z^{10}+1230z^{11}+445z^{12}+105z^{13}+15z^{14}+z^{15}.
\end{aligned}
\]
These finite computations corroborate, but do not establish, the all-\(n\) statement. The proof above supplies the required infinite argument.

## Relationship to prior work

Barrett, Bowcutt, Cutler, Gibelyou, and Owens (2009), as quoted explicitly in Theorem 1.9 of Catral et al. (2012), established the **scalar** zero forcing number \(|E(G)|-|V(G)|+2\) for full subdivisions of a graph with a Hamiltonian path. Since \(K_n\) is Hamiltonian, the scalar \(m-n+2\) is already known and is not an originality claim. Boyer et al. (arXiv:1801.08910v1, 2018) introduced and studied the zero-forcing polynomial and examples in other families. Becker et al. (arXiv:2404.05963v1, 2024) investigated minimal-fort enumeration and proved results for paths, cycles, spiders, and various graph products, but not the full subdivision \(S(K_n)\) in the inspected version. The presently asserted new combination is the explicit three-family fort classification, the full forcing polynomial, and the Cayley enumeration of every minimum forcing set. Generic forest-enumeration and the known scalar alone do not imply this classification without the fort analysis.

## Limitations

These statements concern full one-edge subdivisions of labeled complete graphs only, for \(n\ge3\), under ordinary zero forcing. They do not evaluate the zero forcing polynomial for arbitrary full subdivisions of graphs. The proof is self-contained apart from standard Cayley enumeration and the familiar fort-hitting equivalence, for which a direct argument is also given. The polynomial may have independently appeared under incidence-graph, cycle-transversal, feedback-edge-set, or rooted-spanning-tree terminology; a comprehensive priority guarantee is not possible, and unindexed literature remains a residual risk. No claim about independent mathematical certification is made.

## References

1. W. Barrett, R. Bowcutt, M. Cutler, S. Gibelyou, K. Owens, *Minimum rank of edge subdivisions of graphs*, Electronic Journal of Linear Algebra **18** (2009), 530–563. Cited and theorem identified in reference 2.
2. M. Catral, A. Cepek, L. Hogben, M. Huynh, K. Lazebnik, T. Peters, M. Young, *Zero forcing number, maximum nullity, and path cover number of subdivided graphs*, Electronic Journal of Linear Algebra **23** (2012), 906–922; DOI `10.13001/1081-3810.1565`; especially Theorem 1.9. https://journals.uwyo.edu/index.php/ela/article/download/1131/1131/1131
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (first public 2018-01-26). https://arxiv.org/abs/1801.08910
4. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (first public 2024-04-09). https://arxiv.org/abs/2404.05963
