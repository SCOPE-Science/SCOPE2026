# Scientific review

## Correctness: PASS

The small-market lemma has a direct blocking-pair proof: in a three-pair stable matching without a first-choice recipient, a third-choice recipient would force two other men to rank one woman first, forcing that woman to receive her first choice, contradiction. Thus every such stable matching assigns everyone second choices; the other stable matchings have minimum rank one. Under positive Borda coding the two gap measures are strictly increasing in the same worst rank, giving identical weak rankings through three pairs. A four-value arithmetic table proves nonreversal and the common-optimum property at four pairs. The complete explicit witness has only the two stated stable matchings, with differences \(2,2\) and ratios \(2,3\). The standalone verifier exhaustively checks all strict profiles through three pairs and all four-pair witness bijections. The finite computational checks are not substituted for the universal structural proof.

## Originality: PASS, with residual risk

Sheng and Yokoi (arXiv:2607.07160, July 8, 2026) define and solve both utility-gap optimization problems. Their general polynomial-time solvability results do not imply the pairwise coincidence of the two induced weak orders under fixed positive Borda utilities, or the sharp four-pair separation. Their appendix nonrepresentability/submodularity examples use different value functions. Related stable-marriage records concern egalitarian, regret, sex-equal or rank-maximal objectives and do not establish this difference-versus-ratio relation. Targeted published mathematical-record and literature comparisons found no equivalent, but incomplete indexing and unexamined older literature retain priority risk.

## Value: PASS

The two objective functions introduced in the motivating work are natural but generally different fairness notions. The theorem establishes the exact smallest complete strict Borda-scored stable-marriage market where substituting one for the other changes the set of admissible optimal solutions; its structural blocking-pair lemma and no-strict-reversal frontier explain the boundary rather than merely reporting a computational coincidence. Even with exactly two stable matchings the distinction matters when a mechanism returns every difference-optimal outcome. The result is deliberately limited to a meaningful natural scoring model, without extrapolating beyond it.

Self-review: passed. Independent audit: not yet performed.
