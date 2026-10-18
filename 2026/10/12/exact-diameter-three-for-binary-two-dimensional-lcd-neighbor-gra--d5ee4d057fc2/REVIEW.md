# Independent mathematical audit

## correctness

PASS

For binary dot product q(z)=B(z,z)=B(z,w) and T(z)=z+q(z)w, the Gram determinant of span(c,z) is q(c)q(z)+B(c,z)=B(c,T(z)). For each LCD 2-plane C, if T(z) not in C^perp and z not in C, some c in C yields a one-line-intersecting LCD plane containing z. To connect arbitrary C,D it suffices to choose z outside C,D,T^{-1}(C^perp),T^{-1}(D^perp). For even n, T invertible (T(w)=w when n even), so each preimage dimension n-2 and total excluded ≤2^{n-1}+7<2^n. For odd n, T has kernel span(w), image w^perp, each preimage is proper dimension ≤n-1 (because LCD C cannot lie entirely in span w, and T(C) relation), and union of two proper subspaces has ≤3·2^{n-2} points; plus7<2^n for odd n≥5. Thus diameter ≤3. Explicit disjoint planes C=<e1,e2>, D=<e1+e2+e3,e3+e4> are LCD and no span(c,d) for nonzero c,d is LCD, ruling out common neighbors. Perpendicular complement preserves distances for k=n-2. Independently enumerated exact graph diameter 3 for n=4 (20 vertices) and n=5 (80 vertices); infinite theorem uses counting proof.

## originality

PASS

Best-of-knowledge PASS: The exact 2026 LCD neighbor graph primary paper (all 32 pages lawfully accessed) proves regularity and connectedness for binary q=2 (Corollary 4.1/Theorem 4.2) and treats odd-characteristic structural graphs, but does not state a binary k=2 diameter or 3-step path bound. Earlier Resultary edge-regularity theorem gives common neighbors for adjacent vertices only, which cannot force a distance for disjoint vertices. The odd-field diameter min{k,n-k}=2 does not extend to char2; inspected binary witness demonstrates deviation.

## value

PASS

PASS: It resolves the first nontrivial dimension of a natural coding-theoretic neighbor graph, quantitatively strengthening connectedness and exposing a sharp characteristic-two global-metric obstruction, with explicit general-n construction and duality. This is not a trivial rewriting of regularity or finite small-case data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
