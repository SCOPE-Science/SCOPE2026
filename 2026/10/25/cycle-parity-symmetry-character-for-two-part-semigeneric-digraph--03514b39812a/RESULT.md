# Cycle-parity symmetry character for two-part semigeneric digraphs
## Finding
Let \(a,b\ge1\), and let \(\mathcal S_{a,b}\) consist of all orientations of the complete bipartite graph on labelled sides \(A=[a]\), \(B=[b]\) satisfying the **semigeneric rectangle parity law**: for every two distinct vertices on either side, the four cross-orientations have even binary sum. Code an edge by \(X_{ij}=1\) when the vertex in \(A\) points toward the vertex in \(B\). Let \(c(\pi)\) count the cycles of a permutation, and write \(\varepsilon(\pi)=1\) if **every** cycle has even length, and zero otherwise.

**Theorem (complete finite symmetry character).** For every \((\sigma,\tau)\in S_a\times S_b\), acting by separately permuting the two sides, the number of invariant semigeneric orientations is
\[
\boxed{\operatorname{Fix}_{a,b}(\sigma,\tau)=2^{c(\sigma)+c(\tau)-1}\bigl(1+\varepsilon(\sigma)\varepsilon(\tau)\bigr).}
\]
When \(a=b=n\), allow permutations \(g\) exchanging the sides, specified by bijections \(g(a_i)=b_{\sigma(i)}\) and \(g(b_j)=a_{\tau(j)}\). Writing \(\theta=\tau\circ\sigma\in S_n\), then
\[
\boxed{\operatorname{Fix}^{\mathrm{swap}}_n(\sigma,\tau)=\begin{cases}2^{c(\theta)},&\text{every cycle of }\theta\text{ has even length},\\0,&\text{otherwise}.\end{cases}}
\]
In particular, a prescribed side-swapping permutation preserves **some** semigeneric orientation precisely when each cycle of its square on one side has even length. This cycle-parity obstruction is sharp.

The exact number of isomorphism classes of these orientations with the two sides distinguished is
\[
\boxed{U_{a,b}=\frac{(a+1)(b+1)+\mathbf1_{2\mid a}\mathbf1_{2\mid b}}{2}.}
\]
When the sides have equal size \(n\) and interchanging them is also allowed, the number of (unlabelled) digraph isomorphism classes is
\[
\boxed{V_n=\frac{(n+1)^2+3\mathbf1_{2\mid n}}4.}
\]
The formulas include singleton sides. For example, \(U_{2,2}=5\), whereas \(V_2=3\). The labelled family has \(2^{a+b-1}\) members, yet only quadratically many isomorphism classes when the part sizes grow together.

## Assumptions and scope
These are finite digraphs in the age of the countable semigeneric homogeneous directed graph, not arbitrary bipartite orientations. Each distinct cross-pair supports exactly one oriented edge, and no edges occur inside a side. The two nonadjacency classes are precisely the sides. All permutations in the fixed-point formulas act on the **labelled** vertex set; isomorphism counts quotient by side-preserving relabellings or, in the balanced case, by every graph isomorphism including side exchange. The indicator \(\mathbf1_{2\mid m}\) equals one for positive even \(m\) and zero for odd \(m\).

## Proof
**1. Rank-one parity representation.** For a binary matrix \(X\) the four-entry parity law is equivalent to the existence of vectors \(r\in\mathbb F_2^a\) and \(s\in\mathbb F_2^b\) such that \(X_{ij}=r_i+s_j\) modulo two. Indeed, fix a first row and column, set \(r_i=X_{i1}\) and \(s_j=X_{1j}+X_{11}\), and use the \(2\times2\) parity condition for rows \(1,i\) and columns \(1,j\). The representation has precisely two preimages: simultaneously complementing \(r\) and \(s\) changes no entry. Thus \(|\mathcal S_{a,b}|=2^{a+b-1}\), even when a side is a singleton.

**2. Permutations preserving each side.** The condition \(X_{ij}=X_{\sigma(i),\tau(j)}\) is equivalent to
\[
 r_i+r_{\sigma(i)}=s_j+s_{\tau(j)}=d\in\mathbb F_2
\]
for all \(i,j\). If \(d=0\), each vector is constant on the cycles of its respective permutation, allowing \(2^{c(\sigma)+c(\tau)}\) representations. If \(d=1\), every permutation cycle must be even, in which case there are the same number of representations, with entries alternating along each cycle. The two values of \(d\) are disjoint. Dividing by the twofold representation symmetry proves the first formula.

