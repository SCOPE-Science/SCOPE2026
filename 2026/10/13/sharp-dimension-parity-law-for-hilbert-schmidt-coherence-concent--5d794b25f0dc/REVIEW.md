# Scientific review

## Correctness — PASS
The source-independent proof applies to every CPTP map preserving input diagonals as output diagonals. Its crucial Heisenberg observable is a traceless Hermitian contraction because diagonal states remain diagonal. A direct eigenvalue-polytope argument bounds its Hilbert–Schmidt norm by the exact even/odd constant. The dual pairing and equality construction are algebraically verified, including positive input eigenvalues, both parities, Kraus trace preservation, and the output marginal. The attached standalone code checks dimensions \(2\)–\(12\); the infinite family is established analytically. Mathematical risk: none identified within the stated finite-dimensional assumptions.

## Originality — PASS, with residual risks
Cheng–Hall (arXiv:1508.03240, Sec. II C) proposed the underlying quantity; Rana–Parashar–Lewenstein (arXiv:1511.01854, Sec. IV) already disproved monotonicity and exhibited ancilla-erasure amplification. The latter implies the present lower bound in even dimensions, and this known mechanism is explicitly credited. The contribution assessed is the exact global upper bound over **all** maximally incoherent \(d\)-to-qubit channels, the parity-sharp constant and attainment by SIO on full-rank inputs. It is not a new counterexample to monotonicity. Primary-text checks found no corresponding optimality theorem. A 2020 study with a directly relevant title could be inspected only through a first-page preview; equivalent bounds in less-targeted norm literature remain a genuine priority risk.

## Value — PASS
Dimension-limited coherence concentration is a natural quantitative question precisely because Hilbert–Schmidt coherence is nonmonotone. The result supplies a complete sharp capacity factor for all input dimensions and a broad operational class, including a dimension-three no-amplification boundary and unbounded high-dimensional growth. Full-rank saturation shows the effect is not merely a low-rank edge case. This does not rehabilitate the invalid coherence measure or solve general output dimensions.

Self-review: passed. Independent audit: not yet performed.
