# Independent mathematical audit

## correctness

PASS

Fort duality follows from the color-change rule: a stalled nonempty white set is a fort and no fort can be entered by a first color-change move. Independently enumerated all 2^20 subsets using adjacency for GP(10,2), exact fort test and a complete subset-zeta transform: 74170 forts, 804264 zero-forcing sets, polynomial coefficients k=6..20 exactly (2040,16900,62890,127480,168244,163560,125230,77460,38760,15504,4845,1140,190,20,1), 3000 inclusion-minimal forcing sets sizes (6:2040,7:180,8:780), and 830 inclusion-minimal forts sizes (7:60,8:20,9:200,10:410,11:120,12:20). Separately computed the full 120-element automorphism group and orbit partitions, matching 30 forcing-minimal and 15 fort-minimal orbits with all size/orbit multiplicities in the source certificate. The verifier paths direct.cpp, fort.cpp, verify.py, and orbit_certificate.json were materially inspected; finite exhaustive work establishes precisely this graph, not arbitrary generalized Petersen graphs.

## originality

PASS

Best-of-knowledge: known Z(GP(10,2))=6 and general zero-forcing frameworks are credited; no comparable complete 20-vertex subset/fort/orbit table was identified in exact-object searches or published-finding comparisons.

## value

PASS

GP(10,2) is the canonical highly symmetric 20-vertex cubic dodecahedron. Beyond known Z=6, exact higher coefficients, non-well-forced minimal sets of size 7 and 8, complete minimal-fort obstruction antichain and its automorphism orbits supply naturally reusable exact structural invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
