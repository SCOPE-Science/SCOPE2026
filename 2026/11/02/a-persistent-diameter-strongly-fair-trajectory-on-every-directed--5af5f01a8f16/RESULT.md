# A persistent-diameter strongly fair trajectory on every directed opinion cycle

## Finding

**Theorem.** For every integer \(n\ge3\) and every family of fixed influences \(p_0,\ldots,p_{n-1}\in(0,1)\), the directed cycle with arcs \(i-1\to i\) (indices modulo \(n\)) admits an edge-strongly-fair infinite asynchronous opinion trajectory, starting at \((1,0,\ldots,0)\), whose diameter is at least \(3/4\) after *every individual edge activation*. In contrast, for the bidirected two-agent cycle, every infinite trajectory converges to consensus, without any fairness requirement. Thus three agents and three arcs suffice and are the minimum respective sizes for such a counterexample among strongly connected loopless digraphs.

The construction covers the sparse, exactly-one-in-neighbor case and arbitrary fixed strictly interior influences. It strengthens a known qualitative strong-fairness counterexample by providing this structural graph family and an all-time quantitative separation.

## Assumptions and scope

For each \(n\ge2\), place opinions \(x_i\in[0,1]\) on vertices \(i\in\mathbb Z/n\mathbb Z\). The only allowed arc into vertex \(i\) is \((i-1,i)\). An activation of that arc makes the simultaneous-state update
\[
x_i^+=(1-p_i)x_i+p_i x_{i-1},\qquad x_h^+=x_h\quad(h\ne i).
\]
All \(p_i\) are fixed throughout a trajectory and strictly between zero and one. An infinite activation word is *strongly fair* if each arc occurs infinitely often. The opinion diameter at discrete time \(t\) is \(\Delta(t)=\max_i x_i(t)-\min_i x_i(t)\). Every activation, including repetitions of the same arc, counts as one unit of time. The scheduler is deterministic and may have unbounded intervals between successive uses of an arc.

## Proof

**Step 1: ideal copy schedule.** Temporarily replace a repeated weighted activation of arc \((i-1,i)\) by the exact copy map \(C_i\), which sets coordinate \(i\) equal to coordinate \(i-1\) and leaves all other coordinates untouched. Begin at the binary opinion vector \(y^{(0)}=(1,0,\ldots,0)\). For every nonnegative integer \(j\), execute the following two ideal copy blocks, with indices modulo \(n\):
\[
C_{j+1}\quad\text{followed by}\quad C_j.
\]
At the beginning of the pair there is precisely one unit-valued vertex, \(j\), and all others are zero. The first copy creates a pair of adjacent ones at \(j,j+1\). In the second copy, vertex \(j\) copies vertex \(j-1\), which is zero because \(n\ge3\), leaving precisely the unit-valued vertex \(j+1\). Thus the schedule rotates the unit singleton through all vertices and repeats. Every directed arc occurs exactly twice in each period consisting of \(2n\) ideal blocks. At *every* ideal block's beginning, among the \(n-1\) vertices **other than that block's target**, at least one has value zero and another has value one: for a growth block the source singleton is untouched, and for a shrink block the remaining unit of the adjacent pair is untouched.

**Step 2: uniformly summable approximation.** Enumerate the ideal copy blocks by \(m=0,1,2,\ldots\), writing \(i_m\) for the block target. Choose any positive integer \(N_m\) such that
\[
(1-p_{i_m})^{N_m}\le\varepsilon_m:=2^{-(m+4)}.
\]
Such \(N_m\) exists because \(0<1-p_{i_m}<1\). Replace the ideal block \(C_{i_m}\) by \(N_m\) consecutive activations of the same corresponding arc. If the block begins at \(x\in[0,1]^n\), its endpoint agrees with the copy map except at target \(i_m\), and the target discrepancy is exactly
\[
(1-p_{i_m})^{N_m}\bigl(x_{i_m}-x_{i_m-1}\bigr).
\]
Hence the block's uniform approximation error is at most \(\varepsilon_m\). Each ideal copy map is nonexpansive in \(\ell_\infty\). By induction, the difference between actual and ideal states at the beginning of block \(m\) is bounded by
\[
\sum_{h=0}^{m-1}\varepsilon_h<\sum_{h=0}^{\infty}2^{-(h+4)}=\frac18.
\]
The induction compares the same ordered *block* states; it does not mistake a finite sequence of single activations for one ideal activation.

