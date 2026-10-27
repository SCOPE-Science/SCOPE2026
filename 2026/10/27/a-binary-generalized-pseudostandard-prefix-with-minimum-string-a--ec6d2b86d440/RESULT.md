# A binary generalized pseudostandard prefix with minimum string-attractor size \(6\)

## Finding
Let \(R\) reverse a binary word, and let \(E\) reverse it and exchange its two letters. Starting with the empty word, repeatedly append the next letter of
\[\Delta=11011111\]
and apply the shortest \(R\)- or \(E\)-palindromic closure according to
\[\Theta=RRRERERE.\]
The eighth word \(w\) has length \(182\), and its minimum string-attractor size is exactly
\[\boxed{\gamma(w)=6}.\]
A six-position attractor, with positions indexed from zero, is
\[\Gamma=\{23,43,72,101,130,152\}.\]
Thus a universal upper bound of five on minimum string-attractor sizes of binary generalized pseudostandard prefixes is false. This statement does **not** claim that length \(182\) is the shortest example, that six is an upper bound for this class, or that its attractor sizes are unbounded.

## Assumptions and scope
A factor of \(w=w_0\cdots w_{n-1}\) is a nonempty contiguous substring. A set of indices \(\Gamma\subseteq\{0,\ldots,n-1\}\) is a *string attractor* if every distinct nonempty factor has an occurrence whose interval intersects \(\Gamma\). Write \(\gamma(w)\) for its minimum size.

For \(T\in\{R,E\}\), the \(T\)-closure of \(u\) is the shortest \(T\)-fixed word with prefix \(u\). If \(u=pv\), where \(v\) is the longest \(T\)-fixed suffix, then its closure is \(pvT(p)\). Starting with \(w_0=\varepsilon\), put \(w_i=(w_{i-1}\delta_i)^{\vartheta_i}\). Here \((\delta_1,\ldots,\delta_8)\) are the letters in \(\Delta\), and \((\vartheta_1,\ldots,\vartheta_8)\) the maps in \(\Theta\). The resulting lengths are
\[1,2,5,12,22,46,90,182.\]
Every finite directive admits an infinite extension, so this is a pseudopalindromic prefix of a binary generalized pseudostandard sequence under the standard definition.

## Proof
**Construction.** For each directive step, find the longest \(R\)- or \(E\)-fixed suffix and append the antimorphic image of the preceding prefix. Directly applying this rule produces the length list above; the last word is

`11011100010010001110111000100011101101110001001000111011011100010001110111000100100011101110001000111011011100010001110111000100100011101101110001001000111011100010001110110111000100`

**Upper bound.** Enumerate each interval \([i,j)\) with \(0\le i<j\le182\). Associate its binary factor with the predicate that the interval crosses at least one index in \(\Gamma\). For each distinct factor, take the disjunction of the predicates over all its occurrences. Every predicate is true; there are exactly \(12608\) distinct nonempty factors. The exact standalone verifier performs these interval checks, so \(\gamma(w)\le6\).

**Lower bound.** Consider the following twelve factors, in the indicated order, indexed \(0\) through \(11\):

```
0  000100011101101110001001
1  100100011101101110001000
2  111011100010010001110111
3  000100011101101110001000
4  111011100010010001110110
5  011011100010010001110111
6  01101110001000
7  11101110001001
8  1110111
9  0001000
10 10010001110111
11 00010001110110
```

For each position \(p\), define its *incidence mask*: bit \(j\) is set when position \(p\) lies in at least one occurrence of factor \(j\). Enumerating all occurrences of the twelve explicit factors gives exactly twelve inclusion-maximal masks, written from bit \(11\) to bit \(0\):

```
101000000001  000000000011  001001000010
000110000100  010010000100  010100000100
101000001000  100001001000  001001001000
000110010000  000000110000  010100100000
```

Every positional mask is contained bitwise in one of these twelve. A set of five positions therefore covers no more of the twelve factors than some five maximal masks. Exhaustively OR-ing every five-element selection of maximal masks requires only \(\binom{12}{5}=792\) tests; none yields the all-one 12-bit mask. This is a complete finite certificate, not sampling: a 5-position attractor would cover all twelve factors and force such an all-one OR. Hence \(\gamma(w)\ge6\). Together with the upper bound, \(\gamma(w)=6\).

## Verification
Run `python3 verify.py` using Python 3 standard-library modules only. The program independently constructs the eight closures, checks each resulting pseudopalindrome and its length, verifies that the six positions cover all \(12608\) distinct factors, enumerates every occurrence of the twelve obstruction factors, recomputes all maximal incidence masks, and checks all \(792\) five-mask unions. Its expected output is:

```
PSEUDOSTANDARD_ATTRACTOR_6_PASS length=182 distinct_factors=12608 obstructions=12 maximal_incidence=12 five_type_cases=792
```

The lower-bound exhaustion operates on the *entire* 12-factor incidence system: a five-position attractor would necessarily cover that system. The upper-bound exhaustion visits all intervals of the exact finite word. No numerical optimization package, solver status, or finite-to-infinite extrapolation is required.

## Relationship to prior work
Dvořáková and Hendrychová [1] define these closures, characterize attractors in special subclasses, and explicitly conjectured a universal size-four upper bound for binary generalized pseudostandard prefixes. Their conjectured bound has already been contradicted by a previously published length-36 example with minimum size five [2]. Neither the conjecture's first counterexample nor any established small-subclass results are claimed here. The present finite witness gives a strictly stronger lower bound of six on any putative uniform bound. Knowing an instance with size five does not logically imply that an instance of size six exists.

The source comparison encompasses the original 2023 preprint and full accessible 2024 paper, a 2023 thesis on the same objects, and the published size-five research record. The full contents of the latter record could not be inspected in this run; this is a specific residual originality risk. Searches for the six-point assertion and equivalent formulations disclosed no coverage but do not prove uniqueness or exhaustive novelty.

## Limitations
The assertion concerns one explicit finite word, not a classification, smallest-length theorem, infinite unboundedness claim, asymptotic law, or guarantee for all directives. The proof's computational part is finite exhaustive arithmetic with the disclosed 12-factor certificate; it is reproducible but has not undergone independent mathematical audit. A still-unlocated prior statement may cover the same witness or stronger proposition.

## References
[1] L. Dvořáková and V. Hendrychová, *String attractors of Rote sequences*, Discrete Mathematics & Theoretical Computer Science 26(3) (2024), doi:10.46298/dmtcs.12385, first arXiv version arXiv:2308.00850 dated 2023-08-01. See Definitions 1 and 3, and Section 7.

[2] *A length-\(36\) counterexample to the four-attractor conjecture for binary generalized pseudostandard words*, published mathematical research record 2026/10/4/SCOPE-a-length-36-counterexample-to-the-four-attractor-conjecture-for--23308eeec437 (summary accessible; complete content not inspected).

[3] V. Hendrychová, *String attractors*, Czech Technical University in Prague bachelor's thesis (2023), full text at https://hendrychova.xyz/bachelor-thesis.pdf, especially Sections 2–3 and conclusion.
