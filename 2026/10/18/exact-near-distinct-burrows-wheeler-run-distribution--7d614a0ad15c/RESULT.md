# Exact near-distinct Burrows–Wheeler run distribution

## Finding

Let \(q\ge2\), let \(\Sigma_q=\{0,1,\ldots,q-1\}\) with its displayed ordering, and fix a symbol \(c\in\Sigma_q\). Consider all cyclic necklaces of length \(q+1\) in which \(c\) occurs twice and each other symbol once. Define the Burrows–Wheeler transform (BWT) without an endmarker, by sorting the cyclic rotations and taking the preceding character of each rotation. Let \(r\) denote the number of **linear** constant-letter runs in that BWT.

**Theorem.** Exactly \((q-1)!\) such necklaces have \(r=q\), and exactly \((q-1)!(q-2)/2\) have \(r=q+1\). There are \(q!/2\) necklaces in total. No other run count occurs, and all these necklaces are primitive. The counts are independent of the rank of the repeated symbol \(c\).

Equivalently, under the uniform measure on these necklaces,
\[
\Pr(r=q)=\frac2q,\qquad \Pr(r=q+1)=1-\frac2q.
\]
For \(q=2\) the latter probability is zero. If the repeated letter is not fixed, the respective total counts over all \(q\) choices of \(c\) are \(q!\) and \(q!(q-2)/2\).

**Exact structural test.** If the two copies of \(c\) are separated cyclically, the BWT has \(q\) runs exactly when their two immediate successor symbols are neighboring values in the ordered alphabet and neither equals \(c\). If the copies are cyclically adjacent, the BWT has \(q\) runs exactly when the letter immediately following the \(cc\) pair is an immediate neighbor of \(c\) in the alphabet. Otherwise the BWT has \(q+1\) runs.

## Assumptions and scope

A necklace identifies words modulo cyclic rotation, not reversal or letter relabeling. BWT rows are sorted lexicographically on the fixed alphabet, and BWT run count is the ordinary noncyclic run count of its last column. The symbol \(c\) is fixed for the first two enumerations; all symbols occur, and exactly one is duplicated. Every such necklace is primitive: if it were a proper power, all letter multiplicities would share a divisor exceeding one, contradicting the singleton multiplicities.

## Proof

Let \(\delta(c)\) be the degree of \(c\) in the path graph of the ordered alphabet (that is, \(1\) at an endpoint and \(2\) elsewhere for \(q\ge3\), while \(\delta(c)=1\) when \(q=2\)). For a necklace in the theorem, all BWT characters except \(c\) occur exactly once; hence its run count is \(q\) if the two \(c\)'s in the BWT are consecutive and \(q+1\) otherwise.

First suppose the two occurrences of \(c\) in the input necklace are not adjacent. Write the cyclic word as \(c A c B\), where \(A,B\) are nonempty and jointly permute the \(q-1\) other letters. Let \(x\) and \(y\) be the first characters of \(A\) and \(B\); these are distinct from one another and from \(c\). In the BWT matrix, a character \(c\) precedes exactly the rotations starting with \(x\) and \(y\). Those letters are unique, so their two rows are situated exactly at the alphabetic ranks of \(x\) and \(y\), with two consecutive rows for starting letter \(c\). These rows are adjacent if and only if \(x,y\) are consecutive in the **original** ordered alphabet; deleting \(c\) cannot turn a pair spanning its position into adjacent BWT rows. Of the \(q-1\) edges of the alphabet path, exactly \(q-1-\delta(c)\) have neither endpoint equal to \(c\).

For each unordered pair of designated successors \(\{x,y\}\), exactly \((q-2)!\) necklaces have these successors. To see this, choose the unique orientation with the segment after the first \(c\) beginning with a designated \(x\) and the segment after the second beginning with \(y\). The remaining \(q-3\) symbols form an arbitrary permutation, cut into an ordered tail following \(x\) and an ordered tail following \(y\). The number is \((q-3)!\sum_{j=0}^{q-3}1=(q-2)!\) for \(q\ge3\). The case \(q=2\) has no separated-copy necklaces. Thus the nonadjacent-copy contribution is \((q-1-\delta(c))(q-2)!\).

