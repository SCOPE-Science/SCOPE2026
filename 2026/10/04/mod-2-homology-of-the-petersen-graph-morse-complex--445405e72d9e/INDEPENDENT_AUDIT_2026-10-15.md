# Independent mathematical audit

## correctness

PASS

The graph has 15 edges/30 oriented incidences and Morse faces are rooted forests. A separately recomputed Petersen Laplacian coefficient expansion (1+2t)^5(1+5t)^4 yields exactly the face vector (1,30,390,2880,13305,39882,77640,94800,66000,20000). The pinned artifacts/verify.py blob f58933d4a3c4a8e59cbe743337f8c1f1129a11f2 explicitly builds all 4^10 assignments and F2 augmented boundary ranks (1,29,361,2519,10786,29096,48544,46256,19706) with opposite pivot conventions; inspecting its boundary assembly and rank algorithm shows that those exact ranks imply Betti 38 and 294 in dimensions 7,8. The later fully read integral wedge computation independently entails the same mod-two ranks. The entire 314928-face rank routine was reviewed but not rerun in this execution; full numerical rerun remains a reproducibility limitation, not an asserted alternative proof.

## originality

PASS

No source published before the 2026-10-04 finding was found covering its *ordinary* Petersen Morse-complex F2 homology. Scoville-Zaremsky gives connectivity bounds; Donovan-Lin-Scoville gives other graph families. A 2026-10-11 published integral wedge theorem does imply the exact pair but explicitly recognizes the 2026-10-04 mod-two result as earlier prior work; later implication is not retroactive prior art. The similarly named Petersen graph configuration-space Morse calculation concerns a different object.

## value

PASS

The Petersen graph is a canonical cubic, nonplanar, vertex-transitive graph, and full F2 homology of its ordinary Morse complex is a natural exact invariant not determined by connectivity theorems. The later integral wedge computation explicitly relies on/preserves these Betti numbers, demonstrating use as a meaningful finite benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
