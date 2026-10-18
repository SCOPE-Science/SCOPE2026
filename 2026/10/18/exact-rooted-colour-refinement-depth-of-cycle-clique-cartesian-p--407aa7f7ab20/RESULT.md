# Exact rooted colour-refinement depth of cycle–clique Cartesian products

## Finding

Let \(n\ge5\) and \(m\ge2\) be integers. Give the vertex \(o=(0,0)\) a singleton initial colour in the finite, simple, undirected Cartesian product \(G=C_n\square K_m\); give every other vertex one common initial colour. Let \(\chi_t\) be synchronous one-dimensional counting colour refinement after \(t\) rounds, with the old colour retained as part of every new signature. Put \(D=\lfloor n/2\rfloor\).

**The stable classes are exactly the orbits of the automorphism group fixing \(o\).** They are
\[
A_d=\{(i,0):\min(i,n-i)=d\},\qquad
B_d=\{(i,j):\min(i,n-i)=d,\ 1\le j<m\},\qquad 0\le d\le D.
\]
Thus there are exactly \(2(D+1)\) stable classes. Writing \(s_d=1\) if \(d=0\) or if \(n\) is even and \(d=D\), and \(s_d=2\) otherwise, the class cardinalities are \(|A_d|=s_d\) and \(|B_d|=(m-1)s_d\).

The **least stable refinement round** (the first \(R\) for which round \(R+1\) does not split any round-\(R\) class) is
\[
R(n,m)=\begin{cases}3,&(n,m)=(5,2),\\ \lfloor n/2\rfloor,&\text{otherwise}.\end{cases}
\]
In particular, for all \(n\ge6\), stabilization takes exactly the cyclic radius \(D\) rounds, one less than the eccentricity \(D+1\) of the marked vertex in the product.

## Assumptions and scope

The vertices are \(\{(i,j):i\in\mathbb Z/n\mathbb Z,\ 0\le j<m\}\). Distinct vertices \((i,j)\), \((i',j')\) are adjacent exactly if either \(i=i'\) and \(j\ne j'\), or \(j=j'\) and \(i'-i\equiv\pm1\pmod n\). No edge colours are supplied. The singleton root colour and the common nonroot colour are distinct. Colour equality is considered up to relabelling; only partitions matter. The assertion concerns within-graph root-stabilizer orbit recovery and exact rounds, not identification of the graph against arbitrary nonisomorphic graphs.

## Proof

**1. Automorphism orbits.** The edges internal to the sets \(\{i\}\times V(K_m)\) are distinguishable intrinsically from edges around the cycle. If \(m\ge3\), the former belong to triangles and the latter do not, because \(n\ge5\). If \(m=2\), a former edge lies in exactly two quadrangles, and a latter edge lies in exactly one; \(n\ge5\) again excludes additional four-cycles within a cycle layer. Thus every automorphism permutes the vertical \(m\)-cliques/edges and induces an automorphism of \(C_n\). The horizontal perfect matchings force the coordinate permutation on \(K_m\) to be the same in all columns. Consequently the entire automorphism group is the product of the dihedral group on the cycle and the full symmetric group on \(m\) symbols. Fixing \((0,0)\) leaves cycle reflection and permutations of the \(m-1\) nonzero symbols. Its orbits are precisely \(A_d,B_d\), of the claimed cardinalities. Colour refinement cannot split a root-stabilizer orbit.

**2. Walk-count lemma.** Let \(w_k(v)\) denote the number of length-\(k\) walks from \(v\) to \(o\), with \(w_0(v)=\mathbf1_{v=o}\). The round-\(t\) colour determines the vector \((w_0(v),\ldots,w_t(v))\): at round zero it determines \(w_0\), while the multiset of round-\(t\) neighbour colours allows summing their \(w_t\) values to obtain \(w_{t+1}\). Old colours are retained. In particular, a round-\(t\) colour distinguishes different shortest distances to the root whenever the smaller distance is at most \(t\); and at the first nonzero walk length it also distinguishes different numbers of shortest walks.

