# Independent mathematical audit

## correctness

PASS

For every zero rook cell, r_i+c_j=2 is exactly the closed labeling condition because neighbor sum excludes its own zero label. A zero row and zero column cannot coexist. Square case: n minimum weight forces every row and column sum 1, yielding n! permutation matrices. For 2<=m<n, all rows and columns positive if weight<2m; any row sum>=2 must be completely positive (since positive columns forbid zeros), yielding weight>=n+m-1>=2m, whereas all row sums 1 contradict n positive columns. For equality: a zero column forces all row sums 2 and only fully filled columns, hence one 2-column or two 1-columns. With no zero columns, the weight bound h(n-1)<=m forces a single all-one full row at n=m+1; zero equations force nonheavy rows to select a common column. Independently reconstructed definition-level bounded cases (m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5), matching counts 2,12,10,15,6,22,15 and no lower weight; finite cases only corroborate all-parameter proof.

## originality

PASS

Best-of-knowledge PASS for a complete structural classification and counting, not for scalar domination values already computed. Compared row/column conditions, equalities and graph class to relevant original Cartesian-product paper and published same-topic records. No evidenced prior theorem implies all optimizer families/counts.

## value

PASS

The minimum value alone does not reveal whether every optimizer is column-supported or when mixed row-column solutions occur. The complete equality classification and sharp n=m+1 extra-family threshold is a natural exact structural refinement of a well-studied domination invariant, not merely parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
