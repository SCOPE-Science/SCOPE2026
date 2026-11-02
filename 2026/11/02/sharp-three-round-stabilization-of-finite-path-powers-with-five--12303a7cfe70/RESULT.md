# Sharp three-round stabilization of finite path powers with five boundary profiles

## Finding
Let \(P_n^{[r]}\) be the undirected graph on \(\{1,\ldots,n\}\), with two distinct vertices adjacent precisely when their difference in absolute value is at most \(r\). Work in pure first-order graph logic with equality and undirected adjacency. For all integers \(r,s\ge2\) and \(m\ge4r+3\), \(n\ge4s+3\),
\[
P_m^{[r]}\equiv_3 P_n^{[s]}.
\]
Thus the two-parameter family of sufficiently long, noncomplete path powers has **one common quantifier-rank-three theory even across different powers**. The threshold \(4r+3\) is sharp for every fixed \(r\ge2\):
\[
P_{4r+2}^{[r]}\not\equiv_3 P_{4r+3}^{[r]}.
\]
There are exactly five possible one-point two-round types within every graph in this common tail. The least-order path-power graph in this tail equivalence class is \(P_{11}^{[2]}\), with eleven vertices. Moreover, this tail class is distinct at rank three from every sufficiently long noncomplete cycle power \(C_n^{[s]}\) with \(n\ge4s+3\).

## Assumptions and scope
Parameters are integers with \(r,s\ge2\) and \(m\ge4r+3\), \(n\ge4s+3\). Graphs are simple and undirected. The adjacency language has no distinguished endpoints, distance predicates, linear order, or counting quantifiers. \(G\equiv_3 H\) means agreement on every first-order sentence of quantifier rank at most three, equivalently a winning three-move Ehrenfeucht–Fraïssé strategy for Duplicator.

For a fixed first vertex \(x\) and a distinct second vertex \(y\), let \(b\in\{0,1\}\) be the adjacency indicator of \(x,y\). Let \(M(x,y)\) be the four-bit integer mask in which bit \(2a+c\) is set if and only if a third vertex \(z\notin\{x,y\}\) exists with adjacency indicators \(E(x,z)=a\), \(E(y,z)=c\), for \(a,c\in\{0,1\}\). Thus the bit weights of patterns \(00,01,10,11\) are respectively \(1,2,4,8\). Define the pointed profile \(S(x)=\{(b,M(x,y)):y\ne x\}\). Second-move repetition \(y=x\) is handled separately in the proof.

## Proof
**Pair-extension lemma.** Fix \(r\ge2\), \(n\ge4r+3\), and \(1\le x<y\le n\), writing \(d=y-x\). The third-vertex patterns have the following exact criteria:

- Pattern \(00\) is always possible. Indeed the two closed radius-\(r\) neighborhoods jointly contain at most \(4r+2<n\) vertices.
- Pattern \(11\) is possible exactly when \(d\le2r\). If \(d\ge2\), a point between \(x\) and \(y\) in the overlap witnesses it. For \(d=1\), one of the two immediately external positions is available, and \(r\ge2\) makes it adjacent to both.
- Pattern \(10\) is **absent** exactly if \(y\le r+1\), or \((x,y)=(1,r+2)\).
- Pattern \(01\) is **absent** exactly if \(x\ge n-r\), or \((x,y)=(n-r-1,n)\).

For the final two assertions, put \(I_t=[\max(1,t-r),\min(n,t+r)]\cap\mathbb Z\). Since \(x<y\), private neighbors of \(x\) must occur in the left difference \(I_x\setminus I_y\). This difference is empty when \(y\le r+1\), and otherwise it contains a vertex other than \(x,y\) except when it is the singleton \(\{x\}\) at \((x,y)=(1,r+2)\). Reflection gives the statement for private neighbors of \(y\). This also proves the lemma for all integer parameters, not just tested instances.

**Five pointed profiles.** Write \(a(x)=\min\{x-1,n-x\}\). Applying the pair-extension lemma and allowing either order of the pair gives the following *complete* table, where each entry is the set \(S(x)\) of pairs \((b,M)\):

| Distance of \(x\) from nearer endpoint | Exact pointed profile \(S(x)\) |
|---|---|
| \(a=0\) | \(\{(0,7),(0,11),(0,15),(1,11)\}\) |
| \(1\le a\le r-1\) | \(\{(0,7),(0,15),(1,11),(1,13),(1,15)\}\) |
| \(a=r\) | \(\{(0,7),(0,15),(1,13),(1,15)\}\) |
| \(a=r+1\) | \(\{(0,7),(0,13),(0,15),(1,15)\}\) |
| \(a\ge r+2\) | \(\{(0,7),(0,15),(1,15)\}\) |

The pair-extension criteria rule out any other pairs in these five rows. To establish *attainment* symbolically, reflect the path if necessary so that \(x=a+1\) lies in its left half. The following witnesses \(y\) realize every listed profile entry, with entries listed in precisely the same order as in the preceding table:

| Regime | Explicit witness vertices \(y\) for successive entries of \(S(x)\) |
|---|---|
| \(a=0\) | \(2r+2,\ r+2,\ r+3,\ 2\) |
| \(1\le a<r\) | \(x+2r+1,\ x+r+1,\ x+1,\ 1,\ x+r\) |
| \(a=r\) | \(x+2r+1,\ x+r+1,\ 1,\ x+1\) |
| \(a=r+1\) | \(x+2r+1,\ 1,\ x+r+1,\ x+1\) |
| \(a\ge r+2\) | \(x+2r+1,\ x+r+1,\ x+1\) |

