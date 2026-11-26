# Independent mathematical audit

## correctness

PASS

After any acceptance the next positive-rate waiting time is exponential at the Lebesgue measure of the available centers. The accepted count is bounded by floor(L), and zero-measure contact placements never occur. After the first rod the residual unoccupied arc is an interval of length L−1; its feasible-center length is (L−2)_+. For 2<L≤3 a second rod leaves both empty arcs of length at most one, hence jams. For 3<L≤4 split the residual free length L−2 after the second rod by a uniform position on [0,L−2]; the two empty arc lengths are x and L−2−x. At most one exceeds one, so the resulting positive rate has density 2/(L−2) on (0,L−3), with the remaining mass at zero. Independence from the earlier clocks follows from independent Poisson times and locations up to the stopping time and rotation invariance; a fourth rod is impossible almost surely even at L=4. Integrating exp(−at) against that rate density gives the stated tail, while adding the independent light-tailed clocks changes its large-t expression only by O_L(t⁻²). Integration yields the truncated mean and divergence. For L>4, k=floor(L/2)+1 satisfies k+1<L<2k. Prescribe the first k labeled proposals in cyclic order near a configuration with first center gap 2 and other gaps all (L−2)/(k−1)∈(1,2). Keeping one clockwise chart fixed gives a product box in first-center and gap coordinates with unit Jacobian. Move the first gap through 2+ε and hold the remaining free coordinates in that box so the last gap stays in (1,2). All k proposals are accepted, the remaining rate is ε, and the mean of the next wait integrates against a positive constant density to infinity. This argument handles even integer L, not only generic circumferences. Replay: integrate the two subintervals 0≤x<L−3 and 1<x≤L−2, and use the gap-coordinate Jacobian above for L>4. The packaged quadrature and sampling are supporting tests, not the continuum proof.

## originality

PASS

The supported increment is the physical last-acceptance time law on a finite continuum ring: the sharp mean cutoff (including the equality case), the exact first nontrivial terminal-stage survival, and its explicit coefficient. Small-gap power laws and discrete-lattice jamming times are not new. The inspected prior results do not entail this combination.

## value

PASS

A.s. finite completion despite infinite expected physical time is a concrete distinction for a canonical finite-volume stochastic process, and the exact cutoff shows it begins immediately when a nearly fitting third placement becomes possible. The explicit tail and truncated mean quantify the resulting rare events and give a benchmark that cannot be read from either count-only parking algorithms or infinite-volume coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
