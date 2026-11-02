# Three-variable collapse of nontrivial symmetric-design incidence graphs

## Finding
Let \(\mathcal D\) be any finite symmetric \(2\)-\((v,k,\lambda)\) design with \(2\le k\le v-2\), with distinct blocks and \(\lambda\ge1\). Write \(G(\mathcal D)\) for its bipartite point–block incidence graph. For every pair \(\mathcal D,\mathcal E\) of such designs,

\[
G(\mathcal D)\equiv_{\mathrm{FO}^{3}}G(\mathcal E).
\]

The equivalence holds with *unbounded quantifier rank*, without counting quantifiers, both in the pure undirected adjacency signature and in the richer signature with unary predicates for the two sides. In particular, every nontrivial finite symmetric design yields **the same** three-variable first-order theory. This is not the claim that the graphs are isomorphic, or equivalent in counting logic.

The variable bound is best possible: if \(\mathcal F\) is the Fano \(2\)-\((7,3,1)\) design and \(\overline{\mathcal F}\) is its complement, the two incidence graphs agree on every three-variable formula, but a four-variable sentence asserting the existence of a four-cycle holds only in \(G(\overline{\mathcal F})\). Thus three is the exact largest variable width that fails to distinguish this pair in the adjacency language.

## Assumptions and scope
A symmetric \(2\)-\((v,k,\lambda)\) design has \(v\) points and \(v\) blocks; each block contains \(k\) points, each point lies on \(k\) blocks, and each two distinct points occur together in exactly \(\lambda\) blocks. Blocks are distinct. The known duality property, proved below, ensures that two distinct blocks share exactly \(\lambda\) points. The nontriviality condition is \(2\le k\le v-2\). A side-coloured incidence graph has unary \(P,B\) predicates and a binary incidence relation; a pure graph forgets \(P,B\) and retains adjacency. The logic \(\mathrm{FO}^{3}\) permits repeated quantification using only three variable symbols and arbitrarily deep formulas, but no counting quantifiers.

## Proof
**Dual-design identity.** Let \(N\) be the square point–block incidence matrix. The design axioms give
\[
NN^{\mathsf T}=(k-\lambda)I+\lambda J,\qquad
N\mathbf1=N^{\mathsf T}\mathbf1=k\mathbf1,
\quad \lambda(v-1)=k(k-1).
\]
Since \(v>k\), we have \(0<\lambda<k\), so \(N\) is invertible. The matrix \(N\) commutes with \(J\), hence \(N^{\mathsf T}N=N^{-1}(NN^{\mathsf T})N=(k-\lambda)I+\lambda J\). Thus any two blocks intersect in \(\lambda\) points.

**Uniform extension table.** Preserve for pebbled elements their sorts, equality, and incidence. There are eight ordered pair types: equal points, equal blocks, distinct points, distinct blocks, and each orientation of an incident or nonincident point–block pair. The possible types of a replacement element relative to two retained elements depend only on their ordered pair type and not on \(v,k,\lambda\) or the design.

For distinct elements of one sort (say two points), there are \(v-2\) other points. The numbers of blocks incident with both, exactly the first, exactly the second, or neither are respectively
\[
\lambda,\quad k-\lambda,\quad k-\lambda,\quad v-2k+\lambda.
\]
Every count is positive because
\[
(v-1)(v-2k+\lambda)=(v-k)(v-k-1)>0.
\]
For two distinct blocks, duality gives the same table after interchanging sorts.

For a point \(p\) and block \(L\) with \(p\in L\), the numbers of other points on/off \(L\), and of other blocks through/not through \(p\), are \(k-1,v-k,k-1,v-k\), respectively. If \(p\notin L\), these four counts are \(k,v-k-1,k,v-k-1\). All are positive. The cases in which a replacement equals either retained element are determined by equality. For a repeated pair \((x,x)\), the choices are \(x\), one of the \(v-1\) other elements of its sort, one of \(k\) incident opposite-sort elements, or one of \(v-k\) nonincident opposite-sort elements. Again every required type is available. This exhausts every possible ordered pair and every sort/equality/incidence profile of a third element.

