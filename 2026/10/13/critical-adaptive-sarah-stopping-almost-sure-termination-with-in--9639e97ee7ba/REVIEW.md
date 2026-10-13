# Self-review

## Correctness — PASS
The specified two-component quadratic has component curvatures \(1\) and \(6\), giving signed recursive-gradient multipliers \(1/2\) and \(-2\) at step \(1/2\). Their log-magnitudes form a fair nearest-neighbor walk; the squared gradient threshold \(1/4\) is precisely first passage to \(-1\). Reflection/Catalan enumeration gives a unit total hitting probability and the heavy-tailed odd hitting-time law with infinite expectation. The explicitly defined, disjoint strings with \(h\) expansions followed by \(h+1\) contractions have probability \(2^{-(2h+1)}\), and their stopped signed sums force squared output at least \(4^h x_0^2\), yielding divergent expectation. The same strings give the capped lower bound. The exact-rational verifier checks finite examples; infinite conclusions are proved separately. Boundary: \(x_0\ne0\), a single inner pass, exact arithmetic, and a deliberately nonconservative step.

## Originality — PASS, with residual priority risk
The original SARAH+ text includes the norm-ratio test **and a finite hard cap**, but does not establish the displayed first-passage law, infinite uncapped mean work/risk, or growing capped-error lower bound. The published last-iterate and probabilistic SARAH variants rely on different scheduling or safe-step assumptions; their conclusions do not imply this pathology. Indexed closely related material addresses distinct gradient methods, stopping-time bias, or quadratic instability, not this stopped estimator and objective. The elementary Catalan enumeration itself is classical; originality is confined to its coupling with signed SARAH estimator paths and the risk/cap implications. A matching analysis in unindexed papers or informal literature cannot be excluded.

## Value — PASS
Adaptive gradient-norm criteria are intended to bound inner work, and the defining paper expressly retains a hard cap for robustness. This example quantifies why a gradient-estimator threshold alone can be unreliable: almost-sure termination does not even ensure finite mean work, and the returned objective has infinite expectation although full-gradient descent at the same step contracts. The finite-cap growth lower bound makes the tradeoff operationally concrete. The result is not a claim that the original capped algorithm is ill-defined or that its established small-step guarantees fail.

## Closest literature and limits
Nguyen et al., *SARAH*, arXiv:1703.00102 (Algorithm 2, Section 4); Li et al., *On the Convergence of SARAH and Beyond*, arXiv:1906.02351 (last-iterate and loopless analyses); Zhong et al., *Probabilistic Guarantees of Stochastic Recursive Gradient*, arXiv:2401.15890 (different modified algorithm). Remaining risk: possible equivalent unindexed two-curvature stopping-time analysis. No independent review of the result has been performed.

Self-review: passed. Independent audit: not yet performed.
