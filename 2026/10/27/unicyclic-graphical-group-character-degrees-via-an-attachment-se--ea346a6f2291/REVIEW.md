# Research review

## Correctness — PASS
The proof reduces every supported matrix to a forest or a remaining alternating cycle. The forest rank is twice maximum matching size. The root-essentiality test is expressed by a one-vertex matching-number decrement, equivalent to the bridge functional vanishing on the forest radical. Only the surviving even cycle has a cancellable Pfaffian, and its single nonzero multiplicative equation has exactly \((q-1)^{|S|-1}\) solutions per eligible support. In odd characteristic the class-two Kirillov orbit size gives the stated character multiplicities. The standard-library verifier independently enumerates matrices and recovers the predicted rank counts in 29 configurations over small prime fields. Finite enumeration is corroboration, not infinite proof.

## Originality — PASS, with residual risks
The closest antecedent is Li–Yu (2014), *The skew-rank of oriented graphs*, especially their unweighted-orientation unicyclic rank criteria. Gong–Xu (2012) treats weighted characteristic coefficients broadly, but complete primary full text was unavailable; implicit coverage remains possible. The indexed tree and bare-cycle graphical-group formulas, and the separate earlier double-cone transformation, do not cover arbitrary tree attachments and their support-dependent even-cycle correction. Rossmann (2022) asks for the character-degree enumerator. Searches and implication comparisons are recorded in `AUDIT.json`; failure to locate equivalent work is not mathematical proof of novelty.

## Value — PASS
This completes a motivated infinite family of class-two graphical-group character enumerations and gives a testable all-field alternating-rank polynomial. The distinguishing mathematical fact is when attached trees allow, rather than destroy, the residual even-cycle Pfaffian cancellation. Every rank stratum and every odd-characteristic irreducible character degree is counted, not merely a generic rank or a finite example.

## Remaining limitations
The formula is for connected unicyclic graphs and can have exponential running time as a literal subset sum. Its character conclusion is for odd characteristic. Complete access to Gong–Xu (2012), exhaustive historical priority, and independent verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
