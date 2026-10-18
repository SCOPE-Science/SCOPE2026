# Independent mathematical audit

## correctness

PASS

For nonempty binary non-overlapping codes, length-one prefix/suffix restrictions force a common first bit and opposite last bit; complementation normalizes to 0...1. All self-unbordered normalized words of length 2..n form vertices of the compatibility graph, with incompatibility exactly cross-prefix/suffix overlaps or substring containment. Cliques are exactly admissible codes. The package ordered bitset recursion uses independent color classes as legitimate clique upper bounds and shortest remaining lengths as legitimate total-length lower bounds, with no incomplete stopping rule. An INDEPENDENT sparse 0/1 MILP reconstructed all conflict pairs and proved optimality with solver optimal status and zero MIP gap at all nine n=2..10: (m_n,T_n)=(1,2),(1,2),(1,2),(2,9),(3,16),(5,32),(8,59),(14,119),(24,227); candidate count at n=10 is 295. Thus the finite exact result, with explicit 13 length-9 and 11 length-10 witness words at n=10, is correct. The MILP exact optimum is finite and does not prove results n>10.

## originality

PASS

The exact nine-order joint capacity/bit-length optima and the strict n=10 saving (227 versus 240 bits) are not a direct statement or corollary of the primary general cardinality-transfer and mean-length bounds, nor the located fixed-length or ternary single-order records. This is best-of-knowledge originality, with an unread plausible construction source explicitly retained as risk.

## value

PASS

At maximum synchronization codebook cardinality, total transmitted bit cost is a motivated natural integer invariant; exact optima for nine successive orders solve a finite extremal problem rather than recomputing a known table. The n=10 optimum of 227 saves 13 bits relative to uniform-length 24-codeword realizations and identifies a reproducible boundary for future improved constructions. No general capacity theorem is needed for this finite exact fact to be mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
