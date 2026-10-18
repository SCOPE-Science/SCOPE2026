# Sharp six-point threshold for binary Fourier intensity ambiguity

## Finding
Let \(d\ge1\) and \(G=\mathbb F_2^d\). For every nonempty subset \(A\subseteq G\), put
\[
W_A(\xi)=\sum_{a\in A}(-1)^{a\cdot\xi},\qquad I_A(\xi)=|W_A(\xi)|^2.
\]
For \(A,B\subseteq G\) with equal cardinality \(1\le |A|=|B|\le6\), equality \(I_A=I_B\) has the following complete classification.

1. If their common cardinality is at most five, then \(B=A+t\) for a unique translation class \(t\in G\) (possibly several shifts realize the same set).
2. At cardinality six, \(B=A+t\) still holds unless \(A\) is a six-point *affine circuit*: its affine-direction span \(H=\operatorname{span}\{a+a_0:a\in A\}\) has dimension four and \(\bigoplus_{a\in A}a=0\).
3. If \(A\) is a six-point affine circuit, the entire intensity fiber consists exactly of all six-point affine circuits lying within some coset of its fixed direction space \(H\). The fiber contains \(28\cdot 2^d\) distinct subsets, forming precisely \(28\) translation equivalence classes. Its squared Fourier amplitudes have the explicit form
\[
I_A(\xi)=\begin{cases}36,&\xi\in H^\perp,\\4,&\xi\notin H^\perp.\end{cases}
\]
In particular, \(6\) is the smallest nonzero support size admitting two indicator functions with equal full indexed Walsh magnitudes that are not translations.

## Assumptions and scope
All sets are ordinary subsets, not multisets, with real coefficients identically one on the support and zero elsewhere. Fourier transforms are **unnormalized** as above; squared amplitudes are indexed by individual characters \(\xi\), not merely compared as an unordered multiset. The group is elementary abelian of exponent two; inversion and reflection of a support are the identity, so translation is the only intrinsic support ambiguity. The assertion concerns exact, noiseless intensities. A six-point affine circuit exists only if \(d\ge4\).

For a subset \(A\), define its autocorrelation
\[
C_A(t)=\sum_{x\in G}1_A(x)1_A(x+t)=|A\cap(A+t)|.
\]
The Walsh inversion formula and convolution theorem give \(I_A=\widehat{C_A}\). Because the Walsh matrix is invertible, \(I_A=I_B\) holds if and only if \(C_A=C_B\). For \(t\ne0\), \(C_A(t)\) is twice the number of unordered pairs of distinct points having xor-difference \(t\). Thus the complete pair-difference multiset, including multiplicity, is exactly the information carried by the intensities.

## Proof
**1. Direction space is visible.** For a set with at least two points, the linear span of the nonzero support of \(C_A\) equals the direction space \(H_A=\operatorname{span}\{a+a_0:a\in A\}\). Therefore homometric sets have the same direction space and affine dimension. Translation lets us assume one chosen support point is zero. A set of \(k\) points has direction-space dimension at most \(k-1\).

**2. An independent-set reconstruction lemma.** Suppose that \(A=\{a_1,\ldots,a_k\}\) is affinely independent and \(k\le6\). Its \(\binom{k}{2}\) unordered pair differences \(a_i+a_j\) are distinct. Indeed, equality of two distinct differences would give an affine dependence on four distinct points. Write \(D_A=\{a_i+a_j:i<j\}\). Distinct members of \(D_A\) correspond to edges of the complete graph on the \(k\) vertices. Their sum again lies in \(D_A\) exactly when the edges share a vertex: adjacent edges sum to the third edge of a triangle; disjoint edges cannot, since that would yield a nonempty even-cardinality affine dependence. Consequently the graph on \(D_A\) with adjacency \(u\sim v\) if \(u+v\in D_A\) is precisely the line graph of the complete graph.

