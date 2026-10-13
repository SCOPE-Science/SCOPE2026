# Self-review

## Correctness
**PASS.** The exact Euler–Lotka equation reduces to \(\lambda^2=a\lambda+b\), so exact growth is strictly increasing in the late-age contribution. The generation-time shortcut is \((a+b)\log(a+b)/(a+2b)\). A one-unit late-fertility decrease is equivalent to an exact integer-power inequality. Exhaustion through initial \(R_0=6\) proves no failure for \(R_0\le5\) and a unique first failure at \((5,1)\to(5,2)\), where \(6^{54}>7^{49}\). The packaged verifier returns `VERIFY_OK`.

Risk: the integer cutoff is tied to two reproductive ages and unit increments; other discretizations have different cutoffs.

## Originality
**PASS.** The checked demographic literature establishes that reproductive amount and timing jointly determine growth and that \(\log(R_0)/T\) is an approximation with a restricted accuracy regime. The existing related finite-age result in the checked local record concerns exact Euler–Lotka extrema at fixed \(R_0\) and fixed mean age; it neither studies the shortcut nor changes reproductive amount and timing together. Targeted database and web searches did not locate the monotonicity failure, its derivative criterion, or the exact first positive-integer witness.

Risk: a numerical example with similar values could occur in unindexed teaching material.

## Value
**PASS.** A growth-rate approximation should ideally preserve the direction of an unambiguously beneficial demographic perturbation. Here adding late fertility always raises exact Euler–Lotka growth, yet the standard generation-time shortcut can move downward. Identifying the first exact witness and the general derivative mechanism gives a concrete diagnostic for when the shortcut should not be used for comparative sensitivity analysis.

Self-review: passed. Independent audit: not yet performed.
