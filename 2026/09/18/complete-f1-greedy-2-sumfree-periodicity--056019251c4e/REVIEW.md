# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main theorem is reduced to two explicit residue statements for every even \(g\ge8\), with \(M=4g+3\) and the displayed set \(R_g\).

First, the ten componentwise sums of
\[
R_g=\{1,3\}\cup\{g,g+2,\ldots,2g-2\}\cup\{2g+5,2g+7,\ldots,3g+1\}\cup\{4g,4g+2\}
\]
are listed explicitly modulo \(M\), and none returns to \(R_g\). This establishes the needed restricted-sum exclusion for all terms lying in eventual residue classes. The proof separately treats the two exceptional selected prefix values \(2g\) and \(2g+3\); their translates of \(R_g\) avoid \(R_g\), their mutual sum has residue \(0\), and the only relevant equality producing \(2g\) is the allowed self-sum \(g+g\). Thus the distinction between strict 2-sumfreeness (distinct summands) and ordinary sumfreeness is handled rather than silently discarded.

Second, the identity
\[
(\mathbb Z/M\mathbb Z)\setminus R_g
=
\bigcup_{e\in\{1,g,2g,2g+3\}}(e+R_g)
\]
is expanded into four explicit arithmetic-progressions of residues. Once \(n\ge4g+7\), this gives a representation \(n=e+(n-e)\) with both terms selected, earlier, and distinct. The finite interval before this point is covered by explicit representations, so every omitted integer is genuinely forced out by the greedy rule. This proves equality of the proposed set and the greedy sequence, not merely eventual containment.

The minimality argument is also sound. The eventual residue set has trivial translational stabilizer: for \(g\ge10\) its circular gap \(g-1\) is uniquely largest, and for \(g=8\) the exceptional gap pattern has a unique gap of size \(5\). Hence the characteristic period is minimally \(4g+3\), containing exactly \(g+3\) selected residues. The final exceptional selected prefix term has a residue absent from \(R_g\), which prevents an earlier onset of periodicity. The odd family and \(g=2,4,6\) are covered by explicit descriptions.

The verification artifact directly regenerates the greedy sequence for every \(2\le g\le120\) through at least twelve eventual characteristic periods and checks the two residue identities for every even \(8\le g\le200\). These computations support but do not replace the general proof.

## Originality

**PASS, to the best of our knowledge.** Van Berkel and Bosma's arXiv:2609.18522v1 was inspected in detail. Its Conjecture 5 predicts all period lengths and Conjecture 9 all preperiod lengths. Definition 3 contains the special \(f=1\) period corrections, Definition 8 contains the special \(f=1\) preperiod formulas, and Example 6/10 displays their initial values. The paper explicitly describes these as conjectures.

The proved families in that paper do not cover this result. Theorem 12 handles \(g\le2f-1\), which yields no admissible \(g>1\) when \(f=1\). Theorem 14 treats the diagonal \(g=2f\), with \(S_{1,2}\) only noted separately. Theorems 16 and 17 are finite computational confirmations: both period and preperiod for \(f,d\le250\), and period for \(f,d\le500\). The present theorem proves all \(g\) for \(f=1\) and gives the exact residue description.

The earlier preprint arXiv:2609.16843 was checked through its abstract and through its relevant theorem as restated and proved again as Theorem 12 of arXiv:2609.18522. A separate full-text comparison of arXiv:2609.16843 was not inspected here. This is a residual source-access limitation, although the stated and restated coverage \(g\le2f-1\) does not contain the infinite \(f=1\) family.

External searches covered the exact family \(S_{1,g}\), "greedy strict 2-sumfree", "weakly sum-free" variants, the modulus \(4g+3\), the period \(g+3\), the \(f=1\) column, and the source arXiv identifier. No matching proof or stronger theorem was located. A related 2026 result of Orion Shtrezi proves a parametrized family for **3**-sumfree sequences, not this 2-sumfree family. No inaccessible paper was identified whose title or metadata specifically suggests the theorem proved here. Because the motivating preprints are only days old, unindexed contemporaneous work remains the principal originality risk.

## Value

**PASS.** This is an infinite theorem rather than another finite verification. It settles both quantitative periodicity conjectures for one complete parameter column \(f=1\), supplies an explicit modular description of every sequence in that column, proves minimal period and preperiod lengths, and yields exact densities. The even \(g\ge8\) family has a compact structural explanation: an eventual residue set modulo \(4g+3\) is simultaneously restricted-sum-free and covers every complementary residue after four fixed translates. This mechanism is potentially reusable for other conjectured 2-sumfree families.

## Sources checked

- Daan van Berkel and Wieb Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1: introduction; Definitions 3 and 8; Conjectures 5 and 9; Theorems 12, 14, 15, 16 and 17; computational-range discussion; references.
- Daan van Berkel and Wieb Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843: abstract and the relevant 2-sumfree theorem as restated in arXiv:2609.18522.
- Orion Shtrezi, *The greedy 3-sumfree sequence \(S_{1,g,g+1}\)*, arXiv:2606.17447: abstract and problem scope.
- Web searches for exact and synonymous formulations involving \(S_{1,g}\), eventual periodicity, residue descriptions, \(4g+3\), \(g+3\), and the \(f=1\) parameter family.
