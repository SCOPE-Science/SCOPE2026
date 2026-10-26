# Sharp four-leaf survival law for detecting noncaterpillar phylogenies by rarefaction

## Finding

Let \(T\) be an unrooted binary phylogenetic tree with \(n\geq6\) leaves that is **not** a caterpillar. Independently of its topology, take a uniformly random subset \(S\) of exactly \(k\) leaves, \(6\leq k\leq n\). Let \(T|S\) denote the reduced minimal connecting tree, with all degree-two vertices suppressed. Then

\[
\Pr(T|S\text{ is not a caterpillar})\ \geq\ \frac{(k)_4}{(n)_4}
=\frac{\binom{n-4}{k-4}}{\binom nk},
\]

where \((r)_4=r(r-1)(r-2)(r-3)\). For \(n\geq7\) and every \(6\leq k<n\), equality holds **if and only if** \(T\) has the following unlabelled shape \(F_n\): a degree-three central vertex attaches to two two-leaf cherries and to the root of a binary comb containing the other \(n-4\) leaves. This shape attains equality simultaneously at all sampling sizes. At \(k=n\), equality holds for every noncaterpillar \(T\); at \(n=k=6\), there is only one noncaterpillar binary shape.

A sample of at most five leaves always induces a caterpillar. Thus six is the sharp minimum sample size that can reveal noncaterpillar structure. For six leaves the event means precisely that the induced tree has three cherries. If \(N_6(T)\) counts such six-subsets, then

\[
N_6(T)=\sum_{v\text{ internal}}
\binom{a_v}{2}\binom{b_v}{2}\binom{c_v}{2}
\ \geq\ \binom{n-4}{2},
\]

where \(a_v,b_v,c_v\) are the numbers of leaves in the three components of \(T-v\); equality is attained precisely by \(F_n\) when \(n\geq7\). With \(m\) independent random six-leaf samples, the worst-case probability of detecting a noncaterpillar is exactly \(1-[1-360/(n)_4]^m\) for the extremal shape. For fixed detection confidence and increasing \(n\), this requires sampling effort of order \(n^4\).

## Assumptions and scope

The phylogeny is finite, unrooted, and binary: leaves have degree one and all other vertices degree three; internal degree-two subdivisions are ignored. A *caterpillar* has its internal vertices on one path. Each \(k\)-subset is equiprobable. Topology, not edge lengths or sequence reconstruction error, is the observable. The label set is irrelevant up to leaf permutation. All probability statements are conditional on a fixed noncaterpillar host tree, with \(n\ge6\) and integer \(6\le k\le n\). The six-leaf sampling repetitions in the power formula are independent draws with replacement between samples, while each individual sample uses distinct leaves.

## Proof

**1. Structural witness.** For any vertex \(v\) of degree three, call it *triply internal* if each of the three components of \(T-v\) contains at least two leaves. A binary tree is noncaterpillar if and only if it has a triply internal vertex. Indeed, a component with just one leaf has no other vertices, so absence of such a vertex says that every internal vertex has at least one leaf neighbor; equivalently, the subgraph of internal vertices has maximum degree two and, being connected, is a path. The criterion remains valid in a reduced induced tree: \(T|S\) is noncaterpillar exactly if for some original internal vertex \(v\), at least two selected leaves lie in each of the three components of \(T-v\). Pruning cannot create a previously absent triply internal vertex.

**2. Four-leaf deletion lemma.** Let \(U\) be noncaterpillar with \(r\ge7\) leaves and let \(D(U)\) be the set of leaves whose deletion (followed by suppression of the resulting degree-two vertex) produces a caterpillar. Fix a triply internal vertex \(v\) and denote its three branch sizes by \(a,b,c\ge2\), with sum \(r\). Deleting a leaf outside a branch containing exactly two leaves leaves all three branches with at least two leaves. Thus every member of \(D(U)\) belongs to a size-two branch. As \(r\ge7\), there are at most two such branches, each containing two leaves. Hence \(|D(U)|\le4\).

Equality \(|D(U)|=4\) forces two size-two branches at \(v\) and all their leaves to be destructive. There can be no second triply internal vertex \(w\): it cannot occur in either size-two branch; if it lies in the remaining branch, deleting one leaf from a size-two branch leaves the direction from \(w\) toward \(v\) containing at least three leaves, without changing its two other directions, so \(w\) persists. This contradicts destructiveness. Hence \(v\) is the only triply internal vertex. The remaining rooted branch must be a comb (each internal vertex has a leaf child, until the terminal cherry). Therefore \(U\) has shape \(F_r\). Conversely, \(F_r\) has exactly four destructive leaves, namely those in the two side cherries; removal of any other leaf leaves \(F_{r-1}\). For \(r=7\), \(F_{r-1}\) is the unique noncaterpillar six-leaf shape.

