# A sharp three-round dimension cutoff for proper Boolean face posets

## Finding

For each integer \(n\ge2\), let \(Q_n\) be the finite poset of all **nonempty proper** subsets of \([n]=\{1,\ldots,n\}\), ordered by inclusion. In pure first-order logic with one reflexive inclusion relation and equality, write \(Q_n\equiv_r Q_m\) when the structures satisfy the same sentences of quantifier rank at most \(r\).

**Theorem.** For all integers \(m,n\ge2\),
\[
Q_m\equiv_3 Q_n\quad\Longleftrightarrow\quad\min(m,8)=\min(n,8).
\]
Consequently exactly **seven** rank-three theories occur, represented by \(Q_2,Q_3,\ldots,Q_8\), whose sizes are \(2,6,14,30,62,126,254\), respectively. The class containing every \(Q_n\) with \(n\ge8\) has no representative in this family with fewer than **254** elements, so this is a sharp uniform bound. At rank two the family has only three classes, represented by \(Q_2,Q_3,Q_4\): all \(Q_n\) with \(n\ge4\) are two-round equivalent.

These posets are the proper face posets of simplices: \(Q_n\) is the face poset of the boundary of an \((n-1)\)-simplex, with the empty face omitted. Its order complex is the barycentric subdivision of the simplicial boundary sphere. This geometric motivation does not add any face-rank predicates to the language.

## Assumptions and scope

The empty set and the whole ground set are removed. No constants naming either missing endpoint, Boolean operations, complement, cardinality, counting quantifiers, or predicates distinguishing face dimensions are part of the structure. The parameter \(n\) counts ground-set elements. The statement concerns entire first-order sentence theories **only through rank three**.

## Proof

**1. A uniform three-round cutoff at eight.** Consider the standard three-move Ehrenfeucht–Fraïssé game on \(Q_n,Q_m\), with \(m,n\ge8\). Suppose \(k\) subsets have already been selected in each structure, with \(r=3-k\) rounds remaining. The chosen subsets partition each ground set into its Venn cells indexed by membership patterns \(\eta\in\{0,1\}^k\). Maintain this invariant: corresponding cells either have exactly the same cardinality below \(2^r\), or both have cardinality at least \(2^r\). Initially the sole cells have sizes at least eight, so the invariant holds at \(r=3\).

When the Spoiler selects another subset, it divides every present Venn cell into its part inside the new subset and its part outside. If two old cell sizes coincide below \(2^r\), copy the split exactly. For old large cells, let \(h=2^{r-1}\). If one new piece has fewer than \(h\) points, match its size exactly and put the remainder in the opposite piece, which has at least \(h\) points. If both new pieces have at least \(h\) points, split the responding cell into two pieces each of size at least \(h\), which is possible because its size is at least \(2h\). Thus the invariant persists with \(r-1\) rounds remaining.

Every Spoiler selection is a nonempty proper subset. Its selected and unselected regions are each nonempty. The invariant ensures that the response is also nonempty and proper, so the strategy never leaves the domain \(Q_n\). When \(r=0\), the invariant preserves **which Venn cells are empty**. This determines all inclusion and equality relationships among the three selected subsets, yielding a partial isomorphism. Thus \(Q_n\equiv_3 Q_m\) whenever \(m,n\ge8\).

**2. An exact finite invariant.** To distinguish smaller parameters, encode an ordered pair of elements \(x,y\) by the relation value \(\rho(x,y)\) in \(\{0,1,2,3\}\), meaning equality, strict inclusion, strict reverse inclusion, or incomparability. Let
\[
B(x,y)=\{\bigl(\rho(x,z),\rho(y,z)\bigr):z\in Q_n\},\qquad
U(x)=\{\bigl(\rho(x,y),B(x,y)\bigr):y\in Q_n\},\qquad
H_n=\{U(x):x\in Q_n\}.
\]
Equality of the sets \(H_n\) is **equivalent** to three-round first-order equivalence of the corresponding finite posets. Indeed, \(B\) is the complete atomic third-move extension set after choosing two points, \(U\) is the complete two-move pointed type, and \(H\) is the complete empty three-move type. Induction in the finite Ehrenfeucht–Fraïssé/Hintikka recursion proves both directions, including repeated selections. No multiplicity information is needed in ordinary first-order logic without counting.

