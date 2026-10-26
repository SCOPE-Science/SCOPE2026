# Twenty-one rank-three theories and a sharp nine-point kernel for finite equivalence relations

## Finding
In the language with equality and one binary symbol \(E\) interpreted as an equivalence relation, the nonempty finite structures have exactly \(21\) distinct rank-\(3\) first-order theories. Every such structure has a rank-\(3\)-equivalent representative on at most \(9\) elements, and no smaller uniform bound is possible. Every theory has one smallest representative up to isomorphism. The representatives collectively have \(103\) elements (counted with multiplicity).

The complete list of their equivalence-class multiplicity vectors \((m_1,m_2,m_3)\), where \(m_j\) is the number of classes of size exactly \(j\), is:
  - \((0,0,1)\), \((0,0,2)\), \((0,0,3)\)
  - \((0,1,0)\), \((0,1,1)\), \((0,2,0)\), \((0,2,1)\), \((0,3,0)\)
  - \((1,0,0)\), \((1,0,1)\), \((1,0,2)\), \((1,1,0)\), \((1,1,1)\), \((1,2,0)\)
  - \((2,0,0)\), \((2,0,1)\), \((2,0,2)\), \((2,1,0)\), \((2,1,1)\), \((2,2,0)\)
  - \((3,0,0)\)

The Boolean algebra of properties of nonempty finite equivalence relations expressible by rank-at-most-\(3\) sentences therefore has \(2^{21}\) elements.

## Assumptions and scope
All structures are finite and nonempty; \(E\) is reflexive, symmetric and transitive, with no unary predicates, constants, orders, or second binary relation. The quantifier rank is the maximum nesting depth of quantifiers; \(\equiv_3\) means agreement on all sentences of rank at most \(3\). All isomorphisms preserve \(E\). The claim concerns **all** nonempty finite equivalence structures, not structures of bounded size or only equivalence relations with small blocks.

## Proof
**Step 1 (infinite family reduced without extrapolation).** For a structure \(A\), group its equivalence classes by size \(1\), size \(2\), and size at least \(3\). Replace every size-at-least-\(3\) class by a size-\(3\) class, then retain at most \(3\) classes of each of the three sizes. Call the result \(C(A)\). In the three-move Ehrenfeucht–Fraïssé game on \(A\) and \(C(A)\), the duplicator matches previously visited classes by these size categories, and matches distinct selected elements within each matched class. When the spoiler enters a new class after at most two moves, at most two classes of any category have been used, leaving a fresh one on the other board if the class exists. In a class of type at least \(3\), at most two elements have previously been selected, leaving a fresh one at move three. Types \(1\) and \(2\) have the same exact sizes on both sides. This preserves equality and \(E\) among all selected points. Hence \(A\equiv_3 C(A)\).

Every \(C(A)\) is a nonempty disjoint union of \(m_j\) classes of size \(j\), where \(0\le m_j\le3\) for each \(j=1,2,3\). There are exactly \(4^3-1=63\) such isomorphism types. Thus checking these \(63\) finite representatives really is exhaustive for the original infinite family.

**Step 2 (exact finite-type recursion).** For a structure \(A\), a tuple \(\bar a\) and rank \(r\), let \(H_r(A,\bar a)\) be the usual finite Hintikka signature. Define \(H_0\) to be the equality/\(E\) atomic diagram of \(\bar a\); recursively take \(H_{r+1}\) to be the pair consisting of this same atomic diagram and the **set** of \(H_r(A,\bar a b)\) over every element \(b\in A\). By induction on \(r\), equality of these signatures is equivalent to agreement on all formulas of rank at most \(r\) with the indicated free variables: the possible extension types implement both the forth and back conditions of the Ehrenfeucht–Fraïssé game. This is the standard finite-relational back-and-forth characterization, and uses no assumption that a finite sample generalizes to larger structures.

The complete computation on the \(63\) canonical structures, starting with three free variables and zero remaining moves, has successively \(12\), \(16\), \(18\), and \(21\) different signatures at \((3,0)\), \((2,1)\), \((1,2)\), and \((0,3)\), respectively. The final \(21\) signatures partition the \(63\) canonical forms; minimizing \(m_1+2m_2+3m_3\) within each signature gives precisely the displayed \(21\) distinct vectors, each uniquely minimal. This is a finite exact derivation, fully reproduced by `verify.py`; the program generates every tuple and every child signature, rather than sampling.

