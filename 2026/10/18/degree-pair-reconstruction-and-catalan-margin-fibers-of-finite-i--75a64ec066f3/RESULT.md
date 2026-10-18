# Degree-pair reconstruction and Catalan margin fibers of finite interval orders

## Finding

**Theorem (paired and one-sided information).** Let \(P=(X,<)\) range over finite nonempty strict interval orders, equivalently strict partial orders without an induced disjoint union of two two-element chains. Define \(u(x)=|\{y\in X:x<y\}|\), \(d(x)=|\{y\in X:y<x\}|\), and the paired degree multiset \(\mathcal D(P)=\{\!\{(d(x),u(x)):x\in X\}\!\}\). Then the following hold for every cardinality \(n=|X|\ge1\).

1. The multiset \(\mathcal D(P)\) determines the isomorphism class of \(P\). Within \(P\), equality of ordered pairs \((d(x),u(x))\) is precisely equality of strict lower and upper neighborhoods, and thus is precisely membership in the same automorphism orbit. Sorting elements by decreasing \(u(x)\), each element \(y\) has as predecessors exactly the first \(d(y)\) elements, with no ambiguity from ties.
2. In the relational vocabulary consisting of only the full **transitive strict order relation** \(<\), two-variable first-order logic with counting \(C^2\), already at quantifier rank two, separates every two nonisomorphic finite interval orders. Quantifier rank one does not suffice uniformly for this class. Equivalently, one synchronous round of directed in/out counting color refinement separates their isomorphism types via the global color histograms. Identification is **within the class of interval orders**, not against arbitrary posets or other directed structures.
3. The possible one-sided multisets \(\{\!\{u(x):x\in X\}\!\}\) are precisely the integer sequences \(n-1\ge a_1\ge\cdots\ge a_n=0\) such that \(a_i\le n-i\) for every \(1\le i\le n\). There are exactly \(C_n=\frac1{n+1}\binom{2n}{n}\) such multisets.
4. Fix one permitted one-sided multiset with distinct values \(\delta_1>\cdots>\delta_k=0\) and positive multiplicities \(c_1,\dots,c_k\), and define \(r_1=n-\delta_1\), \(r_i=\delta_{i-1}-\delta_i\) for \(2\le i\le k\). The **exact number of nonisomorphic interval orders** having this multiset is

\[
[\,x_1^{r_1}\cdots x_k^{r_k} y_1^{c_1}\cdots y_k^{c_k}\,]
\prod_{1\le i\le j\le k}(1-x_i y_j)^{-1}.
\]

Equivalently, it is the number of \(k\times k\) upper-triangular nonnegative integer matrices with those row and column sums. The first one-sided ambiguity appears at \(n=4\): there are two nonisomorphic orders with one-sided degree list \((2,1,0,0)\); no smaller size has an ambiguous one-sided list.

## Assumptions and scope

The underlying set \(X\) is finite and nonempty; the sole relational symbol \(<\) is interpreted as an irreflexive, transitive relation. The qualification *interval order* means the absence of an induced \((2+2)\) configuration. The relation is the entire strict order, not merely its immediate-cover or Hasse arcs. There are no vertex colors, endpoint parameters, bounded-width assumptions or bounded-order assumptions. Counting-logic comparisons are made between members of the finite interval-order class. The empty structure can be included with an empty degree multiset and a separate trivial case, but is omitted for clarity.

## Proof

**1. Nested neighborhoods and exact reconstruction.** A finite order is \((2+2)\)-free if and only if its strict successor sets \(U(x)=\{z:x<z\}\) are linearly ordered under inclusion; this is the order-dual version of the established nested strict down-set characterization. Therefore \(u(x)>u(z)\) implies \(U(x)\supsetneq U(z)\), while equality of these two cardinalities implies \(U(x)=U(z)\). Fix any decreasing-\(u\) ordering of the vertices. For any \(y\in X\), the set of all vertices \(x\) satisfying \(y\in U(x)\) is an initial segment of this ordering because the \(U(x)\) are nested. It has cardinality \(d(y)\), so it consists of precisely the first \(d(y)\) vertices. Tied vertices have identical successor sets, hence a predecessor initial segment cannot split a tie. The paired-degree multiset consequently reconstructs all relations up to interchange of vertices with the same pair. Separately, the strict predecessor sets \(D(x)=\{y:y<x\}\) are nested by inclusion; equality of \(d(x)\) implies equality of these sets. Thus any two vertices sharing both counts have the same \(U\) and \(D\), so their transposition is an automorphism. Every automorphism preserves both counts, giving exactly the degree-pair classes as the automorphism orbits. Notice that one-sided equality alone gives identical successor sets but need not give equal predecessors.

