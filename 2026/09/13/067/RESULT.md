# No constant Weisfeiler–Leman dimension after wall-row individualization

## Context

The Weisfeiler–Leman (WL) hierarchy measures descriptive complexity of graphs:
k-WL corresponds to the bijective (k+1)-pebble game. Cai–Fürer–Immerman (CFI)
graphs over high-treewidth base graphs require linearly many variables.
Individualization (assigning unique colours) can lower WL-dimension, e.g. two
vertices suffice for 3-connected planar graphs. The target question asks
whether individualizing linearly many gadgets — a full row of a cubic wall —
collapses the WL-dimension of the CFI pair to an absolute constant.

## Definitions

- Brick wall W = W_{h,w}, h,w = Theta(n): vertex set [h]x[w], horizontal
  path edges in each row, vertical edges (r,c)~(r+1,c) iff r+c even.
  Maximum degree 3, planar, |V| = Theta(n^2), tw(W) = Theta(n).
- Row separator S = {(s,c)} with s = floor(h/2), |S| = w = Theta(n).
  A = {r < s} (top strip), B = {r > s} (bottom strip).
- CFI pair G_0, G_1 over W: each base vertex replaced by parity gadget,
  edge connections straight/twisted; even vs odd total twist.
- Individualized pair G^I_{n,0}, G^I_{n,1}: every gadget F(v) for v in S
  gets a unique colour per gadget vertex (rigid anchor), identical in both
  graphs; the parity difference (single twisted edge) lies deep inside A.
- k-WL distinguishes iff Spoiler wins the bijective (k+1)-pebble game.

## Result

For every fixed K and all sufficiently large n, K-WL does NOT distinguish
G^I_{n,0} from G^I_{n,1}. Duplicator wins the bijective (K+1)-pebble game.
Hence no absolute constant K works for all large n. Distinguishing the
row-individualized pair requires K = Omega(n); WL-dimension grows linearly
despite Theta(n) individualized gadgets.

## Proof / Evidence

Lemma 1 (two large sides): W-S has exactly two components A and B, each
connected (rows are paths chained by vertical rungs), each of size
Theta(n^2). The row does not cut the wall into bounded-treewidth strips.

Lemma 2 (strips keep linear treewidth): tw(A) = Theta(n), tw(B) = Theta(n).
Upper bound by column-sweep path decomposition of width O(n). Lower bound
by the standard wall-to-grid minor fact (s x w wall contains t x t grid
minor with t = Omega(min(s,w))) plus minor-monotonicity of treewidth.
Corollary: by Seymour–Thomas duality, A carries a bramble of order
r = tw(A)+1 = Omega(n).

Lemma 3 (anchored separator): unique anchor colours force Duplicator to map
each S-gadget to its counterpart; the separator is pointwise fixed.

Lemma 4a (clean ladder): if P subset A, |P| <= K and s > 2K+1, two adjacent
rows of A disjoint from P exist; their union is a connected full-width
ladder disjoint from P and S, inside one component of A-P.

Lemma 4 (twist mobility): a CFI path-automorphism shifting the odd twist
along Q avoids pebbled gadgets on stay-set and fixes S pointwise when
Q is inside A avoiding stay-pebbles and S — the classical CFI twist shift
restricted to such Q, i.e. legal robber moves in A.

Theorem: play the (K+1)-pebble game. Anchors forced. At most K stay-cops
constrain A per move (moving pebble lifted; S/B pebbles answered
identically). For large n, r > K so K cops lose the Seymour–Thomas game on
A. Duplicator plays the robber strategy, shifts the twist along Q in A,
extends by canonical local CFI isomorphism identity on S. This is the
Grohe–Marino / Dawar–Richerby CFI–cops correspondence localized to A.
Spoiler needs at least r-1 = Omega(n) cops on A.

Computation (structural certificates only): wall_separator.py builds 8x8
and 12x12 brick walls; certifies max degree <= 3, W-S has 2 components of
sizes 32/24 and 72/60, A and B connected, intact clean ladders rows [0,1]
and giant pieces 27/32 and 68/72 after demo cop sets of size 3 and 4.
No bramble-order claim is computed; Omega(n) comes from the analytic
argument.

## Limitations

Classical CFI twist-shift and CFI/cops correspondence invoked as known
facts with stay-in-A verification; grid-minor fact standard; computation
covers 8x8 and 12x12 instances while general-n claim is analytic; exact
WL-dimension constants not determined.

## Reproducibility

Run `python3 output/artifacts/wall_separator.py`; compare
output/artifacts/wall_separator_results.json. Re-ran during audit:
8x8 comps [32,24] ladder [0,1]; 12x12 comps [72,60] ladder [0,1].

## References

- Cai, Fürer, Immerman — CFI construction and twist automorphisms.
- Seymour, Thomas — treewidth–bramble duality; cops-and-robber game.
- Grohe–Marino / Dawar–Richerby — CFI–cops correspondence.
- Grohe, Lichter, Neuen, Schweitzer, Compressing CFI Graphs (FOCS 2023).
- Kiefer, Ponomarenko, Schweitzer, WL dimension of planar graphs at most 3.
