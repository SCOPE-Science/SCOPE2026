# Independent mathematical audit

## correctness

PASS

Writing E=e^−z−Σ_(k≤m)(−z)^k/k!, the reciprocal is e^z+e^(2z)E+O(z^(2m+2)). For even m, the corrections through degree m+2 are −z^(m+1)/(m+1)! and [1/(m+2)!−2/(m+1)!]z^(m+2); adding the e^z terms cancels a_(m+1) and gives a_(m+2)=−2(m+1)/(m+2)!. In a reachable off-diagonal entry of shortest distance d, powers below d vanish and Q^d has a strictly positive entry. For d≤m this gives positivity. The remaining case d=m+1 on n=m+2 states requires a diagonal stay at power d+1: a walk with d+1 off-diagonal transitions repeats a vertex, and deleting a loop of length at least two contradicts minimal d. Exactly one diagonal stay occurs in any nonzero term at this power and one can insert it at the initial vertex of a shortest path, whose rate of exit is positive. Thus Q^(d+1) has a negative entry and the negative a_(d+1) makes the leading update coefficient positive. Unreachable entries are zero, diagonals approach one, and analyticity at zero and finiteness give a Q-dependent common interval. The m+3 birth chain has distance m+2 and Q^(m+2) entry one. At m=4, the transient denominator has diagonal D(h)/24>0 for all h≥0 and the terminal diagonal is one, so the inverse always exists for this chain. The independently written integer-polynomial recurrence in `/workspace/checks/exact_checks.py` checks the six transient numerators and five shorter absorption numerators, equality of the remaining numerator with h^6P, both Descartes sign transforms, and the strict rational bracket (τ≈0.326062780128963); replay with python3. Together with the nilpotent block expansion and conservation, these give exactly the positivity set stated, including the identity at zero. Terminology at RESULT.md line 22: the update has unit row sums whenever defined, not necessarily stochastic; standard stochasticity additionally requires nonnegativity. The row-sum identity, not that misnomer, is used in the proof, and the Finding explicitly states the negative-entry regime. Nothing here gives a universal step size or global positivity for arbitrary generators.

## originality

PASS

The path-distance, Taylor-zero and diagonal-stay mechanism is known in the neighboring Padé records and generalizes once the relevant coefficients are known; do not count that mechanism as new. The reciprocal even-denominator family at m≥4 and, especially, the exact seven-state quartic all-step sign classification are distinct from the inspected results. The threshold and sign proof are not a reparameterization of the [2/2] or [0/2] witness. The assessment is bounded by the inspected sources, not a claim to publication priority.

## value

PASS

The dimensions at which an update can stop being a transition matrix are useful independently of formal integrator order. The first obstructed fourth-order birth chain is forced by the sharp dimension bound rather than arbitrarily selected. Its exact recovery, where smaller positive steps can lose positivity while all larger steps preserve it, adds information not supplied by the leading negative coefficient or the examples for other Padé families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
