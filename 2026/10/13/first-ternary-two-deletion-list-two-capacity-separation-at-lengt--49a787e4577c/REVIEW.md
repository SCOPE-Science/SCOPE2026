# Independent mathematical audit

## correctness

PASS

The incidence model uses distinct deletion outputs and distinct codewords, including the single empty output at n=2. Multiplying each output's list constraint by its nonnegative rational weight and each word's upper bound x_w<=1 by its own nonnegative weight gives an upper bound on total code size when each word is covered at weight >=1. Independent exact checks of every entry give the pairs of dual objectives (1,2), (3,9/2), (3,6), (33/5,63/5); taking floors and checking the matching codebooks gives the stated exact shorter-length capacities. The length-six compatibility graph on 729 words uses disjoint shadows as adjacency, so unique-decoding codes are its cliques. An independent Python reproduction greedily colors candidate prefixes into independent classes, searches include/exclude extensions with safe color pruning, and returns maximum 11 after 1,428,176 nodes (tested first at n=5, maximum 6). The checked size-11 and size-24 codebooks have shadow loads at most one and two, respectively. Since 24>22 and all shorter lengths satisfy the required non-strict inequality, the first strict gap is proved; the exact length-six list-two capacity is not determined. Replay paths: /workspace/branches/c4cc4d3f-8b96-48b2-8b6f-cb75dc0d6f76/{independent_check.py,finite_replay.txt,clique_check.py,clique_n5_replay.txt,clique_n6_replay.txt}. The frozen Python/C++ files were inspected as evidence, not executed.

## originality

PASS

The previously reported sequence of unrestricted unique-decoding optima through five is credited and not a distinct contribution. The surviving claim is the first strict list-two capacity separation for ternary two-deletion shadows, including the exact length-six unique-decoding optimum and a size-24 list-two witness. The strongest checked overlaps do not establish that separation or its minimality.

## value

PASS

The factor two is the natural benchmark since any union of two unique codes is list-two and has size at most twice the unique capacity. Proving strict separation for the first length, with exact earlier capacities and an explicit witness exceeding that benchmark, answers a meaningful finite coding question. This is not just a recollection of short unique-decoding tables and does not require determining the exact length-six list-two optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
