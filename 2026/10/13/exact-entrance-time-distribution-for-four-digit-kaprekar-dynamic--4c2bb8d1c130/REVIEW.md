# Review of the entrance-time distribution

## Correctness

**PASS.** The integer difference-state dynamics are well-defined for every odd base \(B\ge5\), and the first-entry stopping time is unambiguous. The proof separately classifies interior, diagonal and zero-inner-difference states. It then counts the corresponding states and four-digit words using an exact multinomial weight, with all sums performed symbolically. The finite verifier independently checks 49 odd bases by state enumeration and four small bases by direct word enumeration, without substituting finite cases for the proof.

## Originality

**PASS, with scope and residual risk.** The closest primary source, Chen--Ono--Schwartz--Thakur (2026), proves entry within three steps and gives a one-step transition table. Those inputs are explicitly reused, but the complete closed-form weighted entrance-depth distribution, including a uniform-word probability law, is not stated there. Devlin--Zeng (2021) addresses fixed-point distances and attraction proportions; Kay--Downes-Ward (2022) addresses odd-base terminal cycles. Actual semantic searches of published research for Kaprekar depth, preperiod, first entrance and the stable region found no equivalent distribution. A stronger local formula is available in the source and implies the ability to perform these counts, so the new contribution is quantitative enumeration rather than a new transition law. Unindexed exact counts remain a risk.

## Value

**PASS.** Sharp transient statistics distinguish the rare worst case from typical digit inputs: one state needs three steps, while a uniformly chosen nonconstant string has three-step probability asymptotic to \(3/B^2\). The all-base distribution reveals the parity-dependent finite-size correction and simultaneously supplies a complete state-level and digit-level classification. This is a motivated exact invariant of the recent odd-base Kaprekar model, not a selected numerical table.

## Limitations

The stopping time is entry into the invariant odd region, not convergence to a terminal cycle. The proof uses known casewise dynamics. No claim is made for even bases or arbitrary digit length. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
