# Independent mathematical audit

## correctness

PASS

The number of successor-colour neighbors of any vertex currently colour c equals the global population n_(c+1), since no vertex can be its own successor. All vertices of one colour update together. Zero, one, two, three large positive populations (>=theta) give respectively fixed, one-step merger to fixed, two-step merger to fixed, or primitive 3-cycle; two-colour states merge or are fixed. Thus only (0,1),(1,1),(2,1),(0,3) orbits occur. Counting positive small/large labelled colour blocks yields the four EGF formulas with coefficients (1,3,3,1), and two-colour contributions are separate binomial sums. Three large counts exist iff N>=3theta; exactly two large plus one small is possible iff theta>=2 and N>=2theta+1. For iid uniform colours, multinomial CLT on the two-dimensional sum-zero plane gives covariance diag(2/9), offdiag(-1/9), and the triangle of area 9delta²/2 has density 3sqrt(3)/(2pi), giving Psi(delta)~27sqrt(3)delta²/(4pi). At theta=floor N/3, N=3m+r, admissible offsets are r nonnegative components in binom(r+2,2) ways; 2D local CLT gives N*P→binom(r+2,2)*3sqrt(3)/(2pi). Independent direct vertex-update enumeration for all n=3..7, theta=1..n+1, 30 pairs confirmed exact eventual preperiod classifications; it is not an all-N proof.

## originality

PASS

Best-of-knowledge comparison of exact statements and implications: Searched mean-field cyclic dominance, RPS complete-graph synchronous threshold automata, and 3-colour excitable media; Resultary hits were unrelated ternary semigroup automata or binary parity automata. The arbitrary-graph threshold-one dynamics does not supply this all-integer-theta finite K_N orbit EGF census. Tree results concern a non-complete infinite graph and different outcomes, not a reduction that dominates the complete-graph theorem. Standard probability and EGF tools are legitimate steps but do not alone imply the population reduction; the prior tree and arbitrary-graph results do not entail the stated sharp finite K_N counts.

## value

PASS

The complete graph is a canonical solvable mean-field benchmark for a nontrivial multicolour threshold dynamical system. A complete exact orbit landscape and sharp 1/sqrt(N) critical window, including mod-3 boundary coefficient, offer structural information not captured by merely listing individual finite orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
