# Review

## Correctness

PASS. The detector cosine on an SPD quadratic reduces to a sharp extremal matrix-angle problem. A direct spectral proof gives the universal lower bound \(2\sqrt{\mu L}/(\mu+L)\), and an explicit mixture of the smallest- and largest-eigenvalue directions attains equality. Solving the strict AdamP threshold inequality gives the exact condition-number frontier and its equality behavior.

Risk: this classifies detector activation, not the dynamics after the projected update.

## Originality

PASS. The defining AdamP paper specifies the automatic cosine detector and empirically validates separation between scale-invariant and scale-variant weights, but the inspected full text does not give a worst-case condition-number threshold for an ordinary scale-variant quadratic. Focused published-record searches found no implication-equivalent AdamP statement.

Residual risk: the underlying SPD angle extremum is a classical matrix fact, so originality is in the exact AdamP detector application, dimension-normalized inversion, and false-positive interpretation.

## Value

PASS. AdamP's automatic detector is a central practical feature. The result gives a sharp certificate for when curvature cannot fool that detector and an explicit family showing when it can. The default-\(\delta\) law \(\kappa_\star\sim400d\) provides a direct quantitative interpretation of the detector's robustness to ill-conditioning.

Self-review: passed. Independent audit: not yet performed.
