# Zero forcing sets of fully whiskered complete graphs
## Finding
For every integer \(n\ge2\), let \(W_n=K_n\odot K_1\) be the graph obtained from a clique with vertices \(c_1,\ldots,c_n\) by adjoining a pendant leaf \(l_i\) to each \(c_i\). For \(S\subseteq V(W_n)\), call \(\{c_i,l_i\}\) an *empty pair* when neither vertex is in \(S\).

Then \(S\) is a zero forcing set if and only if one of the following holds:

1. no pair is empty; or
2. exactly one pair is empty and \(S\) contains at least one leaf.

Therefore the complete cardinality enumerator is
\[
\mathcal Z(W_n;x)=(2x+x^2)^n+n\big((2x+x^2)^{n-1}-x^{n-1}\big).
\]
In particular,
\[
Z(W_n)=n-1,
\qquad
z(W_n;n-1)=n(2^{n-1}-1),
\]
and the total number of zero forcing sets is
\[
\mathcal Z(W_n;1)=(n+3)3^{n-1}-n.
\]
Every minimum zero forcing set is obtained by choosing one empty pair, selecting exactly one vertex from every other core-leaf pair, and excluding the all-core choice on those remaining pairs.

## Assumptions and scope
Graphs are finite, simple, and undirected. Zero forcing uses the standard color-change rule: a black vertex with exactly one white neighbor forces that neighbor black. The theorem concerns the ordinary zero forcing process, not skew, positive semidefinite, or other variants. The domain is every integer \(n\ge2\); the case \(n=1\) is excluded because \(K_1\odot K_1\cong K_2\) has a separate degenerate pair structure.

## Proof
Fix \(n\ge2\) and an initial black set \(S\).

First suppose that at least two pairs, say \(\{c_i,l_i\}\) and \(\{c_j,l_j\}\), are empty. Any initially black leaf can force only its own core, so perform all such available leaf-to-core forces. Afterward, both \(c_i\) and \(c_j\) are still white. Every black core is adjacent to both of these white core vertices and therefore has at least two white neighbors. A leaf belonging to an empty pair is white and has a white core neighbor, while every black leaf has a black core neighbor and cannot force anything further. Thus the process stalls. Hence a zero forcing set has at most one empty pair.

Now suppose there is exactly one empty pair \(\{c_i,l_i\}\) and no leaf belongs to \(S\). Then every other pair is in the core-only state: \(c_j\) is black and \(l_j\) is white for \(j\ne i\). Each black core \(c_j\) has two white neighbors, namely \(c_i\) and \(l_j\), so no first force exists. Such an \(S\) is not zero forcing.

Conversely, suppose exactly one pair \(\{c_i,l_i\}\) is empty and some leaf \(l_j\) is black. First, every black leaf in a leaf-only pair forces its core. At that point every core except \(c_i\) is black. The chosen index \(j\) has both \(l_j\) and \(c_j\) black, so \(c_j\) has \(c_i\) as its unique white neighbor and forces \(c_i\). Then \(c_i\) forces \(l_i\). Finally, any remaining white pendant leaf is the unique white neighbor of its black core and is forced. Thus \(S\) is zero forcing.

Finally, suppose no pair is empty. Every leaf-only pair first forces its core, after which all core vertices are black. Each still-white leaf then is the unique white neighbor of its core and can be forced. Thus every set with no empty pair is zero forcing. This proves the characterization.

For the polynomial, a nonempty pair has three possible states: core-only of weight \(x\), leaf-only of weight \(x\), and both selected of weight \(x^2\). Hence sets with no empty pair contribute \((2x+x^2)^n\). With exactly one empty pair, there are \(n\) choices for that pair, and the remaining \(n-1\) pairs contribute \((2x+x^2)^{n-1}\), except that the all-core choice \(x^{n-1}\) is forbidden. This gives the displayed formula.

The smallest possible degree is \(n-1\), arising only from the one-empty-pair term. For each choice of the empty pair there are \(2^{n-1}\) ways to select one vertex from each remaining pair, and precisely one is the forbidden all-core choice. Therefore there are \(n(2^{n-1}-1)\) minimum sets. Substituting \(x=1\) gives the total count \((n+3)3^{n-1}-n\).

## Verification
The proof above is valid for every \(n\ge2\). As a finite corroboration, `artifacts/verify.py` independently constructs \(W_n\), simulates the standard zero forcing rule for every initial subset, and compares the result with the stated empty-pair criterion and polynomial.

For \(2\le n\le8\), all \(87376\) subsets were checked. The exact replay output is:

`VERIFY_OK n_range=2..8 subset_checks=87376 criterion_checks=87376 coefficient_checks=77 minimum_checks=21 max_order=16`

The finite computation is not used as an infinite proof.

## Relationship to prior work
The foundational paper on zero forcing introduced \(Z(G)\) and already treated corona graphs at the level of a general upper bound; it also gives the specific example \(C_5\circ K_1\), the penta-sun, with zero forcing number \(3\). That does not determine the fully whiskered clique family or enumerate its forcing sets.

Javaid, Irshad, Batool, and Raza studied zero forcing numbers of corona products. Their main connected-corona lemma and recurrence explicitly assume the attached graph has order at least two. Their treatment of the singleton attachment \(K_1\) is instead a special theorem for a class of trees; it does not apply to \(K_n\) for \(n\ge3\). Their later disconnected-factor theorem also omits the case of exactly one isolated attached vertex. Thus the singleton-corona boundary relevant here is not supplied by those results.

Boyer et al. introduced the zero forcing polynomial and derived it for several graph families. The inspected full text contains no occurrence of “corona”, “whisker”, “rooted”, or “pendant”, and no theorem there specializes to the present graph family. The result here therefore refines the older scalar/corona literature by giving an if-and-only-if classification of every forcing set, all coefficients, and all minimum bases for \(K_n\odot K_1\).

## Limitations
The theorem is specific to a complete core with one pendant leaf attached at every core vertex. It does not claim a formula for \(G\odot K_1\) for arbitrary \(G\), for iterated coronas, or for other forcing variants. The exhaustive computation through order \(16\) corroborates the proof but does not establish the infinite statement. Poorly indexed literature using uncommon terminology for fully whiskered cliques remains a residual originality risk.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. Publicly available online 2007-11-26.
2. I. Javaid, M. Irshad, A. Batool, and M. Raza, “On the zero forcing number of corona and lexicographic product of graphs,” arXiv:1607.04071v1, 2016-07-14.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1; *Discrete Applied Mathematics* 258 (2019), 35–48.
