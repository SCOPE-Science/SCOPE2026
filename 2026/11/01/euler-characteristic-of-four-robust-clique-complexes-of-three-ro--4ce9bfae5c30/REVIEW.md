# Independent mathematical audit

## correctness

PASS

The five masks 0,1,2,4,5 are exactly the independent last-column masks. The state stores the constrained maximum independent set size, with −1 for impossible masks; only consecutive columns interact and their masks must be disjoint. Capping and then rejecting at 4 is sound since no extension can reduce the untruncated independence number. Surviving column selections are in bijection with the faces and carry signed weight (−1)^|S|. An independent standard-library reconstruction (independent_transfer_check.py, run with python3) enumerated 54 reachable states and 260 unaggregated surviving transitions, computed all 54 coordinates of A(A−I)^4 1 to be zero, and recovered t_1,…,t_4=0,0,4,20. Independent vertex-subset enumeration at widths 2 and 3 returned 0 and 4. The vector identity implies Δ^4 t_n=0 for every n≥1, so interpolation gives binom(2n−2,3) at every width, not just the tested ones. The empty face changes the Euler convention to reduced Euler characteristic −t_n. Both frozen checkers and VERIFICATION.md were inspected and were not executed. The result verifies an Euler invariant, not a wedge or any separate Betti number.

## originality

PASS

The supported distinct claim is the universal reduced Euler characteristic for the three-row, four-robust family. The exact widths 3 through 6 are already covered by stronger homotopy computations, including material same-day overlap at width 4. Those computations do not prove the all-width formula. The published rectangular theorem is for k=2,3, and the edge-only theorem excludes the relevant corner-gluing pattern; the neighboring general wedge conjecture is not a theorem and does not alone fix the number of spheres.

## value

PASS

Three rows are a natural first strip with two-dimensional grid corner attachments beyond the edge-only theorem; k=4 is just beyond the established rectangular k=2,3 range. The exact invariant detects a uniform cubic structure and gives a necessary sphere count for any future five-sphere wedge proof. It is useful without solving that conjecture, and the vector certificate makes it an all-width result rather than a recomputation of the known small grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
