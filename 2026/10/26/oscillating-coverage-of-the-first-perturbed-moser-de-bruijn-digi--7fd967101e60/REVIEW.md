# Review of the weighted Moser–de Bruijn sumset result

## Correctness — PASS

For each digit-pair, the four coefficients \(0,1,6,7\) are distinct modulo four, so their least-differing-digit argument proves global injectivity. All twelve entries in the explicit three-state carry table follow by direct substitution. The row sums of the count-transfer matrix are four; every state has exactly two transitions to zero, yielding \(a_L=4^L/2\). The recurrence for carry one gives \(b_L=(4^L+2)/3\). One more high digit produces \(2a_L+b_L=(4^{L+1}+2)/3\). Distinct limiting fractions prove density nonexistence. The standalone verifier independently enumerates all sums below \(131072\) and checks both formulas through length eight. Computations corroborate but do not replace the proof.

## Originality — PASS (best-knowledge assessment)

The classical \(M+2M\) result is already in OEIS A000695 and Nathanson; de Bruijn's 1964 full text treats signed complete unique decompositions, not the explicitly counted positive \(M+6M\) sumset. OEIS A126684 gives a union of two digital sets, not this weighted sum. Peter's general automatic-density criteria and Heuberger–Kropf–Prodinger's transducer theory may supply implicit machinery but do not display these two concrete counts in the inspected material. Searches for positive \(M+6M\), its literal first values, its aliases, and the two cutoff constants did not find a covering result. Residual risk: an implicit specialization or unindexed record may already state the finding; the available full text of Peter's original paper was not located during this review.

## Mathematical value — PASS

The classical coefficient two has perfect global coverage. Six is the **least greater coefficient** retaining four distinct digit-pair residues modulo four; it therefore preserves injective representations while exposing a genuinely different global coverage law. The exact two-scale discrepancy shows a natural digital weighted basis of positive upper-scale frequency can lack natural density. This is an explicit qualitative boundary for a canonical sparse additive set, not an arbitrary finite slice.

## Limits and sources

No claim is made about global liminf/limsup, other weights, or independent auditing. See the proof and References in `RESULT.md` for de Bruijn (1964), Nathanson (2010), OEIS A000695/A126684, Peter (2003), and Heuberger–Kropf–Prodinger (2015).

Self-review: passed. Independent audit: not yet performed.
