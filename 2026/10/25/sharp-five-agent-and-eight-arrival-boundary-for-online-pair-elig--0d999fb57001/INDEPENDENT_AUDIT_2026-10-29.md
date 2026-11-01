# Independent mathematical audit

## correctness

PASS

Reduce goods to d_i=e_i-2L_i and chores to d_i=2L_i-e_i. For a chosen pair, greedy changes sorted coordinates by -1 at the larger and +1 at the smaller (sign reverses for chores). Independent state-closure enumeration gives precisely nine reachable sorted five-agent discrepancy vectors and maxima at most 2; the complete edge-closed invariant proves arbitrarily many arrivals by induction. Six-agent complete 15-pair successor enumeration has level-cardinalities 1,1,3,6,9,10,11,13 through depth seven; independent equal-level adversarial selections 0,0,1,0,-1,0,1,2 force the terminal sorted vector (3,1,0,-1,-1,-2) regardless of allocator choice. Greedy completeness is only a seven-step existence result, whereas the lower bound quantifies over all allocators. Checked the actual frozen RESULT.md and verify.py state transitions. No finite experiment is being extended to infinity except by explicitly proved invariant closure.

## originality

PASS

The closest same mathematical model Biburger–Megow–Shahkarami paper (arXiv:2610.08064) already uses an equal-deficit two-eligible-agent adverse construction (as credited by the package). This mechanism is not new. However its accessible abstract/general bounds do not themselves establish the exact nine-state infinite five-agent positive invariant nor the first six-agent forcing horizon eight. Offline fair-orientation results do not imply prefix-online irrevocable allocation. A primary Appendix C full-text comparison was attempted but inaccessible; priority remains qualified. Best-of-knowledge the joint threshold theorem is not shown to be covered.

## value

PASS

Natural sharp boundary in number of agents and forcing time for online, eligibility-aware PROP1 under sparse pair eligibility. An explicit finite-state constructive invariant controls arbitrary arrival horizons, while an adaptive adversarial witness gives the precise first failure. This resolves a meaningful algorithmic fairness subproblem, not a merely sampled counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