**3. Separation by the cyclic radius.** Each vertex in \(A_d\) has root distance \(d\), and each vertex in \(B_d\) has root distance \(d+1\). Among the \(2(D+1)\) orbit types, the only pairs at equal distance \(k\le D\) are \(A_k\) and \(B_{k-1}\), for \(1\le k\le D\). For \(2\le k<D\), a vertex of \(A_k\) has exactly one shortest walk to the root, whereas a vertex of \(B_{k-1}\) has exactly \(k\): the latter interleaves one complete-factor step with the unique shortest \((k-1)\)-step cycle path in \(k\) ways. At \(k=D\), the same counts are \(1\) and \(D\) for odd \(n\), and \(2\) and \(D\) for even \(n\). They remain distinct because even \(n\ge6\) gives \(D\ge3\). Thus these equal-distance pairs split no later than round \(k\).

For the remaining equal-distance pair \(A_1,B_0\), length-two walk counts to the root are respectively \(0\) and \(m-2\). Hence round two separates them when \(m\ge3\). When \(m=2\), their length-three counts are respectively \(6\) and \(7\). To verify these values, use the adjacency decomposition \(A_G=A_{C_n}\otimes I+I\otimes A_{K_2}\), expand the cube, and use that a cycle of length at least five has three length-three walks from a neighbour of zero to zero and two length-two closed walks at zero. Thus round three separates \(A_1\) and \(B_0\). For \(n\ge6\), \(D\ge3\); every pair of distinct orbit types is therefore distinguished by round \(D\). For \(n=5,m\ge3\), \(D=2\) already suffices. In each case the stable partition must be the orbit partition, since refinement does not split orbits.

**4. Sharpness.** The graph is regular of degree \(m+1\). In any regular graph with just one initially marked vertex, all vertices at distance greater than \(t\) from the marked vertex have the same colour after \(t\) rounds: prove this inductively, since each such vertex sees only the uniform non-root colour at every smaller wavefront depth. Here every \(A_D\) vertex has root distance \(D\), while every \(B_D\) vertex has distance \(D+1\). They remain together at round \(D-1\), proving \(R\ge D\). The preceding paragraph proves equality except possibly \((5,2)\). In that case, \(A_1\) and \(B_0\) have the same round-one colour and the same round-two signature (each has one neighbour at the root and no neighbour in the other round-one distance-one vertices). Their differing three-walk counts separate them at round three. Therefore \(R(5,2)=3\), as claimed.

## Verification

Two standalone, dependency-free programs accompany this result. `verify_graph.py` constructs individual vertices and edges, computes each synchronous refinement partition, and checks it against the analytically described orbits over \(392\) parameter pairs: \(5\le n\le60\), \(2\le m\le8\) (\(63{,}700\) vertices summed over instances). `verify_quotient.py` independently constructs the weighted orbit-quotient adjacency counts and runs refinement there for \(864\) parameter pairs: \(5\le n\le100\), \(2\le m\le10\) (\(46{,}656\) quotient states summed over instances). Both verify the exact stabilization round, not just the terminal class count. Their recorded outputs are `verification_graph.txt` and `verification_quotient.txt`. The infinite claim follows from the proof, not from the finite checks.

Run from the package directory with `python3 verify_graph.py` and `python3 verify_quotient.py`. Both programs use only the Python standard library; tested with Python 3.11.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015) formalize colour refinement, the orbit partition and refinability, and study the hierarchy of graph-identification and fractional-automorphism properties. Those general definitions do not imply that the particular rooted product has orbit-exact refinement by a specified round. Kiefer and McKay (2020) analyze maximal iteration numbers and construct long-refinement graph families, but their results do not establish the rooted cycle–clique product's exact iteration number. Related work on rooted Cartesian products of complete graphs or powers of cycles concerns different graph families; neither contains \(C_n\square K_m\) with a genuine noncomplete cycle factor as the asserted subcase for \(n\ge5\). Searches found no directly equivalent specialized formula, but absence of such a result cannot certify priority.

## Limitations

The theorem assumes one uniquely coloured root, a cycle length at least five, and a complete factor of order at least two. The exceptional four-cycle product and unmarked graphs are outside scope. The claim is within-graph orbit recovery, not identification against competing nonisomorphic graphs. Literature search may miss specialized prior work on individualization of Cartesian product graphs. No external independent scientific audit or publication-priority certification has been performed.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
2. S. Kiefer, B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182, first posted 2020-05-20, https://arxiv.org/abs/2005.10182.