**2. The exact counting-logic bound.** For fixed nonnegative integers \(a,b\), the formula

\[
\theta_{a,b}(x):=(\exists^{=a} y\,(y<x))\ \land\ (\exists^{=b} y\,(x<y))
\]

uses only variables \(x,y\) and has quantifier rank one. For any positive integer \(m\), the rank-two sentence \(\exists^{=m}x\,\theta_{a,b}(x)\) detects exactly how many vertices have pair \((a,b)\). If two interval orders are not isomorphic, Step 1 implies their pair multisets differ, so one such sentence distinguishes them (allowing \(m=0\) for absent types). Counting rank one, by contrast, can count the cardinality but cannot inspect an off-diagonal binary relation in the irreflexive vocabulary: with at most one active variable, only \(x=x\) and \(x<x\) can be tested. Therefore the two-point chain and two-point antichain satisfy the same rank-one counting sentences but are nonisomorphic interval orders. Initial directed counting-refinement colors after one round are exactly the ordered in/out degrees, proving the equivalent refinement statement.

**3. Characterization and Catalan number of outgoing profiles.** List any interval order's outgoing degrees in weakly decreasing order \(a_1,\ldots,a_n\). If \(x<y\), then \(U(y)\subsetneq U(x)\), hence \(u(x)>u(y)\). All outgoing neighbors of the vertex in position \(i\) occur later in this ordering; therefore \(0\le a_i\le n-i\). The last value is zero. Conversely, given any nonincreasing nonnegative integer sequence satisfying these inequalities, put a strict relation on \(\{1,\ldots,n\}\) by declaring

\[
 i<j \quad\Longleftrightarrow\quad j>n-a_i.
\]

As \(a_i\le n-i\), this always requires \(i<j\) as natural integers, so the relation is irreflexive. The strict upper neighborhood of vertex \(i\) is the terminal suffix \(\{n-a_i+1,\ldots,n\}\); therefore upper neighborhoods are nested, which precludes an induced \((2+2)\). The relation is transitive: if \(i<j\) and \(j<\ell\), then \(\ell>j>n-a_i\), so \(i<\ell\). Its outgoing-degree list is exactly the prescribed one. Such degree lists are exactly Ferrers partitions fitting inside the staircase shape \((n-1,n-2,\ldots,1,0)\), whose number is the Catalan number \(C_n\), by the standard boundary-lattice-path bijection with Dyck paths of semilength \(n\).

**4. Exact isomorphism fibers of the one-sided invariant.** Use the classical bijection between isomorphism types of finite interval orders and upper-triangular nonnegative integer Fishburn matrices with no zero rows or columns. The cell \((i,j)\), where \(1\le i\le j\le k\), represents its multiplicity of interval-elements \([i,j]\), with an element from \((i,j)\) below an element from \((i',j')\) precisely if \(j<i'\). The row sums \(r_i\) and column sums \(c_j\) are strictly positive. Every element in column \(j\) has precisely \(\sum_{i'>j}r_{i'}\) strict successors; because row sums are positive, these values are strictly decreasing in \(j\), and the last is zero. Therefore the one-sided degree list determines all the column sums \(c_j\), and also determines the row sums by successive differences: \(r_1=n-\delta_1\) and \(r_i=\delta_{i-1}-\delta_i\) for \(i\ge2\). Conversely, every upper-triangular matrix with exactly these margins encodes an interval order with exactly this one-sided list. Different such matrices give different isomorphism types under the established bijection. Expanding each factor \((1-x_i y_j)^{-1}=\sum_{m\ge0}(x_i y_j)^m\) now gives the displayed coefficient formula without overcounting.

**5. Minimum ambiguity.** At \(n=1,2,3\) the complete margin fibers each have size one, as is also seen by listing the possible staircase sequences and their upper-triangular margins. At \(n=4\), the one-sided list \((2,1,0,0)\) has two matrices,

\[
M_1=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix},\qquad
M_2=\begin{pmatrix}1&1&0\\0&0&1\\0&0&1\end{pmatrix}.
\]

