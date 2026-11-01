# Research review

## Correctness

**PASS.** The theorem reduces every labelled initial configuration to six homogeneous initial-color cohorts; replacing each cohort size by zero, one, or at least two preserves the exact threshold-two excitation decision at each update. Absent cohorts are masked, so the six-coordinate recurrence preserves the exact labelled least period and first-periodic-entry time. The `certificate.tsv` exhausts all 676 allowed signatures, and `verify.py` regenerates each row, checks the sharp size table, and tests the direct labelled rule on 73,449 configurations. The infinite family follows from the reduction rather than from finite-size extrapolation. The ordinary fixed-point and orbit-count formulas are independently checked by multinomial sums and arise from the three recurrent signature types.

## Originality

**PASS, qualified.** Fisch–Gravner–Griffeath introduced threshold GH models in 1991; the inspected full-text portions concern lattice wave phenomena. Gravner–Lyu–Sivakoff's arXiv:1610.07320v1 addresses threshold-one finite graphs, while Bello–Sivakoff's arXiv:2108.06404 studies threshold-at-least-two on infinite regular trees. A previously available threshold-one biclique classification has different excitation criteria and orbit-count formulas; a threshold-two crown-graph result concerns a different graph and supports periods absent on bicliques. Actual published-finding corpus and literature searches did not identify an implication or equivalent exact threshold-two biclique classification. The original journal-era source was not read in its entirety, and unindexed equivalents remain possible.

## Mathematical value

**PASS.** The sharp, independent onsets at shore sizes four and six separate two kinds of sustained excitable-wave oscillation, while every other initial condition settles in no more than five iterations. Closed primitive-orbit formulas, an explicit all-transient coefficient census, and the overwhelmingly immediate period-three regime for large shores constitute a motivated complete infinite-family dynamic classification rather than a minor numerical increment.

## Verification boundaries

The exhaustively checked finite transition certificate is a mathematical proof component only because the exact homogeneous-cohort reduction covers every graph size. The 73,449 direct trajectories are supplemental checks, not themselves a proof of the infinite statement. Independent review and universal historical originality are not claimed.

Self-review: passed. Independent audit: not yet performed.
