# Review

## Correctness
PASS. The claim is finite and fully quantified for the binary exact \((3,1)\)-burst channel at \(3\le n\le8\). The channel implementation was reconstructed directly from the published definition. Two independent ball generators agree on every source word, every computed ball has the source-predicted size \(n-1\), each lower-bound code is checked directly, and the upper bounds come from exhaustive maximum-clique search with a sound proper-coloring bound. The standalone replay terminates with the claimed profile.

## Originality
PASS within the inspected literature and database scope. The closest primary paper defines the same channel, proves constant ball size and a sphere-packing bound, and gives an asymptotically near-optimal \((3,1)\) construction, but the inspected text does not give this finite profile. The later broader paper gives \(\log n+O(1)\) redundancy for fixed parameters, which does not imply the exact finite values. Searches covered aliases, the disjoint-ball formulation, exact values, the length-\(8\) endpoint, finite tables, and stronger asymptotic coverage. Residual risk remains for unindexed or unpublished finite computations.

## Value
PASS. Maximum correcting-code cardinality is the central finite invariant of this channel. The profile resolves all blocklengths through \(8\) and identifies the first failure, within this range, of the natural constant-ball sphere-packing bound at length \(6\). Because the foundational paper specifically singles out \((3,1)\) as a nontrivial construction problem, this short-block exact boundary is mathematically motivated rather than an arbitrary parameter slice.

## Closest literature and limitations
The main comparison is Lu--Zhang, arXiv:2201.10259v1, together with Sun--Lu--Zhang--Ge, arXiv:2403.11750v1. The result is finite and computationally exhaustive only through length \(8\); no asymptotic or longer-length claim is made, and the literature search does not prove historical uniqueness.

Same-model review: passed. Independent audit: not yet performed.
