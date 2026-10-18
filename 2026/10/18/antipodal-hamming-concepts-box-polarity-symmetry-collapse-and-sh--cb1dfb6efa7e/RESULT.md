# Antipodal Hamming concepts: box polarity, symmetry collapse, and sharp Horn arity

## Finding

**Theorem (complete lattice structure and sharp inference widths).** Fix integers \(q\ge2\) and \(d\ge1\), a \(q\)-element alphabet \(A\), and \(W=A^d\). Form the symmetric formal context \((W,W,I)\) with
\[
xIy\quad\Longleftrightarrow\quad x_i\ne y_i\text{ for every }i\in[d].
\]
This is the maximum-distance relation in the \(q\)-ary Hamming space. Write \(S'=\{y\in W:\forall x\in S,\ xIy\}\) and \(c(S)=S''\). For \(S\ne\varnothing\) put \(P_i(S)=\{x_i:x\in S\}\). Then
\[
c(S)=\begin{cases}
\varnothing,&S=\varnothing,\\
W,&S\ne\varnothing\text{ and some }P_i(S)=A,\\
\prod_{i=1}^{d}P_i(S),&S\ne\varnothing\text{ and every }P_i(S)\subsetneq A.
\end{cases}
\]
The closed extents (equivalently, closed intents) are precisely the bottom \(\varnothing\), the top \(W\), and all nonempty proper boxes \(\prod_i B_i\) with \(\varnothing\ne B_i\subsetneq A\). In particular their number and rank-generating polynomial are
\[
|\mathcal L_{q,d}|=2+(2^q-2)^d,
\qquad R_{q,d}(t)=1+t\left(\sum_{k=1}^{q-1}\binom qk t^{k-1}\right)^d+t^{d(q-2)+2}.
\]
Every proper box has rank \(1+\sum_i(|B_i|-1)\), while the top has rank \(2+d(q-2)\). The full order-preserving automorphism group is
\[
\operatorname{Aut}(\mathcal L_{q,d})\cong
\begin{cases}
\mathfrak S_q,&d=1,\\
\mathfrak S_{2^d},&q=2,\ d\ge2,\\
\mathfrak S_q\wr\mathfrak S_d,&q\ge3,\ d\ge2.
\end{cases}
\]
The lattice is distributive if and only if \(d=1\); it is modular if and only if \(d=1\) or \(q=2\).

For a finite closure system, a **sound unit Horn rule** is \(T\to y\) with \(y\in c(T)\). A basis is *iterative* if repeatedly applying its rules computes \(c(S)\) for every input \(S\); it is *simultaneously direct* if one simultaneous application to the original \(S\) suffices, with no newly inferred premises used in that application. Define the *width* of a basis as the maximum size of any premise, with width zero for an empty basis. Minimize this width over all finite sound bases of the indicated type. Then
\[
a_{\rm iterative}(q,d)=\begin{cases}0,&d=1,\\q,&d\ge2,\end{cases}
\qquad
a_{\rm direct}(q,d)=\begin{cases}
0,&d=1,\\
2,&q=2,\ d\ge2,\\
\max\{q,d\},&q\ge3,\ d\ge2.
\end{cases}
\]
Thus at fixed nonbinary alphabet size \(q\), ordinary forward chaining has bounded optimal premise width \(q\), while one-pass inference has width growing linearly with dimension once \(d>q\).

## Assumptions and scope

The alphabet is merely a finite set; no field or group structure is assumed. Objects and attributes are separate labeled copies of \(W\). The incidence is coordinatewise *inequality in every coordinate*, not Hamming distance at most one, disjointness of subsets, or graph geodesic convexity. The rank convention places the bottom at rank zero. All automorphisms preserve the lattice order, not its order-reversing polarity. Implication bases are allowed to have arbitrarily many finite rules; only their maximum antecedent cardinality is optimized. Simultaneously direct means all rules are tested against the original input, not an ordered single sweep that may use newly derived elements.

## Proof

**Polarity and boxes.** Let \(S\subseteq W\). Directly from the defining universal condition,
\[
S'=\prod_{i=1}^d(A\setminus P_i(S)),
\]
using \(P_i(\varnothing)=\varnothing\). If \(S=\varnothing\), then \(S'=W\); the common antipodes of all \(q^d\) words form the empty set, since \(q\ge2\). If \(S\ne\varnothing\) and some coordinate support is all of \(A\), then \(S'=\varnothing\) and \(S''=W\). Otherwise every factor in \(S'\) is nonempty, so its coordinate projections are precisely \(A\setminus P_i(S)\), and taking the polarity again gives \(S''=\prod_iP_i(S)\). Conversely each nonempty proper box equals its double polarity. All remaining subsets close either to such a box or to the top. The extent poset is the inclusion order on these closed sets; proper-box inclusion is coordinatewise. Counting choices gives the cardinality formula. Increasing a single nonfull coordinate support by one element gives all covers between proper boxes, and every maximal proper box is covered by \(W\). This proves the rank formula. Because \(I\) is symmetric, the order-reversing concept polarity sends a proper box \(\prod B_i\) to \(\prod(A\setminus B_i)\), interchanging bottom and top.

**Automorphisms.** If \(d=1\), the closed-set lattice is \(2^A\), with automorphism group \(\mathfrak S_q\). If \(q=2\) and \(d\ge2\), each nonempty proper box is a singleton; the lattice has \(2^d\) incomparable atoms between bottom and top, so every permutation of these atoms is an order automorphism and the group is \(\mathfrak S_{2^d}\). Now assume \(q\ge3\), \(d\ge2\). The atoms are precisely the singleton words. For distinct atoms \(x,y\), their join is the proper box \(\prod_i\{x_i,y_i\}\), so its lattice rank is \(1+d_H(x,y)\). Consequently the order intrinsically recovers the graph of Hamming-distance-one adjacency on \(A^d\). A graph automorphism of this Hamming graph consists of a permutation of the \(d\) coordinates together with independent permutations of their \(q\) alphabet values: to see this, fix a base word, note that its neighbors divide into \(d\) coordinate cliques of size \(q-1\), normalize the action on the base and its neighbors, and induct on distance from the base because any vertex at distance at least two is uniquely determined by its neighbors one step nearer the base. Thus the graph automorphism group is \(\mathfrak S_q\wr\mathfrak S_d\). Every proper box is the join of its constituent atom-words, so a lattice automorphism is determined by its action on atoms. Conversely every coordinate/alphabet permutation preserves boxes and hence is a lattice automorphism. This proves equality of the groups.

**Modularity.** At \(d=1\) the lattice is Boolean. At \(q=2,d\ge2\) it is the height-two diamond with \(2^d\) atoms, hence modular and not distributive. For \(q\ge3,d\ge2\) let \(x=(0,0,0,\ldots)\), \(y=(1,1,0,\ldots)\), and \(w=(1,0,0,\ldots)\), choosing two distinct alphabet values \(0,1\). Put \(a=\{x\}\), \(b=\{y\}\), and \(z=\{x,w\}\), which is a proper box. Then \(a\le z\), \(b\wedge z=\varnothing\), and \((a\vee b)\wedge z=z>a\). This violates the modular identity \(a\vee(b\wedge z)=(a\vee b)\wedge z\), and hence distributivity as well.

**Iterative Horn upper bounds.** For each pair of words \(x,y\), include the binary mixing rules
\[
\{x,y\}\to z\qquad(z_i\in\{x_i,y_i\}\ \text{for each }i).
\]
They are sound since \(z\in c(\{x,y\})\): for \(q=2\) this follows even when a coordinate is full, and otherwise it follows from the box formula. Also, for every \(q\)-element set of words whose letters in some coordinate exhaust \(A\), include the saturation rules to every word of \(W\). These rules are sound because such a set closes to \(W\). Repeated binary mixing converts any nonempty input into the Cartesian product of its coordinate supports: inductively, if a box \(\prod B_i\) has been formed and a further word \(y\) is inserted, every point of \(\prod(B_i\cup\{y_i\})\) can be obtained by mixing \(y\) with a suitable point of the old box. If no coordinate support is full, the product is the desired closure. Otherwise \(q\) representatives of the full coordinate support trigger saturation. Thus the displayed system computes \(c\) by forward chaining and has width at most \(q\) for \(d\ge2\) (since \(q\ge2\)).

**Iterative Horn lower bound.** For \(d\ge2\), fix a coordinate line \(S=\{(a,0,\ldots,0):a\in A\}\). This line closes to \(W\), but every proper subset \(T\subsetneq S\) is itself closed: it has nonempty proper support in the first coordinate and singleton support in every other coordinate. Therefore a sound rule of premise size less than \(q\) whose premises all lie in \(S\) cannot add a point outside \(S\). Any rule system of width below \(q\), started at \(S\), remains stuck at \(S\), contradicting \(c(S)=W\). Hence the minimum iterative width equals \(q\). If \(d=1\) every subset is closed, and the empty rule basis has width zero.

**Direct Horn upper bound.** If \(y\in c(S)\setminus S\) and a coordinate support is full, select one element of \(S\) realizing each of the \(q\) letters in that coordinate; these \(q\) witnesses force \(y\). Otherwise \(y\) belongs to the box of the coordinate supports; choose at most one witness from \(S\) for each coordinate that realizes \(y_i\). At most \(d\) witnesses force \(y\). Consequently the full family of sound unit implications whose premises have size at most \(\max\{q,d\}\) is simultaneously direct. For \(q=2\), every nonsingleton input has full support in some coordinate, so two witnesses suffice. A singleton is already closed, proving the binary direct upper bound two.

**Direct Horn lower bounds.** The full coordinate line used above forces any point outside it only if all \(q\) line elements are present, giving a direct lower bound \(q\). For \(q\ge3,d\ge2\), let \(u=(0,\ldots,0)\) and, for each coordinate \(j\), let \(x^{(j)}\) have \(0\) in coordinate \(j\) and \(1\) elsewhere. The set \(S=\{x^{(j)}:j\in[d]\}\) has no full coordinate support and \(u\in c(S)\setminus S\). Deleting any \(x^{(j)}\) removes the only occurrence of \(0\) in coordinate \(j\), so \(u\notin c(S\setminus\{x^{(j)}\})\). Every simultaneous one-pass system inferring \(u\) from \(S\) must therefore contain a rule with all \(d\) elements of \(S\) as premises. This gives the lower bound \(d\). When \(q=2,d\ge2\), each singleton is closed but any two distinct words close to \(W\); thus the direct width is at least two. Together with the upper bounds, all width formulas follow.

## Verification

The accompanying standalone `verify.py` independently builds the incidence matrix, applies the two universal Galois derivations, and compares resulting closures against the box formula. It exhausts all \(2^{|W|}\) input subsets for \((q,d)\) equal to \((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2)\), including all \(65{,}536\) subsets for the two sixteen-word cases. It exhaustively checks the maximal sizes of inclusion-minimal direct Horn premises in these cases and tests the mixing/saturation algorithm by explicit pair-rule iteration. For \((q,d)=(3,3)\), it tests \(2{,}000\) reproducibly sampled input subsets and the explicit sharpness witnesses. The expected concept counts for \((q,d)=(3,2)\) and \((4,2)\) are respectively \(38\) and \(198\), and the computed minimal direct premise widths are \(3\) and \(4\). The proof, not the finite runs, establishes the universal assertions, groups, and lattice identities.

Run `python3 verify.py` with the Python 3 standard library. The script executes independent incidence-based closures rather than substituting the theorem's formula as its sole oracle.

## Relationship to prior work

The contranominal scale \((A,A,\ne)\), whose concept lattice is Boolean, is classical. Dürrschnabel, Koyda and Stumme study detection and attribute selection for such scales and general implication bases [1]; the construction here is their coordinatewise *AND/cardinal-product incidence* with a specific Hamming interpretation. Jäkel and Schmidt [2] develop general formal-context cardinal products and lattice tensor dimensions; those general constructions and product laws are not claimed as new. Rawson et al. [3] provide a general correspondence between hypergraph intersection closure and concept lattices, without the stated special-family width computation. Adaricheva, Nation and Rand [4] distinguish ordinary and direct implication bases in general; the distinction itself is not new. The specific sharp \(q\)-versus-\(\max\{q,d\}\) antecedent-width separation, together with the finite-alphabet symmetry collapse of this antipodal Hamming polarity, is the assessed specialized contribution. This is not the incidence \(d_H(x,y)\le1\) or geodesic convexity of the Hamming graph.

## Limitations

This is a structural classification for one explicit family of finite contexts, not an algorithmic lower bound on the number of Horn rules, their total encoding length, or the time required for closure computation. The displayed iterative basis may contain many redundant rules; only maximum premise size is optimized. General tensor-product, closure-system, and Hamming-graph results are used and credited, and the result should not be read as inventing those constructions. An implicit equivalent specialization under product-closure or implication-width terminology remains possible; independent literature priority verification has not been performed.

## References

[1] D. Dürrschnabel, M. Koyda, G. Stumme, *Attribute Selection using Contranominal Scales*, arXiv:2106.10978 (first posted 2021-06-21), https://arxiv.org/abs/2106.10978.

[2] C. Jäkel, S. E. Schmidt, *Cover Problems, Dimensions And The Tensor Product Of Complete Lattices*, in CLA 2018 Proceedings, pp. 81–92, https://cla2018.inf.upol.cz/proceedings-cla2018.pdf.

[3] M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681 (first posted 2023-07-21), https://arxiv.org/abs/2307.11681.

[4] K. Adaricheva, J. B. Nation, R. Rand, *Ordered direct implicational basis of a finite closure system*, arXiv:1110.5805 (first posted 2011-10-26), https://arxiv.org/abs/1110.5805.
