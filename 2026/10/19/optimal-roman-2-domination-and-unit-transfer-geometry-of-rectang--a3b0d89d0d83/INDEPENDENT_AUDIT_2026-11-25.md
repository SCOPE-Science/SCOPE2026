# Independent mathematical audit

## correctness

PASS

Pass for the narrowed files in repairs/3. At a zero cell the sum is r_i+c_j; if some column is empty then every row has weight at least two, otherwise every column has weight at least one. Checking equality and attainment gives the recalled optimizer families, with the intersection counted by assigning exactly two labelled columns to each row. In the square regime the states are permutation matrices and no one-unit transfer can produce a different permutation matrix. For n>m the onto-map graph is connected: first match target fibre sizes using surplus rows whose sizes stay positive, then interchange columns between target fibres. If one donor has size at least two the swap uses two single-column moves; for two singleton fibres borrow a spare column from a third nonsingleton fibre, perform the swap, and return the spare. When n=2m the two connected families share balanced placements, which suffices regardless of extra cross-family edges. When n>2m every minimum has fixed row weight two, so no transfer can change rows. One row is the graph of size-two multisets with distance half the L1 multiplicity difference. A disjoint-support target establishes eccentricity two in each row, and distances add. Repeated and distinct pairs have n-1 and 2(n-1) neighbors respectively, yielding the degree histogram by choosing k distinct-pair rows. The proof is uniform in 2<=m<=n. The frozen support files give documented finite corroboration, not an infinite proof; italian_rook_check2.py sums formula-derived row degrees rather than independently rebuilding every move. Replay paths for the supplied tests are python3 italian_rook_check1.py and python3 italian_rook_check2.py in the source package (source inspected, not executed in this review). No result here for sliding-only transfers or all optimal distances outside the strict product regime.

## originality

PASS

Pass only for the narrowed unrestricted unit-transfer theorem. The original minimum, complete equality cases, and counts are directly covered by Resultary 73393dbef1b4, on a parameter range that includes the frozen range, and are now explicitly attributed background. The published classification fixes the states; it does not give the legal paths between onto maps, connectivity through the critical union, or quantify transfer distances. The product invariants are consequences of the transfer characterization, not new domination values. The inspected same-graph perfect and power-domination results use different feasibility or moves. This is a content comparison, not a determination of exact priority from catalogue date labels.

## value

PASS

A fixed optimal weight need not permit any legal redistribution. The recovered theorem proves that one extra column changes the landscape from m! immobile optima to a single component, with valid transfer paths also at the mixed-family boundary. For wider rectangles the exact rowwise transfer costs and local branching are available for all optimal states. That makes the result useful independently of the already covered minimizer census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
