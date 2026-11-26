# Independent mathematical audit

## correctness

PASS

The birth rate is bounded by a linear function of total population, so comparison with a linear pure-birth process and locally bounded jump rates give nonexplosion; birth and death make the chain irreducible. The coordinate generator is Bn+ℓ. Applying the jump increments to n_i(n_i−1) and n_i n_j gives HF+g with g_ii=4ℓ_i n_i and g_ij=ℓ_i n_j+ℓ_j n_i. In particular, an i→j hop contributes β/(K−1) times F_ii−F_ij to the ij equation; a reset removes diagonal factorial mass at rate r_i, not 2r_i, and mixed mass at rate r_i+r_j. Migration links all pair states through shared indices, so both Metzler matrices are irreducible. Positive inverse-resolvent weights when s(B)<0 give a linear Foster function with drift constant minus total population, yielding the unique invariant law with finite means. When s(H)<0, the positive quadratic weights give drift −∑F plus a linear source, controlled by a sufficiently large multiple of that first Foster function, which yields finite second moments. Conversely, under the corresponding integrability assumption, the stationary generator identities are justified by the integrability of total jump rate times absolute coordinate or polynomial increment (bounded by C(1+|n|) or C(1+|n|²)); the positive left Perron vector makes either moment identity impossible at nonnegative spectral abscissa, including equality. This does not exclude infinite-mean invariant laws. For the witness, B has trace −6/5 and determinant 1/10 and B(56/5,6/5)^T+ℓ=0. Its H_11=3/5 is positive. To force divergence at the first site itself, pair particles with the one-site process that treats migration out as death and ignores arrivals. Its reset-free growth is 7/10 and its factorial second moment at age t is twice the square of (exp(7t/10)−1)/(7/10), by the two scalar drift equations. Integrating over the exponential reset age of rate 4/5 gives finite mean and infinite second moment. The shared-reset coupling and stationary convergence preserve domination; both stability and the witness's inequalities are strict and open. Frozen exact checker and output were inspected, not executed or substituted for the proof.

## originality

PASS

The finite count-valued network's sharp coupled second-moment criterion and open interacting witness are distinct on the evidence inspected. Grange supplies the closely related resetting mechanism and mean analysis; single-site catastrophe results supply the scalar comparison but not the coupled criterion. A plausible general multitype random-environment framework does not have the needed moment conclusions in the inspected results.

## value

PASS

The exact thresholds distinguish when stationary average occupancies are well-defined from when their fluctuations have a finite variance. The explicit open two-site witness makes that distinction meaningful even in a coupled finite system, and the factorial-pair matrix gives a practical stability test without assuming moment closure or treating the entire population as reset at each event.

The dated certificate retains the supplied scientific assessment, sources and limitations.
