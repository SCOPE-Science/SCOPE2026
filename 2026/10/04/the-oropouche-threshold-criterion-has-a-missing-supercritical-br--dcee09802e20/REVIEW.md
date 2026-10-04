# Review of “The Oropouche threshold criterion has a missing supercritical branch”

## Correctness
PASS. The threshold statement follows from the exact quadratic satisfied by \(q=\mathcal R_0^2\): for \(S>2\), the larger root is automatically greater than one; for \(S\le2\), the larger root exceeds one exactly when \(f(1)=1-S+P<0\). The exact witness is generated from the source's Eq. (2), respects the stated probability and equal-recovery assumptions, gives \(R_{FA}=2\), \(R_{FH}=2/3\), \(R_{CH}=8/3\), and makes all four endemic-equilibrium residuals zero at \(1/2\). The checker reproduces these identities with exact rational arithmetic.

## Originality
PASS. The closest semantic database result concerns a different two-patch SEIR reproduction-number bracketing problem and does not imply this algebraic correction. Searches using the exact source title, DOI, cycle labels, threshold expression, witness values, and correction/erratum aliases found no published correction or equivalent statement. The motivating article's relevant qualitative-analysis and Appendix sections were inspected directly; its Appendix explicitly equates \(R_{FA}+R_{CH}+R_{FH}>R_{CH}R_{FA}+1\) with \(\mathcal R_0>1\), which is the statement corrected here. The general next-generation theorem supports the interpretation of \(\mathcal R_0\) but does not contain the source-specific missing-branch result.

## Value
PASS. The error is not a cosmetic sign typo: it removes an entire open supercritical region \(S>2\) with \(P\ge S-1\) from the Appendix's threshold logic. The exact endemic witness proves that this region is not algebraically empty and can occur under the paper's own transmission parametrization. Correctly separating the two branches matters whenever individual sylvatic and urban transmission cycles are both strong, precisely the regime in which a multi-cycle threshold decomposition is meant to guide interpretation.

## Closest literature and limitations
The closest primary source is Peterson et al. (2026), DOI 10.1007/s00285-026-02422-1, whose displayed \(\mathcal R_0\) formula is retained and whose Appendix equivalence is corrected. Van den Driessche and Watmough (2002), DOI 10.1016/S0025-5564(02)00108-6, gives the general disease-free threshold framework but not this source-specific algebra. The result does not prove uniqueness or global stability of endemic equilibria, and the witness is a mathematically admissible parameter set rather than a calibrated Amazonas fit.

Same-model review: passed. Independent audit: not yet performed.
