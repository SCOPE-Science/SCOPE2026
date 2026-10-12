# Scientific review of the exact no-isolate NODF expectation

## Correctness — PASS
The statistic is defined as the average of lower-degree-normalized overlaps over unequal-degree row and column pairs. Inclusion–exclusion over columns counts all admissible matrices exactly. The row numerator uses a marked overlap; the column numerator uses a two-marked-column degree/overlap polynomial and excludes empty marked columns. Exchangeability then yields the full normalized mean. The denominator \(Z\) is strictly positive under the stated feasibility conditions. A separate exact-rational enumeration agrees on 305 full degree-profile cases, covering 145,503 matrices. Computation corroborates, but does not replace, the general proof.

## Originality — PASS, subject to stated residual risk
The nearest prior mathematics is the foundational definition and simulated null models in Almeida-Neto et al. (2008), the exact extremal NODF characterizations in Britton et al. (2016), the analytical **soft-constraint** mean in Payrató-Borràs et al. (2019), and the comparative **fixed-fixed/soft** null-model study in Bruno et al. (2020). The present uniform hard-row, no-isolate law is distinct from the soft independent-edge law and the fixed-fixed law; conditioning changes the distribution of random column degrees and of their degree ties. The inspected full texts do not give or imply this exact coefficient formula. A potentially unindexed exact formula for the same ensemble remains a risk; negative searches alone are not proof of novelty.

## Value — PASS
An exact null baseline is a directly relevant quantity for ecological NODF comparisons, where nonempty guilds, heterogeneous degree profiles and tied random column degrees complicate simulations. The result reduces an exponential ensemble to polynomially many exact coefficient updates, accommodates arbitrary row-degree heterogeneity, and supplies a reproducible benchmark without Monte Carlo error. It is not claimed to solve statistical calibration or fixed-fixed inference.

## Scope and limitations
The theorem concerns the expectation only, for binary degree-sorted NODF in the specified hard-row conditioned ensemble. All displayed denominators are nonzero; the time estimate is in exact arithmetic operations. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