**3. Permutations exchanging the sides.** Assume \(a=b=n\). Under a side exchange, the order of endpoints reverses, so invariance means
\[
 X_{ij}=1-X_{\tau(j),\sigma(i)}.
\]
Writing \(X_{ij}=r_i+s_j\), this forces \(r_i+s_{\sigma(i)}=d\) and \(r_{\tau(j)}+s_j=1+d\) for a common \(d\in\mathbb F_2\). Eliminating \(s\) yields
\[
 r_{\theta(i)}=r_i+1,\qquad \theta=\tau\circ\sigma.
\]
Such a binary vector exists exactly when all \(\theta\)-cycles have even length, and then has two choices per cycle. The value of \(d\) has two choices and determines \(s\), while simultaneous vector complementation identifies each pair of representations. This proves the second formula and its necessity and sufficiency.

**4. Exact isomorphism classes.** Under independent row and column permutations, a representation is determined by the weights \(p=|\{i:r_i=1\}|\) and \(q=|\{j:s_j=1\}|\), with \(0\le p\le a\), \(0\le q\le b\). The twofold representation ambiguity identifies \((p,q)\) with \((a-p,b-q)\). This involution on the \((a+1)(b+1)\) weight pairs has one fixed point exactly when \(a,b\) are both even. Burnside's lemma gives \(U_{a,b}\).

When \(a=b=n\), a side exchange sends \(X\) to \(1-X^\mathsf T\), or \((p,q)\mapsto(n-q,p)\). This map has order four on weight pairs; its square is the complement involution. Its identity has \((n+1)^2\) fixed pairs, while each of its other three powers fixes exactly one pair if \(n\) is even and none otherwise. Burnside gives \(V_n\). Since the sides are precisely the maximal independent classes of the underlying complete bipartite graph, no additional graph isomorphisms are omitted.

## Verification
The accompanying standalone Python program directly enumerates every binary orientation matrix satisfying all \(2\times2\) parity constraints for the tested side sizes. It then computes fixed-point counts for every separate-side permutation and, in balanced cases, every side-swapping permutation, without using either character formula to generate matrices. It also independently applies Burnside's lemma and checks both orbit formulas. Tests cover side sizes \((1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4)\), 288 permutation-character comparisons, and the associated orbit counts. Its expected terminal output is `ALL_TESTS_PASS 288`. The proof, not the finite testing, establishes the unrestricted formulas.

## Relationship to prior work
Jasiński, Laflamme, Nguyen Van Thé, and Woodrow (arXiv:1310.6466, Section 10) give the semigeneric parity class and its role in a Ramsey precompact expansion. Coskey and Ellis (arXiv:1509.04222, Section 4, Lemma 4.1) prove the two-antichain binary factorization; this is the **known premise**, not the novelty claimed here. The public mathematical note *Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph* supplies the global labelled tuple-orbit count by parity-block partitions, again using that known factorization. The public result on side-preserving reducts of the random bipartite graph classifies orbits of arbitrary binary matrices under row/column **bit-switch translations**, not fixed semigeneric parity matrices under **row/column permutations and side exchange**. Neither result states the fixed-point character or the sharp side-swap cycle obstruction shown here.

The contribution is the complete permutation character of the two-part semigeneric age and its isomorphism-class census, including the exceptional parity obstruction under exchanges of the two nonadjacency classes. The character remains a direct elementary consequence of the classical two-antichain representation, and a specialized unpublished classification of its finite symmetries is possible.

## Limitations
This theorem concerns precisely two nonempty nonadjacency classes and does not classify symmetries of semigeneric digraphs with three or more parts. The isomorphism formulas treat unweighted orientations, without distinguished vertices or external relations. The checked primary sources establish the parity representation and broader homogeneous setting, but do not constitute an exhaustive survey of all unpublished symmetry enumerations. Computational checks are finite corroboration only. No independent external review is claimed.

## References
1. J. Jasiński, C. Laflamme, L. Nguyen Van Thé, R. Woodrow, *Ramsey precompact expansions of homogeneous directed graphs*, arXiv:1310.6466 (first public version 2013-10-24), Section 10; later *Electronic Journal of Combinatorics* 21(4), P4.42 (2014).
2. S. Coskey, P. Ellis, *The conjugacy problem for automorphism groups of homogeneous digraphs*, arXiv:1509.04222 (first public version 2015-09-14), Section 4 and Lemma 4.1; later *Contributions to Discrete Mathematics* 12(1) (2017).
3. *Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph*, publicly indexed mathematical finding, identifier `5135d85e91a6` (2026).
4. *Exact ordered-tuple orbit profiles of the side-preserving random bipartite reducts*, publicly indexed mathematical finding, identifier `f8b9342567cf` (2026).
