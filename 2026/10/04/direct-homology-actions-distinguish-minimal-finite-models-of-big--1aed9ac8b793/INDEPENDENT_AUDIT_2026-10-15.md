# Independent mathematical audit

## correctness

PASS

Barmak–Minian’s six-point, eight-Hasse-edge minimum plus p+q=6,pq>=8 gives exactly K2,4, K4,2, K3,3 minus one edge. Each order complex is a connected graph with rank H1=8-6+1=3. An independent clean-room Python checker constructed from the source poset definitions (not just running the uploaded verifier) enumerated all 6^6=46656 set maps on each model, filtered monotone maps, mapped each fundamental-cycle chain on edges, extracted 3×3 integral H1 matrices, and checked inverse monotonicity and det ±1. Obtained 1782 selfmaps, 421 distinct matrices with ranks (1,84,288,48), 48 homology auto/homeomorphism maps for each opposite K2,4 model; K3,3-e yielded 646 maps, 113 matrices with ranks (1,60,48,4), 4 automorphism/homeomorphisms. All counts agree with inspected actual `verify.py` but come from independent enumeration, not logs.

## originality

PASS

Barmak–Minian classifies exactly the three minimal graph models but not their full direct continuous self-map integral H1 action sets; Bradley’s general monotone-map homology result does not supply these complete action semigroups. The related published five-point wedge-of-two-circles action census concerns a genuinely different homotopy type, model size, and rank-two homology action; no stronger matching published census found.

## value

PASS

This is a motivated natural classification of direct H1-action expressivity for *all* minimum-size finite models of the first three-loop bouquet where minimal models are not unique, giving a basis-independent model-dependence invariant and distinguishing 421 and 113 distinct integral actions. A complete finite census is valuable even without a general formula for larger bouquets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
