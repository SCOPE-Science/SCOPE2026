# First failures of two-variable counting logic on finite partial orders

## Finding
Let \(C^2\) be first-order logic with equality, counting quantifiers and at most two variable symbols, in the signature consisting solely of a binary partial-order relation \(\leq\). Two finite posets are \(C^2\)-equivalent when they satisfy the same \(C^2\) sentences, without any bound on quantifier nesting or counting thresholds.

**Theorem.** Every nonempty poset with at most seven elements is \(C^2\)-identified among all finite posets: no nonisomorphic finite poset has its \(C^2\) theory. Among the \(16{,}999\) isomorphism types of eight-element posets, precisely \(16{,}997\) different \(C^2\) theories occur. Exactly two theories are represented twice; all remaining theories are represented once. In each doubleton the two representatives are nonisomorphic.

One doubleton consists of height-two posets with four minimal and four maximal elements, with cover-incidence graphs \(2C_4\) and \(C_8\), respectively. The other consists of height-three posets with two minimal, four middle and two maximal elements, as explicitly specified in `witnesses.json`: for the middle points, the number lying above each minimal point and below each maximal point is described by the two distinct matrices
\[
\begin{pmatrix}2&0\\0&2\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
All comparisons in this theorem are *within the class of finite partial orders*, not among arbitrary directed graphs or arbitrary relational structures.

## Assumptions and scope
A poset is nonempty, finite and unlabelled up to order isomorphism. For finite distinct elements \(x,y\), write \(x<y\) when \(x\leq y\) and \(x\neq y\). Its strict order is transitive, asymmetric and irreflexive. The input lists in `witnesses.json` contain **every strict comparable ordered pair**, including transitive pairs; equality supplies the reflexive part. No colours, constants, cover-relation symbol or additional predicates are present. \(C^2\) includes arbitrary numerical counting quantifiers, not just the first two quantifier ranks.

## Proof
**Step 1: Exhaustive construction.** A finite poset of order \(n\geq2\) contains a maximal element \(m\). Removing \(m\) leaves a poset \(P\) of order \(n-1\); the strict predecessors \(I=\{x:x<m\}\) form a lower ideal in \(P\). Conversely, for every \(P\) and every lower ideal \(I\), adding a new maximal element above exactly the members of \(I\) produces a poset. Thus this construction is both sound and complete for all finite posets. Its duplicates are removed by a *full* isomorphism test: the verifier backtracks over bijections and preserves both strict relation directions, with strict in/out degrees used only as sound pruning. The program asserts transitivity and irreflexivity for every generated candidate. Starting with the singleton, its exact isomorphism-type counts for orders \(1,\ldots,8\) are
\[
1,\ 2,\ 5,\ 16,\ 63,\ 318,\ 2045,\ 16999,
\]
independently matching the classical finite-poset census of Brinkmann and McKay.

**Step 2: Exact logical invariant.** Start with one vertex colour and refine a colour of \(v\) by its old colour together with the three multisets of the current colours of vertices \(u\neq v\) satisfying respectively \(u<v\), \(v<u\), or incomparability of \(u,v\). Use one shared colour dictionary for all structures being compared, not an independently renamed palette. Equal cardinalities have equal \(C^2\) theories exactly when the final colour histograms agree: this is the standard characterization of two-variable logic with counting by the stable equitable partition in a binary relational signature. The three off-diagonal atomic relation cases are exhaustive for partial orders; equality is represented by the diagonal and need not be counted as a separate neighbour. By the two-structure refinement argument, for a pair of \(n\)-element posets at most \(2n\) proper refinement rounds can separate a pair; the verifier performs \(2n+4\) rounds, so its stopping bound is sufficient for every pair. The count of vertices itself is \(C^2\)-definable by a counting sentence, hence different cardinalities cannot be equivalent.

**Step 3: Classification by an exhaustive exact certificate.** The independent invariant calculation in `verify.py` groups each enumerated isomorphism representative by its stable common-palette colour histogram. The resulting numbers of \(C^2\) classes for orders \(1,\ldots,8\) are exactly
\[
1,\ 2,\ 5,\ 16,\ 63,\ 318,\ 2045,\ 16997.
\]
At order eight the two nonsingleton classes each contain exactly two representatives. The checker constructs and recognizes both complete four-poset witness pairs from `witnesses.json` and explicitly tests their nonisomorphism and common \(C^2\) equivalence class. Thus neither an unexamined poset type nor a third doubleton is omitted by the exhaustive search. The counting result and the two soundness lemmas yield the asserted theorem.

**Step 4: Structural interpretation of the exceptions.** For the height-two pair, the two incidence graphs are a disconnected union of two four-cycles and a single eight-cycle; the degree-two regular incidence makes the one-variable equitable profiles identical, while connectivity distinguishes the posets up to isomorphism. In the height-three pair, the middle points form a four-element antichain and each has exactly one predecessor in the bottom level and one successor in the top level; each bottom point has two middle successors and each top point has two middle predecessors. Both posets have every bottom point below every top point. Hence each has the same equitable three-cell quotient \((2,4,2)\), but the multiplicity matrices shown in the finding have different entry multisets \(\{2,2,0,0\}\) and \(\{1,1,1,1\}\). Their distinct middle-incidence patterns prevent isomorphism.

## Verification
Run `python3 verify.py` in the directory containing the bundled files `verify.py` and `witnesses.json` (standard Python 3 only). The code generates every poset by ideal extension, deduplicates by complete backtracking, refines all strict-order atomic neighbour types with a global palette, compares exact classes, and checks both explicit witness pairs. It prints every order's representative count, \(C^2\)-class count and candidate count and finishes with the message `VERIFY_OK: exactly two 2-element C2 classes at n=8; none before`. At eight elements it generates \(48{,}346\) ideal-extension candidates and reduces them to \(16{,}999\) posets, of which \(16{,}997\) logical classes remain. This is exhaustive for orders at most eight, not a statistical sample. Witnesses are in `witnesses.json`; no unavailable files or network connections are required.

## Relationship to prior work
Kiefer, Schweitzer and Selman give general characterizations of identification by counting logics, including a connection between \(C^2\) and coarsest equitable partitions, and classify identification among arbitrary relational structures. Their framework supplies the logical-equivalence criterion; the theorem here is instead a **poset-restricted sharp minimum and complete first ambiguity layer**, obtained by an exact finite-poset census. Brinkmann and McKay establish the counts of finite unlabelled posets, but not their partition into \(C^2\)-equivalence classes. The OEIS record for the poset-counting sequence likewise records object counts, not the logical quotient.

## Limitations
The classification is confined to the signature with just one partial-order relation and finite models of size at most eight. It does not classify nine-point posets, infinite posets, first-order logics with extra predicates, or the stronger notion of identification among arbitrary binary relational structures. The exhaustive proof relies on the standard mathematical equivalence of stable binary-relational colour refinement and \(C^2\) theory, plus the explicit Python verification. A preexisting but unlocated finite-poset logical tabulation is a residual priority risk.

## References
1. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting* (2015), arXiv:1503.08792, https://arxiv.org/abs/1503.08792 . Especially the general relational-structure characterization and coarsest equitable partitions.
2. G. Brinkmann and B. D. McKay, *Posets on up to 16 Points*, *Order* **19** (2002), 147–179, https://users.cecs.anu.edu.au/~bdm/papers/posets.pdf .
3. OEIS A000112, *Number of partially ordered sets (posets) with n unlabeled elements*, https://oeis.org/A000112 .
