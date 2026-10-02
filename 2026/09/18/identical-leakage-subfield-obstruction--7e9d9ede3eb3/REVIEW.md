# Review status

Fresh independent audit: **PASSED**.

Independent audit passed the final claim on all three scientific axes.

- Correctness: **PASS** — For a \(\mathbb B\)-linear leakage map, the set of scalars preserving its kernel is closed under field operations; finite-dimensionality upgrades nonzero inclusion to equality, giving a subfield. Such scalars descend to linear maps on the quotient, so every computed-block leakage with coefficients in the common stabilizer factors through input-block leakage. For a nonzero one-symbol trace functional, nondegeneracy of the finite-field trace pairing forces the stabilizer to be exactly \(\mathbb B\). The product/base repair equivalence and Kronecker rank factorization then follow. An independent GF(8)/GF(2) reconstruction recovered kernel \([0,2,4,6]\) and stabilizer \([0,1]\).
- Originality: **PASS** — The complete Aoutouf--Augot preprint was inspected. Its identical-leakage theorem proves collapse for simple addition and says the same observation seems to extend to array summation; for general coefficients it reports simulations. It does not state the kernel-stabilizer subfield theorem or the all-base-field-computation obstruction. Resultary found only this 2026-09-18 record and stronger related SCOPE records dated 2026-09-19, which postdate it.
- Scientific value: **PASS** — The stabilizer field isolates the exact algebraic boundary at which reused leakage cannot gain information. For trace leakage it proves the suggested array/base-field generalization and cleanly explains why extension-field coefficients can evade the obstruction. This is a reusable structural theorem, not a single simulation.

Full evidence, source comparisons, limitations, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The historical same-model assessment remains preserved in `AUDIT.json` and is not treated as independent validation.
