# Independent mathematical audit

## correctness

PASS

Properness confines each color class to one part. A vertex in another part witnesses every vertex of that class, so the strong-odd neighborhood multiplicity forces odd class size; the converse is immediate. A part of size n needs 1 odd block when n odd, 2 when even, proving chi_so=r+e for r>=2. Allocate disjoint k_i labeled colors to parts, multiply odd-fiber onto counts A(n_i,k_i), sum over parities and K<=q. At the optimum odd parts use 1 and even parts 2, giving (r+e)!*2^{sum_even(n_i-2)}. Direct independently implemented small case K_(2,2,1), q=5, returned 120 admissible labeled colorings as does the closed formula; infinity rests on proof, not enumeration.

## originality

PASS

The inspected introductory source literature records only a complete-bipartite chi_so<=4 estimate and special graph joins, not the full multipartite all-q enumerator or exact even-part parity minimum. The published Resultary result on ordinary neighborhood-parity odd coloring is a weaker different invariant and does not imply strong-odd counts. This is best-of-knowledge, with simple-proof/unindexed prior risk.

## value

PASS

A natural established graph-coloring invariant is completely classified for every complete multipartite graph and every labeled palette, including nontrivial enumeration beyond just the minimum; this is useful as an exact family benchmark even though the core characterization has a short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
