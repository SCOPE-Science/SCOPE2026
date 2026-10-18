# Dissociation faces and facets of complete bipartite graphs with a deleted matching

## Finding
Let \(G_{a,b,t}=K_{a,b}-M_t\), where \(a,b\ge3\), \(0\le t\le\min(a,b)\), and \(M_t\) is a matching of \(t\) deleted edges. A *dissociation set* \(S\) satisfies \(\Delta(G_{a,b,t}[S])\le1\). Put \(D_{a,b,t}(z)=\sum_{S\text{ dissociation}}z^{|S|}\) and \(M_{a,b,t}(z)=\sum_{S\text{ inclusion-maximal dissociation}}z^{|S|}\). Then

\[
D_{a,b,t}(z)=(1+z)^a+(1+z)^b-1+abz^2+t(a+b-2)z^3+\binom{t}{2}z^4,
\]

\[
M_{a,b,t}(z)=z^a+z^b+(a-t)(b-t)z^2+t(a+b-2t)z^3+\binom{t}{2}z^4.
\]

These identities count *labeled vertex subsets*, not isomorphism classes. Every inclusion-maximal dissociation set is exactly one of the structural types described below. In particular, when \(a=b=t=n\ge5\), the possible inclusion-maximal sizes are exactly \(\{4,n\}\). For \(n\ge6\), every integer strictly between \(4\) and \(n\) is absent, giving \(n-5\) consecutive missing sizes in a connected \((n-1)\)-regular bipartite graph.

## Assumptions and scope
All graphs are finite, simple, undirected. Write the bipartition as \(A=\{a_1,\ldots,a_a\}\), \(B=\{b_1,\ldots,b_b\}\). The removed matching consists of precisely \(a_i b_i\) for \(1\le i\le t\), and there are no other nonedges across the two parts. A vertex whose index exceeds \(t\) is called *unmatched* (not an endpoint of the deleted matching). Inclusion-maximal means that no strictly larger vertex subset remains dissociation; it is not synonymous with maximum-cardinality.

## Proof
Fix any vertex subset \(S=X\cup Y\), where \(X\subseteq A\), \(Y\subseteq B\). Write \(x=|X|\), \(y=|Y|\). For each selected \(a_i\), its degree within the induced graph equals \(y-\mathbf1_{\{i\le t,\ b_i\in Y\}}\); the analogous formula holds for each selected \(b_j\), with \(x\) in place of \(y\). These two exact degree formulas are the only local constraints needed.

If \(x=0\) or \(y=0\), every choice is dissociation, giving \((1+z)^a+(1+z)^b-1\) after correcting for the doubly counted empty set. If both are positive, no value of \(x\) or \(y\) can exceed \(2\): any selected vertex on the opposite side would otherwise have at least two neighbors. With \((x,y)=(1,1)\), all \(ab\) choices work. With \((x,y)=(2,1)\), the lone selected vertex in \(B\) must be one of the \(t\) matched endpoints, and its deleted counterpart must be among the two selected vertices of \(A\); the second \(A\) vertex has \(a-1\) choices. Thus there are \(t(a-1)\) choices. Similarly, \((x,y)=(1,2)\) contributes \(t(b-1)\). Finally, \((x,y)=(2,2)\) is possible if and only if both cross nonedges of the two selected \(A\) vertices are exactly the selected \(B\) vertices. Therefore \(S\) consists of the four endpoints of two distinct deleted matching edges, in \(\binom t2\) ways. Summing these disjoint cases proves the formula for \(D_{a,b,t}\).

It remains to determine which of these admissible subsets are inclusion-maximal. A one-sided subset can add a vertex from its own part unless it already equals that entire part. Both full parts are maximal, because any additional opposite-side vertex has at least \(a-1\ge2\), respectively \(b-1\ge2\), neighbors among its selected part.

For \((x,y)=(1,1)\), the selected pair is maximal exactly when both endpoints have index exceeding \(t\). Indeed, if either endpoint is matched, adding the deleted partner of that endpoint preserves the degree bound; conversely, if both are unmatched, adding any third vertex gives one selected vertex at least two neighbors. This contributes \((a-t)(b-t)\) maximal sets.

