# Review

## Correctness
**PASS.** The normalized STFT convention is fixed explicitly. For input support sizes other than both singletons and both full, Cauchy--Davenport and prime cyclic Fourier uncertainty establish a \(2p\)-coefficient lower bound. In the remaining full-support case, one character Fourier row is either accompanied by character rows everywhere (yielding exactly \(p\)), or one shifted ratio has at least three Fourier frequencies, forcing at least \(2p\) total coefficients. The three-term expansion has pairwise distinct frequencies and a nonzero middle coefficient for every odd prime. Point-mass constructions attain both levels, and a separate \(p=2\) example verifies the parity boundary. No finite test is treated as a proof.

## Originality
**PASS.** Nicola's Theorem 1.2 and the 2014 localization-operator theorem characterize the \(p\)-coefficient extremizers. The earlier Krahmer--Pfander--Rashkov Proposition 4.3 provides the row-support lower bound but leaves the full/full case at only \(p\), even though their finite diagram already includes the individual \(p=3\) case. The uniform exact second minimum for all odd primes \(p\ge5\) requires the additional ratio-cocycle argument. The closest indexed STFT results concern two-sparse input pairs or generic windows and do not dominate the claim. An unindexed equivalent remains possible.

## Value
**PASS.** The support-count uncertainty theorem separates the smallest conceivable representation from the next one by a forbidden interval of \(p-1\) integers. This is a sharp, growing, window-independent rigidity phenomenon for prime cyclic time-frequency representations, rather than a relabelled numerical bound: any non-extremal exact STFT support necessarily costs at least twice the minimum. Its proof identifies a concrete obstruction in the full-support case that was not controlled by the standard input-support inequality. It does not imply noisy or approximate stability.

## Closest literature and limitations
The closest primary sources are Krahmer--Pfander--Rashkov (2008), Fernández--Galbis--Martínez (2014), and Nicola (2022/2023). The claim is new in its uniform sharp support-gap quantifier, not in the lower bound \(p\), the classification of exact extremizers, or the individual finite \(p=3\) diagram. Possible unpublished or unindexed equivalences remain a risk. The parity counterexample at \(p=2\) and the lack of approximate-support estimates are explicit boundaries.

Same-model review: passed. Independent audit: not yet performed.
