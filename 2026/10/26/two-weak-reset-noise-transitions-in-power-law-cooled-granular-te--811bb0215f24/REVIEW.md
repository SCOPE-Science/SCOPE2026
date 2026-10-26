# Self-review

## Correctness — PASS

Stationary Poisson age and independence of future resetting imply the exact two-time covariance, strictly positive by the paired-difference identity for two decreasing nonconstant functions. Exponential covariance decay justifies Green–Kubo integration. Complete inter-reset intervals carry the iid centered rewards \(F(L)-m_rL\), which have all required moments; the regenerative reward CLT gives the variance rate. All five correlation-time regimes arise from independently derived three-regime static variance and three-regime integrated variance asymptotics. The crucial \(\alpha=1\) and \(\alpha=1/2\) logarithmic borders are handled separately. Seven numerical covariance/reward comparisons and two weak-reset checks are reproducible from `verify.py`. Risk: the model is a deterministic macroscopic temperature under exponential complete resets; no microscopic noise or joint-limit claim is proven.

## Originality — PASS (bounded evidence)

Bodrova–Chechkin–Dubey (arXiv:2403.18974), examined in its model, stationary-moment and conclusion sections, establish the cooling/reset stationary one-time laws. Evans–Majumdar–Schehr (arXiv:1910.07993, section 5.1) establish general two-time reset identities; their application and specialization alone would not be new. The distinct content is the exact Poisson-age temperature covariance, the evaluated Green–Kubo rate and its divergent low-rate regime, plus all five sharp normalized-correlation-time equivalents. Published mathematical-record searches using the source identifier, aliases, singular exponents and Green–Kubo vocabulary did not return an identical claim; the closest relevant renewal-age result concerns age/residual-power correlations, a different functional. An unrecognized general published renewal asymptotic theorem could subsume the new special case; search absence is not proof of novelty.

## Mathematical value — PASS

The exact Haff-type law already specifies temperature relaxation under resetting, so the experimentally interpretable remaining question is the reliability of integrated temperature measurements. The theorem identifies a noncommuting low-reset versus long-observation noise effect: vanishing one-time variance can coexist with divergent per-time accumulated variance. Its thresholds distinguish integrability of the cooling profile from square-integrability and supply a complete non-arbitrary regime classification, including concrete Haff and viscoelastic specializations. It is not a generic exercise simply reparametrized, though future physical validation would be needed.

## Closest literature and limits

Primary comparison: Bodrova–Chechkin–Dubey, arXiv:2403.18974. General two-time machinery: Evans–Majumdar–Schehr, arXiv:1910.07993. Regenerative CLTs: Glynn–Whitt (1993). The present work does not claim novelty for the underlying stationary one-time distribution, general renewal CLT, or generic reset covariance decomposition. Priority against all broader renewal results is not proven.

Self-review: passed. Independent audit: not yet performed.