For \((x,y)=(2,1)\), the lone \(B\) vertex is some \(b_i\) with \(i\le t\), the selected \(A\) vertices are \(a_i\) and \(a_j\), and \(j\ne i\). This set is maximal exactly when \(j>t\). If \(j\le t\), adding \(b_j\) produces one of the permissible four-vertex configurations. If \(j>t\), adding any \(B\) vertex creates degree at least two at \(a_j\), and adding any \(A\) vertex creates degree at least two at \(b_i\). Thus there are \(t(a-t)\) maximal triples. Symmetry gives \(t(b-t)\) other maximal triples of type \((1,2)\). Every admissible \((2,2)\) subset is maximal, since any additional vertex would see at least two vertices across the bipartition. This proves \(M_{a,b,t}\) and the complete structural classification.

For \(a=b=t=n\), all terms involving \(a-t\) or \(b-t\) vanish, so \(M_{n,n,n}(z)=2z^n+\binom n2z^4\). If \(n\ge5\), these are precisely the two asserted sizes. The missing interval \(5,6,\ldots,n-1\) has \(n-5\) integers for \(n\ge6\). The crown graph is connected for \(n\ge3\) and \((n-1)\)-regular by construction.

## Verification
A standalone program `verification.py` constructs adjacency masks directly for each \(a,b\in\{3,4,5,6\}\) and every \(0\le t\le\min(a,b)\). It independently checks, for every one of the 83,456 vertex subsets across the 78 parameter profiles, the dissociation condition and the impossibility of a one-vertex extension; it compares each resulting counting polynomial coefficient with both claimed formulas. The verified program prints `VERIFICATION_OK profiles=78 vertex_subsets=83456`. The proof above establishes the infinite parameter ranges; these finite tests are consistency checks only.

## Relationship to prior work
Dissociation sets are equivalently complements of \(3\)-path vertex covers. Bock–Pardey–Penso–Rautenbach (2022) relate maximum dissociation numbers to independence and induced matching parameters and analyze equality cases in broad bipartite families; these numerical/algorithmic results do not directly give all-set and all-maximal-set counting polynomials for \(K_{a,b}-M_t\). Tu–Li–Du (2021) develop bounds for the number of maximal and maximum dissociation sets, including triangle-free graphs, rather than the exact three-parameter family enumerators here. Orlovich–Dolgui–Finke–Gordon–Werner (2011) study complexity of minimum maximal and maximum dissociation problems. Published calculations on dissociation polynomials of complete multipartite graphs address a different edge set: \(K_{a,b}\) is the \(t=0\) boundary, whereas deleting a nonempty matching changes facet structure. Other studies of \(K_{a,b}-M_t\) concern different parameters, including clique–stable-set incidence and geodesic subpaths. No identity of the present two polynomials was found among the inspected references, but this does not constitute a complete priority proof.

## Limitations
The parameter assumption \(a,b\ge3\) is essential to the stated facet classification: very small part sizes can create new maximal cases. The formulas do not address deleting edges that are not a matching, nor maximal induced subgraphs of maximum degree higher than one. The verification is exhaustive only for the finite tested range. Equivalent enumeration formulas might exist under the alternative names *maximum degree-one vertex subsets*, *induced \(P_3\)-free sets*, or *minimal \(3\)-path vertex covers*; comprehensive bibliographic priority verification and independent scientific validation are not performed.

## References
1. F. Bock, J. Pardey, L. D. Penso, D. Rautenbach, *Relating dissociation, independence, and matchings* (public preprint 2022-02-02), arXiv:2202.01004; https://arxiv.org/abs/2202.01004.
2. J. Tu, Y. Li, Z. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs* (2021), arXiv:2103.01402; https://arxiv.org/abs/2103.01402.
3. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366; https://doi.org/10.1016/j.dam.2011.04.023.
