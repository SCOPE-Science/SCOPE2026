# Complete commuting-clique geometry of the braid face monoid

## Finding

Let \(B_n\) be the monoid of ordered set partitions of \([n]\) under the Tits face product, for an integer \(n\geq1\). The full commuting graph \(\Gamma_n\) has one vertex per ordered partition and an edge between two *distinct* vertices precisely when their Tits products agree in both orders. All statements below concern the actual finite monoid and this full graph, not its complex semigroup algebra.

**Structural classification.** The maximal cliques of \(\Gamma_n\) are exactly the sets \(\mathcal C_\sigma\) of all consecutive-block coarsenings of a permutation \(\sigma\in\mathfrak S_n\). There are exactly \(n!\) maximal cliques, each containing \(2^{n-1}\) faces. Every clique lies inside one of them. For any permutations \(\sigma,\tau\), put
\[
d(\sigma,\tau)=\#\{j:1\le j<n,\ \{\sigma(1),\ldots,\sigma(j)\}=\{\tau(1),\ldots,\tau(j)\}\}.
\]
Then
\[
|\mathcal C_\sigma\cap\mathcal C_\tau|=2^{d(\sigma,\tau)}.
\]
For a fixed \(\sigma\), the complete distribution of intersections is determined by the numbers \(a_m\) of indecomposable permutations under direct sum: \(a_1=1\), \(a_m=m!-\sum_{j=1}^{m-1}a_j(m-j)!\). Specifically, if \(N_{n,k}\) is the number of \(\tau\in\mathfrak S_n\) for which \(|\mathcal C_\sigma\cap\mathcal C_\tau|=2^{k-1}\), then
\[
N_{n,k}=\sum_{m_1+\cdots+m_k=n\atop m_i\ge1}\prod_{i=1}^k a_{m_i},\qquad1\le k\le n.
\]
These counts are independent of \(\sigma\).

**Centralizers and graph degrees.** Let \(F_m=\sum_{j=1}^m j!\left\{\begin{smallmatrix}m\\j\end{smallmatrix}\right\}\) for \(m\ge1\), and \(F_0=1\), so \(F_m\) is the number of ordered partitions of an \(m\)-element set. If \(\alpha=(A_1,\ldots,A_b)\), then
\[
|C_{B_n}(\alpha)|=2^{b-1}\prod_{i=1}^b F_{|A_i|}.
\]
Consequently \(\deg_{\Gamma_n}(\alpha)=2^{b-1}\prod_iF_{|A_i|}-1\). Every possible degree, with multiplicity, is specified by the polynomial
\[
D_n(z)=\sum_{b=1}^n\ \sum_{m_1+\cdots+m_b=n\atop m_i\ge1}
\frac{n!}{m_1!\cdots m_b!}z^{\,2^{b-1}\prod_iF_{m_i}-1}.
\]
In particular, for \(n\ge2\), the one-block identity is the unique universal graph vertex.

**Higher commutativity and clique numbers.** For each integer \(r\ge1\), let \(T_{n,r}\) count *ordered* \(r\)-tuples, repetitions allowed, of pairwise commuting elements of \(B_n\). Then
\[
T_{n,r}=\sum_{b=1}^n b!\left\{\begin{smallmatrix}n\\b\end{smallmatrix}\right\}(2^r-1)^{b-1},
\qquad \sum_{n\ge1}T_{n,r}\frac{x^n}{n!}=\frac{e^x-1}{1-(2^r-1)(e^x-1)}.
\]
If \(c_{n,k}\) is the number of unordered commuting cliques with exactly \(k\) distinct faces, then
\[
c_{n,k}=\frac1{k!}\sum_{j=1}^k s(k,j)\,T_{n,j},
\]
where \(s(k,j)\) are signed Stirling numbers of the first kind. In particular \(c_{n,k}=0\) for \(k>2^{n-1}\), and \(c_{n,2^{n-1}}=n!\) for \(n\ge2\). For each fixed \(r\ge1\), with \(u_r=2^r-1\) and \(\rho_r=\log(1+1/u_r)\),
\[
T_{n,r}\sim\frac{n!}{u_r(u_r+1)\rho_r^{n+1}}\qquad(n\to\infty).
\]
The numerical formula for \(r=2\), including its asymptotic, already appears as OEIS A050352, and the variable-parameter ordered-tree formula there gives the same numerical sequence for every fixed \(r\). Those *numerical identities in isolation* are explicitly not claimed as new; the assertion here is their common interpretation in the full braid-face commuting graph, together with the explicit centralizers, all maximal cliques, the exact clique overlap spectrum, and the complete clique counts.

