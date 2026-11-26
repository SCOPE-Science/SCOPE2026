# Independent mathematical audit

## correctness

PASS

In the transient states 11, 10, 01 the holding rates are r+E, r+u+a, r+v+b; from 11 the 10 and 01 transition rates are v and u respectively. Accessibility of the absorbing state on this finite chain gives a finite mean even at r=0. Eliminating the singleton-state means gives numerator N=(r+E)(r+E+K)+A−U and denominator D=rN+U(2r+E+K), which expand to the displayed coefficients. N>0 follows, e.g., from E²−U>0, so D>0. With totals fixed, cross-multiplication cancels the rN_P N_Q terms and leaves (2r+E+K)(V N_P−U N_Q). This proves the stated sign factor. The quadratic h=(r+E)(r+E+K) starts at E(E+K) and is strictly increasing to infinity. For U≠V the strict-threshold case gives a simple interior root with the asserted quadratic-formula value, equality gives just the endpoint tie, and a lower threshold gives no tie. With U=V the sign reduces to the constant product comparison for A and B. In the witness U=1, A=4, V=24/25, B=3; the threshold is 21 and h(1)=21. D_P=(r+3)(r²+5r+2), so cancellation reproduces the displayed difference. A separate exact rational Gaussian elimination of the three-state equations reproduced the witness difference at r=0, 7/8, 1, 9/8, 7. Inspected, not executed: verify_two_patch.py. The finite checks are corroboration, not the universal proof.

## originality

PASS

Credit the matched-total reversal criterion and its sharpness, not the finite-chain first-step method or the general effect of independent killing. Strong model overlaps do not cover the joint matched-total comparison; the historical literature assessment is qualified.

## value

PASS

Even fixing both rate sums need not yield a uniformly best design for mean persistence. The proof isolates which product tradeoff matters and limits its consequence to one reversal, with an exact decision condition and feasible witness. This is a motivated structural comparison, not a fitted effect or a generic first-step calculation. It applies to a two-patch mean from full occupancy and does not rank other survival statistics or establish a field-management rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
