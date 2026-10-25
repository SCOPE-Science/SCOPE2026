# Independent mathematical audit

## correctness

PASS

For each word w(i,j), deletion of a one leaves exactly one weight-1 output if adjacent, two otherwise; hence ℓ+2e≤n-1. Two adjacent double-one words have a common weight-2 output after deleting their distinct exterior zeros, so ℓ≤ceil((n-1)/2). Combining gives |C|≤n-1-floor((n+1)/4). The stated U_r=(2r,2r+1) and V_s=(4s+1,4s+4) achieve equality; their remaining-one locations are disjoint and their zero-deletion shadows have disjoint adjacent/nonadjacent gap classes and distinct first-one bands, including n=2 boundary. Independent brute-force compatibility search computed exact maxima n=2..7 and verified construction; no finite test substitutes for the all-length shadow argument.

## originality

PASS

Classical Sloane/VT work treats unrestricted one-deletion binary codes. Gómez Soto et al. optimize packings in a double-vertex graph for adjacent transpositions, which is not this deletion descendant-intersection relation: explicitly different confusability pairs arise even at n=4,5. A September 2026 multi-deletion paper optimizes an unrestricted, stronger error channel, not the fixed-weight-two exact n-formula. No primary theorem inspected dominates it, with residual obscure older coding-table risk.

## value

PASS

Determines a natural exact constant-composition one-deletion capacity at every blocklength with a sharp local obstruction and uniform construction; the second path-packing obstruction is needed beyond elementary one-shadow packing, so it is not only standard VT repackaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
