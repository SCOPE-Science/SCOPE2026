# Scientific review: stationary qubit phase-information optimum

## Correctness: PASS

The stationary reset channel contracts traceless differences, so its fixed point is unique. Directly solving the off-diagonal fixed-point equation gives the full-rank Bloch coefficient for every nonresonant phase. Substitution into the standard SLD qubit formula produces the displayed positive rational QFI. The exact reset-odds derivative has a polynomial with precisely one change in its ordered coefficient signs throughout the entire allowed phase range, including the half-turn boundary; Descartes' rule and endpoint signs prove the critical point unique and simple. The small-detuning polynomial scaling brackets this point and yields both sharp limits. Algebraic identities were checked symbolically, and an independent two-by-two SLD calculation agreed at 24 parameter pairs. No global fact is inferred from sampled values.

## Originality: PASS, with residual priority risk

Wald et al. (arXiv:2410.11497v1) establish the geometric steady-state mixture and identify quasienergy resonances, but their accessible complete preprint analyzes two-qubit correlations, concurrence and local quantum uncertainty, not the single-qubit stationary phase-QFI maximum. Their general stationary density-matrix formula is credited as a premise, and its specialization alone is not counted as new. The result here is the exactly one-root global optimal-reset classification and its punctured near-resonance universal law. Li, Tong and Bao (arXiv:2610.31249) give a general quantum-Fisher reset-response identity for a continuous-time dissipative generator, not an implication of the discrete-time parameterized polynomial. O'Connor and colleagues (DOI 10.1088/1367-2630/ad345c) examine sequential-measurement Fisher-information rates, which differ from stationary unconditioned snapshot QFI. Scientific searches also checked phase estimation, geometric reset ages and one-qubit reset parameter optimization; no exact matching claim was established. A possibly unlocated general optimization result remains a genuine publication-priority risk; absence of a returned match is not a uniqueness certificate.

## Mathematical value: PASS

For phase estimation from the stationary averaged state of a randomly reset gate device, reset frequency simultaneously trades off coherent phase accumulation and mixing. Proving one and only one best probability for every nonresonant phase removes an otherwise significant optimization ambiguity. The half-turn exact optimum and the singular linear-detuning / inverse-squared-information limits quantify opposite experimentally meaningful regimes. The result is a complete parameter classification, not just a single numerical optimum; its all-phase proof is structural and the singular scaling is not a generic consequence of a fixed-parameter derivative test.

## Boundaries and limitations

The result uses a pure equatorial reset state, a single phase gate, constant Bernoulli resets and no access to the reset history. It does not order finite-time, cost-normalized or trajectory-conditioned precision. The rank-changing identity-gate phase is explicitly excluded. Independent scientific audit and complete priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
