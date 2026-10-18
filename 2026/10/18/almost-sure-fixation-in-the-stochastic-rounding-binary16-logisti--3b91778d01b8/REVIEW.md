# Scientific review

## Correctness — PASS

The defined Markov transition semantics is exact-real polynomial evaluation followed by one unbiased stochastic rounding, with positive probabilities on its one/two bracket outputs. The companion standard-library checker enumerates all \(15{,}361\) binary16 states with exact fractions, constructs all \(30{,}623\) positive-probability edges, and exhaustively computes SCCs and directed reachability: exactly two terminal singleton SCCs, \(0\) and \(3/4\), with exact reachability partition. Standard finite-Markov-chain recurrence proves almost-sure absorption. Proof is limited to this explicitly defined arithmetic semantics; finite graph exploration suffices because the state space is fully exhausted.

## Originality — PASS, subject to identified priority risk

Klöwer et al., *Periodic orbits in chaotic systems simulated at low precision* (initially public 8 November 2022; peer-reviewed 2023) empirically document transient benefits of stochastic rounding and mention Bernoulli-map stochastic collapse, but do not state the exact two-absorber stochastic logistic \(r=4\) theorem. Related deterministic binary16 logistic census covers a different, one-output functional graph, so it implies neither the two absorbing recurrent classes nor the mixed stochastic absorption partition. Targeted published-record and literature searches revealed no equivalent classification. The search is not a proof of global historical uniqueness. Primary-source arithmetic-order differences prevent treating their implementation as identical to the explicitly defined one-rounding model.

## Mathematical value — PASS

The fixed parameter \(r=4\), IEEE binary16, and ideal unbiased stochastic rounding are canonical rather than arbitrary slices. The complete result resolves a motivated question left open by simulation-based demonstrations: whether stochastic rounding preserves nonperiodic behavior indefinitely. It shows almost-sure fixed-point absorption, and identifies the exact reachability partition, thus distinguishing short-run accuracy improvements from long-time recurrent structure. This is a natural complete finite-state classification; no general theorem beyond the specified arithmetic semantics is claimed.

## Closest literature and boundaries

The 2022/2023 Klöwer–Coveney–Paxton–Palmer work contains the same base logistic polynomial and both deterministic and stochastic rounding, but provides qualitative or experimentally observed effects, not this graph's exact recurrent classes. A prior deterministic binary16 orbit census is scientifically related but does not imply the stochastic result. A possible unpublished equivalent graph computation and intermediate-operation convention differences remain residual priority and applicability risks. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