**Step 3: persistence at every activation.** Fix an arbitrary block. By Step 1, there are two non-target coordinates whose ideal values at the beginning of that block are zero and one. By Step 2, their actual values are respectively less than \(1/8\) and greater than \(7/8\). Neither of these coordinates changes during the entire repeated-arc block, so their difference remains greater than \(3/4\) at every intermediate time. This also covers all block endpoints and proves \(\Delta(t)\ge3/4\) for every integer \(t\ge0\). Every block is finite, but there are infinitely many blocks; the single-action trajectory is well-defined for all time, and every arc is activated at least twice in every full block-cycle. The trajectory is therefore strongly fair but never approaches consensus.

**Step 4: sharp two-agent contrast.** On the bidirected two-vertex cycle an activation updating either vertex multiplies the absolute difference of opinions by precisely \(1-p_i\). For fixed \(p_0,p_1\in(0,1)\), letting \(q=\max\{1-p_0,1-p_1\}<1\), after \(t\) arbitrary activations \(\Delta(t)\le q^t\Delta(0)\). Moreover the minimum opinion is nondecreasing and the maximum nonincreasing under every convex combination, so both have a common limit and both coordinates converge to it. One vertex is trivial. A strongly connected loopless digraph on three vertices has at least three arcs, and a directed three-cycle attains this bound.

## Verification

The accompanying `verify_cycles.py` implements the exact recurrence using rational arithmetic, including every intermediate activation. Its deterministic tests cover cycles of sizes \(3,4,5,7\), heterogeneous influence fractions and two complete ideal rotations, asserting exact ideal support, summable error, and \(\Delta\ge3/4\) at every update, together with two-agent diameter contraction. Run using `python verify_cycles.py` (Python standard library only). The symbolic all-size proof in Steps 1–4, not the finite tests, establishes the theorem for infinitely many vertices and updates.

## Relationship to prior work

Aranda, Betancourt, Díaz and Valencia's opinion transition-system model defines this asynchronous convex-combination arc update and strong fairness as infinitely recurring activations. Their Proposition 9 / Construction 10 establishes non-consensus on a three-agent **four-arc** graph with a central vertex that can be influenced from either side. The present theorem concerns a **three-arc oriented cycle** (and every longer oriented cycle), so every vertex has exactly one in-neighbor; it supplies an explicitly summable block approximation and a uniform lower diameter throughout all individual activations. It neither asserts the earlier existential failure is new nor conflicts with that work's convergence theorem under the stronger \(m\)-bounded-fairness property. Generic ergodicity and randomized gossip results also do not supply a deterministic arbitrary-weight, strongly fair directed-cycle certificate in the inspected materials.

## Limitations

This is an existential adversarial-schedule result, not a claim that random activation fails with positive probability. The scheduler can have unbounded stretches of repeated activations, and the result does not apply to bounded fair or \(m\)-bounded-fair schedules, for which earlier convergence theorems apply. The precise constant \(3/4\) is a convenient quantitative separation, not an optimality bound; any fixed tolerance whose sum is small enough yields other positive bounds. The result assumes fixed edge influences strictly between zero and one, a loopless oriented cycle, and exact deterministic state updates. Priority relative to specialized uncatalogued matrix-product literature remains to be independently checked.

## References

- J. Aranda, S. Betancourt, J. F. Díaz, F. Valencia, *Fairness and Consensus in an Asynchronous Opinion Model for Social Networks* (technical report), arXiv:2312.12251, first submitted 19 December 2023. https://arxiv.org/abs/2312.12251
- J. Aranda, S. Betancourt, J. F. Díaz, F. Valencia, *Fairness and Consensus in an Asynchronous Opinion Model for Social Networks*, CONCUR 2024, LIPIcs 311, article 7, DOI:10.4230/LIPIcs.CONCUR.2024.7. https://doi.org/10.4230/LIPIcs.CONCUR.2024.7
- B. Chatterjee and E. Seneta, *Towards Consensus: Some Convergence Theorems on Repeated Averaging*, Journal of Applied Probability 14 (1977), 89–97, background on stochastic matrix products; no claim of a complete source comparison.
