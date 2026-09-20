# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof of the universal inequality was checked by following the
witness assignment from a maximum open packing to a minimum maximal open
packing. For each vertex outside the latter packing, maximality supplies a
common-neighbor witness. Open-packing disjointness gives the two required
injectivity facts: witnesses for a fixed target are distinct, and witnesses
outside both packings cannot be reused by two targets. The resulting count is
\(|P\setminus Q|\le2|Q\setminus P|+|V\setminus(P\cup Q)|\), which is
algebraically equivalent to \(2\rho^o\le n+\rho_L^o\).

The \(\rho_L^o=1\) case was reviewed separately because the general inequality
alone would be one vertex too weak for odd order. A singleton maximal open
packing forces every vertex of a maximum open packing to share a neighbor with
the singleton; distinctness of these witnesses gives \(2\rho^o\le n\).
The connected sharpness constructions were checked directly through their
open-neighborhood graphs. Exact finite enumeration agrees with all formulas.

## Originality

**PASS, to the best of our knowledge.** The closest prior result is Henning and
Slater's 1999 Theorem 6, which already proves
\(\rho^o(T)-\rho_L^o(T)\le(n-2)/2\) for trees and supplies a sharp family of
orders \(4k+2\). That tree upper bound is therefore not a new claim here.
Sahul Hamid and Saravanakumar (2015) show that the gap can be arbitrarily large
and realize arbitrary prescribed pairs of lower and upper open-packing values;
their displayed clique-with-pendants family already realizes the odd-order
sharpness construction used here. Hartnell and Rall (2020) study graphs for
which all maximal open packings have one size and explicitly identify maximal
open packings with maximal independent sets of the open-neighborhood graph.
The 2026 spectral work of Abiad, Yang, and Zhou concerns the upper open-packing
number rather than the lower-versus-upper spread.

Exact and synonymous searches did not locate the graph-wide inequality
\(2\rho^o\le n+\rho_L^o\), its singleton sharpening, the exact fixed-order
connected maximum, or the all-order tree sharpness statement. Residual risk
remains from older or poorly indexed work, especially a result that could be
phrased entirely as a relation between independence and independent domination
on open-neighborhood graphs.

## Value

**PASS.** The result converts the previously qualitative fact that lower and
upper open-packing numbers can be arbitrarily far apart into an exact
order-sensitive extremal law. The parameter inequality is stronger than the
fixed-order corollary and applies to disconnected as well as connected graphs.
It also gives a short graph-wide mechanism that recovers the established tree
upper bound, while explicit constructions settle every order rather than only
an infinite sharpness subsequence.

## Evidence and limitations

The proof is elementary and general; exhaustive computation is used only as a
sanity check. The public verification script checks all Graph Atlas graphs of
order at least two and all nonisomorphic trees through order twelve.
Originality remains qualified as “to the best of our knowledge.” The 1999 tree
bound and the 2015 arbitrary-gap construction are prior art and are explicitly
separated from the new contribution. No classification of all equality graphs
is claimed.
