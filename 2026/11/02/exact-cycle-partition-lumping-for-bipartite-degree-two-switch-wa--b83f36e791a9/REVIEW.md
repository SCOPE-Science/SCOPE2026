# Review: cycle-partition projection for degree-two bipartite switch walks

## Correctness (PASS)
The claim has quantified scope \(n\ge2\), specified matrix entries/margins and the exact rectangle proposal distribution. On each bipartite cycle, two alternating one-factors divide switches into same-factor nonconsecutive pairs (splits) and different-factor disjoint pairs (type preservation); choosing edges from different components merges them. The counts exhaust all possibilities. Direct double counting of labelled cycles establishes the state multiplicities, and reversible rectangle proposals establish the stationary law. Finite exhaustive checks over the actual embedded sources cover every state through \(n=6\); they corroborate rather than replace the unrestricted proof.

## Originality (PASS; residual qualification)
The nearest primary general source is Miklós–Erdős–Soukup (arXiv:1004.2612, 2010; Electronic Journal of Combinatorics 2013), which defines the same rectangular-switch dynamics and proves connectivity and rapid mixing in a general family; full-text material in §§1–3 and the alternating-cycle section was compared. Nester (1994) tabulates Eulerian orientations of balanced complete bipartite graphs (including 90 for a 4-by-4 binary matrix), while OEIS A001499 independently tabulates the total number of matrices with margin two. Those results are acknowledged. The exact strong-lumping rules, complete cycle split/merge/stay rates and projected conditioned-Ewens law are not implied by those global results and were not located in searches of direct aliases. An inaccessible or unindexed paper could still contain these precise formulas; priority is not certified.

## Value (PASS)
The binary fixed-margin switch walk is a canonical sampling mechanism. Determining whether a coarse observable is itself Markov is not automatic; exact strong lumpability makes cycle counts dynamically sufficient, gives an explicit small partition-state chain for each \(n\), and converts high-dimensional moves into integer-partition transitions with a closed equilibrium measure. These rates permit exact reduced-state calculations without enumerating every labelled matrix and are substantively more informative than the classical total-state counts.

## Limits
The result does not determine full-chain mixing times or show a new connectivity theorem. The Ewens law is conditioned on no singleton parts. Finite checks establish only the tested sizes; the general theorem is the constructive proof. Potential equivalent treatments under coagulation–fragmentation terminology remain a residual risk.

Self-review: passed. Independent audit: not yet performed.
