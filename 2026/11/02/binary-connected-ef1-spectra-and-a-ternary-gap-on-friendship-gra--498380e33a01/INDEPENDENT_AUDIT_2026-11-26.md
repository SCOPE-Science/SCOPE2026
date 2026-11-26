# Independent mathematical audit

## correctness

PASS

In a connected partition each nonhub bundle lies within a petal. The binary lower witness gives it at most one mark and forces the hub bundle to have at least k−n+2≥3. At k bundles, writing W=k+b+r₂−r₀ verifies all feasibility inequalities: W<k gives 0≤r₀−r₂−1≤r₀; otherwise r₂≥r₀−b. With k≤W<2k the source uses no splits when r₀=0, r₀−1 splits when b=1 and r₀>0, and gains the required r₀ extra nonhub bundles from two-mark petals when b=0 (including the half-petal at the hub if r₁=0). Each construction totals k connected nonempty bundles with balanced marks, and W=2k or 2k+1 gives all twos or a single three. For refinement that only three splits into a hub singleton and its petal; subsequently a tree edge on the path between the two marks in a two-mark bundle separates them, preserving values in {1,2} until all values are at most one. Further connected splits then preserve EF1. For the ternary assignment, keeping the two weight-two vertices together forces total value ≥2k+2>k+4. Separating the two leaves either the hub with one weight-two vertex and at least one ordinary unit petal vertex, or the hub without them but with at least two unit petal vertices. In both cases its one-deletion value is at least two and there is a nonhub ordinary bundle worth at most one (k−3≥1 in the last case). The proof covers exactly k≥4 for this ternary witness and ordinary EF1 with no connectivity requirement on the deletion. The supplied exhaustive checks for small k were inspected, not executed; the proof is the all-k evidence.

## originality

PASS

The supported contribution is the sharp identical-binary threshold at n=k uniformly in k and the explicit three-level obstruction there. The low-agent obstruction is an exact specialization of Chen–Zwicker; their high-agent theorems already give part of the positive range. Neither gives the threshold phenomenon reviewed here.

## value

PASS

The threshold asks how many agents are needed to divide a graph built from paired resources around one hub. At the first universally feasible agent count for identical binary weights, allowing one additional weight level already destroys the guarantee. The constructive all-k threshold and the matched failure at that same boundary clarify the role of binary weights and the cutset, rather than merely testing a few small graphs or restating the known lower obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
