# Scientific review

## Correctness — PASS
The normal form for all wheel-geodesically convex sets follows from the two length-two geodesics between rim vertices separated by one vertex. The proof of the rim-only characterization constructs a convex trace witness for every subset and the hub classification eliminates every excluded trace. The coefficient formula follows by marking zeros in circular binary words; the degree bound, constructions, and exact maximum counts use exact finite algebra valid for every integer rim size at least five. A separate standard-library program enumerates shortest-path geometry, convex sets and shattered supports directly for all smaller cases and checks larger coefficients. There are no extrapolations from finite tests to infinite conclusions.

## Originality — PASS under the inspected sources
The relevant accessible primary literature sets up the graph-convexity learning problem and general VC/mistake bounds without the claimed wheel-support structure. The dissociation polynomial is an established invariant; the identifying equivalence from wheel shattering to cycle dissociation is the central added step. Published cover-free-wheel results do not imply VC shattering. Semantic research-record searches for wheel convexity, shattering, `111` avoidance and dissociation equivalences did not locate an equivalent or dominating indexed claim. The absence of a retrieved result is not itself a proof of global novelty, and differently termed graph-convexity literature is a remaining historical-priority risk.

## Value — PASS
The complete shattering complex and face enumerator determine every finite support trace, rather than merely giving a VC bound. The structural link with a classical graph polynomial explains a linear VC dimension in a natural graph family formed by adding one universal vertex to a cycle, and gives an exact maximum-support census with a genuine three-residue-class distinction and one small exception.

## Closest literature and limitations
Thiessen–Gärtner (2022), *Online Learning of Convex Sets on Graphs*, Section 4, gives general graph-convexity learning bounds but not the wheel enumeration. Tu–Xiao–Lang (2023), *Counting the number of dissociation sets in cubic graphs*, supplies background on the known dissociation polynomial rather than this specific wheel shattering equivalence. There is no Littlestone result here, no assertion about wheels on fewer than six vertices, and no claim of priority over unexamined terminology.

Self-review: passed. Independent audit: not yet performed.
