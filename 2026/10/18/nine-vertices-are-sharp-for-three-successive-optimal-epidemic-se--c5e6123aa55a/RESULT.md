# Eight-vertex trees admit at most two distinct unique decay-centrality maximizers

## Finding

Let \(T\) be a finite tree with \(2\le n\le8\). For \(0<p<1\) define \(C_v(p)=\sum_{u\ne v}p^{d_T(u,v)}\). At most two distinct vertices of \(T\) are ever strict maximizers of this score, even if each vertex is tested at a different value of \(p\). Together with the three-winner nine-vertex broom \(B_{2,6}\), this gives nine as the sharp minimum **over all trees**, not just over brooms.

Under independent edge opening with common probability \(p\), this is also a single-sentinel theorem: a uniformly selected seed (including the sentinel itself) is connected to \(v\) with probability \((1+C_v(p))/n\), by uniqueness of paths. The sentinel detects eventual reachability perfectly; speed or timing of detection, correlated transmission, and nonuniform seeds are outside scope. Vertices tied at a maximum do not count as strict winners.

## Proof of the all-tree obstruction

Let \(A_j(v)=\#\{u:1\le d_T(u,v)\le j\}\). Then telescoping the distance-layer counts gives
\[
C_u(p)-C_v(p)=(1-p)\sum_{j=1}^{n-2}(A_j(u)-A_j(v))p^j,
\]
since both final cumulative counts equal \(n-1\). A componentwise dominated cumulative profile with at least one strict inequality never wins. If two vertices share a profile, neither can be the unique winner. Consequently the number of distinct nondominated profiles is an upper bound.

Enumerate all unlabeled trees through order eight by adjoining a leaf to each possible vertex of every smaller tree; deleting a leaf proves coverage by induction. Deduplicate by a canonical rooted encoding at the center or centers: write each vertex as a matched pair of parentheses containing its rooted child encodings in sorted order and take the least of the central encodings. The breadth-first distance counts give the following exhaustive table.

| Order | Trees | Largest number of distinct nondominated profiles |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 1 | 1 |
| 4 | 2 | 1 |
| 5 | 3 | 1 |
| 6 | 6 | 2 |
| 7 | 11 | 2 |
| 8 | 23 | 3 |

The only tree with three profiles consists of a five-edge path with two additional leaves at one endpoint. Order the first three path vertices starting at that branching endpoint. Their scores are respectively \(3p+p^2+p^3+p^4+p^5\), \(2p+3p^2+p^3+p^4\), and \(2p+2p^2+3p^3\). These are precisely the three profiles on the cumulative frontier. The second minus the third is \(p^2(1-p)^2>0\), so only the first two can produce strict maximizers. In particular, no parameter grid is needed to exclude a third winning interval.

## Attainment and relation to other results

The nine-vertex broom \(B_{2,6}\) can be labeled by the edges \(01,12,05,23,34,56,67,68\). Its three possible winners are \(6,5,0\); all other cumulative profiles are strictly dominated. The adjacent score differences are
\[
C_6-C_5=p(1-p)(1-p-p^2-p^3-p^4),\qquad
C_5-C_0=p^2(1-p)(1-p-p^2).
\]
The parenthesized expressions decrease strictly from positive to negative. The first is already negative at \(s=(\sqrt{5}-1)/2\), the root of the second. Thus the roots satisfy \(r<s\); the winners are \(6,5,0\) on the successive open intervals, with exactly the adjacent ties at \(r,s\). This attainment is also covered by *Exact multi-stage epidemic source migration on broom contact trees* (Resultary `5d05a9b4e6b1`, Finding and Proof). Its expected outbreak size from a selected source is \(1+C_v(p)\), giving identical optimization. The broom construction and the phase boundaries are therefore not claimed as distinct contributions. The all-tree exclusion below nine is not implied by that broom-family result.

Coroničová Hurajová, Gago and Madaras, *On Decay Centrality in Graphs*, DOI `10.7146/math.scand.a-106210`, Proposition 2.2, provide the cumulative-distance comparison. Their Table 1 counts stability of whole rankings, which does not determine how many different vertices can strictly maximize the score. Tsakas, *On Decay Centrality*, arXiv:1604.05582, gives endpoint comparisons with degree and closeness, not the all-tree obstruction to an intermediate third winner. No historical priority claim is made.

## Verification

The unchanged standard-library certificate `verify_three_sentinel_winners.py` reproduces the tree and frontier counts, an exact coefficient comparison for the exceptional eight-vertex tree, and the witness score factorizations and dominance checks. Root decimals, if displayed, are not used for the sign proof.
