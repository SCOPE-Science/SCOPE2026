# Complete four-element semilattice spectrum of diagonal relations

## Finding
For a finite meet-semilattice \(Y\), let \(D(Y)\) be the number of reflexive relations \(R\subseteq Y\times Y\) closed under coordinatewise meet, and let \(C(Y)\) be the number of congruences. The coefficient introduced by Barber and Ruškuc is \(\chi(Y)=C(Y)/D(Y)\). **Every four-element meet-semilattice is isomorphic to exactly one of five types**, and their complete values are as follows. Each type contains a least element \(0\), and the description concerns the remaining three elements:

| Nonzero order type | \(D(Y)\) | \(C(Y)\) | \(\chi(Y)\) |
|---|---:|---:|---:|
| Three-element antichain (flat star) | 322 | 8 | \(4/161\) |
| Exactly one comparable pair, third incomparable | 400 | 8 | \(1/50\) |
| One nonzero element below two incomparable nonzero elements | 625 | 8 | \(8/625\) |
| Two incomparable nonzero elements below a greatest element (Boolean diamond) | 306 | 7 | \(7/306\) |
| Three-element chain | 576 | 8 | \(1/72\) |

These five rational numbers are **pairwise distinct**. Thus among four-element meet-semilattices, the single numerical invariant \(\chi(Y)\) already determines the isomorphism type. The Boolean diamond is the unique type with seven congruences. Its diagonal-relation count \(306\) is smaller than the counts of all other four-element types, yet its coefficient lies strictly between the values for the flat star and the one-comparability type.

More strongly, put \(F_Y(t)=\sum_{R\in\operatorname{Diag}(Y)}t^{|R|-4}\). In the order of the five types displayed above, their complete coefficient vectors, starting with degree zero, are

```
flat-star: (1,6,15,26,39,48,52,48,39,26,15,6,1)
one-comparability: (1,6,17,32,48,62,68,62,48,32,17,6,1)
common-lower: (1,6,19,44,77,106,119,106,77,44,19,6,1)
Boolean-diamond: (1,4,10,20,31,44,52,52,45,28,14,4,1)
chain: (1,6,19,42,71,96,106,96,71,42,19,6,1)
```

Each sum is the corresponding \(D(Y)\). In particular, the Boolean-diamond distribution is not palindromic, unlike the chain and common-lower examples.

## Assumptions and scope
There is **only one semigroup operation**, binary meet. A diagonal subsemigroup is a relation containing all four diagonal pairs and closed under coordinatewise meet. A congruence is a compatible equivalence relation; no join or complement operation is required even in the Boolean-diamond case. The five nonzero poset structures distinguish the isomorphism types without needing arbitrary element labels. No statement is made about semilattices of larger orders.

## Proof
**Complete isomorphism classification.** Every finite meet-semilattice has a least element, namely the meet of all its elements. After removing that element, one obtains a three-element partially ordered set. Up to isomorphism, the three-element posets are precisely: an antichain; a single comparable pair and an isolated point; one point below two incomparable points; two incomparable points below one point; and a three-element chain. Adjoining a fresh least element to each of these gives a meet-semilattice: every two incomparable nonzero elements either have a common nonzero greatest lower bound in the common-lower case or meet at zero. Hence these five are exactly all four-element meet-semilattices.

**Finite exhaustive counting certificate.** Label the least element by \(0\) and the other elements by \(1,2,3\). There are exactly six possible directed comparabilities among the nonzero elements, so every candidate partial order on the labeled set occurs among the \(2^6=64\) subsets of comparabilities. Reject nonantisymmetric or nontransitive candidates and candidates without unique pairwise meets; identify duplicates by the six permutations of nonzero labels. This yields exactly the five multiplication tables displayed in the independent checker.

For each of the five meet tables, a reflexive relation is determined by twelve optional off-diagonal ordered pairs. Thus there are exactly \(2^{12}=4096\) possible reflexive relations, **all of which** are considered by the finite enumeration certificate. For every such relation, test all ordered pairs of its elements for meet closure. For the compatible ones, test all reversed pairs and all composable pairs for symmetry and transitivity, respectively, to count congruences. Retain also a histogram of the number of off-diagonal pairs. This exhaustive finite calculation gives the five integer pairs and the five coefficient vectors stated above.

To cross-check the main count independently, start from each of the same \(4096\) subsets, adjoin the diagonal and repeatedly add all coordinatewise meets until stable. Every generated set is a diagonal subsemigroup, and every diagonal subsemigroup appears by starting from itself. The distinct generated closures are compared as sets with the relations accepted by the first direct closure test; the two resulting collections are **exactly identical** for every type. The checker also verifies that the five integer pairs, after sorting, are \((306,7),(322,8),(400,8),(576,8),(625,8)\). Direct rational comparison shows that \(7/306,8/322,8/400,8/576,8/625\) are pairwise distinct. This is a finite exhaustive proof: it claims no conclusion about unenumerated larger semilattices.

## Verification
Run `python3 verify.py` using only the Python standard library. The program constructs every possible labeled partial order on the three nonzero elements, checks meet existence, classifies by all six relabelings, exhaustively checks every reflexive relation for all five types, compares direct acceptance with independently generated meet closures, computes the complete size polynomials, and checks all five DSC coefficients are distinct. Actual execution ended with `VERIFY_OK` and the five exact profiles given above. The searches for larger types are not exhaustive and no larger-size claim is made.

## Relationship to prior work
Barber and Ruškuc [1] introduce the numerical coefficient and explicitly ask what values it can have for finite semilattices; their formulas cover Rees matrix semigroups and their Clifford theorem bounds coefficients using a semilattice's coefficient without computing the latter. Their earlier work [2] supplies a qualitative criterion, not this small-order spectrum. Existing classifications for **chains** and **flat semilattices** determine the chain and flat-star rows individually; those two rows are included for *completeness* and are not claimed anew. The new finite-order contribution is the full five-type spectrum and the exact counts for the three remaining nonflat, nonchain types, especially the Boolean diamond.

Targeted searches for complete four-element semilattice DSC tables, exact Boolean-diamond diagonal-relation counts, and compatible-relation aliases found no identical full classification. Earlier universal-algebra counting literature may contain some or all of these numbers under other terminology; absolute historical priority is unconfirmed.

## Limitations
The theorem is an exhaustive result for semilattices of **exactly four** elements, not an all-dimensions formula. It does not establish asymptotics, monotonicity, or a full spectrum across all finite semilattices. It depends on the correct and complete execution of the provided finite enumeration; all loops and tested conditions are included in source form. The numbers alone do not settle the broader semilattice question. Independent mathematical audit has not been performed.

## References
[1] C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286, first public 19 February 2026, version 2 (7 October 2026), Section 4. https://arxiv.org/html/2602.17286v2

[2] C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, Bull. Aust. Math. Soc. 113 (2026), 123–134; arXiv:2504.02428, public since 3 April 2025. https://doi.org/10.1017/S0004972725100166
