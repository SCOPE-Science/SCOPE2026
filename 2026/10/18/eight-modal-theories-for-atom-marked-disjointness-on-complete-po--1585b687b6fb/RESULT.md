# Eight modal theories for atom-marked disjointness on complete powersets

## Finding

Let \(U\) range over all nonempty sets, finite or infinite. Form the pointed Kripke models \(M_U\) whose worlds are all nonempty subsets \(S\subseteq U\), with \(S\,R\,T\) if and only if \(S\cap T=\varnothing\). The language has Boolean connectives, one modal operator \(\Diamond\) for \(R\), and one **fixed** proposition \(p\), true exactly at singleton subsets. No arbitrary valuation of \(p\) is permitted.

Across all such models there are **exactly eight** distinct pointed modal theories, and each is defined by a formula of modal depth at most three. The numbers of pointed theories at modal depths \(0,1,2\), and \(d\geq3\) are respectively
\[
\boxed{2,\quad6,\quad7,\quad8}.
\]
Consequently the numbers of formula-equivalence classes at those respective depths are exactly
\[
\boxed{4,\quad64,\quad128,\quad256}.
\]
Modal depth three is necessary: a co-singleton subset of a three-element ground set and a co-singleton subset of a four-element ground set agree on all formulas of depth at most two, but are separated at depth three.

Every formula satisfiable in any \(M_U\), including one based on an infinite set, is satisfiable in some \(M_V\) with \(1\leq |V|\leq4\). The bound four is optimal. Satisfaction and validity over the entire class are therefore decidable by bottom-up evaluation on a fixed eight-state quotient in time linear in formula length.

## Assumptions and scope

The ground set \(U\) is nonempty, with no cardinality restriction. The carrier is exactly \(\mathcal P(U)\setminus\{\varnothing\}\), not an arbitrary induced substructure. The disjointness relation is symmetric and irreflexive. The built-in atomic proposition is \(p(S)\iff |S|=1\); \(\Box\) is the standard dual \(\neg\Diamond\neg\). A pointed theory is the set of all formulas true at one world; two pointed worlds in possibly different ground sets are equivalent when they agree on every formula of this restricted language. Formula equivalence is agreement at all such pointed worlds.

The following eight mutually exclusive types partition the pointed worlds (\(|U\setminus S|=1\) means that \(S\) is a co-singleton):

| Type | Exact condition on \(U,S\) | Types of disjoint nonempty successors |
| --- | --- | --- |
| A | \(|U|=1\), necessarily \(S=U\) | none |
| B | \(|U|=2\), \(|S|=1\) | B |
| C | \(|U|=3\), \(|S|=1\) | C, F |
| D | \(|U|\geq4\), \(|S|=1\) | D, G, H |
| E | \(|U|\geq2\), \(S=U\) | none |
| F | \(|U|=3\), \(|U\setminus S|=1\) | C |
| G | \(|U|\geq4\), \(|U\setminus S|=1\) | D |
| H | \(|S|\geq2\) and \(|U\setminus S|\geq2\) | D, H |

In particular, **all infinite ground sets share precisely the same four pointed theories as a four-element ground set**: D, E, G, and H. The four remaining types are genuine finite exceptions. Every type in the table is realized.

## Proof

**1. Exhaustiveness and the successor table.** For \(|U|=1,2,3\), direct inspection of nonempty subsets yields types A; B and E; or C, E, and F, respectively. If \(|U|\geq4\), every nonempty subset is either a singleton (D), the whole set (E), a proper co-singleton (G), or has both itself and its complement of size at least two (H). This partition is valid when \(U\) is infinite.

For any \(S\), the disjoint nonempty successors are precisely the nonempty subsets of \(U\setminus S\). A singleton in a ground set of size at least four has successors of all three types D, G, H: choose a distinct singleton, its full complement, or a two-element subset of its complement. A co-singleton has only the unique complementary singleton as successor. If \(|S|\geq2\) and \(|U\setminus S|\geq2\), a complementary singleton realizes D, and a two-element subset of \(U\setminus S\) realizes H because its complement still contains all of \(S\). No co-singleton can be disjoint from a set of size at least two. The full set has no nonempty disjoint successor. These arguments, including the existence of the requisite two-element subsets, hold for infinite \(U\). They prove every entry in the table.

**2. Upper bound from bisimulation.** Take the disjoint union of the models \(M_U\) under consideration and relate worlds exactly when they have the same table type. This relation matches the truth value of \(p\): precisely A, B, C, and D satisfy \(p\). Furthermore, the third column of the table is independent of the representative. For every successor of one world, another world of the same type has a successor of that successor's type, and conversely. Thus the type-matching relation is a Kripke bisimulation. Structural induction on formulas gives invariance under type matching; at most eight pointed theories occur, and all modal depths stabilize once these types are definable.

**3. Eight characteristic formulas and a sharp depth bound.** Put
\[
\eta:=\Diamond(\neg p\wedge\Diamond\neg p).
\]
This has modal depth two. The following formulas define the indicated types over the entire class; their claims follow either directly from the successor table or by induction on modal depth:

| Type | Characteristic formula |
| --- | --- |
| A | \(p\wedge\neg\Diamond\top\) |
| B | \(p\wedge\Diamond\top\wedge\neg\Diamond\neg p\) |
| C | \(p\wedge\Diamond\neg p\wedge\neg\eta\) |
| D | \(p\wedge\eta\) |
| E | \(\neg p\wedge\neg\Diamond\top\) |
| F | \(\neg p\wedge\Diamond p\wedge\neg\Diamond\neg p\wedge\neg\Diamond\eta\) |
| G | \(\neg p\wedge\Diamond p\wedge\neg\Diamond\neg p\wedge\Diamond\eta\) |
| H | \(\neg p\wedge\Diamond\neg p\) |

