# Independent Audit — 2026/09/18/garsia-counterexamples-finite-butson-hadamard-bases--5e0ce6e50d84

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `38b892bfb285596e770987c53c500986a3a4a9db`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite completion argument is sound. On Z_M times {0,1}, the u_n block has two Fourier copies with the second frequencies permuted, and v_n=(-1)^epsilon u_n. Character orthogonality makes the 2M vectors mutually orthonormal, hence a complete unimodular basis; for odd prime M their entries are 2M-th roots of unity. For an arbitrary ordering of all columns, restriction to the distinguished u_1,...,u_N columns gives the permutation to which Lewko's two-ordering pattern lemma applies. Giving every other column coefficient zero preserves maximal partial sums. A sufficiently fine prime grid samples the open bad set with positive density, and the nonzero arithmetic-progression step is invertible mod M, so multiplication by it merely permutes the grid. Thus the source obstruction survives discretization and square completion exactly as claimed.

## Originality

**PASS** — Lewko's September 2026 preprint gives the negative solution, based on two differently ordered trigonometric copies, and constructs a complete uniformly bounded infinite system. Searches combining the Garsia problem with finite groups, finite atomic probability spaces, complex/Butson Hadamard matrices and Fourier block completions did not locate the submitted finite square unimodular-basis strengthening. The construction is a short consequence of a very recent theorem, but its finite atomic/Butson restriction is not stated in the located source.

## Scientific value

**PASS** — The result rules out two plausible explanations for the counterexample at once: incompleteness and nonatomicity. It places the every-permutation obstruction inside a rigid finite matrix class and gives infinitely many matrix orders for each threshold. That makes the phenomenon available to finite-dimensional harmonic analysis and explicit matrix experimentation, even though it does not improve the infinite counterexample itself.

## Sources

- On Kolmogorov's rearrangement problem and Garsia's conjecture (Mark Lewko): https://arxiv.org/abs/2609.18491 — Primary recent source; the indexed abstract confirms the two-copy trigonometric construction and prescribed-permutation-pattern mechanism.
- On Kolmogorov's rearrangement problem for orthogonal systems and Garsia's conjecture (Jean Bourgain): https://doi.org/10.1007/BFb0090057 — Classical background on the rearrangement problem and Garsia's conjecture.

## Limitations

- The finite Butson strengthening gives no useful dimension-versus-threshold bound and does not produce real ±1 Hadamard examples.
- Because Lewko's preprint is extremely recent, an unindexed parallel finite-cyclic observation remains a real originality risk.
- The audit independently checked the finite cyclic orthogonality, discretization and completion steps; it relies on Lewko's published two-ordering/Fourier obstruction as the imported source theorem rather than re-proving that theorem.

GitHub was read only as evidence; no repository mutation was performed. The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. Open-access/preprint material was checked before other sources; no Oxford Download was needed for this record.
