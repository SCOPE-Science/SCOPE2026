# Scientific review: sharp cumulant transition in asymmetric telegraph transport

## Correctness: PASS

The two-state Feynman–Kac resolvent gives an exact fourth-cumulant identity in terms of two explicitly defined positive functions. Their second-derivative ratio decreases strictly, and two weighted-average arguments show that the function ratio decreases from \(2\) to \(1\), proving the sharp rate thresholds \(1/5\) and \(1/3\), the one-simple-zero intermediate regime and strict signs at equality. The independent matrix-exponential checker passed 333 comparisons and regime assertions; these finite tests corroborate rather than prove the global theorem. The Brownian extension follows from cumulant additivity.

## Originality: PASS on inspected evidence, with residual priority risks

López and Ratanov (2014), *On the Asymmetric Telegraph Processes*, https://doi.org/10.1239/jap/1402578644, treat precisely the two-rate telegraph generator and compute moments of all orders. Their Theorem 4.1 and subsequent formulas were read in full and explicitly credited. The proposed contribution is not another moment formula or model, but the sharp classification of its fourth-cumulant sign over **every** positive observation time and switching asymmetry, including a unique-crossing proof. A. D. Kolesnik (2012), https://www.mathnet.ru/eng/basm304, treats homogeneous symmetric telegraph moments; its abstract was reviewed, but its separate full PDF could not be retrieved. Related earlier findings treat three-state resting dynamics, spatially periodic reversal rates, or random speeds, none of which entails the present two-state result. Searches for occupation-time cumulants and telegraph excess-kurtosis sign thresholds did not establish equivalent coverage. The existence of previously uninspected work deriving this exact classification remains possible, and independent priority checking is needed.

## Mathematical value: PASS

The physical rate imbalance can now be read directly from the qualitative evolution of transient transport kurtosis: it either always stays negative, crosses once toward positive, or stays positive. Proving absence of further temporal sign crossings is a nontrivial global conclusion; the exact thresholds and robustness to independent Gaussian diffusion make it a useful structural baseline for intermittent transport experiments and theory.

## Limitations and risks

The claim requires stationary initialization, exactly two constant velocities and positive homogeneous switching rates. It does not apply to nonstationary starts, state-dependent diffusion, or more-than-two-state models. Its priority assessment is conditional on examined literature, with the general-moment source already providing ingredients to derive the result. Finite numerical verification and self-review are not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
