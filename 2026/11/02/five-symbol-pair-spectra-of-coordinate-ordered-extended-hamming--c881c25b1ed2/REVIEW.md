# Scientific assessment: five symbol-pair spectra of the extended Hamming code

## Correctness — PASS

A self-contained affine-incidence proof counts the fourteen four-point planes, three planes through each two-point edge, and gives the full pair-weight enumerator from two natural incidence indicators. Counting opposite four-windows and conditioning on the alternating affine-plane partition produces the exact class multiplicities \(10,12,4,2,2\). The affine-code stabilizer has order \(1344\), yielding exactly thirty distinct coordinate-labeled codebooks. Two independent constructions and all normalized coordinate permutations were checked by `verify.py`, which returned `VERIFY_OK`. The computation corroborates rather than supplies the proof.

## Originality — PASS, qualified

The pair metric and symbol-pair Singleton bound predate this work. Chee et al. (arXiv:1211.1728, Proposition 4.4/Table I) already give an explicit binary length-eight pair-MDS code with pair-distance six; **existence** of a code at these parameters is not claimed as new. Chen (arXiv:2206.12668, Example 4) examines an extended Hamming code under one coordinate presentation and reports its pair metric and covering behavior. Saniga (arXiv:1509.06009) explicitly lists thirty labeled Fano planes with a different arithmetic-line classification, furnishing related incidence data. The inspected materials do not present the **simultaneous five-type pair-weight enumerator classification and exact multiplicities for all coordinate permutations**. Searches for alternate Hamming/permutation/Fano/pair-metric descriptions and an indexed mathematical record search found no matching stronger result. Residual risk: an unindexed prior finite table or a later derivation from existing Fano incidence lists could cover the same statement; priority is not independently certified.

## Value — PASS

For overlapping-pair read channels, the Hamming-equivalent presentations of one code need not be equivalent. The theorem answers exactly which cyclic coordinate interleavings attain the optimal pair distance and how all pair weights change: a natural selection problem for a standard length-eight code, with a structural invariant, an exhaustive classification and a sharp MDS/non-MDS split. This is a complete motivated fixed-length fact rather than merely proving the existence of another code or reprinting an incidence table. No physical device performance is inferred.

## Limitations and independent verification

The theorem is specific to the binary length-eight extended Hamming code, indexed cyclic coordinate order and one-step symbol-pair metric. General lengths and external peer validation are outside its scope. All thirty incidence systems were counted with exact arithmetic; the accompanying computation is finite and repeatable.

Self-review: passed. Independent audit: not yet performed.
