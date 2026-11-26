# Independent mathematical audit

## correctness

PASS

Independently reconstructed the rank and support argument in RESULT.md, lines 25–68. The SRG adjacency relation on the constant-orthogonal space gives the two roots r and s there. Primitivity implies 0<mu<k (mu=k would make equal open neighborhoods of nonadjacent vertices give complete multipartite classes), so r>0>s; s<-1 since A+I positive semidefinite would give unit Gram vectors equal along every edge, implying completeness by connectedness. With d=e_u-e_v and delta=c-1, the Laplacian update is delta dd^T and acts only on the two directions E_r d,E_s d, both nonzero by the projector formulas and adjacency of u,v. The restricted 2-by-2 matrix has nonzero off-diagonal for delta!=0, and the secular polynomial is nonzero at either old eigenvalue. The two new roots are therefore distinct from each other and the old nonzero eigenvalues; positivity of the connected weighted Laplacian rules out zero. Their resolvent eigenvectors have nonzero entry at an outsider exactly when A_wu!=A_wv, since the two denominators differ. At u and v the entries are ±1/(2 delta) for the chosen eigenvector scaling by the secular equation. For the two residual eigenspaces, choose an outsider x having equal adjacencies to the endpoints: common neighbors suffice if lambda>0, and otherwise (N-k-1)mu=k(k-1) with mu<k gives N>2k. Both projected d vectors vanish at x. For a vertex w of this outsider type, E_r e_w and E_s e_w have a strictly positive diagonal entry at w and hence cannot be parallel to the respective projected d. Otherwise pick such an x distinct from w; each off-diagonal projector entry at x,w is nonzero because its adjacency offset (k-s)/N or (k-r)/N lies strictly between 0 and 1, using the connected complement for k-s<N. This proves both residual modes exist and are visible from all vertices, without inferring visibility merely from multiplicity. The constant mode is always visible. A Vandermonde argument on the active orthogonal spectral projections gives the Krylov rank; at unit weight the three positive projector diagonals give rank three, and at nonunit positive weight only endpoints and exclusive neighbors add two modes. The exclusive-neighbor census gives 2+2(k-1-lambda), so the C5 and N>5 conclusions follow. The recorded 14846 exact finite checks and their script were inspected, not rerun or used in place of the proof.

## originality

PASS

The rank-one spectral splitting is genuinely covered by Godsil–Guo–Kempton–Lippner under a shift and parameter substitution; the eigenvalue-support rank criterion is also known. The distinct content is the every-vertex joint visibility and inherited-mode argument and thus the exact all-positive-weights rank and location census on primitive SRGs. Earlier indexed coverage includes an endpoint on C5, not that classification. This assessment is bounded to checked statements, not a global priority finding.

## value

PASS

The result gives an actuator-placement criterion depending only on how the vertex sees the defective edge, not on solving a weighted eigenproblem for each candidate weight or examining one graph realization. It resolves whether splitting the uniform spectrum actually produces additional reachable modes, quantifies how many actuator locations gain them, and proves that the gain never suffices for full single-input control beyond order five. The all-weights support result is useful separately from the established splitting and from endpoint examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