Now suppose the two copies are adjacent. The cyclic word has a unique representation \(ccP\), with \(P\) an arbitrary permutation of the remaining \(q-1\) symbols. Write \(x\) for the first character of \(P\). The two BWT occurrences of \(c\) occupy (i) the row starting with \(x\), and (ii) one of the two consecutive rows starting with \(c\). The two \(c\)-initial rotations start with \(cc\) and \(cx\), respectively. If \(x<c\), the row starting with \(cx\) comes first within that block and is preceded by \(c\); if \(x>c\), it comes last. Therefore those BWT occurrences are consecutive exactly when \(x\) is the immediate predecessor or successor of \(c\) in the alphabet. There are \(\delta(c)\) such choices, and the remaining \(q-2\) symbols can be ordered arbitrarily. This contributes \(\delta(c)(q-2)!\), including \(q=2\).

Adding the disjoint cases gives \((q-1-\delta(c)+\delta(c))(q-2)!=(q-1)!\) necklaces with exactly \(q\) BWT runs, independent of \(c\). Finally, the number of linear multiset permutations with the prescribed multiplicities is \((q+1)!/2\). Since every necklace is primitive it has exactly \(q+1\) rotations; there are \(q!/2\) necklaces. Subtracting \((q-1)!\) gives \((q-1)!(q-2)/2\) with \(q+1\) runs. Summing over the \(q\) disjoint repeated-symbol choices and dividing by \(q!/2\) proves the remaining assertions. \(\square\)

## Verification

The accompanying independent program `check.py` constructs the necklace set directly from multiset permutations for each alphabet size \(2\le q\le7\) and every duplicated letter. It computes the cyclic-rotation BWT, counts its ordinary linear runs, independently checks that the stable last-to-first permutation is a full cycle, and compares the observed counts to the theorem. Run it from this package directory using `python3 check.py`; `check-output.txt` is the captured output. The executable finite check does not establish the theorem for unbounded \(q\); the combinatorial proof above does.

## Relationship to prior work

Fici, Gabory, Romana and Sciortino establish existence and general lower bounds for totally unclustered BWT images over alphabets with at least three symbols (CPM 2026, Theorems 2 and 30). They do not enumerate the one-duplicated-letter content class. Kumallagov (arXiv:2606.01267, submitted 31 May 2026), Section 5.2 and Proposition 5.5, gives a general fixed-content count of **all** primitive-necklace BWT images and explicitly distinguishes this from enumerating those satisfying complete unclustering. The present result refines that baseline for the natural near-permutation content class \((2,1,\ldots,1)\), giving a closed exact count and structural criterion. Neither the unrestricted fixed-content formula nor the general nonbinary existence theorem implies the displayed unclustered proportion without the successor-adjacency argument.

## Limitations

This is an exact classification for the first nontrivial (one repeated symbol) fixed-content family, not a formula for arbitrary Parikh vectors. The conclusion uses the ordinary BWT without a sentinel, a fixed total order, and necklaces modulo rotation only. Possible equivalent earlier enumerations under different nomenclature cannot be excluded by finite literature searches alone. No independent scientific audit has been performed.

## References

1. G. Fici, E. Gabory, G. Romana, and M. Sciortino, *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, LIPIcs 369, Article 13, DOI: 10.4230/LIPIcs.CPM.2026.13. Open-access full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.13/LIPIcs.CPM.2026.13.html.
2. D. Kumallagov, *An extremal problem for completely unclustered Burrows-Wheeler images*, arXiv:2606.01267v1, 31 May 2026, https://arxiv.org/pdf/2606.01267.