Let \(C_B=C_A\), and translate \(B\) to contain zero. The remaining \(k-1\) elements of \(B\) are pairwise distinct elements of \(D_A\); because their pairwise differences also lie in \(D_A\), they form a clique of size \(k-1\) in the line graph. Every pairwise-intersecting family of at least four edges of a complete graph is a star: if three edges form a nonconcurrent triangle, no fourth edge meets all three. Hence for \(k=5,6\), the clique is exactly the star at some \(a_i\), and \(B=A+a_i\). For \(k=4\), a three-edge clique could instead form a triangle, but then the four-point set formed with zero is an affine plane, giving repeated pair differences in contradiction with the distinctness of \(D_A\). For \(k\le3\), the claim is immediate from one or two pair differences. Thus every affinely independent support of size at most six is uniquely reconstructible up to translation.

**3. The remaining small affine geometries.** A four-point affinely dependent set is a two-plane \(P\); its nonzero autocorrelation equals four on the three nonzero directions of \(P\) and zero elsewhere. A five-point dependent set necessarily has the form \(P\cup\{x\}\), where \(P\) is a four-point affine plane and \(x\notin P\). After translating \(P\) to a linear plane, its autocorrelation has value four on the three nonzero elements of \(P\), value two at each of the four elements of \(x+P\), and zero at all remaining nonzero directions. These distributions recover the plane direction and the exceptional coset; two such sets with the same autocorrelation differ by translation. This proves uniqueness through cardinality five.

**4. Six-point supports of affine dimension three.** Such a set \(A\) is a three-dimensional affine flat \(L\) with two distinct points \(p,q\) deleted. Writing \(H\) for its direction space and \(h=p+q\), one has \(C_A(0)=6\), \(C_A(h)=6\), \(C_A(t)=4\) for the remaining six nonzero \(t\in H\), and zero for \(t\notin H\). The spectrum therefore determines \(H\) and \(h\). Any two omitted pairs with the same xor \(h\) are translates, establishing uniqueness here.

**5. Six-point supports of affine dimension four with a four-point dependence.** Such a set has a unique affine relation, supported on a plane \(P\) of four points, and has the form \(P\cup\{x,y\}\). Translate so \(P\) is a linear two-plane. Because the affine dimension is four, the cosets \(x+P\) and \(y+P\) are distinct nonzero cosets. Its autocorrelation equals four on the three nonzero directions of \(P\), equals two at each of the four points of each of \(x+P\) and \(y+P\) and at the single point \(x+y\), and is zero at other nonzero directions. Therefore the correlation identifies \(P\), both outer cosets (unordered), and the unique inter-point difference \(x+y\). Any other support with the same correlation has outer representatives \(x+u\) and \(y+v\) with \(u,v\in P\); the fixed sum imposes \(u=v\). Translation by that common \(u\) recovers the original support. Thus uniqueness holds.

**6. The sole exceptional six-point geometry.** The other affine-dimension-four type has its unique even affine dependence supported on all six points: it is a six-point affine circuit. It has no affine four-point subset, so all fifteen unordered pair differences are distinct. Because these differences lie in its four-dimensional direction space \(H\), they exhaust its fifteen nonzero elements. Hence
\[
C_A(0)=6,\qquad C_A(t)=2\quad(0\ne t\in H),\qquad C_A(t)=0\quad(t\notin H).
\]
Walsh transformation yields the two-level intensity distribution in the theorem. Conversely, any six-point set \(B\) with this autocorrelation lies in one coset of \(H\), has all pair differences distinct, and therefore has no four-point affine dependence. Six points in a four-dimensional affine flat are dependent, and their unique affine dependence must consequently involve all six points. Thus \(B\) is exactly a six-point affine circuit in an \(H\)-coset. Every such circuit has the same correlation, so the fiber description is both necessary and sufficient.

To count the circuit subsets in a fixed four-flat, count ordered affinely independent five-tuples: choose the first point in \(16\) ways and the successive four direction vectors in \(15,14,12,8\) ways. Dividing by \(5!\) yields \(2688\) unordered affinely independent five-point sets. Each determines exactly one sixth point, namely its xor-sum, forming a six-point circuit; each circuit contains six such five-sets. Therefore there are \(2688/6=448\) circuits in each fixed four-flat. Since a circuit has \(C_A(t)=2\) for every nonzero \(t\in H\), no nonzero translation stabilizes it (a stabilizing translation would give \(C_A(t)=6\)). Hence the \(448\) circuits in a fixed four-flat form \(448/16=28\) translation classes. There are \(2^{d-4}\) cosets of \(H\) in \(G\), giving \(448\cdot2^{d-4}=28\cdot2^d\) distinct supports and the same \(28\) translation classes across all cosets.

