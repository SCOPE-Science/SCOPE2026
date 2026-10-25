# Independent mathematical audit

## correctness

PASS

For every prime power q and k>=2 in the q-subspace disjointness graph qK_(2k:k), fixing A, the linear stabilizer acts transitively on U with fixed s=dim(U∩A). The direct-sum/graph description gives |O_s|=q^((k-s)^2)[k choose s]_q^2. Complements W of A are graphs of f:B→A, and W∩U=0 iff the induced restriction D→A/C is bijective (both rank k-s); this counts q^(k^2) product_(j=1)^(k-s)(1-q^(-j)) common neighbours, strictly increasing with s. Round one separates the anchor, all complements, and remaining vertices; round two splits by these common-neighbour counts. k=2 needs only one round, and k>=3 needs two because round one has three classes versus k+1>=4. These are unrestricted algebraic deductions, not inferred from finite test outputs. The actual source Git tree and RESULT.md/check_formula.py/check_refinement.py were inspected; arithmetic formula independently follows from GL rank counting.

## originality

PASS

Best-of-knowledge, subject to explicitly documented priority risks: searched the available Resultary records and primary literature, compared the exact claimed quantifiers/invariants to prior implications rather than matching titles, and did not treat inaccessible full text as proof of noncoverage.

## value

PASS

A sharp constant-depth orbit-recovery theorem over an entire geometrically natural q-Kneser family gives a useful refinement benchmark distinct from merely knowing the association scheme. It supplies orbit sizes, exact early-stabilization thresholds, and a direct certificate of what 1-WL learns from one named subspace. These are structural invariants, not a parameter rename.

The dated certificate retains the supplied scientific assessment, sources and limitations.
