# Sharp edgewise Hodge stability for a clique with one partially connected vertex

## Finding
Let \(r\ge2\) and \(h\ge1\) be integers. Construct \(G_{r,h}\) from a clique on \(r+h\) vertices by adjoining a new vertex connected to exactly \(h\) clique vertices. This is the graph obtained from \(K_{r+h+1}\) by deleting the \(r\) edges of one star. On the oriented edge space, let \(P\) be the Euclidean orthogonal projection onto graph-gradient flows. Then its sharp coordinatewise norm is
\[
\|P\|_{\ell^\infty\to\ell^\infty}=\begin{cases}
\frac{2r}{r+1},&h=1,\\[3pt]
\frac{(r+1)(2r+7)}{(r+2)(r+3)},&h=2,\\[3pt]
\frac{2h^2+3hr-2r}{h(h+r+1)},&h\ge3.
\end{cases}
\]
Every value is attained by sign-valued edge data. For \(h=1\), the maximizing rows are those indexed by edges entirely within the \(r\)-vertex group and by edges between the two clique groups. For \(h=2\), only edges joining the groups maximize. For \(h\ge3\), only the edges incident with the newly adjoined vertex maximize.

The norm exceeds \(2\) if and only if \(h\ge3\) and \(rh>2(r+h)\). The smallest graph size admitting this amplification is ten vertices: at \((r,h)=(5,4)\), the sharp norm is \(41/20\). With the vertex count \(n=r+h+1\ge10\) fixed, maximizing attachments have integer \(h\) satisfying
\[
h(h-1)\le2(n-1)\le h(h+1).
\]
Consequently, the optimizing attachment degree satisfies \(h\sim\sqrt{2n}\), the largest norm among these graphs is \(3-2\sqrt{2/n}+O(n^{-1})\), and the supremum over the entire family equals \(3\) without attainment.

## Assumptions and scope
All graphs are finite, simple, unweighted, and connected. Write the clique as the disjoint union of a nonneighbor set \(F\) with \(|F|=r\) and a neighbor set \(H\) with \(|H|=h\); denote the extra vertex by \(c\). Choose any orientation of the graph edges. Let \(B\) be the vertex-by-edge incidence matrix (one positive and one negative entry in each column) and \(L=BB^\mathsf T\) the unnormalized graph Laplacian. The gradient projection is \(P=B^\mathsf T L^\dagger B\), where \(L^\dagger\) is the Moore–Penrose inverse. The orientation does not affect its coordinatewise operator norm. The norm uses the unweighted maximum of absolute edge coordinates, and does not assert optimality among all projections or other graph families.

## Proof
Fix an oriented edge \(e=(x,y)\). Any solution of \(Lu=\mathbf e_x-\mathbf e_y\), unique modulo constants, gives the exact absolute row sum of the edge projection:
\[
R_e=\sum_{\{a,b\}\in E(G_{r,h})}|u_a-u_b|.
\]
Indeed, \(P_{ef}\) is the signed potential difference across edge \(f\). The norm of a finite matrix in \(\ell^\infty\) is its largest absolute row sum; choosing signs that agree with the maximizing row attains it.

There are four edge orbits: \(A\) for edges within \(F\), \(B\) for edges between \(F\) and \(H\), \(C\) for edges between \(c\) and \(H\), and \(D\) for edges within \(H\). The last orbit is absent when \(h=1\). Put \(n=r+h+1\). For an edge in orbit \(A\), place potentials \(1/(n-1)\) and \(-1/(n-1)\) at its two endpoints and zero at all other vertices. For an edge in orbit \(D\), use \(1/n\) and \(-1/n\) at its endpoints, with zeros elsewhere. These solve the Laplacian equations and yield
\[
R_A=\frac{2(n-2)}{n-1},\qquad R_D=\frac{2(n-1)}n.
\]

