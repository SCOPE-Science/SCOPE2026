# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The lower guarantee is a finite-order consequence of the cut-edge argument in Sivashankar's proof of the odd-degree k=2 theorem. In connected simple r-regular graphs of odd degree, the omitted-vertex count is at most floor((c-1)/(r-1)), where c is the number of cut-edges; the sharp O--West cut-edge bound converts c >= (r-1)t+1 into n >= (r^2-3)t+2(r+2). The argument extends componentwise to disconnected regular graphs because each positive-deficiency component separately pays the same additive order overhead.

Sharpness at every admissible order is supplied by an explicit construction. A Walecki decomposition of K_N for odd N produces, for every odd N>=r+2, a block with one vertex of degree r-1, all others of degree r, and a spanning Hamilton cycle. Attaching such blocks to a degree-completed path of t core vertices yields a connected r-regular graph whose core is incident only with bridges. The minimum-order version has (r^2-3)t+2(r+2) vertices. Any admissible intermediate order differs from this by an even amount smaller than r^2-3, and that entire excess can be absorbed by enlarging one Walecki block. No 2-regular subgraph can use a core vertex, while the block Hamilton cycles cover all non-core vertices, so the omission is exactly t.

A standalone verifier constructs these graphs directly and checks simplicity, regularity, connectivity, bridge counts, and the explicit 2-regular coverage on 565 parameter cases for odd r in {3,5,7,9,11}. It also checks the r=3 formula against the known exact cubic expression through order 498. These finite checks support but do not replace the proof.

## Originality

Sivashankar's 2026 preprint was inspected as the closest source. It proves delta_2(r)=1/(r^2-3) for odd r and its proof already contains the finite-order upper inequality used here. Its sharpness family occurs at orders (r^2-3)t+2(r+2). The present claim is deliberately narrower than claiming a new upper bound: the new step is the variable-order block interpolation showing that this floor bound is sharp for every admissible order, hence giving the exact fixed-order extremal function.

The cubic case is not claimed new. Choi--Kim--Kostochka--Park--West determine the minimum f_2 for every cubic order, and the formula here specializes to their result. O--West's cut-edge work and the 2026 van den Heuvel--Toft 2-factor survey were also checked for the relevant structural regime. Searches under largest 2-regular subgraph, nearly spanning 2-regular subgraph, regular-graph 2-factor deficiency, fixed-order regular factor, cut-edge, and synonymous terminology found no general odd-degree every-order formula.

The assessment is therefore to the best of our knowledge. The principal residual originality risk is an older factor-theory source expressing the same interpolation in different language, or a very recent/unindexed parallel result or revision. No specific inaccessible source was identified as especially likely to contain the full every-order formula. The isolated threshold (r+1)^2 and the finite-order upper inequality are not asserted to be individually new.

## Value

The result upgrades a sharp asymptotic theorem with endpoint constructions into a closed exact extremal function for every admissible graph order. It also identifies the exact order cost per forced omitted vertex and supplies connected extremizers uniformly across the gaps between the previously displayed sharp orders. The construction is elementary once the Walecki block is isolated, and recovers the classical exact cubic answer as a consistency check.

## Limitations

The theorem concerns k=2 and simple regular graphs; it does not resolve exact fixed-order extremal functions for k-regular subgraphs with k>=3. The originality search cannot exclude equivalent old formulations under remote terminology or very recent parallel work. The finite verifier checks the construction, not the literature search or the general upper-bound proof. No independent validation is asserted.
