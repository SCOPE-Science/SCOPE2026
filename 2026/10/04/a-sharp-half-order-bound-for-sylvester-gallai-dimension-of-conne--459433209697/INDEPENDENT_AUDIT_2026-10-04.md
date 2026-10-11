# Independent mathematical audit

## correctness

PASS

Deduplicate the special lines arising from edges. Graph connectedness makes their line-intersection incidence graph connected, so they can be ordered with each new line meeting the previous union at a configuration point. The first special line consumes at least three vertices and contributes affine dimension one. Any later line that increases affine dimension by one has exactly one previously used configuration point and therefore contributes at least two new vertices; a line with two old points lies in the old affine span. Hence \(n\ge3+2(d-1)\), giving \(d\le\lfloor(n-1)/2\rfloor\). For every tree, the diameter-end reduction removes two vertices while preserving a tree, either as a pendant two-edge path or as two sibling leaves; restoring them on a fresh line through the surviving anchor adds exactly one affine dimension and preserves all special-edge conditions. Induction from orders three and four attains the upper bound. The bundled finite tree enumeration checks the reduction logic only; it is not used as the infinite proof.

## originality

PASS

Dvir’s 2026 paper introduces the graph parameter and the accessible primary abstract states lower bounds for sparse/bounded-degree/minor-free graphs and a random-graph upper bound. A detailed secondary synopsis of the paper likewise lists those results and no deterministic sharp half-order upper bound for every connected graph or exact classification of every tree. The published SCOPE \(K_{2,n}\) formula is a separate family result and does not imply the universal connected bound or all-tree equality. The primary PDF itself was not retrievable through the available lawful route in this run, so possible unindexed text beyond the abstract remains a stated residual risk rather than being treated as absent.

## value

PASS

A sharp extremal bound for every connected graph and a complete exact value for the entire natural class of trees are central structural facts for a newly introduced graph invariant. The proof identifies the precise two-new-vertices-per-dimension mechanism and is not an arbitrary finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
