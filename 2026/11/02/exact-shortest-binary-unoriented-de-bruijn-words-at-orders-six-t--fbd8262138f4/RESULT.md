# Exact shortest binary unoriented de Bruijn words at orders six through nine

## Finding

Write \(w^R\) for reversal of a binary word \(w\). For every integer \(n\ge 1\), let \(U(n)\) be the minimum length of a **linear** binary word that contains at least one representative of every reversal class \(\{w,w^R\}\) of binary length-\(n\) words as a contiguous factor. Then the first four values after the orders treated by the illustrative Eulerizations of Burris--Motta--Shipman are

\[
\boxed{U(6)=48,\qquad U(7)=92,\qquad U(8)=162,\qquad U(9)=318.}
\]

The corresponding numbers of distinct reversal classes are \(36,72,136,272\), and the **unavoidable repeated class-windows** are respectively \(7,14,19,38\). Here repeated class-windows means \(U(n)-n+1-|\mathcal R_n|\), where \(\mathcal R_n\) denotes the reversal classes. This is a theorem about linear words, **not** about circular sequences or orientation-distinguishing sequences.

| Order \(n\) | Required classes \(|\mathcal R_n|\) | Extra windows | Minimum linear length \(U(n)\) |
|---:|---:|---:|---:|
| 6 | 36 | 7 | 48 |
| 7 | 72 | 14 | 92 |
| 8 | 136 | 19 | 162 |
| 9 | 272 | 38 | 318 |

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Reversal identifies a word with its reverse, without identifying its bit complement. Factors are linear contiguous length-\(n\) windows; endpoints do **not** wrap around. The word must cover every reversal class at least once, and repetitions are allowed. The four claims are exactly for \(n\in\{6,7,8,9\}\), with no extrapolation.

The number of reversal classes follows directly from Burnside's lemma:
\[
M_n=|\mathcal R_n|=\frac{2^n+2^{\lceil n/2\rceil}}{2}.
\]
For a candidate length \(L\), there are \(L-n+1\) consecutive windows. Define the excess \(r=L-n+1-M_n\); the theorem says the least possible excess is \(r=7,14,19,38\) in the four cases.

## Proof

**1. The signed unoriented overlap multigraph.** Its vertices are reversal classes \([v]=\{v,v^R\}\) of length-\(n-1\) words, and each reversal class \([w]\) of length-\(n\) words is a labeled undirected edge between \([w_1\cdots w_{n-1}]\) and \([w_2\cdots w_n]\). Edges and loops are retained with multiplicity. At a nonpalindromic vertex, an incident edge-end receives type \(0\) if the associated oriented occurrence leaves the lexicographically smaller representative, and type \(1\) if it enters that representative. Choosing \(w\) as the lexicographically smaller member of \([w]\), the prefix end has type \(0\) precisely when its actual prefix is the smaller representative; the suffix end has type \(1\) precisely when its actual suffix is the smaller representative. This convention is independent of choosing the other orientation, because reversal exchanges both end and orientation. At palindromic vertices the incidence type is flexible.

Every binary covering word projects to a walk using each such labeled edge at least once. At each nonpalindromic intermediate vertex, consecutive edge incidences must be of opposite types. The reason is explicit: once an actual length-\(n-1\) overlap has entered the vertex, the next factor must leave the same representative, not its reversed counterpart. Reversal exchanges the two directions simultaneously; hence the type-alternation rule. This is the alternating-Eulerian encoding described by Burris, Motta and Shipman (2016, Sections 2--3).

**2. Forced terminal imbalances.** Take exactly one instance of each reflection-class edge as the mandatory multigraph. Let \(d_0(v)\) and \(d_1(v)\) count the two incidence types. Directly enumerating the \(M_n\) classes (the standalone verifier constructs this list, with no prior data files) shows for each of the four orders that every nonpalindromic even-degree vertex satisfies \(d_0=d_1\), while each nonpalindromic odd-degree vertex has \(|d_0-d_1|=1\). At each latter vertex an additional path end must have the minority incidence type if the total covering walk does not terminate there. Palindromic odd-degree vertices have no required type. The odd-vertex counts for orders \(6,7,8,9\) are respectively \(8,14,16,30\).

**3. A necessary matching bound.** Remove one occurrence per reversal class from any covering walk, leaving \(r\) extra edge traversals. Pair excess incidences of opposite types at each nonpalindromic vertex, and pair excess incidences arbitrarily at a palindromic vertex. The unpaired ends decompose the extras into alternating paths (and possibly closed walks). Each odd vertex of the mandatory graph contributes an appropriate endpoint demand, except that the two endpoints of the original covering word can absorb or create up to two free endpoint demands. Represent those two free choices by auxiliary terminals \(\star_1,\star_2\); a path ending at one of them is charged only the nonnegative cost zero. If an endpoint reverses the majority type, its surplus two minority-type incidences are represented by one ordinary demand and one free terminal. Thus the extra-edge multiset yields, after discarding nonnegative paths and cycles if necessary, a perfect pairing of the odd-vertex demands and two free terminals whose total charged path length is no greater than \(r\).