**3. Uniform pruning.** Construct a uniform \(k\)-subset by repeatedly deleting a uniformly chosen leaf from the current reduced tree until \(k\) leaves remain. Every \(k\)-subset has the same probability. Caterpillarhood is preserved by deletion, so noncaterpillar status can only be lost, never regained. Conditional on a noncaterpillar reduced tree of \(r\ge7\) leaves, the deletion lemma shows that the probability of retaining noncaterpillar status after one deletion is at least \((r-4)/r\). Iterating from \(n\) down to \(k\) yields

\[
\Pr(T|S\text{ noncaterpillar})\ge
\prod_{r=k+1}^{n}\frac{r-4}{r}
=\frac{k(k-1)(k-2)(k-3)}{n(n-1)(n-2)(n-3)}.
\]

When \(T=F_n\), every successful pruning produces \(F_r\), and at every stage there are exactly four destructive leaves. Hence equality holds. When \(6\le k<n\) and \(T\ne F_n\), the first deletion has strictly more than \((n-4)/n\) chance of preserving noncaterpillar status by the equality case of the deletion lemma; subsequent conditional factors are no smaller. The overall inequality is then strict. This proves uniqueness.

**4. Sextet count and sampling effort.** A six-leaf reduced unrooted binary tree is noncaterpillar precisely when it has three cherries around a unique central vertex. For a given host internal vertex \(v\) with leaf-branch sizes \(a_v,b_v,c_v\), selecting exactly two leaves in each branch yields that pattern. Each such six-set has exactly one central vertex, so no double counting occurs, establishing the stated sum. The \(k=6\) probability formula then yields the sharp lower bound. For independent repeated six-leaf draws, the miss probability is the \(m\)-th power of the single-sample miss probability. In the extremal host, the success probability is \(360/(n)_4\), so the number of draws for a fixed nontrivial confidence threshold grows proportionally to \(n^4\).

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The checker independently generates every unlabelled unrooted binary tree shape through eleven leaves, verifies the exact combinatorial bound for every permissible sample size on every noncaterpillar shape, checks uniqueness in the nontrivial range, and compares the branch criterion against explicit minimal-subtree construction in 770 individual cases. It also checks the sextet branch-product identity and the four-leaf deletion lemma. `verify_output.txt` records the actual run result. These finite checks corroborate but do not replace the all-size proof.

## Relationship to prior work

Fischer and Liebscher (2015, arXiv:1510.07882) optimize functionals of unrooted phylogenetic-tree **edge-split sizes**. Such functionals do not directly give the present bound on the probability that an induced sample has a non-path internal skeleton. Czabarka, Székely and Wagner (2016, arXiv:1601.07149) introduce inducibility for **rooted binary trees**, especially extremal *maximum* densities of specified rooted shapes. Czabarka and collaborators (2018, arXiv:1802.03817) extend maximal-density inducibility to rooted degree-bounded trees. Dossou-Olory and Boadi (2022, arXiv:2206.14287) minimize the number of **nonisomorphic induced shapes** for rooted topological trees, rather than the frequency of a noncaterpillar outcome under uniform sampling. None of these treatments, as inspected, states the finite all-\(n\), all-\(k\) sharp lower detection bound or its unique unrooted extremizer.

## Limitations

The theorem is a mathematical worst-case bound for exact known tree shapes and uniform taxon sampling, not a finite-data phylogeny-inference guarantee. Label errors, branch-length uncertainty, sampling bias, polytomies, and unrooted multifurcations can invalidate its assumptions. For \(k=n\), all noncaterpillar trees tie, so uniqueness is deliberately restricted to \(k<n\). The finite verification stops at eleven host leaves; only the analytical deletion argument establishes the unrestricted theorem. Existing inducibility and phylogenetic balance literature is extensive, so a previously overlooked equivalent finite bound remains a bibliographic risk.

## References

- Fischer, M. and Liebscher, V. (2015). *On the Balance of Unrooted Trees*. arXiv:1510.07882, first posted 2015-10-27. https://arxiv.org/abs/1510.07882
- Czabarka, É., Székely, L. A. and Wagner, S. (2016). *Inducibility in binary trees and crossings in random tanglegrams*. arXiv:1601.07149, first posted 2016-01-26. https://arxiv.org/abs/1601.07149
- Czabarka, É., Dossou-Olory, A. A. V., Székely, L. A. and Wagner, S. (2018). *Inducibility of d-ary trees*. arXiv:1802.03817, first posted 2018-02-11. https://arxiv.org/abs/1802.03817
- Dossou-Olory, A. A. V. and Boadi, I. (2022). *On isomorphism classes of leaf-induced subtrees in topological trees*. arXiv:2206.14287, first posted 2022-06-26. https://arxiv.org/abs/2206.14287
