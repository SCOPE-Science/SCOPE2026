# Independent mathematical audit

## correctness

PASS

At r≥1, the Edmonds inequalities x(E)=n−1, x_e≥0 and x(E(S))≤|S|−1 turn reflection membership for every spanning tree x into (r+1)c_e≥1 and (r+1)c(E(S))≤r(|S|−1): max_T x_e=1, min_T x(E(S))=0 by an outside-rooted star. Summing n co-singleton inequalities forces r≥n−1; c_e=2/n attains equality. At equality all co-singletons are tight and yield vertex degree c(δ(v))=2(n−1)/n. The exact z_e=nc_e−1 transform enforces z≥0, degree n−1 and cut lower bound F_n(s)=s²−ns+2n−2. The s=2,n−2 cases give edge cap z_e≤n−2; at n=6 s=3 gives z(δ(S))≥1; all interior s at n≥7 have F_n(s)≤7−n≤0 by convexity. A split of K6 into internally 5/2-weighted triangles violates the triple cut, with reflected star violating the original induced-edge inequality by 21/10>2. A K7 3+4 split, internal weights 3 and 2, is allowed despite a zero crossing cut. Triangle relations show unsigned incidence rank n and affine dimension |E|−n=n(n−3)/2. Checked the actual RESULT.md and verify.py Git blobs; finite Prüfer and rank tests are corroboration only, not all-n proof. All quantifiers and boundary n=3,4,6,7 cases are addressed.

## originality

PASS

Best-of-knowledge originality PASS for the complete K_n spanning-tree/base-polytope *minimizing-center locus* and six-vertex cut exception, not for Edmonds' inequalities or Minkowski asymmetry itself. Matroid independence polytopes, rank-two bases and general facet/reconstructibility results have different hypotheses and do not imply the full rank-(n−1) complete-graph center family. Resultary self-entry is not independent priority evidence. Unindexed equivalent affine-symmetry/optimization formulations remain possible.

## value

PASS

An all-n explicit affine center polytope in dimension n(n−3)/2, with a necessary—and uniquely exceptional—nontrivial cut at n=6, is a genuine structural convex-geometric classification for canonical graphic matroid base polytopes. The essential exception and sharp K7 contrast make the invariant mathematically motivated rather than a parameter substitution or numeric microgain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
