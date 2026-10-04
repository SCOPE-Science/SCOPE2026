# Same-model review

## Correctness

PASS. Under pathwise nesting \(C_{m1s}\subseteq\cdots\subseteq C_{mRs}\), the miss indicators are ordered at every observation time. Common predictable exposure weights preserve that order in every weighted prefix-average conditional risk, so the shifted margin vector belongs to the nonincreasing cone. For a nonempty interval box intersected with that cone, the coordinate minimum is the suffix maximum of the lower endpoints and the coordinate maximum is the prefix minimum of the upper endpoints; explicit minimal and maximal cone vectors attain both bounds. The possible-feasibility equivalence uses the nonincreasing tolerances, and the certified-feasibility rule follows from the exact coordinate suprema. The constrained-argmin formula is reconstructed from necessity and a product-region sufficiency argument. The strict rational example and the finite compatibility identities are replayed by the packaged exact-arithmetic checker. The checker supports, rather than replaces, the analytic proof.

## Originality

PASS. The closest primary source, Li and Zhu (arXiv:2609.28522v1), supplies simultaneous rectangular intervals, possible/certified feasibility, and the exact constrained-argmin projection; it also allows the constraint index to encode a nominal level. The inspected source does not impose cross-level nesting or derive an order-cone closure. Ochoa Rivera and Tewari (arXiv:2605.12668v1) establish that nested multi-level online conformal sets are a natural contemporary object but do not study coverage-constrained model selection. Classical order-restricted inference establishes the broad statistical principle that known monotonicity can sharpen inference. Targeted statement-level searches did not reveal the specific suffix/prefix CC-SMCS closure, its certification criterion, or the preserved exact constrained-argmin projection. Residual risk remains because the underlying box/order-cone geometry is elementary and may have an equivalent generic formulation under different terminology; the claim is therefore limited to the stated sequential conformal-model-selection result rather than historical priority for isotonic geometry itself.

## Value

PASS. The motivating sequential model-selection framework explicitly supports multiple nominal-level constraints but pays for them as unrelated coordinates. Modern multi-level conformal procedures deliberately enforce nestedness, so the ignored cross-level structure occurs in a directly motivated use case. The result recovers that structure in \(O(MR)\) deterministic postprocessing, uses no additional data or error budget, and can strictly convert an otherwise ambiguous multi-method projection into a singleton by certifying a cheaper method. It also identifies the precise boundary of the gain: possible feasibility is unchanged under monotone tolerances, while certification is the part that improves.

## Closest literature and limitations

The primary comparison is Li and Zhu, arXiv:2609.28522v1. Ochoa Rivera and Tewari, arXiv:2605.12668v1, provides the recent nested-level conformal setting. Dykstra–Kuo and Berk–Marcus provide classical order-restricted inference context. The theorem requires genuine pathwise nesting, common exposure weights, and monotone tolerances. General partial orders and incompatible order-restricted boxes are outside the exact closed form stated here.

Same-model review: passed. Independent audit: not yet performed.
