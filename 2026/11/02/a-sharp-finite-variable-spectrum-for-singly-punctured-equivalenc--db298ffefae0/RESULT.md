# A sharp finite-variable spectrum for singly punctured equivalence grids

## Finding
Let \(E\) and \(F\) be *named*, reflexive equivalence relations on a finite set. For integers \(m,n\ge2\), define \(G_{m,n}\) on the whole Cartesian product \([m]\times[n]\), with \(E((i,j),(i',j'))\) iff \(i=i'\), and \(F((i,j),(i',j'))\) iff \(j=j'\). Let \(H_{m,n}\) be its induced structure after removing the cell \((0,0)\). The two equivalence symbols are never interchanged.

Write \(\equiv_{\mathrm{FO}^{k}}\) for equivalence in counting-free first-order logic with at most \(k\) reusable variable names and *arbitrary* quantifier depth. The following is a complete classification of the nonempty family \(\{G_{m,n},H_{m,n}:m,n\ge2\}\).

For \(k=1\), every structure belongs to one theory. For \(k=2\), there are exactly four theories: (i) all full grids together with punctured grids having both dimensions at least three; (ii) punctured grids with \(m=2,n\ge3\); (iii) punctured grids with \(m\ge3,n=2\); and (iv) the punctured \(2\)-by-\(2\) grid.

For every \(k\ge3\), full and punctured grids are never equivalent. Within the full grids,
\[
G_{m,n}\equiv_{\mathrm{FO}^{k}}G_{u,v}
\quad\Longleftrightarrow\quad
\min(m,k)=\min(u,k),\ \min(n,k)=\min(v,k).
\]
Within the punctured grids,
\[
H_{m,n}\equiv_{\mathrm{FO}^{k}}H_{u,v}
\quad\Longleftrightarrow\quad
\min(m-1,k)=\min(u-1,k),\ \min(n-1,k)=\min(v-1,k).
\]
There are exactly \((k-1)^2+k^2=2k^2-2k+1\) theories at each such width. Their unique smallest representatives are \(G_{\min(m,k),\min(n,k)}\) and \(H_{1+\min(m-1,k),1+\min(n-1,k)}\), respectively. The variable-width hierarchy is strict at every step: a single erased cell in dimensions at least three is invisible at width two but visible at width three, and higher widths successively reveal additional ordinary rows and columns.

## Assumptions and scope
Only equality and the two named binary equivalence predicates \(E,F\) occur. There are no constants, row or column sorts, counting quantifiers, extra labels, orders, or coordinates in the signature. Cartesian coordinates are merely a representation of the underlying relational structures. All dimensions are integers at least two; the position of the one omitted cell is immaterial up to isomorphism. The equivalence relations are interpreted on the *remaining* domain of an induced deletion.

## Proof
**One and two variables.** In the one-variable language all atomic instances of \(E\), \(F\), and equality on the same variable are true, so all nonempty structures agree. For two variables, when one element \(x\) is held, the possible second-element types are: equality, the same \(E\)-class only, the same \(F\)-class only, and neither. In every full grid and in every punctured grid with \(m,n\ge3\), all four types occur for every \(x\). A permanent two-pebble response therefore exists even between full and punctured grids in this range.

If \(m=2,n\ge3\) and one cell is omitted, the surviving cell in the deficient \(F\)-class is the unique \(F\)-singleton. The remaining vertices fall into two nonempty classes, depending on whether they share its \(E\)-class. Each of these latter classes contains at least two vertices; the set of possible second-element relation types and vertex classes, relative to every held vertex, is independent of \(n\ge3\). This defines a permanent two-pebble correspondence across all such punctures. The case \(m\ge3,n=2\) is dual, with \(E,F\) interchanged. The \(2\)-by-\(2\) puncture has three elements and is a single isomorphism type. These four phases are separated by two-variable sentences asserting the existence of an \(E\)-singleton or an \(F\)-singleton: \(\exists x\,\forall y(E(x,y)\Rightarrow x=y)\), and its \(F\)-analogue.

**Three-variable definition of the defect.** In a punctured grid set
\[
R(x):=\exists y\,\neg\exists z\,[E(x,z)\land F(z,y)],
\qquad
C(x):=\exists y\,\neg\exists z\,[F(x,z)\land E(z,y)].
\]
The formula \(R\) holds exactly at cells of the deficient \(E\)-class (the row of the deletion), and \(C\) holds exactly at cells of the deficient \(F\)-class. On a full grid neither formula is realized. Thus \(\exists x\,R(x)\) distinguishes the full and punctured phases with just three variables. In a puncture, \(\neg R\) and \(\neg C\) respectively identify the ordinary rows and ordinary columns.

