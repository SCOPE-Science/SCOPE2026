# Independence complex of the Desargues graph is \(S^4\vee\bigvee^5 S^5\)
## Finding
Let \(D=G(10,3)\) be the Desargues graph, with vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Its independence complex satisfies \(\operatorname{Ind}(D)\simeq S^4\vee\bigvee^5 S^5\).

## Assumptions and scope
The graph \(D\) is the generalized Petersen graph \(G(10,3)\): its vertices are \(u_i,v_i\), where \(i\in\mathbb Z/10\mathbb Z\), and its edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). The independence complex \(\operatorname{Ind}(D)\) has as simplices exactly the independent vertex sets of \(D\). The statement is only for this graph; no classification of generalized Petersen graphs is claimed.

## Proof
Encode \(u_i\) by \(i\) and \(v_i\) by \(10+i\). Exact enumeration gives \(6212\) simplices including the empty face and nonempty face vector
\[
(20,160,660,1510,1924,1320,480,115,20,2).
\]

Use the staged face-poset matching with vertex order
\[
(u_9,u_6,v_6,u_1,v_3,u_0,u_8,v_8,v_7,v_2,u_2,v_9,v_5,v_4,u_3,v_0,v_1,u_5,u_4,u_7).
\]
At a stage with vertex \(w\), pair every still-unmatched face \(\sigma\) not containing \(w\) with \(\sigma\cup\{w\}\) whenever the latter is also still unmatched. The resulting matching has the empty face matched and has exactly six critical faces: one of dimension \(4\), namely
\[
\{u_0,u_2,v_4,v_5,v_6\},
\]
and five of dimension \(5\), namely
\[
\begin{aligned}
&\{u_0,u_2,u_4,u_7,v_1,v_3\},\quad
\{u_3,u_8,v_0,v_1,v_5,v_6\},\quad
\{u_3,u_5,u_7,v_0,v_1,v_9\},\\
&\{u_2,u_4,u_7,v_0,v_5,v_9\},\quad
\{u_0,u_3,u_5,v_4,v_8,v_9\}.
\end{aligned}
\]
Orient every unmatched Hasse cover upward and every matched cover downward. Exhaustive traversal of all \(30380\) covers is acyclic, so discrete Morse theory gives a homotopy-equivalent CW complex with one additional \(0\)-cell, one \(4\)-cell, and five \(5\)-cells.

It remains to determine the five attaching maps. With the standard increasing-vertex orientation, signed gradient-path elimination gives the integral Morse boundary coefficients from the five critical \(5\)-cells to the unique critical \(4\)-cell as
\[
(0,0,0,0,0).
\]
Thus the \(4\)-skeleton is \(S^4\), and each \(5\)-cell is attached by a map \(S^4\to S^4\) of degree \(0\). Since maps \(S^4\to S^4\) are classified up to homotopy by degree, all five attaching maps are null-homotopic. Therefore
\[
\operatorname{Ind}(D)\simeq S^4\vee\bigvee^5 S^5.
\]

## Verification
The accompanying `verify.py` reconstructs \(D\) from the definition, enumerates every independent set, rebuilds the matching, checks acyclicity on all \(30380\) Hasse covers, computes the signed integral Morse boundary, and independently computes simplicial homology over \(\mathbb F_2\). The boundary ranks are
\[
(19,141,519,991,932,383,97,18,2),
\]
and the Betti numbers are \(1\) in degree \(0\), \(1\) in degree \(4\), \(5\) in degree \(5\), and \(0\) otherwise. Successful replay ends with `DESARGUES_IND_VERIFY_OK`.

## Relationship to prior work
Nilakantan and Shukla compute independence complexes for the cyclic-interval regular bipartite family \(G_m^d\) [arXiv:1709.04789v1]. Their defining neighborhood pattern for \(G_{10}^3\) is not isomorphic to the Desargues graph, so their closed formula does not imply the finding here. Goyal, Shukla and Singh study categorical products of complete graphs, generalized Mycielskians of complete graphs, and a local suspension construction [arXiv:1905.06926v1]; their full text contains no Desargues or Petersen instance. Exact searches under the aliases “Desargues graph” and “generalized Petersen graph \(G(10,3)\)” found no source stating this homotopy type.

## Limitations
This is an exact result for one canonical finite graph, not a theorem for all generalized Petersen graphs. The novelty check covers the named graph, its standard alias \(G(10,3)\), the closest regular-bipartite formula, and two broad independence-complex sources, but obscure or unindexed literature could still contain the same computation. No independent audit has been performed.

## References
1. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1, first public 2017-09-14.
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, first public 2019-05-16.
