# Rigidity and exact optimal-colouring enumerator for sub-quorum colourings of clique prisms

## Finding
Let \(R_n=K_2\square K_n\), with vertices \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where each of \(A,B\) induces a clique and the only edges between them are \(a_i b_i\). A sub-quorum colouring is a partial assignment of colours such that each coloured vertex has at least half its *coloured closed neighbourhood*, including itself, in its own colour. Write \(\psi_{\mathrm{sq}}\) for the maximum number of distinct colours.

**Theorem.** For every integer \(n\ge1\),
\[
\psi_{\mathrm{sq}}(R_n)=\begin{cases}
2,&n=1,2,\\
3,&n=3,\\
4,&n\ge4.
\end{cases}
\]
For every \(n\ge4\), a partial colouring achieves four distinct colours **if and only if** its two clique layers use disjoint pairs of colours, each of the two colours occupies the same positive number of vertices in its layer, and no matched pair \(a_i,b_i\) has both endpoints coloured. In particular, this is a complete classification of all four-colour optimizers, not merely an extremal construction.

For a fixed named palette of \(k\ge4\) colours, let \(F_n(k)\) count partial colourings of \(R_n\) that are sub-quorum colourings and use exactly four colours. Then for \(n\ge4\),
\[
F_n(k)=\frac{(k)_4}{4}\sum_{\substack{a,b\ge1\\2a+2b\le n}}
\frac{n!}{(a!)^2(b!)^2(n-2a-2b)!},
\qquad (k)_4=k(k-1)(k-2)(k-3).
\]
The identity extends to all \(n\ge0\) by setting \(F_n(k)=0\) for \(n<4\). Its exponential generating function is
\[
\sum_{n\ge0}F_n(k)\frac{z^n}{n!}
=\frac{(k)_4}{4}e^z\left(I_0(2z)-1\right)^2,
\]
where \(I_0(2z)=\sum_{j\ge0}z^{2j}/(j!)^2\) denotes the modified Bessel series. For example, \(F_4(4)=144\) and \(F_5(4)=720\).

## Assumptions and scope
All graphs are finite, simple, undirected and labelled by the displayed vertices. The matching \(a_i b_i\) is part of the graph definition. Uncoloured vertices are omitted when testing the local majority condition; the closed neighbourhood of a coloured vertex includes that vertex itself. Colours need not be proper and are not required at uncoloured vertices. A palette may contain unused colours; \(F_n(k)\) counts actual maps to that named palette using exactly four distinct names. The uniqueness statement is structural up to interchanging colours, not an assertion of a unique labelled colouring.

## Proof
For an arbitrary sub-quorum colouring, let \(a\) be the number of coloured vertices of the clique \(A\), and let \(u_c\) be the multiplicity of colour \(c\) within \(A\). For a coloured \(a_i\) of colour \(c\), let \(\delta_i=1\) when \(b_i\) is coloured and zero otherwise, and let \(\epsilon_i=1\) when \(b_i\) has colour \(c\) and zero otherwise. The condition at \(a_i\) is exactly
\[
2(u_c+\epsilon_i)\ge a+\delta_i. \tag{1}
\]
Indeed the coloured closed neighbourhood contains the \(a\) coloured vertices of \(A\) and possibly \(b_i\), of which \(u_c+\epsilon_i\) carry colour \(c\). The same equation, with \(A,B\) interchanged, applies to \(B\).

**Row-colour lemma.** No clique layer uses more than three colours. If it uses exactly three, it contains exactly three coloured vertices, of three different colours, and all three matched vertices in the other layer are coloured with their matching colours.

To prove the lemma, each colour occurring in \(A\) has multiplicity at least \(\lceil(a-1)/2\rceil\) by (1), because \(\epsilon_i\le\delta_i\le1\). If \(a\ge4\), three colours would need at least \(3\lceil(a-1)/2\rceil>a\) vertices. For \(a\le2\), three colours are impossible for cardinality reasons. Hence three colours force \(a=3\) and each multiplicity one. Substituting \(a=3,u_c=1\) in (1) shows that \(\delta_i=\epsilon_i=1\) for each of the three vertices, as claimed.

If three different colours appear in \(A\), then the lemma places their three matched same-coloured partners in \(B\). Thus \(B\) also contains at least three colours; the lemma makes its coloured support exactly those three matched vertices. Consequently the entire colouring has only three colours. Therefore a colouring with four or more colours must have at most two colours in each layer, and can have **at most four altogether**.

