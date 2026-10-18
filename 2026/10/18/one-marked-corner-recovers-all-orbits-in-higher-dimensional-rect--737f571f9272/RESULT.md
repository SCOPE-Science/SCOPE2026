# One marked corner recovers all orbits in higher-dimensional rectangular grids

## Finding
Let \(d\ge3\) and \(n_1,\ldots,n_d\ge2\) be arbitrary integers. Let \(G=P_{n_1}\square\cdots\square P_{n_d}\) be the finite simple Cartesian product of paths, with vertex set \(V=\prod_{i=1}^d\{0,\ldots,n_i-1\}\) and an edge between tuples differing by one in exactly one coordinate. Give the origin \(o=(0,\ldots,0)\) its own colour and every other vertex one common initial colour. Then the stable partition of ordinary one-dimensional counting colour refinement is **exactly the orbit partition** of the automorphism group of \(G\) fixing \(o\).

More precisely, set \(L_i=n_i-1\). Two vertices \(x,y\) have the same stable colour if and only if their **joint distance-to-the-two-corners multisets** agree:
\[
\{\!\{(x_i,L_i-x_i):1\le i\le d\}\!\}
=\{\!\{(y_i,L_i-y_i):1\le i\le d\}\!\}.
\]
Equivalently, for every factor length \(m\), the multisets of coordinate values over indices with \(n_i=m\) agree. If \(r_m=|\{i:n_i=m\}|\), the exact number of stable classes is
\[
N=\prod_{m:r_m>0}\binom{r_m+m-1}{m-1}.
\]
For a class with \(c_{m,a}\) coordinates of length \(m\) taking value \(a\), its size is
\[
|C|=\prod_{m:r_m>0}\frac{r_m!}{\prod_{a=0}^{m-1}c_{m,a}!},
\qquad\sum_{a=0}^{m-1}c_{m,a}=r_m.
\]
In particular, when all factor lengths differ, every stable class is a singleton; when all factors have length two, there are exactly \(d+1\) classes. The argument also works for \(d=1,2\), but novelty is claimed only for higher dimensions.

## Assumptions and scope
All paths have at least two vertices and all edges are undirected and unlabelled. A product corner means a vertex all of whose coordinates are endpoints; coordinate reflections reduce an arbitrary product corner to the displayed origin. Refinement begins with exactly two initial colours, singleton at the corner and uniform elsewhere, and iterates the signature consisting of the old colour and the multiset of neighbour colours. The theorem is about **within-graph automorphism orbits**, not identification against an arbitrary nonisomorphic graph, and does not claim an optimal number of refinement rounds.

## Proof
Write \(L_i=n_i-1\) and \(D=\sum_iL_i\). For a vertex \(x\), define its lower rank \(r(x)=\sum_i x_i\), its upper rank \(D-r(x)=\sum_i(L_i-x_i)\), and the two ordinary coordinate multisets
\[
A(x)=\{\!\{x_1,\ldots,x_d\}\!\},\qquad
B(x)=\{\!\{L_1-x_1,\ldots,L_d-x_d\}\!\}.
\]
We show that the stable colour recovers \(A(x)\) and \(B(x)\), then determines their **coordinatewise pairing**.

**1. Rank layers and both distinguished corners are visible.** Any equitable partition refining the singleton origin has every cell contained in a distance layer around it. Indeed, begin with the origin cell; inductively a cell has vertices with a neighbour in the preceding union of distance layers either everywhere or nowhere, because all its vertices have the same number of neighbours in each already identified cell. Therefore the least distance from the origin is constant on each cell. In the Cartesian grid this distance is \(r(x)\). The unique vertex at maximum distance \(D\) is \(t=(L_1,\ldots,L_d)\), so \(t\) also forms a singleton stable cell. Repeating the same argument from this singleton shows that \(D-r(x)\), too, is stable-colour-invariant.

**2. Reconstruct the multiset of lower coordinate values from predecessor cards.** We prove by induction on \(r(x)\) that the stable colour determines \(A(x)\). At rank zero the tuple is the origin. Suppose it is known at rank \(r-1\) and consider a vertex \(x\) of rank \(r>0\). Its predecessor neighbours, lying at rank \(r-1\), are exactly \(x-e_i\) for all indices with \(x_i>0\). Equitability tells us, from the stable colour of \(x\), the complete multiset of their stable colours; the induction hypothesis turns this into the multiset \(\mathcal D_A(x)\) of predecessor coordinate multisets.

Let \(a_j\) be the number of coordinates of \(x\) equal to \(j\), and let \(p\) be the number of predecessor neighbours. Then \(a_0=d-p\). For each \(j\ge0\), let \(S_j\) be the sum, over all \(p\) predecessor cards, of the multiplicity of \(j\) in that card. A coordinate with value \(j\ge1\) is decremented in exactly one card, while a coordinate with value \(j+1\) creates one extra occurrence of \(j\). Hence
\[
S_0=p a_0+a_1,\qquad
S_j=(p-1)a_j+a_{j+1}\quad(j\ge1).
\]
These triangular equations recover the entire multiplicity sequence:
\[
a_0=d-p,\quad a_1=S_0-pa_0,\quad a_{j+1}=S_j-(p-1)a_j\quad(j\ge1).
\]
Only finitely many nonzero values occur. Thus \(A(x)\) is determined by its stable colour for every vertex.

**3. Reconstruct the upper coordinate multiset.** Apply the same argument to the unique opposite corner \(t\), using the rank from \(t\), namely \(D-r(x)\). A predecessor toward \(t\) is an upper neighbour \(x+e_i\), existing whenever \(L_i-x_i>0\). The reflection \(x\mapsto(L_i-x_i)_i\) identifies the same triangular deck formulas. Because \(t\) already forms a singleton stable cell, its distance layers and neighbour-card multiplicities are visible to the *original* stable colouring; no second initial marker has been introduced. This proves that \(B(x)\) is determined by the same original stable colour.

