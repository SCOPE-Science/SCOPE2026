# Review of the fixed-reset-velocity persistence reversal

## Correctness

PASS. The no-reset backward generator, Dirichlet–Neumann boundary conditions, regenerative mean-FPT identity, and two-moment first variations are explicit. The main coefficient \(\chi(\eta)\) follows from the invertible positive resolvent \(R_\eta\) and the simple passive threshold \(x_*=1-1/\sqrt5\). The singular limits are analytically controlled: \(\chi(0+)=4/125\), while \(\chi(\eta)=-1/\eta+O(\eta^{-2})\). The independent checker passed exact symbolic endpoint identities, six double-resolvent comparisons and three full backward-equation Hermite calculations. Finite-dimensional numerical tests do not certify an infinite-dimensional claim; the continuum proof is in RESULT.md.

## Originality

PASS, with residual risk. Georgiou, Bressloff and Bertrand (arXiv:2609.21124v1), specifically Sec. 3.4, treat fixed reset velocities numerically, while their analytical expansion uses Gaussian velocity reinitialization. Pal and Reuveni (arXiv:1607.06048) give the general restart criterion, which is explicitly credited but does not determine the present OU susceptibility. Wang (arXiv:2102.00711) develops the boundary perturbation method. Published literature and mathematical-record searches yielded no claim with both exact persistence endpoint coefficients and forced reversal. The older Wang primary full text was not materially inspected beyond its abstract, and unlocated general theory may still imply the result.

## Value

PASS. This addresses a parameter-sensitive physical ambiguity in a recently published first-passage/resetting study: the same outward initial velocity can enlarge or shrink the region where infinitesimal resetting improves mean search time, depending on persistence. The reversal follows from exact asymptotics rather than extrapolation of simulation plots. It is an analytically testable prediction; neither uniqueness of the crossing nor global finite-reset-rate optimization is asserted.

## Scope and literature limits

The model uses proportional weak propulsion noise and proportional fixed reset velocity, with absorption at zero and reflection at one. The result is only the local small-reset-rate boundary and the first order in propulsion amplitude. The numerical crossing near \(\eta=0.2112213694\) is illustrative, not a proven unique zero. Primary comparisons: arXiv:2609.21124v1, arXiv:1607.06048v3; method background arXiv:2102.00711v1.

Self-review: passed. Independent audit: not yet performed.
