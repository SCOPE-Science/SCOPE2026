# Single-commutator width of unicyclic graph Lie algebras over arbitrary fields

## Finding
Let \(G\) be a finite, connected, simple unicyclic graph. Write \(C\) for its unique simple cycle and \(U\) for the set of vertices of \(C\) without neighbors off the cycle. Give each edge an orientation, and construct the two-step nilpotent graph Lie algebra \(L_G=K^{V(G)}\oplus K^{E(G)}\) over an arbitrary field \(K\), with each edge basis element central and \([v,w]\) equal to the signed basis element of edge \(\{v,w\}\) (zero for nonedges).

**Theorem.** The commutator width of \(L_G\) is always at most \(2\). It equals \(1\) precisely when
\[
 \forall e\in E(C),\qquad U\setminus V(e)\neq\varnothing.
\]
If the condition fails, its width is exactly \(2\). Equivalently, the width-one graphs have either at least three unbranched cycle vertices or precisely two nonadjacent unbranched cycle vertices. This includes every bare cycle. Here width means the smallest \(t\ge1\) such that every member of \([L_G,L_G]\) is a sum of at most \(t\) brackets of pairs of elements.

## Assumptions and scope
The graph is finite, undirected, simple, connected, and has exactly one cycle (of length at least \(3\)); trees of arbitrary finite shape may be attached at its cycle vertices. All fields, including finite fields and characteristic \(2\), are allowed. The Lie bracket is alternating in characteristic \(2\). Fix a cyclic ordering for the cycle, with its edges oriented consecutively, and orient tree edges outwards. Reversing an edge only rescales a central basis vector by \(-1\), so the width is orientation independent. The derived algebra is exactly the edge space \(K^{E(G)}\).

## Proof
For elements \(x,y\in L_G\), write their vertex coordinates as \(a_v,b_v\in K\) and set \(X_v=(a_v,b_v)\in K^2\). The coefficient of the oriented edge \(v\to w\) in \([x,y]\) is
\[
 \det(X_v,X_w)=a_vb_w-b_va_w.
\]
Central coordinates of \(x,y\) do not affect their bracket. Conversely, any assignment of vectors \(X_v\in K^2\) arises from a pair of elements. Thus the word-image problem is precisely the simultaneous prescription of determinants along edges.

**Tree extension.** On a rooted tree, suppose the root vector is nonzero. For arbitrary target coefficients on its edges one can choose all descendant vectors nonzero inductively: given \(X\neq0\) and desired \(c\in K\), take \(Y=X\) if \(c=0\), and otherwise choose \(Y\neq0\) with \(\det(X,Y)=c\). Such a vector exists over every field. Hence attaching trees imposes no constraints provided all their root vectors on the cycle are nonzero.

**Cycle assignment with no zeros.** Prescribe arbitrary edge coefficients \(c_1,\dots,c_h\) around a cycle. If every coefficient is zero, use the same nonzero vector at all vertices. Suppose at least two coefficients are nonzero, and consider maximal paths of zero-coefficient cycle edges. For at least three nonzero coefficients, contract the zero paths, obtaining a shorter cyclic system of length \(k\ge3\) with all edge coefficients nonzero. The length-three system has the explicit nonzero solution
\[
 X_1=(1,0),\quad X_2=(0,c_1),\quad X_3=(-c_2/c_1,-c_3).
\]
A cyclic edge with nonzero determinant can be subdivided into two prescribed nonzero determinants: given independent endpoints \(A,B\), the two independent linear equations \(\det(A,X)=d_1\) and \(\det(X,B)=d_2\) determine a unique, nonzero intermediate \(X\). Iterated subdivision solves every longer cyclic system with all nonzero coefficients. Expand each contracted zero path using the same nonzero vector throughout.

When exactly two cycle coefficients are nonzero, the remaining edges form two zero paths between these edges, at least one of which has positive length. Orient cyclically and choose names so that the zero path from the endpoint of the second nonzero edge back to the start of the first is nonempty. Assign \(X_a=(1,0)\), \(X_b=(0,c_1)\) along the first nonzero edge, take the vector along the following zero path equal to \(X_b\), assign the other endpoint of the second edge \(X_d=(-c_2/c_1,0)\), and follow the remaining zero path with nonzero vectors proportional to \((1,0)\), returning to \(X_a\). All zero and nonzero target determinants are then correct. This also works in characteristic \(2\). Thus every cyclic target with either zero or at least two nonzero coefficients has a realization with all cycle vectors nonzero, and it extends to all attached trees.

