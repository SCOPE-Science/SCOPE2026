# Exact bounded-morphism census between finite crown Kripke frames

## Finding
Let \(\mathfrak C_r\), for every integer \(r\ge2\), be the \(2r\)-point reflexive crown order with minimal points \(a_i\), maximal points \(b_i\), and strict relations \(a_i<b_i\) and \(a_i<b_{i-1}\), with indices modulo \(r\). Let \(N(n,m)\) be the number of globally onto bounded morphisms \(\mathfrak C_n\to\mathfrak C_m\), where \(n,m\ge2\) and the points in both crowns are individually indexed. Then, for \(m\ge3\),
\[
N(n,m)=\sum_{S\subseteq E(C_m)}(-1)^{m-|S|}\operatorname{tr}\bigl((I_m+A_S)^n\bigr),
\]
where \(C_m\) is the ordinary cycle on the \(m\) target maximal points and \(A_S\) is the adjacency matrix of the spanning subgraph with edge set \(S\). These morphisms correspond bijectively to cyclic lazy walks of length \(n\) on \(C_m\) that traverse every edge at least once. In particular, \(N(n,m)=0\) for \(n<m\), \(N(m,m)=2m\), and, for \(m\le n<2m\),
\[
N(n,m)=2m[z^m](z^{-1}+1+z)^n.
\]
The first zero-winding edge-covering walks appear at \(n=2m\), precisely \(2m^2\) of them, yielding
\[
N(2m,m)=2m\bigl([z^m](z^{-1}+1+z)^{2m}+1\bigr)+2m^2.
\]
At the exceptional four-point target \(m=2\), the exact count is
\[
N(n,2)=3^n+(-1)^n-2^{n+1}+2 \qquad(n\ge2).
\]
Thus, for every \(m\ge2\), an onto bounded morphism \(\mathfrak C_n\to\mathfrak C_m\) exists exactly when \(n\ge m\).

## Assumptions and scope
A bounded morphism (also called a modal \(p\)-morphism) between reflexive Kripke frames is a function \(f\) satisfying \(f(\uparrow x)=\uparrow f(x)\) for every source point \(x\). This equality includes both forward order preservation and the back-lifting property. The word *onto* additionally requires surjectivity of \(f\) on every target point. This work counts actual indexed functions, not maps modulo crown automorphisms and not mere continuous maps or homotopy classes. Loops in the Kripke frames are supplied by reflexivity; an ordinary lazy walk permits the stationary step, and the matrices have identity diagonals. For \(m=3\), the ordinary three-cycle has three distinct edges; for \(m=2\), the target is \(K_{2,2}\) as a height-two poset and is treated separately because its two minimal points have the same upper pair.

## Proof
**1. Normal form for targets with at least three maximal points.** A source maximum \(b_i\) has a singleton principal upset. The back-lifting equality forces its image to be a target maximum, denoted \(b_{v_i}\) with \(v_i\in\mathbb Z/m\mathbb Z\). Since the principal upset of each source minimum \(a_i\) consists of precisely \(a_i,b_{i-1},b_i\), two possibilities remain. If \(v_{i-1}=v_i\), the image of \(a_i\) must be that same target maximum, since the image principal upset is a singleton. If \(v_{i-1}\ne v_i\), the target image of \(a_i\) must be a target minimum with exactly these two upper maxima; such a minimum exists if and only if \(v_{i-1}\) and \(v_i\) are adjacent in \(C_m\), and it is unique for \(m\ge3\). Conversely, every cyclic sequence \(v_0,\ldots,v_{n-1}\) with differences in \(\{-1,0,+1\}\) modulo \(m\) gives the unique map described, and it satisfies the bounded-morphism equation pointwise. Every target minimum is hit exactly when the corresponding target edge is traversed. Traversing all target edges also visits every target maximum, so this is equivalent to global surjectivity.

**2. Exact enumeration.** Let \(E(C_m)\) be the set of its \(m\) distinct undirected edges. For each \(S\subseteq E(C_m)\), the trace \(\operatorname{tr}((I_m+A_S)^n)\) counts all indexed cyclic lazy walks using only edges of \(S\). Inclusion–exclusion over the edges not used counts walks using every edge, giving the first formula. For \(n<m\), a walk has fewer than \(m\) steps and cannot traverse all \(m\) edges. For \(n=m\), it must follow the full target circuit without pauses or reversals, in either direction from any of the \(m\) labeled starting points, giving \(2m\) maps.

**3. Winding threshold.** Lift each step of a cyclic lazy walk to \(\delta_i\in\{-1,0,1\}\) in the infinite integer cover of \(C_m\). Because the walk closes modulo \(m\), its total displacement is \(km\) for an integer winding number \(k\). If \(k\ne0\), the lifted path crosses a full block of \(m\) consecutive integer edges and hence uses every target edge. If \(k=0\), the finite lifted path is a closed integer walk, and it uses every target edge if and only if its maximum minus its minimum is at least \(m\): the visited interval of lifted edges projects onto all target edge classes precisely at that threshold. Indeed, any interval of \(m-1\) or fewer distinct integer edges misses an edge residue, and an interval of at least \(m\) covers them all.

