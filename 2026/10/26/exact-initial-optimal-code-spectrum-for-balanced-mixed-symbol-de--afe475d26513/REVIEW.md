# Independent mathematical audit

## correctness

PASS

A balanced length-(n−2) subsequence of a balanced length-n source deletes exactly one symbol of each value; there is no multiplicity of an output as a constraint. Pairwise disjoint output shadows are therefore exactly the cliques of the compatibility graph. I inspected RESULT.md:30–48, VERIFICATION.md:19–25 and check.py:18–95,119–142, including the proper-color prefix bound and the exhaustive recursive partition by last chosen vertex. I independently built each output's source support by greedy subsequence matching, rather than deletion-position pairs, and ran exact integer-mask search on all five lengths and both channels. At n<=8 I branched on an output support: either use none of its available sources or use a unique one and remove its entire conflict neighborhood. A cover of candidates by fewer supports than the remaining target is a valid prune. At n=10 I used independent pairwise-conflict layers on a run-count-ordered source list and partitioned search nodes by the last selected vertex, rejecting only when remaining layers cannot meet the target. The complete mixed target search and target+1 exclusion at n=10 visited 600388 and 200216 nodes respectively; it replayed 666 distinct optima and no size-11 code. All lengths reproduced A=(1,2,2,6,10), M=(2,1,40,3,666), and orbit-size histograms for sizes 1/2/4 of (0,1,0),(1,0,0),(2,5,7),(1,1,0),(0,15,159). Taking the four reversal/complement images and checking their codebook membership gives the claimed orbit counts; the printed size-ten representative belongs to the independently found set. The arbitrary-deletion targets and one-higher exclusions also replayed exactly (1,1,2,4,8). The frozen replay path is check.py as documented in VERIFICATION.md in the record directory, not executed for this review; its mixed-only assertions do not check the arbitrary-deletion comparison or the specific printed representative. This audit's independent search did check both. No claim extends to n>10 or to an unbalanced source universe.

## originality

PASS

The distinct result is the complete finite maximum-codebook and symmetry census for the conditional mixed-deletion channel on balanced inputs, together with its evaluated exact maxima. The graph formulation, unrestricted two-deletion studies and the mixed-symbol case analysis as a decoding mechanism are prior. No exact conditional census or dominating exact theorem supplying its values was found in the inspected passages and catalogue matches.

## value

PASS

The conditional, balanced binary channel is a natural composition-constrained problem, and the initial range through 252 source words gives a reproducible exact benchmark. The gap from arbitrary deletion is explicit, the complete census records which optima are genuinely distinct up to natural symmetries, and a concrete length-ten optimum is provided. This motivates the precise finite slice without implying an asymptotic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
