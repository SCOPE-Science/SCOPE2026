# Independent mathematical audit

## correctness

PASS

Earliest-position embedding is optimal by induction on the scanned letters. A requested run of length r starts at the first fresh host block of the correct symbol; with host capacity c it skips exactly floor((r−1)/c) intervening blocks of the opposite symbol. Each change of requested symbol then advances one block. For length L this gives terminal host index δ+L+Σ[2 floor((r−1)/c)−(r−1)], where δ is 1 iff the candidate starts in 1. For both capacities ≥2 all penalties are nonpositive; equality occurs for odd r at capacity 2, and only r=1 at larger capacities. Hence all lengths below 2k are present, and at 2k the absent words are exactly those starting in 1 with all penalties zero. These even-length words have an even number of runs, i.e. a sequence of 1-run/0-run pairs; the phrase 'even number of alternating symbol-pairs' in the proof should be read as an even number of runs, not a parity restriction on the number of pairs. The run-pair generating functions give coefficients F_{2k}, 2^{k−1} and 1. When a capacity is one, one symbol per block embeds every word of length k and a constant word fails at k+1. For a=1<b, at length k+1 a word with z between 1 and k−1 zeros contributes at most z−1 in zero-run penalties and hence is present; the all-one word also fits. With k zeros only putting the lone 1 first fails; with k+1 zeros the constant word fails. Reversal and complement give the swapped case. With both capacities one the failure threshold allows no switch from an initial 0 and at most one switch from an initial 1, giving exactly k+2 words. This includes k=1. Inspected the frozen verifier and reported checks; the general result follows from the proof, not the finite sample.

## originality

PASS

The general arch length rule and the exactly overlapping doubled-run Fibonacci branch are credited. The supported distinct content is the uniform classification across both run capacities, including the parity-to-singleton change and the mixed-capacity word families. The checked general algorithmic results do not establish this symbolic classification without the family-specific argument.

## value

PASS

Two-run block powers form a natural periodic test family for subsequence universality. Giving whole word sets, not just lengths or sample counts, identifies the exact capacity threshold at which the shortest-absent language loses odd runs and the corresponding growth changes from Fibonacci to powers of two to a singleton. This distinguishes hosts with the same minimum absent length and is more than enumerating instances of a general algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
