# Review of the six-period symmetric-padding cover spectrum

## Correctness

**PASS.** The proof reduces all positive padding lengths and all positive center integers to the \(6\cdot111111\) residue states using the exact identity \(R_{m+6}-R_m=10^m111111\). The direct gcd condition and a prime-wise CRT root condition are algebraically equivalent. The standalone verifier exhaustively evaluates both on every state and checks the exact six counts. For the stronger ternary obstruction, the reduced modulus \(37037\) yields a short complete table of digit-\(3\)/digit-\(9\) candidates, with explicit digit-\(1\) noncover witnesses for both nonzero classes modulo \(3\). A finite computation is sufficient because the period reduction proves the state space is complete. Risk: a transcription or implementation error is possible, mitigated by the two independently expressed tests, complete source code, and a second reduced certificate.

## Originality

**PASS, subject to the stated literature risk.** Wu (2015) constructs individual six-period covers and reports an empirical pattern for \(4919\) centers below \(10^7\). The present result gives a complete modulo-\(111111\) classification for all center sizes, identifies the short ternary obstruction for every length class, and counts each class exactly. A090287 formulates the broader prime-search problem rather than this complete finite-cover enumeration. Grantham, Jarnicki, Rickert, and Wagon (2019) establish existence of one-sided appending covers; those do not imply the two-sided, fixed-six-period spectrum. Broader covering-system work does not automatically imply these precise congruence counts. An identical finite-table calculation in informal or unlocated literature cannot be excluded.

## Mathematical value

**PASS.** The modulus \(111111\) is not an arbitrary numerical slice: it is the repunit underlying the explicit period-six prime-cover pattern \(3,7,11,13,37\) used for the notable symmetric-padding examples. The theorem establishes an infinite-scope restriction on the proof method itself: no use of these primes alone, even with flexible dependence on digit and padding length, can produce a counterexample to the ternary condition in Wu's conjecture. The exact residue-spectrum counts also distinguish even-length behavior, including the two twenty-class exceptional strata. These are natural complete invariants of that cover, not sample-based statements about primes. The proof does not establish the broad conjecture, nor does it rule out longer prime covers.

## Closest prior statements and limitations

The closest primary comparison is Chai Wah Wu's 2015 article, Sections 2–4, in particular its modulus-six covering test and Conjecture 2. The source's bounded search is neither a modular classification nor a proof covering all integer centers. The OEIS entry records known covered centers but no complete congruence spectrum. The 2019 one-sided covering construction concerns a different arithmetic sequence. Residual risk remains for equivalent but unlocated results.

Self-review: passed. Independent audit: not yet performed.
