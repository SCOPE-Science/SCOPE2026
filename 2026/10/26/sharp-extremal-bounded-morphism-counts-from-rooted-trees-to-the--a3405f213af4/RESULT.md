# Sharp extremal bounded-morphism counts from rooted trees to the four-world diamond

## Finding
Let \(T\) be a finite nonempty rooted tree, equipped with the reflexive ancestor order, and let \(B_2\) be the four-world reflexive Boolean diamond \(0<a<1\), \(0<b<1\), with \(a\) and \(b\) incomparable. Count all bounded morphisms \(f:T\to B_2\) of frames, without requiring global surjectivity, as distinct functions on the fixed vertices of \(T\). Write \(N(T)\) for their number. If \(T_1,\ldots,T_d\) are the rooted child subtrees, then
\[
N(T)=\begin{cases}1,&|T|=1,\\2+\prod_{i=1}^{d}N(T_i),&|T|\ge2.\end{cases}
\]
For every integer \(n\ge2\), the exact minimum among rooted trees on \(n\) vertices is \(3\), attained only by the star rooted at its center (including the unique rooted two-vertex tree).

The exact maximum is
\[
M_n=\begin{cases}
1,&n=1,\\
3,&n=2,\\
2+3^{(n-1)/2},&n\ge3\text{ odd},\\
2+5\cdot3^{(n-4)/2},&n\ge4\text{ even}.
\end{cases}
\]
For every \(n\ge2\) the maximizing rooted tree is unique up to root-preserving isomorphism: if \(n\) is odd it has a root with \((n-1)/2\) children, each of which has exactly one leaf child; if \(n\ge4\) is even, it has a root with one three-vertex chain as a child subtree and \((n-4)/2\) two-vertex chain child subtrees. At \(n=2\) it is the single edge rooted at an endpoint. In particular the largest possible count grows at exponential base \(\sqrt3\) per vertex, with an explicit parity-dependent constant.

## Assumptions and scope
A rooted tree here is a finite connected undirected acyclic graph with one distinguished vertex. Its Kripke accessibility is the **reflexive transitive ancestor relation**, not the one-step parent relation. A bounded morphism is a map satisfying both forth and back: \(u\le v\Rightarrow f(u)\le f(v)\), and for each \(u\in T\) and \(y\ge f(u)\) some descendant-or-self \(v\ge u\) satisfies \(f(v)=y\). Thus, equivalently, \(f(\uparrow u)=\uparrow f(u)\) for every \(u\). The target middle worlds \(a,b\) are distinct and fixed; the maps are not quotiented by tree automorphisms or target automorphisms. A bounded morphism need not be onto \(B_2\): its image may be \(\{1\}\), \(\{a,1\}\), \(\{b,1\}\), or the entire diamond.

## Proof
**Local enumeration.** For a rooted subtree \(S\), denote by \(A(S),B(S),Z(S),U(S)\) the counts of bounded morphisms whose root goes, respectively, to \(a\), \(b\), \(0\), and \(1\). By symmetry \(A=B\); every leaf must map to the sole maximal world \(1\), so \(U(S)=1\) for all \(S\), and for a leaf \(A=B=Z=0\). Set \(q(S)=A(S)=B(S)\) and \(N(S)=Z(S)+2q(S)+1\).

Let \(S\) be nontrivial and \(S_i\) its nonempty list of child subtrees. A map with root \(a\) sends each child root to \(a\) or \(1\). The back requirement for \(1\) is already met by the image of every individual child subtree, whose morphism image is the entire upper cone of its own root. Therefore
\[
q(S)=\prod_i(1+q(S_i)).
\]
For root image \(0\), first choose independently one bounded morphism on each child subtree; there are \(\prod_iN(S_i)\) choices. The union of the child images must contain \(a\) and \(b\), and then contains \(1\) automatically. Missing \(a\) means each child has root image in \(\{b,1\}\), hence there are \(\prod_i(1+q(S_i))\) choices; missing \(b\) has the same number, and missing both forces all child roots to be \(1\), giving exactly one choice. By inclusion–exclusion,
\[
Z(S)=\prod_iN(S_i)-2\prod_i(1+q(S_i))+1.
\]
Adding the two middle-root cases and the unique top-root case gives the cancellation
\[
N(S)=Z(S)+2q(S)+1=2+\prod_iN(S_i).
\]
The argument applies to every non-leaf, without any regular-branching assumption. This proves the recurrence and the minimum: all subtree counts are at least \(1\), and equality in \(N(S)\ge3\) holds precisely when every child is a leaf.

**Sharp maximum.** Define the integer-partition envelope
\[
F(1)=1,\qquad F(2r)=3^r\ (r\ge1),\qquad F(2r+3)=5\cdot3^r\ (r\ge0).
\]
For every positive integer \(k\), \(F(k)\) is the largest product of parts' weights over additive partitions of \(k\) into parts of sizes \(1,2,3\), with weights \(1,3,5\), respectively. Indeed, one can improve any partition having \(1+1\), \(1+2\), or \(1+3\), and replace two threes by three twos because \(25<27\). The only optimal partition for \(k\ge2\) therefore consists of twos, with one three exactly when \(k\) is odd. It follows at once by concatenating optimal partitions that \(F(s)F(t)\le F(s+t)\) for positive \(s,t\).

