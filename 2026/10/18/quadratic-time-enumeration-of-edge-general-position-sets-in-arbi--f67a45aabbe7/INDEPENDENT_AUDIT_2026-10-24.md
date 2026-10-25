# Independent mathematical audit

## correctness

PASS

Indicator weights 0/1 on tree edges yield selected-weight diameter ≤2 exactly when no simple path has 3 selected edges. For each rooted subtree F_v^(a), a=max marked weight from root and a∈{0,1,2}. Adding child edge b lifts child branch height to a+b; merging distinct child branches has maximum connecting path weight exactly their root-height sum, so retaining pairs a+h≤2 and state max(a,h) proves the polynomial convolution recurrence without double counting. Pairwise edge charging bounds arithmetic operations O(n²), not bit time. Independently compared implemented three-state DP with unique-graph-path brute enumeration for all 1442 labeled trees through 6 vertices and 43615 masks, plus manuscript star/path/double-star closed forms. Proof by induction handles any finite tree.

## originality

PASS

The previously known edge-general-position maximum for trees and a full polynomial only for spiders are strictly weaker than an O(n²) coefficient enumerator for every tree. Best-of-knowledge; checked source and access limitations recorded in residual_risks.

## value

PASS

The edge-general-position polynomial enumerates all sizes of a recognized graph invariant, beyond its known leaf maximum. Counting by three heights yields a uniform quadratic-arithmetic algorithm on every tree shape, including unbounded branching where the prior spider closed form does not suffice. An arbitrary-tree polynomial is independently useful even absent a general-graph theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
