# Three rank-four theories of finite biplanes and a sharp eleven-point representative bound

## Finding

Consider a finite **biplane** \(\mathcal B=(P,L,I)\) with point set \(P\), block set \(L\), and point–block incidence \(I\). Here the design is symmetric \(2\)-\((v,k,2)\), with \(k\ge3\), no repeated points or blocks, and
\[
v=1+\frac{k(k-1)}2,\qquad |P|=|L|=v.
\]
Interpret it as a one-domain first-order structure with unary predicates \(P,L\) naming the disjoint sorts and binary oriented predicate \(I(p,b)\). No block sizes, parameters, constants, or derived operations are named. Write \(\equiv_r\) for agreement on all sentences of quantifier rank at most \(r\), with arbitrary Boolean combinations and quantifier alternation.

**Theorem.** For any such biplanes \(\mathcal B_k\) and \(\mathcal B_{k'}\),
\[
\mathcal B_k\equiv_4\mathcal B_{k'}\quad\Longleftrightarrow\quad
(k=k'=3)\ \lor\ (k=k'=4)\ \lor\ (k\ge5\text{ and }k'\ge5).
\]
All three classes occur, represented by the complete \(2\)-\((4,3,2)\) design, the complement of the Fano plane \(2\)-\((7,4,2)\), and the Paley \(2\)-\((11,5,2)\) design. Thus every finite biplane with \(k\ge3\) has a rank-four representative on at most \(11\) points and \(11\) blocks. Both bounds are sharp. Restricting to the convention \(k\ge4\) that excludes the smallest biplane gives exactly two classes.

There is also a sharp preceding collapse: rank three has exactly two classes, \(k=3\) and \(k\ge4\). The new distinction between \(k=4\) and all \(k\ge5\) first appears at rank four.

## Assumptions and scope

The parameter \(k\) is the number of points in every block, equivalently the number of blocks through each point. Every pair of distinct points belongs to exactly two blocks. Symmetry and \(k>2\) imply every two distinct blocks meet in exactly two points. The language has equality, both unary sort predicates and one binary incidence predicate; in particular this is not a point-only collinearity theory, a counting logic, or an isomorphism classification. The theorem ranges over **every existing** finite biplane; no existence in unresolved parameter values is assumed.

For distinct blocks \(b,c\), the number of points on neither is
\[
u(k)=v-2k+2=\frac{(k-2)(k-3)}2.
\]
In particular it is \(0,1,3,6,\ldots\) for \(k=3,4,5,6,\ldots\). Exactly the same four intersection cells, with sizes \(2,k-2,k-2,u(k)\), describe the blocks incident with two distinct points.

## Proof

**1. Symmetric duality and triple intersections.** Let \(M\) be the square point–block incidence matrix. Pair balance gives \(MM^{\mathsf T}=(k-2)\mathrm{Id}+2J\), which is nonsingular for \(k>2\). Since every row and column sums to \(k\), conjugating by \(M\) yields \(M^{\mathsf T}M=(k-2)\mathrm{Id}+2J\). Thus two different blocks meet in exactly two points. This establishes duality for every incidence count below, without requiring a self-dual or transitive biplane.

For three distinct points, let \(t\) denote the number of common blocks; for three distinct blocks, use the dual interpretation of \(t\). Since two distinct blocks cannot share three points, \(t\in\{0,1\}\). For three fixed blocks \(A,B,C\), the eight point-incidence cells have sizes
\[
\begin{array}{c|c}
\text{incidence with selected blocks}&\text{size}\\\hline
ABC&t\\
AB\text{ but not }C\text{ (each pair cell)}&2-t\\
A\text{ only (each singleton cell)}&k-4+t\\
\text{none}&v-3k+6-t.
\end{array}
\]
The same formula counts candidate new blocks incident with prescribed subsets of three selected points. When \(k\ge5\), all seven cells apart from the possible zero triple cell are positive. In detail, \(2-t\ge1\), \(k-4+t\ge1\), and \(v-3k+6-t\ge1\); the last is smallest at \(k=5,t=1\), where it equals \(1\). Therefore the entire zero/nonzero extension profile of a distinct same-sort triple depends only on whether \(t=0\) or \(t=1\).

**2. Every pair admits both values of \(t\).** For distinct points \(p,q\), exactly two blocks contain both. Their intersection is exactly \(\{p,q\}\); selecting a third point from either block outside \(\{p,q\}\) gives \(t=1\), and there are \(2(k-2)\) such choices. A third point outside their union gives \(t=0\); there are \(u(k)\ge3\) such choices for \(k\ge5\). By duality this also holds for any two distinct selected blocks. Consequently both distinct same-sort triple extension profiles occur over every distinct same-sort pair.

**3. Mixed triples have parameter-independent one-step profiles.** For two selected distinct points and one selected block, the number of *other* blocks realizing each of the four incidence patterns on the selected points is obtained from \((2,k-2,k-2,u(k))\) by subtracting at most one. Every entry remains positive when \(k\ge5\). The number of *new* points on or off the selected block after excluding up to two named points remains positive, since \(k\ge5\) and \(v-k\ge6\). The dual argument treats one selected point and two selected blocks. Repeated entries reduce to smaller patterns, with equality choices explicitly preserved. Thus, for \(k\ge5\), each mixed triple's rank-one extension type is determined by its atomic incidence-and-equality diagram.

**4. Back-and-forth induction.** A rank-zero tuple type is its atomic diagram. By steps 1–3, the rank-one type of any ordered triple is determined by its atomic diagram and, only for three distinct same-sort entries, the Boolean \(t\). Step 2 guarantees that both \(t\)-profiles are available after **any** distinct same-sort pair. The elementary cell counts in step 3 guarantee the same rank-one triple types after every mixed pair of a fixed atomic diagram. Hence the rank-two type of an ordered pair is determined by its atomic diagram. Because every point has \(k\) incident and \(v-k\) nonincident blocks (both nonempty), and the dual statements hold, the rank-three type of a singleton depends only on its sort. Both sorts occur. The rank-four type of the empty tuple is therefore identical for all biplanes with \(k\ge5\). This is the usual recursive Ehrenfeucht–Fraïssé type construction, and proves the infinite equivalence statement without a symmetry or group-action assumption.

**5. Sharp separations.** Let \(\Psi_3\) state that three distinct points exist with no block containing all three:
\[
\exists p\,\exists q\,\exists r\;\bigl(P(p)\land P(q)\land P(r)\land p\ne q\land q\ne r\land p\ne r\land
\forall b\,(L(b)\rightarrow\neg(I(p,b)\land I(q,b)\land I(r,b)))\bigr).
\]
It has quantifier rank four; it is false for \(k=3\), where every point triple is a block, and true for every \(k\ge4\), since \(u(k)>0\) supplies a point not on either block through a chosen point pair.

Let \(\Psi_4\) state that two distinct blocks have **exactly one** point outside their union:
\[
\begin{aligned}
\exists a\,\exists b\,\exists p\;(&L(a)\land L(b)\land a\ne b\land P(p)
\land\neg I(p,a)\land\neg I(p,b)\\
&\land\forall q\,((P(q)\land q\ne p)\rightarrow(I(q,a)\lor I(q,b)))).
\end{aligned}
\]
Its quantifier rank is four, and by the formula for \(u(k)\) it is true **exactly** at \(k=4\). The two sentences together distinguish the three displayed classes. Finally, the rank-three sentence asserting a point outside two distinct blocks is false exactly at \(k=3\). The same pair-extension count used above shows \(k\ge4\) is uniform at rank three, proving the preceding two-class statement. The smallest representatives have \(4,7,11\) points; hence the eleven-point / twenty-two-element bound is sharp.

## Verification

Two independent, standalone C++17 programs directly compute recursive first-order types, with all equality, sort and incidence atoms, for four explicit biplanes. Their construction passes the incidence parameters, column-size, row-size, pair-concurrence, and pair-block-intersection tests. The programs do **not** assume the stated classification during the type computation.

Use `g++ -std=c++17 -O2 verify_rank3.cpp -o verify_rank3 && ./verify_rank3` and separately `g++ -std=c++17 -O2 verify_rank4.cpp -o verify_rank4 && ./verify_rank4`. Reproduced transcripts appear in `output_rank3.txt` and `output_rank4.txt`. They find respectively two and three root classes: the \(k=3\) design alone at rank three, and \(k=3\), \(k=4\), \(k\ge5\) at rank four; the Paley \(k=5\) biplane and a \(k=6\) Kummer biplane have identical rank-four root types.

These four finite checks support the argument, but the equivalence for arbitrary biplanes, including all unknown or nonisomorphic higher-order biplanes, follows from the symbolic positivity and extension-profile proof, not from enumeration.

## Relationship to prior work

Kaski and Östergård's article *There are exactly five biplanes with \(k=11\)*, available online on 22 February 2007 (DOI 10.1002/jcd.20145), classifies designs of one parameter value up to isomorphism. Its publicly accessible abstract and bibliography do not assert cross-parameter first-order logical equivalence. Its complete text was not accessed; an unrestricted novelty claim relative to its full article is not made.

Martinjak, *A class of symmetric association schemes as inclusion of biplanes* (arXiv:1401.5441, posted 21 January 2014), develops association schemes extracted from certain canonical biplane incidence matrices. Definitions, Theorem 1, examples, and conclusion were inspected. Its construction of smaller designs and association schemes neither states nor implies the present rank-four equivalence of the original whole incidence structures.

Earlier point–line incidence results for projective or affine planes concern designs with different pair-intersection structure (in particular \(\lambda=1\) for projective planes), so do not imply this \(\lambda=2\) classification. Targeted literature searches identified no direct covering theorem; this is not a mathematical proof of priority.

## Limitations

The theorem concerns ordinary first-order quantifier rank, without counting quantifiers, parameters, named degrees, or induced graph-only reducts. It does not classify biplane isomorphism types or assert existence of biplanes for every \(k\ge5\). The case \(k=2\), sometimes called the trivial two-point digon with repeated blocks, is explicitly excluded. The sharper equivalence may fail in richer signatures, particularly with counting. The novelty check was limited by full-text access to one relevant classification paper and incomplete indexing; independent validation was not performed.

## References

1. P. Kaski and P. R. J. Östergård, “There are exactly five biplanes with \(k=11\),” *Journal of Combinatorial Designs* **16** (2008), 117–127, DOI: 10.1002/jcd.20145. First online 2007-02-22.
2. I. Martinjak, “A class of symmetric association schemes as inclusion of biplanes,” arXiv:1401.5441v1 (2014-01-21), https://arxiv.org/pdf/1401.5441.
