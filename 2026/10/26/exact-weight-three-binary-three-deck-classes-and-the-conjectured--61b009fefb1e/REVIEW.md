# Scientific review

## Correctness: PASS

The complete three-deck is equivalent, for fixed length and exactly three ones, to the three counts of \(011\), \(110\), and \(001\). The first two restrict changes in one-positions to an integer one-parameter line. The third reduces to a quadratic with exactly one possible nonzero root, making every class at most a pair. The explicit orientation of that pair and its endpoint inequalities prove the coefficient and generating-function formula. The standalone verifier's complete enumeration through length 36 and formal-series comparison through 140 agree with the proof. This finite evidence is supportive, not the reason the infinite statement holds.

## Originality: PASS, with residual risk

The exact rational generating function appears **as a conjecture, not a theorem**, in Chrisnata et al. [1, Conjecture 1]. Section 5.3 of that same paper supplies the zero-vector kernel, a lower bound, and the first collision; none is claimed as new. What is newly established here is the exhaustive two-element collision classification and a proof of their complete all-length conjecture. General binomial-equivalence results [2] and newer unconstrained-deck asymptotics [4] do not imply that formula. An overlooked independent solution or terminology-equivalent statement remains possible; the evidence does not establish global uniqueness.

## Mathematical value: PASS

This resolves an explicitly formulated natural finite-word reconstruction conjecture and determines the exact codebook capacity for the fixed-weight-three, length-three scattered-read channel at every block length. The gap-swap involution gives a complete structural description, explaining each collision rather than only computing another small table.

## Sources and limitations

[1] Chrisnata et al., *On the number of distinct k-decks: Enumeration and bounds*, https://doi.org/10.3934/amc.2021032 (full text, §5.3, Conjecture 1).

[2] Lejeune, Rigo, Rosenfeld, *On the binomial equivalence classes of finite words*, https://arxiv.org/abs/2001.11732 (general and two-deck context).

[4] Nilforoushan, Parvaresh, *Improved upper bound on the number of distinct k-decks*, https://arxiv.org/abs/2609.23106 (unrestricted three-deck bounds).

Only binary words with exactly three ones and exact scattered length-three decks are covered. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
