# Independent mathematical audit

## correctness

PASS

Utility-based JR tested on each voter's peak requires utility at least 1. Endpoint peaks are mandatory; a run of r omitted interior peaks forces r+1 different bridges, disjoint across runs, exceeding the seat budget. The all-peak committee satisfies JR because every demanded single-candidate utility is at most 1. For odd size the uniform bridge weights rho/(2v) and endpoint peaks rho/2 give budget k and every utility rho. For even size the alternating 1,z bridges (z=h/(h-1+2v)) and endpoint peaks vz do the same, including k=2. All weights satisfy the caps. For a coalition block of size s, alternating normalized voter weights give a bound aB in odd size and a[B+2v-1] in even size, B the incident mass; the one excess even edge has weight at most 1. In either case attaining more than rho_s requires B>s. The incident candidate sets of disconnected blocks are disjoint, so the sum of their B cannot exceed |S|. Both parity expressions equal 2v minus v(2v-1) divided by a denominator that increases strictly with size (also from s=1), hence a utility strictly above rho_k violates the budget. This proves sharpness over all coalitions and the inclusive threshold under strict blocking. The rational and LP checks in the source are finite corroboration, not used as proof or rerun.

## originality

PASS

The profile, uniqueness of JR and asymptotic obstruction are prior work. The distinct finding is the exact finite-size parity-dependent maximin over all eligible coalitions, attained by the grand coalition, and therefore the exact strict-core boundary for this profile.

## value

PASS

The exact obstruction measures the best possible deviation in an already motivated impossibility profile. The upper bound controls disconnected coalitions as well as intervals, and the parity corrections and strict boundary are information not supplied by a large-k lower witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
