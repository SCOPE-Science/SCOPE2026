# Independent mathematical audit

## correctness

PASS

Five EF rounds need extension over at most four distinct previously selected vertices; smaller patterns are obtained by padding. Conversely a failed pattern refutes its rank-five universal-existential extension sentence. Deleting the only witness, or a non-anchor when there were none, proves the two-witness necessity. The q=5 edge case falls outside the phrasing 'more than five' in Step 1, but deletion leaves four vertices and the rank-five sentence asserting five distinct vertices fails, while a four-anchor pattern can never have two witnesses in P_5. In the tail calculation singleton sums vanish, each of six pair sums is -1, four cubic and one quartic Weil estimates cost 11 sqrt(q), and excluded anchors cost at most 32. The lower bound is greater than 2 at 241 and increasing thereafter. Square and nonsquare affine multipliers normalize a four-set to 0,1,a,b, with nonsquares only complementing the checked pattern. I inspected rather than ran the supplied scripts. A separately written exact program, /workspace/reviews/paley_reproduction.py, generates prime powers and finds its own irreducible moduli, constructs adjacency using squares, and partitions by three anchors before tallying both signs for the fourth. Its run reproduced all 30 minima below 241, including 181 with minimum 2 and 125 with minimum 1. It also reproduced witnesses [4] in the published F_125 representation and [11,81] at 89. Thus there is no uncovered range or reliance on a spot check.

## originality

PASS

The distinct claim is the exact all-prime-power classification for two four-point witnesses, especially the failure after deletion at 125. The rank-five interpretation is standard and the least successful ordinary Paley order 89 and the positive two-witness case 121 have direct indexed overlaps, so neither constitutes separate novelty here. Prior multiple-witness inequalities already imply a positive tail. They do not determine the exceptional low field or the exact robust classification in the inspected statements.

## value

PASS

One-vertex deletion robustness is a natural next invariant of a classical pseudorandom family. Its exact all-order range is useful for finite rank-five approximants and not determined by the usual tail bounds. The singleton at 125 makes the robustness margin genuinely different from the ordinary extension property and shows an actual failure after deletion amid successful orders; this is not an arbitrary truncated census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
