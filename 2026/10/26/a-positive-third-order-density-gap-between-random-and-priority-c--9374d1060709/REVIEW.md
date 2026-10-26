# Scientific review: colouring choice and short-time adsorption density

## Correctness

PASS. The calculation uses an exact Poisson insertion identity. The first nonzero rejection term comes from exactly two prior proposals in the test object's exclusion region. The probability of a third prior proposal in the finite enlarged neighbourhood is \(O(t^3)\), giving an \(O(t^4)\) error in accumulated density. Overlapping earlier proposals must have distinct colours in either protocol; nonoverlapping earlier proposals can share a colour, but random selection makes them opposite with probability \(1/2\) while fixed priority makes both colour 1. These cases give the displayed integrals and their coefficients. The one-dimensional overlap volume is \(3\sigma^2\); the two-dimensional disk overlap integral equals \(\sigma^4(\pi^2-3\sqrt3\pi/4)\). The independent checker reproduces these identities and the counterexample history. No simulation is used as a proof of the asymptotic theorem.

## Originality

PASS subject to external priority assessment. The motivating open preprint, Parida--Dhillon, arXiv:2202.10547v1, expressly claims equality of total admitted densities for randomly selected and sequentially selected colours in Section II, equation (1), and builds its first approximation on that equality. Its treatment of the actual random-choice model does not give an exact cubic separation from the priority scheme. The distinct discrete priority-only processes of Fleurke--Külske (2009) do not imply the comparison for continuum rods or disks. Searches for random-versus-priority coloured RSA and short-time geometric coefficients did not identify a covering result; failure to locate one is not a mathematical uniqueness proof.

## Scientific value

PASS. This is the first nonzero dynamical rejection coefficient for the original multilayer model and an explicit distinction between two channel-allocation policies that were treated as density-equivalent in a model developed for statistical physics and wireless resource allocation. The strictly positive volume formula gives an exact calibration, with simple closed forms in both physical dimensions considered in the source. It is not a merely syntactic counterexample: it quantifies a change in the actual observable used to assess packing and channel occupancy.

## Limitations and closest literature

The proof is a fixed-parameter \(t\downarrow0\) expansion; it does not determine the sign of the density difference for arbitrary later times, jamming densities, higher colours or full spatial correlations. The precise published support is Parida and Dhillon, *Multilayer Random Sequential Adsorption*, arXiv:2202.10547v1 (Sections I--IV), and Fleurke and Külske, *A Second-row Parking Paradox*, Journal of Statistical Physics 136 (2009), 285--295. General random greedy colouring phenomena are potential background, not evidence that the evaluated Poisson geometry coefficients were previously established. Independent scholarly priority assessment remains necessary.

Self-review: passed. Independent audit: not yet performed.
