# Scientific review

## Correctness — PASS
The reduction of a two-state stochastic matrix to an affine interval self-map is exact. When all letter maps preserve order, the upper or lower envelope gives the extremal final state at each fixed length. Its orbit is monotone, so strict active affine lines cannot disappear and reappear. In the converse construction, every crossing lies between the last two orbit states of the preceding block; the additive slope increments make the correct block's affine line strictly dominant exactly on its intended states. The parameter \(\varepsilon=2^{-(2n+10)}\) keeps each transition stochastic and the orbit below \(1/2\), and rationality is explicit. The one-state lower bound applies because the alphabet has at least two letters. Exact-rational construction checks cover 103 block profiles, 416,353 competitor words, and longer local-inequality instances.

## Originality — PASS within inspected evidence
Gill's Theorem 4.1 gives the binary two-state classification, including two-block words, and Section 4.4 shows that binary witnesses can be embedded in larger alphabets. These do not imply two-state witnessability for words with three or more *occurring* letters, nor the exact order-preserving witness-language characterization. Kjos-Hanssen's universal three-state theorem treats a different bound and specifically leaves the larger-alphabet two-state classification open. Searches for monotone two-state PFA winners, affine envelope symbolic itineraries, distinct-letter blocks, and related mathematical records found no prior covering statement. An unindexed affine-IFS result may nonetheless be equivalent.

## Mathematical value — PASS
The theorem identifies a structurally natural, maximal-by-characterization subclass of order-preserving two-state witnesses over every finite alphabet, with explicit rational machines and arbitrarily many distinct letter blocks. This gives an exact and nontrivial subfamily of the open larger-alphabet two-state complexity classification, not merely a single finite example. The necessity proof also explains the boundary: interleaved repetitions require departures from order preservation.

## Limits and closest literature
The statement does not classify arbitrary two-state PFAs with order-reversing letters, does not provide length-uniform gap bounds, and does not prove universal novelty beyond the inspected sources. The closest works are Gill, arXiv:2402.13376 (2024), and Kjos-Hanssen, arXiv:2607.26275 (July 2026).

Self-review: passed. Independent audit: not yet performed.
