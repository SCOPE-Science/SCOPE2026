# Mathematical review

**Correctness — PASS.** The proof reduces the unrestricted optimum to symmetric edge classes through the concavity of the algebraic-connectivity variational formula. An independently reconstructed Fourier/quotient-block decomposition gives the complete spectral minimum; the exact feasibility reduction to \(S_m(a)\), strict derivative signs, and all-optimizer symmetry argument close every parameter case, including the boundary \(m=6\). The supplied standard-library checker reproduced the symmetric spectra, candidate normalized eigenvalues, and upper bounds against random nonsymmetric allocations (468 finite tests), but the infinite statements depend on the analytic proof, not the tests.

**Originality — PASS, subject to stated search limits.** Sun–Boyd–Xiao–Diaconis gives the broad semidefinite optimization problem, not this graph-specific closed form. Boyd–Diaconis–Parrilo–Xiao solves a different discrete-time wheel problem without the hub leaf; Berman–Förster treats changing a pendant-edge weight, not optimizing all cycle and spoke weights under a budget. Published records on wheel edge polytopes and accessible related optimization findings do not give an implication-equivalent spoke/rim/leaf screening threshold. The general methods could derive specialized examples not explicitly documented, and unlocated specialized coverage remains a real originality risk; absence of hits is not a uniqueness certificate.

**Mathematical value — PASS.** A natural network-design objective has an exact sharp structural transition: the rim edges are useful for three to five rim vertices but worthless in every optimal allocation for six or more. The positive-weight formulas and the unconditional all-optimizer screening assertion offer a design rule that general semidefinite algorithms and ordinary eigenvalue calculations do not state by themselves.

The proof assumes independent nonnegative conductances and one leaf attached at the hub; it does not solve arbitrary pendant placements or enforce positive lower bounds. No claim of external certification is made.

Self-review: passed. Independent audit: not yet performed.