**One nonzero cycle coefficient.** Suppose only the coefficient of cycle edge \(e\) is nonzero. In any realization, some cycle vertex outside \(V(e)\) must have vector \(0\). Indeed, if every vector on the path obtained by deleting \(e\) were nonzero, the zero determinants on that path would force all those vectors to be collinear; the determinant on \(e\) would then also vanish. If a zero vector occurs at a vertex having an attached tree, the bracket coefficient on every tree edge incident with that vertex must vanish.

Conversely, if some \(v\in U\setminus V(e)\) exists, put \(X_v=0\). The two incident cycle-edge targets are zero because \(v\) is not an endpoint of \(e\). Deleting \(v\) leaves a path; choose vectors on this path by the tree extension argument so that each is nonzero and all its edge coefficients are correct. At the other cycle vertices, extend to their attached trees, producing the entire prescribed central value as one bracket.

It follows that if \(U\setminus V(e)\neq\varnothing\) for every cycle edge, every central value is a single bracket. If the criterion fails for some edge \(e\), prescribe coefficient \(1\) on \(e\), zero on all other cycle edges, and coefficient \(1\) on one off-cycle edge incident with each cycle vertex outside \(U\) (all other tree-edge coefficients may be zero). Any putative single-bracket representation must have a zero vector at a cycle vertex outside \(V(e)\), but every such vertex has a prescribed incident coefficient \(1\), contradiction. Therefore width one is impossible.

**Universal width-two bound.** Delete an arbitrary cycle edge \(e_0\), obtaining a spanning tree. Prescribe all desired coefficients on this tree by choosing nonzero vertex vectors as above, producing a bracket whose coefficients agree everywhere except possibly on \(e_0\). Any residual multiple of the basis element of \(e_0\) is a single bracket: take nonzero coordinates at the two endpoints of \(e_0\) and zero at all other vertices. Thus at most two brackets always suffice. This proves both implications and the sharp values.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It exhaustively enumerates every pair of vertex-coordinate vectors over \(\mathbf F_2\) and \(\mathbf F_3\) for eight representative graphs, including all bare triangles, a triangle with a leaf, a square with one leaf, and squares with leaves at opposite or adjacent vertices. It verifies the predicted surjectivity versus strict failure and, for failing graphs, that sums of two brackets cover the entire center. Run `python verify.py`; success prints `VERIFY_OK`. These finite checks test boundary cases and are not substitutes for the all-field proof above.

## Relationship to prior work
Godoy Molina and Lagos (arXiv:2308.00272, first submitted August 1, 2023) construct graph-associated two-step nilpotent Lie algebras and investigate graph ideals and graded derivations; their sections on graph ideals and complete bipartite derivations do not state this unicyclic commutator-width criterion. Niranjan and Rani (arXiv:2204.13050, first submitted April 27, 2022) classify the image of a degree-two Lie polynomial when the derived algebra has dimension at most four, including coverage of some low-edge cases of the present theorem in odd characteristic. Their statements do not cover arbitrary unicyclic graphs with arbitrarily many edges and arbitrary fields. Rossmann (arXiv:2107.05564) enumerates conjugacy classes of graphical groups and is relevant context but counts a different invariant. The distinction between individual commutator images and the linear span of brackets is essential: the latter is always the entire derived space by definition. No claim of exhaustive literature coverage is made.

## Limitations
The classification is restricted to connected simple unicyclic graphs and uses distinct central labels for all edges. It does not classify images on arbitrary multicyclic or edge-labeled graph Lie algebras; it counts the maximum number of brackets but does not count their individual fibers. Some small-dimensional implications are already contained in the prior Lie-polynomial image literature. The work has received only self-review, not independent audit.

## References
1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272, first submitted 2023-08-01. https://arxiv.org/html/2308.00272v2
2. Niranjan and S. Rani, *Image of Lie polynomial of degree 2 evaluated on Nilpotent Lie algebra*, arXiv:2204.13050, first submitted 2022-04-27. https://arxiv.org/html/2204.13050v1
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first submitted 2021-07-12. https://arxiv.org/abs/2107.05564