**Lower bound on distinguishability.** With \(k\ge3\) variables, a formula requiring \(j\le k\) elements in pairwise different \(E\)-classes distinguishes whether there are at least \(j\) rows. In the punctured phase one also requires \(\neg R(x_i)\) for every chosen element, thereby counting *ordinary* rows. Even if \(j=k\), each occurrence of \(R(x_i)\) can bind two of the other \(k-1\) variable names locally; the scopes do not interfere with the other conjuncts. Applying the analogous construction to \(F\) and \(C\) proves that any difference between the stated clipped parameter pairs is detected with \(k\) variables.

**Permanent upper-bound strategy.** Suppose the clipped parameter pairs agree. During a \(k\)-pebble game, maintain injective coordinate correspondences between the *currently occupied* row indices and column indices. For punctures, the distinguished deficient row and column correspond to their counterparts; all remaining row and column indices are ordinary. Every matched pebble pair represents the same corresponding ordered pair of indices. This preserves equality, \(E\), and \(F\). After a pebble is lifted, at most \(k-1\) row indices and \(k-1\) column indices are occupied. Any newly requested ordinary index can be matched because either both dimensions have the same number below \(k\), or both have at least \(k\) available ordinary indices in total. The sole omitted cell cannot be requested in either structure and is respected by the distinguished-index correspondence. This maintains a partial isomorphism for arbitrarily many moves, proving all claimed implications at unrestricted quantifier depth. For full grids the same argument omits the distinguished indices.

**Enumeration and sharpness.** At width \(k\ge3\), a full-grid theory has one ordered pair of clipped dimensions from \(\{2,\ldots,k\}^2\). A punctured-grid theory has one ordered pair of clipped ordinary-coordinate counts from \(\{1,\ldots,k\}^2\). Hence the stated count follows. The smallest representative replaces each dimension by its least value realizing the same truncated count. Strictness from one to two variables is witnessed by a full and a punctured \(2\)-by-\(2\) grid. From two to three it is witnessed by a full and punctured \(3\)-by-\(3\) grid. For every \(k\ge3\), the punctured grids \(H_{k+1,3}\) and \(H_{k+2,3}\) agree at width \(k\), but not at width \(k+1\).

## Verification
Two standalone Python programs using only the standard library are included. Run `python3 verification/verify_two_equiv_grid.py` and `python3 verification/verify_equiv_two_pebble.py` from the package root. The first computes non-counting variable-type refinement jointly across model pairs: all \(153\) pairs from \(18\) small full/punctured grids are checked at widths two and three, supplemented by six three-variable cutoff comparisons and ten four-variable boundary comparisons. The second independently computes the two-pebble vertex-type transition signatures for \(50\) full/punctured grids and compares all \(1225\) pairs. Both produced `VERIFIED`, with recorded outputs supplied. These are finite diagnostics only: the unbounded claims rest on the permanent game strategies above.

## Relationship to prior work
Two equivalence relations are a classical setting for two-variable logic. Kieroński, Michaliszyn, Pratt-Hartmann, and Tendera study satisfiability and equivalence-closure complexity; their full text includes a grid encoding with intersections of equivalence classes. Their complexity results and constructions do not state the exact counting-free variable-width equivalence spectrum for complete grids versus one-point induced deletions. Kieroński and Otto study small-substructure methods for the two-variable fragment, while Grohe and Otto develop general (including non-counting) pebble-game methodology. The present result specifies a concrete, sharp single-erasure spectrum rather than a satisfiability complexity bound or a general game correspondence.

## Limitations
The theorem concerns only full Cartesian products and a *single* removed cell, with both equivalences separately named and each coordinate set of size at least two. It neither classifies arbitrary patterns of missing cells nor structures with two equivalence relations having multiple elements in one joint class. Adding counting, a coordinate order, constants, or auxiliary predicates changes the logical theory. The mathematical proof is self-contained; the historical novelty comparison is limited to inspected accessible sources, and a stronger unlocated result could imply the spectrum.

## References
- E. Kieroński, J. Michaliszyn, I. Pratt-Hartmann, and L. Tendera, *Two-Variable First-Order Logic with Equivalence Closure*, Proceedings of LICS 2012, DOI: 10.1109/LICS.2012.53; accessible author full-text transcript at `https://www.researchgate.net/publication/261055330_Two-Variable_First-Order_Logic_with_Equivalence_Closure`.
- E. Kieroński and M. Otto, *Small Substructures and Decidability Issues for First-Order Logic with Two Variables*, Journal of Symbolic Logic 77 (2012), 729–765, DOI: 10.2178/jsl/1344862160.
- M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first posted 2012-04-09), `https://arxiv.org/abs/1204.1990`.
