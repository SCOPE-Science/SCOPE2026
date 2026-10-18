# Six-voter majority frames: exact coherence census and sharp integer certificates

## Finding
Fix the six-element labelled carrier \(W=\{1,2,3,4,5,6\}\). A *maximal standard social-decision frame* in the sense of Moss–Pedersen is the family \(\mathcal M\subseteq\mathcal P(W)\) that contains every set of size at least four, no set of size at most two, and exactly one set from each complementary pair of three-element sets. Call it *measurable* when positive finitely additive integer singleton weights \(w_i\) realize precisely the chosen sets as those having weight strictly greater than half the total weight.

**Theorem.** The \(2^{10}=1024\) labelled maximal standard frames fall into exactly thirteen isomorphism classes under permutations of voters. Exactly six classes, containing \(332\) labelled frames, are measurable; the other seven classes contain \(692\) labelled frames. Every nonmeasurable frame contains four distinct winning three-sets in which every voter occurs twice. Conversely, absence of such a balanced four-set witness implies measurability for these six-voter frames. Every measurable frame admits positive integer representing weights at most \(4\), and \(4\) is the smallest uniform upper bound on integer singleton weights.

These are statements about the specified six-voter maximal standard family only, not arbitrary six-voter voting games or larger electorates.

## Assumptions and scope
Index the ten three-sets containing voter \(1\), in this order:
\[
123,124,125,126,134,135,136,145,146,156.
\]
For a mask \(m\in\{0,\ldots,1023\}\), a one-bit at position \(j\) selects the corresponding displayed triple as winning; a zero-bit selects its complement. Thus each mask determines exactly one maximal standard frame. The bit at position zero is the least significant bit. For each frame, *balanced four-set witness* means four **distinct** winning triples such that each voter belongs to exactly two of the four. This is the six-voter case of the source's balanced-family concept.

The table is a complete set of orbit representatives. The tuple in the certificate column gives the six singleton weights (in voter order) for measurable representatives; a comma-separated sequence of four triples gives a balanced contradiction certificate for nonmeasurable representatives. Every entry is checked by the accompanying standalone program.

| Mask representative | Orbit size | Measurable | Explicit certificate |
|---:|---:|:---:|:---|
| 0 | 6 | yes | \((1,2,2,2,2,2)\) |
| 1 | 60 | yes | \((1,3,3,2,2,2)\) |
| 3 | 180 | yes | \((1,4,3,3,2,2)\) |
| 7 | 60 | yes | \((1,3,2,2,2,1)\) |
| 15 | 6 | yes | \((1,2,1,1,1,1)\) |
| 19 | 20 | yes | \((1,2,2,2,1,1)\) |
| 20 | 90 | no | 125, 134, 246, 356 |
| 21 | 180 | no | 125, 134, 246, 356 |
| 28 | 180 | no | 125, 134, 246, 356 |
| 29 | 90 | no | 125, 134, 246, 356 |
| 58 | 120 | no | 126, 134, 235, 456 |
| 126 | 20 | no | 125, 134, 236, 456 |
| 220 | 12 | no | 136, 145, 235, 246 |

## Proof
Each of the twenty three-subsets belongs to one of ten complementary pairs. Consequently there are exactly \(2^{10}\) masks. The symmetric group on six voters acts by permuting triples and reselecting the unique triple containing voter \(1\) in each complementary pair. Compute the orbit of mask \(m\) by examining all \(720\) permutations. Starting with the smallest unvisited mask, the orbit-generation algorithm returns exactly the thirteen representatives and orbit sizes in the table. These orbits are pairwise disjoint, their union contains every mask (explicitly tested for all \(1024\) masks), and their sizes sum to \(1024\). This is a finite exhaustive classification; the accompanying `CHECK.py` supplies the exact entire enumeration with no randomness, numerical optimization, or omitted cases.

For each of the first six representatives, the displayed weight tuple consists of strictly positive integers, and for **all sixty-four subsets** the strict half-total threshold agrees with the stipulated frame: sets of size at least four win, sets of size at most two lose, and exactly the ten chosen triples win. The checker verifies all these inequalities as exact integer comparisons. Relabelling the voters gives equally bounded certificates for all frames in the same orbit. The six orbit sizes sum to \(332\).

