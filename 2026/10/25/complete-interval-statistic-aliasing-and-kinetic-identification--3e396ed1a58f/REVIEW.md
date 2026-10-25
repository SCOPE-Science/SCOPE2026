# Scientific review

## Correctness

PASS. The stationary empty-interval recurrence and boundary values follow from the microscopic hopping and independent Poisson reset process. Solving the characteristic equation, treating its repeated-root case, and using inclusion--exclusion establishes the exact static observation fibers. Root positivity establishes sufficiency of the sharp feasible region. The local generator proves the occupation autocorrelation slope, and strict monotonicity yields global reconstruction. `check.py` checks the algebra numerically, including the repeated-root boundary and an independently solved truncated recurrence. Numerical work is supplemental, not an infinite-lattice proof.

## Originality

PASS, with historical-priority uncertainty. arXiv:1309.2107 gives the forward empty-interval process and a continuum formula that implicitly exhibits a related static interchange. The distinct contribution is the exact discrete inverse fiber, its sharp observation feasibility wedge, and the dynamic observable that breaks the ambiguity, together with an unrestricted global two-observable inverse theorem. arXiv:1012.4724 considers time correlations without resetting; arXiv:1801.09216 analyzes reaction/diffusion scaling on lattices and trees, not inverse identification. Searches for reset-coagulation identifiability, interval duality and short-time autocorrelation did not reveal a directly dominating classification. An equivalent specialized treatment may exist.

## Mathematical value

PASS. This is a natural structural identifiability problem for a microscopic reaction--diffusion model: even perfect knowledge of the entire distribution of stationary empty runs cannot resolve a hidden parameter swap, whereas a single experimentally interpretable short-time local observable does. The exact feasibility region allows an observation to be rejected as incompatible, and the fold at equal latent roots pinpoints loss of static identifiability. The result is more than recomputing a density or making an arbitrary finite-parameter comparison.

## Limits

Known per-neighbour hopping rate, independent fresh configuration at every reset, exact stationary expectations and right derivative. The result is not a finite-data estimator or a general theorem for quenched resetting, source injection or non-contiguous multipoint statistics. The prior continuum expression implies a weaker static algebraic symmetry; the priority of the full inverse theorem is not independently certified.

Self-review: passed. Independent audit: not yet performed.
