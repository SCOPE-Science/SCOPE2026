# Independent mathematical audit

## correctness

PASS

Take the first k columns as blue. At stage t>=k, vertices (a,t-k+1) on each rail uniquely force (a,t+1), giving Z<=2k. Construct X of 2(ell-k) window rows and 2ell vertex columns using u0=(1,0), uk=(1,1), interior u=(1,3); v0=(1,-1), vk=(0,1), interior v=(3,7). Disjoint windows force zero off-diagonals at column gap>k; at gap k same-rail inner products 1 and -1 are nonzero while cross-rail inner products vanish. At gap<k exact contributions are nonzero: rail-one positive, rail-two at most one negative -4 offset pairing with +7 or +58 terms, cross-rail either positive or one -2 supplemented by nonzero +10/+24. The square submatrix restricting to two vertices per column of first ell-k columns is block triangular with 2x2 diagonal [u0,v0] determinant -1, so X full row rank. Gram A=X^T X has exact graph off-diagonal support, PSD rank 2(ell-k), nullity 2k. The universal inequalities M+<=Z+<=Z and M<=Z trap all equalities; 100 independently reconstructed finite Gram support profiles corroborate but do not replace the uniform proof.

## originality

PASS

Statement/implication comparison, not mere title search. Closest inspected antecedents give related machinery or narrower/scalar/qualitative statements, but not the full asserted theorem; coverage and inaccessible-source limitations are explicit.

## value

PASS

The exact two-row infinite family resolves the first nonpath width of the motivating grid-power zero forcing conjecture and supplies a simultaneous positive semidefinite minimum-rank realization, an independently useful inverse-eigenvalue certificate rather than a mere restatement of an upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
