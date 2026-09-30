# Review

## Correctness assessment
PASS. The proof derives an exact feasibility criterion: if \(s\) and \(t\) selected vertices lie in the two parts, the omitted counts must satisfy \(a-s\le\binom{t}{2}\) and \(b-t\le\binom{s}{2}\), because each omitted vertex can be the internal vertex of exactly one selected same-part geodesic slot. The criterion is also sufficient by assigning distinct slots. Upward closure reduces minimality to one-vertex deletions. The star, \(K_2\), lower-bound construction, and upper-bound deletion argument cover all parameter ranges. The maximum-set classification is obtained by substituting \(|S|=b+1\) and exhausting the possible omitted count \(q=b-t\); each exceptional balanced case is checked explicitly. An independent-from-the-formula finite verifier tests all vertex subsets of 35 labeled complete bipartite types through \(a\le7\), \(b\le8\), reproducing every value, pattern, and count.

## Originality assessment
PASS, best-of-knowledge. The defining 2021 strong-upper paper was checked in full text: it introduces \(\operatorname{sg}^{+}\), proves general complexity results, and treats several named families, but no complete-bipartite exact formula or maximum-set classification was located. Exact-phrase and notation-variant searches for strong upper geodetic number on complete bipartite graphs returned that defining paper and later distinct vertex-strong variants, not an equivalent theorem. The 2017–2018 complete-bipartite literature concerns the ordinary minimum strong geodetic number \(\operatorname{sg}\), not \(\operatorname{sg}^{+}\). Repeated semantic searches in the indexed finding repository returned no equivalent or stronger result; the nearest hits concern unrelated parameters despite similar wording.

## Value assessment
PASS. The general strong-upper problem is NP-complete, while this theorem gives a closed form on a canonical graph family already central to the ordinary strong-geodetic literature. It goes beyond the parameter value by classifying every maximum-cardinality minimal strong geodetic set and giving exact enumeration formulas. The capacity criterion isolates the structural reason the upper parameter is simple on complete bipartite graphs and can support related extremal questions.

## Closest literature
The primary source is *Strong Upper Geodetic Number of Graphs* (`doi:10.26713/cma.v12i3.1597`), which defines the parameter and establishes general results. The closest family-specific literature is V. Iršič, *Strong Geodetic Number of Complete Bipartite Graphs and of Graphs with Specified Diameter* (`arXiv:1708.02416`, `doi:10.1007/s00373-018-1885-9`), and V. Gledel–V. Iršič, *Strong geodetic number of complete bipartite graphs, crown graphs and hypercubes* (`arXiv:1810.04004`); both study the minimum strong geodetic number rather than the maximum size of a minimal strong geodetic set. The closest indexed semantic hits located were on Sylvester–Gallai dimension of \(K_{2,n}\) and on geodesic-subpath extremality at diameter two, neither of which is equivalent to strong upper geodetic number.

## Scientific limitations
Originality remains best-of-knowledge and may miss inaccessible or unusually phrased work. The theorem is confined to complete bipartite graphs. The exhaustive verifier covers finite parameter ranges only; it is a corroborative check, while the infinite statement rests on the written proof. No independent audit, Lean verification, or expert attestation has been performed.

Same-model review: passed. Independent audit: not yet performed.
