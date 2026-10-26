# Self-review: independent birthday laws for sparse histogram variation

## Correctness — PASS

For the iid uniform ordered-bin model, the deterministic identity \(2N-T=X_1+X_n+2Z\) holds exactly, and the difference between adjacent occupied-bin overlaps and adjacent sample-pair counts is bounded by an explicit triple-collision factorial moment. The two-color pair dependency graph has exact aggregate intensities and shared-index probabilities, so the process version of the Arratia–Goldstein–Gordon Poisson bound gives a rigorous bivariate total-variation error. Independent-set counting and Stirling surjections prove both extreme-value formulas. The finite verifier passed 75,160 checks; it corroborates but does not establish the infinite asymptotics. Risks are confined to interpretations outside the stated growth range and independent proof checking, not an unproved computational extrapolation.

## Originality — PASS with limitations

The inspected *Comb Test* paper provides a finite dynamic program but no uniform birthday-sparse limit. The inspected Part 1 gives expectations and mentions separate sparse/null-law work; Part 2 derives variance mainly at fixed bin count. The mathematical result on the same object in the proportional-occupancy regime does not imply this vanishing-occupancy bivariate Poisson law. The 1989 multivariate Chen–Stein theorem is an indispensable known proof tool and is not claimed as new. The remaining priority risk is substantive: an unlocated companion manuscript, or older near-birthday literature, might already contain the same model-specific specialization. Search absence is not proof of priority.

## Mathematical value — PASS

The birthday threshold is forced by the number of observation pairs, not chosen arbitrarily. The explicit finite TV bound characterizes the transition from a maximally oscillatory histogram to a non-Gaussian doubled-Poisson defect and then to independent Gaussian collision/variation fluctuations. Because both variables come from the same sample, their limiting independence provides a useful joint null calibration beyond separate marginal means/variances. The exact maximal-variation mass is a natural extreme-event invariant. Claims about power, nonuniform nulls, cyclic boundaries or larger samples are expressly excluded.

## Sources and limits

The scientific references are the 2026 Banić–Elezović Comb Test and its Part 1/Part 2 analytical sequels; Arratia, Goldstein and Gordon (1989) for the exact multivariate Poisson bound; and classical birthday-collision literature as background. The separate sparse and null-distribution manuscripts advertised by the authors could not be inspected as a located public document, so comprehensive historical priority is not certified. The finite programs use the standard library; no external certification or independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
