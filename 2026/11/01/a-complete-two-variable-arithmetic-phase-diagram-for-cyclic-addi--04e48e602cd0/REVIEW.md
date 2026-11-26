# Independent mathematical audit

## correctness

PASS

For the repaired file, the universal claim and proof are unchanged and check out. Every two-variable ternary atom reduces to a zero predicate on x or y or a bit for y=2x or x=2y; equality is the remaining bit. In the CRT decomposition doubling on the odd factor is a permutation, and the 2-primary factor gives exactly a levels, with one off-cycle child per root and two children per positive-height internal vertex. The root counts are 1 for fixed, 2 for two-cycle when present, and at least 4 for longer cycles when present. With one anchor, same-level cyclic diagrams distinguish equality, both directions on a two-cycle, and separate forward/backward neighbors on a longer cycle. A longer-cycle root always has an unrelated root of its color. At different heights there are at most two incident competitors in any target color, so for a long-root color a nonadjacent target always survives; for fixed and two-cycle colors the exact cardinalities are known. For all colors this gives identical sets of possible anchored atomic diagrams at matching a and phase. It handles coincident pebbles and initial placement, hence works at every depth. Leaves lie at height a for a>0; a path of length j from a leaf reaches zero exactly for j≥a (extend by the loop), and paths of length a select exactly periodic vertices. For a=0 there are no leaves. The mutual-edge and nonfixed, nonmutual periodic tests then separate the phases, and the least odd parts are 1,3,5,9. The original Verification paragraph erroneously read three unary-refinement rounds as sentence rank three. A rank-(d+1) sentence tests the spectrum of unary types of rank d, with its outer quantifier contributing one; conversely finite observed unary types of rank d can be tested by characteristic formulas and an outer existential. Independent reproduction by generating all eight ternary substitutions directly gave 17 mismatches at unary rank two (in particular, moduli 32 and 64 agree on all rank-three sentences), and none at unary rank three over all 12,720 sampled modulus pairs. Thus rank four, not three, is the exact sample threshold. The complete corrected RESULT.md is under /workspace/repairs/5/ and the diff affects only the Verification paragraph; the frozen code, output and VERIFICATION.md remain unchanged. Independent reproduction listing: /workspace/fo2_rank_reproduction.js (matching calculation run in a JavaScript runtime; Node is not installed locally). Additional bounded pair-state comparison of moduli 1,2,3,5,7,9,15: /workspace/branches/839faaa5-1741-468e-838b-1ea2a6d08320/fo2_color_check.py. Both experiments are finite; neither certifies the unbounded theorem. Frozen scripts and snapshots were inspected, not executed.

## originality

PASS

The final constant-free, counting-free theorem for all cyclic moduli survives the repair; the corrected sample-rank observation is not relied on as an independent original finding. The closest catalogue work on permutation digraphs already accounts for the odd-modulus part by specialization; the audited contribution is the complete arithmetic classification including all 2-primary depths and the extension of odd phases through incoming trees. Other exact and broader results were compared by vocabulary and structure, not by date.

## value

PASS

The ternary relational language is a natural encoding of cyclic addition, and the result identifies exactly which arithmetic survives a two-variable restriction: every step of the two-primary height is visible, but odd periods collapse to four phases even after binary predecessor trees are attached. It supplies explicit full-depth equivalences between nonisomorphic addition relations and least representatives within the model family. The repair only corrects how to interpret the bounded check, not this structural contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
