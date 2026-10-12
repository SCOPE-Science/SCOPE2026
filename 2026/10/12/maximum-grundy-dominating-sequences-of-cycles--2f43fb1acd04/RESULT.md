# Maximum Grundy dominating sequences of cycles

## Finding

Let \(C_n\) be the labeled cycle on \(\mathbb Z_n\). A legal closed-neighborhood sequence is a sequence \(S=(v_1,\ldots,v_k)\) of distinct vertices such that each \(v_i\) footprints at least one vertex not contained in \(\bigcup_{j<i}N[v_j]\); it is dominating when the union of these closed neighborhoods is all of \(V(C_n)\). For every \(n\ge4\), the known scalar value is \(\gamma_{\mathrm{gr}}(C_n)=n-2\).

The maximum sequences have a complete frontier description. Once \(v_1\) is chosen, the initially undominated vertices form one cyclic interval. While that interval has at least two vertices, the next term must be one of the two already dominated frontier vertices, and it removes exactly one endpoint of the undominated interval. When one undominated vertex remains, the final term may be that vertex or either of its two frontier neighbors.

Hence the number of ordered maximum Grundy dominating sequences is
\[
3n2^{n-4}.
\]
Their underlying vertex sets are exactly the complements of pairs of vertices at cyclic distance \(1\) or \(2\). Thus there are \(6\) maximum Grundy dominating sets when \(n=4\), and \(2n\) when \(n\ge5\). For \(n\ge5\), every set omitting an adjacent pair supports exactly \(2^{n-3}\) maximum sequences, and every set omitting a distance-two pair supports exactly \(2^{n-4}\) maximum sequences.

## Assumptions and scope

Graphs are finite, simple, and undirected. Cyclic distance means the ordinary graph distance in \(C_n\). The theorem concerns ordinary Grundy domination using closed neighborhoods, not Grundy total, Z-Grundy, or L-Grundy variants. The scalar identity \(\gamma_{\mathrm{gr}}(C_n)=n-2\) is used as prior work; the contribution here is the all-extremizer classification and exact sequence/set census.

## Proof

Fix \(n\ge4\) and a maximum Grundy dominating sequence \(S=(v_1,\ldots,v_{n-2})\). The first term footprints exactly the three vertices of \(N[v_1]\). Every later term footprints at least one new vertex. There are \(n-3\) later terms and exactly \(n-3\) vertices remain after the first footprint, so every later term must footprint exactly one new vertex.

After choosing \(v_1\), the undominated vertices form a path of \(n-3\) consecutive cycle vertices. Suppose at some later stage that the undominated set is a nonempty consecutive path \(U\). If \(|U|\ge2\), an undominated vertex footprints at least two vertices of \(U\), so it cannot be the next term of a maximum sequence. A dominated vertex away from the two boundaries footprints nothing. The only vertices that footprint exactly one new vertex are the two dominated frontier vertices adjacent to the endpoints of \(U\). Neither frontier vertex has already appeared in the sequence, because if it had been selected then its current adjacent endpoint of \(U\) would already be dominated. Therefore exactly two legal maximum-preserving choices are available, one deleting the left endpoint and one deleting the right endpoint of \(U\).

There are \(n-4\) such binary frontier choices before \(|U|=1\). If \(U=\{x\}\), the only legal terms that footprint the last undominated vertex are \(x\) and its two frontier neighbors, and all three are unselected. Thus, for each of the \(n\) choices of \(v_1\), there are \(2^{n-4}\) frontier words and then three final choices. This proves the ordered count \(3n2^{n-4}\).

At the terminal stage the three possible final terms lie in a consecutive triple \(\ell,x,r\). The two vertices not used by the sequence are therefore either \(\{\ell,x\}\), \(\{x,r\}\), or \(\{\ell,r\}\): respectively an adjacent pair, an adjacent pair, or a distance-two pair. Conversely, the frontier construction can be reversed from any such omitted pair, so these and only these pairs occur.

For \(n\ge5\), there are \(n\) adjacent pairs and \(n\) distance-two pairs, giving \(2n\) maximum sets. Among the \(3n2^{n-4}\) frontier encodings, the two frontier choices at the final step produce an adjacent omitted pair, so there are \(2n2^{n-4}=n2^{n-3}\) ordered maxima of adjacent-pair type. The terminal choice \(x\) produces a distance-two omitted pair, so there are \(n2^{n-4}\) ordered maxima of distance-two type. The dihedral group of \(C_n\) acts transitively on the \(n\) adjacent pairs and separately on the \(n\) distance-two pairs while preserving legal-sequence multiplicity. Hence every adjacent omitted pair supports \(2^{n-3}\) maximum sequences and every distance-two omitted pair supports \(2^{n-4}\). When \(n=4\), the four adjacent omitted pairs and two opposite pairs each support two maximum sequences, so there are six sets and twelve sequences.

## Verification

The included `verify.py` performs an independent exhaustive search over legal closed-neighborhood dominating sequences for \(3\le n\le10\). It checks the maximum length, the formula \(3n2^{n-4}\) for \(n\ge4\), the omitted-pair characterization, the \(n=4\) boundary case, and the per-set multiplicities for \(n\ge5\). The finite replay is corroborative; the arbitrary-order result is established by the proof above.

## Relationship to prior work

Brešar et al., *Dominating sequences in grid-like and toroidal graphs*, give the same definition, list primary MSC 05C69, and explicitly use the known fact \(\gamma_{\mathrm{gr}}(C_n)=n-2\). Their paper studies Grundy domination numbers of graph products; inspection of the full text did not locate an enumeration of maximum sequences of a single cycle or a classification of their underlying sets.

Brešar and Dravec, *Graphs with unique Grundy dominating sets*, explicitly motivate the question of how many extremal sets an invariant has and study uniqueness up to automorphism. Their results do not supply the cycle census above; in particular, their ordinary Grundy-domination uniqueness discussion is qualitative rather than an enumeration of cycle extremizers.

## Limitations

The theorem is restricted to cycles. It counts ordered sequences and separately counts their underlying sets; these are different quantities. The originality assessment cannot exclude a poorly indexed equivalent enumeration under different terminology. No claim is made that the known scalar value \(\gamma_{\mathrm{gr}}(C_n)=n-2\) is new.

## References

1. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, B. Patkós, Z. Tuza, and M. Vizer, “Dominating sequences in grid-like and toroidal graphs,” arXiv:1607.00248v1, 1 July 2016; *Electronic Journal of Combinatorics* 23(4), P4.34 (2016), DOI: 10.37236/6269.
2. B. Brešar and T. Dravec, “Graphs with unique Grundy dominating sets,” *Computational and Applied Mathematics* 45, 444 (2026), DOI: 10.1007/s40314-026-03835-w.
