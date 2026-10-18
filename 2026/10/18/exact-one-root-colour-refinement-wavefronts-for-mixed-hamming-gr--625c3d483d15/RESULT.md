# Exact one-root colour-refinement wavefronts for mixed Hamming graphs

## Finding

Let \(d\geq1\), let \(q_1,\ldots,q_d\geq2\) be integers, and put
\[
G=K_{q_1}\square\cdots\square K_{q_d}.
\]
Mark the vertex \(o=(0,\ldots,0)\) with its own initial colour and give all other vertices one common colour. Starting at round \(0\), perform synchronous one-dimensional counting colour refinement, retaining the old colour in every new signature. Write \(Q\) for the set of distinct factor sizes, \(d_q=|\{i:q_i=q\}|\), \(k_q(x)=|\{i:q_i=q,\ x_i\ne0\}|\), and \(w(x)=\sum_q k_q(x)\).

**Exact partitions at every round.** At each integer round \(0\le t<d\), two vertices have the same colour exactly when one of the following applies:

1. Both have weight less than \(t\) and their full vectors \((k_q)_{q\in Q}\) are equal.
2. Both have weight exactly \(t\).
3. Both have weight greater than \(t\).

At round \(d\), the colour classes are exactly the sets with fixed \((k_q)_{q\in Q}\); these are precisely the automorphism orbits fixing \(o\). The least stable round, i.e., the smallest \(R\) whose partition is unchanged by the next refinement, is
\[
R=\begin{cases}d-1,&|Q|=1,\\d,&|Q|\ge2.\end{cases}
\]
This includes \(d=1\), for which \(R=0\).

The stable partition has \(\prod_{q\in Q}(d_q+1)\) classes. The orbit of profile \((k_q)\) has size
\[
\prod_{q\in Q}\binom{d_q}{k_q}(q-1)^{k_q}.
\]
For \(0\le t<d\) the number of colour classes is
\[
2+\sum_{j=0}^{t-1}[z^j]\prod_{q\in Q}(1+z+\cdots+z^{d_q}),
\]
where the sum is empty when \(t=0\). The weight-\(t\) class contains \([z^t]\prod_i(1+(q_i-1)z)\) vertices, and the weight-above-\(t\) class contains the sum of the coefficients of higher degrees of that same polynomial.

## Assumptions and scope

All graphs are finite, simple and undirected. Every complete factor has at least two vertices, and there are no other initially distinguished vertices. The round count refers to strict *partition changes*, not an extra computational call which detects stability. The conclusion concerns refinement **within this marked graph**, not identification against every competing graph. The heterogeneous case \(|Q|\ge2\) with \(d\ge3\) is the main nonuniform phenomenon; the dimension-two and all-equal-factor boundaries are included for precision.

## Proof

**Step 1: distance and automorphism orbits.** In the Cartesian product, graph distance from \(o\) is \(w(x)\). The neighbours of \(o\) split into disjoint maximal cliques, one for each coordinate, of respective sizes \(q_i-1\), and there are no edges between different such cliques. Any root-fixing automorphism therefore permutes these cliques only when they have equal size, and arbitrarily permutes their members. For a vertex \(x\ne o\), the root neighbours which lie on some shortest path from \(o\) to \(x\) are exactly the one-coordinate vertices \((0,\ldots,x_i,\ldots,0)\) for \(x_i\ne0\). This set uniquely determines \(x\). Hence a root-fixing automorphism is fully specified by permutations of equal-size coordinate cliques and permutations within each clique. Conversely these permutations preserve adjacency. The resulting rooted orbits are exactly the profiles \((k_q(x))_{q\in Q}\), with the claimed multinomial-binomial sizes.

**Step 2: the unsplit wavefront.** Let \(c_t\) be the colouring after round \(t\). By induction, all vertices at distance exactly \(t\) have one common colour under \(c_t\), all at distance greater than \(t\) have one further common colour, and those two colours are distinct from each other and from any earlier layer. At \(t=0\) this is the definition of the initial colouring. Assume it at \(t\). Every vertex at distance \(t+1\) has exactly \(t+1\) neighbours in the preceding distance layer: remove any one nonzero coordinate. All its remaining neighbours have distances at least \(t+1\). Every vertex farther than \(t+1\) has no neighbour within distance \(t\). Since every vertex has the same degree \(\sum_i(q_i-1)\), the round-\(t+1\) signatures are constant within the layer \(t+1\) and within the farther region, but distinct between those two regions. Old colours prevent mixing with earlier layers. This gives the asserted wavefront for all applicable rounds.