## Assumptions and scope

An ordered partition is a sequence \(\alpha=(A_1,\ldots,A_b)\) of pairwise disjoint nonempty subsets with union \([n]\). Its product with \(\beta=(B_1,\ldots,B_c)\) is the ordered sequence of all nonempty intersections \(A_i\cap B_j\), sorted first by \(i\) and then by \(j\). There are no field assumptions. A consecutive-block coarsening of \(\sigma=(\sigma(1),\ldots,\sigma(n))\) is obtained by choosing which of the \(n-1\) gaps remain separators, and then treating each resulting consecutive segment as one *unordered* block. The graph always includes all faces, including the identity. The case \(n=1\) consists of one vertex and satisfies the formulas with \(d=0\).

## Proof

**1. Commutation is compatibility of weak orders.** Encode each ordered partition by signs \(\varepsilon_{ij}\in\{-1,0,+1\}\), expressing whether the coordinates indexed by \(i,j\) are strictly ordered or tied. In the Tits product, each coordinate sign is taken from the left factor unless it is zero, in which case it is taken from the right. This follows directly from the nonempty-intersections definition: nonzero first-factor inequalities persist, while ties in the first factor are resolved by the second.

It follows that \(\alpha\beta=\beta\alpha\) if and only if no pair \(i,j\) receives *opposite nonzero* signs in \(\alpha\) and \(\beta\). In this case the common product refines both ordered partitions, and each pairwise relation is their common nonzero sign, if any. More generally, if \(\alpha_1,\ldots,\alpha_r\) commute pairwise, the common product \(\gamma=\alpha_1\cdots\alpha_r\) is independent of factor order and refines every \(\alpha_i\). Conversely, any family of coarsenings of a common face consists of pairwise commuting elements: their nonzero pair signs are all compatible. Every face has a chamber (total-order) refinement by ordering the points within each block. Thus every commuting family is contained in \(\mathcal C_\sigma\) for at least one \(\sigma\).

**2. Maximal cliques and their overlaps.** A chamber has singleton blocks and is a left zero. A face commuting with a chamber \(\sigma\) must have no reversed comparison relative to \(\sigma\), hence its blocks are consecutive segments of \(\sigma\). Therefore the graph-neighborhood of \(\sigma\), including \(\sigma\), is precisely \(\mathcal C_\sigma\). This set is a clique of size \(2^{n-1}\). Because every clique extends to a chamber, it is maximal; distinct chambers yield distinct maximal cliques (each contains precisely its own chamber). A common coarsening of \(\sigma,\tau\) can retain exactly those cuts \(j\) whose first-\(j\)-letter subsets coincide, so there are \(2^{d(\sigma,\tau)}\) of them. Relabel positions according to \(\sigma\), making \(\sigma\) the identity. Shared prefix sets then mark the unique direct-sum decomposition of the new permutation into indecomposable components. Counting each indecomposable block independently gives the stated \(N_{n,k}\). The recurrence for \(a_m\) partitions permutations by their first direct-sum component length.

**3. Centralizers.** Fix \(\alpha=(A_1,\ldots,A_b)\). For a commuting \(\beta\), restrict the weak order of \(\beta\) to each \(A_i\); these restrictions are arbitrary ordered partitions \(\beta_i\) of \(A_i\). Compatibility with the strict \(A_i<A_j\) comparisons forces the \(\beta_i\)-blocks to appear in order of \(i\), with one possibility of equality across each adjacent boundary: either the last block of \(\beta_i\) is strictly before the first block of \(\beta_{i+1}\), or those two blocks are merged. No other interleaving or merging is possible because it would reverse an \(\alpha\)-comparison. Conversely, arbitrarily choosing each \(\beta_i\) and each of these \(b-1\) binary merge decisions produces exactly one commuting \(\beta\). Restriction recovers all \(\beta_i\) and the merge decisions, so the construction is bijective. This proves \(2^{b-1}\prod_iF_{|A_i|}\). Grouping by compositions of block cardinalities gives \(D_n(z)\). For \(n\ge2\), the indiscrete identity alone commutes with every chamber, proving uniqueness of the universal vertex.

