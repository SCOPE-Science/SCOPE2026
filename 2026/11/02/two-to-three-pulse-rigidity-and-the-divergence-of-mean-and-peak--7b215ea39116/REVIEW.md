# Scientific review

## Correctness — PASS

The affine return map contracts by the strict factor \(e^{-\mu T}\prod_i(1-p_i)\); a unique periodic susceptible profile exists. The deficit recurrence gives exact post-pulse formulas. For two pulses, direct integration reduces mean susceptibility to a strictly minimized \(x+E/x\) expression, and monotonicity of two pre-pulse deficits gives a unique crossing and exact peak optimizer. For three pulses the first variation is computed on the constraint \(xyz=E\), not by wrongly holding all three gaps independent. The two derivative identities vanish jointly only for equal strengths. The symbolic checks and exact rational witness in the attached program reproduce the critical computations. A finite numerical parameter sweep is supplementary, not an infinite proof.

## Originality — PASS (historical priority provisional)

The full 2010 Terry paper studies vaccination across distinct patches and explicitly defines one fixed-fraction pulse per patch. The inspected 2013 Browne–Smith–Bourouiba work compares regional pulse synchrony and different vaccination resource constraints; the inspected 2015 Doutor–Rodrigues–Soares–Chalub paper optimizes effort under seasonal infection risk. None of the inspected material states or visibly implies the combined all-parameter two-pulse mean/peak dichotomy and the sharp three-pulse equal-spacing stationary criterion. published-finding corpus searches for the precise scheduling claims yielded no directly equivalent record; closest hits concern different waiting-time laws or multi-group stability. Absence of a discovered theorem does not establish uniqueness in literature. Possible uninspected general impulse-optimization theorems remain a historical-priority risk.

## Value — PASS

The result gives a complete closed-form answer to two distinct policy-relevant timing objectives under the precise fixed-fraction protocol and establishes a structural two-to-three campaign boundary. It shows that the universally valid mean-invasion half-period rule does not transfer to peak-risk optimization, and that it stops being a stationary rule when a third unequal-strength campaign is allowed. These observations help separate mean growth thresholds, instantaneous growth peaks, and vaccine-budget constraints. It is not claimed to solve optimization under a fixed dose budget or realistic multi-class epidemic models.

## Closest literature and residual limitations

Terry (2010), DOI 10.3934/mbe.2010.7.455; Browne et al. (2013), arXiv:1309.0265; Doutor et al. (2015), arXiv:1507.02940. Broader impulse-spacing/control results may subsume the formula despite not appearing in compared texts. Exact mean-invasion and peak-instantaneous growth quantities are surrogate objectives, not full nonlinear outbreak outcomes. Individual campaign dose counts are generally not fixed when timing varies.

Self-review: passed. Independent audit: not yet performed.
