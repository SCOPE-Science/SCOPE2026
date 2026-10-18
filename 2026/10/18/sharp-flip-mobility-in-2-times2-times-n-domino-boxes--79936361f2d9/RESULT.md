# Sharp flip mobility in \(2\times2\times n\) domino boxes

## Finding
For every integer \(n\ge1\), let \(B_n\) consist of the \(4n\) unit cubes of a rectangular \(2\times2\times n\) box. Let \(\mathcal F_n\) be the simple graph of all (position-distinguished, not identified under spatial symmetry) domino tilings of \(B_n\), where an edge represents replacing two parallel dominoes occupying one elementary \(2\times2\times1\) slab by the other pairing of those four cubes. Every flip acts on exactly four cubes.

The smallest and largest vertex degrees in this graph are exactly
\[
\boxed{\delta(\mathcal F_n)=\left\lceil\frac{2n}{3}\right\rceil,
\qquad \Delta(\mathcal F_n)=3n-2.}
\]
The maximum is attained by exactly two tilings when \(n=1\) or \(n\ge3\), and by exactly three tilings when \(n=2\). For \(n\ge3\), the two maximizing tilings are the two uniform transverse pairings of every four-cube layer.

If \(n=3k\) with \(k\ge1\), the minimum-degree tilings have an exact structural classification: they are concatenations of \(k\) alternating-vertical-pair blocks of length three, indexed by successive adjacent pairs \(A_1,\ldots,A_k\) of a four-cycle satisfying \(A_{i+1}\ne A_i^c\) (complement within the four vertices). Consequently their number is exactly
\[
\boxed{4\cdot3^{k-1}.}
\]
The proof also supplies a fixed finite-state transfer formula for the *entire* degree enumerator \(P_n(q)=\sum_{T\in V(\mathcal F_n)}q^{\deg(T)}\), not only its two extremal degrees.

## Assumptions and scope
Coordinates are \((x,y,z)\in\{0,1\}\times\{0,1\}\times\{1,\ldots,n\}\). Two unit cubes are adjacent exactly when their coordinate triples differ by one in exactly one coordinate. A domino is one such adjacent pair. Different tilings are different perfect matchings of this finite adjacency graph. A flip is counted once for each distinct elementary square containing two matching edges on opposite sides. Different elementary squares give different adjacent tilings. No flips of six or more cubes, no trits, and no identification by rotation or reflection are permitted.

Label the four cubes in each layer cyclically by \(0,1,2,3\), so their transverse adjacency graph is \(C_4\). Put \(A_j=\{j,j+1\pmod4\}\) for its four adjacent vertex pairs. The complement of \(A_j\) in \(\{0,1,2,3\}\) is again an adjacent pair. An internal *ring edge* is one of the four edges of this \(C_4\).

## Proof
**1. Normal form for all tilings.** For \(0\le i\le n\), let \(S_i\subseteq\{0,1,2,3\}\) be the set of positions carrying dominoes between layers \(i\) and \(i+1\), with \(S_0=S_n=\varnothing\). The two plugs \(S_{i-1}\) and \(S_i\) are disjoint, and the other positions within layer \(i\) must be perfectly matched using ring edges.

When the incoming plug is empty, the outgoing plug can only be empty, one of the four adjacent pairs \(A_j\), or the full four-set. Indeed, its complement must have an internal perfect matching on the ring. When the incoming plug is full, the outgoing plug is necessarily empty. When the incoming plug is an adjacent pair \(A\), the outgoing plug must be either empty or its complementary pair \(A^c\): these are the only disjoint outgoing possibilities leaving an internally matchable set. Therefore every tiling decomposes *uniquely* at the empty plugs into consecutive blocks of the following forms:

* A one-layer **monomer block** with its four ring vertices paired in one of two ways.
* A two-layer **full block** with all four interlayer dominoes.
* A **pair-tube block** of length \(m\ge2\), specified by its initial adjacent pair \(A\), whose consecutive nonempty interlayer plugs are \(A,A^c,A,A^c,\ldots\), followed by the empty plug. It has the forced single transverse ring edges at its two endpoint layers and no ring edges at interior layers.

Every such block concatenation is a tiling, establishing that the decomposition is exhaustive and unique.

