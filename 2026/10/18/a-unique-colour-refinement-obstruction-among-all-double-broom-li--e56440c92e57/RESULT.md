# A unique colour-refinement obstruction among all double-broom line graphs

## Finding

Let \(a,b\ge 2\) and \(\ell\ge 1\) be integers. Construct the double-broom tree \(T_{a,b,\ell}\) from a path of \(\ell\) edges by attaching \(a\) new leaves to its first endpoint and \(b\) new leaves to its last endpoint. Let \(G_{a,b,\ell}=L(T_{a,b,\ell})\), the simple line graph whose vertices are the edges of the tree. Run ordinary synchronous one-dimensional counting colour refinement on \(G_{a,b,\ell}\) from a single uniform vertex colour.

**Theorem.** The stable colour classes are exactly the full automorphism orbits of \(G_{a,b,\ell}\) for every parameter triple **except** \((a,b,\ell)=(2,2,4)\), up to swapping \(a,b\). In the exception the stable classes have sizes \(2,6\), but the automorphism orbits have sizes \(2,4,2\).

For all triples, the full orbit partition has the following explicit form. If \(a\ne b\), each individual spine-edge vertex is its own orbit, while the \(a\) left leaf-edge vertices form one orbit and the \(b\) right leaf-edge vertices form another: there are \(\ell+2\) orbits. If \(a=b\), opposite spine positions \(i\) and \(\ell-1-i\) form one orbit, and all \(2a\) leaf-edge vertices form one further orbit: there are \(1+\lceil \ell/2\rceil\) orbits. In particular these are the stable class counts outside the single exception.

## Assumptions and scope

Graphs are finite, undirected, and simple. The two terminal branching vertices of the tree are distinct. The spine has vertices \(0,1,\ldots,\ell\) and edges \(p_i=\{i,i+1\}\) for \(0\le i<\ell\). The leaf-edge classes are \(A\) and \(B\), of cardinalities \(a\) and \(b\). A vertex of \(G\) corresponding to \(p_i\) is also denoted \(p_i\). By definition the line graph joins two distinct edges precisely when they have a common endpoint in \(T\).

A counting-colour-refinement step replaces each vertex colour \(c(v)\) by the pair of \(c(v)\) and the multiset of colours of its neighbours. The stable partition is the first partition unchanged by another step; names or numerical encodings of colours have no mathematical significance. Refinability here is equality of this stable partition with the automorphism-orbit partition **within the same graph**; it makes no claim of distinguishing nonisomorphic graphs.

## Proof

**1. Structure and exact orbits.** The vertices \(A\cup\{p_0\}\) form a clique of size \(a+1\), and \(B\cup\{p_{\ell-1}\}\) form one of size \(b+1\). For \(\ell=1\) these cliques intersect in the sole spine vertex. For \(\ell\ge2\) they are disjoint, with the spine vertices forming an induced path between the two connector vertices. The two terminal cliques are exactly the maximal cliques of size at least three. Their relative sizes and the intervening path identify their two sides, up to exchanging the sides when \(a=b\). Permutations within \(A\) and within \(B\) induce automorphisms; when \(a=b\), reflecting the spine and interchanging its two leaf sets does as well. No further orbit mergers are possible, because every automorphism must preserve the distinguished terminal cliques (as an unordered pair), the path positions between them, and the leaf groups. This establishes the orbit description in the theorem. It also covers \(\ell=1\), where the terminal cliques meet in one vertex.

**2. Two elementary refinement facts.** Every automorphism preserves every refinement colour, so stable classes are unions of automorphism orbits. Moreover, refinement first separates vertices with distinct degrees. If a union \(S\) of initial or subsequently recognized colour classes is known, then vertices sharing a stable colour have equal graph distance to \(S\): inductively, whether distance is \(0\), at most \(1\), at most \(2\), etc. is determined from the preceding neighbourhood-colour multisets. The same argument applies to a singleton colour class. At any finite distance, this induction terminates on the finite graph.

**3. The one-spine-edge case.** Suppose \(\ell=1\). The shared connector \(p_0\) has degree \(a+b\); members of \(A\) have degree \(a\), and members of \(B\) have degree \(b\). Thus degree refinement is orbit-exact, using the symmetry between \(A\) and \(B\) if \(a=b\).

**4. Unequal terminal leaf counts.** Let \(\ell\ge2\), and swap the two sides if necessary to take \(a>b\ge2\). The connector \(p_0\) has degree \(a+1\), uniquely the largest degree in the graph. The other connector \(p_{\ell-1}\) has degree \(b+1\), each left leaf-edge vertex has degree \(a\), each right leaf-edge vertex degree \(b\), and each internal spine vertex has degree \(2\). Thus \(p_0\) becomes a singleton colour class after one step. Distances from this singleton separate all spine positions \(p_0,\ldots,p_{\ell-1}\), except potentially the left leaf-edge group at distance one from \(p_0\), which could share the colour of \(p_1\).

