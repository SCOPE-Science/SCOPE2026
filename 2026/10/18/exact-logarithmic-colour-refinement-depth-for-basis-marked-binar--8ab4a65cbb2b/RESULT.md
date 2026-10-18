# Exact logarithmic colour-refinement depth for basis-marked binary projective geometries

## Finding

Let \(d\ge2\), and let \(\Gamma_d\) be the bipartite point--line incidence graph of the binary projective geometry \(\operatorname{PG}(d-1,2)\). Its point vertices are the nonzero vectors of \(\mathbb F_2^d\); its line vertices are the unordered triples \(\{u,v,u+v\}\), for distinct nonzero vectors \(u,v\). Put distinct initial colours on the \(d\) standard-basis points, give every other point the same colour, and give all line vertices a separate common colour. Perform **simultaneous ordinary one-dimensional colour refinement**, preserving old colours in every round.

At the end of even round \(2j\), for every \(j\ge0\), the point-colour classes are **exactly** the singleton classes indexed by the nonzero vectors of Hamming weight at most \(2^j\), and one additional class containing all remaining points (if any). At odd rounds the point partition does not change. In particular the exact number of point-colour classes after round \(2j\) is
\[
C_j(d)=\sum_{h=1}^{\min(d,2^j)}\binom dh+\mathbf1_{2^j<d},
\]
and the final nonsingleton class, when it exists, has \(\sum_{h=2^j+1}^{d}\binom dh\) elements. Thus the exact first round when all points are individually coloured is
\[
 R_{\mathrm{pt}}(d)=\begin{cases}0,&d=2,\\ 2\lceil\log_2(d-1)\rceil,&d\ge3.\end{cases}
\]
For \(d\ge3\), set \(k=\lceil\log_2(d-1)\rceil\) and \(t=2^{k-1}\). The exact first round when **the entire incidence graph**, including all its line vertices, is discretely coloured is
\[
 R_{\mathrm{all}}(d)=\begin{cases}
 0,&d=2,\\
 2k,&d\ge3\text{ and }d\le t+2,\\
 2k+1,&d\ge3\text{ and }d>t+2.
 \end{cases}
\]
Finally, among sets consisting solely of individually coloured **point** vertices, the least cardinality sufficient to make the refinement discrete is exactly \(d\); every vector-space basis attains the minimum and the same displayed depths.

This is an exact statement about partitions **inside the specified marked incidence graph**. No identification claim among arbitrary graphs is made.

## Assumptions and scope

A projective line over \(\mathbb F_2\) has precisely the three nonzero vectors of a two-dimensional vector subspace, so the displayed construction has \(2^d-1\) points, \((2^d-1)(2^d-2)/6\) lines, and point degree \((2^d-2)/2\). Every line has degree three. The initial two sorts have distinct colours even when their degrees coincide. Every selected basis point receives its own colour. The numbering starts at round zero, before any refinement. A refinement step recolours each vertex according to its old colour and the multiset of its neighbours' old colours.

For a nonzero vector \(x\), let \(\operatorname{supp}(x)\subseteq[d]\) denote the nonzero-coordinate set; its Hamming weight is \(|\operatorname{supp}(x)|\). Vector sums correspond to symmetric differences of supports. Let
\[
 T_j=\{x\ne0:|\operatorname{supp}(x)|\le2^j\},\qquad U_j=\{x\ne0:|\operatorname{supp}(x)|>2^j\}.
\]
An empty \(U_j\) contributes no class; a one-element \(U_j\) is already a singleton class. Statements are valid for every integer \(d\ge2\), with no asymptotic or genericity assumptions.

## Proof

**1. Alternating behaviour of the bipartite refinement.** Suppose at even round \(2j\) that every point of \(T_j\) is uniquely coloured and all points of \(U_j\) share one other colour. The colours of lines at the following odd round \(2j+1\) are determined exactly by their unordered multisets of current point colours. In particular, a line containing at least two points of \(T_j\) has its own singleton colour: no other line has those same two points, since any two distinct projective points determine precisely one line. A line with precisely one point \(x\) of \(T_j\) has a colour determined by \(x\), but no finer information about its other two endpoints. Lines containing no point of \(T_j\) have a common colour. This remains true with old-colour retention because earlier line-colour partitions are coarsenings of their current point-colour signatures.

