# Independent mathematical audit

## correctness

PASS

A singleton needs only an unbordered word. For any code, length-one exclusions force opposite endpoints within each word and a common first symbol across words; bit complementation preserves both conditions. This proves the one-orientation reduction. With self-overlaps excluded at vertex construction and both ordered overlaps excluded at each edge, a clique is exactly a feasible code. In the supplied search, every color class is independent, so after removing later vertices the remaining improvement is bounded by the current color index. Branching on a vertex and restricting the child to its neighbors covers every potentially improving clique. I independently built the bitwise graph for both orientations, with fresh upper-bound search and witnesses, recovering all 55 target values and all ten d=1 controls. The full n=11 graph had 568 vertices, 284 in each orientation. The n=11 row at d=2..11 is (42,14,10,4,2,2,2,1,1,1); A(10,1),A(10,2),A(11,1),A(11,2)=(24,23,44,42). All 55 frozen certificates were separately checked against both ordered overlaps, self-overlap, the exact lengths, cardinality and Hamming distances. The two single-deletion comparisons in RESULT.md also check directly. Replay /workspace/review-work/frontier.py 2 11 1, saved output frontier_results.txt. This verifies binary aligned Hamming constraints only, not frame recovery after a substitution.

## originality

PASS

The complete binary joint frontier, in particular the optimized n=10 and n=11 tradeoff, is distinct on inspected evidence. Credit earlier coverage of A(9,2)=14, the already established d=1 controls, and the prior 42-word construction giving A(11,2)>=42. No individual originality is claimed for previously determined or elementary cells. The novel comparison is simultaneous strict overlap exclusion and aligned distance, not the definition, problem framework, or use of a clique reduction.

## value

PASS

The joint optimization is motivated by simultaneous strict synchronization constraints and within-block substitution tolerance. The complete short-block profiles identify exactly where even distance-two enforcement costs codewords and give a sharp n=11 aligned one-substitution capacity of 14, not obtainable from the known unconstrained optimum or generic separation bound. Some high-distance cells are immediate from the orientation, and A(9,2) was known; neither supplies the salient remaining optima. The checked profiles are useful design benchmarks without asserting synchronization under corruptions at unknown boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