**4. Higher tuples and the clique polynomial.** Fix the common product \(\gamma\) of an ordered commuting tuple; suppose \(\gamma\) has \(b\) blocks. Each tuple entry must be a coarsening of \(\gamma\), represented by a subset of the \(b-1\) cuts. The common product equals \(\gamma\) precisely when every one of these cuts occurs in at least one of the \(r\) entries. Thus each cut is independently marked by a nonempty subset of \([r]\), giving \((2^r-1)^{b-1}\) tuples per fixed \(\gamma\). There are \(b!\left\{\begin{smallmatrix}n\\b\end{smallmatrix}\right\}\) ordered partitions with \(b\) blocks. Summing proves the formula. The Stirling EGF \(\sum_n b!\left\{\begin{smallmatrix}n\\b\end{smallmatrix}\right\}x^n/n!=(e^x-1)^b\) yields the rational-exponential generating function.

A tuple with exactly \(k\) distinct entries arises by choosing an unordered commuting clique of size \(k\) and then a surjection of its \(r\) labeled positions onto its \(k\) faces. Hence \(T_{n,r}=\sum_{k=1}^{r} k!\left\{\begin{smallmatrix}r\\k\end{smallmatrix}\right\}c_{n,k}\). Standard Stirling inversion yields the claimed formula for \(c_{n,k}\). In the displayed EGF, the simple pole of smallest modulus lies at \(\rho_r=\log(1+1/u_r)\); its other poles are \(\rho_r+2\pi i j\), for nonzero integers \(j\), and so are strictly farther from the origin. Expansion at \(\rho_r\) has singular part \(1/[u_r(u_r+1)(\rho_r-x)]\). Singularity transfer proves the stated asymptotic for fixed \(r\).

## Verification

Run `python verify_braid.py` with Python 3 and no external packages. The independent checker constructs every ordered partition via surjective coordinate labels and multiplies directly by the nonempty-intersection rule. It checks all commuting-pair counts and *every* centralizer for \(1\le n\le5\); all commuting triples and quadruples and all unordered clique cardinalities for \(1\le n\le3\); all chamber cliques, adjacency compatibility, and maximal-clique intersections for \(1\le n\le4\); and the indecomposable permutation overlap distribution for \(1\le n\le7\). It performs 163882 direct comparison/structural checks and reports `VERIFY_OK`. The finite checks are not used as a substitute for the unrestricted proof.

## Relationship to prior work

Carson–Dolinka–East–Gould–Zenab (first public arXiv date 2022-04-29; primary MSC 20M10) develops broad semigroup product, restriction and embedding theory, not the numerical or graph-level classification here. Commins (first public 2024-03-31), especially §2.1 and Theorem 1.2, explicitly supplies the same braid-face monoid and its multiplication but investigates the associated face algebra as a simultaneous symmetric-group/descent-algebra representation, not centralizers or commuting-graph cliques. Brauner–Commins–Reiner study the free left-regular band, an injective-word semigroup distinct from this monoid. The simple numeric sequence \(T_{n,2}\) is A050352, and its published variable-height rooted-tree formula already yields the numeric formula for all fixed \(r\) by the substitution \(m=2^r\). Therefore novelty of the bare enumerator or its singularity asymptotic is *not* asserted. The claimed refinement is the complete semigroup commutation mechanism, centralizer distribution and maximal-clique geometry with a permutation-factorization overlap profile.

## Limitations

This result applies to the braid-arrangement face monoid \(B_n\), not all Coxeter face monoids. Its graph includes the identity, so it is not the sometimes-used commuting graph obtained by deleting central elements. It does not classify isomorphism types of arbitrary graphs or the face algebra's linear commutant. The numerical higher-commutativity sequence is already covered in an unrelated tree-counting guise; the independent scientific claim is structural. A theorem in the broad literature on left-regular bands or compatibility graphs may imply parts of this package, and publication priority beyond the inspected sources is not established. No independent external mathematical audit has been performed.

## References

1. S. Carson, I. Dolinka, J. East, V. Gould, R. Zenab, *Product decompositions of semigroups induced by action pairs*, arXiv:2204.13833 (first posted 2022-04-29), especially abstract, §§2 and 5.7. https://arxiv.org/abs/2204.13833
2. P. Commins, *Invariant theory for the face algebra of the braid arrangement*, arXiv:2404.00536 (first posted 2024-03-31), especially §2.1 and Theorem 1.2. https://arxiv.org/abs/2404.00536
3. S. Brauner, P. Commins, V. Reiner, *Invariant theory for the free left-regular band and a q-analogue*, arXiv:2206.11406 (2022), abstract and initial definitions. https://arxiv.org/abs/2206.11406
4. OEIS Foundation, *A050352: Number of 4-level labeled linear rooted trees with n leaves*, entries and formulas recorded 2003–2014. https://oeis.org/A050352
