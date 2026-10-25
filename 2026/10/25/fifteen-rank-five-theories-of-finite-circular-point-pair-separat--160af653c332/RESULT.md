# Fifteen rank-five theories of finite circular point-pair separation structures

## Finding
For every positive integer \(n\), let \(\mathcal S_n\) have universe \(\{0,\ldots,n-1\}\) and the sole non-equality relation \(S\) of arity four, where \(S(a,b,c,d)\) holds exactly when all four points are distinct and the two pairs \(\{a,c\}\) and \(\{b,d\}\) alternate in clockwise cyclic order. Neither a starting point nor an orientation is named. Then, for all \(m,n\ge1\),
\[
\mathcal S_m\equiv_5\mathcal S_n\quad\Longleftrightarrow\quad \min(m,15)=\min(n,15).
\]
Thus the entire family has precisely fifteen equivalence classes for agreement on first-order sentences of quantifier rank at most five, represented by \(\mathcal S_1,\ldots,\mathcal S_{15}\). The uniform representative-size bound fifteen is optimal. In particular the 15- and 16-point structures agree at rank five, whereas the 14- and 15-point structures do not.

## Assumptions and scope
Only finite nonempty circles of distinct points with the indicated *quaternary pair-separation relation* are considered. A relation tuple with repeated entries is false. Quantifier rank is the maximum nesting depth of first-order quantifiers. The result concerns full first-order logic (unbounded variable count), not bounded-variable or counting logic, and does not claim a classification of arbitrary quaternary structures, circles with additional named vertices, or larger quantifier ranks.

## Proof
**Exact finite-type recursion.** For a tuple \(\bar a\) of \(k\le5\) *pairwise distinct* previously selected elements, let \(A(\bar a)\) be its complete atomic \(S\)-diagram (all ordered quartets of the selected entries). Define recursively
\[
T_5(\bar a)=A(\bar a),\qquad
T_k(\bar a)=\bigl(A(\bar a),\{T_{k+1}(\bar a,x):x\notin\bar a\}\bigr)
\quad(0\le k<5).
\]
The displayed set is a set of *exact types*, not a list of witnesses or a multiset. The standard one-point back-and-forth induction shows that two tuples of the same length have matching \(T_k\) precisely when Duplicator wins the remaining \(5-k\) moves: each new move has an extension of exactly the same type in the other structure. Selecting an old point merely forces the same old point as a response and introduces no new test. Hence equality of \(T_0\) is exactly rank-five elementary equivalence.

**Uniform reduction.** Given \(k\) distinct marked positions around a circle, call the number of unmarked points in each of the \(k\) successive cyclic gaps its gap length. With four marked positions and one move left, the possible atomic diagrams of a fifth point depend only on *which of the four gaps are nonempty*. Indeed, inside a fixed gap the five-element circular order, hence every atomic quartet, is unchanged. With three marked positions and two moves left, placing a fourth splits one of the three gaps of length \(g\) into nonnegative lengths \(u,v\) with \(u+v=g-1\). The complete list of possible pairs \((\mathbf1_{u>0},\mathbf1_{v>0})\) depends only on \(\min(g,3)\); the other gaps contribute only their positivity. Consequently the exact remaining two-round type of an ordered triple is determined by its three cyclic gap lengths, each truncated at three, together with the ordering of marked labels.

With two marked positions and three moves left, placement of a third point splits either of the two gaps. Every truncated pair \((\min(u,3),\min(v,3))\) obtainable from a gap of length \(g\) depends only on \(\min(g,7)\): for \(g\ge7\) all saturated and nonsaturated split patterns are available, while for smaller \(g\) they are directly enumerated. The other original gap is unchanged. Therefore the exact three-round type of any ordered pair is determined by its two gap lengths truncated at seven. This is a sufficiency assertion, not an assertion that all distinct truncated vectors yield distinct types.

**Finite boundary certificate.** The attached `separation_rank5_verify.py` implements the above finite-type recurrence directly from alternating quartets, reducing tuples only by actual dihedral automorphisms. It exhaustively determines \(T_0\) for each size 1 through 16; the first fifteen types are distinct, while sizes 15 and 16 have identical types. It also directly evaluates the critical two-marked-point identity
\[
T_2(6,7)=T_2(7,7),
\]
where \(T_2(u,v)\) denotes the exact remaining three-round type of two marked positions with cyclic gap lengths \(u,v\). This finite identity follows by enumerating the at most sixteen possible clipped gap values and applying the exact extension recursion, not by extrapolation from large circles. The program additionally checks the seven-cap sufficiency on 121 concrete gap pairs as a redundant computation.

**All larger sizes.** Fix any first selected point of a circle of size \(n\ge15\). On selecting a distinct second point, the two gaps total \(n-2\). If their smaller length is at most six, the larger is at least seven, and the pair type equals one of \(T_2(i,7)\) for \(0\le i\le6\). If both lengths are at least seven, seven-cap sufficiency and the verified identity show that this pair has type \(T_2(7,7)=T_2(6,7)\). Conversely, all seven types \(T_2(i,7)\), \(0\le i\le6\), occur for **every** \(n\ge15\), by choosing two points with gap lengths \(i,n-2-i\). Thus the *set of pair extension types* from any singly marked point is identical for every size \(n\ge15\). The one-point type, and consequently the empty-tuple rank-five type, is identical across all these sizes. The finite boundary certificate proves that no two of the first fifteen sizes agree. This completes both directions and sharpness.

## Verification
Run `python3 separation_rank5_verify.py` using Python 3 and its standard library. The recorded run printed `VERIFY_OK classes=15 sharp_minimum_representative=15` and also confirmed the key \((6,7)/(7,7)\) identity. Type identifiers in its output are computational labels assigned on first encounter and have no invariant mathematical significance beyond their equalities. The infinite reduction is proved by the gap-splitting lemmas above; no bounded finite scan is used as an infinite proof.

## Relationship to prior work
Kulpeshov and Macpherson (2005) develop model theory of circularly ordered structures with the oriented ternary cyclic-order relation, rather than these finite quaternary separation reducts and their exact rank-five theories. Brown and Hoshino (2007, Theorem 4.9) give sharp quantifier-rank equivalence thresholds for *undirected cycle graphs* in the binary adjacency signature; their formula gives a rank-five eventual threshold of nineteen, not fifteen. Those statements do not imply the present separation-language classification: graph adjacency and cyclic pair alternation have different atomic diagrams and there is no quantifier-rank-preserving change of signature in either direction furnished by those results. Published results on cyclic-order extendability and self-duality concern distinct invariants. Searches of the indexed claims examined did not identify an equivalent or dominating classification; this negative search is not a proof of uniqueness.

## Limitations
The result is specific to quantifier rank five and the exact quaternary signature. Full text of one potentially relevant 2005 article was not accessible for comparison; its available abstract concerns infinite circular-order minimality rather than this finite invariant. Unindexed and inaccessible historical literature may contain equivalent results. No independent scientific audit has been performed.

## References
1. B. Sh. Kulpeshov and H. D. Macpherson, *Minimality conditions on circularly ordered structures*, Mathematical Logic Quarterly **51** (2005), 377–399, DOI: 10.1002/malq.200410040 (first published 8 June 2005).
2. J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, especially Theorem 4.9; openly accessible at https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf.
3. P. Alles, J. Nešetřil and S. Poljak, *Extendability, Dimensions, and Diagrams of Cyclic Orders*, SIAM Journal on Discrete Mathematics, DOI: 10.1137/0404041.
