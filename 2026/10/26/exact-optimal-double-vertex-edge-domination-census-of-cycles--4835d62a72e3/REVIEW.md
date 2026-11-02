# Independent mathematical audit

## correctness

PASS

For n>=5 each edge-neighborhood union is the four-block {i-1,i,i+1,i+2}; double counting its selected incidences gives |D|>=ceil(n/2). Cyclic selection every other vertex attains this. For cyclic gaps d_i between selected vertices, the every-four-block constraint is equivalent to d_i+d_{i+1}<=4. With e_i=2-d_i in {-1,0,1}, require e_i+e_{i+1}>=0 and sum e_i=2k-n (zero for even, one for odd). Every minus is flanked by plusses; each nonzero run separated by zeroes has positive total; this forces the stated all-2 or cyclic 1,3 patterns. An odd alternating run with r threes has r+1 ones and remaining 2s, yielding k cyclic anchored words and exactly n labeled sets per r. Exceptions C3,C4 checked directly. Independent exhaustive actual edge-neighborhood enumeration n3..15 verified 223 minimum sets and no smaller feasible sets. There is no reliance on the transfer counts to prove the infinite classification.

## originality

PASS

Best-of-knowledge comparison after fresh Resultary searches, focused primary-source proof inspection and explicit implication checks. A related method, family or parameter alone does not establish identity/coverage; historical risk remains noted.

## value

PASS

For a standard redundant vertex-to-edge coverage constraint on cycles, the complete labeled minimizer count, orbit structure and exact alternating-gap classification answer a mathematically natural enumeration/optimization question not resolved by the elementary minimum cardinality. Distinct parity classes give drastically different optimizer multiplicities and symmetry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
