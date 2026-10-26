# Scientific review

## Correctness

**PASS.** The finite-graph circulation criterion for the exact synchronous three-state rule is used within its hypotheses. The elementary triangular cycle basis and the refractory three-step excitation bound force either extinction or period three. The transfer trace counts labelled cyclic words; subtracting the all-refractory rim correctly enforces hub excitation, and division by three is handled by fixing the hub phase. The extinction-basin trace counts cyclic words avoiding both disallowed adjacent colour orders. The exact characteristic polynomials and all trajectories for wheel sizes \(3\) through \(10\) are independently checked by executable standard-Python code. The finite checks do not replace the proof for all sizes.

## Originality

**PASS, subject to bounded-search risk.** The closest precise predecessor is the graph-independent circulation criterion of Gravner, Lyu and Sivakoff (arXiv:1610.07320, Theorem 3): its qualitative trichotomy and rate formula are used, not claimed as new. Material checked from the original primary paper and related finite-graph analysis did not provide the wheel transfer spectrum, exact three-cycle counts or closed extinction-basin count. Searches tested wheel/excitable-media aliases and recurrence/coefficient descriptions, with no equivalent implication identified. The early Greenberg–Hastings founding article remained inaccessible in full, and hidden prior enumerations remain possible.

## Mathematical value

**PASS.** The wheel is a natural minimal graph family where every rim interaction shares a central vertex, rather than a parameter-picked small instance. The result answers two distinct global questions exactly—how many oscillating recurrent orbits exist, and how many initial configurations avoid them—revealing incompatible exponential scales \(\lambda\) and \(1+\sqrt2\). It provides more quantitative information than the existing arbitrary-graph activity test and is directly reproducible without numerical approximations.

## Scope and limitations

The statements are for labelled wheels, three states, synchronous threshold-one excitation and all integral rim sizes at least three. A source-based general dynamics theorem is invoked. No independently conducted audit or exhaustive all-literature priority check is claimed.

Self-review: passed. Independent audit: not yet performed.
