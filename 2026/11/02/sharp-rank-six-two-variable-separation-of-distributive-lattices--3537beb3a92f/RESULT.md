# Sharp rank-six two-variable separation of distributive lattices with at most seven join-irreducibles

## Finding
Let \(\mathscr D_7\) consist of all finite distributive lattices with at most seven join-irreducible elements, including the one-element lattice. Work in the pure relational language of equality and reflexive order \(\preccurlyeq\). Write \(\equiv_q^{\mathrm{FO}^2}\) for equivalence of all ordinary first-order sentences of quantifier rank at most \(q\), using only the two reusable symbols \(x,y\), without counting quantifiers.

**Exact finite classification.** The class \(\mathscr D_7\) has \(2451\) isomorphism types. Their numbers of distinct \(\equiv_q^{\mathrm{FO}^2}\)-classes for \(q=1,2,3,4,5,6\) are, respectively,
\[
1,\quad5,\quad78,\quad789,\quad2449,\quad2451.
\]
At rank five precisely two equivalence classes have two nonisomorphic members, and every other class is a singleton. The two exceptional pairs contain lattices of sizes \(34\) versus \(32\), and \(16\) versus \(14\). At rank six all \(2451\) isomorphism types separate. Hence **six is the sharp uniform two-variable quantifier rank needed to distinguish any two nonisomorphic members of \(\mathscr D_7\)**. This is an exact finite result, not a claim about all finite distributive lattices.

Explicit generating posets for the exceptional pairs are specified by strict-upper-set bitmask tuples. For \(P=\{0,\ldots,6\}\), the integer in position \(i\) has bit \(j\) set exactly when \(i<_{P}j\). The four tuples are

```
Pair A: (112,80,96,0,0,0,0) and (112,112,96,0,0,0,0)
Pair B: (124,120,64,96,96,0,0) and (124,120,64,112,96,0,0)
```

Their lattices are the corresponding downset lattices \(J(P)\). Both pairs agree through rank five and differ at rank six. The appendix program gives a directly repeatable independent check of these explicit witnesses.

## Assumptions and scope
Birkhoff's representation identifies each finite distributive lattice \(L\) with the inclusion-ordered downset lattice \(J(P)\), where \(P\) is its finite poset of join-irreducibles. The rank of \(L\) equals \(|P|\). Thus classifying \(\mathscr D_7\) means classifying *all* posets \(P\) of sizes zero through seven, not a selection of lattices by cardinality, symmetry or chosen presentations. Every downset is represented by a bitmask, and \(A\preccurlyeq B\) is equivalent to bitwise inclusion.

## Proof
**Completeness of finite enumeration.** The singleton empty poset initializes the enumeration. Given one representative of every poset on \(n\) elements, generate all posets on \(n+1\) elements by adjoining one maximal element whose set of predecessors is any downset of the old poset. Any nonempty finite poset has a maximal element, so deleting it proves inductively that every isomorphism type occurs. Every pair of candidates is compared using directed-graph isomorphism of its strict transitive order; the preliminary degree and downset-count buckets are only isomorphism-invariant filters and never prevent a necessary comparison. The full isomorphism-class counts for orders zero to seven are
\[
1,1,2,5,16,63,318,2045,
\]
whose sum is \(2451\). The count through seven also agrees with the classical unlabeled-poset enumeration; in particular the full seven-element layer has \(2045\) types.

**Exact two-variable logical types.** In each lattice define the four-valued ordered-pair atomic relation \(\rho(a,b)\in\{=,<,>,\parallel\}\). Set \(T_0(a)\) to the same zero-round unary type for every element and recursively define
\[
T_{t+1}(a)=\{(\rho(a,b),T_t(b)):b\in L\}.
\]
The root signature \(U_t(L)=\{T_t(a):a\in L\}\) uses *sets*, not multisets. Two structures have the same \(U_t\) exactly when they satisfy the same \(\mathrm{FO}^2\) sentences of quantifier rank at most \(t+1\). This follows by induction: a two-variable formula with one free variable and one more layer of quantification tests existence or nonexistence of a related element having a preceding unary type, and every binary atom is determined by \(\rho\). Conversely each finite unary type is specified by conjunctions of its positive and negative one-step extension requirements. An outer existential quantifier specifies which unary types occur. Bound-variable reuse is permitted; equality moves are included in \(\rho\). No counting is introduced.

**Exhaustive exact calculation.** The deterministic program `dist_fo2_census.py` executes the complete poset generation and the preceding recurrence simultaneously over the entire \(2451\)-member family. It prints the six class counts stated above, confirms exactly two nontrivial classes at rank five, and verifies all signatures distinct at rank six. Exact integer bitmasks, finite sets, directed-graph isomorphism and canonical sorted type identifiers are used, with no randomized or floating-point tests. The independent `exceptional_fo2_check.py` constructs only the four exceptional downset lattices from the displayed masks, uses a different direct set-of-pair-types recurrence, and verifies the predicted equivalences through rank five and inequivalences at rank six. Since all isomorphism types are exhaustively represented, no unlisted lattice can invalidate the rank-six upper bound; the two explicit rank-five collisions prove sharpness.

## Verification
With Python 3 and the `networkx` package installed, run from the directory containing the files:

```sh
python3 dist_fo2_census.py
python3 exceptional_fo2_check.py
```

Their exact recorded outputs are in `dist_fo2_census.out` and `exceptional_fo2_check.out`. The main script takes each poset up to isomorphism, generates its entire downset lattice, and performs exact uncounted two-variable Hintikka-type refinement. The second script needs only the Python standard library. The reported exhaustive certificate is *finite*: no statement is made about lattices with more than seven join-irreducibles.

## Relationship to prior work
Birkhoff's classical representation theorem and Erné–Heitzig–Reinhold's 2002 complete enumeration methods supply the underlying bijection and context, but do not classify finite distributive lattices by the expressive power of noncounting \(\mathrm{FO}^2\). Kiefer–Schweitzer–Selman study identification in the strictly stronger counting logic \(C^2\), among all finite relational structures rather than the present class and rank bound. Other existing restricted-family results handle divisor lattices (products of chains) or bounded-rank products of two chains; neither implies the exhaustive \(2451\)-type classification or the two exceptional collisions across arbitrary distributive lattices. This exact comparison is not a proof of absolute historical priority.

## Limitations
The theorem is **relative** to the class of finite distributive lattices with at most seven join-irreducibles. It does not say a lattice is uniquely identified among arbitrary finite posets; nor does it prove that \(\mathrm{FO}^2\) distinguishes arbitrary finite distributive lattices with eight or more join-irreducibles. The program depends on `networkx` for graph isomorphism in the full census; the witness check is standard-library-only. The external-priority search is substantial but not exhaustive, and there is no independent mathematical audit.

## References
1. M. Erné, J. Heitzig, J. Reinhold, *On the Number of Distributive Lattices*, Electronic Journal of Combinatorics 9 (2002), #R24, accepted April 1, 2002, DOI 10.37236/1641; full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r24/pdf .
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, first arXiv version March 30, 2015, arXiv:1503.08792v1, https://arxiv.org/pdf/1503.08792 .
3. A. Dawar, B. Holm, *Pebble Games with Algebraic Rules*, Fundamenta Informaticae 150 (2017), DOI 10.3233/FI-2017-1471, accepted manuscript https://www.repository.cam.ac.uk/items/0e270edb-84d7-451b-b52e-f6ff267bb592 .
