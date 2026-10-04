# Same-model review

## Correctness

**PASS.**  Below \(p=1/2\), an explicit exact degrading channel reproduces the complement.  Above threshold, unitary covariance and block pinching reduce the degrading map to a depolarizing data block plus an invariant flag response.  The maximally entangled input yields a lower bound depending on two nonnegative scalars \(A,B\); its exact piecewise minimization is \(2A(1-d^{-2})\), and complete positivity forces \(A\ge2p-1\).  The proposed degrading map attains equality and leaves \((2p-1)(\operatorname{id}-\mathcal R)\).  The exact diamond norm \(2(1-d^{-2})\) is certified by the same maximally entangled input and a matching Choi-SDP feasible bound.  Supplementary rational checks replay successfully.

## Originality

**PASS, narrowly scoped.**  Sutter--Scholz--Winter--Renner define the quantity and its SDP but the inspected full text has no erasure-channel specialization.  The later Siddhu--Tayur tutorial passage checks only \(p\le1/2\), where the defect is already zero, and notes antidegradability above.  Focused database and web searches did not locate the positive-half closed formula \(2(2p-1)(1-d^{-2})\) or its explicit optimizer.  The accepted originality claim is restricted to this analytic erasure-channel evaluation.

Residual risk: the derivation is short after exploiting covariance, so an equivalent formula could occur in notes, notebooks, or unindexed discussions.  No broad priority claim is made.

## Value

**PASS.**  The result evaluates a canonical SDP benchmark in closed form for every input dimension and every erasure probability, including the entire antidegradable half where the defect is nonzero.  It supplies an explicit optimizer and a dimension-dependent exact value, making it directly useful for validating approximate-degradability solvers and for inserting a sharp error parameter into general capacity bounds.

Same-model review: passed. Independent audit: not yet performed.
