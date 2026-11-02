# Independent mathematical audit

## correctness

PASS

On a tree, two selected edges are forbidden exactly when a third edge joins their endpoints, equivalently for every uv, (d_S(u)-epsilon_uv)(d_S(v)-epsilon_uv)=0. For a subtree with parent-edge indicator x and j selected child edges, the proof partitions all root boundary states into j=0, j=1, j>=2 and derives the exact recurrence. Substitution proves the explicit three-residue DP solution and strict maximizing j=b at h=1 mod3, j=0 at h=0,2 mod3 for b>=2. The forced boundary continuations are unique; the layers thus give the only maximizer, and the ratio is the quotient of two geometric sums. Independently enumerated every edge subset on six small instances, including b=2,h=3 (16,384 subsets), b=3,h=2 (4096), verifying unique optima. Infinite uniqueness follows the recurrence, not finite experiments.

## originality

PASS

Best-of-knowledge: existing all-tree algorithm can compute these optimum numbers but does not provide the closed two-parameter formula and uniqueness/rigid-layer theorem directly. Inspected full relevant primary preprints and retained possibility of hidden formula in 2022 foundational article.

## value

PASS

The exact optimizer and uniqueness across all branching factors is a substantial structural rigidity refinement over generic tree algorithms; the period-three selected-layer phenomenon and limiting density are natural, not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