For each of the other seven representatives, the listed four triples are distinct and winning, and each of the six voters occurs exactly twice. If a strictly positive representing weight vector existed, each winning triple would have weight strictly greater than half the total \(T\). Summing the four inequalities would give a sum strictly greater than \(2T\); but counting each voter twice shows that the same sum equals \(2T\), a contradiction. Relabelling preserves this certificate. The remaining seven orbit sizes sum to \(692\). Since all thirteen orbits are covered, this proves equivalence between measurability and absence of balanced four-set witnesses **in this family**; it does not assume general four-coherence sufficiency.

Finally, mask \(3\) admits the displayed representation with maximum weight \(4\). Suppose it had a representing positive integer tuple with each weight at most \(3\). The winning triples \(123,124\) and the losing triples \(125,126,134\) imply, by comparing the indicated winning triple weights with the indicated losing triple weights, the strict inequalities
\[
w_2>w_3,\quad w_2>w_4,\quad w_3>w_5,w_6,\quad w_4>w_5,w_6.
\]
The only possibilities with singleton weights in \(\{1,2,3\}\) are \(w_2=3\), \(w_3=w_4=2\), and \(w_5=w_6=1\). But the losing triple \(125\) must have weight strictly less than its complement \(346\), requiring \(w_1+3+1<2+2+1\), or \(w_1<1\), contrary to positivity. Thus the upper bound \(4\) is sharp.

## Verification
Run `python3 CHECK.py` from this package. It constructs every complementary-pair orientation, exhausts all \(720\) voter permutations, verifies the thirteen disjoint orbit sizes and the \(332/692\) partition, checks every listed weight against every subset, and checks every balanced contradiction witness. A separate enumeration of all \(4^6\) positive integer tuples with weights in \(\{1,2,3,4\}\) confirms precisely \(332\) canonical six-voter masks arise, compared with only \(152\) under the bound \(3\). The theorem is proved by the finite exhaustive orbit certificates and the explicit strict inequalities, not extrapolated from a sample.

## Relationship to prior work
Moss and Pedersen, *The Measurable Majority* (2026), introduce these finite social-decision frames, give the general equivalence between coherence and measure representability, characterize maximal standard frames (Appendix B.11–B.17), give one nonmeasurable six-voter example (Example 2.4), and show equivalence of four-coherence and absence of balanced four-element families (Proposition B.21). Example B.18 states that a characterization of maximal standard measurable spaces is not known. The present theorem supplies a **complete six-voter, not general, classification**, finite obstruction equivalence, exact orbit census, and sharp bounded integer weights. Their separate 2026 note on nonfinite axiomatizability constructs unbounded incoherence indices; it does not imply this exact small-carrier census. Earlier voting-game literature on trade robustness and enumerations concerns broader or differently restricted classes; the six-voter intersection claimed here was not found stated in the inspected material.

## Limitations
This is one finite carrier size and one specified maximal standard subclass. It does not characterize all maximal standard measurable frames in all sizes, establish four-coherence sufficiency in larger sizes, or yield an arbitrary-size enumeration. The census is a complete finite computation supported by explicit witnesses and transparent executable exhaustive code, not an infinite classification. Full originality across unindexed or unavailable voting-game tabulations cannot be guaranteed; the closest general weighted-game tables may allow indirect extraction after further filtering. Independent expert validation has not been performed.

## References
1. L. S. Moss and A. P. Pedersen, *The Measurable Majority*, arXiv:2606.23853, public release 2026-06-22. https://arxiv.org/abs/2606.23853
2. L. S. Moss and A. P. Pedersen, *Measurable Majorities Are Not Finitely Axiomatizable*, arXiv:2606.25954, public release 2026-06-24. https://arxiv.org/abs/2606.25954
3. J. Freixas, M. Freixas and S. Kurz, *On the characterization of weighted simple games*, 2017, especially trade-robustness and weightedness comparisons. https://www.researchgate.net/publication/317768403_On_the_characterization_of_weighted_simple_games
4. X. Molinero, M. Serna and M. Taberner-Ortiz, *On Weights and Quotas for Weighted Majority Voting Games*, *Games* 12(4), 2021. https://www.mdpi.com/2073-4336/12/4/91
