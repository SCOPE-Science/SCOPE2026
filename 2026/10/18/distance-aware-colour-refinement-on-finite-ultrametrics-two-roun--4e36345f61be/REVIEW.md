# Independent mathematical audit

## correctness

PASS

The strong triangle inequality makes each radius-δ_j relation an equivalence relation. Inductively c_r(x) determines the isometry type of the radius-δ_r equivalence class of x: accumulate old colours within its E_r ball, decode smaller E_{r-1} blocks, divide each point-multiplicity by block size, and join all blocks at distance δ_r. At r=h-1 the global histogram gives the multiset of top proper balls; join them at δ_h. For h=1 n is encoded by c_0 multiplicity. The one-round signature at h=3 recovers (p,q,n); a unique collision before n=8 is impossible because there cannot be two δ2 balls of size at least 4. At n=8 two size-four partitions have sole nontrivial aggregate ambiguity 2×(2,1,1)↔(2,2)+(1,1,1,1). Separate independent partition-census with raw comparable signatures recovered 1,3,6,14,27,58,111,223 types for n=1..8 and exactly that single pair; this corroborates but does not prove the all-size theorem.

## originality

PASS

Ambient relational colour refinement and hierarchical ultrametrics were previously studied, but general logic/algorithmic characterizations do not imply the exact within-ultrametric h-1 round bound or the unique first eight-point collision. The claim is explicitly relative to finite ultrametrics using the same labeled distance alphabet.

## value

PASS

The exact sharp first obstruction and hierarchy-depth reconstruction give a natural complexity boundary for a canonical algorithm on structured metric spaces, and the first-collision classification is a precise reusable instance for testing expressivity. Both are structurally motivated rather than arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
