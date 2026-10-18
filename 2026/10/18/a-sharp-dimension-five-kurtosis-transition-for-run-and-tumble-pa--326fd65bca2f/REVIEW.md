# Scientific review

## Correctness — PASS
The displacement has an exact representation by i.i.d. centered run velocities and Poisson–Dirichlet run lengths. The conditional second and fourth moments, the two Laplace transforms, and the closed-form cumulant agree. A nonnegative sum of fourth powers certifies \(A(x)>0\). The differentiated threshold has a globally positive exponential-series certificate: eight initial zero coefficients, \(c_8=112\), and a positive inductive recurrence for every larger coefficient. This establishes a strict single crossing, not merely a numerical trend. Exact coefficient manipulations and independently evaluated renewal sums are checked in the accompanying Python script (1,136 checks). The finite checks do not replace the analytic argument.

## Originality — PASS, subject to independent priority review
The full, accessible source arXiv:2006.06989 studies the precise random-redraw speed model, but its persistence/time-of-maximum/record assertions do not entail a cumulant classification. Its earlier 2020 precursor arXiv:2001.01492 is acknowledged as the earliest public motivating source. The inspected source arXiv:2211.07337 derives fixed-speed two-dimensional higher moments but does not derive an all-dimensional random-speed strictly decreasing sign threshold. The inspected arXiv:2103.04637 and arXiv:2107.00338 emphasize rare deviations and condensation; neither supplies the present finite-time fourth-cumulant single-crossing result. Related published-record searches with velocity-jump, random-resampling, fourth-cumulant and dimension-five aliases found only different processes; absence of matches is not itself proof of novelty. A general older velocity-jump cumulant identity might imply the exact moment formula; no claim of absolute priority or independent verification is made.

## Scientific value — PASS
The exact sign of the fourth cumulant is a physically interpretable departure from Gaussian transport. This theorem gives a complete and sharp classification for every observation time from only the second/fourth speed moments and spatial dimension. The unexpected first crossover dimension \(5\), the unique time when a crossover exists, and speed-heterogeneity thresholds address a substantive observable property not fixed by the ordinary effective diffusivity. These are not parameter relabelings or computations at one arbitrary dimension.

## Limitations
Only free Poisson velocity-refresh dynamics with independent uniform directions and finite fourth speed moment are covered. Earlier general theorems may imply pieces of the argument. The sign diagram concerns finite-time fourth cumulants rather than a thermodynamic singularity, and independent audit and priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
