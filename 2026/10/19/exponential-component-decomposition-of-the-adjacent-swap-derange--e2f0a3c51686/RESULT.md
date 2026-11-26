# The first geodesic detour in the adjacent-swap derangement graph

## Finding

Let \(\mathcal D_n\) be the graph on the derangements of \([n]\) with edges for swaps of adjacent positions. For \(2\le n\le5\), every component of \(\mathcal D_n\) is isometric in the full adjacent-transposition graph on \(S_n\). For **every \(n\ge6\)** there are two derangements in the same component whose distance in \(\mathcal D_n\) is \(7\), while their unrestricted adjacent-swap (Kendall) distance is \(5\). Thus six is the first order at which preserving the derangement condition can force a detour even for reachable endpoints.

## Assumptions and scope

A permutation is a word whose entries are the distinct values in \([n]\), with positions numbered from one. A derangement has no entry equal to its position. Only consecutive positions in the linear word can be swapped; there is no wraparound move. All intermediate words on a restricted path must be derangements. Isometry is a statement about pairs within an individual connected component, not about distances between components.

## Proof

### The finite boundary

For each \(n=2,3,4,5\), the supplied `verify.py` lists all \(n!\) permutations and keeps just the derangements. It generates an edge for each neighboring-position swap whose endpoint is in that list. Breadth-first search from each derangement visits precisely those words reachable by a legal path and returns their exact path distances. For each reachable unordered pair \((a,b)\), it independently counts the unordered pairs of labels in opposite relative orders in \(a\) and \(b\). This count is the unrestricted distance: each adjacent swap changes one label-pair order, and ordinary bubble sort to the order of \(b\) can correct one disagreement per swap until none remain. The exhaustive comparison is:

| \(n\) | Derangements | Reachable distinct unordered pairs | Pairs with a detour |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 2 | 0 | 0 |
| 4 | 9 | 11 | 0 |
| 5 | 44 | 188 | 0 |

### A persistent exact detour

For \(n\ge6\), append the common tail \(T_n=(7,8,\ldots,n,4)\) to the five-entry prefixes \((3,1,2,5,6)\) and \((3,6,2,5,1)\) to obtain \(a_n\) and \(b_n\). Here \(T_6=(4)\). The labels are exactly \([n]\), and the tail entry at position \(j<n\) is \(j+1\) for \(6\le j<n\), while the last entry is \(4\). The following path of prefixes, with the tail kept fixed, consists of derangements and swaps one adjacent pair at each step:
\[
31256\ \longrightarrow\ 31526\ \longrightarrow\ 35126\ \longrightarrow\ 35216\ \longrightarrow\ 35261\ \longrightarrow\ 35621\ \longrightarrow\ 36521\ \longrightarrow\ 36251.
\]
The Kendall distance is five: restricted to the first five places, label \(1\) changes its order with \(2,5,6\), and label \(6\) additionally changes its order with \(2,5\). No pair involving the common tail changes order. A path of length five must decrease the number of disagreements with \(b_n\) at every step. In \(a_n\) the only adjacent pairs in the opposite order in \(b_n\) are \((1,2)\) and \((5,6)\), both in the prefix. Swapping the former fixes position two, and swapping the latter fixes position five. Thus no legal path of length five exists. Every path has length congruent to five modulo two because each swap changes the number of disagreements by one. The displayed legal path of length seven is therefore shortest, including if a path is allowed to move tail entries.

## Relationship to related results

The component classification and diameter bound are available for general forbidden position sets in [Component signatures for permutations avoiding selected fixed points](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-component-signatures-for-permutations-avoiding-selected-fixed-po--79c08e75f702/RESULT.md) and are not claimed here. Connectivity within a signature fiber does not give isometry. The [derangement detour for inverse triangle products](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-an-exact-linear-derangement-swap-detour-between-inverse-triangle--a01ace1f3db3/RESULT.md) allows arbitrary-position switches and compares with unrestricted transposition distance, rather than Kendall distance. A [first-detour result for prefix-normal word-chain generators](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-sharp-first-geodesic-detour-in-prefix-normal-word-chain-gene--26333db55de7/RESULT.md) concerns a different permutation class.

## Limitations

The small-order part is an exhaustive finite computation. The fixed-tail proof applies to every \(n\ge6\), but gives neither the maximum detour nor the full distance distribution at those orders.
