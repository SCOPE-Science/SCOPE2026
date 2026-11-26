# Independent mathematical audit

## correctness

PASS

The frozen claim is a census of distinct, nonempty scattered Lyndon strings in each linear binary host, with 0<1 and no quotient on host words. The append/omit set recursion and strict cyclic rotation test are correct, including single letters and exclusion of periodic longer candidates. An independent full census instead inserted every strictly least rotation word up to length 20 into a shared-prefix trie. At each prefix, the earliest greedy embedding leaves maximal space for continuation; a failed next occurrence rules out all longer completions from that prefix. Each reachable terminal therefore contributes one distinct subsequence. The host loops are exhaustive, not merely witness checks: 2^n visits at each length, 2,097,150 total and 1,048,576 at n=20. Replay: `python /workspace/branches/3c7fd282-4efa-422e-bc8e-d396524b8025/replay_trie.py 20`; `replay_trie_n20.txt` and `comparison.txt` in that directory record exact agreement with all 20 frozen maxima, tie counts and complete optimizer lists. In particular n=20 has count 4701 and unique word 00010101010101101011. The two source programs were inspected but not executed; the packaged second program has only longer-length witness checks, whereas this reproduction establishes the entire finite upper-bound classification. No length beyond 20 is established.

## originality

PASS

The checked distinct contribution is the complete finite binary MDS census through length 20, including all equality cases. The strongest accessible primary source defines the very same maximum and leaves its exact determination open; multiplicity, expectation, longest-length optimization, and contiguous-factor counts are different. Bounded catalogue comparisons did not establish a matching or stronger census. The broad primary literature lookup and exact-OEIS-query access were unavailable; this neither proves priority nor defeats the affirmative statement-level distinctions from the strongest accessible sources.

## value

PASS

The maximum is a natural explicitly open invariant in primary combinatorics literature, distinct from the solved occurrence maximum. The census gives exact best values and all equality cases on the full binary space through the million-host depth-20 level. It supplies useful benchmark data, reveals nontrivial ties and eventual uniqueness within the measured range, and distinguishes the optimum from the known multiplicity extremizer as early as length six. The cutoff marks the demonstrated exhaustive range, not a claimed structural threshold or an answer for general n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
