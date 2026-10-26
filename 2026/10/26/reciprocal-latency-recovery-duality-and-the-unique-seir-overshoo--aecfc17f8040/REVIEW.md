# Scientific review

## Correctness — PASS

The exact growing-branch reduction, unique infectious peak, strict scalar comparison in the effective parameter \(\kappa\), and exact reciprocal change of compartments together prove the continuum theorem. The endpoint comparison and classical final-size equation prove the claimed supremum. The standalone symbolic checks and numerical replications in `verify.py` pass; they are corroborating checks rather than infinite-domain certificates. The proof explicitly excludes unmatched finite initial stage allocations.

## Originality — PASS (priority provisional)

The original Nguyen–Freedman–Ozbay–Levin SIR overshoot theorem supplies the sharp classical constant but not an SEIR infectious-peak stage-rate comparison. The full Heng–Althaus homogeneous SEIR analysis gives approximated peak curves rather than an exact reciprocal conjugacy. The full Dobie et al. SEIR timing paper addresses different stage-delay questions. Semantic searches of mathematical research findings for reciprocal stage rates, SEIR peaks, and epidemic overshoot did not recover direct statement-level coverage; priority outside the accessible corpus remains a limitation. Merely changing an established SIR parameter or restating SEIR invariants is not claimed as original.

## Value — PASS

Post-infectious-peak attack fraction is an interpretable burden relevant to interpreting epidemic peaks. The previously uncharacterized exact reciprocity and unique strict minimum at equal progression and removal rates are structural results across every supercritical reproduction ratio, with a sharp relation to the known SIR maximum; their value does not rely on an arbitrary numerical instance.

## Limitations and closest literature

The scope is deterministic homogeneous SEIR, exponential compartments, growing-mode infinitesimal seeding. Arbitrary finite unmatched initial exposed/infectious allocations, changing contact rates, and stochastic or network epidemic models are outside scope. Full comparison with all worldwide literature is impossible, and unidentified broader exact SEIR phase-curve literature is a publication-priority risk. Closest sources: Nguyen et al. (arXiv:2303.01650), Heng–Althaus (doi:10.1038/s41598-020-76563-8), Dobie et al. (arXiv:1909.11317).

Self-review: passed. Independent audit: not yet performed.
