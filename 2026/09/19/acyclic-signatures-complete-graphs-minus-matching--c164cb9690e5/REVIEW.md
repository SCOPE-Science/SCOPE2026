# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at four separate points: the signed topological-order
encoding, the sink-layer cancellation giving the inverse series, the
hyperbolic even/odd simplification, and the final coefficient extraction.

For a complete multipartite graph, any two topological orders of the same
acyclic orientation differ by adjacent swaps of incomparable vertices, which
must lie in one part.  Hence the signed monomial attached to an orientation is
well defined.  Cross-part anticommutation records exactly the parity of edges
reversed from the part-ordered reference orientation.

The identity \(\mathcal F\mathcal C=1\) was rechecked coefficientwise: for a
nonempty orientation \(H\), possible final independent layers are precisely
subsets of its nonempty sink set, and their alternating sum is zero.  The
algebraic reduction
\[
\mathcal F=
\frac{1+\sum u_i+\sum w_i}
     {1+2\sum_{i<j}u_i u_j}
\]
follows from cross-part anticommutation and
\(\sinh^2 z_i=(1+u_i)^2-1\).

For a two-vertex part, \(u_i=a_ib_i\); for a singleton, \(u_i=0\).  The full
coefficient therefore reduces to perfect-matchings among the doubleton-part
indices.  The coefficient of \(Q^k\) on \(2k\) specified indices is
\((2k)!/2^k\), so the factor \((-2)^k\) gives \((-1)^k(2k)!\).  The even,
odd, and singleton cases then give exactly the stated factorial formula.

A standalone brute-force verifier checks all 28 parameter pairs
\(2\le n\le9\), deduplicating acyclic orientations induced by all vertex
orders and comparing their signed parity sums with the formula.  Every check
passes.  The computation is supporting evidence and is not required by the
proof.

## Originality

Originality is assessed **to the best of our knowledge**.

The directly relevant new source is Mühlherr--Poullot,
arXiv:2609.02249v2.  Its accessible abstract defines the new acyclic-polynomial
framework and states the nonzero-signature obstruction to Hamiltonicity.  The
full current v2 text was not completely inspected, so a specialized
example in the uninspected portion remains a concrete residual risk.  Indexed and
exact-phrase searches for matching complements, cocktail-party graphs,
complete multipartite graphs, and equivalent signed-enumerator terminology
did not reveal such coverage.

The accessible full HTML of Carballosa--Khera--Reyes was inspected.  It gives
a source/sink encoding of complete multipartite acyclic orientations and a
closed formula for the total labelled count (Theorem 3.4), but no signed
edge-disagreement enumerator or evaluation at \(-1\) was found.

The accessible Savage--Squire--West PDF was also checked.  It establishes the
even/odd bipartition of the acyclic-orientation graph and studies several
families, including complete graphs and some complete bipartite graphs.
Searches within the paper found no occurrence of “multipartite” or “cocktail”
and no treatment of complete graphs with a matching deleted.

Broader searches used exact and synonymous formulations involving acyclic
signature, acyclic polynomial at \(-1\), parity imbalance, rank/distance
enumerators, complete graph minus a matching, cocktail-party graph, complete
multipartite graphs, Gray codes, and Hamiltonicity.  No equivalent or stronger
formula was found.

The main residual risks are the uninspected portions of the very recent
arXiv:2609.02249v2, older hyperplane-arrangement or trace-monoid literature
using a different statistic name, and very recent parallel work.

## Value

The result gives an exact factorial bipartition imbalance for an infinite
dense family: every cocktail-party graph \(K_{2r}-M_r\) has
\(|\sigma|=r!\).  It therefore supplies a simple infinite family of explicit
non-Hamiltonicity certificates for acyclic-orientation graphs, together with a
sharp contrast for near-perfect matchings where the obstruction alternates
with the parity of \(r\).

The proof also isolates a reusable signed cancellation identity for complete
multipartite orientations.  It converts the edge-disagreement parity sum into
a coefficient problem whose denominator is controlled by pairings of even
part-contributions.

## Limitations

The full polynomial \(\Psi(D;t)\) is not determined.  Zero signature does not
imply Hamiltonicity.  The current v2 source paper was not completely inspected
in full text, so originality remains to the best of our knowledge with that
explicit residual risk.  Computational checks are finite supporting evidence,
and independent audit has not been performed.
