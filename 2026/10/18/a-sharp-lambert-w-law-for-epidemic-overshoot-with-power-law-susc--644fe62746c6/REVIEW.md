# Review of the power-law epidemic-overshoot theorem

## Correctness — PASS

The claim is explicitly restricted to homogeneous closed SIR outbreaks with real \(p\ge2\) and the vanishing-infection-seed limit. The conserved quantity gives \(q=(1-s)/\int_s^1u^{-p}du\); the susceptible fraction at the unique prevalence maximum is \(q^{1/p}\), and a strictly concave final-size equation selects the nontrivial solution. The resulting peak-to-final gap is an inverse-power mean minus its left endpoint, which proves strict monotonicity in the exponent. The separate small-\(s\), near-one, and intermediate-band bounds justify uniform localization and the \(o(1)\) error in \(pM(p)=W((p-1)/e)+o(1)\). Symbolic checks at \(p=2\), comparison at \(p=3\), and the supplied numerical script corroborate critical identities but are not substituted for the proof.

## Originality — PASS with recorded risk

Nguyen (arXiv:2303.01653, first public 2023-03-03) analyzes fixed nonlinear incidences and explicitly evaluates the cubic case. The 2024 journal version states a general numerical/analytical recipe and qualitatively observes smaller maxima for steeper functions; neither inspected text states or implies the strict, all-real-exponent ordering together with its sharp Lambert-\(W\) two-term asymptotic. Nguyen et al. (arXiv:2303.01650) covers the bilinear case. Indexed searches returned results on SIRS equilibrium bifurcations and unrelated Lambert-\(W\) asymptotics, not this exact SIR worst-overshoot invariant. The journal's separately linked supplemental PDF was not accessible in the attempted retrieval; the earlier open preprint contains the relevant cubic derivation. This remaining material-access risk is not a demonstrated covering implication.

## Value — PASS

The maximized post-peak fraction is a natural, dimensionless epidemic burden quantity; comparing the maxima across nonlinear incidence exponents is motivated by the published question of how incidence steepness changes overshoot. The theorem gives an actual universal monotone law and resolves its large-exponent limiting scale, including a nontrivial logarithmic correction. It is not a re-expression of the already known single-exponent cubic or bilinear calculations. The scientific scope remains mathematical: it does not claim accuracy for network epidemics, stochastic epidemics, fixed-parameter comparisons, or large initial seeds.

## Reproducibility and limitations

Run `python3 verify.py` to reproduce the finite checks. The universal and asymptotic quantifiers rely on the proof, not the script. Unindexed literature and the inaccessible 2024 supplement are residual originality risks; the strength of the claim is limited to the precise model and vanishing-seed regime.

Self-review: passed. Independent audit: not yet performed.
