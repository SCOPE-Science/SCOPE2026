# Self-review

## Correctness
PASS. The source defines \(\pi_g=x\pi_{gs}+(1-x)\pi_{gw}\) and \(\dot x=x(\pi_{gs}-\pi_g)\), so \(x(1-x)\) follows by exact algebra. The same identity applies to the victim coordinate and the source explicitly prints \(z(1-z)\) in Eq. (17). The source then deletes complement factors before Eqs. (19)–(21). At its baseline \(B_g=3\), \(C_g=2.5\), \(C_{\mathrm{weak}}=1.5\), Eq. (19) gives the exact outward normal velocity \(2\) at \((1,0,1)\), proving failure of forward invariance.

## Originality
PASS. published-finding corpus searches using the exact DOI, “dropping 1-x 1-y 1-z,” “probability cube invariance,” and the boundary/equation context returned no record implying this source-specific correction. The motivating full text was inspected through the payoff construction, simplification step, stochastic-model setup, and baseline parameter table. Comparison literature retains the standard complement factors but does not identify this paper's concrete boundary failure.

## Value
PASS. The defect changes the mathematical state space: variables explicitly interpreted as probabilities can leave \([0,1]\), and pure-strategy faces that are invariant under replicator dynamics cease to be invariant. This directly affects the meaning of boundary stability and probability-valued numerical trajectories, so the correction is a structural boundary result rather than a cosmetic normalization or notation check.

## Closest literature and limitations
The closest inspected comparison is a 2026 tripartite evolutionary-game model in *Mathematics*, which writes all three coordinates with \(x(1-x)\)-type factors. A 2021 public-health tripartite model likewise retains them. These establish the standard formulation but do not cover the exact Su–Long boundary witness. The result does not claim every interior equilibrium is changed, and it does not rely on resolving the later paper's inconsistent Brownian notation.

Self-review: passed. Independent audit: not yet performed.
