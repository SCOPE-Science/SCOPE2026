# Independent mathematical audit

## correctness

PASS

On deleting uv, the only external influence on u's component is whether v is selected. After choosing u's bit s, each child sees that bit; u is dominated exactly when p, s, or some child selection is true. If dominated, the child edges pass automatically; if undominated, every child must be unselected and dominated. This gives the four stated finite-entry types including the zero-child base case. The last aggregate tracks the cost of at least one selected child by associative Boolean-OR convolution. Prefix/suffix products on incoming messages exclude precisely the outgoing neighbor, costing O(sum deg) time and space with arc-indexed storage, and applying p=0 at a whole-tree root gives both constrained costs even for n=1. Theorem 3.2 of arXiv:2606.21190 has the stated nonstar scope and closed-neighborhood criterion. Independently, one can combine the two directed messages of any edge with external bit t for the new subdivision vertex: if d_x=t∨s_u∨s_v, require (d_u∨d_x) and (d_v∨d_x) and add t to the sum of the component costs. That verifies the linear-time consequence directly by constant work per edge. A separate component-product DP and subset enumeration agreed on 177 trees including 792 actual subdivisions (python3 /workspace/evidence/review_checks.py 2); finite corroboration only. repairs/2/RESULT.md changes emphasis and prior-work attribution, not the proven algorithm or scope.

## originality

PASS

The repaired claim credits prior classification of vertices in all or no optimum vertex-edge dominating sets on trees. The supported distinct deliverable is a fully specified linear-time simultaneous numerical profile (every J_v and K_v), not the class labels per se, generic rerooting, or the previously proved subdivision criterion. The closest older classification paper is inaccessible in full; complexity, recurrence and numerical outputs there remain an explicit priority risk.

## value

PASS

The corrected presentation supplies an explicit input-linear algorithm for the full constrained optimum-size profile, which gives quantitative information beyond membership labels. It also closes the specific algorithmic case identified by Dettlaff et al. without performing a separate optimization for each vertex, and gives the requested linear-time recognition rather than claiming a new general paradigm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