**Step 3 (independent game replay).** A separate recursive routine in `verify.py`, which does not consult the computed Hintikka IDs, directly tests the three-move two-sided spoiler–duplicator game. It independently establishes that all \(210\) unordered pairs of distinct displayed representatives are separated and that each of the \(63\) canonical structures is equivalent to its designated representative. This duplicates the essential finite classification by a different state transition rule.

**Step 4 (sharpness of the finite-model cutoff).** Every displayed representative has at most \(9\) elements (the largest is three classes each of size three); Step 1 and Step 2 therefore prove the upper bound. For the matching lower bound consider the conjunction of rank-\(3\) sentences
\[
\bigl(\exists x\,\exists y\,\exists z\, [\neg E(x,y)\wedge\neg E(x,z)\wedge\neg E(y,z)]\bigr)
\wedge
\bigl(\forall x\,\exists y\,\exists z\,[x\ne y\wedge x\ne z\wedge y\ne z\wedge E(x,y)\wedge E(x,z)]\bigr).
\]
It says there are at least three distinct equivalence classes and every class contains at least three points. It is satisfied by the disjoint union of three three-point equivalence classes but no structure of fewer than \(9\) points. Thus the bound \(9\) is sharp, independently of any computer enumeration.

Finally, distinct finite Hintikka signatures are separated by rank-at-most-\(3\) sentences: turn the finite recursive type descriptions into formulas using conjunction, negation and one existential quantifier at each stage. Arbitrary unions of the \(21\) definable classes are therefore definable by finite disjunctions of these sentences, and no rank-at-most-\(3\) sentence can split any one class. There are \(2^{21}\) resulting definable properties.

## Verification
Run `python3 verify.py` using Python's standard library. The expected deterministic output is included as `verify_output.txt`. It checks all \(63\) canonical structures, the four levels of the exact signature recursion, all \(21\) minimal forms, all \(210\) pairwise representative games, and each of \(63\) membership games. The reported output ends in `VERIFY_OK`. The direct EF solver is a check of the finite calculation; the independent infinite-family reduction and the explicit lower-bound formula above are mathematical proofs, not experiments.

## Relationship to prior work
Dawar and Otto (LICS 2005, Section 3.2; expanded journal version, Section 3.3) investigate modal characterisation over finite equivalence frames, including structures with multiple equivalence relations and unary predicates, through bisimulation-invariant first-order logic. Their stated theorems provide a different sort of expressive-completeness result and do not state the exact number of pure one-relation rank-\(3\) theories or the sharp \(9\)-point universal kernel. The general Ehrenfeucht–Fraïssé machinery used in the proof is standard and is not claimed as new. He (2014) addresses strictness of quantifier-structure hierarchies over general finite structures, rather than the present exact finite relational quotient.

## Limitations
The claim excludes empty structures and any vocabulary enrichment. It gives an exact profile at quantifier rank \(3\), not a closed formula for arbitrary rank. The finite verifier is a replayable exhaustive finite certificate, not an external independent audit. Exact classification might already be present in unindexed examples or folklore despite the recorded literature and database searches; no uniqueness assertion beyond the mathematical equivalence classes is inferred from database coverage.

## References
1. A. Dawar and M. Otto, *Modal Characterisation Theorems over Special Classes of Frames*, LICS 2005, pp. 21–30, doi:10.1109/LICS.2005.27. Public conference: 26–29 June 2005. https://www.cl.cam.ac.uk/~ad260/papers/lics05.pdf
2. A. Dawar and M. Otto, *Modal characterisation theorems over special classes of frames*, *Annals of Pure and Applied Logic* **161** (2009), 1–42, doi:10.1016/j.apal.2009.04.002. https://www.cl.cam.ac.uk/~ad260/papers/apal09.pdf
3. Y. He, *On the strictness of the quantifier structure hierarchy in first-order logic*, *Logical Methods in Computer Science* **10** (2014), arXiv:1409.7488, initial public preprint 26 September 2014. https://arxiv.org/abs/1409.7488
