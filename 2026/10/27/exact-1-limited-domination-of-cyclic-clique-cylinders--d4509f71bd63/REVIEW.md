# Independent mathematical audit

## correctness

PASS

On a cycle a total dominating word with omissions has selected runs of length at least two and omission runs of length at most two. Their counts are equal; equality of selected and omitted totals therefore forces every run to have length two, i.e. 4|n. The four displayed constructions attain H=⌊n/2⌋+1_(4∤n), including n=3, and imply H≤2n/3 and H≤n/2+1. Filling precisely the fibres over a minimum total dominating word gives the upper bound. Within any nonempty fibre a selected vertex sees all omissions there, so occupancy is 0, m−1 or m. With no zero fibres the size is at least (m−1)n≥mH; with no partial fibres the selected fibre indices must totally dominate the cycle. In the mixed case a zero cannot touch a partial, and a full touching a zero cannot touch a partial on its other side: its vertex of the omitted coordinate in the partial would have two outside neighbors. Zero runs have length at most two by domination, and the complementary runs have at least two full fibres. Any complementary run containing a partial has two distinct full fibres at each end (the first and last partial are strictly between them). Thus f≥2b+2≥z+2 for b zero runs and |D|=mn/2+(m/2)(f−z)+(m/2−1)p≥m(n/2+1)≥mH. The argument uses distinct cycle neighbors even at n=3. For the width-two witness select one of the two length-six rows; its vertical matching gives exactly one outside neighbor per selected vertex and dominates the other row. Any feasible set has size at least half the order by counting crossing edges, so 6 is optimal and 2H=8. The checker's code and frozen output were inspected, not run; the exact-subset and transfer tests are finite corroboration. The broken inline rendering of the floor formula in the proof does not change the correctly displayed formula or missing any argument.

## originality

PASS

Bounded pass for the uniform exact lower bound at n≥5 with 4∤n, for all m≥3. The n=3 rook subcase and the 4|n subcase are already covered, as are the factor formula and upper bound. The width-two example is a boundary witness, not a novelty claim. None of the inspected stronger statements gives the equality for the remaining cycle lengths. The fibre-run count provides the additional argument.

## value

PASS

This identifies a uniform equality family for a stated Cartesian-product bound and explains why partial fibres cannot beat the total-domination construction even when the universal lower bound leaves a gap. The nonzero residue classes, unrestricted clique widths and width-two boundary make this a structural exact invariant rather than a small table or the re-expression of the cycle value alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
