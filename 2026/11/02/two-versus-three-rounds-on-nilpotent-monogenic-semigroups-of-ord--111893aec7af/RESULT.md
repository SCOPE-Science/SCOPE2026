# Two versus three rounds on nilpotent monogenic semigroups of orders 16 and 20

## Finding

Let \(N_t=\{a,a^2,\ldots,a^{t-1},0=a^t\}\), where the product is \(a^ia^j=a^{\min(i+j,t)}\). Interpret \(N_t\) in the finite *relational* signature consisting of equality, named zero \(0\), and ternary multiplication \(M(u,v,w)\) meaning \(uv=w\). The two semigroups \(N_{16}\) and \(N_{20}\) are indistinguishable by all first-order sentences of quantifier rank at most two, but are distinguished by one of rank three:

\[
N_{16}\equiv_2N_{20}\quad\text{and}\quad N_{16}\not\equiv_3N_{20}.
\]

In particular, their different nilpotency indices \(16\) and \(20\) are invisible at depth two in this relational language. The least distinguishing quantifier rank for this pair is exactly three.

## Assumptions and scope

All first-order quantifiers range over semigroup elements, and atomic multiplication statements are \(M(u,v,w)\), *not* functional product terms. Zero is a named constant. For each \(t\), represent \(0\) by exponent \(t\) and use \(u\cdot v=\min(t,u+v)\) for exponent representatives \(u,v\in\{1,\dots,t\}\). The result is about these two specific semigroups; no periodicity or classification across all orders is claimed. Both are finite, commutative, monogenic, and nilpotent, with nilpotency index equal to their order.

## Proof

**Two-round equivalence.** For two selected exponents \(x,y\) and the named zero \(t\), their complete atomic diagram is determined by the following eight Boolean quantities, in this order:

\[
(x=t),\ (y=t),\ (x=y),\ (2x\ge t),\ (2y\ge t),\ (x+y\ge t),\ (\min(2x,t)=y),\ (\min(2y,t)=x).
\]

Indeed these determine every equality and every ternary multiplication atomic statement over \(\{x,y,t\}\): the possible products are \(x^2\), \(y^2\), \(xy\), and products with zero, and the only possible named targets are \(x,y,t\). In particular, if \(x,y<t\), their product cannot equal either factor; if a factor is zero, its product is zero. This proves the reduction without assuming a computational heuristic.

For fixed first move \(x\), let \(P_t(x)\) be the **set** of eight-bit diagrams obtained as the second move \(y\) varies through \(\{1,\ldots,t\}\). Encoding a Boolean vector by the integer \(\sum_{j=0}^{7}2^jb_j\), direct arithmetic gives exactly the following twelve distinct profiles. Each row gives all first moves sharing that profile in each semigroup, followed by all eight-bit codes realized by second moves.

| Class | First moves in \(N_{16}\) | First moves in \(N_{20}\) | Eight-bit codes in the shared profile |
|---|---|---|---|
| 1 | 1, 3 | 1, 3 | 0, 4, 16, 48, 50, 64 |
| 2 | 2 | 2, 4 | 0, 4, 16, 48, 50, 64, 128 |
| 3 | 4 | 6 | 0, 4, 16, 48, 50, 80, 128 |
| 4 | 5 | 5 | 0, 4, 16, 48, 50, 80 |
| 5 | 6 | 8 | 0, 4, 16, 48, 50, 112, 128 |
| 6 | 7 | 7, 9 | 0, 4, 16, 48, 50, 112 |
| 7 | 8 | 10 | 8, 56, 60, 122, 136 |
| 8 | 9, 11, 13 | 11, 13, 15, 17 | 8, 40, 56, 60, 122 |
| 9 | 10 | 12 | 8, 40, 56, 60, 122, 136 |
| 10 | 12, 14 | 14, 16, 18 | 8, 40, 56, 60, 122, 168 |
| 11 | 15 | 19 | 40, 56, 60, 122 |
| 12 | 16 | 20 | 41, 185, 255 |

Every possible first move in either structure appears in exactly one row, and each row has a nonempty counterpart. After matched first moves, every second move has a reply with exactly the same atomic diagram, because the sets of codes are identical. The symmetric response holds as well. Therefore Duplicator wins the two-round Ehrenfeucht–Fraïssé game and \(N_{16}\equiv_2 N_{20}\).

**Three-round separation.** The following sentence has quantifier rank three:

\[
\exists x\,\exists y\,\exists z\;[M(x,x,y)\land M(x,y,z)\land M(z,z,0)\land\neg M(y,z,0)].
\]

For a nonzero \(x=a^i\), its conjuncts force \(y=a^{2i}\), \(z=a^{3i}\), \(a^{6i}=0\), and \(a^{5i}\ne0\). Hence the sentence is true in \(N_t\) exactly if an integer \(i\ge1\) satisfies \(5i<t\le6i\). For \(t=16\), \(i=3\) works; the explicit witness is \((x,y,z)=(a^3,a^6,a^9)\). For \(t=20\), \(i\le3\) is forced by \(5i<20\), whereas \(20\le6i\) forces \(i\ge4\), a contradiction. Thus it separates the two structures at rank three, proving the least distinguishing rank is exactly three.

## Verification

The accompanying `verify_ef2.py` computes all reduced second-move codes for all first moves in both structures, independently computes complete equality and all \(27\) ternary atomic multiplication tests, checks that reduced profiles and complete atomic profiles induce identical pairwise identifications across both structures, and prints the twelve-row certificate above. It also enumerates all triples satisfying the displayed sentence.

The independent `verify_game.py` constructs the complete recursive first-order quantifier-rank signatures directly from equality and relational multiplication atoms for ranks one, two, and three. It confirms equivalence at rank two and inequivalence at rank three without relying on the eight-bit reduction. The recorded outputs are `verify_ef2.txt` and `verify_game.txt`. Reproduce with `python3 verify_ef2.py` and `python3 verify_game.py` from this directory; no nonstandard dependencies are required.

## Relationship to prior work

Distler's 2010 thesis, particularly §1.2 and §2.1 (including Lemma 2.1.5), places finite monogenic nilpotent semigroups within the classification of nilpotent semigroups and identifies their maximal nilpotency index. It does not supply the present comparison in the relational multiplication language. Gomaa's 2007 dissertation studies finite-group descriptive complexity and quantifier depth, rather than nilpotent monogenic semigroups. Searches for cyclic nilsemigroup, monogenic semigroup, two-round Ehrenfeucht–Fraïssé equivalence, and the order pair 16/20 did not reveal a published implication of this exact rank gap. This is evidence from the specified searches, not an exhaustive priority certification.

## Limitations

The distinction depends on the relational multiplication signature with named zero. In the usual functional multiplication language, longer product terms are atomic and this rank calculation need not apply. No assertion is made that the pair is lexicographically minimal among *all* semigroup orders or that the family has a certain eventual periodicity. The result is a self-review and has not undergone independent validation. Unindexed older literature may contain equivalent observations.

## References

1. A. Distler, *Classification and Enumeration of Finite Semigroups*, PhD thesis, University of St Andrews, repository date 2010-06-23; §1.2 and §2.1, especially Lemma 2.1.5. https://research-repository.st-andrews.ac.uk/handle/10023/945
2. W. Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, public repository date 2007-07-06. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