For example, a singleton has \(\eta\) precisely when it can access a nonsingleton that itself can access a nonsingleton. This first occurs when the ground set contains four elements: the intermediate nonsingleton and its disjoint nonsingleton each require at least two elements. A co-singleton can access only a singleton, so \(\Diamond\eta\) distinguishes F from G. Every table type is thus definable at depth at most three, giving at least eight theories. Combined with the bisimulation upper bound, there are exactly eight.

At depth zero the only distinction is \(p\), giving two classes. At depth one, the classes are A, B, (C together with D), E, (F together with G), and H, giving six. The formula \(\eta\) separates C and D at depth two. The classes F and G remain depth-two equivalent: each has only singleton successors, of types C and D respectively, and C and D have identical depth-one theories. Finally \(\Diamond\eta\) separates F and G at depth three. Hence the exact depth profile is \(2,6,7,8\), and the depth-three bound is strict.

Every depth-\(d\) class in this finite profile is definable at depth at most \(d\): inductively, a depth-\(d\) signature consists of its \(p\)-value and the set of depth-\((d-1)\) successor signatures, each expressed by a characteristic formula. Finite conjunctions of existence and nonexistence tests characterize the signature. Arbitrary unions of these finitely many definable classes are expressed using Boolean disjunctions. Therefore the number of formula-equivalence classes at depth \(d\) is precisely \(2\) raised to the number of depth-\(d\) pointed classes, producing \(4,64,128,256\).

**4. Optimal finite cutoff and decision procedure.** Each type has a representative over a ground set of cardinality at most four; moreover, a world of a model with \(|U|\geq4\), finite or infinite, is bisimilar to a world with the same type in \(M_{\{1,2,3,4\}}\). Thus a satisfiable formula has a model with at most four ground elements. The formula \(\neg p\wedge\Diamond\neg p\) holds exactly at type H, which needs at least four ground elements, so the cutoff is optimal.

Construct the fixed eight-state Kripke model given by the table's successor column, with \(p\) true at A, B, C, D. The preceding bisimulation and characteristic-formula proofs show that evaluating any input formula in this quotient yields exactly its truth value on each pointed type. Standard recursive Boolean and modal evaluation on eight states uses a fixed amount of work per syntax node, yielding a linear-time algorithm in the formula length. Satisfiability is the existence of a true quotient state; validity is truth at all eight quotient states.

## Verification

The standalone standard-library Python program `verify.py` constructs the disjointness graphs for every \(1\leq|U|\leq9\). It checks the exact successor-type sets at every world, evaluates all eight displayed characteristic formulas directly under the original Kripke clauses, and separately refines depth-bounded modal signatures. The run checked \(1013\) pointed worlds and \(8104\) characteristic-formula/world evaluations, and obtained the class counts \(2,6,7,8,8\) through depths zero to four with the matching \(4,64,128,256,256\) formula counts. It also verified that F and G first separate at depth three. Output: `ATOM_DISJOINTNESS_VERIFY_OK`.

This finite computation does not prove the assertion for arbitrarily large or infinite \(U\). That assertion follows from the explicit cardinality-independent successor table and bisimulation proof in Steps 1–2. Reproduce the finite checks with `python3 verify.py`; no third-party packages are required.

## Relationship to prior work

Jockwich, Tarafder, and Venturi (2026) study the internal modal logic of Boolean compatibility, \(S\cap T\neq\varnothing\), and translated propositional valuations in Boolean-valued models. Their Sections 3–6 provide the motivating Boolean-frame setting and establish broad validity and finite/infinite phenomena. The present theorem instead studies the **opposite, orthogonality relation** \(S\cap T=\varnothing\), with all nonempty subsets as states and one canonical atom-indicator valuation. Results for arbitrary valuations on compatibility frames do not imply the eight-type classification or its depth and finite-cutoff bounds.

McDonald and Bimbó (2023) develop orthogonality-based relational/topological dualities for orthomodular lattices. Their representation space uses filters and additional order/topological structure; it does not assert the present fixed-valuation modal type spectrum of nonempty elements of complete powersets. The finite bisimulation proof here is elementary, but the complete signature computation is specific to these disjointness frames.

## Limitations

The result does not concern arbitrary propositional valuations, arbitrary induced subframes, compatibility rather than incompatibility, atomless Boolean algebras, or expanded languages with graded/modal counting operators. It does not establish a classification for all orthoframes or all Boolean algebras. The linear-time procedure measures input formula length while treating the fixed eight-state quotient as constant, not construction cost for an explicitly presented enormous powerset. Novelty is assessed relative to the sources inspected, not as a proof of historical priority; an equivalent unindexed classification remains possible.

## References

1. Santiago Jockwich, Sourav Tarafder, Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1, first publicly submitted 2026-07-28. https://arxiv.org/abs/2607.25977
2. Joseph McDonald and Katalin Bimbó, *Topological Duality for Orthomodular Lattices*, *Mathematical Logic Quarterly* (2023), DOI:10.1002/malq.202200044. https://doi.org/10.1002/malq.202200044
3. Piotr Kozicki and G. A. Kavvos, *Relational Dualities and Bisimulation*, FSCD 2026, DOI:10.4230/LIPIcs.FSCD.2026.20. https://doi.org/10.4230/LIPIcs.FSCD.2026.20