For instance, when \(a=r+1\) the choice \(y=1\) exploits the unique left-endpoint exception and realizes the nonadjacent mask \(13\). Every witness belongs to \(\{1,\ldots,n\}\) and differs from \(x\), because \(r\ge2\), \(n\ge4r+3\), and \(x\le(n+1)/2\). Substitution in the proved pair-extension lemma gives the displayed masks. Thus all five distance regimes are nonempty for \(r\ge2\) and have distinct *exact* profiles for every permitted parameter, not merely for tested instances.

**Three-round strategy.** For a first choice \(x\), respond with a vertex \(x'\) whose distance to its nearer endpoint lies in the same one of the five regimes. If the second choice repeats the first, repeat it; every vertex has both adjacent and nonadjacent alternatives, so the third choice can be matched. Otherwise, use equality of \(S(x)\) and \(S(x')\) to choose a second vertex with the same adjacency bit \(b\) and mask \(M\). The third choice is either a repeated vertex (match equality) or belongs to one of the four indicated adjacency patterns (match the same occupied bit). This maintains every atomic equality and adjacency relation among all three selected vertices. The strategy is symmetric because the profiles agree in both directions; hence all stated tail graphs are rank-three equivalent.

**Sharpness.** The rank-three sentence
\[
\exists x\,\exists y\,\forall z\;[z=x\lor z=y\lor E(x,z)\lor E(y,z)]
\]
asserts domination by at most two vertices. It holds in \(P_{4r+2}^{[r]}\), taking \(x=r+1\) and \(y=3r+2\). It fails in any \(P_n^{[r]}\) with \(n\ge4r+3\), because two closed radius-\(r\) neighborhoods cover at most \(4r+2\) vertices. This proves sharpness for every radius.

**Least representative and cyclic separation.** Every smaller complete path power is distinguished by the rank-two sentence \(\exists u\,\exists v\,[u\ne v\land\neg E(u,v)]\), which holds in \(P_{11}^{[2]}\) but not in a complete graph. Every other noncomplete path power on fewer than eleven vertices has a different complete three-round type from \(P_{11}^{[2]}\), as verified by a fully exhaustive recursion over all \(36\) parameter pairs \(3\le n\le10\), \(1\le r\le n-2\); the code constructs the full labelled atomic diagrams, including repeated choices. The pair-profile proof establishes that the eleven-vertex graph belongs to the common tail. Finally, the rank-three sentence
\[
\exists x\,\exists y\,[x\ne y\land E(x,y)\land\forall z\,(z=x\lor z=y\lor\neg E(x,z)\lor E(y,z))]
\]
holds in every path power \(P_n^{[r]}\) with \(r\ge2\) (take \(x=1,y=2\)), but fails in each \(C_n^{[s]}\) with \(n\ge4s+3\): for every directed adjacent pair, a radius-\(s\) neighbor of the first vertex on its far side is not adjacent to the second. Thus the stable path and cycle classes remain logically separate even though their sharp thresholds have the same linear form.

## Verification
The standalone standard-library program `verify_pathpowers_rank3.py` implements both the integer pair-mask criteria and an independent exact recursive computation of complete three-round first-order types, including all repeated choices. It checked \(89{,}205\) pairs in \(90\) stable graphs, complete tail equivalences for the representatives \((n,r)=(11,2),(15,3),(19,4),(23,5),(27,6)\), boundary separation for the preceding parameters, all \(36\) smaller noncomplete path-power parameter pairs, and an explicit stable cycle comparison. A second implementation `check_pathpair_formula.py` independently enumerated third vertices and verified \(105{,}200\) pairs across \(96\) stable graphs. The recorded stdout files and `reproduce.sh` allow byte-for-byte replay with Python 3. These finite checks corroborate the already-proved all-parameter interval lemma and do not substitute for its infinite proof.

## Relationship to prior work
Brown and Hoshino (2007) completely analyze Ehrenfeucht–Fraïssé games on **ordinary** paths and cycles (radius one). Their results do not assert equivalence across different path-power radii or the five boundary profiles given here. Ganian et al. (2015) develop efficient first-order model checking for interval graphs whose representations use a fixed finite set of interval lengths, but do not state this sharp parameter-dependent three-round stabilization. Foucaud et al. (arXiv:1505.03459) study geometric representations preserved under graph powers, without quantifier-rank-three classification. Related rank-three analyses of **cycle powers** have the same stable threshold shape but do not imply the path result: cyclic vertex transitivity removes the boundary types that are essential to the five-profile proof, and the last sentence in the proof explicitly distinguishes the stable families.

## Limitations
This result does **not** give the full classification of shorter path powers, any rank-four statement, or equivalence in languages naming endpoints, order, distance, or counting. The least-representative assertion uses an exhaustive finite program for all smaller noncomplete members, whereas the infinite stabilization and separation are mathematical proofs. The literature comparison supports best-knowledge originality, not a definitive historical priority guarantee. No independent mathematical audit has been performed.

## References
1. J. I. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. R. Ganian, P. Hliněný, D. Král’, J. Obdržálek, J. Schwartz, J. Teska, “FO Model Checking of Interval Graphs,” *Logical Methods in Computer Science* **11** (2015), 4:11, arXiv:1302.6043. https://arxiv.org/pdf/1302.6043
3. F. Foucaud, R. Naserasr, A. Parreau, P. Valicov, “On Powers of Interval Graphs and Their Orders,” arXiv:1505.03459 (2015; revised 2021). https://arxiv.org/pdf/1505.03459
