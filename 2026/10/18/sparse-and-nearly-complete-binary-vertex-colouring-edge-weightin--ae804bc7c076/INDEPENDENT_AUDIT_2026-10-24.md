# Independent mathematical audit

## correctness

PASS

The literal condition is disjointness of all row and column sums in the selected-edge matrix, including zeros on original edges. Below m selected edges each bipartition has a zero, which is forbidden. At m<n, an isolated right vertex forces every left selected degree to be exactly one, and each occupied right fibre to have size at least two; the exponential generating-function and inclusion-exclusion formulas count these maps, and fibre partitions give all orbits and labelled multiplicities. For balanced q, any minimum q-edge support with a zero on either side is one of two disjoint star orientations; if neither side has zero, the support is a perfect matching and fails. Complementation subtracts degrees from q on both sides, giving reciprocity. For m,n=m+1, the zero-edge graph condition x_u-y_v≠1 proves no deletion of one or two edges, and precisely the left-centred 3-stars as first allowable deletion; n≥m+2 admits all mn single deletions. The m=1 boundaries are verified separately. The all-size proof is not inferred from enumeration.

## originality

PASS

The two-weight vertex-sum criterion, existence for many bipartite graphs and some scalar endpoints are established prior art. The claim being assessed is instead the complete extremal support classification, fibre-partition orbit multiplicities, balanced support reciprocity, and sharp first near-full gap for K_{m,m+1}. Aute–Panolan–Philip concerns complexity and partially specified weighting; Lu concerns existence; Bensmail et al. treat edge deletion local irregularity checked only on retained edges, a genuinely weaker original-edge condition. The inspected primary statements and proofs do not supply the joint enumeration or gap. This is best of knowledge, subject to unknown specialized weighted degree-matrix enumerations.

## value

PASS

Classifying all cheapest 0/1 vertex-sum weightings on a ubiquitous biclique is a natural extremal optimization problem; the integer-partition fibre types and exact labelled multiplicities capture all optimizers, not merely an attainable endpoint. The symmetric reciprocity for square bicliques is an exact full-support constraint, while the sharp 3-deletion plateau at consecutive part sizes isolates a meaningful qualitative transition from the unbalanced n≥m+2 case. These facts have structural content independent of code reproducibility and are not textbook restatements of the known scalar endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
