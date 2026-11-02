# Independent mathematical audit

## correctness

PASS

For distinct variables and lax team semantics, dep(x_1)∨...∨dep(x_r) holds precisely if r coordinate hyperplanes, one per coordinate, cover the team. A noncoverable possibly infinite team has a finite noncoverable subteam by induction on r using a base row s* and counterwitness sets T_i of rows differing in coordinate i. For an inclusion-minimal finite noncoverable F, covering F\{s} after deleting s yields a_i(s) distinct from s_i, and P_s(X)=∏_i(X_i-a_i(s)) evaluates nonzero at s and zero at each other row. These |F| multilinear polynomials are linearly independent in a 2^r-dimensional space, implying |F|≤2^r. The Boolean cube {0,1}^r itself is noncoverable, but every proper subset is coverable by choosing complementary hyperplanes of an excluded row; sharp. Independent complete enumerations for (arity,alphabet) (1,4),(2,2),(2,3),(3,2),(4,2) corroborated obstruction sizes and diagonal evaluations; the polynomial proof is universal.

## originality

PASS

Fröhlich–Kolaitis–Meier CSL 2026 Corollary 23 derives coherence 4 for two constancy atoms. The present theorem proves and realizes 2^r for arbitrary r, and does not claim r=2 novelty. Barlag et al. 2026 study broad coherence/first-order rewritability and may hide an equivalent general formula; only abstract/secondary exposition was accessible and authorized Oxford access was VPN-disconnected. A generic multilinear-polynomial injection is classical, but this exact application and all-arity sharp obstruction are not derived in material read. PASS is risk-qualified.

## value

PASS

The sharp worst-case finite witness size gives an exact, all-arity compactness/coherence cutoff for a natural logical fragment. The polynomial method cleanly separates large minimal obstructions from smaller ones (e.g. both size 3 and 4 when r=2), and supports sound finite-subteam testing over arbitrary structures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
