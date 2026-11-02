# Independent mathematical audit

## correctness

PASS

Verified the final theorem for every unequal positive integer a,b (d>=3) in standard Euclidean coordinates. The radical parameters satisfy q-p=(b-a)/d and d(p^2+q^2)-2pq=d; their positivity follows from s^2-delta^2=2d(1-delta^2)/(d-1)>0. Symbolic independent algebra confirms Delta=AB-ab=abH/(pq)>0, F1-F2=H[(a-b)+d(q-p)], F1+F2=d+2pq-d(p^2+q^2), and the claimed covariance-diagonal differences are p F1/[d(1+p)H^2] and q F2/[d(1+q)H^2]. The off-block inverse is -1/Delta. Consequently all coordinate and cross normals have exact squared support equal to their slacks, proving containment, and distinct nonparallel supporting normals imply distinct relative-interior contacts. Direct facet weights gamma bp, gamma aq, gamma with gamma=d/(abH) are strictly positive, cancel the first moment and satisfy sum omega nn^T/r^2=gamma H^2 K=Sigma^{-1}. The actual Gruber–Schuster John criterion gives unique global maximum volume, not merely stationarity. The K eigenspace decomposition and det K=A^(a-1)B^(b-1)(AB-ab) give the full spectrum and volume; orthogonal reflection transfers to the order polytope. Independent SymPy factorization and separately written NumPy facet/moment tests on six uneven (a,b) instances (including one-element ranks) agreed within numerical roundoff; these finite checks are corroboration only. Source verifier was inspected but not treated as proof or executed blindly.

## originality

PASS

Best-of-knowledge: independent comparisons against full-text Ahmad–Fourier–Joswig and Mori on this exact maximal-ranked-poset family, full statement of the John criterion, and fully read published Resultary balanced (r=2,a=b) and balanced r>=3 multipartite results did not find an evaluated John ellipsoid for unequal positive biclique part sizes. The closed radical center, off-block inverse, explicit positive three-orbit weights, and four squared-semiaxis subspaces are not implications of f-vector results or the balanced-only cases. The generic John theorem is used as an optimality criterion but leaves the evaluated solution to prove. This is a qualified priority assessment, not proof of absence from all literature.

## value

PASS

Complete height-two posets with rank sizes a and b are a canonical infinite graph/poset family. The metric invariant is the unique standard-Euclidean maximum-volume ellipsoid (John ellipsoid), not a cosmetic rescaling. Unlike the already-known balanced case, a!=b has independent natural block sizes and generally different internal eigenspaces. The theorem provides a radical center, covariance, four block-spectral pieces (with legitimate zero multiplicities for singleton blocks), Euclidean volume, and a positive all-facet contact design, a natural complete classification and reusable exact calibration for polytope metric geometry. Face enumerations and balanced special cases do not imply it. The significance is this family-specific structural solution; no generalization to arbitrary posets or claim of a large new general theorem is required or made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