There are no other possibilities: for six distinct points the affine direction rank is three, four or five. Rank five is affine independence, rank three was handled in step 4, and rank four has one affine relation, of size four or six because nonempty affine relations in characteristic two have even support. The preceding steps exhaust all configurations. This completes the proof for all \(d\).

An explicit inequivalent homometric pair in \(\mathbb F_2^4\), written with coordinates encoded as bit-mask integers, is \(A=\{0,1,2,4,8,15\}\) and \(B=\{0,1,2,4,9,14\}\). Both are circuits; they have equal autocorrelations but are not translates.

## Verification
The standalone exact C++17 program `checker.cpp` enumerates every translation class of nonempty subsets of size at most six in \(\mathbb F_2^5\). It represents a support by a sorted tuple and translates only by one of its own vertices; this is exhaustive since every translate containing zero arises in that manner. For every canonical support it computes the full autocorrelation by integer pair counts, groups exact correlation signatures, and verifies the ambiguity classification. For sizes one through five there are no nontrivial fibers. At size six there are exactly \(31\) nonsingleton correlation fibers, each containing \(28\) translation classes, and all consist solely of the six-point circuits of one four-dimensional direction subspace. The program also checks the displayed nontranslation example.

Compile and execute from the directory containing `checker.cpp` using `c++ -std=c++17 -O2 checker.cpp -o checker && ./checker`. The program emits `CHECK_PASS` on success and returns nonzero on failure. Its enumeration is finite and exhaustive; the all-dimension theorem itself has the direct geometric proof above, so there is no extrapolation from numerical experiments.

## Relationship to prior work
Bendory, Edidin, and Gonzalez [1] formulate finite-alphabet phase retrieval and its equivalence with homometric support reconstruction; Section 6.1 discusses finite abelian groups without giving a Boolean-cube threshold or full six-point ambiguity fibers. Bendory and Edidin [2], particularly Appendix E, formulate the arbitrary-finite-abelian phase retrieval setting and conjectures about generic sparse signals, not this exact indicator-support reconstruction theorem. Rosenblatt and Seymour [3] provide classical homometric-set factorization methods in Euclidean spaces; their abstract does not establish the present finite exponent-two classification. The special six-point circuits are the classical \((16,6,2)\) difference sets, whose flat nontrivial Walsh magnitudes are related to bent Boolean functions [4]. Neither that difference-set identity nor the existence of such sets is claimed as new. The result established here is the sharp reconstruction threshold for all sizes through six and the complete exceptional fiber geometry and cardinality in every ambient dimension.

## Limitations
The classification is specific to supports with coefficients exactly one, binary vector-space groups, exact indexed Fourier powers, and support cardinality at most six; it neither classifies larger sets nor establishes stability under noise. The exceptional \((16,6,2)\) structure itself is classical. The proof is self-contained, but older work on finite-group homometry or difference sets may contain an equivalent reformulation; bibliographic exhaustiveness is not established. Independent mathematical verification has not been performed.

## References
[1] T. Bendory, D. Edidin, and I. Gonzalez, *Finite alphabet phase retrieval*, arXiv:2301.10647 (first public 2023-01-25), especially Sections 2, 3 and 6.1; doi:10.1016/j.acha.2023.04.005.

[2] T. Bendory and D. Edidin, *Toward a mathematical theory of the crystallographic phase retrieval problem*, arXiv:2002.10081 (first public 2020-02-24), especially Section 4.1.2 and Appendix E; doi:10.1137/20M132136X.

[3] J. Rosenblatt and P. D. Seymour, *The structure of homometric sets*, SIAM J. Algebraic Discrete Methods 3 (1982); doi:10.1137/0603035. Abstract consulted; full text not examined.

[4] *Bent Boolean Functions*, Boolean Functions research wiki, https://boolean.wiki.uib.no/Bent_Boolean_Functions (support of a bent Boolean function as a difference set).
