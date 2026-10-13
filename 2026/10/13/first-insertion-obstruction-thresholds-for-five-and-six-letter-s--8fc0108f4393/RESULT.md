# First insertion-obstruction thresholds for five- and six-letter square-free words

## Finding

Fix an alphabet \(\mathcal A_q\) of \(q\ge2\) symbols. Let \(b(q)\) be the minimum length of a square-free word \(w\) over \(\mathcal A_q\) possessing an insertion gap \(j\) such that insertion of **every** letter of \(\mathcal A_q\) at gap \(j\) creates a square. Then

\[
(b(2),b(3),b(4),b(5),b(6))=(2,4,6,10,14).
\]

In particular, the first such word on five symbols has length \(10\), and on six symbols has length \(14\). At their respective first obstructed lengths, the numbers of words modulo permutation of the alphabet are \(1,2,1,2,1\) for \(q=2,3,4,5,6\), respectively. For \(q=3\) and \(q=5\), each pair consists of reversals up to relabeling. Thus there is exactly **one** shortest obstructed word up to both relabeling and reversal for every \(2\le q\le6\).

A general construction additionally supplies the bound

\[
b(q)\le 2^{\lfloor q/2\rfloor}+2^{\lceil q/2\rceil}-2\quad(q\ge2).
\]

This bound is attained for the five alphabet sizes above. The construction uses a known structural property of Zimin words; the new finite exactness and uniqueness statements are concentrated on the five- and six-letter cases.

## Assumptions and scope

A square is a nonempty consecutive factor of the form \(XX\). A word is square-free if it contains no square. For a word \(w=w_0\cdots w_{n-1}\), insertion at gap \(j\in\{0,\ldots,n\}\) means the word \(w_0\cdots w_{j-1}xw_j\cdots w_{n-1}\), where \(x\in\mathcal A_q\). A gap is **blocked** if each of the \(q\) insertions introduces some square, with the square allowed to depend on \(x\). A word is nonbifurcate precisely when at least one gap is blocked. Permuting alphabet symbols and reversing the word preserve this property.

Alphabet size is fixed, so words may use fewer than \(q\) symbols; such words cannot have a blocked gap, because inserting a previously unused symbol cannot create a square. The finite classification covers every square-free word, not merely words of a prescribed special form. No assertion about arbitrarily long bifurcate trees or completely unextendable words is made.

## Proof

**1. General construction.** Define \(Z_1=0\) and, recursively, \(Z_{r+1}=Z_r\,r\,Z_r\) for \(r\ge1\), with symbol \(r\) new. The length of \(Z_r\) is \(2^r-1\). Inductively each \(Z_r\) is square-free: a square spanning the unique central symbol \(r-1\) would contain that symbol once, whereas each half of a square contains identical occurrences; a square not spanning the center would occur in one of the square-free copies of \(Z_{r-1}\). Also, for every symbol \(x\) occurring in \(Z_r\), the word \(Z_rx\) has a square: if \(x=r-1\), it ends in \((Z_{r-1}(r-1))^2\); for smaller \(x\), its suffix \(Z_{r-1}x\) contains a square by induction. Because \(Z_r\) is a palindrome, likewise \(xZ_r\) contains a square.

Partition the alphabet into two nonempty disjoint sets of sizes \(a\) and \(q-a\). Concatenate copies of \(Z_a\) and \(Z_{q-a}\) using those disjoint alphabets. The concatenation is square-free: a square crossing the unique alphabet transition would have one half crossing that transition and the other not, or its halves would lie in disjoint alphabets, both impossible. Its joining gap is blocked, because inserting a letter from the left (respectively right) alphabet makes a square in the left (respectively right) block. Taking the most balanced partition gives the announced bound.

**2. Exhaustive lower bounds and uniqueness.** Two words differing by a permutation of alphabet symbols have the same blocked-gap status. Every word has a unique *restricted-growth representative*: rename symbols to \(0,1,\ldots\) in order of their first appearance. Generate these representatives recursively, starting from \(0\) and appending either an earlier symbol or the next unseen symbol, with fewer than \(q\) distinct symbols. Any newly created square must end at the appended position, so checking all suffixes \(XX\) of the new word is a complete incremental square-freeness test.

