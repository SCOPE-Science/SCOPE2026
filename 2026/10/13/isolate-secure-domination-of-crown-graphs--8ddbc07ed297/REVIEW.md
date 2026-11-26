# Independent mathematical audit

## correctness

PASS

Use closed domination and require the result of a defender swap to have some selected isolate, not necessarily the same isolate. If a_i is isolated, it confines the selected B-side to {b_i}. With no b_i, domination forces all of A. With b_i, each omitted a_j can swap only with b_i, and the resulting one-sided set dominates only if a_j was the unique omission. In that case an attack at b_j leaves at least two A-vertices with b_i and b_j for n>=4; b_j sees every remaining A-vertex, and b_i sees at least one, ruling out isolation. If the A-side was full, an attack at any b_j different from b_i leaves both selected B-vertices with neighbors and every remaining A-vertex with a B-neighbor. Conversely, for A a swap against b_i can remove any a_j with j different from i, preserving domination and leaving a_i isolated; B is symmetric. For n=3 the same confinement and forced first swap leave only the two sides and triples consisting of a deleted pair and one other vertex; each such triple succeeds (for A={a_i,a_j,a_k}, S={a_i,a_k,b_i}, the attacks a_j,b_j,b_k can be defended by b_i,a_k,a_i respectively). Hence there are exactly 14 sets of size 3. Read VERIFICATION.md, verify.py and verify_output.txt. The frozen verifier's n=3 count is printed rather than asserted; separately enumerated all 63 nonempty subsets at n=3 and 255 at n=4 by a bit-mask check, obtaining 14 and 2. The frozen code was not run; its recorded range is 3<=n<=7 with additional side checks through n=50.

## originality

PASS

The supported distinct claim is the full swap-feasible family on crowns n>=4 and the boundary census, not the definition, nonexistence on complete bipartite graphs, or the already implied numerical minimum at C6. In the strongest checked same-graph sources, the conditions are ordinary minimal domination, semitotal domination, or secure total domination; none entails preserving an isolate under a defender swap.

## value

PASS

A perfect-matching deletion is a natural symmetric change from a dense bipartite nonexistence case. The result gives a rigid all-set transition, not only the minimum: the new non-neighbors can preserve an isolate in a swap from a full side, but every mixed candidate for n>=4 fails. The exceptional 6-cycle shows exactly where this rigidity begins and separates the new census from the known numerical cycle invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