Their paired-degree multisets, written here with predecessor count first, are respectively

\[
\{\!\{(0,0),(0,2),(1,1),(2,0)\}\!\},\qquad
\{\!\{(0,1),(0,2),(1,0),(2,0)\}\!\}.
\]

These differ, so the corresponding posets are nonisomorphic. Complete enumeration at sizes below four, or direct evaluation of the coefficient for all permitted smaller staircase profiles, proves minimality.

## Verification

The attached program `verify_fishburn.py` independently enumerates all upper-triangular matrices with positive row and column sums through order nine (31,240 distinct isomorphism types at nine), checks that no two have the same paired degree profile, counts one-sided degree profiles as the Catalan numbers, and cross-checks the coefficient-fiber count by an independently coded row-margin dynamic recursion for every profile through order eight. It records the complete census in `verify_fishburn_output.txt`.

The distinct program `verify_posets.py` enumerates naturally topologically labeled irreflexive transitive relations through six elements, filters by nested successor sets, directly reconstructs every vertex's full predecessor neighborhood from its count and sorted successor counts, and verifies that tied degree pairs are genuine interchangeable twins. It independently recovers the known interval-order isomorphism counts \(1,2,5,15,53,217\), and independently recovers the corresponding Catalan one-sided counts. Its output is in `verify_posets_output.txt`.

Both programs require only Python 3 standard-library modules and can be reproduced with `python3 verify_fishburn.py` and `python3 verify_posets.py` from this package. The exhaustive computations are finite corroboration; the all-cardinality statements follow from the preceding proofs.

## Relationship to prior work

The nested-neighborhood characterization and the interval-order/Fishburn-matrix bijections are previously established results and are not claimed as contributions here. Dukes, Kitaev, Remmel and Steingrímsson (arXiv:1006.2696, publicly posted 2010-06-14) discuss nested strict down-sets, indistinguishable elements and the Fishburn-matrix correspondence. Jelínek (arXiv:1501.05157, posted 2015-01-21) studies Catalan and Fishburn encodings and presents a minimal matrix representation of interval orders. The present theorem concerns instead the precise information encoded by joint and one-sided strict-degree data, the exact one-sided fibers, and the induced sharp rank-two counting-logic bound. The use of the Fishburn representation makes the formula a transparent reduction to triangular contingency-table margins; it is not a new class of matrices. Related structural results may imply or overlap with individual components and warrant specialist comparison.

## Limitations

The degree reconstruction theorem applies to the complete strict order, not to Hasse arcs; replacing the vocabulary changes the invariant. The counting-logic identification is relative to the interval-order family and does not assert a distinguishing sentence against arbitrary finite structures. The coefficient formula enumerates isomorphism classes, not labeled structures or automorphism-weighted classes. Enumeration through finite sizes corroborates, but does not substitute for, the structural proof. The primary historical structural ingredients are credited. A closely related specialized result may exist in literature not available in full text, particularly treatments of refined degree enumerations of interval orders. No independent mathematical audit or priority certification has been performed.

## References

- M. Dukes, S. Kitaev, J. Remmel, and E. Steingrímsson. *Enumerating (2+2)-free posets by indistinguishable elements*. arXiv:1006.2696, first posted 2010-06-14. https://arxiv.org/abs/1006.2696 .
- V. Jelínek. *Catalan pairs and Fishburn triples*. arXiv:1501.05157, first posted 2015-01-21. https://arxiv.org/abs/1501.05157 .
- F. Disanto, E. Pergola, R. Pinzani, and S. Rinaldi. *Generation and Enumeration of Some Classes of Interval Orders*. *Order*, DOI:10.1007/s11083-012-9269-x. Abstract consulted; complete text not inspected.
- P. C. Fishburn. *Interval Orders and Interval Graphs*. Wiley, 1985 (classical reference, bibliographic background; not claimed directly inspected).
