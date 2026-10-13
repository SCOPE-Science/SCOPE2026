# Seven-cell counterexamples to an odd-even flat-band equality

## Finding

Let \(\mathcal F_n^s\) denote the set of real energies that occur as **single-cell flat bands** of adjacency operators on connected, simple, unweighted, \(\mathbb Z\)-periodic graphs with an \(n\)-vertex fundamental cell, as in Sabri--Youssef. Then
\[
\boxed{\{\lambda:\lambda^2+\lambda-4=0\}\ \cup\ \{\lambda:\lambda^3+\lambda^2-4\lambda-2=0\}\ \subseteq\ \mathcal F_7^s\setminus\mathcal F_6^s.}
\]
These two polynomials have five distinct real roots. Consequently \(\mathcal F_7^s\ne\mathcal F_6^s\), providing counterexamples at the first previously unresolved odd-even stage to the equality question posed in Sabri--Youssef, *Flat bands of periodic graphs*, Section 4.

## Assumptions and scope

All graphs in this result are simple, undirected, unweighted, and loop-free. A fundamental cell is a specified set of \(n\) vertices whose integer translates partition the vertices of a connected \(\mathbb Z\)-periodic graph. A single-cell flat band is a real adjacency eigenvalue with a nonzero eigenfunction supported on one fundamental cell. Every such eigenvalue is an eigenvalue of the simple finite \(n\)-vertex graph induced by that cell: the eigenvalue equation at vertices inside the cell reduces to the induced adjacency eigenvalue equation.

To construct explicit graphs, let \(H\) be a simple connected graph on vertices \(0,1,\ldots,6\), and let \(\delta\in\{0,1\}^7\setminus\{0\}\). On the vertex set \(\mathbb Z\times\{0,\ldots,6\}\), reproduce the edges of \(H\) inside each cell and, for each \(m\in\mathbb Z\), add an undirected edge from \((m,i)\) to \((m+1,j)\) whenever \(\delta_i=\delta_j=1\). These intercell edges join distinct cells and cannot be loops or duplicate an intracell edge. The infinite graph is connected because \(H\) is connected and at least one intercell edge exists. Its Floquet adjacency matrix is
\[
A_H+(z+z^{-1})\delta\delta^{\mathsf T},\qquad |z|=1.
\]

## Proof