Fix \(y\in U_j\). For each \(x\in T_j\), there is precisely one line through \(y\) and \(x\). If \(y=x+z\) for two **distinct** vectors \(x,z\in T_j\), then the line \(\{x,z,y\}\) has a singleton colour at round \(2j+1\). No different point outside \(T_j\) can be incident to this particular uniquely coloured line: its only point outside \(T_j\) is \(y\). Consequently distinct elements of \((T_j+T_j)\setminus(T_j\cup\{0\})\) receive distinct colours at round \(2j+2\), and cannot share a colour with the remainder.

Conversely, if \(y\in U_j\) has no representation as a sum of two distinct elements of \(T_j\), the line from \(y\) to each \(x\in T_j\) has **exactly one** endpoint in \(T_j\). Thus \(y\) sees exactly one line of the colour indexed by each \(x\in T_j\), and all its other incident lines have the zero-labelled colour. Since every point has the same degree, all such \(y\) have the same full line-neighbour multiset. Hence they are still one class at round \(2j+2\). In the intermediate odd round the point partition does not change, since line colours at round \(2j\) already equal those from the preceding odd round. The initial round \(j=0\) has exactly the basis points as singleton colours and the other points as one class, so this argument iterates.

**2. The support-doubling identity.** Vector addition over \(\mathbb F_2\) is symmetric difference of supports. For any nonzero vector supported on at most \(2^{j+1}\) coordinates, if it is not already in \(T_j\), partition its support into two nonempty sets of cardinality at most \(2^j\). This gives a representation as the sum of two distinct vectors in \(T_j\). Conversely, adding two vectors in \(T_j\) cannot create more than \(2^{j+1}\) nonzero coordinates. Therefore
\[
 T_j\cup\{x+z:x,z\in T_j,\ x\ne z\}=T_{j+1}.
\]
Together with Step 1, this proves by induction the exact point partition at every even round, including the statement that every remaining point has a common colour. Since odd rounds cannot change the point partition, the exact point-discretization depth follows: at \(2k\), where \(2^k\ge d-1\), at most the all-ones vector remains in \(U_k\), so all points are singletons; at \(2k-2\), where \(t=2^{k-1}<d-1\), there are at least two points in \(U_{k-1}\) and those cannot yet be separated. For \(d=2\), the two basis points and the sole remaining point already have singleton classes at round zero.

**3. Exact timing for line vertices.** Once every point is a singleton at round \(2k\), the three point neighbours uniquely identify each line at round \(2k+1\). To decide whether the lines were already discrete at round \(2k-1\), use the point classes from round \(2k-2\): precisely the vectors of support weight at most \(t\) are individually named, and the others form a single class. Each line with at least two named points is individually coloured, as established in Step 1.

If \(d=t+1\), the unnamed set comprises only the all-ones vector, and every line has at least two named endpoints. If \(d=t+2\) and \(t\ge2\), the unnamed vectors are the all-ones vector and those omitting exactly one basis coordinate. Two unnamed vectors sum either to a one-coordinate vector (all-ones paired with one omitted coordinate) or to a two-coordinate vector (two distinct omitted coordinates). Every such named sum determines **exactly one** unordered pair of unnamed endpoints. Hence lines with one named endpoint are also uniquely coloured; there are no lines with three unnamed endpoints. The only remaining boundary case is \((d,t)=(3,1)\): the three weight-two unnamed points form precisely one wholly unnamed line, and each basis point is the sole named endpoint of precisely one other line with two unnamed endpoints. Thus all lines are unique at round \(2k-1\) whenever \(d\le t+2\).

