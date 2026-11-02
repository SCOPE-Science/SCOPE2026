# Self-review

## Correctness — PASS

The proof derives the method's scalar stability function from the Butcher coefficients, diagonalizes the reversible star generator into three invariant subspaces, and writes every endpoint-matrix entry explicitly. The strict decrease of \(F(x)=(1-r(x))/x\) gives positivity of all off-diagonal entries. The global lower bound \(r(x)\ge-(\sqrt2-1)/2\) establishes unconditional positivity when the rates are balanced and \(2\le m\le4\). For every \(m\ge5\), the two complementary cases \(z>3+2\sqrt2\) and \(z\le3+2\sqrt2\) give explicit negative hub or leaf diagonals. The irrational sign certificate is verified exactly. Independently implemented Runge–Kutta stages agree with the analytic expressions in the standalone verifier (2,827 assertions over symbolic identities and 420 randomized full matrix cases). The infinite quantifiers rest on analytic inequalities, not finite tests.

## Originality — PASS with bounded coverage risk

The precise claim is the smallest reversible star whose endpoint positivity cannot be made unconditional by any two homogeneous positive spoke rates, for Alexander's particular two-stage method. Horváth (1998) establishes broad positivity radii for RK/DSRK methods, but its full 18-page discussion of general dissipative problem classes and method-level radii does not give star-graph dimension/rate-tuning classification. Kocsis and Németh (2014, full 11-page preprint) optimize absolute-monotonicity radii over schemes, not within a fixed Markov generator family. Blanes, Iserles and Macnamara (2021/2022 preprint, relevant sections inspected) discuss a general positivity order barrier, not rate-dependent star endpoints. The Alexander (1977) full paper was unavailable; its accessible abstract and a documented tableau were inspected. Other integrator-specific star phenomena are not logically stronger statements for the Alexander stability function. General positivity barriers are uniform over all problems and do not negate the restricted-family existence at small \(m\). The full original 1977 text and any unindexed special-purpose analysis remain residual risks; no independent historical novelty certification is asserted.

## Mathematical value — PASS

Positivity of computed transition probabilities is a physical and probabilistic constraint that A/L-stability alone does not guarantee. The result provides a sharp six-state size obstruction *regardless of homogeneous spoke-rate tuning*, a positive all-timestep construction on every smaller star, and explicit counterexample timesteps with a strict negative margin. The proof also locates the only possible sign obstructions on the diagonal. This distinction between some-rate existence and all-rate failure is not implied by a generic Runge–Kutta SSP-radius calculation; it directly informs model-rate selection versus integrator choice.

## Limits

The classification is not for heterogeneous spokes or stagewise positivity, and it does not count all disconnected unsafe intervals. Publication overlap outside the accessible full texts is not excluded. Finite numerical tests are not substitutes for proof.

Self-review: passed. Independent audit: not yet performed.