We claim \(N(S)\le F(|S|)\), with equality possible only for subtree sizes \(1,2,3\). The assertion is immediate at sizes \(1,2,3\) from the recurrence. If \(|S|=n\ge4\) and its children have sizes \(n_i\), induction and supermultiplicativity yield
\[
N(S)\le2+\prod_iF(n_i)\le2+F(n-1)<F(n).
\]
The final strict inequality holds by direct substitution in the displayed parity formulas: for even \(n=2r\ge4\), the difference \(F(n)-F(n-1)-2=4\cdot3^{r-2}-2>0\); for odd \(n=2r+1\ge5\), it is \(2\cdot3^{r-1}-2>0\). Hence, for each \(n\ge2\),
\[
N(T)\le2+F(n-1).
\]
Every optimal partition of \(n-1\) is realizable as root-child sizes: use a two-vertex chain for every part of size two, and a three-vertex chain for the optional part of size three (or the single leaf for \(n=2\)). These child subtrees have morphism counts \(3\) and \(5\), precisely the weights in the maximizing partition. The upper bound is therefore attained and gives the formula for \(M_n\).

To obtain equality, each child must simultaneously attain \(F(n_i)\) and their envelope product must attain \(F(n-1)\). Strictness for subtree sizes \(n_i\ge4\), uniqueness of the optimal integer partition, and uniqueness of the maximizing two- and three-vertex rooted chains force exactly the stated root-preserving isomorphism type. This also proves uniqueness at the small cases. The parity formulas immediately give \(M_n=\Theta((\sqrt3)^n)\), with distinct parity constants.

## Verification
The accompanying executable \(check_tree.py\) independently generates every unlabelled rooted-tree shape through ten vertices. It verifies the upper/lower extrema and uniqueness across all generated shapes using the recurrence. For every shape through seven vertices, it independently enumerates all vertex maps into the four-world target, tests order preservation and the complete back condition at every vertex, and compares the resulting number to the recurrence. Separate constructions verify the proposed extremal shape and formula through forty vertices. Run \(`python3 check_tree.py`\) from the containing directory; the supplied output ends with `ALL_CHECKS_PASS`.

These finite checks do not prove the unrestricted extremal statement. The preceding inductive inequality and inclusion–exclusion proof supply the all-size argument.

## Relationship to prior work
The notion of bounded (\(p\)-)morphism and its forth/back conditions is standard, as described in the 2011 modal-logic lecture notes and the PlanetMath definition. A related earlier calculation for globally **surjective** morphisms from rooted trees onto more general finite middle-layer fans already yields a root-state recursion and an existence threshold. The present statement does **not** claim this root-state method as new: its contribution is the collapsed **all-map** recurrence for the four-world target and, especially, the exact all-order maximum, minimum, and unique optimizing rooted-tree shapes. The earlier surjective count and minimal-source theorem do not state these optimizations.

Zhang, Zhang, Gray, and Wang study extremal numbers of connected subtrees of trees. Their rooted subtree invariant is different: even on a large star, the number of connected subtrees containing its center grows exponentially with the number of leaves, whereas the present bounded-morphism count is exactly \(3\). Consequently their greedy-tree extremal theorem does not imply the present shape classification. The finite-tree invariants have different recurrences, optimization targets, and extremizers.

## Limitations
The theorem concerns only finite **rooted trees with reflexive ancestor accessibility** and this one labelled Boolean-diamond target. It does not enumerate only globally surjective maps, maps for one-step accessibility, maps from arbitrary finite posets, or morphisms modulo automorphisms. The exact recursion can be evaluated without drawing all morphisms, but the numbers grow exponentially in the number of tree vertices in the extremal family. A related unpublished/root-state calculation for surjective maps is acknowledged; the main originality assertion is the all-size extremal classification, not the presence of a recursive computation. Unindexed treatments of the same special extremal problem remain a literature risk.

## References
1. *Introduction to Modal Logics*, lecture notes (draft dated 16 September 2011), sections 2.4 and 2.7, especially the bounded-morphism and tree-unravelling discussions. https://gki.informatik.uni-freiburg.de/teaching/ss11/ml/script.pdf
2. CWoo, *p-morphism*, PlanetMath, creation timestamp 22 March 2013, MSC 03B45. https://planetmath.org/pmorphism
3. Xiu-Mei Zhang, Xiao-Dong Zhang, Daniel Gray, and Hua Wang, *Trees with the most subtrees—an algorithmic approach*, arXiv:1210.2871v1 (posted 10 October 2012), especially §§1,3. https://arxiv.org/abs/1210.2871