When \(m\le n<2m\), an edge-covering walk cannot have winding zero: spanning an integer interval of width \(m\) and returning requires at least \(2m\) nonstationary steps. Also \(|k|\le\lfloor n/m\rfloor=1\), so precisely the two nonzero windings remain. For each of the \(m\) starting vertices, the number of increment words summing to \(+m\) equals \([z^m](z^{-1}+1+z)^n\), and the negative winding count is the same, proving the short-length coefficient formula. At \(n=2m\) there are also winding \(k=\pm2\) words, each comprising all \(+1\) or all \(-1\), giving another \(2m\) walks. Every zero-winding edge-covering walk of length \(2m\) has exactly \(m\) consecutive positive increments and \(m\) consecutive negative increments, cyclically (no zeros or extra reversal). There are exactly \(2m\) distinct indexed increment words (all rotations of the word with \(m\) pluses followed by \(m\) minuses), and \(m\) possible initial vertices, giving \(2m^2\). Combining the \(\pm1\), \(\pm2\), and zero winding cases yields the stated formula.

**4. Four-point target.** In \(\mathfrak C_2\), both minimal points lie under the same two distinct target maxima. The images of the source maxima therefore form an arbitrary binary cyclic word \(v_0,\ldots,v_{n-1}\). If adjacent entries agree, the corresponding source minimum must map to that common maximal point. If they differ, its image may be either of the two target minima, independently of all other positions. Let \(q\) be the number of changes in the binary cyclic word; it is even. Global surjectivity holds precisely when these \(q\) minima choices include both target minima, giving \(2^q-2\) options. There are \(2\binom nq\) indexed cyclic binary words with exactly \(q\) changes. Thus
\[
N(n,2)=2\sum_{\substack{2\le q\le n\\q\ \mathrm{even}}}\binom nq(2^q-2).
\]
The even-part binomial identity gives \(2\sum_{q\text{ even}}\binom nq2^q=3^n+(-1)^n\). Subtract the \(q=0\) term and twice the corresponding even binomial sum, obtaining \(3^n+(-1)^n-2^{n+1}+2\). This is positive for every \(n\ge2\); together with step 2 it gives the claimed existence criterion for all targets.

## Verification
The attached dependency-free Python script `artifacts/verify_crowns.py` independently checks the defining bounded-morphism equation \(f(\uparrow x)=\uparrow f(x)\) by enumerating entire functions for 10 small instances, rather than assuming the lazy-walk correspondence. It also compares inclusion–exclusion matrix counts against direct lazy-walk enumeration for 27 parameter pairs, checks 11 special-target binomial identities, and verifies the coefficient and first zero-winding formulas. Execute with `python3 artifacts/verify_crowns.py` from the extracted artifact directory. The full successful output is in `artifacts/verify_output.txt`. These finite checks corroborate but do not establish the all-parameter theorem.

## Relationship to prior work
Finite reflexive posets are the specialization-preorder models of finite \(T_0\)-spaces; see Barmak–Minian. Čukić–Kozlov classify graph-homomorphism complexes for ordinary cycles, and Georgiadis–Callan–Hou count certain edge-moving circular walks that visit all *vertices*. Neither framework imposes the modal back-lifting equation, and neither reported theorem counts edge-covering *lazy closed walks* arising from globally onto crown bounded morphisms. Farley's earlier enumeration of all order-preserving maps between fences and crowns is especially relevant; counting unrestricted monotone maps does not by itself identify the back-lifting constrained onto subfamily, although its inaccessible full text leaves a specialized-coverage risk.

An existing analysis of homotopy classes between finite crowns (published comparison record, identifier `2026/10/4/SCOPE-divisibility-controls-homotopy-classes-between-finite-crown-circ--706147a4828e`) establishes winding-based **homotopy classes** of all monotone maps; it also contains the full-winding \(n=m\) maps. The present theorem concerns an incomparable equivalence relation—indexed globally onto bounded morphisms—with an edge-surjectivity criterion and exact cardinality for all \(n,m\), including the exceptional \(m=2\) family and the first zero-winding threshold. Therefore, the boundary value \(2m\) alone is not presented as a novel standalone theorem. A second analysis of crown maps to complete height-two spaces (identifier `2026/10/4/SCOPE-necklace-classification-of-maps-from-finite-crowns-to-complete-h--09e0671f38c4`) counts homotopy classes for different targets, not globally onto bounded morphisms.

## Limitations
The theorem treats finite indexed crowns only, and does not enumerate morphisms modulo automorphisms, arbitrary Kripke frames, or the homotopy classes of underlying continuous maps. Only the displayed short-length cases and general matrix formula are provided; no closed elementary expression for every \(m,n\) is claimed. The checked computations cover bounded finite examples, not the infinite proof. Farley's full text was not accessible and remains a specific literature-priority risk. No independent validation or publication-priority certification has been performed.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156 (first public 2006-11-06).
2. S. L. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015 (first public 2004-08-02).
3. A. Georgiadis, D. Callan and H. Hou, *Circular Digraph Walks, k-Balanced Strings, Lattice Paths and Chebychev Polynomials*, Electron. J. Combin. 15 (2008), DOI:10.37236/832.
4. J. D. Farley, *The number of order-preserving maps between fences and crowns*, Order 12 (1995), 5–44, DOI:10.1007/BF01108588.
