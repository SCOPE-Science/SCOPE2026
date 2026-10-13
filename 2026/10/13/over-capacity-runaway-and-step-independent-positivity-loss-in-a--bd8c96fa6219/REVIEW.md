# Self-review

## Correctness — PASS

The equations are transcribed from Gao (2026), equations (6) and (7), with \(A=r-b\) and \(K=k_2\). On the stated open wedge, signs of both derivatives make the wedge forward invariant for the ODE, and bounds \(u(t)\le u_0 e^{-\delta t}\), \(v_0e^{\theta t}\le v(t)\le v_0e^{cf t/d}\) establish global existence and integrability of the exact rate deficit. The logarithmic asymptotic constants follow from that identity and L'Hôpital's rule. The Euler proof gives a strict geometric lower bound until the first nonpositive prey iterate, whose existence follows from the same prey multiplier; no invalid extension through a negative state is used. A standard-library checker confirms the rational witness and verifies its finite simulation within the analytic bound. The theorem does not infer an infinite-horizon statement from this finite experiment.

## Originality — PASS

The exact motivating primary full text covers local equilibrium stability, flip and Neimark–Sacker bifurcations and finite numerical trajectories; its statements do not imply the unrestricted open overcapacity runaway region or its exact asymptotic rates and the complementary step-size-independent finite-positivity failure. Semantically focused prior-search checks find related but non-identical Smith-growth predator–prey systems, including Bai–Zheng–Kang (2024), whose predator–prey equations are different and whose consulted primary abstract does not state this source-specific phenomenon. Elsadany et al. (2026) use Smith growth in prey and a different response. Similar keywords or generic Euler positivity cautions do not imply these simultaneous conclusions. Full text for Bai–Zheng–Kang was unavailable from the consulted source, so possible deeper connections remain a residual risk; failed searches alone are not novelty proof.

## Value — PASS

This is a structural, parameter-independent boundary in the newly published ecological equations: above carrying capacity, low prey reverses density feedback, yielding a precise predator asymptotic and a superexponential prey decline. The same mathematical input has no globally nonnegative forward-Euler realization for *any* fixed positive step, despite small-step restrictions. That exact continuous/discrete discrepancy is materially relevant to interpreting the model's bifurcations, numerical long-run trajectories, and admissible biological state domain. No empirically realistic runaway population is asserted, and the theorem does not overturn any local equilibrium calculation.

## Closest literature and limits

Gao (2026), DOI 10.1155/jom/9152254, full text and equations (6)–(7). Bai–Zheng–Kang (2024), DOI 10.3934/dcdsb.2023161, accessed abstract/metadata but not primary full text. Elsadany et al. (2026), DOI 10.28924/2291-8639-24-2026-165, accessed abstract/metadata. The finite replay is a spot check, not a general proof. Independent assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