**4. Pair the two multisets.** Write \(b_i=L_i-x_i\). For each predecessor \(u=x-e_i\), its known pair of multisets satisfies
\[
A(u)=A(x)-[x_i]+[x_i-1],\quad
B(u)=B(x)-[b_i]+[b_i+1].
\]
Here \([a]\) denotes one occurrence of integer \(a\). The signed differences identify the unique pair \((x_i,b_i)\) with \(x_i>0\): the removed lower value is \(x_i\), and the removed upper value is \(b_i\). The multiset of stable colours of predecessor neighbours therefore gives all such pairs with their full multiplicities. For coordinates with \(x_i=0\), we instead inspect the successor \(u=x+e_i\), whose known multisets change by \(-[0]+[1]\) and \(-[b_i]+[b_i-1]\). The signed difference recovers \((0,b_i)\). This covers every remaining coordinate, because \(b_i=L_i\ge1\) whenever \(x_i=0\). Equitability supplies the successor-card multiset as well. Consequently the stable colour determines
\[
J(x)=\{\!\{(x_i,b_i):1\le i\le d\}\!\}.
\]
The pairs also recover the factor lengths \(n_i=x_i+b_i+1\), so this is precisely the multiset of coordinate values grouped by factor length. A potentially important distinction is that \(A(x)\) and \(B(x)\) *separately* need not determine the pairing: in \(P_2\square P_3\square P_4\), vertices \((0,2,1)\) and \((1,0,2)\) have both ordinary coordinate multisets equal to \(\{0,1,2\}\) but different \(J\). The neighbour-pairing argument is necessary.

**5. Orbit equivalence and enumeration.** For each fixed length \(m\), permuting factors of length \(m\) is a graph automorphism fixing the origin. If \(J(x)=J(y)\), suitable independent permutations of equal-length factors carry \(x\) to \(y\). Thus each \(J\)-class lies in a single rooted automorphism orbit. Step 4 proves that a stable cell lies inside a \(J\)-class; conversely any rooted automorphism preserves every refinement colour, so the stable partition cannot split an orbit. All three partitions are equal. Counting multisets of size \(r_m\) on \(m\) possible coordinate values gives \(\binom{r_m+m-1}{m-1}\) options; multiplying independent choices gives \(N\). A fixed multiset has \(r_m!/\prod_a c_{m,a}!\) orderings; multiplication yields the stated cell sizes. \(\square\)

## Verification
Four standalone programs accompany the proof. `verify_direct.py` constructs individual vertices and edges and runs rooted synchronous refinement for 239 unordered factor tuples, totaling 124,767 explicitly inspected vertices, checking exact class counts and cell sizes. `verify_quotient.py` independently refines the weighted occupancy-state graph for 188 factor tuples, totaling 24,015 quotient states. `verify_orbits.py` uses exact root-preserving graph automorphism enumeration on seven representative small grids, checking colours against actual orbit partitions rather than relying on the predicted group. `verify_reconstruction.py` verifies both triangular deck identities and the final coordinate-pair recovery for 106 tuples and 31,285 vertices. Their recorded standard outputs are embedded alongside the programs. To rerun the first, second, and fourth checks, run `python3 verify_direct.py`, `python3 verify_quotient.py`, `python3 verify_reconstruction.py` with Python 3. The third uses `networkx` version 3.6 or compatible. All four checks passed when run from the accompanying source files. Finite tests corroborate but do not replace the all-dimension proof.

## Relationship to prior work
Arvind, Köbler, Rattan, and Verbitsky (2015) develop the distinction between stable refinement cells and graph automorphism orbits and study refinable and amenable graphs. Their inspected paper treats general graph classes, not this explicit corner-marked product theorem. Boiko and collaborators (2014) give a Cartesian-product factorisation and automorphism framework, but not a colour-refinement theorem for a distinguished corner.

A related earlier mathematical result handles **two-dimensional** corner-marked path products and even determines their precise stabilization rounds. That statement covers \(d=2\), but does not imply the higher-dimensional result. Another related result proves orbit recovery for finite **products of chains equipped with the full strict coordinatewise order relation**, using counts over all strict predecessors and successors. A grid graph contains only **unit cover edges** and uses a single initial corner marker; predecessor/filter counts from the full order cannot simply be read in one graph-refinement round. The joint-multiset reconstruction above supplies a separate proof in this weaker adjacency language. Product graphs of complete factors likewise have different adjacency and do not subsume path-factor products. No equivalence or dominating coverage was identified in the inspected literature and accessible research records; this is not a certification of publication priority.

## Limitations
The theorem concerns finite products of **paths**, not arbitrary Cartesian products or graphs with cycles, and a marked **corner**, not an arbitrary vertex. It does not identify the product against arbitrary other graph families and supplies no exact stabilization-depth formula in dimension at least three. The formula for class sizes assumes the specified labelled factor decomposition, but no canonical-factorisation theorem is needed for the orbit proof. The conclusion applies to every finite dimension \(d\ge3\) with factors of length at least two. An earlier specialized theorem may have escaped the literature comparison. No independent mathematical audit has been performed.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v1, first public 2015-02-04, particularly Sections 1, 2 and 8. https://arxiv.org/abs/1502.01255
2. T. Boiko, J. Cuno, W. Imrich, F. Lehner, C. E. van de Woestijne, *The Cartesian product of graphs with loops*, arXiv:1411.6887v1, first public 2014-11-25, particularly Sections 1 and 3. https://arxiv.org/abs/1411.6887
3. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383v1, first public 2016-06-14, abstract consulted for background and related limitations. https://arxiv.org/abs/1606.04383
