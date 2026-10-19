# Scientific review: finite-window phase recovery in the random dimer shift

## Correctness — PASS

The specified stationary dimer law supplies uniform cylinder weights on the two alignment-compatibility sets. For even length their sizes are \(2^m\) and \(2^{m+1}\), with likelihoods \(2^{-m}\) and \(2^{-m-1}\); for odd length both sizes are \(2^{m+1}\), each with likelihood \(2^{-m-1}\). Their intersection comprises exactly the two alternating words, which proves the support and optimal Bayes-risk formulas by direct summation. The Shannon formulas follow by the entropy chain rule for the latent fair phase. Stationarity then gives the predictive-information limit. Exact enumeration independently checks all words through length 12. Boundary cases, including the single-symbol word, are covered; finite testing is not the proof.

## Originality — PASS, subject to priority uncertainty

Baake and van Enter, arXiv:1011.1628 (2010), define this process and prove its hidden period-two eigenfunction via infinite observations. Their complete accessible paper was examined, especially Sections 3–6. It does not report a finite-window Bayes-error law, exact Shannon-block expressions, or the \(3/2\)-bit predictive-information value. Semantic research-record searches for the model name, phase decoding, word entropy, and equivalent likelihood-overlap language did not identify those formulas. Nearby results about entropy bounds or unrelated finite-block models do not imply this evaluated dimer law without the model-specific overlap calculation. Aaronson–Gilat–Keane–de Valk (1989) concerns general one-dependent processes; only its abstract was accessible. Priority is not independently certified.

## Mathematical value — PASS

The source paper demonstrates a physically motivated discrepancy between diffraction and dynamical spectrum; finite data cannot exhibit its infinite-sequence eigenfunction directly. The sharp optimal error law supplies the exact sample-information cost of extracting that hidden eigenphase. The complete block entropy sequence and \(3/2\)-bit excess-entropy limit quantify the global predictive structure even though the symbol entropy rate is only \(1/2\) bit per site. The two parity-specific corrections distinguish phases and boundaries and cannot be recovered merely from the entropy rate or the two-point diffraction. The result is a self-contained evaluated invariant, not a generic entropy-chain-rule identity.

## Evidence and limits

Primary full text: Baake and van Enter, DOI: 10.1007/s10955-011-0163-5, pages 91–99. Source classification: symbolic dynamics (MSC 37B10). The exact enumerator checks all \(2^n\) words for lengths 1–12; it does not certify claims beyond those lengths. Historical-priority uncertainties include unindexed computational-mechanics calculations and inaccessible full text of general one-dependent-process research. The result is restricted to the unbiased stationary model and does not cover noisy or unequal-phase cases.

Self-review: passed. Independent audit: not yet performed.
