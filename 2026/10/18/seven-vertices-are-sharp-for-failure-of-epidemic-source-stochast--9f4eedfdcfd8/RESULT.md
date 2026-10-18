# Seven vertices are sharp for failure of epidemic-source stochastic dominance on trees

## Finding

Let \(T=(V,E)\) be a finite undirected tree. Retain each edge independently with common probability \(p\in(0,1)\), and let \(X_v(p)\) be the number of vertices in the retained-edge component containing a specified source \(v\), including that source. Write \(Y\succeq_{\mathrm{st}} Z\) when \(\Pr(Y\ge k)\ge\Pr(Z\ge k)\) at every integer threshold \(k\).

**Sharp finite-source theorem.** For every tree on at most six vertices and every pair of sources \(u,v\), either \(X_u(p)\succeq_{\mathrm{st}} X_v(p)\) for **every** \(p\in(0,1)\), or the reverse holds for every such \(p\). In fact a single orientation works coefficientwise in the Bernstein expansion of all tail probabilities. Seven vertices are the smallest possible order at which two sources can have incomparable outbreak-size distributions; a seven-vertex example is incomparable for **every** \(p\in(0,1)\).

Label the vertices \(0,1,\ldots,6\) and take the three-arm tree with edges
\[
E=\{\{0,1\},\{1,2\},\{2,3\},\{0,4\},\{4,5\},\{0,6\}\}.
\]
Compare the source at vertex \(2\), two steps down the long arm, with the leaf at vertex \(6\). The complete tail-difference identities are
\[
\begin{aligned}
\Pr(X_2\ge2)-\Pr(X_6\ge2)&=p(1-p),\\
\Pr(X_2\ge3)-\Pr(X_6\ge3)&=0,\\
\Pr(X_2\ge4)-\Pr(X_6\ge4)&=-p^4(1-p),\\
\Pr(X_2\ge5)-\Pr(X_6\ge5)&=p^4(1-p)^2,\\
\Pr(X_2\ge6)-\Pr(X_6\ge6)&=p^5(1-p),\\
\Pr(X_2\ge7)-\Pr(X_6\ge7)&=0.
\end{aligned}
\]
Thus the source with the larger chance of any secondary infection has the **smaller chance of infecting a strict majority** (four or more of seven individuals); the larger and smaller tail comparisons persist for every interior transmissibility. Summing the tails gives the additional exact identity
\[
\mathbb E[X_2(p)]-\mathbb E[X_6(p)]=p(1-p)>0.
\]
Consequently even ordering sources by expected outbreak size can misrank their probability of a majority outbreak.

## Assumptions and scope

The graph is a finite, connected, simple, undirected **tree** with an explicitly fixed initial infected source. Every edge is independently open with the same probability \(p\). Infection reaches precisely the source's open component, as in independent undirected bond-transmission/Reed--Frost percolation. The theorem compares exact **final outbreak-size laws**; it assumes neither a uniformly random source nor a particular infection/recovery clock. The statement makes no assertion for networks with cycles, unequal transmission probabilities, or SIR models with correlated outgoing transmissions.

## Proof

**Exact tail coefficient identity.** For \(n=|V|\), write \(m=n-1\), and let \(\mathcal C_v(F)\) denote the connected component containing \(v\) when the open-edge set is \(F\subseteq E\). For every \(2\le k\le n\) and \(0\le j\le m\), define the nonnegative integer
\[
c_{v,k,j}=\#\{F\subseteq E:\ |F|=j,\ |\mathcal C_v(F)|\ge k\}.
\]
Independence of edges, with no approximations, gives
\[
\Pr(X_v(p)\ge k)=\sum_{j=0}^{m}c_{v,k,j}p^j(1-p)^{m-j}.
\tag{1}
\]
If all the integer differences \(c_{u,k,j}-c_{v,k,j}\) have one weak sign as \(k,j\) vary, the same weak tail comparison follows simultaneously for all \(p\in(0,1)\). This is sufficient for first-order stochastic order; no converse is assumed or required.

**Exhaustive small-order proof.** The classical Prüfer correspondence bijects labeled trees on \(\{0,\dots,n-1\}\), \(n\ge2\), with the \(n^{n-2}\) words of length \(n-2\) on those labels. The bundled standard-library-only `verify.py` constructs the tree for **every** such word for each \(n=2,3,4,5,6\), enumerates **every** of its \(2^{n-1}\) edge subsets, and computes \(c_{v,k,j}\) by connected-component search for every root, threshold, and edge count. It then compares every unordered source pair \(\{u,v\}\) and checks that all nonzero differences \(c_{u,k,j}-c_{v,k,j}\) have a common sign. A pair with all zero differences is permitted; any sign conflict makes the verifier fail.

