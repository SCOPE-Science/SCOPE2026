# The independent double Roman weight enumerator of leaf coronas
## Finding
Let \(G=(V,E)\) be any finite simple graph of order \(n\ge1\); disconnected graphs and isolated vertices are permitted. Write \(X=G\circ K_1\) for the leaf corona with core \(V\) and a private pendant vertex \(v'\) attached to each \(v\in V\).

Define the independent double Roman weight enumerator
\[
\mathcal F_X(z)=\sum_{f\in\operatorname{IDRDF}(X)}z^{\omega(f)},
\]
and define the independent-set open-neighborhood enumerator
\[
\mathcal B_G(x)=\sum_{I\subseteq V\colon I\text{ independent}}x^{|N_G(I)|}.
\]
Here \(N_G(I)=\{v\in V\setminus I:\exists u\in I,\ uv\in E\}\) is the open neighborhood of the set \(I\), and the empty set contributes one term to \(\mathcal B_G\).

**Exact transform and complete function classification.** For every finite simple graph \(G\) as above,
\[
\boxed{\mathcal F_{G\circ K_1}(z)
=\sum_{I\,\text{independent}}z^{3n-|N_G(I)|}(1+z)^{|N_G(I)|}
=z^{3n}\mathcal B_G(1+z^{-1}).}
\]
There is a canonical bijection from feasible functions to pairs \((I,J)\) with \(I\subseteq V\) independent and \(J\subseteq N_G(I)\). Its labeling is
\[
\begin{aligned}
f(v)&=3,\quad f(v')=0 &&\text{if }v\in I,\\
f(v)&=0,\quad f(v')=2 &&\text{if }v\in J,\\
f(v)&=0,\quad f(v')=3 &&\text{if }v\notin I\cup J.
\end{aligned}
\]
The weight is \(3n-|J|\).

**Minimum and optimal count.** Let \(i(G)\) denote independent domination, namely the minimum cardinality of a maximal independent vertex set. Then
\[
\boxed{i_{dR}(G\circ K_1)=2n+i(G),}
\qquad
\boxed{\#\operatorname{Opt}(G\circ K_1)=[x^{n-i(G)}]\mathcal B_G(x).}
\]
The transform is reversible:
\[
\mathcal B_G(x)=(x-1)^{3n}\mathcal F_{G\circ K_1}((x-1)^{-1}).
\]
The substitution is understood as a polynomial identity after cancellation, not a numeric evaluation at \(x=1\).

## Assumptions and scope
An independent double Roman dominating function (IDRDF) on a graph \(H\) is a map \(f:V(H)\to\{0,1,2,3\}\) for which the positive support \(\{v:f(v)>0\}\) is independent; every vertex labeled \(0\) has a neighbor labeled \(3\) or at least two distinct neighbors labeled \(2\); and every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\). Its weight is \(\omega(f)=\sum_{v\in V(H)}f(v)\). The minimum weight is \(i_{dR}(H)\).

All graph vertices are distinct, and the private leaf \(v'\) is adjacent only to its corresponding core vertex \(v\). A graph may contain isolated core vertices; the corona itself has no isolated vertices. The label-counting polynomial distinguishes all functions on labeled vertices, not equivalence classes under graph automorphisms.

## Proof
**Step 1: Labels and private-pair rigidity.** In any IDRDF, label \(1\) is impossible: it requires an adjacent vertex with label at least \(2\), contrary to independence of the positive support. For each private pair \(vv'\), the leaf and its core cannot both be positive. They cannot both be zero, because then the degree-one leaf \(v'\) has no label-\(3\) neighbor and cannot have two label-\(2\) neighbors. If \(f(v)>0\), then \(f(v')=0\), and the leaf condition forces \(f(v)=3\). If \(f(v)=0\), then \(f(v')\in\{2,3\}\). Thus exactly the three local states \((3,0)\), \((0,2)\), and \((0,3)\) are possible.

**Step 2: Characterize feasible configurations.** Let \(I=\{v\in V:f(v)=3\}\). Because the support is independent, \(I\) is independent in \(G\). For \(v\notin I\) the core has label \(0\). If \(f(v')=2\), then the only possible label-\(3\) neighbor of \(v\) is a core neighbor in \(I\), and no distinct label-\(2\) core neighbors exist. Therefore \(v\in N_G(I)\) is necessary. It is also sufficient: any adjacent label-\(3\) core vertex defends \(v\). If \(f(v')=3\), then \(v\) is defended by its own private leaf, regardless of the core neighborhood. Consequently the set \(J=\{v:f(v')=2\}\) is an arbitrary subset of \(N_G(I)\). Conversely, every independent \(I\) and every \(J\subseteq N_G(I)\) yield a feasible IDRDF by the displayed assignment. The maps \(f\mapsto(I,J)\) and \((I,J)\mapsto f\) are inverse, proving the bijection.

**Step 3: Count by weight.** Each of the \(n\) private pairs contributes weight \(3\) except that every \(v\in J\) contributes weight \(2\). Thus \(\omega(f)=3n-|J|\). For a fixed independent \(I\) with \(|N_G(I)|=k\), summing over the arbitrary subsets \(J\subseteq N_G(I)\) gives
\[
\sum_{J\subseteq N_G(I)}z^{3n-|J|}=z^{3n-k}(1+z)^k.
\]
Sum over independent \(I\) to obtain the polynomial transform. Its inverse is the formal substitution \(z=(x-1)^{-1}\) followed by multiplication by \((x-1)^{3n}\).

**Step 4: Identify the minimum.** Every independent \(I\) extends to a maximal independent set \(D\supseteq I\). Since \(N_G(I)\subseteq N_G(D)\) and \(D\) dominates \(G\),
\[
|N_G(I)|\le |N_G(D)|=n-|D|\le n-i(G).
\]
A minimum maximal independent set \(D\) has order \(i(G)\), and \(|N_G(D)|=n-i(G)\), so this upper bound is attained. It follows that the least possible weight is
\[
3n-(n-i(G))=2n+i(G).
\]
For a function to attain this weight, its independent core set \(I\) must satisfy \(|N_G(I)|=n-i(G)\), and its optional \(2\)-leaves must be chosen at *every* vertex in \(N_G(I)\); the choice \(J=N_G(I)\) is then forced. Hence the minimum-function count is precisely the indicated top coefficient of \(\mathcal B_G\). Note that such maximizing \(I\) need not themselves be maximal independent sets.

## Verification
The included `verify_idrd_corona.py` independently constructs every leaf corona, checks the exact label predicate on every vertex, enumerates all \(4^{2n}\) assignments, and independently computes both sides of the polynomial identity from independent subsets of the base graph.

It exhaustively checks **all labeled simple graphs** of orders \(1,2,3,4\), namely \(1+2+8+64=75\) base graphs, and four additional five-vertex graphs (the path, cycle, star, and complete graph). Across these \(79\) base graphs, it tests \(8{,}421{,}904\) full assignments, as counted in the included output. For every case the *entire* feasible-function weight polynomial agrees with the transform, and the minimum weight agrees with \(2n+i(G)\).

A concrete optimizer-count distinction occurs on the four-vertex path \(P_4\): the base has independent domination number \(2\), hence its corona minimum is \(10\), but there are **five** minimum IDRDFs, whereas there are only **three** minimum independent dominating sets of \(P_4\). This illustrates why a scalar minimum result cannot determine the new optimizer enumeration.

The exhaustive calculations are corroborative only; the arbitrary-order formula follows from the bijection proved above.

## Relationship to prior work
The independent double Roman domination predicate and its graph-theoretic classification \(05C69\) appear in the 9 April 2019 public first version of Mojdeh and Mansouri (arXiv:1904.04788v1). Their work proves general bounds and exact values for paths, cycles, and some standard families; its later tree construction invokes a specific corona but does not provide a full all-function corona enumerator.

The closest direct leaf-corona comparison is Nahani Pour, Abdollahzadeh Ahangar, Chellali, and Sheikholeslami (2022), especially their Theorem 3. That theorem characterizes **trees** of order \(N\) attaining the extremal \(5N/4\) independent double Roman value as certain leaf coronas \(H\circ K_1\) with \(i(H)=|V(H)|/2\). Its proof uses labels \(3\) on an independent dominating set and labels \(2\) on complementary leaves. The present result does **not** claim that restricted extremal construction as new: it classifies and counts *every feasible function* for **every finite simple base graph**, including disconnected bases, and gives the invertible weight-distribution transform and optimal-count coefficient.

Outer independent double Roman domination, also treated in the literature on corona graphs, is a distinct invariant: it requires the *zero* set to be independent instead of the *positive* support. Its general corona formulas do not imply the present IDRDF polynomial.

## Limitations
The transform is restricted to the corona operation with one private leaf attached to each core vertex; it does not cover larger attached graphs or general graph products. The polynomial \(\mathcal B_G\) records independent-set neighborhood sizes and is not claimed to reconstruct the base graph up to isomorphism. The minimum formula alone is not the main novelty: a restricted tree-corona extremal construction was previously known. No claim is made that the independent-set open-neighborhood enumerator was previously unknown under every possible name. Published-paper overlap was checked by definitions, the relevant theorems, and indexed literature, but a nonindexed same-parameter enumeration could remain undiscovered; the 2022 publisher PDF was not accessible for complete page-by-page inspection. The arbitrary-order proof is symbolic, and the exhaustive verifier stops at order five.

## References
1. D. A. Mojdeh and Z. Mansouri, *Independent double Roman domination in graphs*, arXiv:1904.04788v1, first public 9 April 2019; subsequent article in *Bulletin of the Iranian Mathematical Society* (2020).
2. F. Nahani Pour, H. Abdollahzadeh Ahangar, M. Chellali, and S. M. Sheikholeslami, *An improved upper bound on the independent double Roman domination number of trees*, *AKCE International Journal of Graphs and Combinatorics* 19 (2022), 206–210, DOI:10.1080/09728600.2022.2094735, published online 12 July 2022.
3. D. Rupnik Poklukar and J. Žerovnik, *Double Roman Domination: A Survey*, *Mathematics* 11 (2023), 351, DOI:10.3390/math11020351.
4. H. Abdollahzadeh Ahangar et al., *Outer independent double Roman domination number of graphs*, arXiv:1909.01775v1 (2019); different independence convention (zero set rather than positive support).