**2. Exact local flip accounting.** A one-layer block has one internal ring-square flip. A full two-layer block has four side-square flips from its four adjacent pairs of interlayer dominoes. A pair-tube block of length two has two internal flips: its vertical pair can rotate to two transverse ring edges, and its two already present identical endpoint ring edges can rotate to a complementary pair of vertical dominoes. A pair-tube block of length \(m\ge3\) has exactly \(m-1\) internal flips, one at each nonempty plug; its two endpoint ring edges are never on consecutive layers. In short, the internal contributions \(f(B)\) are
\[
 f(B)=\begin{cases}
 1&\text{monomer, length }1,\\
 4&\text{full block, length }2,\\
 2&\text{pair tube, length }2,\\
 m-1&\text{pair tube, length }m\ge3.
 \end{cases}
\]
At a junction of two blocks, the interlayer plug is empty. The only possible flips there come from ring edges which coincide in both adjacent endpoint layers. If \(R\) and \(R'\) are those layers' sets of ring edges, the contribution is \(|R\cap R'|\in\{0,1,2\}\). All face orientations have thereby been counted exactly once.

**3. Lower bound and all its equality cases when three divides the length.** Each block satisfies \(f(B)\ge2\,\operatorname{len}(B)/3\), with equality precisely for a length-three pair tube. Junction contributions are nonnegative. Thus for every tiling \(T\),
\[
 \deg(T)\ge\frac{2n}{3},\qquad \deg(T)\ge\left\lceil\frac{2n}{3}\right\rceil.
\]
Choose successive length-three tubes. A tube starting with plug \(A_i\) ends in a ring edge on \(A_i\), while its first layer has a ring edge on \(A_i^c\). Therefore the junction between successive tubes has no available flip exactly when \(A_{i+1}\ne A_i^c\). Four choices exist for the first adjacent pair and three for each subsequent one, proving that the minimum is attained by precisely \(4\cdot3^{k-1}\) tilings when \(n=3k\). Conversely, equality at \(n=3k\) forces every block to have length three and every junction contribution to vanish, giving the complete classification.

For \(n=3k+1\), append one monomer whose two ring edges have the *other transverse orientation* from the final ring edge of the previous tube, so the new junction contributes zero. When \(k=0\), use a monomer by itself. For \(n=3k+2\), append one length-two pair tube with its first ring edge different from the preceding tube's last ring edge, again creating no junction flip. When \(k=0\), use that length-two tube alone. The resulting total internal degrees are respectively \(2k+1\) and \(2k+2\), proving the lower bound is sharp in all residue classes.

**4. Upper bound and rigidity.** For every block \(B\) of length \(m\), \(f(B)\le3m-2\): equality holds for a monomer and for a full length-two block; it is strict for all pair-tube blocks. If a tiling has \(b\) blocks, its \(b-1\) junctions each contribute at most two. Hence
\[
 \deg(T)\le\sum_B(3\operatorname{len}(B)-2)+2(b-1)=3n-2.
\]
Uniformly matching all layers in either of the two ring orientations realizes \(n\) layer flips plus two flips at each of \(n-1\) interfaces, hence equality. No pair-tube can occur in an equality tiling. A full block has no ring edge at either endpoint, so an external junction next to it contributes zero rather than two. Therefore, if \(n\ge3\), any full block also prevents equality. Every layer must then be a monomer, and every consecutive pair must use the same ring orientation; precisely the two uniform tilings remain. At \(n=2\), the single full block is an additional maximizer. At \(n=1\), both monomer orientations maximize.

**5. Complete degree enumerator.** A fully explicit transfer representation is given by the sixteen layer types \(u=(a_u,b_u,R_u,c_u)\). Here \(a_u,b_u\) are respectively incoming and outgoing plugs, \(R_u\) is the subset of the four ring-edge labels used in the layer, and \(c_u\in\{0,1\}\) is the cap-face flip count. The types are: two types \((\varnothing,\varnothing,R,1)\), one for each perfect ring pairing \(R\); four types \((\varnothing,A,\{A^c\},0)\); four \((A,\varnothing,\{A^c\},0)\); four \((A,A^c,\varnothing,0)\); and the two types \((\varnothing,F,\varnothing,0)\), \((F,\varnothing,\varnothing,0)\), where \(F=\{0,1,2,3\}\). In \(\{A^c\}\), the complement pair is interpreted as its unique ring-edge label.

Set \(\nu(S)\) equal to the number of adjacent pairs contained in the plug \(S\); thus \(\nu(\varnothing)=0\), \(\nu(A)=1\), and \(\nu(F)=4\). Define a \(16\times16\) matrix, initial row, and terminal column by
\[
 W(q)_{uv}=\mathbf1_{b_u=a_v}\,q^{c_v+\nu(b_u)+|R_u\cap R_v|},\quad
 h(q)_u=\mathbf1_{a_u=\varnothing}q^{c_u},\quad
 t_u=\mathbf1_{b_u=\varnothing}.
\]
Then, for every \(n\ge1\),
\[
 \boxed{P_n(q)=h(q)W(q)^{n-1}t.}
\]
Each path of layer types is in bijection with one tiling and its exponent equals its number of distinct available elementary flips by Step 2. This formula determines all degree multiplicities without constructing the full reconfiguration graph.

## Verification
The standalone `verify_direct.py` enumerates all perfect matchings of the actual three-dimensional cube-adjacency graph and counts exactly the legal opposite-edge pairs on each elementary square. Independently, `verify_transfer.py` uses the sixteen-layer state description and a weighted transfer computation; the first program does not use the normal form or its transition weights. Their full degree histograms agree identically for every \(1\le n\le8\), covering \(2,9,32,121,450,1681,6272,23409\) tilings. The transfer computation also checks the extremal formulas through \(n=15\). The all-orders claim is proved by Steps 1–4, not inferred from finite tests.

Reproduce in Python 3 without extra packages by executing `python3 verify_direct.py` and `python3 verify_transfer.py`. Each prints its degree-enumerator certificate followed by `DIRECT_VERIFY_OK` or `TRANSFER_VERIFY_OK`. The two packaged outputs contain the full exact coefficient dictionaries for \(n\le8\), with identical first lines.

## Relationship to prior work
Milet and Saldanha's 2014 preprint on two-story domino tilings defines the standard elementary flip and explicitly records flip connectivity for \(L\times2\times2\) boxes as an elementary observation. Their 2014 general-cylinder paper develops the twist invariant and different phenomena for thicker three-dimensional regions. The present result neither rediscovers that connectivity nor uses twist: it determines the *minimum and maximum number of immediately available flips*, their extremal multiplicities, the classification of all least-mobile tilings for lengths divisible by three, and a degree-enumeration transfer representation.

Liu, Wang, Li and Zhang's 2022 work on flat quadriculated cylinders studies connected components and forcing numbers for periodic two-dimensional tilings. It does not give these three-dimensional thin-box face-flip degree formulas; the present move set includes ring-square flips in every end-cap-style layer, not merely cylindrical side-face flips. Later work on three-dimensional domino groups and twist distributions is about components and asymptotics rather than this exact local-degree problem. General resonance-graph results about connectivity cannot by themselves yield this degree distribution.

## Limitations
Only unit dominoes in the exact \(2\times2\times n\) box, with elementary four-cube flips and fixed cube positions, are covered. The proof does not determine shortest flip distances, mixing times, spectral gaps, or analogous formulas for thicker boxes. It does not claim the already known connectivity as a discovery. Novelty is assessed against accessible literature and mathematical-record searches, not independently certified priority; an equivalent result in unindexed work is possible. No independent external mathematical audit has been performed.

## References
1. P. H. Milet and N. C. Saldanha, *Flip invariance for domino tilings of three-dimensional regions with two floors*, arXiv:1404.6509 (first public version April 25, 2014), https://arxiv.org/abs/1404.6509.
2. P. H. Milet and N. C. Saldanha, *Domino tilings of three-dimensional regions: flips, trits and twists*, arXiv:1410.7693 (first public version October 28, 2014), https://arxiv.org/abs/1410.7693.
3. N. C. Saldanha, *Domino tilings of cylinders: connected components under flips and normal distribution of the twist*, arXiv:2007.09500 (2020), https://arxiv.org/abs/2007.09500.
4. Q. Liu, J. Wang, C. Li and H. Zhang, *Components of domino tilings under flips in quadriculated cylinder and torus*, arXiv:2211.10935 (2022), https://arxiv.org/abs/2211.10935.
