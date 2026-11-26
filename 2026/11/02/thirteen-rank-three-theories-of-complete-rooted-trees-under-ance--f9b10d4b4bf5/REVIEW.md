# Independent mathematical audit

## correctness

PASS

The three-round type is the set of pointed two-round types. For comparable picks, the third point can witness a nonempty gap, room above or below, or a side branch; ancestor and descendant gaps give all Boolean patterns once each depth is clipped at three. For incomparable picks, with least common prefix depth l and divergences u,v, the third point can be incomparable with both unless the picks are the two root children in a binary tree. The other tests are u≥2, v≥2, and whether the two residual heights are positive. At fixed first point, 1≤u≤d and 1≤v≤u+t; the possible tests on v stabilize at u+t=3 and u≥3 can be replaced by u=3. This verifies the uniform cap on (d,t) including repeated picks. The capped list along a tree's depths first stabilizes at height six. A rank-two pointed formula can witness three ancestors by finding a middle ancestor with one below and one above it on the chain to the chosen node; its dual works downward. Combining those threshold predicates under one existential separates all heights below six. The rank-three sentence for an incomparable pair covering the tree by comparability separates binary from higher branching at every positive height. Height zero is the common singleton. Independent direct enumeration over actual words (binary heights 0–7, ternary 0–6, quaternary 0–3) gave all 13 classes and agrees on tested equalities and distinctions. Replay: `python3 /workspace/branches/ef_replay.py trees 7`, output `/workspace/branches/ef_trees.txt`. The finite check corroborates rather than replaces the cap argument. Frozen verification_output.txt lines 1–19 was inspected as recorded evidence, not a fresh run of those scripts.

## originality

PASS

The strongest identified catalogue matches share either the trees and rank or the ancestry signature and a broader family, but not the game parameters needed for the exact partition. The primary works inspected do not imply the sharp two-parameter partition. This is a bounded statement-level finding, not a historical priority claim.

## value

PASS

A sharp expressibility boundary for a natural family in the ancestry language. It gives explicit criteria for when height information stops being visible, while showing that binary branching stays detectable at every positive height. These are useful distinctions for checking what bounded-depth formulas can test on trees; the result is not merely a sample census or the parent-only table under renamed parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