**Quadratic witness.** Take the nine internal edges
\[
E_2=\{(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(2,5),(2,6),(5,6)\}
\]
and selector \(\delta_2=(0,0,1,1,0,0,0)^{\mathsf T}\). Let \(p_2(X)=X^2+X-4\) and
\[
v_2(X)=(X+1,X+1,-2,2,2,-(X+2),-(X+2))^{\mathsf T}.
\]
For each root \(\lambda\) of \(p_2\), direct adjacency multiplication gives \(A_{H_2}v_2(\lambda)=\lambda v_2(\lambda)\) and \(\delta_2^{\mathsf T}v_2(\lambda)=-2+2=0\). The vector is nonzero because its third component is \(-2\). Thus the vector supported on a single cell is an eigenfunction of the infinite adjacency operator at either root, regardless of neighboring-cell amplitudes: the coupling to neighboring cells vanishes since \(\delta_2^{\mathsf T}v_2=0\). Equivalently the same vector is an eigenvector of every Floquet fiber. Both roots \((-1\pm\sqrt{17})/2\) are real, distinct, and irrational.

**Cubic witness.** Add the edge \((0,1)\) to \(E_2\) to obtain \(E_3\), and use \(\delta_3=(1,1,1,1,1,1,0)^{\mathsf T}\). Let
\[
\begin{aligned}
p_3(X)&=X^3+X^2-4X-2,\\
a(X)&=2(X-1),\qquad b(X)=(X-1)^2,\\
c(X)&=X(X-1)-4,\qquad d(X)=(X-1)c(X),\\
v_3(X)&=(a(X),a(X),d(X),b(X),b(X),c(X),c(X))^{\mathsf T}.
\end{aligned}
\]
Direct multiplication shows every component of \((A_{H_3}-XI)v_3(X)\) is divisible by \(p_3(X)\), while
\[
\delta_3^{\mathsf T}v_3(X)=2a(X)+d(X)+2b(X)+c(X)=p_3(X).
\]
At every root \(\lambda\) of \(p_3\), the resulting nonzero \(v_3(\lambda)\) is therefore a single-cell eigenfunction of the connected periodic graph. Nonvanishing follows because \(a(\lambda)=0\) would require \(\lambda=1\), but \(p_3(1)=-4\). The cubic has no rational root among the only candidates \(\pm1,\pm2\), hence is irreducible over \(\mathbb Q\); its discriminant is \(316>0\), so all three roots are distinct and real. Since \(p_2\) is irreducible with discriminant \(17\), and \(\gcd(p_2,p_3)=1\), the five constructed energies are pairwise distinct.

**Why none fits in six vertices.** If an energy \(\lambda\) is a single-cell flat band with six cell vertices, the restriction of a single-cell eigenfunction to that cell is nonzero and satisfies \(A_Hv=\lambda v\), where \(H\) is a finite simple graph on six vertices (not necessarily connected). It is therefore necessary that \(\lambda\) be an eigenvalue of the adjacency matrix of at least one such graph. Up to graph isomorphism, there are exactly \(156\) finite simple graphs on six vertices, including disconnected graphs. The bundled, frozen `atlas_n6.graph6` enumerates every class. For each entry, `verify.py` computes its integer adjacency characteristic polynomial exactly and verifies
\[
p_2\nmid\det(XI-A_H),\qquad p_3\nmid\det(XI-A_H).
\]
Because both \(p_2\) and \(p_3\) are irreducible over \(\mathbb Q\), an eigenvalue that is a root of either must force that entire minimal polynomial to divide \(\det(XI-A_H)\). The exhaustive exact check excludes this possibility for every six-vertex cell and completes the proof.

## Verification

Run `python verify.py` in the directory containing `verify.py` and `atlas_n6.graph6`, with the packages specified in `requirements.txt` installed. The verifier checks connectedness and nonzero bridge selectors for both seven-vertex motifs, symbolic eigenvector identities modulo each exact minimal polynomial, selector orthogonality, the discriminants and irreducibility, coprimality, the complete list of \(156\) six-vertex graph-isomorphism types against NetworkX's Graph Atlas, and the absence of either polynomial factor in every integer characteristic polynomial. All operations determining the mathematical conclusions are exact; no floating-point root estimate or finite sampling over Floquet parameters is used as proof. The frozen graph6 entries allow a reader to inspect every six-vertex class used in the finite proof. The reference enumeration is the Graph Atlas of Read and Wilson.

## Relationship to prior work

Sabri and Youssef (2023), Section 4 and Theorem 4.6, give the binary-selector criterion for single-cell flat bands and determine small-cell examples through five vertices. Having observed equality between the adjacent even/odd cases studied there, they ask whether the analogous equality persists in general. The present explicit connected seven-cell witnesses, together with an exhaustive six-vertex obstruction, answer that equality question negatively at the next odd stage. The sufficiency of the selector construction is compatible with their criterion; the genuinely new part is the discovery and minimality of the five algebraic spectral values relative to all six-vertex cells.

The same quadratic and cubic factors occur in the known adjacency characteristic polynomial of the **24-vertex McGee graph**, as recorded in spectral graph catalogues. This occurrence supplies neither a one-cell periodic graph construction with seven vertices per cell nor the necessary exclusion for all six-vertex motifs. Our claim is about the *minimal size for an unweighted periodic single-cell realization*, not first appearance of these algebraic numbers in any graph spectrum.

Faust--Liu (2025) and Faust--Kachkovskiy (2025) establish generic absence of flat bands under parameter variation. Those genericity statements do not determine the exact unweighted single-cell spectral sets at specified cell sizes and do not imply the exhibited inequality.

## Limitations

Only five explicitly identified energies are shown to lie in \(\mathcal F_7^s\setminus\mathcal F_6^s\); no exhaustive description of \(\mathcal F_7^s\), its cardinality, or the full difference set is asserted. The six-vertex exclusion is exhaustive within *simple unweighted adjacency* cell graphs, not weighted graphs or Schrödinger operators with arbitrary site potentials. The result concerns flat bands having a nonzero eigenfunction on one specified fundamental cell; it does not classify flat bands whose shortest eigenfunctions span multiple cells. The literature search could miss an equivalently phrased construction in an incompletely indexed source. Independent review has not been performed.

## References

1. M. Sabri and P. Youssef, *Flat bands of periodic graphs*, Journal of Mathematical Physics **64** (2023), 092101; arXiv:2304.06465, first public 2023-04-13. Theorem 4.6, Section 4 and Appendix A. DOI: 10.1063/5.0156336.
2. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998; six-vertex simple graph catalogue, also distributed through `networkx.generators.atlas.graph_atlas_g` (NetworkX documentation, https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html).
3. M. Faust and W. Liu, *Rare Flat Bands for Periodic Graph Operators*, arXiv:2503.03632, 2025.
4. E. W. Weisstein, *McGee Graph*, MathWorld (https://mathworld.wolfram.com/McGeeGraph.html); exact adjacency characteristic-polynomial factorization.
5. M. Faust and I. Kachkovskiy, *Absence of flat bands for discrete periodic graph operators with generic potentials*, arXiv:2509.01927, 2025.
