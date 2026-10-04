# Same-model review

## Correctness
**PASS.** For any proposed two-vertex side, the two alternating color-vector classes control orderability exactly: if both are present they form an alternating four-cycle obstruction, while if one is absent an explicit vertex ordering works. In the red-Hamilton-cycle witness on \(K_{t+2}\), both classes are nonempty for every pair when \(t\ge3\), proving the universal lower bound. Li's published upper bound then matches it at \(t=4,5\). The bundled verifier directly tests the cycle witnesses and independently enumerates all vertex orders for the smallest cases.

## Originality
**PASS.** The initiating 2026 paper was inspected in the relevant complete-bipartite sections and searched for the exact \(K_{2,4}\), \(K_{2,5}\), and cycle-lower-bound formulations. It supplies the upper theorem, asymptotics, and infinitely many algebraic exact cases, but no statement covering these two small exact values was located. The closest 2025 small-value paper includes \(K_{2,4}\) in computations for other canonical target pairs and no \(K_{2,5}\) case was located. published-finding corpus, exact-formula, alias, and own-ledger searches found no implication-equivalent result. Residual risk remains for differently phrased or unindexed literature.

## Value
**PASS.** The two exact values are natural low-parameter cases of newly introduced graph Ramsey invariants, and they are obtained by a simple structural construction that simultaneously gives a general lower bound. The result closes a genuine lower/upper gap at \(t=4,5\), rather than reporting a routine recomputation.

## Closest literature and limitations
Li's Theorem 1.8 is the decisive prior upper bound. Brosch–Lidický–Miyasaki–Puges is the closest small-value computational literature inspected. The universal \(t+3\) lower bound is not claimed asymptotically sharp, and the exact conclusion is restricted to \(t=4,5\). No independent audit has been performed.

Same-model review: passed. Independent audit: not yet performed.