Suppose precisely four colours are used. Then each layer has exactly two colours, and the two layer palettes are disjoint. In \(A\), let their multiplicities be \(u,v\), so \(u+v=a\). Because no colour appears in both layers, \(\epsilon_i=0\) at every coloured vertex. Equation (1) gives \(2u\ge a\) and \(2v\ge a\). Since \(u+v=a\), equality must hold: \(a=2u=2v\), so the layer support is positive and even, and its two colour classes are balanced. Equality in (1) also forces \(\delta_i=0\) at every coloured vertex of \(A\). Thus no matched pair is coloured at both ends. The same argument holds for \(B\). Conversely any colouring with the stated structure has, at every coloured vertex, exactly half of its coloured closed neighbourhood in its own colour, so is admissible.

This classification implies that four colours exist if and only if \(n\ge4\): choose two differently coloured vertices in \(A\), two differently coloured vertices in \(B\), all at distinct matching indices. For \(n=3\), four colours are impossible; the three distinct singleton colours on \(a_1,a_2,b_3\) give three. For \(n=2\), the graph is the four-cycle and its sub-quorum number is two (alternatively, two differently coloured vertices in one layer attain two, while any third colour forces a matching neighbour across a two-coloured layer and breaks the local condition). For \(n=1\), the graph is a single edge and two different colours are allowed. This establishes the first formula.

To enumerate four-colour optimizers, choose ordered distinct names \((c_1,c_2,c_3,c_4)\) with the first two assigned to \(A\). For any positive integers \(a,b\) with \(2a+2b\le n\), distribute \(a,a,b,b\) distinct matching indices to those four names and leave the remaining \(n-2a-2b\) indices entirely uncoloured. The multinomial coefficient is \(n!/((a!)^2(b!)^2(n-2a-2b)!)\). Every resulting colouring is counted exactly four times, by independently swapping the two names within each layer. Dividing \((k)_4\) by four proves the finite sum. Finally, the exponential formula separates the uncoloured indices (factor \(e^z\)) from the four named colour classes (the two squared positive-even series), proving the generating function. All quantifiers and boundary cases are included.

## Verification
The standalone file `verify.py` directly constructs coloured closed neighbourhoods from the graph edges, checks the original weak-majority inequality rather than assuming the row-colour lemma, and enumerates all partial vertex partitions up to colour relabelling for \(1\le n\le5\). It reports maximum colour counts \(2,2,3,4,4\) and exactly \(6\) and \(30\) unlabelled four-colour optimizers at \(n=4,5\), agreeing with the formula. It also tests the four-colour construction for \(4\le n\le44\). Invoke `python3 verify.py` from this directory; only the Python standard library is needed. These finite experiments are supplementary, not a proof for arbitrary \(n\).

## Relationship to prior work
Ma, Sahbi and Zhang's *Sub-quorum colorings of graphs* (arXiv:2609.25128, first publicly posted 2026-09-20) develops the invariant, proves the universal \(\beta_2\) lower bound, a general degree upper bound, and exact evaluations for paths, cycles, complete and complete multipartite graphs, ladders, selected corona/join families, and hypercubes. The clique prism \(K_2\square K_n\) is neither the ordinary ladder \(P_2\square P_n\) nor a complete multipartite graph for \(n\ge3\), and its exact sub-quorum optimum and optimal-colouring enumerator are not implied by these stated results. In fact its degree is \(n\) and its order is \(2n\), so that work's general degree bound yields \(\psi_{\mathrm{sq}}(R_n)\le \lfloor2n^2/(2n-1)\rfloor\), growing linearly with \(n\), whereas the present exact bound is four. The small cases through \(n=4\) are consistent with that general bound and are not asserted to be independently novel numerical bounds. The novelty claimed is the unrestricted stable bound, complete rigidity and enumerator.

The 2013 foundational quorum-colouring paper introduced sub-quorum colouring as a question. Full comparison against all older alliance-colouring literature is not established. Published work on topological complexes of the same clique-prism graphs concerns different invariants and does not imply this colouring enumeration.

## Limitations
This finding concerns one specifically structured Cartesian-product family, not arbitrary rook graphs \(K_m\square K_n\) or general line graphs. It counts only optimal four-colour partial assignments for \(n\ge4\), not all sub-quorum colourings with fewer colours. The proof is mathematical; the executable verifies finitely many instances. The bibliographic search did not establish absolute priority, and the complete text of the newest revision of arXiv:2609.25128 was unavailable through the consulted access path; its publicly accessible revision abstract and the earlier complete online text were compared. Independent expert validation has not been performed.

## References
1. H. Ma, R. Sahbi and W. Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128 (first public version 2026-09-20; revised 2026-10-14), https://arxiv.org/abs/2609.25128 .
2. S. M. Hedetniemi, S. T. Hedetniemi, R. Laskar and H. M. Mulder, *Quorum colorings of graphs*, AKCE International Journal of Graphs and Combinatorics 10 (2013), 97–109, DOI: 10.1080/09728600.2013.12088727.
3. Published mathematical record, *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition* (used only to distinguish an unrelated topological result on the same graph family).
