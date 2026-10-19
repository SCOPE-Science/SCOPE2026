# Research review

## Correctness — PASS

The payoff difference was independently recomputed from both cooperator- and defector-conditioned hypergeometric sampling, including finite-population corrections and all boundary regimes. The balance equation makes the expected payoff difference exactly odd around the population midpoint. Reflection symmetry gives constant stationary mean; irreducible finite birth-death detailed balance reduces adjacent stationary likelihood ratios to neighboring transition probabilities. On the upper half, each ratio varies strictly with selection intensity in the claimed direction; accounting separately for the odd-population central pair yields strict likelihood-ratio order of absolute deviations, and variance and heterozygosity follow. The accompanying exact-rational checker confirms 3432 payoff identities, 2376 stationary checks, and 14139 distribution comparisons on a finite parameter family. The proof, not enumeration, establishes the infinite parameter statements. No erroneous extension to fitness-dependent mutation, absent exploration, or arbitrary return parameters is included.

## Originality — PASS, with residual risk

The motivating paper by Hauert and McAvoy (arXiv:2404.13728v1, first public 2024-04-21; journal DOI 10.1098/rsif.2024.0334) develops precisely the nonlinear public-goods return and finite-population Fermi/exploration model. Its examined main text provides equations, dynamical equilibrium conditions, and numerical stationary behavior; it does not state or prove this exact balanced-surface, finite-population, all-intensity **strict monotone-likelihood-ratio ordering**. Sandholm (DOI 10.3982/TE554) establishes general limit-order and stochastic-stability comparisons, but its 'stochastic dominance' concerns equilibrium-selection/risk dominance rather than this distributional ordering for fixed positive mutation. Ji and Wang (DOI 10.1088/1674-1056/20/3/030203) study a Moran rule and therefore do not cover the specified imitation transitions. Earlier work on general birth-death processes may contain a stronger sufficient condition that subsumes the adjacent-ratio argument; the work's distinguishing object-specific content is the exact hypergeometric balance condition and consequent full law. Priority cannot be certified from searching alone.

## Value — PASS

Selection strength is widely varied in finite-population evolutionary public-goods models, while conclusions drawn only from mean-field equilibria or plotted stationary modes do not imply distribution-wide ordering. This theorem supplies a robust comparison **for all positive exploration probabilities, all permitted population and interaction sizes, and every pair of intensities** on a naturally specified risk-balanced surface. It proves strict inequalities simultaneously for every polarization tail and for stationary variance/heterozygosity, and identifies a clean reversal between economies of scale and diminishing returns. That is a quantitative statement stronger than an example of increased polarization or a generic weak-selection approximation. The codimension-one restriction and the existing theory of reversible birth-death chains temper the scientific scope.

## Principal limitations and risk

The proof addresses only an exactly balanced and reflection-symmetric Fermi/imitation model with uniform exploration. A general stochastic-comparison theorem in the older probability or evolutionary-game literature could imply this theorem once its payoff gap is calculated; that is an unresolved but not presently decisive equivalence risk. No independent audit, external expert validation, empirical observation, or priority certification was performed.

Self-review: passed. Independent audit: not yet performed.
