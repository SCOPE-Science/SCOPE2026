# Independent mathematical audit

## correctness

PASS

The list constraint is on distinct transmitted words per length-five output, not on deletion patterns. For each nonnegative certified vector y, set z_w=(1−Σ_u a_{u,w}y_u)_+. On any admissible code, summing Σ_u a_{u,w}y_u+z_w≥1 gives |C|≤LΣy+Σz. Integrality and |C|≤256 permit the floor of the minimum. An independent exact replay in /workspace/branches/53425eac-f557-4e76-9c2f-f492bac5ccb0/replay_capacity.py read the frozen certificate as data and reconstructed all incidence entries, checked the six nonnegative duals and rational intercepts, and checked each separately listed feasible witness for L=1,…,93 for cardinality equal to that floor. Its log is replay.log in the same directory. It reproduced transitions at 4,12,30,35,53 and the cap at 93. At L=0 every prospective word has at least one output, excluding a nonempty code. For a fixed output, greedy matching of its next bit (with an arbitrary continuation after the fifth match) is a success or failure on each of eight steps. These eight success/failure bits biject with the eight input bits, giving Σ_{j=5}^8 binom(8,j)=93 matching input words. Thus the whole set is infeasible below 93 and feasible at and above 93. The exact certificate and these endpoints prove the all-integer profile; neither continuous LP optimality nor enumeration of all optimal codes is asserted.

## originality

PASS

The supported distinct claim is the complete fixed-block all-list profile, including the six-line bound with integer attainment and the full finite witness range. The closest matching indexed result covers exactly the L=2 slice at n=8. The inspected primary results cover the model and general bounds, not the exact all-L theorem. This is bounded comparison, not a statement of absolute priority or novelty of each individual list value.

## value

PASS

The list limit interpolates between unique three-deletion correction and inclusion of every binary 8-bit word. Determining the entire interpolation for the natural 32-output incidence problem, not just one chosen allowance, provides a concrete tight benchmark for finite list-code bounds and optimization. The successive rational bounds, saturation cutoff, and exact constructions for every allowance make the benchmark reusable without an optimizer. No asymptotic benefit or larger-block theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
