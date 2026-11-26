# Independent mathematical audit

## correctness

PASS

On at least six vertices with no universal vertex a total Roman dominating function of weight ≤3 is impossible: it needs a 2 and a neighboring positive, and the only remaining feasible weight pattern would make the 2 universal. A weight-four pattern 2+2 is an adjacent dominating pair, and a 2+1+1 pattern also has such a pair by taking the 2 and any positive neighbor; the other positive vertex must meet one of that pair. Only rungs dominate as adjacent pairs in the complete prism, since a same-layer edge misses the opposite layer at any third index. A surviving rung loses domination exactly when a respective endpoint loses an incident clique edge, or loses adjacency when its own edge is deleted. Fewer than n deletions cannot isolate a degree-n vertex. Requiring each rung index to be hit gives inclusion–exclusion on untouched indices with exactly (n−j)² admissible edges, counting labelled edge subsets by size. The minimum covers are a layer-colored perfect matching for even n, or for odd n one rung and a matching or a three-index path and a matching; counting these cases gives the two closed multiplicities. For n=2 the excluded C4 case indeed cannot increase above its order. In a fresh direct minimization over {0,1,2}-labelings every graph with k<n was checked for n=3 (46 graphs) and n=4 (697 graphs), yielding (0,0,18) and (0,0,12,248). Replay files: /workspace/branches/5c87dcc1-ad4d-41a3-903a-9911a4872235/direct_replay.py, direct_replay_n3.txt and direct_replay_n4.txt. The uploaded verifier and its output were inspected, not executed, and finite replays are not the general proof.

## originality

PASS

The adjacent-dominating-pair criterion and equality with ordinary total bondage at weight four are prior, and the resulting edge-cover inclusion–exclusion is standard. The observed distinct result is the exact failure profile in the labelled matched-clique prism: its prism-specific coverage equivalence, the full deletion-size distribution below minimum degree, and the minimum multiplicities. No inspected existing theorem already gives this profile.

## value

PASS

The cutoff k<n is the largest uniform window in which edge deletion cannot isolate a vertex, not an arbitrary truncation. The full profile gives failure probabilities at each size in that window and distinguishes robustness of the crown of rung defenders from the single minimum-size threshold. The closed minimum multiplicities quantify a genuine parity distinction on a standard graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
