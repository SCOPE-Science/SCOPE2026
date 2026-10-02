# Independent mathematical audit — 2026-09-30

## Final claim

On a general smooth projective curve of genus 11, every semistable rank-3 vector bundle of degree 20 has at most 6 sections; equivalently the semistable coherent-system cell \(3,20,7\) is empty.

## Correctness — PASS

Assume semistable rank-3 degree-20 E has at least 7 sections. Paranjape-Ramanan with n=3,s=4 forces either a proper subbundle with excess sections or h0(det E)>=13. The latter is impossible because a degree-20 line bundle on genus 11 has h0<=11 by Riemann-Roch. A line witness is impossible: h0>=2 requires degree at least 7 on a general genus-11 curve, exceeding the semistable line-subbundle cap 6. Thus a saturated rank-2 witness N has h0(N)>=3 and degree 10..13. If N were unstable, its destabilizing line and quotient both have degree at most 6 and hence at most one section, contradiction. So N is semistable. Applying Paranjape-Ramanan to N gives h0(N)<=3 for degree 10..12 and <=4 at degree 13. The quotient line Q has degrees 10,9,8,7 with Brill-Noether section caps 3,2,2,2 respectively. Therefore h0(E)<=6 in every case, contradiction. The numerical rho=-28 and gamma=4 calculations are consistent.

## Originality — PASS (best of knowledge)

The exact (3,20,7) emptiness statement was not found in the checked higher-rank Brill-Noether/Mercat literature. A primary genus-11 source constructs/controls nearby rank-3 degree-20 loci with six sections, while the audited seven-section exclusion requires the additional Paranjape-Ramanan/semistability argument given here.

### Equivalent formulations

Searches: Resultary semantic search: genus 11 rank 3 degree 20 seven sections semistable Mercat coherent system; Targeted search for B(3,20,7) genus 11.

Evidence: Resultary returned this record as the exact-topic hit. No checked source stated emptiness of the semistable coherent-system cell (3,20,7).

Reasoning: The final claim is equivalent to emptiness of the semistable Brill-Noether/coherent-system locus with rank 3, degree 20, at least 7 sections on a general genus-11 curve.

### Broader coverage

Searches: Lange-Newstead rank-3 genus-11 literature / Paranjape-Ramanan lemma; Farkas-Ortega arXiv:1102.0276; Bakker-Farkas arXiv:1511.03253.

Evidence: The inspected genus-11 rank-3 source gives nearby degree-20 six-section results and general Clifford-index bounds, not this seven-section emptiness. Farkas-Ortega concerns K3-section constructions and higher-rank BN phenomena; Bakker-Farkas is rank 2 and does not imply the rank-3 cell.

Reasoning: Known rank-2 Mercat results and nearby six-section existence do not mechanically settle the seven-section rank-3 cell.

### Exact database or table

Searches: Resultary exact-topic search; Targeted web/literature search for rank 3 degree 20 h0=7 genus 11.

Evidence: No independent exact theorem/table for the cell was located.

Reasoning: This is best-of-knowledge evidence rather than a proof of novelty.

### Claim versus prior implication

Searches: Paranjape-Ramanan lemma as quoted in the genus-11 rank-3 literature; Classical line-bundle Brill-Noether thresholds.

Evidence: These standard inputs do imply the result only after the multi-case semistability argument: a PR witness must be rank 2, has degree 10..13, must itself be semistable, and its section cap combined with the quotient line cap gives at most 6 sections. No checked source packaged that implication for this cell.

Reasoning: The result is a nontrivial but short deduction from standard inputs, not a mere one-line substitution.

### Source inspections

- **On an example of Mukai.** Material read: Paranjape-Ramanan lemma and the genus-11 rank-3 theorem giving nearby degree-20 six-section information. Assessment: the inspected source does not state the seven-section emptiness result.
- **Higher rank Brill-Noether theory on sections of K3 surfaces** (arXiv:1102.0276). Material read: abstract and result scope. Assessment: K3-section constructions do not cover the general-curve \(3,20,7\) emptiness claim.

Checked sources: Paranjape-Ramanan lemma in the inspected genus-11 rank-3 literature; Farkas-Ortega arXiv:1102.0276; Bakker-Farkas arXiv:1511.03253; Resultary published-record search.

Residual risks: A specialized coherent-systems paper could contain the same one-cell deduction under different notation; none was identified in the targeted searches.

## Scientific value — PASS

The seven-section cell is the immediate section-count boundary above a known natural degree-20 rank-3 six-section locus on genus-11 curves and directly tests the rank-3 Mercat inequality at gamma=4 versus Clifford index 5. A clean emptiness theorem at that boundary is a motivated exact fact likely useful in higher-rank Brill-Noether/coherent-system work.

## Limitations

- The argument decides only the \(3,20,7\) cell.
- Classical line-bundle Brill-Noether bounds and the Paranjape-Ramanan lemma are cited inputs.
- Originality is best-of-knowledge, with the residual literature risk above.

## Conclusion

The unchanged final claim passes correctness, originality, and scientific-value review.
