# A sharp five-name stabilization for definable quotients of ordered pairs

## Finding
Let \(A\) be a nonempty finite or infinite set of atoms in the pure equality language, and let \(Q(A)\) be the set of parameter-free definable equivalence relations on \(A^2\). Equivalently, these are the \(\operatorname{Sym}(A)\)-invariant equivalence relations. The complete cardinality spectrum is
\[
|Q(A)|=\begin{cases}
1,&|A|=1,\\
7,&|A|=2,\\
16,&|A|=3,\\
15,&|A|=4,\\
13,&|A|\ge5\text{ (including infinite sets).}
\end{cases}
\]
Thus five atoms are necessary and sufficient for stabilization to the infinite-atom answer; the finite spectrum is not monotone.

## Assumptions and scope
An equivalence relation on \(A^2\) is **definable** when a first-order formula of pure equality, without constants or parameters, defines it. The full permutation group acts coordinatewise on pairs. Every permutation-invariant subset of \(A^4\) is a union of equality-pattern orbits, each defined by a Boolean combination of equalities, so invariance and parameter-free definability coincide both for finite and infinite \(A\). We count distinct labeled relations, not isomorphism types of quotients. The assertion applies to all nonempty cardinals, with no ordering or predicates on \(A\).

## Proof
For \(|A|\ge2\), split \(A^2\) into the two transitive permutation orbits \(D=\{(a,a):a\in A\}\) and \(O=\{(a,b):a\ne b\}\). On \(D\), an invariant equivalence relation is either equality or universal, because the natural permutation action on atoms is primitive (also directly because all distinct pairs of atoms form one orbit).

**Off-diagonal classification.** The number \(u(A)\) of invariant equivalence relations on \(O\) is \(2,6,6,5\) when \(|A|=2,3,4,\ge5\), respectively. The complete lists justify these numbers:

* At size two, \(O\) has two elements and admits equality or the universal relation.
* At size three, \(O\) is a regular \(S_3\)-set; its invariant equivalence relations correspond exactly to the six subgroups of \(S_3\): the identity subgroup, three order-two subgroups, the order-three subgroup, and the whole group.
* At size four, the six relations are equality, equality of first coordinates, equality of second coordinates, equality of unordered underlying two-element sets, equality of unordered sets **up to complement** in \(A\), and the universal relation. The fifth relation has three classes, each joining the two orientations of a two-element subset with the two orientations of its complementary subset.
* At size at least five, precisely the five listed relations remain after deleting the complementary-set relation. To verify completeness, classify a related pair of directed edges by the equality pattern of their four coordinates. A related pair with a common first coordinate generates first-coordinate equality; similarly for a common second coordinate, while reversal generates unordered-pair equality. A mixed-role common endpoint generates the universal relation after transitivity and relabeling. A related pair with four distinct endpoints generates universality because the disjointness graph of unordered pairs, \(KG(|A|,2)\), is connected for \(|A|\ge5\); it is also connected when \(A\) is infinite, choosing fresh atoms. The only exception is \(|A|=4\), where the disjointness graph has three two-vertex components and creates the complementary-set equivalence. If more than one of the two coordinate-equality patterns, or either with reversal, is present, transitivity again makes the relation universal. These exhaust all four-coordinate equality patterns; at size three the preceding regular-action argument handles the patterns that collapse.

**No mixing between \(D\) and \(O\).** Choose either of the two independent relations on \(D\) and any of the \(u(A)\) relations on \(O\). This contributes \(2u(A)\) relations.

**Mixing between \(D\) and \(O\).** If one diagonal element is equivalent to an off-diagonal element, equivariance makes every off-diagonal element equivalent to some diagonal element. If the diagonal elements are all equivalent, the entire relation is universal. Otherwise, the diagonal elements are pairwise inequivalent, and each off-diagonal element has a unique equivalent diagonal element. These relations correspond bijectively to equivariant functions \(f:O\to A\), by putting \((a,b)\) in the class of \((f(a,b),f(a,b))\). Such a function is determined by \(f(a,b)\) for one fixed distinct pair \((a,b)\); its value must be fixed by every permutation fixing \(a\) and \(b\). There are exactly two choices \(a,b\) at sizes two and at least four, but exactly three at size three (the third atom is fixed as well). Hence the mixed counts, including the universal relation, are \(3,4,3,3\) at sizes \(2,3,4,\ge5\).

Combining the unmixed and mixed cases gives, in order, \(2\cdot2+3=7\), \(2\cdot6+4=16\), \(2\cdot6+3=15\), and \(2\cdot5+3=13\). At size one, \(A^2\) has one element and just one equivalence relation. The distinct values at sizes four and five prove that stabilization cannot start earlier. \(\square\)

## Verification
Run `python3 verify_pair_quotients.py` with the Python standard library. It constructs all fifteen equality patterns on four coordinates, groups them into eleven classes under swapping the two ordered-pair arguments, and enumerates all symmetry-closed choices. For each size one through six, it evaluates the resulting relations on \(A^2\), checks reflexivity and transitivity using bitset rows (symmetry is by construction), and deduplicates collapsed patterns in small universes. Its output is `QUOTIENT_COUNTS=1,7,16,15,13,13` and `VERIFICATION_OK`. For sizes at least six, every transitivity failure is witnessed using at most six atoms (three ordered pairs), so the finite pattern check also cross-checks the infinite-atom classification; the structural argument above establishes the theorem independently of the experiment.

## Relationship to prior work
Ciobanu's 2026 finitely supported structures papers motivate the distinction between finite contexts and invariant/equivariant relations. Bojańczyk's nominal-sets framework and Healy–Klin's first-order definable structures furnish the general viewpoint that equality-pattern orbits allow finite presentations. The present claim instead classifies **all invariant equivalence relations on ordered pairs** and identifies the sharp nonmonotone finite-cardinality spectrum. General orbit- or subgroup-based descriptions do not, by themselves, give the complete explicit finite exceptional cases and cardinality counts stated here. No claim is made that the underlying symmetry methods are new.

## Limitations
This is restricted to pure equality, zero parameters, and ordered pairs; predicates, constants, higher powers, and arbitrary finitely supported (rather than equivariant) quotient relations can have different spectra. Exhaustive checker outputs are supplementary, not a substitute for the general proof. Ciobanu's motivating preprint was available by bibliographic record and abstract, but its complete text was not accessible for a decisive whole-document novelty comparison. An equivalent unindexed or unpublished classification remains possible. Independent audit has not been performed.

## References
1. G. Ciobanu, *Finite-Context Semantics in Finitely Supported Structures*, arXiv:2609.31917 (first public 2026-09-25).
2. G. Ciobanu, *Finite Dependence and Invariance Hierarchies for Finitely Supported Structures*, arXiv:2609.15879 (2026-09-14).
3. A. Healy and B. Klin, *Karp's NP-Complete Problems over First-Order Definable Structures*, FoSSaCS 2026, DOI:10.1007/978-3-032-22730-0_15.
4. M. Bojańczyk, *Nominal Monoids*, Theory of Computing Systems (2013), DOI:10.1007/s00224-013-9464-1.