For odd vertices \(u,v\), let \(D(u,v)\) be the shortest **alternating** path length that starts with the demanded type at \(u\) and ends with the demanded type at \(v\), with no type constraint at a palindromic endpoint. The length is computed by ordinary breadth-first search over states \((v,t)\), where \(t\in\{0,1\}\) is the required next end-type. Crossing an edge with type \(s\) at the next vertex sets the next requirement to \(1-s\). Take the smaller of the two direction orders if needed. Add two auxiliary terminals with cost zero to every original odd vertex and cost zero between themselves. Consequently, every covering word obeys
\[
r\ge \min\{\text{weight of a perfect matching on the original odd vertices and two auxiliaries}\}.
\]
This lower bound uses only a **necessary** condition on a covering walk; it does not assume that an arbitrary matching can be realized by a single word.

**4. Exact dual lower certificates.** The supplied `certificates.json` contains, in fixed lexicographic odd-vertex order followed by two auxiliaries, twice an exact rational potential \(z_i=2y_i\) for each order. The standalone `verify.py` checks every inequality
\[
z_i+z_j\le 2D(i,j),\qquad z_i+z_{\star_a}\le0,\qquad z_{\star_1}+z_{\star_2}\le0.
\]
It also checks \(\sum_i z_i=2r\), with \(r=7,14,19,38\), respectively. Multiplying each edge's dual inequality by the nonnegative weight of a perfect-matching incidence, summing, and using that every vertex occurs once proves that every matching has cost at least \(\tfrac12\sum_i z_i=r\). This is a finite exact-integer certificate, **not** a numerical optimizer log. The BFS enumerates the complete finite signed state graph, so the distances are exhaustive rather than sampled.

**5. Matching upper witnesses.** For each order, `certificates.json` contains a fully explicit binary word of the claimed length. The same standalone verifier scans every one of its length-\(n\) windows, maps the window to the lexicographically smaller of it and its reversal, and checks equality with the entire set of \(M_n\) reversal classes. Hence \(U(n)\le M_n+n-1+r\), matching the lower bound for each of the four orders and completing the proof.

## Verification

Extract `verify.py` and `certificates.json` into one directory and run:

```text
python3 verify.py certificates.json
```

Only the Python standard library is required. The checker reconstructs the graphs and signed shortest paths; it does not load computed graph tables. It verifies the four exact dual certificates and four explicit covering words and prints `VERIFY_OK` only if all checks pass. The four verified records are \((n,M_n,r,U(n))=(6,36,7,48),(7,72,14,92),(8,136,19,162),(9,272,38,318)\).

## Relationship to prior work

Burris, Motta and Shipman, *An Unoriented Variation on de Bruijn Sequences* (first publicly available August 30, 2016), introduce reversal-class covering words and alternating Eulerizations, characterize exactly when no repetition is needed, and give examples at binary orders four and five plus general upper bounds. Their Sections 4--5 do not determine these four later exact shortest lengths or give their signed-distance matching duals. The present result supplies sharp values and explicit certificates for the next four binary orders; it does not claim the graph construction or general Eulerization method as new.

Mitchell and Wild, *New orientable sequences* (2026), study **maximum** cyclic periods with no repetition up to reversal, not the shortest **linear** covering words that permit repeated windows. Its period bounds therefore do not imply the stated covering minima. Indexed searches for “unoriented de Bruijn”, “reversal-class shortest superstring”, and the precise parameter/value combinations found no directly equivalent finite table; lack of an indexed hit is not a proof of historical priority.

## Limitations

Only the four exact finite orders are established. No general formula, optimality claim for order ten, enumeration of all minimizers, or result for larger alphabets follows. The mathematical certificate guarantees the stated extrema subject to the elementary signed-incidence/matching argument; independent scientific review and complete historical-priority verification are not performed. Some unindexed literature could contain equivalent earlier values.

## References

1. Christie S. Burris, Francis C. Motta and Patrick D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480v1 (August 30, 2016), https://arxiv.org/abs/1608.08480 . Sections 2--5 (full open preprint).
2. Chris J. Mitchell and Peter R. Wild, *New orientable sequences*, *Acta Informatica* 63, article 14 (March 18, 2026), https://doi.org/10.1007/s00236-026-00528-z . Introduction and sequence definitions; a related but distinct extremal problem.
