# Independent mathematical audit

## correctness

PASS

State n-1 is fixed by all letters. Each of the n starting distances from it must be the sum of the values of those instructions that actually move that start, so the multiset of letters in a reset word must have all subset sums 0 through n-1. Sort the letters. The first value greater than the previous prefix sum plus one leaves that very integer missing, since taking any of the remaining letters already exceeds it. Every prefix before that gap covers through its total and its next increment is at most min(m,1+prefix total). Thus the best possible coverage after k letters is bounded by S_k with S_0=0 and S_{j+1}=S_j+min(m,1+S_j); doubling before the cap and constant increments after it give the sum in the claim. For the matching word take those extremal increments in decreasing order. If remaining distance t is bounded by the total of the remaining letters, using the largest letter d either subtracts d or leaves t<=d-1, which is no greater than the total after dropping d. Induction ends at distance zero. This proves the exact threshold rather than just feasibility of subset representations; it includes n=2 and the stated m=1, m=2 and uncapped regimes.

## originality

PASS

The general stay-put difference-DFA framework and the no-gap subset-sum argument are known ingredients. The exact capped all-state reset threshold and the optimal word for this directed interval family were not established by the plausible nearby indexed or primary results inspected. This is a best-of-knowledge pass for the specialized exact invariant, not for the general DFA model or for the complete-sequence principle.

## value

PASS

The endpoint synchronization cost for a canonical finite directed translation geometry is a natural exact invariant. The stay-put obstruction is materially different from clipping. The formula explains the regime change from capped, effectively linear growth to logarithmic cost with an ample alphabet, and gives a provably shortest uniform control word. Even though the subset-sum ingredient is elementary, the equality closes a meaningful upper/lower gap for all interval sizes and command caps and is useful as a benchmark for nearby difference DFAs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
