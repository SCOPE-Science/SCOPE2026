# Parity-dependent rank-three theories of all Boolean hypercube powers

## Finding
For integers \(r,d\ge 1\), let \(G_{d,r}\) be the simple undirected graph on binary words \(\{0,1\}^d\), with distinct words adjacent exactly when their Hamming distance is at most \(r\). Equivalently, \(G_{d,r}\) is the \(r\)-th graph power of the \(d\)-cube. In the first-order language containing only adjacency and equality, fix any radius \(r\) and compare dimensions by equivalence \(\equiv_3\), meaning agreement on all sentences of quantifier rank at most three.

The complete classification is as follows. Every row below is one equivalence class, and different rows (within the appropriate case) are inequivalent.

| Radius | Dimension ranges, each a separate class | Number of classes |
| --- | --- | ---: |
| \(r=1\) | \(d=1\); \(d=2\); \(d=3\); \(d\ge4\) | 4 |
| \(r=2\) | \(d=1\); \(d=2\); \(d=3\); \(d=4\); \(d=5\); \(d\ge6\) | 6 |
| Odd \(r\ge3\) | \(d=1\); \(2\le d\le r\); \(d=r+1\); \(r+2\le d\le(3r+1)/2\); \((3r+3)/2\le d\le 2r\); \(d=2r+1\); \(d\ge2r+2\) | 7 |
| Even \(r\ge4\) | \(d=1\); \(2\le d\le r\); \(d=r+1\); \(r+2\le d\le3r/2\); \(d=3r/2+1\); \(3r/2+2\le d\le2r\); \(d=2r+1\); \(d\ge2r+2\) | 8 |

In particular, for every fixed \(r\ge1\), all dimensions \(d\ge2r+2\) have one rank-three theory, but the dimension \(2r+1\) is distinguishable from them. The smallest maximum number of vertices needed to represent every class **within this fixed-radius family** is exactly \(2^{2r+2}\). The additional middle class for even radii is a genuine parity effect.

## Assumptions and scope
The graphs are finite, simple, undirected, and have nonempty vertex sets. Only adjacency and equality belong to the language: neither Hamming distance nor coordinates nor the radius are named inside the structure. The comparison holds with \(r\) fixed, rather than asserting the classification of cross-radius pairs. Quantifier rank is nesting depth, with arbitrary Boolean combinations allowed. There are no counting quantifiers and no extra constants. Every claim is uniform in all positive integers \(d\) and \(r\).

## Proof
**1. The three-round reduction.** For an ordered pair \((x,y)\), its one-extension profile consists of whether \(x=y\), whether \(x\) and \(y\) are adjacent, and which of the four adjacency patterns \((E(x,z),E(y,z))\in\{0,1\}^2\) are realized by a vertex \(z\notin\{x,y\}\). Together with the two equality responses \(z=x\) and \(z=y\), these data determine the complete quantifier-rank-one type of the pair. Every graph \(G_{d,r}\) is vertex-transitive under word translations. Therefore the quantifier-rank-two type of one vertex is determined by the set of profiles of its ordered pairs with possible second vertices, and the rank-three sentence theory is determined by that set. Conversely, if the profile sets differ, a Boolean combination of one-quantifier formulas describes a profile present on one side and absent on the other; prefixing \(\exists x\exists y\) distinguishes the graphs at rank at most three. Thus equality of the pair-profile sets is an *if and only if* criterion, not merely a sufficient game strategy.

**2. Exact Hamming extension criterion.** Put \(h=\delta(x,y)\). By translating and permuting coordinates, take \(x=0^d\) and \(y\) of weight \(h\). A third word \(z\) flips \(i\) of the \(h\) differing coordinates and \(j\) of the \(d-h\) remaining coordinates. The distances are exactly
\[
\delta(x,z)=i+j,\qquad \delta(y,z)=h-i+j,
\]
where \(0\le i\le h\) and \(0\le j\le d-h\). For \(x\ne y\), the following four pattern rules are necessary and sufficient, with the requirement \(z\ne x,y\):

- Pattern \((1,1)\) exists precisely when \(2\le h\le2r\), or when \(h=1\), \(r\ge2\), and \(d\ge2\).
- Both patterns \((1,0)\) and \((0,1)\) exist precisely when \(h\le r\) and \(d\ge r+1\), or \(h=r+1\) and \(d\ge r+2\), or \(h\ge r+2\). By exchanging \(x\) and \(y\), one of these patterns exists if and only if both do.
- Pattern \((0,0)\) exists precisely when
\[
 d\ge r+\lceil h/2\rceil+1.
\]
- The pair itself is adjacent precisely for \(1\le h\le r\).

For completeness, if \(x=y\), a distinct \(z\) realizes \((1,1)\), and also realizes \((0,0)\) precisely when \(d\ge r+1\); no mixed patterns occur.

