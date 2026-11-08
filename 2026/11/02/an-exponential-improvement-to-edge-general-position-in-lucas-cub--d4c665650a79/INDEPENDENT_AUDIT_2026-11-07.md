# Independent mathematical audit

## correctness

PASS

For n>=5, identify Lucas cube vertices with independent sets of cyclic positions; delete u\v then insert v\u to get an admissible path of Hamming length, hence every geodesic flips each coordinate at most once. The selected edges are all theta_0, theta_1 with coordinate n-1=0, and theta_(n-1) with coordinate 1=0. Their three-coordinate projections are distinct spokes 000-100, 000-010 and 000-001; a shortest path cannot revisit projected states since each coordinate is changed at most once, so cannot use all three spokes. Selected edges are edge-general-position. Independent-set counts on paths give F_(n-1)+2F_(n-2)=L_(n-1)=2F_(n-1)+F_(n-4). Exact pairwise shortest-path dynamic programming checked all vertex pairs for n=5..8, selected sizes 7,11,18,29. This proves a lower bound only, not gp_e equality.

## originality

PASS

Klavžar–Tan 2023 gives two whole coordinate classes and bound 2F_(n-1) for all Lucas n, plus equality 7 at n=5. The restricted three-class star witness beats their formula by F_(n-4) in n>5. General theta-class and network bounds do not directly imply this restricted construction; possible equivalent later construction remains a priority risk.

## value

PASS

The original Lucas-cube paper identifies a nonsaturating two-class lower bound and an n=5 exception. The new all-dimension three-spoke construction closes a motivated gap with exponentially growing additive improvement F_(n-4), a structural geodesic proof and a natural standard graph invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
