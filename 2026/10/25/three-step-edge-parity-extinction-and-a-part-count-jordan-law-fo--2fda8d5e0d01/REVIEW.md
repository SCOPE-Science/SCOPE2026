# Review: edge-neighbor parity extinction on even complete multipartite graphs

## Correctness — PASS

The proof is over \(\mathbb F_2\) and distinguishes \(N\) underlying vertices from \(E\) edge states. The equality \(F=B^{\mathsf T}B\) is exact, including the zero diagonal, because each simple edge has exactly two endpoints. Connectivity gives \(\operatorname{im}B=W\) and \(\ker B^{\mathsf T}=\langle\mathbf1_N\rangle\); even total order puts the constant vector inside \(W\). For \(Q=BB^{\mathsf T}\), restriction to \(W\) is identified with the parity-zero vector of \(r\) part sums. Projecting through \(B^{\mathsf T}\) removes one dimension precisely for even \(r\). Since every part has even size, the next \(Q\) kills this image. This proves all rank and zero-cube statements for all allowed class sizes. The Jordan rank differences and kernel cardinalities yield the complete extinction census. Direct matrix checks and exhaustive simulations corroborate the proof without replacing it.

## Originality — PASS, qualified

The line-graph incidence identity is a known fact (Abudayah–Alomari–Sander). General finite-field finite-time convergence is known (Pasqualetti–Borra–Bullo). The closest published complete-multipartite parity analysis concerns bits on the **original graph vertices**, for which the all-even adjacency square vanishes; the present dynamics instead updates **underlying edges** and computes the ranks of \(B^{\mathsf T}B\) and its square. Lights Out on graphs additionally uses a different operator and question. Searches under line-graph, incidence, binary parity, nilpotence and Jordan aliases did not identify the same complete edge-state formula. The remaining risk is a historical graph-code or modular-rank formula not found in indexed literature; search absence alone is not proof of novelty.

## Value — PASS

The sharp nilpotency transition between two and three graph parts, the all-parameter Jordan block structure, and the part-count parity plateau in the exact final-step proportion form a motivated structural classification of a natural graph dynamics. The result applies to infinitely many class sizes and provides all depth strata rather than one small matrix rank. No novel incidence identity, general finite-field convergence theorem, or result for odd class sizes is claimed.

## Limits

Independent evaluation and priority/uniqueness verification have not occurred. Numerical tests reach finite sizes only; the proof is the unrestricted certificate. See the verification document and standalone program for the reproducible checks.

Self-review: passed. Independent audit: not yet performed.
