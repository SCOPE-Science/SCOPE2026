# Review

## Correctness
**PASS.** The claim is finite and fully quantified. The verifier reconstructs all \(128\) binary length-seven words, implements the zero-padded adjacent-multiset read vector in two equivalent encodings, checks all pair distances for agreement, and proves the compatibility graph has clique number \(8\) using two exact algorithms. The displayed eight-word witness is checked directly. The classical value \(16\) is supported by the radius-one Hamming bound and an explicitly verified length-seven Hamming code.

## Originality
**PASS, with residual risk.** Sun--Ge study precisely \(2\)-read codes at minimum distance \(5\), but the inspected full text gives general/asymptotic bounds and does not state an exact binary length-seven value. Banerjee et al. introduce the read-vector model but their stated coding results concern the earlier \(\ell\ge3\), distance-three regime. Exact-claim, alias, parameter, and broader-coverage searches found no source asserting the value \(8\). The closest semantic database hits concern different metrics such as ordered symbol-pair codes, so they do not imply this claim. A small unpublished or unindexed finite table remains possible.

## Value
**PASS.** Length seven is structurally motivated rather than an arbitrary cutoff: it is the first nontrivial perfect binary Hamming length. Sun--Ge's distance-five reduction gives only the classical distance-three ceiling, which here equals \(16\); the exact read-metric optimum \(8\) shows that the reduction loses a factor of two at this natural boundary. That isolates a concrete finite effect of the nanopore read-vector geometry.

## Closest literature and limitations
The closest source is Sun--Ge, arXiv:2403.11754, whose definition and distance-five section cover the same objects and metric but whose reported result is asymptotic rather than this finite optimum. Banerjee et al., arXiv:2305.10214, is the foundational source for the composition/read-vector model. The result is confined to one exact finite parameter and leaves all neighboring lengths and asymptotics open.

Same-model review: passed. Independent audit: not yet performed.
