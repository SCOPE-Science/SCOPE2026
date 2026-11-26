# Independent mathematical audit

## correctness

PASS

On a primitive temporal four-orbit every vertex is excited exactly once in a cyclic four-word: excitations are separated by at least three steps; a never-excited site remains resting and forces its neighbors never to excite, impossible on the connected graph unless all-zero. The local rule precisely forbids adjacent opposite phases and requires an adjacent predecessor phase at every vertex. A row must be bichromatic (otherwise every column contains all globally present phases); rotate its colors to 0,1. The phase-0 cell's predecessor 3 is in its column in a second row. That 3 must find phase 2 in its own row, not in its column above a 0, and this 2 must be in a column with first-row phase 1. The two colors 3,2 then fix the entire second row in agreement with the two column classes. These reference rows restrict all other rows to {0,3} on one class and {1,2} on the other; opposite-phase exclusions force exactly the first or second row type. Conversely the cyclic rectangle labelling meets both phase conditions, and each vertex's four-word has least period four. The partitions are recoverable from the labelled phase array, and phase rotation removes only the phase origin, leaving two cyclic orders per pair of unordered bipartitions. The independent NumPy transition-table enumeration, with exact ternary integers and phase recovery from actual trajectories, checked all 20,280,861 configurations on the nine frozen boards and reproduced all counts; this is corroboration, not the all-size proof. The frozen C++ guard should not be taken as supporting arbitrary 20-cell tests, since signed int cannot represent 3^20; none of the nine samples exceeds 15 cells, so that does not affect the recorded calculation or statement.

## originality

PASS

The supported distinct claim is the rigidity and shift-only count on every labelled rectangular rook graph, not the novelty of the square-board integer sequence or the 4-by-4 count. The inspected general excitation results give activity or existence of waves, not the phase-array rigidity or exact orbit count. The two strongest exact Resultary neighbors are later: one gives a census of the same dynamics on one rook graph, and the other counts the same period on the complete bipartite graph itself, not its line graph. The latter even gives the same two-parameter numeric period-four formula, but its proofs about shore adjacency do not mechanically classify row/column cliques of the line graph. Remaining historical/equivalent-formulation risk is acknowledged.

## value

PASS

Period four is the first nontrivial period above the intrinsic three-state firing/recovery cycle, and rook graphs form a natural two-parameter family with overlapping large cliques. The theorem gives a complete structural classification, not just an exact count or an observed firing rate: exponentially many orbit states are all determined by two independent labelled cuts and orientation. It explains the known finite-board numbers and computes an exact dynamical invariant for arbitrarily large boards without enumerating configurations. Neither the scope nor the significance depends on a claim about other periods or basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