**Step 3: recovery behind the wavefront.** At round \(2\), a weight-one vertex supported in a factor of size \(q\) has exactly \(q-2\) neighbours in the weight-one colour from round \(1\). It is thus coloured according to \(q\), precisely its orbit profile. Suppose for \(k\ge2\) that weight-\(k-1\) vertices already have their orbit profiles distinguished by round \(k\). A vertex of weight \(k\) and profile \(\mathbf{k}=(k_q)\) has, for each \(q\) with \(k_q>0\), exactly \(k_q\) neighbours in the predecessor orbit with profile \(\mathbf{k}-\mathbf e_q\). Therefore the multiset of predecessor colours in its round-\(k+1\) signature determines the vector sum
\[
\sum_{q\in Q} k_q(\mathbf{k}-\mathbf e_q)=(k-1)\mathbf{k}.
\]
Because \(k\ge2\), this uniquely determines \(\mathbf{k}\). Rooted automorphisms preserve all refinement colours, so equal profiles are never distinguished. Induction shows that all layers of weight below \(t\) are resolved into full rooted orbits by round \(t\). Step 2 proves that the weight-\(t\) shell and its farther complement are each still one class. This gives exactly the partition claimed at every \(t<d\). At round \(d\), all layers below \(d\) have been resolved, and the last layer consists of one orbit; hence the partition is stable and orbit-exact.

**Step 4: sharp stabilization.** If every factor has the same size, there is precisely one rooted orbit at each distance. The distance shells are all separate at round \(d-1\), so that round is already stable. At every round \(t<d-1\), the wavefront merges distinct distances \(t+1\) and higher, so stability has not been reached. If there are two different factor sizes, the weight-\(d-1\) shell has at least two rooted orbits (depending on the size of the single omitted coordinate), yet Step 2 says it is a single colour class at round \(d-1\). That shell splits at round \(d\), so the least stable round is exactly \(d\).

Finally, an orbit profile is a choice \(0\le k_q\le d_q\) for each distinct factor size, giving the stated product count and orbit-size formula. At round \(t<d\), each orbit profile of total weight below \(t\) is one class, followed by the two unsplit regions; counting profiles by their generating polynomial proves the intermediate class formula. The shell sizes follow by taking coefficients in the ordinary Hamming-distance enumerator.

## Verification

The standalone script `verify_graph.py` constructs the full Cartesian-product graph from coordinate tuples, executes direct neighbour-multiset colour refinement, and compares **every partition at every round** against the theorem for eighteen factor lists, totalling 2,859 graph vertices. The separate script `verify_quotient.py` constructs a multiplicity-weighted orbit quotient and checks the same exact wavefront, class counts and sharp stabilization for 3,014 factor lists and 126,596 quotient states. Both scripts include all-equal and unequal factor sizes, repeated factors, and binary/nonbinary mixtures. Run with standard-library Python 3 using `python verify_graph.py` and `python verify_quotient.py`; their captured standard outputs are `graph_output.txt` and `quotient_output.txt`. Their finite tests are corroboration, not the dimension-uniform proof.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky describe stable counting colour refinement, its counting-logic interpretation and the orbit-refinable property, without a mixed-Hamming-product round-by-round theorem [1]. Imrich and Klavžar study Cartesian products of complete graphs and their canonical coordinate labels in graph recognition, but do not analyse counting-colour-refinement wavefronts [2]. The classical Cartesian prime-factor automorphism decomposition recalled by Bailey and Cameron implies the group-theoretic part of Step 1 but not the refinement iterations [3]. The two-factor rook-graph instance and the all-binary hypercube boundary overlap previously studied cases; the main claim here is the **heterogeneous, arbitrarily-many-factor exact wavefront and sharp stabilization dichotomy**, including exact sizes at every round. A later perfect-two-colouring study concerns equitable two-partitions of equal-alphabet Hamming graphs, not the particular singleton-root refinement sequence [4]. The inspected sources do not establish this combination of statements.

## Limitations

The theorem does not assert graph identification against arbitrary competitors, multi-landmark behavior, arbitrary Cartesian factors, or a faster graph-isomorphism algorithm. Priority against an unlocated specialized source cannot be certified by a bounded search.

## References

[1] V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255 .

[2] W. Imrich and S. Klavžar, *On the Complexity of Recognizing Hamming Graphs and Related Classes of Graphs*, European Journal of Combinatorics 17 (1996), 209–221, https://users.fmf.uni-lj.si/klavzar/preprints/complex-phg.pdf .

[3] R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, https://maths.qmul.ac.uk/~pjc/preprints/bsod.pdf (particularly its account of Sabidussi's Cartesian-product automorphism theorem).

[4] E. Bespalov, D. Krotov, A. Matiushev, A. Taranenko and K. Vorob'ev, *Perfect 2-colorings of Hamming graphs*, arXiv:1911.13151, https://arxiv.org/abs/1911.13151 .
