# Independent mathematical audit

## correctness

PASS

Recomputed the ranks by decomposing the regular module into subspaces of paths with a common terminal vertex. At vertex j≥3 the basis (e_j,u_{j−1},v_{j−2}) gives a triangular block with the only possible nonzero entries a_{j−1}, a_{j−2}, b_{j−2}. Its rank is e+f+(1−e)(1−f)η_{j−2}, with e=ε_{j−2} and f=ε_{j−1}, and its square has rank ef. Vertex two adds ε_1 to the rank and zero to the square rank; vertex one contributes zero. Regrouping the arrow contributions gives weight 2 for each active arrow except weight 1 for the last. For each pair, summing over b gives 1+(q−1)X if both arrows vanish and q otherwise, with a Y factor exactly if both are active. This gives the displayed initial row, interior transitions and different final transition. Directly at n=3, q=2 the eight triples give 1+3X+2X²+2X³Y. For n=1 the radical is zero, and n=2 has a rank-one operator exactly when the sole arrow coefficient is nonzero. Since L_x³=0, ranks r,s give block counts s,r−2s,D−2r+s. Square-zero means no adjacent active arrows; choosing j nonadjacent positions among n−1 gives the stated binomial coefficient, and the length-two coefficients are free. The proof uses only whether field coefficients vanish and works also for non-prime q. Frozen RESULT.md lines 20–42 suffice to replay the argument. The accompanying prime-field checker was read, not run; its cap and prime-field scope do not certify the theorem.

## originality

PASS

Bounded pass for the full joint regular-action rank census on the open path. Closely related censuses either impose different boundary conditions or count another operator. The standard square-zero specialization is not a separate originality basis.

## value

PASS

The full Jordan census of radical multiplication is an exact invariant of the natural regular module. It gives rank-stratum sizes over every finite field by a fixed-size recurrence without enumerating radical elements, and exposes the effect of the endpoints of the chain. Neither the finite checks nor the standard independent-set specialization supply this value on their own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
