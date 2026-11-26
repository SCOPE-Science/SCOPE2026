# Independent mathematical audit

## correctness

PASS

Normalize the initial hub color to zero. A clique containing all three colors rotates rigidly and never loses a color. In its co-rotating hub frame, the leaf phase 2 stays at 2, 0 goes to 2, and 1 goes via 0 to 2. The full orbit therefore has least period three, with one entrance time 0,1,2 for each labelled initial clique phase. Inclusion–exclusion on the nonhub word requires both colors 1 and 2 and gives Q_r possible words. Three hub phases give 3Q_r states per oscillatory layer and Q_r orbits, with layers (3,3,3) in each. For a non-rainbow clique, after one update: with only zero initially on the clique, leaf phases 0,1,2 give T=0,2,1; with color 1 present and 2 absent, the clique becomes all 1, and only leaf phase 1 is already synchronized; with color 2 present and 1 absent, all nonhub vertices become 0, and only leaf phase 1 leaves a mismatch, resolved on the next update. This gives 1, 3·2^r−2, 3·2^r−2 states per initial hub color for the fixed sector. Color equivariance makes the three fixed basins have identical layers. A zero clique with a phase-1 leaf attains T=2, and period three occurs for r≥2. At r=1 the census, time bound and fixed basin formula hold with Q_1=0; conditioning on p=3 is not defined there. Fresh graph-edge enumeration and generic functional-graph decomposition checked all 29,511 labelled colorings at r=1,…,7, including each individual basin (branches/replay_pendant.py). The frozen support/direct output logs separately report the 21 support cases and 2,391,471 labelled states through r=11; the universal count comes from the proof.

## originality

PASS

The ordinary finite-graph circulation theorem already separates the two sectors and bounds the consensus entrance time by the diameter. Related indexed statements include the very same iterate identity on complete multipartite graphs, temporal basin counts on book graphs, and the same number of cyclic basins of total size nine at one leaf under a different update rule. None of the inspected statements gives the pendant-clique threshold-one CCA transition classes or the per-orbit labelled (3,3,3) entrance profile. Credit is for the complete first-entry census and its individual basin refinement, not for the general fixation criterion or the short iterate identity in isolation.

## value

PASS

Adding the smallest pendant perturbation to a rotating-clique system preserves the number of oscillatory orbits but creates a width-independent nine-state basin with two nonempty transient layers, exactly as large as the recurrent layer. The orbit-level first-entry profile is a useful exact timing invariant that period and activity bounds do not resolve; the fixed-sector count completes the labelled census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
