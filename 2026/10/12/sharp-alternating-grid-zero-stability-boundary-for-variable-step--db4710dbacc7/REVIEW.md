# Scientific review

## Correctness — PASS
The Lagrange derivative formula defines exactly the standard variable-coefficient BDF method and reduces its zero-equation recurrence to a two-step product on differences. Reconstructing the quadratic/cubic/quartic monodromy characteristic polynomials gives the explicit positive-coefficient Jury certificates. The sole order-five changing inequality is the sign of the reciprocal sextic; Descartes' rule and endpoint signs establish exactly two positive boundary ratios. The simple-eigenvalue gcd and continuity establish boundedness at the endpoints. An executable symbolic checker separately reproduces the identities; finite rational experiments are supplementary, not a substitute for the all-ratio proof.

## Originality — PASS (qualified)
The primary contribution is an order-resolved, sharp characterization of the two-periodic BDF recurrence, especially the order-five threshold with reciprocal roots and an ordinary-versus-strong endpoint distinction. Older variable-grid stability theory provides methods and broader necessary/sufficient product criteria, but the available inspected texts of later smooth-grid and BDF2/BDF3 work do not state this classification. Complete text of several older plausible sources was not obtainable, leaving a recorded equivalence risk; no inaccessible source is misrepresented as fully inspected.

## Value — PASS
Alternating timesteps represent a natural stringent test of arbitrary-step stability requirements: an arbitrarily large local ratio repeatedly followed by its reciprocal can be stable for BDF2–BDF4, yet BDF5 exhibits a finite exact ratio threshold. The complete classification and sharp boundary distinguish local ratio restrictions from genuine periodic Floquet instability and can inform variable-step method design.

## Scope and residual risk
Fixed positive two-cycle only, orders at most five, linear zero equation; does not imply arbitrary-grid stability. A preexisting specialized period-two calculation in the older variable-step BDF literature remains possible despite the searches and available full-text comparisons. The scientific review is not independent publication certification.

Self-review: passed. Independent audit: not yet performed.
