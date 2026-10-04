# Same-model review

## Correctness
PASS. The exact coordinate minimizer gives the stated cyclic sweep matrix. Its nonzero eigenvalues are a conjugate pair with known modulus and real part. Applying the Schur--Cohn criterion to the lifted constant-momentum modal polynomial yields the factor \((1-c)P_c(\alpha)\) exactly. The derivative argument proves that \(P_c\) is strictly decreasing on \([0,1]\), and Descartes' rule plus endpoint signs gives the unique quartic threshold. The two-block comparison follows independently from the real Jury conditions. The packaged checker reproduces the algebraic identities and representative root radii from the final files.

## Originality
PASS with a stated residual risk. The primary Chambolle--Pock source proves a two-block acceleration mechanism and discusses the difficulty of general cyclic acceleration but does not state this three-block stability boundary. Hong--Yavneh supply the general stationary-iteration momentum recurrence and complex-spectrum framework; that recurrence is treated as prior, while their inspected results do not state the exact spectrum or block-count phase transition here. The 2025 cyclic-BCD worst-case paper studies a different accelerated algorithm and reports deterministic inefficiency numerically, not this sharp global-before-sweep threshold. published-finding corpus searches returned related acceleration and Gauss--Seidel records but no implication-equivalent statement. The main residual risk is older extrapolated or semi-iterative Gauss--Seidel literature using different terminology.

## Value
PASS. The two-block versus three-block transition directly addresses a structural limitation highlighted by the primary source. It is not merely a recomputed convergence factor: the result identifies the first block count at which complex sweep eigenvalues make a natural global momentum extension unstable, gives the complete fixed-momentum stability test, and supplies an exact algebraic boundary. This provides a compact adversarial benchmark for deterministic cyclic acceleration and separates a genuinely safe two-block mechanism from a three-block obstruction.

Same-model review: passed. Independent audit: not yet performed.
