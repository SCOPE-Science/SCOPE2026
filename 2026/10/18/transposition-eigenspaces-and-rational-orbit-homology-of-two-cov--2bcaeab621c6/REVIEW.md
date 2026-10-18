# Review of the transposition-eigenspace finding

## Correctness — PASS

The proof fixes the complex on graph-edge vertices and distinguishes chain orientation signs from edge-orbit counts. For a fixed face with \(q\) orbits the reduced Lefschetz contribution is \((-1)^{q+1}\), including the augmented empty face. It classifies all extension choices of a nonempty outside graph by its one- and two-vertex covers, then proves the only nonzero outside weights arise from one edge, two edges, a triangle, or a four-cycle. The exact count gives \(\widetilde L=\binom{m-1}{3}\) for every \(m\ge4\). Jonsson's Theorem 7.1 supplies the homology groups; an explicitly credited published four-subset permutation module supplies the fourth-degree trace. Rational averaging justifies taking quotient invariants. The standalone exact checks are corroboration, not substitutes for the parameter-uniform proof.

## Originality — PASS, with residual risk

The same complex is called \(\operatorname{Cov}_{m,2}\) in Jonsson's paper and the two-subset Čech complex in Biswas's. Jonsson's Theorem 7.1 computes nonequivariant groups, while Biswas's §5.2 concerns an unproved nonequivariant homotopy splitting. The closest published equivariant study, *Four-subset sphere cycles give the rational top-homology permutation character of covering complexes* (identifier d06d65e27c16), establishes the complete degree-four module but explicitly leaves degree three undetermined. Targeted published mathematical findings searches included exact H3 transposition traces, equivariant covering complexes, two-subset Čech aliases, and quotient invariants. The fixed-face computation is a needed new input and was not found in the checked sources. The original older paper's entire PDF could not be inspected, and an unindexed equivalent result remains possible.

## Mathematical value — PASS

The theorem supplies the full \(C_2\)-module in degree three of a natural infinite family, and with the known fourth-degree module determines the rational homology of its geometrically canonical symmetry quotient. This distinguishes symmetry data not implied by Betti ranks and identifies the exceptional contribution of four-cycles in the fixed-face calculation. It may inform a future full symmetric-group character without falsely claiming one. No homotopy splitting, torsion classification or complete \(S_m\)-character is asserted.

## Reproducibility and limitations

`python3 verify.py` enumerates complete graph-cover examples and invariant simplices for the stated finite ranges, independently checking signed Lefschetz numbers and binomial consequences; `verify_output.txt` contains the real output. The all-parameter proof rests on the exhaustive two-hub classification, not empirical extrapolation. Full-text overlap risk for a paywalled original and possible unindexed equivariant literature remain documented.

Self-review: passed. Independent audit: not yet performed.