If \(\ell\ge3\), then \(p_1\) has degree \(2\), whereas each member of \(A\) has degree \(a\ge3\); these are separated. If \(\ell=2\), then \(p_1\) is the opposite connector, of degree \(b+1\). Unless \(a=b+1\), degree already separates \(p_1\) from \(A\). In the remaining case \(a=b+1\), every vertex of \(A\) has degree-neighbour multiset consisting of \(a-1\) entries of degree \(a\) and one of degree \(a+1\), whereas \(p_1\) has \(b\) entries of degree \(b\) and one of degree \(a+1\); these multisets differ because \(a\ne b\). Hence they separate at the next step. The right leaf-edge group is at distance \(\ell\) from \(p_0\), beyond every spine vertex. Consequently all orbits are separated, so the stable partition is orbit-exact.

**5. Equal terminal leaf counts at least three.** Suppose \(\ell\ge2\) and \(a=b\ge3\). The two connectors \(S=\{p_0,p_{\ell-1}\}\) have degree \(a+1\), the leaf-edge vertices degree \(a\), and the internal spine vertices degree \(2\). These three kinds are distinguished by degree. Among internal spine vertices, distance to \(S\) is exactly \(\min\{i,\ell-1-i\}\) at position \(p_i\). Distances distinguish precisely the reflection-paired orbits. All leaf-edge vertices are automorphic, and the two connectors are automorphic. Thus the degree and distance information already gives the full orbit partition.

**6. Equal terminal leaf counts of two.** Let \(\ell\ge2\), \(a=b=2\). The two connectors \(S\) have degree \(3\), while every other vertex has degree \(2\). For \(\ell=2\), there are only the connectors and leaf-edge vertices, exactly two orbits, separated by degree. For \(\ell=3\), the sole internal spine vertex has two neighbours in \(S\), whereas each leaf-edge vertex has exactly one, so refinement separates the three orbits.

For \(\ell\ge5\), distance to \(S\) separates all internal spine positions up to reflection **except** that the internal positions \(p_1,p_{\ell-2}\) have distance one, the same as the leaf-edge vertices. However \(p_1\) and \(p_{\ell-2}\) have a neighbour at distance two from \(S\), while each leaf-edge vertex has no such neighbour (its degree-two neighbour lies in the leaf-edge group at distance one). A further refinement therefore separates these two kinds. The distance classes of the remaining spine vertices are exactly their reflection-paired orbits. So this case is orbit-exact as well.

Finally, let \(\ell=4\). The two degree-three connectors have all three neighbours of degree two. Each of the other six degree-two vertices has exactly one neighbour of degree three and one neighbour of degree two. Therefore the degree partition into cells of sizes \(2\) and \(6\) is equitable and is already stable. Yet triangle membership is invariant under automorphisms: the four leaf-edge vertices lie in terminal triangles, while \(p_1,p_2\) lie in no triangle. By Step 1 these form distinct orbits of sizes \(4\) and \(2\), alongside the connector orbit of size \(2\). Thus the degree-two colour class is not an orbit. This is precisely the asserted exception.

All parameter ranges have been exhausted, proving the theorem.

## Verification

Two independently structured finite checkers are included. `verify_structure.py` is a standard-library implementation that constructs each tree line graph from edge incidence, runs exact synchronous refinement, and compares its colour classes to the explicit orbit formula for every \(2\le a\le b\le14\) and \(1\le\ell\le30\). It tests 2,730 triples and reports only the predicted exception. `verify_independent.py` separately constructs the line graphs using NetworkX, computes refinement anew, and tests orbit membership by exact marked graph isomorphism, not by the orbit formula. It checks 63 further triples with \(2\le a\le4\), \(a\le b\le5\), and \(1\le\ell\le7\), again finding precisely the exception. Execution records are included, and each script prints `PASS` only when its assertions hold. Both checks are finite corroborations; the preceding case analysis is the general proof.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015), *Graph Isomorphism, Color Refinement, and Compactness*, define refinability as equality of the stable colour partition and automorphism-orbit partition, and establish a broader hierarchy of algorithmic properties. They do not state this exact double-broom line-graph family classification in their paper. Kiefer, Schweitzer and Selman (2015), *Graphs Identified by Logics with Counting*, classify graphs identified by two-variable counting logic, a stronger and different property than orbit-exact refinement of a single graph. Their characterization does not directly give this all-parameter line-graph result. The present theorem concerns orbit recovery and cannot be read as graph identification.

A finite classification of tree line graphs through nine original-tree vertices identifies the same smallest exceptional configuration, but it does not imply the present unbounded parameter theorem or the fact that no other double-broom parameters fail. Likewise, orbit recovery with one uniquely coloured vertex is a different hypothesis; it does not directly cover the uniform initial colouring here.

## Limitations

Only double-broom trees with two terminal branching vertices, each supporting at least two leaves, are covered. The result does not claim refinability for arbitrary tree line graphs or block graphs; indeed the displayed exception lies among them. The all-parameter proof does not give a sharp number of refinement rounds. Exhaustive finite scripts cannot alone establish the all-parameter statement. The literature comparison is not an independent priority certificate; a specialized earlier derivation outside the inspected sources remains possible.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, especially pp. 2–3 and Section 8. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30, especially Section 4 and Theorem 17. https://arxiv.org/abs/1503.08792
