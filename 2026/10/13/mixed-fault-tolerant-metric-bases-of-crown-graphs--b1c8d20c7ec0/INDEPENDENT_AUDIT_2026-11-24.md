# Independent mathematical audit

## correctness

PASS

For degenerate matched pairs only in the sense of deleted edges, the distinguisher set for same-side a_i,a_j is precisely P_i union P_j, so multiplicities must satisfy x_i+x_j>=2. If one index is omitted, every other index is doubled and the size is at least 2n−2>n; otherwise size n requires a full transversal. To check deletion, on a one-hole transversal all vertex pairs are separated using one of their own indices or a represented third index. The coordinates of an edge different from 1 identify its represented endpoint indices, and at each such index the 0/2 value and landmark orientation recover the endpoint side; a missing index is known. A nonincident vertex with a represented pair is separated there by distance 0 or 3. For an omitted vertex a_h and a nonincident edge a_i b_j, i is represented, and at a_i the distances are 2/0 while at b_i they are 1/2. The symmetric case is identical with sides exchanged. For the actual incidence a_i vs a_i b_j the complete distinguisher set is {b_i,b_j} union {a_s:s is outside {i,j}}, so a one-hole collision exists exactly when there are one or two A landmarks, and symmetrically for B. Hence deletion of any landmark works precisely for a pure transversal or if both orientations initially occur at least four times. The pure sets establish attainment and the binomial sum counts all valid orientations, first mixed at n=8. Fresh direct distance-vector examples give minimal distinguisher number 1 for (n,p)=(4,1),(7,3) and 2 for (4,0),(8,4),(9,4).

## originality

PASS

The closest exact catalogue result already gives the vertex-only two-distinguisher lower bound, scalar n and the full transversal candidate family. The edge-only catalogue classification already gives the one-hole edge-resolving family. The distinct result is the incidence-aware condition for all bases of the simultaneous vertex-and-edge problem with deletion tolerance: the allowed mixed orientations have counts at least four on both sides. That restriction and enumeration do not follow from counting together the known vertex-only and edge-only systems.

## value

PASS

The crown's canonical matched pairs provide a natural test of robustness under simultaneous vertex and edge identification. The exact result isolates an incident mixed collision invisible to separate vertex and edge bases, and identifies the first size at which a minimum fault-tolerant basis can place landmarks on both sides. The count describes every design of minimum size rather than a redundant scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
