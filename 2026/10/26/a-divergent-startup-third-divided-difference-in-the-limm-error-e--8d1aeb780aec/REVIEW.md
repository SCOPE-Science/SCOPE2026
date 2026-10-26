# Review

## Correctness

PASS. For the linearly implicit Euler starter on \(y'=y\), exact rational substitution gives \(\widehat{\delta^3}=(2h-1)/(6h(1-h))\), hence \(h\widehat{\delta^3}\to-1/6\). The paper’s own normalization instead gives the exact target limit \(1/6\). The proof and `verify.py` agree.

## Originality

PASS with residual risk. Targeted literature searches for the LIMM startup formula, its aliases, and divided-difference initialization found no implication-equivalent result. The claim is limited to the printed formula, with residual risk for unindexed literature or a later correction.

## Value

PASS. The discrepancy changes the estimator’s asymptotic power from \(h^3\) to \(h^2\), so it is not merely a constant-factor difference. Startup error estimates guide the adaptive step-size and order selection of a variable-order integrator.

## Limitations

The paper’s software implementation and any later erratum were not inspected. This finding does not refute the fixed-step convergence theorem or assert that the published implementation necessarily uses the printed formula.

Self-review: passed. Independent audit: not yet performed.
