# Independent mathematical audit

## correctness

PASS

For each shorter circular separation r<n/2, the two branches of D_n give the disjoint consecutive ranges (r-1)n+1 through (r-1)n+r and (r-1)n+r+1 through rn. The even antipodes fill the final n/2 ranks. Substitution of the two images of {i,n-1}, with the singleton assigned rank zero, verifies the transition table, including the odd i=(n-1)/2 and even i=n/2-1 junctions where the unique minimum rise occurs. Away from n-1, a decreases rank by one and b is a loop. Thus the descending letter is forced for shortest words and the path visits precisely the ranks down to one. Telescoping rank up to the first merge shows that slack equals the number of idling letters plus the sum of 1+rise over upward jumps, plus the arbitrary suffix length. This proves the window, the loop generating factor and the factor 1/(1-2z) for the two suffix letters. At first excluded slack from the highest rank, only the unique smallest upward jump can occur and it exhausts slack, so it adds exactly one word; n=2 separately merges on the first b. The frozen verification files were inspected and not executed. Replay the separate exact checker with python3 /workspace/branches/d3d3be15-a159-46e6-a087-318aee507dd5/independent_pair_dp.py; the saved independent_pair_dp_sweep.txt records agreement for every pair and allowed slack at 3<=n<=10, including the first sharp correction. The proof, not this finite sweep, covers all n.

## originality

PASS

The distinct contribution is the state-dependent count of all near-shortest words merging a fixed pair, with the growing sharp slack window and its first exact defect. The shortest-word uniqueness and distance spectrum are materially covered by existing indexed findings and do not earn originality credit. No inspected result gives the count or makes it a direct specialization of an existing enumeration.

## value

PASS

The coefficient describes the entire low-slack fixed-pair language of a canonical synchronizing automaton rather than one word or a tiny case. It quantifies when idling and post-merge extensions exhaust all near-optimal words, and locates exactly when and by how much a real detour first changes the count. The growing cutoff and its sharpness are structural information beyond the Hamiltonian shortest path.

The dated certificate retains the supplied scientific assessment, sources and limitations.
