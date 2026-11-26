# Independent mathematical audit

## correctness

PASS

Intersecting differently named lines through singleton colours makes their unique intersection a singleton in the next round. With C_0, C_g, and successive symbol lines this iterates (tg,0) to ((t+1)g,0), and then all of H² is distinguished. For the proposed partition, each line whose defining value is in H contains h singleton cells and n−h cells in its matching part. Each line defined by a value outside H contains one cell for each H-value in each of the other two line types; the two sets are disjoint (two values in H force the third in H), leaving n−2h cells in Z. This gives equitability for every named relation; past the singleton stage, relation counts against H² read the partial row, column and sum profile. The sizes and census follow, with Z empty exactly for k≤2. Any automorphism of the named relations has coordinate maps α,β with α(x)+β(y)=γ(x+y); subtracting the two translations gives a common group automorphism. Fixing the marks leaves units t with t≡1 mod h. For k≥3 the row-part witnesses (0,1),(0,2) cannot be joined by such a unit; for k=2,h≥3 use (0,1),(0,3). For (n,h)=(4,2), multiplication by 3 swaps the two elements of every nonsingleton part; k=1 is discrete. Independent exact checks for all 231 cases 2≤n≤22, 1≤g<n matched the whole partition and the orbit criterion, including 150 orbit-exact cases. Exhaustive permutation triples for n≤6 also agreed with the affine formula. Replay: python3 /workspace/branches/1ac146ad-a57e-4d05-885e-d46193229a72/independent_record3_check.py.

## originality

PASS

Best-of-knowledge pass for the combining of the exact cyclic subgroup partition and the complete orbit-exactness criterion for this named structure. The closest named Latin-square automorphism results concern different actions, and the inspected Latin-square equitable-partition work classifies a merged graph. The closest indexed two-root theorem is about Hamming graphs, not a group addition table with three named relations. No exact or dominating statement was found in the inspected evidence; this is not a priority certification.

## value

PASS

The theorem gives the entire local counting invariant for a natural marked group table, not just success or failure on particular orders. The orbit comparison exposes an infinite family where counts miss actual symmetry and identifies the sole nongenerator exception, with explicit same-colour different-orbit witnesses for both remaining index regimes. Those are useful distinctions when using refinement to approximate stabilizer orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
