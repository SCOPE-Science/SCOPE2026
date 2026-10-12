# Review

## Correctness
PASS. For any computational-basis code, conditioning on a survivor set \(S\) reduces decoding to choosing one message from each distinct projected binary word, so the conditional average success is exactly \(N_S(C)/M\). The explicit codes for \(n\le3\) have \(N_S(C)=\min\{M,2^{|S|}\}\) for every coordinate subset. The primary source supplies the matching fixed-pattern dimension converse for arbitrary quantum codewords and the same patternwise feedback optimum, so equality follows for every message-independent erasure-pattern distribution. Its Theorem 6.1 supplies the strict \(n=4\), \(M=4\) gap for \(0<p<1\), completing the minimality conclusion.

## Originality
PASS. The primary paper states the four-use strict gap and several sufficient attainability regimes, but it does not state all-message attainability for every qubit blocklength \(n\le3\) or the resulting minimal-blocklength theorem. In particular, its displayed sufficient cases do not cover \(M=3\) at \(n=2\) or \(M\in\{3,5,6,7\}\) at \(n=3\). Rosati gives general upper and lower bounds based on error-correcting codes, not this exact short-block classification. Searches using feedback-advantage, short-block, correlated-erasure, projection-code, and orthogonal-array formulations did not locate a covering statement. A residual risk is that the small projection constructions may appear implicitly in classical short-code tables under different terminology.

## Value
PASS. The primary source establishes the first explicit finite-blocklength feedback gap but does not determine whether four uses are minimal. The new statement closes that natural boundary question completely for the qubit channel, for every message size and even for arbitrary message-independent correlated erasures at shorter blocklengths. This is a meaningful exact cutoff, not a numerical refinement of the known four-use example.

## Closest literature and limitations
The closest source is arXiv:2610.00440v1 itself: it provides the exact feedback formula, the sectorwise dimension bound, sufficient no-feedback equality regimes, and the strict four-use counterexample. Rosati's 2024 paper provides the same numerical no-feedback upper bound and coding-based lower bounds, while noting that nontrivial binary maximum-distance-separable constructions are scarce. Neither inspected source states the complete \(n\le3\) all-message equality or blocklength-four minimality. The result is limited to qubit inputs and average success and does not determine the exact four-use no-feedback optimum.

Self-review: passed. Independent audit: not yet performed.
