# Review

## Correctness
PASS. The lower bound follows from the first nonempty forcing event. If it occurs from a black vertex in part \(V_i\), at most \(k\) white vertices can be outside \(V_i\); after that event all outside whites are black, and more than \(k\) whites left inside \(V_i\) would be permanently unforceable. Connectivity of a non-singleton initial set supplies an initially black vertex on each side of this cut, giving the additional caps \(n_i-1\) and \(N-n_i-1\). The matching construction leaves exactly the two capped quantities white and forces them in at most two nonempty rounds. The one-vertex case is separately and exhaustively characterized by universality and \(k=N-1\). A brute-force checker confirms every multipartite type through order nine for all admissible \(k\).

## Originality
PASS. The initiating 2026 paper's full accessible text defines the parameter and proves the complete-graph all-\(k\) formula and the complete-bipartite \(k=2\) formula, but contains no occurrence of “multipartite.” The 2025 connected dom-forcing paper was inspected in full text at the \(k=1\) boundary and gives the biclique value \(m+n-2\). The 2020 connected \(k\)-forcing paper was inspected in full text and gives the connected zero-forcing value for bicliques and all-\(k\) value for stars, but studies a weaker parameter without domination. None of these statements implies the arbitrary-part, arbitrary-\(k\) formula. Targeted semantic and exact-phrase searches found no covering statement. Residual risk remains that an equivalent theorem exists under terminology not found in the searches.

## Value
PASS. The result solves the newly introduced hybrid invariant on the entire classical complete-multipartite family for every admissible \(k\), with a closed formula depending only on the part profile. It unifies several separately known boundary cases and exposes the exact structural reason for the optimum: the first forcing part can hide at most \(k\) whites on each side, subject to keeping the initial set connected. This is a natural exact family theorem rather than a parameter substitution or finite-table computation.

## Closest literature and limitations
The closest same-parameter source is Susanth–Dominic–Premodkumar (2026), DOI 10.9734/jamcs/2026/v41i22096. Relevant boundary sources are DOI 10.17654/0974165825046 and DOI 10.28919/jmcs/4446. The theorem does not address propagation time, incomplete multipartite cross-edges, or enumeration of all minimizers.

Same-model review: passed. Independent audit: not yet performed.