If \(d\ge t+3\), then \(t\ge2\). Fix the named weight-two vector with support \(\{1,2\}\). Choose two distinct \(t\)-element subsets \(H_1,H_2\) of \(\{3,\ldots,d\}\). For each choice, the three supports
\[
 H_i\cup\{1\},\quad H_i\cup\{2\},\quad \{1,2\}
\]
form a projective line. The first two have weight \(t+1\) and are unnamed; the third is the same named point in both lines. These two distinct lines therefore have identical colours at round \(2k-1\), so they have not yet become discrete. They separate by round \(2k+1\). Since the point partition was not discrete earlier than \(2k\), these observations establish the exact total-graph formula. The \(d=2\) graph has three points and one line, each with an initially distinct colour.

**4. The minimum number of marked points.** If fewer than \(d\) points are marked, their representative vectors span a proper subspace \(W\) of \(\mathbb F_2^d\). There is a nonidentity invertible linear transformation fixing every vector of \(W\): when \(W\ne\{0\}\), add one fixed nonzero vector of \(W\) to one complement-basis vector while fixing the other basis vectors; when \(W=\{0\}\), take any nonidentity invertible transformation. Such a transformation permutes points and lines, respects incidence, and fixes every mark. Therefore no colour-refinement partition can be discrete. A basis of \(d\) marked points suffices by Steps 1--3. Every basis is equivalent under an invertible linear change of coordinates, preserving the exact depths.

## Verification

The standalone `checks/check_refinement.py` constructs the complete point--line incidence graphs directly, runs synchronous colour refinement from the stated initial colouring, compares the exact point partition in each round with the support-weight formula, and verifies the **first** fully discrete round for each \(2\le d\le9\). This includes graphs with up to \(511\) point vertices and \(43{,}435\) line vertices.

The independent `checks/check_combinatorics.py` does not call the graph-refinement program. It computes line-incidence neighbour-type multisets directly from binary XOR arithmetic, independently checks support doubling and the sole anonymous residual class through \(d=10\), and verifies explicit late-line-collision constructions for \(3\le d\le17\). Their recorded standard outputs are embedded alongside the programs. Both checks ran successfully; the all-dimension conclusions follow from the proof, not finite enumeration.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015; arXiv:1502.01255) place ordinary colour refinement and its orbit-partition interpretation in the graph-isomorphism framework; see their Introduction and Section 8. Arvind, Fuhlbrück, Köbler, Kuhnert and Rattan (2016; arXiv:1606.04383) explicitly study how vertex individualization makes a graph discretely refinable, including bounded-round decision problems (Section 4.2). Neither inspected text supplies a corresponding binary-projective incidence calculation, its exact doubled-support refinement partition, or its dimension-dependent sharp depths.

Assmus (1995; DOI:10.37236/1203) studies binary-code structure of Steiner triple systems and provides older background for the binary-projective setting. Its accessible abstract does **not** establish a colour-refinement theorem; the entire full text was not confirmed inspected, so any undiscovered overlapping specialization remains a priority risk.

Earlier exact refinement calculations for marked projective planes in dimension three and marked collinear/noncollinear Steiner configurations concern genuinely smaller geometries or different marking conditions. The present all-dimension claim includes the three-dimensional case but is not inferred from it: the new assertion is an exact depth-and-partition formula for every dimension, with its sharp whole-graph transition.

## Limitations

The graph is specifically the **two-sorted incidence graph** over \(\mathbb F_2\), not the collinearity graph (which is complete), a cover graph of a lattice, or a projective geometry over larger fields. Initial colours must individually distinguish every chosen basis point, with one common colour for unmarked points and a separate line-sort colour. A claim about all projective geometries or about identification among arbitrary finite graphs would require further proof. No independent validation or publication-priority certification is claimed. The verification programs are finite checks only.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04. https://arxiv.org/abs/1502.01255
2. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert and G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383, first posted 2016-06-14. https://arxiv.org/abs/1606.04383
3. E. F. Assmus Jr., *On 2-ranks of Steiner triple systems*, Electronic Journal of Combinatorics **2** (1995), R9, public 1995-04-17. https://doi.org/10.37236/1203