The complete per-order labeled-tree counts are \(1,3,16,125,1296\); the source-pair counts are \(1,9,96,1250,19440\). The enumerator evaluates \(609408\) exact integer coefficient differences across \(20796\) source pairs and \(1441\) labeled trees. There are **zero** sign conflicts. Because the Prüfer map is a bijection and every edge subset, root pair, threshold and edge-count index is explicitly visited, this is an exhaustive finite proof of the required statement for every tree of order two through six. For a one-vertex tree there is only one source, so the claim is trivial. Equation (1) propagates this integer sign proof to the complete continuum \(p\in(0,1)\).

**Seven-vertex obstruction.** For the displayed tree, the same exact enumeration gives, for each \(k=2,3,\ldots,7\), the displayed polynomial tail differences. These polynomials can be checked without enumeration by the independent rooted-tree probability-generating recursion
\[
\Phi_{v\mid a}(z)=z\prod_{w\sim v,\ w\ne a}\left(1-p+p\Phi_{w\mid v}(z)\right),
\]
with a leaf branch equal to \(z\), and root distribution \(\Phi_{v\mid\varnothing}\). At \(p=1/2\), the exact probabilities for \(X_2=1,\ldots,7\) have numerators \((16,24,10,5,5,3,1)\) over \(64\); those for \(X_6\) have numerators \((32,8,8,8,5,2,1)\). The independent rooted recursion reproduces both arrays. Finally \(p(1-p)>0\) while \(-p^4(1-p)<0\) for all \(0<p<1\), proving failure of both possible stochastic-order directions for all such \(p\). The lower bound already established proves sharpness.

## Verification

Run `python3 verify.py > reproduced.json` using only Python's standard library. The deterministic output must match `certificate.json` byte for byte, including the \(1441\) labeled-tree count, \(20796\) source comparisons, \(609408\) integer coefficient comparisons, zero conflicting signs, the six exact polynomial-tail differences, and the independent \(p=1/2\) root-PGF computation. No floating-point tolerances, simulated epidemics, or interpolation are used.

The finite exhaustive calculation **is** the proof of the sharp small-order lower bound because its enumeration is complete for all orders covered. It makes no claim about universal stochastic comparability for larger trees, and the independent pointwise PGF test is a cross-check of the witness, not a substitute for the polynomial identity.

## Relationship to prior work

Kenah and Robins (2006 preprint; 2007 journal publication) rigorously distinguish independent bond-percolation predictions from general network SIR outbreak distributions when infectious periods are nondegenerate. Their analysis motivates the restricted independent-bond model here but does not classify the stochastic comparison of epidemic sources within a fixed finite tree. Holme (2017) investigates distinct notions of epidemic node importance for small graphs. Bucur and Holme (2019 preprint; 2020 journal publication) investigate estimating influence/mean outbreak sizes using network centralities. Those are complementary to, rather than implications of, the universal six-vertex stochastic-order comparison and the sharp seven-vertex majority-tail reversal proved here.

The lower-bound finite enumeration uses the classical Prüfer encoding of labeled trees, an established combinatorial bijection. The new claim is not that correspondence, not the general epidemic-percolation representation, and not an assertion that mean influence determines full outbreak distributions. A preexisting result in graph-reliability, rooted subtree-polynomial or stochastic graph-order terminology may establish equivalent coverage; independent literature review is not complete.

## Limitations

The result describes exact homogeneous independent edge outcomes on **trees**, not generic continuous-time SIR with shared random infectious periods. In particular, the high-mean/low-majority reversal is a rigorous within-model counterexample, not evidence that source degree always predicts outbreak risk. The sharp lower bound is confined to tree orders at most six; seven is the minimal failure order, not the sole order or unique tree at which failures occur. The polynomial identities do not quantify statistical estimation noise or detectability from finite sampled outbreaks.

## References

1. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057, first version 2006-10-30; *Physical Review E* **76**, 036113 (2007). DOI: 10.1103/PhysRevE.76.036113. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/.
2. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (2017).
3. D. Bucur and P. Holme, *Beyond ranking nodes: Predicting epidemic outbreak sizes by network centralities*, arXiv:1909.10021 (2019); *PLOS Computational Biology* **16**, e1008052 (2020). DOI: 10.1371/journal.pcbi.1008052.
4. E. W. Weisstein, *Labeled Tree*, MathWorld, https://mathworld.wolfram.com/LabeledTree.html (for classical Prüfer/tree counts).
