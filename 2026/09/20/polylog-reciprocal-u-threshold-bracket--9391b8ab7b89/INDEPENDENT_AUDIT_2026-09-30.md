# Independent Audit — 2026-09-30

**Record:** `2026/09/20/polylog-reciprocal-u-threshold-bracket--9391b8ab7b89`  
**Title:** A quantitative bracket for the polylogarithmic reciprocal-smoothing threshold  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `acaad43f49c25d64f9983bde5c5162167007a4e2`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The upper bound is valid: Bieberbach plus the area theorem and Cauchy–Schwarz give the exact zero-free majorant 2^(1-s)+sqrt(T(s)), and the separate U-expression square sum is <1 throughout the claimed range. The root is unique by monotonicity and independently evaluates to 1.413519504254766... . The lower obstruction is also sound: for any sigma<1 choose m with alpha=2/m and sigma+alpha<1; the starlike f_m=z/(1-z^m)^(2/m) has reciprocal coefficients c_k<0 with -c_k asymptotic to C k^(-1-alpha), so the radial U-series has positive terms asymptotic to k^(-sigma-alpha) and diverges unless analyticity already fails by a zero of the reciprocal.
- **Originality — PASS:** The upper endpoint s_* is shared with the companion SCOPE record `polylogarithmic-reciprocal-univalence-threshold--41ca59617c30`, whose broader contribution is the general reciprocal-multiplier Hilbert criterion. This record is complementary rather than redundant because it supplies the independent sharp obstruction tau_U>=1 via explicit starlike root transforms and packages the first two-sided bracket 1<=tau_U<=s_*. The 2013 Ali–Obradović–Ponnusamy paper gives only the universal sufficient bound sigma>=3/2 and poses the smallest-parameter problem.
- **Scientific value — PASS:** A nontrivial lower obstruction materially changes the status of the open threshold problem: it rules out every sigma<1 and, together with the improved upper bound, localizes the universal tail exponent to a finite explicit interval. The extremal family is simple and reusable.

## Independent findings
- Independent numerical evaluation gives s_*=1.413519504254766..., within the filed certified bracket.
- The root-transform family is starlike because z f_m'/f_m=(1+z^m)/(1-z^m) has positive real part.
- The positive radial coefficients in the U-expression force failure for every sigma<1 when sigma+2/m<1.
- The shared upper bound with the companion record is not counted twice as a distinct novelty; the lower obstruction is this record’s independent contribution.

## Independent checks
- Recomputed the root of the exact Hilbert-tail equation at high precision.
- Checked convergence and strictness of the zero-free and U-class estimates for |z|<1.
- Re-derived the generalized-binomial coefficient asymptotic for the root-transform reciprocal.
- Read the 2013 source statement of Corollary 1.7 and its terminal smallest-parameter question.

## Literature evidence
- https://doi.org/10.1080/17476933.2011.599116 — Ali, Obradović and Ponnusamy (2013), primary paper; Corollary 1.7 gives sigma>=3/2 and the paper ends with the smallest-parameter problem.
- https://doi.org/10.1007/s40840-015-0115-3 — Ali and Alarifi (2015), related U-radius work; no matching polylogarithmic tail lower obstruction located.

## Limitations
- The exact universal U-tail exponent remains open between 1 and 1.413519504... .
- The record addresses the monotone universal U-tail interpretation, not every literal reading of the source’s terse U-or-S question.
- Equivalent older multiplier-language formulations remain a residual originality risk.

The assigned source tree remained unchanged from the source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `acaad43f49c25d64f9983bde5c5162167007a4e2` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
