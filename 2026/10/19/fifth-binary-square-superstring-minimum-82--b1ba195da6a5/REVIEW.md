# Review of the exact fifth binary square-superstring minimum

## Correctness — PASS
The minimum-overlap Hamiltonian-path reduction is proved in both directions, including the distinction between linear and cyclic factors, zero overlap, and repeated optional factors. The finite lower bound is an integer optimum of a deliberately relaxed directed Hamiltonian-tour model with a dummy vertex, 1056 binary arc variables, 66 degree equations and 20 valid subtour inequalities. These inequalities can only reduce the relaxation's feasible set relative to the assignment model, but every genuine Hamiltonian circuit satisfies them; thus an optimal relaxed value of 82 excludes any cheaper true tour. The executable checks solver status, lower bound, integer route and integer cost; its independent coverage and shorter-order checks succeeded. An 82-bit explicit witness closes the bound.

## Originality — PASS, with residual risk
Au's full-length source (arXiv:0904.3997, first public 2009-04-25; updated 2015) supplies the general setting and a lower bound 72 and a constructive upper bound 89 at this parameter, not the exact fifth value 82. OEIS A372435, inspected as an exact same-invariant table, lists only 4, 12, 24, 48. Tan–Shallit's 2013 original full text treats represented factor sets and shortest witnesses, not the same mandatory-subset covering optimum. Search of published research records using exact parameters, shortest-common-superstring aliases, and published mathematical claims found no equal or stronger exact value. An unindexed computation or update not present in accessible sources remains possible; negative search is not proof of uniqueness.

## Mathematical value — PASS
The precise fifth minimum is the next natural missing term of a publicly maintained mathematical sequence and closes the first gap beyond four exact cases in an explicitly studied power-covering problem. It improves the literature's order-five interval from 72–89 to a sharp 82 and supplies a reusable small integer-program benchmark with a constructive witness. No unproved general pattern, all-order statement, or claim about the enumeration of optima is made.

## Review boundaries
No independent audit or solver-proof-trace check has been performed. The finite computational result assumes a correct implementation of the supplied integer-program solver; the source, fixed cuts and direct witness are supplied for independent reproduction. The residual originality risk concerns equivalent results under alternative terminology or in sources unavailable to the present inspection.

Self-review: passed. Independent audit: not yet performed.
