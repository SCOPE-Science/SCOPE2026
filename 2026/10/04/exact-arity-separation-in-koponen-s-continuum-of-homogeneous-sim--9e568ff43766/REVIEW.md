# Independent mathematical audit

## correctness

PASS

Constraints H_j with j>=n have at least n+1 vertices, so below arity n the two ages are identical. At size n+1 only H_n can differ. From the defining failed triples, any embedding H_m->H_n with m<n would have to send 0 to 0 and embed the entire directed m-cycle induced by failures into the directed n-cycle; successor-closure forces the full n-cycle, so no proper such embedding exists. In H_n, 0 is fixed by every automorphism and the positive vertices form a directed n-cycle, hence Aut(H_n) is exactly its n rotations. Therefore one forbidden isomorphism type removes \((n+1)!/n\) labeled structures. Homogeneity identifies these with injective ordered-tuple orbits. Allowing repeated coordinates gives the Stirling transform \(b_k=\sum_j {k\brace j}a_j\), preserving the first nonzero difference. A fresh independent finite reconstruction for n=3,4,5,6 gave automorphism counts 3,4,5,6 and labeled-copy counts 8,30,144,840, matching the symbolic formula; the finite check is corroborative only.

## originality

PASS

Best-of-knowledge comparison found Koponen's construction and general orbit/age background but no theorem that gives the first differing tuple arity or the exact factorial gap. The audited result adds a finite-orbit invariant calculation for the constraint coding, not merely a relabeling of the construction. The primary paper's full text was not materially available in this run, so the possibility of an unindexed remark in the source remains an explicit residual risk rather than negative evidence.

## value

PASS

Finite orbit profiles are a natural oligomorphic invariant of homogeneous structures. The theorem identifies exactly when the continuum coding first becomes visible to that invariant and by how much, while also showing arbitrarily long finite-profile agreement among continuum many nonisomorphic members. This is a motivated structural refinement of the construction rather than an arbitrary small-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
