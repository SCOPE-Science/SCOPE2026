# Review

## Correctness
PASS. The claim is a finite statement over all binary words of lengths \(1\) through \(7\). The error ball is reconstructed independently by string and tuple operations for every word. Explicit witnesses give the lower bounds. The upper bounds are exhaustive maximum-clique proofs with a valid greedy-coloring bound, so no sampling, timeout, or asymptotic extrapolation is used. The packaged replay returns exactly \(2,3,4,7,11,17,30\).

## Originality
PASS. The 2022 Wang--Vu--Tan paper introduces the same either/or error channel and supplies an order-optimal-redundancy construction, while the expanded 2023 full text develops the channel and constructions without the exact initial table. The 2025 Ye--Ge work supplies asymptotic cardinality upper bounds rather than these finite exact values. Searches using the exact channel name, equivalent asymmetric-shift language, the length-\(7\) value, and the full sequence found no inspected publication or checked published-finding record that states or implies the result. Residual risk is limited to unindexed or unpublished finite computations.

## Value
PASS. Exact finite optima are a natural benchmark for a channel whose published theory is primarily constructive and asymptotic. The complete initial profile quantifies short-block performance, gives a reference point for evaluating finite-length constructions, and separates the precise either/or model from stronger simultaneous-error models. The result is limited but mathematically motivated rather than an arbitrary parameter slice.

## Closest literature and limitations
The closest primary source is Wang--Vu--Tan, DOI `10.1109/ITW54588.2022.9965921`, with its expanded treatment arXiv:`2301.11680`. The closest broader upper-bound source inspected is Ye--Ge, arXiv:`2507.04806`. The result makes no claim for \(n\ge8\), no claim for simultaneous deletion and transposition, and no claim that all possible unpublished computations have been excluded.

Same-model review: passed. Independent audit: not yet performed.
