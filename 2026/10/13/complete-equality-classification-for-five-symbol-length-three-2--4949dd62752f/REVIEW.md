# Self-review

## Correctness
PASS. The published theorem gives the exact optimum \(F(3,5)=7\). The finite classification is independently replayable: all coordinate partitions, all length-three IPP conditions, the quotient by codeword relabeling, descendant checks, stabilizers, and distance profiles are recomputed from scratch by `verify.py`. The classification is expressly limited to seven-word codes over five symbols.

## Originality
PASS. The closest direct full text proves the optimum and studies a selected partial-order-minimal maximum graph; it does not state that all optimum codes lie in one equivalence class or give a census. Exact-parameter and structural searches found no prior statement of the two classes, \(432{,}000\) literal maxima, equal orbit sizes, or stabilizer order \(48\). The nearby length-three traceability result is stronger in property but smaller in optimum size and does not imply the seven-word IPP equality structure.

## Value
PASS. The five-symbol case is explicitly singled out in the classical small-alphabet theorem. The classification reveals that partial-order minimization hides a second natural extremizer, so it adds structural information rather than a routine recount of the known optimum.

## Closest literature and limitations
Tô and Safavi-Naini, DOI 10.1137/S0895480102400424, is the decisive comparison. It supplies the exact optimum and one q=5 maximum graph but not the complete equality classification. The embedded verifier does not independently re-prove their upper bound. A residual risk remains that an obscure unindexed historical source may have enumerated the same equality cases.

Self-review: passed. Independent audit: not yet performed.
