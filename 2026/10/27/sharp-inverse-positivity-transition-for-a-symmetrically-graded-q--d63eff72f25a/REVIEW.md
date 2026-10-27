# Scientific review

**Correctness — PASS.** The stated tensor-product stiffness and quadrature mass are reconstructed from the quadratic Gauss–Lobatto element matrices. An exact reflection-parity inversion and integer polynomial sign certificate establish the unique cutoff for every positive grading ratio, not just for sampled values. The standalone exact-arithmetic verifier reconstructs 55 representative Green entries and tests all required polynomial inequalities. The claim is limited to this fixed 25-interior-node family.

**Originality — PASS, with priority uncertainty.** Cross–Zhang (arXiv:2310.15341) proves sufficient nonuniform-grid monotonicity criteria and reports a different five-cell numerical failure. Its Theorem 4.1 and Section 5.2 do not imply the exact symmetric three-cell cutoff. Cross–Zhang (arXiv:2010.07282) discusses the related Q3 scheme and uniform-grid Q2 theory. The 2021 Hao Li thesis was located, but its full text could not be inspected, leaving a real priority risk. Searches did not establish a covering theorem, which is not proof of global uniqueness.

**Value — PASS.** The exact transition is a natural sharp benchmark for Q2 graded-mesh discrete maximum principles: it converts nonsharp mesh restrictions into a precise necessary-and-sufficient criterion on an interpretable minimal symmetric family, with a positive-to-negative Green-entry sign change and equality characterization. The result does not classify general anisotropic or arbitrary graded meshes, nor time-integration behavior.

Self-review: passed. Independent audit: not yet performed.
