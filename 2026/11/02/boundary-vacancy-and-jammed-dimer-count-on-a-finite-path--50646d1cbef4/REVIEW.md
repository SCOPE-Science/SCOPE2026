# Scientific review: boundary vacancy and jammed dimer count

## Correctness — PASS

The first-arriving edge splits a path into independent subpaths, producing explicit recurrences for the mean dimer count, endpoint vacancy probability and their mixed moment. Formal-power-series solutions give the stated closed mixed-moment generating function. The coefficient formulas are rational and were independently checked by exhaustive attempted-edge enumeration through eight sites. The all-size sign proof does not extrapolate from finite tests: for lengths at least ten it bounds exponential-series tails strictly below the magnitude of the negative limiting constant. The remaining sizes are exactly evaluated. The limiting constant follows from the singular and entire parts of the explicit generating functions.

## Originality — PASS, with priority qualifications

The discrete dimer-parking model and recursive splitting are classical, not claims of novelty. Gerin's arXiv:1411.8002 supplies an exact first-edge construction and occupation-density results; Krapivsky's arXiv:2009.08609 treats an isomorphic monomer-exclusion model and gives marginal total-count statistics and boundary occupation probabilities. Neither inspected manuscript states the mixed endpoint-vacancy versus final dimer-count generating function, the exceptional fifth-size zero, or the nonzero limiting covariance. The closest related current mathematical records concern endpoint-to-endpoint vacancy dependence and random-greedy matching on different graphs, which do not directly imply this mixed boundary/global claim. Full historical coverage of older adsorption correlation methods has not been established: J. W. Evans's 1993 survey and certain older books were accessible only as abstracts/descriptions.

## Mathematical value — PASS

The question couples a local boundary defect to a natural global jamming statistic. Its dependence remains strictly negative, with a nonzero limiting covariance, and exhibits a finite-size equality at exactly five sites. This contrasts with rapidly decaying endpoint-to-endpoint interactions and cannot be read from either marginal expectation alone. The exact mixed generating function supplies reusable finite-volume information for boundary-sensitive sequential adsorption.

## Limitations and risks

Only uniformly ordered nearest-neighbor dimers on a finite path are treated. Full statistical independence is neither asserted nor established from a covariance zero. Existing general correlation frameworks may subsume portions of the argument; independent priority assessment remains necessary. Computational checks cover finitely many instances and are not infinite proofs.

Self-review: passed. Independent audit: not yet performed.
