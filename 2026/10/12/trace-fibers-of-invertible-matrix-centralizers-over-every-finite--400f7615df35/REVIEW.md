# Scientific review: trace fibers of invertible centralizers

## Correctness

**PASS.** The trace identity, including the multiplicity of each elementary-divisor length, is reconstructed from the primary decomposition and filtration. The semisimple quotient and Jacobson radical give the factor \(q^r\), and the full matrix-group additive-character factor is proved with subspace Möbius inversion. Fourier inversion proves the exact zero and nonzero fibers with the \(p\mid s\) boundary separated. A standalone direct enumerator checks all trace fibers for 45 explicit matrices over four finite fields; the proof, not those tests, covers arbitrary \(n\), \(q\), and rational canonical types.

## Originality

**PASS with literature risk.** The same-domain paper of Britnell and Wildon (arXiv:1001.0811, §3) treats class-type structure and determinants of centralizer elements; its simple-module length decomposition is credited as a structural antecedent. Li and Hu (arXiv:1105.4513, Theorems 2.1 and 3.1) establish both the general-linear Gauss-factor identity and the scalar-matrix \(A\) special case of the trace count; neither is presented as new. The stated new result is the closed trace-fiber formula for every invertible centralizer, including mixed irreducible factors and characteristic-sensitive block lengths. The complete 2019 centralizer-structure source (arXiv:1909.06198) was also inspected, especially its block descriptions and determinant/dimension results, but it has no prescribed-trace count. The SageMath centralizer-cardinality table also does not report trace fiber counts. Database searches and accessible papers did not establish a stronger covering theorem.

## Value

**PASS.** The theorem completes a natural and previously structurally motivated invariant: prescribed-trace counting in \(\mathcal C(A)^\times\), the family underlying the standard commuting-pair and class-type questions. The result unifies all similarity types, explains exactly which Jordan lengths are invisible to trace in characteristic \(p\), and yields the precise signed bias between zero and nonzero trace fibers. These are structural and reusable quantitative facts, not an arbitrary isolated enumeration.

## Residual limitations

A combined deduction from familiar centralizer structure and group Gauss sums is conceptually close to this theorem; the credit is explicit. Similar trace counts may have been catalogued under different terminology. No additional determinant conditioning or internal conjugacy classification is claimed. Exhaustive computer checks cover selected examples only.

Self-review: passed. Independent audit: not yet performed.
