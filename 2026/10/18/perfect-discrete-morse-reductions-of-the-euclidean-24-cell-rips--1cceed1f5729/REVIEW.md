# Independent mathematical audit

## correctness

PASS

Fresh code independently generated the D₄ roots and integer adjacency, enumerated cliques by cardinality, replayed the frozen JSON, and topologically sorted each matching-oriented face poset. At squared cutoff 2 it verified (24,96,96), 96 pairs and critical vector (1,0,23), with 480 Hasse incidences checked. At squared cutoff 4 it verified (24,168,480,600,288,24), 791 pairs and critical vector (1,0,0,1,0,0), with 5760 incidences checked. Every nonempty face was consumed once. Replay: /workspace/branches/5b366b35-9eed-4007-88ed-31741e526210/independent_replay.py and replay-full.json in that directory. The uploaded verifier was read, not executed. In either sequence, the deletion time strictly increases along unmatched downward covers and is constant along matched upward covers, so the operation check proves acyclicity. One critical vertex and only top-dimensional critical cells yield the stated integral homotopy types at both scales. The distance histogram (96,72,96,12) at squared distances (2,4,6,8) gives the other stages, including the join of twelve antipodal pairs at cutoff 6. For the narrower repair all 23 critical triangles are maximal in the original first-scale complex and disjoint from the pairs, so they may be deleted first; retaining the unmatched vertex cannot add a coface of any nonempty face. The same 96 pairs then give the claimed spanning collapse without any changed certificate data.

## originality

PASS

Pass is for the repaired exact first-scale matching and spanning-collapse witness on the unsubdivided faces, not for the full filtration or perfectness at the second scale. The close 24-cell result 6421d0ac1ad1 gives the identical filtration types and a stronger marked collapse at radius 2, which already yields a perfect matching there. At radius √2 its wedge proof uses the two-skeleton and homological Whitehead theorem, not a matching on the 216 original faces. The thesis reports homology ranks, not the actual spanning subcomplex or reduction. No inspected source provided the first-scale witness retained here; this is a bounded conclusion, not a priority assertion.

## value

PASS

The retained datum is a complete optimal reduction of a natural geometric complex without subdivision, specifying exactly how to select top facets to leave a collapsible spanning subcomplex. A researcher can use the actual pairs or retained subcomplex to study explicit cells and attaching data, rather than working only from Betti numbers or an abstract wedge equivalence. The independent exact replay confirms the intended original-face structure; neither second-scale duplication nor the already covered homotopy types are credited as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
