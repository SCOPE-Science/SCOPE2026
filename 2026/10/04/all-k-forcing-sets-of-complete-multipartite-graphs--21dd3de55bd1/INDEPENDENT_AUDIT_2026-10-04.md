# Independent mathematical audit

## correctness

PASS

The first force must occur from a black vertex in one part \(V_i\), so before any color change it sees exactly the whites outside \(V_i\). Its force clears all outside whites; the remaining whites are precisely those in \(V_i\), and a now-black outside vertex can clear them exactly when their count is at most \(k\). This proves necessity and sufficiency. Maximizing whites gives \(\min\{k,n_i-1\}+\min\{k,N-n_i\}\). At the optimum, a part witnesses a minimum set exactly when its within-part white count attains the first cap, so inclusion-exclusion gives the stated count. Fresh literal dynamics checked 42,640 cases through order seven.

## originality

PASS

Best-of-knowledge originality passes. The foundational k-forcing paper gives general bounds, while the 2024 automata paper treats the complete bipartite case and states minimum-set behavior there. Neither inspected source gives an arbitrary complete-multipartite all-set first-force criterion or the inclusion-exclusion count of all minimum sets.

## value

PASS

The theorem gives a compact all-set decision rule for a standard propagation process, not merely its minimum parameter, and it counts all optimum initial sets on an arbitrary complete multipartite profile. The two-part and \(k=1\) slices are established prior territory, while the arbitrary-profile structural rule and optimum multiplicity are natural reusable extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
