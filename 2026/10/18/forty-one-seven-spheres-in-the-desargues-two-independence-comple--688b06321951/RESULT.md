# Forty-one seven-spheres in the Desargues two-independence complex

## Finding
Let \(D=\operatorname{GP}(10,3)\) be the twenty-vertex Desargues graph. Its two-independence complex is the simplicial complex of vertex subsets whose induced connected components have cardinality at most two. There is an integral homotopy equivalence
\[
\operatorname{Ind}_2(D)\simeq\bigvee^{41}S^7.
\]
In particular, \(\widetilde H_7(\operatorname{Ind}_2(D);\mathbb Z)\cong\mathbb Z^{41}\), and every other reduced integral homology group vanishes. The original simplicial complex has dimension \(11\); this is a classification of its homotopy type, not just a calculation of Betti numbers.

## Assumptions and scope
For each \(i\in\mathbb Z/10\mathbb Z\), the graph has vertices \(u_i,v_i\) and precisely the thirty undirected edges
\[
\{u_i,u_{i+1}\},\quad\{u_i,v_i\},\quad\{v_i,v_{i+3}\}.
\]
No other graph, parameter value, or convention for the ten-vertex graph sometimes also called a Desargues graph is intended. Label \(u_i\) with integer \(i\) and \(v_i\) with integer \(10+i\). A subset \(A\) is a simplex exactly when the induced graph \(D[A]\) has maximum degree at most one: a finite simple graph has this property if and only if each component is an isolated vertex or an edge. All statements use the abstract simplicial complex and its ordinary geometric realization.

## Proof
Represent each nonempty face by its twenty-bit incidence mask. Write \(\mathcal F\) for the set of masks that satisfy the induced-degree condition. Direct exhaustive enumeration from the displayed thirty edges gives \(|\mathcal F|=62{,}048\) and the dimension-by-dimension face counts
\[
(f_0,\ldots,f_{11})=(20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5).
\]
The computation is certified by the included standalone program `verify_desargues_ind2.py`, which also reconstructs exactly the same face set by independent inductive extension.

Construct the following completely specified partial matching on the poset of **nonempty** faces. Set the unmatched set initially to \(\mathcal F\). Process the vertices in the fixed order
\[
0,2,4,6,8,10,12,14,16,18,1,3,5,7,9,11,13,15,17,19.
\]
At vertex \(w\), pair every currently unmatched face \(\sigma\) not containing \(w\) with \(\sigma\cup\{w\}\) if both are still unmatched, and remove the paired faces. Pairs are codimension-one inclusions, and no face occurs twice. The sequential-element-matching theorem (Deshpande–Singh, Proposition 2.10) implies acyclicity; the standalone verifier additionally constructs **every** codimension-one cover of the nonempty face poset, reverses precisely these matching covers, and checks acyclicity by a complete directed topological sort. The precise result is \(31{,}003\) matched pairs, \(400{,}760\) directed covers, and only \(42\) critical cells: one critical zero-cell and forty-one critical seven-cells. All \(62{,}048\) faces occur in the topological sort.

Forman's acyclic-matching theorem now gives a CW model with exactly one zero-cell and forty-one seven-cells, with no cells in dimensions one through six. Each attaching map of a seven-cell therefore maps its boundary six-sphere to the unique zero-cell and is constant. The model is precisely a wedge of forty-one seven-spheres, proving the asserted integral homotopy classification. No assumption about the vanishing of integral attaching degrees, or inference from a finite Betti-number experiment, is used.

## Verification
Run `python3 verify_desargues_ind2.py` and `python3 verify_mod2.py` with a standard Python 3 interpreter, from a directory containing those files; no packages or data files are required. The first independently constructs the face set in two ways, verifies the full face-vector, constructs the stated matching, enumerates all covers, and proves that the directed Hasse graph is acyclic by topological sorting. The second computes full mod-two simplicial boundary ranks from a separate all-mask enumeration and obtains reduced Betti number \(41\) in degree \(7\), with all others zero. Recorded outputs are included as `verify_desargues_ind2.output.txt` and `verify_mod2.output.txt`. This second test corroborates the homology but is not substituted for the integral homotopy proof.

## Relationship to prior work
Deshpande and Singh [1] determine higher-independence homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees; their general matching theorems provide a proof tool here, but the Desargues graph belongs to none of those classified families. Sawant [2] establishes vertex decomposability of higher-independence complexes for trees and explicitly identifies the three-path-free complex with the two-independence complex. The Desargues graph has cycles and is not covered by the tree theorem. The ordinary independence complex \(\operatorname{Ind}_1(D)\), the graph's matching complex, its three-cut complex, and its graph-metric Rips complex are different simplicial complexes; knowing their homotopy types does not determine \(\operatorname{Ind}_2(D)\). The displayed result is therefore an exact calculation for the next higher-independence case of a canonical incidence graph, not a restatement of the ordinary-independence result.

## Limitations
The proof treats exactly \(\operatorname{GP}(10,3)\) with the stated two-independence definition; it does not classify all generalized Petersen graphs, graph coverings, or higher values of the independence parameter. It gives the integral homotopy type but does not determine the automorphism representation on the forty-one-dimensional top homology. Mathematical originality has been compared with identifiable prior sources, but an exhaustive search of all unpublished or unindexed work is impossible. The finite certificate has not undergone independent external audit.

## References
[1] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted 2020-01-15); especially the family classifications, Theorem 2.4, and Proposition 2.10. https://arxiv.org/abs/2001.05448

[2] R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150 (first posted 2026-05-24); especially Theorem 1.1 and the discussion of three-path-free complexes. https://arxiv.org/abs/2605.25150

[3] E. W. Weisstein, *Desargues Graph*, MathWorld; graph identification \(\operatorname{GP}(10,3)\), twenty vertices, thirty edges. https://mathworld.wolfram.com/DesarguesGraph.html