**3. Exhaustive orbit-compressed classification.** The symmetric group acts transitively on subsets of each fixed size. Therefore it is enough to calculate \(U(x)\) once for each \(|x|=i\), \(1\le i\le n-1\). An ordered pair \((x,y)\) has four disjoint Venn cells of sizes
\[
a=|x\cap y|,\quad b=|x\setminus y|,\quad c=|y\setminus x|,\quad d=n-a-b-c.
\]
All nonnegative quadruples with \(0< a+b<n\) and \(0<a+c<n\) are realized. A third subset \(z\) is characterized, for these purposes, by the numbers of points it selects from each cell: any integers \(0\le u_j\le(a,b,c,d)_j\) are possible, subject precisely to \(0<\sum_j u_j<n\). Inclusion relationships of \(x,z\) and \(y,z\) follow from these four counts. This gives a finite **exact arithmetic enumeration**, without constructing the exponentially many subsets. The code `verify_orbit_spectra.py` implements these formulas and calculates the complete nested sets \(H_n\) for every \(2\le n\le16\). In particular the seven \(H_2,\ldots,H_8\) are pairwise unequal, and \(H_8=H_9\). A logically independent `verify_independent_types.py` forms actual bit-subsets and directly computes the same full recursive types for every \(2\le n\le9\). It recovers the same exact seven classes.

Combining the finite separation \(H_2,\ldots,H_8\) with the proved uniform cutoff at eight establishes the theorem for **all** integer parameters. The verification beyond eight is a check only, not an extrapolation.

**4. Sharpness and rank two.** The smallest member of the stable class is \(Q_8\), with \(2^8-2=254\) elements; all smaller dimensions have different rank-three types by Step 3. At rank two a selected element is either minimal, maximal, or neither, when \(n\ge4\). These types have respective possible relations to another selected point \(\{=,<,\parallel\}\), \(\{=,>,\parallel\}\), and \(\{=,<,>,\parallel\}\). For \(n=3\) only the first two occur, and for \(n=2\) every element has type \(\{=,\parallel\}\). These sets of pointed one-move types completely classify two-round sentences, proving the stated three classes.

## Verification

With Python 3 and only its standard library, run:

```sh
python3 verify_orbit_spectra.py
python3 verify_independent_types.py
```

The scripts are independent realizations of the finite rank-three invariant: one enumerates feasible Venn-cell splits, the other checks the actual subsets directly. Their expected console outputs are preserved as `evidence/orbit.stdout.txt` and `evidence/independent.stdout.txt`. They verify all seven finite classes and the collapse between \(n=8\) and \(n=9\). The infinite cutoff rests entirely on Step 1.

## Relationship to prior work

Armstrong and Hersh use the proper part of the Boolean lattice and its spherical order complex in a poset-topological setting (2009), but the inspected full introduction and poset-map material do not address bounded first-order theories. Bova, Ganian and Szeider develop model-checking methods for finite posets (2014), not this exact classification. He studies first-order quantifier hierarchies and game methods (2014), without an equivalent classification in the accessible abstract.

Two related prior results require different implication analyses. A full **Boolean-algebra-language** theorem asserts rank-three equivalence of Boolean algebras once the number of atoms is at least eight. Since \(Q_n\) is definable there by the **quantifier-free** condition \(x\ne0\land x\ne1\), that theorem **already implies the stable-direction equivalence** \(Q_n\equiv_3Q_m\) for all \(m,n\ge8\). The present elementary game proof independently establishes this implication. But first-order sentences in the full Boolean-algebra language have operations unavailable in the pure order reduct, so its lower-size separation statements **do not imply** that \(Q_2,\ldots,Q_8\) are pairwise rank-three distinct. Those lower bounds and the exact classification require the extension-type calculation. Separately, an existing theorem for the **full Boolean inclusion posets** (with endpoints retained) has rank-three stabilization at dimension six; deleting those endpoints is not a quantifier-rank-preserving interpretation in the pure order language, and the new classification shows a genuinely different threshold. Prior topological work on the proper Boolean sphere does not address the exact logical classes.

## Limitations

Only the proper-subset inclusion language and rank at most three are classified. Nothing is established about richer Boolean-algebra signatures, higher first-order ranks, counting quantifiers, or arbitrary simplicial complexes. Historical-priority review is not exhaustive. The finite separation is proved by a reproducible exact calculation; the unbounded equivalence is proved independently by the explicit game strategy.

## References

1. D. Armstrong and P. Hersh, *Sorting orders, subword complexes, Bruhat order and total positivity*, arXiv:0909.2828, first submitted 2009-09-15; inspected introduction and Sections 1–2 of accessible HTML.
2. S. Bova, R. Ganian and S. Szeider, *Model Checking Existential Logic on Partially Ordered Sets*, arXiv:1405.2891, first submitted 2014-04-15; abstract inspected.
3. Y. He, *On the strictness of the quantifier structure hierarchy in first-order logic*, arXiv:1409.7488, first submitted 2014-09-26; abstract inspected.
