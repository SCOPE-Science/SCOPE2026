# Rotation-wise subsequence universality of two-block binary necklaces

## Finding
A cyclic word is **rotation-wise \(k\)-subsequence universal** if, for each binary target word of length \(k\), some (possibly target-dependent) rotation contains that target as a scattered subsequence. Let \(\rho(W)\) be its largest such \(k\); this is different from requiring a *single* rotation to contain every target.

**Theorem.** For all integers \(a,b,r\ge1\), the binary necklace represented by \(W=(0^a1^b)^r\) has
\[
\rho(W)=\min\{ra,rb,2r+1\}.
\]
Consequently, if \(m=\min(a,b)\), the index is \(r\) for \(m=1\), \(2r\) for \(m=2\), and \(2r+1\) for \(m\ge3\). All statements concern subsequences within one traversal of the finite cyclic word, not arbitrarily many revolutions.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A rotation is a cyclic shift of the finite word. A scattered subsequence selects strictly increasing positions from *one* chosen rotation, with no index reused and no second traversal. The empty target is always present; the theorem has \(a,b,r\ge1\) so both letters occur. Cyclic run changes count the boundaries between different neighboring symbols, including the last-to-first boundary.

## Proof
**Upper bounds.** Every length-\(ra+1\) all-zero target and length-\(rb+1\) all-one target is absent, because \(W\) has exactly \(ra\) zeroes and \(rb\) ones. Moreover \(W\) has exactly \(2r\) cyclic symbol changes. Selecting positions in cyclic order cannot increase the number of cyclic symbol changes: every change among selected letters must cross a distinct change in the underlying cyclic word. The alternating target of even length \(2r+2\) has \(2r+2\) cyclic symbol changes, hence cannot occur. This proves \(\rho(W)\le\min\{ra,rb,2r+1\}\).

**A reduction.** Put \(m=\min(a,b)\). Deleting surplus letters separately inside each block proves that \(V_m=(0^m1^m)^r\) is a cyclic subsequence of \(W\). Cyclic subsequence containment is transitive (compose increasing selections around the same circle), so proving \(\rho(V_m)\ge\min\{rm,2r+1\}\) suffices. It remains to treat \(m=1,2,3\): if \(m\ge3\), \(V_3\) is in turn a cyclic subsequence of \(V_m\).

**A greedy displacement certificate.** Let \(A_m=(0^m1^m)^\infty\) be the right-infinite periodic word with \(m\in\{1,2,3\}\). Start at a prescribed occurrence of the first letter of a nonempty target \(p=p_1\cdots p_k\) and greedily choose each subsequent letter at its earliest position strictly after the preceding choice. If all choices lie in fewer than \(2mr\) consecutive positions, the target is a subsequence of the corresponding rotation of \(V_m\).

For \(m=1\), start at a position carrying \(p_1\). Each subsequent match moves at most two positions, so the final displacement is at most \(2(k-1)\). With \(k=r\), this is \(2r-2<2r\).

For \(m=2\), start at the **first** symbol of a run carrying \(p_1\). Record the offset \(j\in\{0,1\}\) of the last selected position within its homogeneous run and let \(h(0)=0\), \(h(1)=-1\). The greedy next-match transition satisfies
\[
\delta\le2+h(j')-h(j),
\]
where \(\delta\) is the forward displacement and \(j'\) the new offset. Indeed, a repeated letter moves by \(1\) from offset \(0\), or by \(3\) from offset \(1\) (then the offset resets to \(0\)); a changed letter moves by \(2-j\) and resets the offset to \(0\). These four cases satisfy the displayed inequality. Telescoping over \(k-1\) matches, and using \(h(j_{\rm last})\le h(0)=0\), gives displacement at most \(2(k-1)\). For \(k=2r\), this is \(4r-2<4r\).

For \(m=3\), first start at offset \(0\) of a run carrying \(p_1\), and set \(h(0)=h(1)=0\), \(h(2)=-1\). The greedy transitions satisfy
\[
\delta\le3+h(j')-h(j),\qquad j,j'\in\{0,1,2\}.
\]
A repeated letter advances one position when \(j<2\), and four positions with offset reset to zero when \(j=2\); a changed letter advances \(3-j\) positions and resets to zero. Direct substitution verifies the inequality in all six cases. Starting from offset zero, **equality at every transition** is possible only when every successive target letter differs from the preceding one: the first repeated-letter transition from offset zero is strictly below the inequality, while changed-letter transitions from offset zero have equality. Thus if \(p\) is not alternating, the final displacement is an integer at most \(3(k-1)-1\). For \(k=2r+1\), that is \(6r-1<6r\).

If \(p\) is alternating, instead start at offset \(1\) of a run carrying its first letter. Its first changed-letter transition advances only \(2\) positions; all remaining changed-letter transitions from offset zero advance \(3\) positions. The final displacement is \(2+3(k-2)=3(k-1)-1=6r-1<6r\) when \(k=2r+1\). The case \(k=1\) is immediate. This completes all three cases, hence proves the lower bound and the theorem. \(\square\)

## Verification
The standalone `check.py` implements the definition directly: for each target it tests all rotations with a conventional greedy subsequence matcher. The script tested 144 parameter triples \(1\le a,b\le6\), \(1\le r\le4\) having formula value at most nine, checked all 14,270 targets of the predicted maximal length, and explicitly found a missing target at the next length in each case. It independently verifies that the cyclic word `000111` contains every binary length-three target across its rotations although no single rotation is length-three subsequence universal. Execute `python3 check.py`; the expected output is in `check_output.txt`. Computations corroborate the proof but are not its basis.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka (2020) define *circular \(k\)-universality* by **existence of one conjugate which is itself \(k\)-universal**. Fleischmann, Germann and Nowotka (2021) retain this definition while studying repeated words and arch remainders. Their quantifiers are \(\exists\) rotation \(\forall\) targets. Here the rotation may depend on the target, reversing these quantifiers to \(\forall\) targets \(\exists\) rotation; the two conditions differ already for `000111` at length three. The present formula does not follow merely from a bound on the earlier index. Adamson et al. (2025) study existence of universal words in regular languages, and Fazekas, Huang and Mercaş (2026) study existential/universal indices of Parikh-matrix languages; neither inspected work gives this three-parameter, target-dependent rotation formula. Related general automata algorithms may decide its finite instances without proving the displayed identity.

## Limitations
The result concerns binary periodic necklaces with exactly two homogeneous blocks per period. It is not a characterization for arbitrary binary necklaces, and it does not determine the different, single-rotation circular universality index. The finite checker does not verify arbitrary parameters. The claim is a mathematical derivation accompanied by finite corroboration; no independent scientific audit has been performed. An equivalent formula might occur under different terminology in unindexed literature.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (first posted 2020-03-10), particularly Definition 4 and Section 4.
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063 (first posted 2021-04-19), especially Definition 2 and Theorems 9–10.
3. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, *k-Universality of Regular Languages Revisited*, arXiv:2503.18611 (first posted 2025-03-24).
4. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first posted 2026-10-05).
