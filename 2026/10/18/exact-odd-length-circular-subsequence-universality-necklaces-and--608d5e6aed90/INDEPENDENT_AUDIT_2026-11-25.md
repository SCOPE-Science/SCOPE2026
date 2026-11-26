# Independent mathematical audit

## correctness

PASS

Greedy shortest rich blocks determine the linear index: the sequence of their closing letters followed by a letter absent from the remainder is a missing subsequence, since the earliest possible embeddings of the closing letters are the arch endpoints. Each rich factor supplies an adjacent unlike pair, and k disjoint unlike edges on the odd cycle leave one vertex unmatched; cutting there linearizes all k pairs. Removing the equal edges leaves paths, isolated vertices included. A path with t edges leaves t+1 modulo 2 vertices uncovered by a maximum matching, so maximality means exactly one even t. For counting, distinguish the equal edge after that unique even run. If there are 2h odd runs, the 2h+1 run-plus-terminal-edge lengths have base lengths 2,...,2,1 and even excess; the resulting composition count is binom(k,2h). The sum is 2^(k-1) for k>=1. There are 2k+1 labels for the distinguished edge and two binary lifts of each transition vector. An odd maximizer uses k and k+1 symbols (it must realize both constant targets), so it cannot be a nontrivial power; equivalently, a rotation stabilizing it must fix the distinguished edge. Thus each necklace has 2k+1 distinct origins. The two fixed-origin cases (all arches of length two with one remaining symbol, or one length-three arch) are disjoint by greedy uniqueness and give (k+2)2^k, proving the rescue count by subtraction. The k=1 result and zero-length even runs are included.

## originality

PASS

The contribution is the odd extremal run criterion and circular maximizer census. Linear arch methods and the fixed-origin count are prior or immediate from prior methods; primitivity itself follows from the coprime symbol multiplicities, and the rescue count follows by subtracting the known linear count once the circular count is available. Distinct later catalog entries overlap substantially, including an exact match on the odd parity criterion, labeled/necklace counts and primitivity. The bounded comparison found no earlier covering statement for the circular classification and counts, without asserting exclusive priority or independent origin across catalog entries.

## value

PASS

The shortest odd length at which index k is possible is a natural one-extra-letter regime. Classifying all maximizers by a local parity statistic and using it to count necklaces determines precisely what rotations add to the known linear count. The proof works uniformly rather than extrapolating a short census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
