# Independent mathematical audit

## correctness

PASS

PASS. Two-list constraint is row capacity <=2 for the distinct-output binary two-deletion incidence matrix A_n. An independent exact BigInt rational checker reconstructed all 256 columns/64 rows for n=8; validated the explicit 15-codeword witness, all 46 nonzero fractions in feasible primal, and 40 root nonnegative dual weights. Both objectives equal 2188/135. It independently traversed ALL 205 certificate nodes (102 exhaustive binary branches, 103 rational leaves), all residual-capacity and forced-zero rules and leaf bounds below 16, proving M8=15. Rechecked all n=2..7 integer witnesses and exact rational dual bounds 2,3,4,4,36/5,666/59, so floor(F_n)=M_n below 8; n8 floor(F8)=16>15. These exact finite certificates, not solver logs, prove this precise domain.

## originality

PASS

PASS best-of-knowledge. Lin 2026 full eight-page primary paper defines precisely t-list k-deletion codes and the deletion hypergraph, but proves asymptotic size lower bounds (Theorem 1.1) and general subsequence counts rather than finite blocklength-eight integer/LP disparity. Guruswami-Hastad address asymptotic two-deletion construction. Prior exact result M6=7 is accounted for and does not imply M8=15 or fractional optimum. Specific older packing tables remain a risk.

## value

PASS

PASS. Earliest failure of naive integer rounding in a canonical deletion-shadow fractional packing relaxation is a motivated structural finite threshold. Exact dual/primal and 205-node independent exclusion certificate make it a reusable benchmark rather than an isolated unproved optimizer claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
