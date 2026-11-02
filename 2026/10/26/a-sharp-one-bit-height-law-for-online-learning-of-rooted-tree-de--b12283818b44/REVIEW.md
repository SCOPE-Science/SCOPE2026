# Independent mathematical audit

## correctness

PASS

For nodes as hypotheses and queries, every positive answer at x leaves at most h+1 ancestor-rooted cones; consequently the positive branch of a depth-d mistake tree gives 2^(d-1)<=h+1. A maximal root-leaf chain is an (h+1)-threshold class attaining floor(log2(h+1)). In a full b-ary tree of height >=2, the positive branch at 0^h shatters the ancestor threshold chain via off-spine nodes 0^j1 and the negative branch contains the whole b-ary subtree rooted at 1 of height h-1; induction gives the upper endpoint. Base cases h=0 and h=1,b=2 vs b>=3 handled separately. Laminarity forbids 3-point VC shattering, and explicit sibling-leaf witnesses give VC=2 under stated conditions. Independent version-space recursion on paths through h=8 and full trees (b,h)=(2,0),(2,1),(3,1),(2,2),(3,2),(2,3),(2,4) matched exact values. Finite checks corroborate but do not prove all-height bounds.

## originality

PASS

Best-of-knowledge exact statement and implication comparison: closest accessible primary papers and ranked published findings do not establish this precise claim under the stated parameters. This is not a historical-priority certificate; see source inspections and risks.

## value

PASS

The node-indexed ancestor-cone concept family is a canonical hierarchical classification model. Its online mistake complexity is tightly governed by height rather than total vertices, and complete b-ary trees show a sharp VC-two versus unbounded Littlestone dimension separation. Matching extremes at every height and exact regular-tree cases are motivated global structural information, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
