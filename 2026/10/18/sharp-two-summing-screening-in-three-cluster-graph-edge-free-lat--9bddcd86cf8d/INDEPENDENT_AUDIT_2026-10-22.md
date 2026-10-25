# Independent mathematical audit

## correctness

PASS

The domain is real Euclidean R^{2a+b}, the lattice element is the supremum of all absolute graph-edge differences for K_{a,a,b}, and the FBL^{(2)} norm uses the weak-l2 test-family contraction constraint. Expanding l2 duality over individual maximally active edges gives a nuclear norm of a weighted incidence matrix. Its squared singular values are precisely a probability-weighted graph Laplacian L_mu; this proves pi_2(D_G)=max_mu tr sqrt(L_mu) without any symmetry assumption. Matrix square-root trace is concave; averaging over the graph automorphism group restricts the objective to two edge orbits parametrized by s∈[0,1]. Direct invariant subspace diagonalization gives eigenvalues (1+s)/(2a) of mult 2a-2, (1-s)/b of mult b-1, (1+3s)/(2a), and (2a+b)(1-s)/(2ab); the zero constant eigenvalue is excluded. Their square roots produce exactly Phi_{a,b}(s). Strict concavity yields unique optimal orbit mass. The derivative at s=0 compares H_{a,b} with (2a+1)/sqrt(2a); verified monotonic H(b) and bracketing b=2a+1 and 2a+2 give the stated sharp integer threshold. At s=0 the trace matches the complete bipartite graph; for s>0 strict concavity forces larger norm. The witness z=(1,-1,0) across parts confirms different lattice functions. Independently assembled six rational/float Laplacian spectra and nine neighboring integer cutoffs and checked the exact analytic derivative sign. These tests corroborate, rather than replace, nuclear-norm duality and infinite-parameter threshold proof.

## originality

PASS

The publicly indexed exact Löwner-ellipsoid computation solves the SAME K_{a,a,b} edge-orbit Laplacian eigenvalues but maximizes log determinant, not trace sqrt. Its screening begins at b>=2a+1, whereas the current free-lattice two-summing screening starts at b>=2a+2, so prior metric ellipsoid implication is demonstrably insufficient. The FBL2 norm definition and its summing-map relation are prior, but they do not supply the new spectral-design optimization or cutoff.

## value

PASS

Two-summing norms of finite graph incidence operators are natural operator-ideal invariants, while free-lattice edge generators are canonical examples. A nontrivial sharp integer screening criterion in which pointwise extra generators remain active but norm becomes insensitive distinguishes this invariant from an already solved Löwner design on the same graph and supplies a structurally motivated exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
