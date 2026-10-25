# Twelve rank-four theories of complete triple systems with matching defects

## Finding
Let \(a,b\) be nonnegative integers with \(a+b\ge3\). Construct the \(3\)-uniform hypergraph \(H_{a,b}\) on \(a+2b\) vertices by partitioning its vertices into \(a\) singleton parts and \(b\) doubleton parts, and declaring a triple to be an edge exactly when its vertices lie in three distinct parts. Equivalently, start from a complete triple system and delete every triple containing a pair from a fixed matching of size \(b\), leaving \(a\) unmatched vertices. The logical language has equality and only a symmetric irreflexive ternary edge predicate; no parts, pairs, or constants are named.

The entire infinite family has **exactly twelve first-order quantifier-rank-four equivalence classes**. To specify them, put \(A=\min(a,4)\), \(B=\min(b,4)\). Each following set lists precisely the pairs \((A,B)\) in one class:

| Class | Capped parameter pairs \((A,B)\) | Smallest representative \((a,b)\) | Smallest vertex count |
|---:|---|---|---:|
| 1 | \((3,0)\) | \((3,0)\) | 3 |
| 2 | \((2,1)\) | \((2,1)\) | 4 |
| 3 | \((4,0)\) | \((4,0)\) | 4 |
| 4 | \((1,2)\) | \((1,2)\) | 5 |
| 5 | \((3,1),(4,1)\) | \((3,1)\) | 5 |
| 6 | \((0,3)\) | \((0,3)\) | 6 |
| 7 | \((2,2)\) | \((2,2)\) | 6 |
| 8 | \((1,3),(1,4)\) | \((1,3)\) | 7 |
| 9 | \((3,2),(4,2)\) | \((3,2)\) | 7 |
| 10 | \((0,4)\) | \((0,4)\) | 8 |
| 11 | \((2,3),(2,4)\) | \((2,3)\) | 8 |
| 12 | \((3,3),(3,4),(4,3),(4,4)\) | \((3,3)\) | 9 |

For all allowed \((a,b),(a',b')\), \(H_{a,b}\equiv_4 H_{a',b'}\) **if and only if** the two capped parameter pairs occur in the same row. Every family member therefore has a rank-four-equivalent representative with at most **nine vertices**. No smaller uniform bound is possible within the family, since \(H_{3,3}\) requires nine vertices in its class.

## Assumptions and scope
The number of parts is \(a+b\ge3\), every part has exactly one or two vertices, and every part is unlabelled in the logical language. Repetitions in an edge tuple are forbidden, and edge triples are unordered despite their use as the interpretation of a symmetric ternary relation. Rank refers to first-order nesting depth, with unrestricted variable reuse and Boolean operations; no counting quantifiers are allowed. The result does not classify general multipartite triple systems with arbitrary part sizes.

## Proof
**Reduction to nineteen finite cases.** In a four-round Ehrenfeucht--Fraïssé game, Duplicator can always preserve equality, part-membership equality, and whether each represented part has size one or two between \(H_{a,b}\) and \(H_{\min(a,4),\min(b,4)}\). When Spoiler chooses an already represented vertex or the unchosen partner of an already represented doubleton part, Duplicator copies that pattern. When Spoiler enters an entirely new part of size \(s\in\{1,2\}\), Duplicator selects a new part of the same size. There are at most four newly represented parts of either size, so identical counts below four and counts at least four suffice. Since edges are precisely triples drawn from three distinct parts, the resulting selected-tuple map is a partial isomorphism. This proves rank-four equivalence between each member and its capped member. The allowed capped pairs number \(25-6=19\).

**Exact finite classification.** On a finite structure \(G\) and a chosen vertex tuple \(\bar x\), define \(T_0(G,\bar x)\) to be its complete atomic equality and edge truth diagram (including negated atoms). Recursively define
\[
T_{r+1}(G,\bar x)=\left\{T_r(G,\bar x y):y\in G\right\}.
\]
Two structures have the same rank-\(r\) theory iff their empty-tuple \(T_r\) values agree. The forward direction follows by induction on formulas; the converse follows since the finite set of possible extension types admits a characteristic existential formula at each stage, or equivalently by the \(r\)-round Ehrenfeucht--Fraïssé theorem. The recursive construction uses *all* vertices and all atomic diagrams and therefore is an exhaustive finite proof, not a sample or heuristic.

The accompanying `verify.py` implements this construction in two distinct ways. Its first implementation visits all vertices on every step. The second visits one representative of each orbit of the tuple-fixing automorphism group: old selected vertices, a fresh partner in a represented doubleton part, and a new vertex in any as-yet-unrepresented singleton or doubleton part. Such vertices are mutually conjugate within each category because the automorphism group freely permutes equal-size unused parts. Thus the second implementation computes the same type exactly without omitting distinct extensions. Both calculations give the *same partition* of the nineteen capped pairs into the twelve rows printed above. Since these are exact characteristic types, every pair in distinct rows has a distinguishing sentence of quantifier rank at most four, and every pair within one row is rank-four equivalent. The reduction proves the claimed infinite classification.

**Sharpness.** For each class the smallest \(a+2b\) appears in the table; the maximum of these minima is nine, attained by class 12. Hence nine is the least common upper bound for sizes of representatives of all twelve classes within this family.

## Verification
Run `python3 verify.py` with Python 3 standard library only. It recomputes the full 19-case type partition at rank four by direct vertex recursion and by orbit-reduced recursion, asserts agreement, checks the printed twelve groups, and checks all minimal representative sizes and the sharp bound. Its supplied `verify.log` records `VERIFY_OK`. The mathematical truncation lemma, rather than tests beyond the cap, proves the reduction for arbitrary parameters. No external proof assistant or independent audit is claimed.

## Relationship to prior work
Pikhurko, Veith, and Verbitsky (2003), especially §9 on uniform hypergraphs, study general quantifier-rank distinguishability and similarity-based hypergraph reductions. Their bounds and structural principles do not directly give the present exact twelve-class rank-four partition for matching-defect triple systems. Kiani and Saeedi Madani (2014 preprint; 2015 journal publication) develop the general complete-multipartite-hypergraph framework, but their theorems concern edge ideals, Cohen--Macaulay conditions, and related algebraic properties, not first-order rank-four equivalence. A previously recorded exact rank-four classification of **three-part** complete tripartite hypergraphs concerns unrestricted part sizes but exactly three parts; it overlaps only in the three-part subfamily, and does not imply a classification allowing arbitrarily many singleton and doubleton parts. The research-index searches described in the associated review did not reveal a covering exact classification.

## Limitations
This is an exact classification only for the matching-defect family, not for arbitrary multipartite triple systems or arbitrary 3-uniform hypergraphs. The finite computation is a proof of the nineteen reduced cases only together with the separately proved parameter-uniform truncation lemma. The literature search does not establish absolute priority against inaccessible or unindexed historical material. The mathematical evidence has received self-review only, not independent scientific audit.

## References
1. O. Pikhurko, H. Veith, O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041v1, first public 2003-11-04, https://arxiv.org/abs/math/0311041; especially §9.
2. D. Kiani, S. Saeedi Madani, *The Edge Ideals of Complete Multipartite Hypergraphs*, arXiv:1402.2469v1, first public 2014-02-11, https://arxiv.org/abs/1402.2469; especially §§2--3.
