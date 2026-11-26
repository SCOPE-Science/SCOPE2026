# Independent mathematical audit

## correctness

PASS

Flattening a series–parallel tree leaves an ordered series decomposition identifiable by its incomparability components. Each nonsingleton factor is a top parallel node; additivity of width forces two nonempty chains. At prefix size p, the first point of each chain and no later factor has exactly p predecessors. At a two-chain factor with successor counts u and v at those points, the two lengths, as an unordered multiset, are n-p-1-u and n-p-1-v. Taking the full predecessor interval of width equal to the factor size consumes exactly that factor, since later factors start at the next prefix or above. Within a factor, identical pairs require identical chain positions and, for points in distinct chains, equal lengths; only then can the chain-swap automate the match. Counting vertices of each pair is expressible with two variables with counting, so the conclusion is internal to the strict-order class. The sum over unordered chain lengths is z^2/((1-z)(1-z^2)); carrying out the sequence expansion gives the listed coefficients. For the finite boundary, induct on size: a series composite introduces no cross-factor orbit collision because the predecessor ranges are disjoint; in a parallel composite work with the connected comparability components. An isolate has pair (0,0), and two size-two connected components are interchangeable chains. Through size five the only remaining possible cross-component collision is between a chain of size two and a connected size-three poset. The latter is a chain, V, or its dual. The three-chain's degree sums are 2 and cannot match the size-two chain's sums of 1, whereas V and its dual give exactly the claimed types. Independent enumeration of reduced series/parallel trees and all vertex permutations confirmed 1,2,5,15,48 types and 0,0,0,0,2 failures through order five. Width sharpness here concerns first-round orbits, not cross-structure reconstruction. The supplied scripts were inspected but not executed.

## originality

PASS

The supported distinct contribution is exact all-order reconstruction and orbit recovery on the stated series–parallel class with the sharp finite orbit boundary. The numerical sequence and rational generating function, as series, already occur in another combinatorial setting; they are not an independent novelty claim. Same-day Resultary comparisons were made on scope, without inferring priority.

## value

PASS

A weak invariant consisting of just one round of strict predecessor/successor counts recovers both an unlabeled order and its orbits on a natural hereditary class. The minimal boundary tells exactly where that orbit statistic first ceases to suffice within the series–parallel family; it is not merely a table of known counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
