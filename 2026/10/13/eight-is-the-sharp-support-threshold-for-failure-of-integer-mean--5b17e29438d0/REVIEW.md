# Scientific review: sharp support threshold for integer-mean medianity

## Correctness — PASS

The theorem's domain is finite, contiguous-support integer-valued log-concave probability mass functions with integer expectation. The discrete localization theorem of Marsiglietti and Melbourne (arXiv:2004.12005, Theorem 2.10) applies to the linear upper-tail objective under the half-space condition \(\mathbb E X\le m\), and reduces the maximum to a truncated geometric distribution on a subinterval. Every interior integer mean position for every subinterval of length at most seven is one of the 15 enumerated pairs. Strict monotonicity of the geometric mean and upper-tail probability in \(\log q\) converts each pair of exact rational signs into a strict sub-half bound. Reflection supplies the other tail. The eight-point counterexample is specified by an exact polynomial root, and rational endpoint signs plus monotonicity ensure the mean and failure without numerical rounding.

The delivered `verify.py` passes all 15 exact fraction sign certificates and the eight-point root bracket. This checks finite algebra, not the general localization theorem, whose published proof was separately inspected. The claims require no extrapolation from finite distribution sampling. Unproved limits: no uniform margin above half and no claim for noninteger expectations or support lengths at least eight.

## Originality — PASS, subject to bibliographic risk

The 2022 initial preprint by Alqasem, Aravinda, Marsiglietti and Melbourne (arXiv:2208.12702; inspected full arXiv HTML v2) provides the general \(e^{-1}\) inequality and an eight-point counterexample to the one-half strengthening. It does not claim or establish the *smallest* support on which failure can occur. The 2020 paper by Marsiglietti and Melbourne (arXiv:2004.12005; inspected full arXiv HTML v4) provides the localization reduction, but does not list or derive the 15 finite exact sign comparisons or the seven-point universal consequence. Existing related distributional and location-theory claims were compared at the level of mathematical implication; they do not imply the seven-point theorem.

The full text of Alqasem's 2024 dissertation, *Deviation Inequalities for Discrete Log-Concave Distributions*, was not obtained. Its available abstract concerns the general Feige bound and discrete gamma-concavity; an unindexed seven-point result, there or elsewhere, remains a priority risk. Search failure is not a proof of novelty. The known eight-point counterexample and the published localization theorem are explicitly credited; only the sharp minimality conclusion is proposed as a new contribution.

## Value — PASS

The motivating paper explicitly exhibits a support-eight failure of the often-valid one-half inequality at an integer mean, without determining whether eight is necessary. Establishing the exact first admissible support size is a natural, complete classification of the finite-support threshold, not an arbitrary numerical slice: it pinpoints where the median guarantee ceases to hold for all log-concave distributions. This has a concrete interpretation in discrete small-deviation/median comparisons. The finite calculation is substantial only in conjunction with the exact, general localization reduction and the mathematical motivation; no greater downstream general theorem is asserted.

## Scope and limitations

The four-way priority comparison covered equivalent mean/median formulations, stronger general concentration statements, existing tables/databases, and implication from both primary papers. The full-text dissertation limitation and possible earlier equivalent result under different terminology remain. The result has received the self-review only. No independent mathematical, bibliographic, or priority audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
