# Scientific review

## Correctness — PASS

The proposed theorem is quantified for each strictly positive diffusion coefficient, on-state relaxation rate, and symmetric switching rate under joint stationary initialization. The conditional stationary characteristic functions solve the two coupled generator equations; independent gamma-difference and Gaussian variables represent the resulting positional law. Direct generator substitution confirms the bounded-jump Poisson corrector, and its exact martingale bracket establishes the variance coefficient. Stationary ergodicity, a fixed jump bound and finite fourth moments justify the martingale central limit theorem and boundary-term removal. A positive-probability single-switch construction proves divergence of the work exponential moment separately for each sign of the tilting parameter. Exact algebra, transform identities and independent finite-sample simulations are reproduced by `verify.py` (4 rational parameter checks, 18 transform identities and 3 simulations). Numeric simulations do not prove either asymptotic limit.

## Originality — PASS, qualified

The base on/off trap and its stationary distribution and rate-independent mean thermodynamic flux were previously established, including by Frydel (arXiv:2407.12213v1). Santra, Das and Nath (arXiv:2104.00609) establish positional and first-passage results; Alston, Cocconi and Bertrand (arXiv:2202.02630) discuss nonequilibrium mean thermodynamic behavior. Frydel's broader 2026 semi-Markovian formulation (arXiv:2607.05173, section III.2) identifies mean injected power, not the present time-integrated work fluctuation law. Classical Markov-additive-functional limit theorems explain a possible proof strategy but do not themselves give the explicit variance rate or universal divergence of both work exponential moments in this model. Targeted literature and mathematical-record searches found no direct statement implying the complete claim. This is evidence of a gap, not a certification of novelty; uninspected fluctuation-theorem literature and equivalent tilted-generator formulations remain residual priority risks.

## Mathematical value — PASS

The time-integrated stochastic work is the physical input needed to maintain a nonequilibrium alternating trap. Previous stationary means are independent of switching rate, while the exact variance rate diverges as switching becomes slow and retains a strictly positive fast-switching floor. The combination of a conventional central limit theorem and the absence of *any* finite bilateral exponential moments is a substantive structural boundary for fluctuation-theorem and large-deviation methods. This is a natural full-observable statement for the original model, not an arbitrarily sliced moment calculation.

## Closest literature and limits

The relevant comparison is between stationary one-time distributions or mean injected power and the complete fluctuation law of an additive work observable. The 2013 work-fluctuation treatment by Pal and Sabhapandit concerns a continuously fluctuating *trap location*, not the Poisson on/off *trap stiffness*. The theorem does not establish a full large-deviation principle, nor extend to asymmetric or non-Poisson switching. Independent priority and scientific audits remain unperformed.

Self-review: passed. Independent audit: not yet performed.
