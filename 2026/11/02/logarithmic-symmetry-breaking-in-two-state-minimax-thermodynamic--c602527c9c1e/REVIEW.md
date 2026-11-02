# Scientific assessment

## Correctness — PASS

The binary channel transition probabilities and exact entropy functional follow directly from the two-state generator. An independent minimax argument uses the KL contraction identity, nonnegative conditional entropy and the unique interior entropy maximizer. Strict concavity is proved from total variance. The fixed-rate \(1/\log(1/t)\) optimizer is bracketed by the signs of the exact derivative, and a uniform local entropy expansion establishes the full \(o(t)\) error in the optimum. The balanced formula is exact; the variable-rate crossover uses uniform compact expansions and a unique limiting maximizer. A high-precision verifier evaluating both joint-distribution and channel expressions passed 76 checks. Numerics do not establish the infinite limits.

## Originality — PASS (best-knowledge, qualified)

The closest source, Yousef–Ansbacher–Wolpert, arXiv:2610.03478 (2026), contains the same minimax objective, the established leading maximum-escape-rate coefficient, and convergence of optimal priors toward the fastest state. Its main derivation and the continuous-time supplemental Section SX were inspected. They do not supply the negative logarithm-of-logarithm correction, the sharp optimal prior scale, or the near-degenerate rate crossover. Khouzani–Malacaria (2018) treat optimization of channels for a given input prior, rather than optimization over input priors of a fixed Markov channel. Dedicated record and literature searches did not surface a dominating exact two-state small-time result. Absence from search results is not proof of global novelty. Binary-channel formulas are longstanding and explicitly credited.

## Value — PASS

The source's leading short-time estimate cannot determine how fast the optimal design prior approaches its singular limit or quantify the first correction to the robust thermodynamic penalty. This result supplies both a parameter-dependent mass law and a universal logarithm-of-logarithm cost penalty, and resolves the practically motivated near-symmetry boundary layer where the fixed-gap expansion ceases to be informative. The change from a uniform prior at equal rates to a slowly vanishing minority mass under fixed rate imbalance is a structural singular perturbation, not merely an isolated parameter evaluation.

## Limits and priority risks

A two-state chain is reversible at stationarity, so this does not describe nonzero housekeeping entropy production; the object is thermodynamic *mismatch*. The source provides the minimax identity and leading behavior. Independent review is needed to rule out equivalent binary-channel asymptotics in older information-theory work. The cited 2018 channel-design paper does not dominate the statement, but the general topic of optimal posterior entropy has a longer history. No uniform crossover for growing perturbation parameter is established.

Self-review: passed. Independent audit: not yet performed.
