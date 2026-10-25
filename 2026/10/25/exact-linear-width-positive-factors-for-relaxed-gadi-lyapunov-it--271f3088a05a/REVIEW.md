# Review of the exact GADI factor identity

**Correctness — PASS.** Direct substitution of the two-stage iteration yields \(X_{k+1}=cX_k+bTX_kT^{\mathsf T}+EE^{\mathsf T}\). Binomial powers, positive weights and a Vandermonde witness prove all claimed ranks and factor formulas. The independently constructed dense iteration was compared numerically with the factor representation. Finite tests are not the infinite proof.

**Originality — PASS (self-review, priority uncertain).** Zhang and Xun arXiv:2404.06034v1 explicitly build \((2^k-1)p\)-column GADI factors and discuss their exponential storage/complexity; their ordinary ADI special case already uses \(kp\) columns. The new comparison isolates the nonzero-relaxation binomial Krylov factor and its exact PSD rank. Classical CF-ADI/rational Krylov work supplies the same general space but not an identified covering expression. Targeted published-finding corpus searches found no directly matching published record. Other source formulations remain possible, and the complete Li--White primary text was not independently inspected.

**Mathematical value — PASS.** Replacing exponential factor width with \(kp\) exactly (not approximately) is a substantive structural improvement for the given matrix-equation algorithm. The rank formula and positive factor apply to all allowed relaxation values. Nothing is asserted about variable parameters, floating-point robustness or realized timing.

Self-review: passed. Independent audit: not yet performed.
