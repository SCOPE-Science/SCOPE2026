# Scientific review: two-level Van der Laan rigidity and growth

## Correctness — PASS

For \(0<u<v\), direct sorting of all five possible multiplicities of \(u\) in a four-block shows that only multiplicities two and three are possible and that they force \(v=2u\). For \(u=0\), the only allowed four-block multiplicities of zero are one and four; forbidden intermediate multiplicities prevent a mixed sequence from containing an all-zero window. The equality of successive one-zero window counts forces period four. These arguments cover every index, not a finite experiment. For the positive subshift, its explicit eight-state transition graph yields an exact generating function by a finite matrix inverse; the characteristic polynomial, seven-state primitivity, and Perron–Frobenius theorem yield the exponential growth claim. The supplied standard-library verifier independently rechecks the key finite algebra and sample words. The proof does not infer infinitude from finite enumeration.

## Originality — PASS, relative to inspected literature

D. Nacin's 2022-public paper defines the four-window property and analyzes increasing and selected permutation-increasing sequences. It lists the period-four \((1,1,1,2)\) example, also tabulated as OEIS A177704, but neither source claims the complete classification over arbitrary fixed two-valued alphabets, the forced dichotomy for zero-containing sequences, nor the exact generating function and entropy. OEIS A000931 discusses the Padovan recurrence and related individual word counts, not this seven-state language. Semantic mathematical-record searches for alternative names, exact counts and the growth polynomial identified no dominating statement. A bibliography that is not indexed by these searches may exist, and the transfer-matrix method itself is standard.

## Value — PASS

The two-valued case is the smallest nontrivial alphabet restriction for the four-term max/min equation. Resolving it reveals a sharp change from only five zero-containing possibilities to a positive-entropy, uncountable aperiodic family as soon as the lower symbol becomes positive; the larger symbol is then compelled to be exactly double. The exact rational word series and six-degree Perron polynomial quantify that qualitative contrast. The result responds to the observed failure of the original Padovan-merging conjecture by classifying a complete, nontrivial bounded stratum, rather than presenting one more periodic example. It does not settle more general alphabets.

## Closest sources and limits

D. Nacin, *Van der Laan Sequences and a Conjecture on Padovan Numbers*, Journal of Integer Sequences 26 (2023), Art. 23.1.2, publicly issued December 30, 2022: https://cs.uwaterloo.ca/journals/JIS/VOL26/Nacin/nacin5.pdf . OEIS A177704: https://oeis.org/A177704 . OEIS A000931: https://oeis.org/A000931 . A possible equivalent enumeration in older combinatorics literature remains a residual originality risk. Computational tests are corroboration, not a replacement for the unrestricted proof.

Self-review: passed. Independent audit: not yet performed.
