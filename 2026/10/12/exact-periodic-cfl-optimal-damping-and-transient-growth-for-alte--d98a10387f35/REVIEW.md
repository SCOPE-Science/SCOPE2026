# Scientific review

## Correctness — PASS
The variable-step AB2 extrapolation was reconstructed from physical-time interpolation rather than inferred from a constant-step formula. Exact multiplication gives \(\operatorname{tr}P=1-L+L^2/2+xy/4\) and \(\det P=xy/4\). Schur inequalities classify the entire open stability region and both boundaries. Real nonnegative roots and a strict monotonicity derivative prove unique damping optimality. At \(x=y=2/3\), the map equals \(I/3\). A rank-one matrix limit proves the exact unbounded-transient law. The accompanying checker independently performs exact rational and floating tests; universality follows from the written proof, not sample enumeration.

## Originality — PASS, with residual historical risk
The classical fixed-step AB2 root polynomial is prior art. Gear–Tu (1974), Skeel–Jackson (1983), and Calvo–Lisbona–Montijano (1989) are genuine potential anticipations; only their publisher abstracts and metadata could be inspected. Two inspectable public full papers (Sandu–Constantinescu 2007, and Hadjimichael et al. 2015) investigate different multirate component methods or optimized SSP schemes; neither implies the specific arbitrary-positive-pair AB2 scalar optimum, total-step boundary, and transient norm law. Indexed mathematical results on other integrators do not dominate this statement. An equivalent specialization in the inaccessible older articles cannot be eliminated and should be checked by a future human review.

## Value — PASS
The combined result supplies an exact method-selection rule: total step length determines two-period decay stability regardless of step ratio; equal physical steps optimize the asymptotic period contraction; extremely uneven stable steps can still magnify stored-value perturbations without bound. The optimum \(1/3\) and sharp transient coefficient are precise and directly interpretable for multistep solver design. Claims are restricted to the scalar negative-real test equation and spectral/per-state amplification, not solution accuracy or unrestricted variable steps.

## Review status
Self-review: passed. Independent audit: not yet performed.
