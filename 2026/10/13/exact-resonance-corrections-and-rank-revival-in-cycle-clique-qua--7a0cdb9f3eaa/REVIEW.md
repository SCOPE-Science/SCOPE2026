# Independent mathematical audit

## correctness

PASS

For finite adjacency Hamiltonian of C_n square K_q (n>=5,q>=3), Fourier characters diagonalize the walk. The mixing-kernel Fourier eigenvalue rho_(h,j) equals the number of ordered equal-energy pairs (r,s) and (r-h,s-j) divided by nq. Cosine equalities give B_n(h): n at h=0, 1 at nonzero h for odd n, 2 for even n even h, 0 otherwise. Cross-clique bands need a cosine-energy gap q. For q>4 impossible by spectral range; q=4 only (2,-2), and q=3 algebraic-integrality and conjugate norm restrict to (2,-1),(1,-2), yielding the complete C_(n,q)(h) table. Hence rho_(h,0)=B/n, rho_(h,j!=0)=((q-2)B+2C)/(nq), correction positive semidefinite, rank nq for odd n; nq/2 for even n except q4,n=2 mod4 when rank nq/2+3. Independent direct Fourier equal-energy pair count checks for 5<=n<=31,3<=q<=8 agreed with all displayed values and exception masks. Infinite family relies on the algebraic-integer proof, not floating-point enumeration.

## originality

PASS

Godsil's general average-mixing matrix and spectral projectors are established; the new result specializes those tools to C_n square K_q and classifies all cross-band resonance parameters and rank revival. The inspected circulant bunkbed paper treats path–circulant products and average near-uniformity, not this graph family's complete characterwise spectrum. Potential coverage by a more general product-energy difference theorem remains a priority risk.

## value

PASS

Average-mixing rank and factorization are central quantum walk invariants. This sharp all-n,q phase diagram gives surprising rank revival at q=4,n≡2 (mod4) and separates factorization failure from rank increase, a structural classification reusable when studying continuous-time walks on Cartesian graph products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
