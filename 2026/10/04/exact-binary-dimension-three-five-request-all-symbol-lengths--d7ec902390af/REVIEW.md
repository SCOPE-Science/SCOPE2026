# Review

## Correctness
PASS. The claim is exactly Over \(\mathbb F_2\), the exact minimum lengths for five-request all-symbol PIR and all-symbol batch codes of dimension \(3\) are both \(10\): \(\operatorname{ASP}(3,5,2)=\operatorname{ASB}(3,5,2)=10\). A length-\(10\) witness has column multiplicities \((0,1,1,2,2,2,2)\) on the seven nonzero vectors of \(\mathbb F_2^3\), and no rank-\(3\) binary generator multiset of length at most \(9\) satisfies the five-all-symbol PIR property. The lower-bound search is exhaustive because a minimum binary dimension-three generator can omit zero columns, leaving exactly seven possible nonzero column types; every multiset of a given length is represented by one seven-entry multiplicity vector. Every recovery set can be shrunk to an inclusion-minimal recovery set, and in dimension \(3\) such a set has size at most three. The verifier checks all rank-\(3\) multiplicity vectors through length \(9\) and finds none with five disjoint recovery sets for every stored type. For the upper bound, it checks all \(252\) five-request multisets of the six stored types of the explicit length-\(10\) witness and validates a complete certificate file.

Risk: this is a finite exact theorem, not an asymptotic or infinite-family argument. Its correctness depends on the enumerated finite state space and the recovery-set reduction; both are explicit in the proof and independently recomputed by the packaged verifier.

## Originality
PASS. arXiv:2601.04041v2 defines the exact invariants and gives only \(8\le\operatorname{ASP}(3,5,2)\le\operatorname{ASB}(3,5,2)\le10\) from its general bounds. Its Section 5 explicitly leaves optimal lengths at small dimension open beyond the solved small-request cases. The source also identifies the equivalent disjoint-repair-group language, and the inspected literature trail does not supply this exact parameter. The closest published published-finding corpus finding is the four-request binary dimension-three value \(7\), which implies only the lower bound \(8\) at five requests.

Risk: an older small case could be hidden under availability, majority-logic decoding, or disjoint-repair-group notation. The 2022 DGRP conference paper was identifiable and its role was inspected through the 2026 paper's literature review and available bibliographic/full-text indexing, but a complete publisher-hosted full-text comparison was not available in the inspected route.

## Value
PASS. The 2026 source explicitly identifies exact optimal lengths for small dimension as an open direction. This result resolves the first five-request binary dimension-three point, closes the source paper's interval \([8,10]\) to a single value, and shows that the stronger all-symbol batch optimum equals the all-symbol PIR optimum at this parameter. The fact is a natural exact invariant of the newly introduced code family, rather than an arbitrary parameter slice.

Risk: the contribution is deliberately narrow and finite; its value is as a sharp boundary datum for the small-dimension program, not as a general construction theorem.

## Closest literature and limitations
The closest primary source is Boruchovsky–Gruica–Niemann–Yaakobi, arXiv:2601.04041v2. The closest equivalent-language source is Karingula–Vardy–Wootters, ISIT 2022, on disjoint repair groups. The closest published exact small-dimension comparison located in published-finding corpus is the dimension-three four-request binary result. No claim is made beyond \((k,t,q)=(3,5,2)\).

Same-model review: passed. Independent audit: not yet performed.