**Unrestricted three-pebble strategy.** Play the ordinary non-counting three-pebble game on any two such designs, preserving sorts, equality and incidence at all times. When a pebble moves, at most two others remain. By the table, the second design contains an element of the requested sort having *exactly* the same equality and incidence relations to those retained pebbles; choose it as the answer. If fewer than two pebbles remain, the same existence conditions apply. The invariant is therefore maintained after every move, for arbitrarily many moves. The resulting placement always defines a partial isomorphism of the side-coloured structures. By the pebble-game characterization of finite-variable logic, all \(\mathrm{FO}^{3}\) sentences agree. Forgetting the side predicates preserves equivalence in the pure adjacency reduct.

**Strictness at four variables.** The Fano design has \(\lambda=1\), so any two points and any two blocks have at most one common opposite-sort neighbour; its incidence graph has no four-cycle. Its complementary design is the symmetric \(2\)-\((7,4,2)\) design: every two points have two common blocks, hence its incidence graph contains a four-cycle. The adjacency sentence
\[
\exists a\exists b\exists c\exists d\ \bigl(a\ne b\land a\ne c\land a\ne d\land b\ne c\land b\ne d\land c\ne d\land E(a,c)\land E(a,d)\land E(b,c)\land E(b,d)\bigr)
\]
uses four variables and distinguishes the graphs. Since their three-variable theories coincide, four is the minimum distinguishing variable width for this pair.

## Verification
Run `python3 verify_extension.py` for direct verification of the eight ordered-pair extension classes in cyclic symmetric designs of parameters \((7,3,1)\), \((7,4,2)\), \((11,5,2)\), \((13,4,1)\) and \((37,9,2)\). It also checks the sharp four-cycle witness (zero versus twenty-one cycles) and an excluded trivial boundary design \((4,3,2)\). Run `python3 verify_pebble.py` for an independently implemented fixed-point computation of non-counting three-pebble colours on four of these designs. `verification_output.txt` contains the reproduced outputs. The programs independently verify finite instances; the counting identities and back-and-forth proof above establish the infinite theorem.

## Relationship to prior work
Grohe and Otto's *Pebble Games and Linear Equations* develops general links between ordinary bounded-variable logic, non-counting pebble games and Boolean linear-algebraic certificates; it does not state this exact cross-design collapse in the inspected sections. Combinatorial work on biplanes describes symmetric designs, including the complement of the Fano plane, but not this unrestricted-depth three-variable comparison. The closest related low-depth incidence-language studies address specific families such as projective planes or biplanes and bounded *quantifier rank*, whereas this theorem covers all nontrivial symmetric designs with unbounded rank and fixed variable width. A separation criterion for three-element configurations in symmetric designs concerns existence of triple configurations, not the two-pebble extension uniformity used here. A general equivalence theorem formulated for positive binary relation extension spectra could imply the result after specialization; exhaustive priority verification is not claimed.

## Limitations
The conclusion requires ordinary first-order logic *without counting*, at most three variable symbols, and symmetric \(2\)-designs with \(v-k\ge2\). Counting quantifiers can detect degrees, and unrestricted-variable logic detects four-cycles. The trivial symmetric \(2\)-\((4,3,2)\) design does not satisfy the same extension table. Nothing is claimed about arbitrary nonsymmetric designs, higher variable widths, or a complete classification within \(\mathrm{FO}^{4}\). The mathematical argument has not undergone independent formal or expert audit.

## References
- M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first posted 2012-04-09; CSL 2012, DOI 10.4230/LIPIcs.CSL.2012.289.
- *Modelling biplanes on surfaces*, *European Journal of Combinatorics* 25 (2004), 899–909, DOI 10.1016/j.ejc.2003.05.004 (design examples and difference sets).
- Y. J. Ionin and M. S. Shrikhande, *Combinatorics of Symmetric Designs*, Cambridge University Press, 2006 (general design background).
- Y. Venema, *Points, lines and diamonds: a two-sorted modal logic for projective planes*, *Journal of Logic and Computation* 9 (1999), 601–621, DOI 10.1093/logcom/9.5.601 (related but different modal signature).