For an existing square-free word, inserting a symbol at gap \(j\) can only create squares containing the new position. For each possible square half-length \(h\), and each start \(s\) of a length-\(2h\) factor containing \(j\), compare all paired locations except the inserted one. If the pairs disagree, that placement cannot yield a square. Otherwise the placement forces exactly the alphabet symbol at the partner position \(j+h\) or \(j-h\). Taking the union of all such forced symbols (including \(h=1\), which forbids the adjacent letters) gives **exactly** the set of symbols that produce squares. A gap is blocked if and only if this union equals the full alphabet. Every start \(s\) and half-length \(h\) permitted by the finite factor are checked.

The accompanying `verify.cpp` implements this enumeration, verifies the total restricted-growth square-free representatives and blocked representatives at the first obstruction length, and asserts that no preceding length has any blocked representative. The results are:

| Alphabet size \(q\) | First blocked length \(b(q)\) | Canonical square-free representatives at length \(b(q)\) | Canonical blocked representatives |
| ---: | ---: | ---: | ---: |
| 2 | 2 | 1 | 1 |
| 3 | 4 | 3 | 2 |
| 4 | 6 | 29 | 1 |
| 5 | 10 | 6,936 | 2 |
| 6 | 14 | 6,480,694 | 1 |

At the thresholds the canonical blocked words are, respectively: `01`; `0102`, `0121`; `010232`; `0102010343`, `0102324232`; `01020103435343`. The two canonical words at each two-element row are mutual reversals after first-occurrence renaming; the unique representative at each one-element row maps to itself by reversal and renaming. This proves the claimed uniqueness up to both symmetries.

The gap indices of witnesses are specified in `witnesses.json` and independently checked by `check_witnesses.py`. In particular, the six-letter witness `01020103435343` is blocked at the gap after its first seven symbols. The matching Zimin construction proves the upper bounds, and the exhaustive absence below each threshold proves minimality.

## Verification

Compile and run the self-contained C++17 checker with `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. It enumerates all restricted-growth square-free words through each claimed threshold and checks the complete forbidden-letter masks at all gaps, including the two end gaps. It prints `VERIFY_OK first_nonbifurcate_lengths_2_through_6` only after checking all five thresholds, terminal counts, blocked counts, and canonical witnesses. The independent Python witness checker uses direct substring comparisons for all single-symbol insertions: `python3 check_witnesses.py`.

The exhaustive finite census is part of the proof and must be executed to independently reproduce its numerical lower bounds. The stated theorem does not follow from a bounded random search or from witness verification alone.

## Relationship to prior work

Dębski, Grytczuk, and Pawlik (2022) introduce the term *bifurcate*, prove that steady square-free words are bifurcate, and study complete bifurcate trees. Their Theorem 7 provides a four-letter obstruction of length six through the word `abacdc`; consequently the quaternary obstruction and the idea of separating alphabet blocks are **not claimed as original**. Grytczuk, Kordulewski, and Pawlik (2021), §3.2, explicitly analyze the nonextendable external positions of Zimin words, so the underlying one-sided blocking mechanism is also known. The newly established assertions here are exact least lengths and complete shortest-obstruction classifications at alphabet sizes five and six.

A later result of Hng and Rathke (2026) excludes *extremal* square-free words for alphabets of size at least five. Extremality forbids every insertion at **every** gap, whereas failure of bifurcation requires only **one** blocked gap, and therefore the later result neither contradicts nor implies the present construction. The earlier results on an infinite special family of bifurcate words also do not imply that *every* shorter word is bifurcate.

## Limitations

Only lengths and uniqueness for \(2\le q\le6\) are decided; for larger alphabets the Zimin bound is an upper bound, not a proved minimum. The enumeration and certificate do not determine extremal square-free words, complete bifurcate tree existence, or counts of longer blocked words. No independent external audit or definitive priority search of unpublished/unindexed work has been performed.

## References

1. M. Dębski, J. Grytczuk, and B. Pawlik, *Extensions and reductions of square-free words*, arXiv:2209.08507v1, first public September 18, 2022. https://arxiv.org/html/2209.08507v1 . Sections 1, 2.3, 2.4; especially Theorem 7.
2. J. Grytczuk, H. Kordulewski, and B. Pawlik, *Square-free extensions of words*, arXiv:2104.04841v3, first public April 10, 2021. https://arxiv.org/html/2104.04841v3 . Sections 2–3; especially §3.2.
3. E. K. Hng and S. Rathke, *No extremal square-free words over alphabets of size at least 5*, arXiv:2608.10591v1, first public August 11, 2026. https://arxiv.org/abs/2608.10591 . Used for a comparison of the distinct quantifiers, not as the eligibility date.
