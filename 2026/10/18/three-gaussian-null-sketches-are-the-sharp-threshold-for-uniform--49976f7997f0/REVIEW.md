# Self-review

## Correctness — PASS

The analytical proof expresses the exact original-residual quotient as a monotone transform of the maximum of independent squared coordinates of rotationally invariant null lines. The beta near-zero expansion gives a necessary and sufficient moment condition \(K>2q\), and elementary integration gives the dimension-three sharp constant \(K/(K-2)\). The limiting one- and two-trial rates agree with the beta boundary-layer analysis. An exact integer matrix witness, fifteen independent quadrature comparisons, limiting integrals, and direct Gaussian-matrix checks passed in `verify.py`. Finite experiments corroborate but do not replace the theorem proof.

## Originality — PASS, with residual risk

The closest directly relevant full texts are Epperly, Park, and Nakatsukasa (2026, arXiv:2602.16797v1) and Park and Nakatsukasa (2023, DOI 10.1007/s10543-023-00979-7). Their inspected sketch-and-solve guarantees assume a full-column-rank embedding with at least as many sketch rows as columns; that premise fails for the one-row-short construction. Searches for beta, inverse-direction, repeated undersketched-nullspace, and rank-deficient best-of-sketch formulas did not find a published result covering the claim. Beta-coordinate and order-statistic laws themselves are classical and explicitly credited as proof components. General older randomized matrix approximation surveys might contain an equivalent implication; full-text coverage was not exhaustively excluded. No independent priority judgment has been made.

## Mathematical value — PASS

The number of repeats needed to make the expected quality of a minimal-row null-vector sketch stable is a natural algorithmic reliability cutoff. One and two repetitions have provably unbounded contrast-uniform expected relative squared residual, while three is the exact first count with a finite bound in every fixed dimension. The special case \(n=3\) yields the sharp constant 3 with transparent exact finite-contrast expressions. This is not a claim that existing full-rank sketch-and-solve methods fail, nor a runtime-complexity guarantee.

## Limitations and related literature

The singular spectrum has one small and otherwise equal singular values; the sketches are real, independent Gaussian and have exactly one fewer row than columns. Selecting the best null vector requires exact unsketched-residual evaluations, so no speedup is asserted. Finite precision and general spectra remain untreated. Full-length primary texts were inspected for the 2026 and 2023 papers. The broad Halko–Martinsson–Tropp (2011) survey was located by bibliographic record but not fully inspected; its possible implicit coverage remains a risk.

Self-review: passed. Independent audit: not yet performed.