To prove the third rule, the maximum of \(\min\{\delta(x,z),\delta(y,z)\}\) over all words is
\[
 d-\lceil h/2\rceil:
\]
flip all \(d-h\) agreeing coordinates, and split the \(h\) differing coordinates as evenly as possible. This maximum also gives necessity because decreasing \(j\) decreases both distances and the smaller of \(i\) and \(h-i\) never exceeds \(\lfloor h/2\rfloor\). The bound being at least \(r+1\) automatically excludes \(z=x,y\). For the first rule use an interior point of a shortest Hamming path when \(h\ge2\); at \(h=1\), a common neighbor exists exactly when a second coordinate may be flipped and \(r\ge2\). The second rule follows by flipping an agreeing coordinate when available, or one differing coordinate if \(h\ge r+2\). In an adjacent pair with \(d\ge r+1\), flip up to \(r\) agreeing coordinates (all when fewer are available), producing a neighbor of one endpoint outside the ball of the other. If \(h=r+1=d\), every vertex adjacent to one endpoint is also adjacent to the other; these constructions exhaust the exceptions. All steps follow directly from the displayed integer ranges.

**3. Exact classification by profile thresholds.** If \(d\le r\), the graph is complete; \(G_{1,r}\) has two vertices and all \(G_{d,r}\), \(2\le d\le r\), are complete graphs of at least four vertices and hence mutually rank-three equivalent. Suppose \(d\ge r+1\). At \(d=r+1\), the sole nonedge distance \(h=r+1\) has no mixed extension; this profile disappears for all larger dimensions. For \(d\ge r+2\), edge pairs have a \((0,0)\) extension for some distances \(h\le r\). Every edge-pair distance has that extension exactly from
\[
 d\ge r+\lceil r/2\rceil+1.
\]
A nonedge pair that has a common neighbor first admits a \((0,0)\) extension at
\[
 d\ge r+\lceil (r+1)/2\rceil+1.
\]
These thresholds coincide for odd \(r\), and differ by exactly one for even \(r\). Prior to the first threshold, edges with and without \((0,0)\) both occur (when the interval is nonempty); between the two even-radius thresholds only the all-\((0,0)\)-edge and no-\((0,0)\)-nonedge profiles occur; after the second, nonedges with and without \((0,0)\) both occur until \(d=2r\). Hence the middle intervals are exactly those displayed in the table.

At \(d=2r+1\), the first pair at distance greater than \(2r\) occurs. It lacks both a common neighbor and a \((0,0)\) extension. At \(d\ge2r+2\), such far nonedge pairs all have a \((0,0)\) extension, and the extension profiles at every distance fall into a fixed finite set, independent of \(d\). For dimensions at most \(2r\), there is no far pair. Each successive regime changes the presence or absence of at least one distinct pair profile; there is no return to an earlier profile set. The special cases \(r=1,2\) follow from the same rules after empty intervals are discarded, with the \(h=1\) common-neighbor exception observed above. This establishes both equivalences within rows and inequivalences across rows for all parameters.

**4. Sharp vertex bound.** A graph at dimension \(d\) has exactly \(2^d\) vertices. The stable final class begins at dimension \(2r+2\), and no smaller dimension belongs to it. It therefore requires at least \(2^{2r+2}\) vertices among representatives from this fixed-radius family, while that graph represents every larger dimension. Every other class has a representative of smaller dimension.

## Verification
The accompanying \(\texttt{verify.py}\) implements (a) direct vertex enumeration of all third-vertex patterns, (b) independent two-integer Hamming-orbit enumeration, and (c) the closed symbolic criterion. The direct and symbolic rank-three signatures agree for all 42 pairs with \(1\le d\le9\) and \(1\le r\le\min(d,7)\); the orbit rule agrees with the symbolic criterion for every parameter through radius 18 and all dimensions through \(2r+5\). The closed criterion reproduces the asserted classification for every radius through 150 and dimensions through \(2r+5\). These are regression and boundary checks, not the proof of the unbounded theorem; Steps 1–4 provide that proof.

## Relationship to prior work
Fu, Ling, and Xing (arXiv:1001.2209, first public version 2010-01-13) study binary Hamming-distance colorings for general distance thresholds. Kokkala and Östergård (arXiv:1607.01605, first public version 2016-07-06) analyze colorings of the square of the eight-cube. Their examined papers give the canonical graph-power setting but concern chromatic and coding invariants, not first-order rank-three equivalence or a radius-parity class count. General finite-model-theory game principles justify the profile method. A previously recorded classification of the ordinary hypercube at quantifier rank four implies a *partial* upper-tail statement for the square power via interpreting distance at most two, but does not yield the all-radius phase diagram or the distinguishing directions. Relevant mathematical-index searches found no matching rank-three graph-power classification; that absence is not a uniqueness certificate.

## Limitations
The result compares dimensions for a *fixed* radius and does not classify \(G_{d,r}\) versus \(G_{e,s}\) for different radii. It concerns first-order logic without counting quantifiers and does not determine spectra, chromatic numbers, or higher-rank theories. A mathematical proof and finite independent-format calculations are provided, but no independent external mathematical audit has been performed. Unindexed or inaccessible literature may contain equivalent results.

## References
1. F.-W. Fu, S. Ling, and C. Xing, *New Results on Two Hypercube Coloring Problems*, arXiv:1001.2209, first public version 2010-01-13. https://arxiv.org/abs/1001.2209
2. J. I. Kokkala and P. R. J. Östergård, *The chromatic number of the square of the 8-cube*, arXiv:1607.01605, first public version 2016-07-06. https://arxiv.org/abs/1607.01605
3. Ehrenfeucht–Fraïssé finite-game equivalence theorem, standard finite-model-theoretic background; see, e.g., lecture notes at https://pi.math.cornell.edu/~mec/Summer2009/Raluca/lesson5.html .
