# Independent mathematical audit

## correctness

PASS

An unrepresented cohesive group can be reduced to exactly q=ceil(n/k) voters, so JR is equivalent to fewer than q uncovered supporters of every candidate, including with empty ballots. With two seats, a quota-supported newcomer leaves fewer than q voters outside its support for odd n. For n=2q, if both insertion pairs fail JR, the entire complement of the newcomer's support must jointly approve some candidate and neither old member touches that complement, contradicting original JR. Once one quota seat is present, some quota member of a feasible DR pair either has a distinct support set (so their union has more than q voters in the even case), or the reference pair has exactly the same coverage as the replacement. This completes in at most two swaps; each replaces an off-quota member with exact quota and avoids the exclusion. At k=1 a full-support candidate suffices. In the interval witness, both committees cover all three voters and each strictly improving swap removes b, losing one of its two voters. If m<=k+1, a feasible DR committee distinct from a non-DR JR committee differs in one swap, necessarily replacing a non-quota member, proving candidate minimality. Independent direct-cohesive-group and exchange-graph checks passed for 5407 profiles counted up to voter permutation at each of k=1,2, for 4844 at k=3,m=4, and for the witness (python3 /workspace/repro/frozen_checks.py). The proof gives the unbounded conclusion.

## originality

PASS

The best known overlap covers the qualitative two-to-three-seat boundary but does not supply the two-swap bound, interval-domain witness or general minimal-candidate argument. The original local-DR axiom and its four-seat obstruction are credited. The specific constructive and sharp distinctions survive the checked comparisons; this is not a claim of absolute priority for the qualitative boundary in isolation.

## value

PASS

The exact path-length guarantee makes the local axiom actionable at two seats. The candidate-minimal three-seat interval trap identifies failure even under a commonly structured preference domain; neither the number of candidates nor the interval constraint is an arbitrary slice. Together these delimit when simple exchange can substitute for global feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