For \(e=(f_1,h_1)\) in orbit \(B\), set the potential at \(c\) to zero and define
\[
u_{f_1}=\frac{h+1}{h(n-1)},\quad
u_{f}=\frac{1}{h(n-1)}\ (f\in F\setminus\{f_1\}),\quad
u_{h_1}=-\frac{h-1}{hn},\quad
u_h=\frac1{hn}\ (h\in H\setminus\{h_1\}).
\]
The displayed assignments directly satisfy \(Lu=\mathbf e_{f_1}-\mathbf e_{h_1}\), including when \(h=1\). Inserting their differences into the edge-sum formula gives
\[
R_B=\frac{2h^3+4h^2r+h^2+2hr^2+2hr-3h-2r}{h(h+r)(h+r+1)}.
\]
For \(e=(c,h_1)\) in orbit \(C\), use \(u_c=1/h\), \(u_f=0\) for all \(f\in F\), \(u_{h_1}=-(h-1)/(hn)\), and \(u_h=1/(hn)\) for the remaining vertices in \(H\). This solves the Laplacian equation and gives
\[
R_C=\frac{2h^2+3hr-2r}{h(h+r+1)}.
\]

The comparisons simplify exactly to
\[
R_B-R_A=\frac{(h-1)(h+2r)}{h(h+r)(h+r+1)},\qquad
R_C-R_B=\frac{(r-1)(h^2+hr-3h-2r)}{h(h+r)(h+r+1)},
\]
\[
R_C-R_D=\frac{r(h-2)}{h(h+r+1)},\qquad
R_B-R_D=\frac{h^2+2hr-3h-2r}{h(h+r)(h+r+1)}.
\]
For \(h=1\), orbit \(D\) does not exist and \(R_A=R_B>R_C\). For \(h=2\), the displayed differences give \(R_B>R_A,R_C,R_D\). For \(h\ge3\), all \(R_C-R_B\) and \(R_C-R_D\) are positive, and \(R_B\ge R_A\), so \(R_C\) uniquely dominates. Substitution gives the three claimed formulae.

In the third case, \(R_C-2=[rh-2(r+h)]/[h(r+h+1)]\). This is strictly positive precisely under the asserted condition. At most nine vertices imply \(r+h\le8\) and hence \(rh\le(r+h)^2/4\le2(r+h)\); taking \((r,h)=(5,4)\) gives \(41/20>2\). For fixed \(n\ge10\), write \(r=n-1-h\) in the third branch, obtaining
\[
R_C(h)=3-\frac{h+1}{n}-\frac{2(n-1)}{nh},\quad
R_C(h+1)-R_C(h)=\frac{1}{n}\left(\frac{2(n-1)}{h(h+1)}-1\right).
\]
Because the optimal third-branch value exceeds two while the first two branches are strictly below two, this difference proves the integer criterion for all global maximizers in the given family. It gives \(h=\sqrt{2(n-1)}+O(1)\). The continuous optimum and bounded rounding error prove \(3-2\sqrt{2/n}+O(n^{-1})\). Every finite branch is strictly below three, whereas these maxima converge to three.

## Verification
Run `python verify_projection.py` from the same directory. The standalone standard-library checker constructs the graph Laplacian, inverts the regularized matrix \(L+\mathbf 1\mathbf1^\mathsf T/n\) by exact rational Gauss–Jordan elimination, independently recomputes every projection row, and compares the four edge-orbit row sums, sharp norms, and threshold predicates for all \(2\le r\le8\) and \(1\le h\le8\). It produced `PASS: 2884 exact-rational row and threshold comparisons for 56 graphs.` These finite tests do not replace the preceding proof for all integers.

## Relationship to prior work
The graph-gradient least-squares projection is the standard graph-Hodge projection developed, among other places, by Jiang, Lim, Yao, and Ye. Its matrix entries also have the transfer-current/Green-function description developed by Kassel and Wu. Those general frameworks yield the starting projection identity, but the statements inspected do not supply the present exact four-orbit edgewise norms, the sharp ten-vertex threshold, or the optimal square-root attachment degree. The result concerns a clique with one partially connected vertex, not the graph classes of complete multipartite graphs, complete bipartite graphs with matching deletions, or wheels.

## Limitations
This is an exact analysis of a restricted two-parameter unweighted family under Euclidean projection in edge space, not the optimal projection over all possible complements, nor a characterization among all graphs. Priority is assessed against the material inspected; an older equivalent result under electrical-transfer-current or graph-ranking terminology may exist. The standalone finite computation cannot establish universal identities. Independent mathematical and bibliographic checks have not been performed.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, first posted 2008-11-07. Particularly the least-squares/Hodge discussion and Theorem 5.1.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first posted 2013-12-10. Particularly the transfer-current kernel and Green-function representation.
