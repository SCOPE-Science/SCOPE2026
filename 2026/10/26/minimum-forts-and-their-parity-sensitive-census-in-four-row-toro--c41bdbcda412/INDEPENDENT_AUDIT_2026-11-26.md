# Independent mathematical audit

## correctness

PASS

The local three-column condition exactly tests every outside vertex, including n=3 where the two horizontal neighbors are distinct. Consecutive empty columns force the all-empty walk. With (0,0) removed, fixed labels correspond bijectively to walks rooted at column zero; the sum of reduced costs is |F|-n. I independently rebuilt the transfer certificate using set-valued columns, mutual reachability and walk traces (replay: python3 /workspace/branches/replay_2.py). It confirmed 255 states, 2671 admissible edges, nonnegative reduced costs, no tight loops, bipartite recurrent components of sizes 4,4,10,10, and characteristic polynomials t^4-1 and t^10-t^8-2t^6, each twice. Tight odd walks are impossible. The alternating opposite-row pairs attain the claimed size: each empty column is flanked by identical selected masks, also at odd wraparound, and every outside vertex in a selected column has two vertical neighbors in the fort. Trace of T^n gives the even formula. For odd length, each rooted walk has exactly one cost-one edge; cyclic invariance of trace gives n times tr(B(T^2)^m). The independent two-step walk counts give h_1=6, h_2=10 and all 255 residual zeros. Cayley–Hamilton for the 255-dimensional matrix T^2 propagates those zeros to every subsequent index, so this is a finite certificate for the all-order recurrence, not extrapolation. Translation averaging and the uniform 1/f_n weights give the fractional corollary. The frozen script was inspected, not executed.

## originality

PASS

The supported distinct contribution is the labeled minimum-fort census for the width-four family, not the general fort-transversal interpretation, vertex-transitive fractional formula, or the already covered four-cube member. No inspected prior statement supplies the all-order parity formula.

## value

PASS

On a natural fixed-width torus the complete census determines the multiplicity of sharp forcing obstructions, distinguishing parity and divisibility by four. It resolves an all-order counting question substantially beyond the known bounds and the one hypercube case, with a replayable finite-state mechanism that separates tight walks and a single defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
