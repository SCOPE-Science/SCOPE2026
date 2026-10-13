# Exact color-refinement depth of lollipop graphs
## Finding
For integers \(m\ge 3\) and \(n\ge 1\), let \(L_{m,n}\) be the lollipop graph obtained from a clique \(K_m\) with distinguished vertex \(q_0\) and a path \(p_1,\ldots,p_n\) by adding the bridge \(q_0p_1\). Start ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least \(s\) for which the partition after round \(s+1\) equals the partition after round \(s\).

Then
\[
\operatorname{Stab}(L_{m,n})=
\begin{cases}
\left\lceil n/2\right\rceil,&m\ge 4,\\
1,&m=3,\ n=1,\\
2,&m=3,\ n=2,\\
\max\{3,\left\lceil n/2\right\rceil\},&m=3,\ n\ge 3.
\end{cases}
\]

There is also an exact round-by-round description. Write \(Q=\{q_1,\ldots,q_{m-1}\}\). If \(m\ge4\), then for every round \(r\ge1\), \(q_0\) and \(Q\) are separate color classes, every \(p_j\) with \(j<r\) or \(j>n-r\) is already a singleton color class, and all remaining path vertices
\[
p_r,p_{r+1},\ldots,p_{n-r}
\]
form one color class when this interval is nonempty. For \(m=3\), round \(1\) has the class \(Q\cup\{p_1,\ldots,p_{n-1}\}\); for \(n\ge3\), round \(2\) has the class \(Q\cup\{p_1\}\); from round \(3\) onward the same two-sided path-wave description as above holds, with \(Q\) as its own class.

## Assumptions and scope
All graphs are finite, simple, undirected, and unlabeled. The path parameter \(n\) counts the path vertices outside the clique, so \(L_{m,n}\) has \(m+n\) vertices. Color refinement uses the standard update
\[
C^{r+1}(v)=\left(C^r(v),\ \{\!\{C^r(w):w\in N(v)\}\!\}\right),
\]
up to renaming of colors. Stabilization refers to equality of the induced vertex partitions, not literal equality of color names.

## Proof
Suppose first that \(m\ge4\). In round \(1\), degrees already give four possible types: \(q_0\) has degree \(m\), the vertices of \(Q\) have degree \(m-1\), each non-leaf path vertex has degree \(2\), and \(p_n\) has degree \(1\). Hence \(q_0\), \(Q\), and \(p_n\) are separated, while \(p_1,\ldots,p_{n-1}\) form one class when \(n\ge2\).

Inductively assume the stated partition at round \(r\). The vertices strictly inside the unresolved interval \(p_r,\ldots,p_{n-r}\) have the same old color and see the same multiset of old colors as long as they are not at an end of that interval. The left boundary \(p_r\) sees the already distinguished color immediately to its left, while the right boundary \(p_{n-r}\) sees the already distinguished color immediately to its right. Those two outside colors are distinct, and therefore the two boundary vertices split from the unresolved class in the next round. Previously separated singleton classes cannot merge under refinement, and the vertices in \(Q\) remain together by clique symmetry. This proves the round-by-round description by induction.

Consequently the only color class that can still split after round \(r\) is the unresolved path interval, of size
\[
n-2r+1.
\]
The partition is stable exactly when this size is at most \(1\). The least such \(r\ge1\) is \(\lceil n/2\rceil\).

Now let \(m=3\). The two vertices of \(Q\) have degree \(2\), which is the same degree as every non-leaf path vertex. Thus round \(1\) merges \(Q\) with \(p_1,\ldots,p_{n-1}\), while \(q_0\) and \(p_n\) are separate. If \(n=1\), this partition is already stable.

For \(n=2\), the vertex \(p_1\) sees \(q_0\) and the leaf \(p_2\), whereas a vertex of \(Q\) sees \(q_0\) and the other vertex of \(Q\). Hence \(p_1\) separates from \(Q\) in round \(2\), and the partition is then stable.

Assume \(n\ge3\). In round \(2\), a vertex of \(Q\) and \(p_1\) still have the same old color and both see one neighbor of the \(q_0\)-color and one neighbor of their common degree-\(2\) color, so they remain together. The right-hand leaf wave simultaneously separates \(p_{n-1}\), and the remaining middle path vertices stay together. In round \(3\), a vertex of \(Q\) sees another vertex of the class \(Q\cup\{p_1\}\), whereas \(p_1\) sees \(p_2\), whose round-\(2\) color is different. Thus \(Q\) and \(p_1\) split. At the same time the usual path boundary vertices split from the remaining middle block. From this point on, the same induction as for \(m\ge4\) applies. Therefore stabilization cannot occur before round \(3\), and after round \(3\) it occurs exactly when the unresolved path interval has size at most \(1\). This gives
\[
\operatorname{Stab}(L_{3,n})=\max\{3,\lceil n/2\rceil\}
\]
for \(n\ge3\).

## Verification
The accompanying `verify.py` implements color refinement directly and independently checks both the depth formula and the full round-by-round partition description for every \(3\le m\le20\) and \(1\le n\le80\). It returns:

`VERIFY_OK depth_checks=1440 partition_checks=29523 m=3..20 n=1..80`

The computation is a finite consistency check; the proof above establishes the formula for all allowed parameters.

## Relationship to prior work
Krebs and Verbitsky define the stabilization number \(\operatorname{Stab}(G)\), study its round complexity, and prove that round-\(r\) colors are exactly the depth-\(r\) rooted universal-cover types. Their framework explains why color information propagates locally one edge per round, but it does not give a lollipop-graph formula. Arvind, Köbler, Rattan, and Verbitsky study the structural range of color refinement and amenability rather than exact stabilization depths for this family. Kiefer and McKay later prove general extremal results for the iteration number of color refinement; their broad bounds do not state this lollipop-specific law.

The lollipop family is a standard named graph family. The formula isolates a sharp structural boundary at \(m=3\): for every larger clique, the clique/path interface is separated by degree in the first round, while the triangle creates an exact two-round delay because its two ordinary clique vertices have degree \(2\), matching the path interior.

## Limitations
This result concerns ordinary one-dimensional color refinement from the uniform initial coloring. It does not address higher-dimensional Weisfeiler--Leman refinement, arbitrary initial vertex colors, graph pairs under disjoint-union refinement, or logical defining depth. The computation checks only the stated finite parameter range and is not used as a substitute for the general proof.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015.
3. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73.
