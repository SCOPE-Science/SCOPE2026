# Self-review

## Correctness
PASS. Every physical two-mode density operator is parity block diagonal. Each pure vector in the even block is the image of \(|00\rangle\) under an explicit determinant-one matchgate block, and each pure vector in the odd block is the image of \(|01\rangle\) under an explicit determinant-one matchgate block. Spectral decomposition therefore proves that the full physical two-mode state space equals the convex hull of pure fermionic Gaussian states. The source's channel family preserves parity superselection. Its written local convex-Gaussian channel condition is consequently automatic, while its own formula yields \(C_+(\mathrm{SWAP},0)=1\) and \(C_-(\mathrm{SWAP},0)=0\), giving a direct counterexample to Eq. (35).

## Originality
PASS. The 2014 four-mode concurrence theorem and its first-nontrivial-dimension statement are prior art and are used as supporting structure, not claimed as new. A public review of the 2026 preprint had already called the channel-to-Choi equivalence unproved. The present claim is stronger and more specific: it proves that the equivalence is false under the exact local input-output definition written in the paper and supplies the explicit noiseless-SWAP witness. Targeted exact-identifier, alias, implication, broader-literature, semantic-index searches did not locate an equivalent correction.

## Value
PASS. The corrected distinction is load-bearing for the paper's interpretation of its \(\approx 62\%\) Choi threshold as the onset of convex-Gaussianity of the two-mode resource channel. Because the written local property is already true at zero noise, a meaningful threshold must concern a stronger ancilla-sensitive channel notion. Identifying this dimensional collapse prevents a four-mode state criterion from being mistaken for a nontrivial local two-mode channel criterion.

## Closest literature and limitations
The closest scientific source is Oszmaniec--Gutt--Kuś, which proves the four-mode state criterion and explicitly identifies four modes as the first non-trivial convex-Gaussian state case. The closest critical discussion is a public technical review that notes the missing proof of the Choi-to-channel step but does not exhibit the counterexample. The claim does not dispute the Choi concurrence algebra and does not determine whether the same numerical threshold remains valid for a properly defined ancilla-sensitive resource-preservation notion.

Self-review: passed. Independent audit: not yet performed.
