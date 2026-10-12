# Scientific review — sharp preperiods of A158690

## Correctness (PASS)

The formal substitution into an integral series gives a finite power spectrum modulo every \(2^e\). Odd bases obey Carmichael periodicity while even bases die at index \(e\). At index \(e-1\), only bases congruent to \(2\) modulo \(4\) remain; their coefficient parity is \(g_2+g_3=2+7\equiv1\pmod2\), via an exact periodic binomial parity identity. A gcd-of-periods argument excludes every alternative earlier-starting period, not just the Carmichael shift. All exponents and the exceptional modulus \(2\) have been checked. The exact finite certificate and independent initial-EGF comparison passed in `verification/verify.py`; finite tests are not being used as infinite proof.

## Originality (PASS, with residual risk)

The closest fully inspected source, Kallat, arXiv:2609.07238, Proposition 2.1 and Remark 2.2, proves eventual periodicity from \(n\ge e\) and calls the starting bound not necessarily sharp. This does not imply the lower-onset statement. Danesh's 2026-08-26 abstract covers universal eventual Carmichael periods but was not accessible for complete manuscript inspection: an implicit sharpness proof there remains a risk. OEIS A158690 gives the single example modulo \(16\), not all exponents. A previous exact least-period finding for high powers of two was found and is **not** claimed as original here; its valid claim supplies an eventual period but not a matching obstruction at \(e-1\). Searches against related forms, the research records, and the published literature found no stronger theorem establishing the universal sharp onset. Search absence alone is not a novelty proof.

## Mathematical value (PASS)

The least index of eventual periodicity is a natural, exact arithmetic invariant. The 2026 general theorem left the sharpness of its starting threshold open. The new identity proves a uniform optimal obstruction for infinitely many prime-power moduli, not a single computation or renaming of an existing period bound. It gives a complete preperiod classification, and the precise mechanism (a sparse parity sum governed by the second and third integral Stirling weights) is reusable in studying sharp onsets for related sequences.

## Residual scientific limits

The shortest eventual periods are not presented as new; odd prime powers and composite moduli are outside the claim. The 2026 Danesh full text could not be inspected. The novelty assessment remains fallible and is not independent certification.

Self-review: passed. Independent audit: not yet performed.
