# Independent mathematical audit

## correctness

PASS

If e_i encodes the rim direction and s_i the outgoing spoke from the hub, the prescribed rim parity forces s_i=1+p_i+e_(i−1)+e_i mod 2. Hence every choice of rim bits determines one orientation, and even total indegree forces the hub parity to be the rim parity sum. A directed cycle through the hub must follow a rim path from spoke bit one to spoke bit zero, so its first 1-to-0 transition gives a directed hub triangle. Any cycle avoiding the hub is the directed rim. The corrected proof explicitly includes the possible directed rim triangle for m=3. The trace counts every labelled cyclic assignment once by the paired-state overlap and forbids exactly the local hub triangles. A constant rim-direction assignment can survive this local test only with constant spoke bits, equivalently constant p, giving the subtraction of two. Constant spokes in the solvable even-sum cyclic system e_(i−1)+e_i=q_i construct both complementary nondirected rims when q≠0. For odd m a choice of common spoke direction always gives even q-sum; for constant p the odd-degree source/sink obstruction is exact. For even m and odd p-sum a zero-parity site can be the unique incoming spoke and a rim source in the solvable cyclic system, forbidding all triangles. For even m and constant p, the hub is forced to be a sink or source, leaving exactly the two alternating rims. Fixed 4×4 products take O(m) arithmetic operations, not necessarily O(m) bit operations. The repair fixes the false universal assertion about triangles at m=3 without changing any claim or count.

## originality

PASS

Bounded pass for the labelled wheel fibre formula and exact feasibility boundary. A later wheel Fourier result supplies the same counts by an explicit reduction; it is genuine later coverage, not evidence of prior coverage. The same-day open-path fan result is particularly close in method but not a theorem about the closed rim; no priority is inferred from its date.

## value

PASS

Wheels are a natural simple closed-rim test family for parity-constrained acyclic orientation. The new information relative to feasibility or total counting is sharp labelled fibre multiplicity, in linear arithmetic time, with a complete obstruction and constant-vector boundary. The cyclic correction is required rather than a mere change of graph name from the fan recurrence; a researcher checking parity-refined counting on elementary planar families can use the exact formula and boundary counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
