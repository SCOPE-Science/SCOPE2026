# Self-review

## Correctness
PASS. The level partition is an exact equitable quotient because every vertex at one side/level has the same neighbor multiplicities. Equal heights give central-edge symmetry; adjacent heights make the taller root the center of a regular-tree ball. With a gap of at least two, round \(a+1\) leaves paired leaf-distance classes plus one core. In the next round the core endpoints split because their multiplicities toward the paired boundary are \(d\) and \(1\). Core refinement then proceeds inward from both ends, while the endpoint asymmetry propagates back through the paired classes. These independent strict-split clocks are exactly \(\lfloor(a+b+2)/2\rfloor\) and \(2a+3\). The stable cells are explicit automorphism orbits. The standalone checker confirms 2,500 quotient instances and 32 full graphs.

## Originality
PASS with residual priority risk. Repeated published-finding corpus searches using double-Bethe, joined perfect-tree, equitable-partition, color-refinement, \(1\)-WL, and Weisfeiler--Leman terminology returned no matching result. The inspected Bethe-tree literature is spectral, while Krebs--Verbitsky supplies only the general refinement/universal-cover framework. Current and prior archive ledgers contain no double-Bethe claim. The closest private result is the spider-tree depth formula, but the present family has no degree-distinguished central junction; that difference creates a new three-regime phase transition and the \(2m+3\) delayed-propagation term.

## Value
PASS. The result gives a closed all-parameter iteration law on a standard exponentially branching tree construction and exhibits a nonmonotone-looking phase structure invisible from vertex count alone. Most notably, the answer is independent of branching factor, yet changes qualitatively when the two heights move from equal, to adjacent, to separated by at least two. The separated regime is governed by two simultaneous propagation clocks, giving a structural explanation rather than a finite table.

## Closest literature and limitations
Krebs--Verbitsky (2014) is the methodological source for refinement depth. Rojo--Medina (2006) and Rojo (2007) are object-side Bethe/generalized-Bethe sources. No inspected source states the exact iteration law. Generalized level-dependent branching and unequal branching factors remain outside scope.

Self-review: passed. Independent audit: not yet performed.
