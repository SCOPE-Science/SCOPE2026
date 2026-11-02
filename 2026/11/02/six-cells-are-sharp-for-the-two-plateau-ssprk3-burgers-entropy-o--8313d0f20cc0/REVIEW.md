# Self-review

**Correctness — PASS.** The rational modal recurrence reproduces the source large-grid term and produces exact special formulas for six and eight cells. The simple polynomial bounds imply a strict \(A+2\) overshoot for every \(s\in(0,1/4]\); exponential domination establishes the necessary entropy-condition failure. Bernstein positivity of all final means for two and four cells and mass conservation yield the matching nonincrease for every convex entropy on the fixed two-plateau family. Wave-speed consistency is proved through exact stage-trace Bernstein enclosures. The bundled independent-from-symbolic-library rational checker runs successfully; finite grid calculations are combined with a separate stencil-locality proof for all even mesh sizes.

**Originality — PASS, subject to priority uncertainty.** The source [1] treats the same scheme and entropy pair but establishes the counterexample only on even meshes \(N\ge12\), without the sharp minimal cutoff. The 2025 Wei–Shu preprint [2] studies quadratic DG and smooth data with square entropy and does not imply the present two-plateau cell-mean classification. Actual published-finding corpus alias, source-ID, method and cutoff searches returned no matching implication; search nonmatches are not interpreted as a uniqueness theorem. Another paper might contain a small-mesh calculation under a different formulation.

**Mathematical value — PASS.** The mesh size is an intrinsic finite design parameter of the exact published counterexample, not a random numerical slice. Resolving the smallest mesh turns a sufficient twelve-cell obstruction into a complete minimality classification within the natural two-plateau test family, and distinguishes actual counterexample capability from the necessary global entropy obstruction being absent on two and four cells.

**Limitations.** This does not establish that SSPRK3-DG is stable on small meshes for arbitrary initial data, or that entropy fluxes exist when only the global obstruction is absent. The detailed polynomial certificates are specific to the declared method and parameters.

Self-review: passed. Independent audit: not yet performed.
