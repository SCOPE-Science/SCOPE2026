# Even-theta spectral rigidity and simultaneous metric–Laplacian equality

## Finding
Let \(G_r=\Theta_{2,2,r}\) be the simple graph obtained by joining two terminals by three internally vertex-disjoint paths of lengths \(2,2,r\), where \(r\ge2\) is even. Let \(\operatorname{mm}_L(G)\) and \(\operatorname{mm}_Q(G)\) denote the largest multiplicity of any eigenvalue of the ordinary and signless graph Laplacians. Then
\[
\operatorname{mm}_L(G_r)=\operatorname{mm}_Q(G_r)=
\begin{cases}2,&r\equiv2\pmod4,\\1,&r\equiv0\pmod4.\end{cases}
\]
More precisely, every Laplacian eigenvalue other than \(2\) is simple, and \(2\) has multiplicity two if and only if \(r\equiv2\pmod4\). The metric dimension (minimum cardinality of a vertex-distance resolving set) is
\[
\dim(G_r)=\begin{cases}3,&r\in\{2,4\},\\2,&r\ge6\text{ even}.\end{cases}
\]
Consequently **both** equalities \(\operatorname{mm}_L(G_r)=\dim(G_r)\) and \(\operatorname{mm}_Q(G_r)=\dim(G_r)\) hold simultaneously exactly when \(r\equiv2\pmod4\) and \(r\ge6\). The metric-dimension component agrees with the known theta-graph classification; the new component is the exact all-eigenvalue multiplicity classification in the previously omitted even-length regime.

## Assumptions and scope
All graphs are finite, undirected, unweighted and simple. Write \(r=2s\), \(s\ge1\). Name the terminal vertices \(u,v\), the degree-two vertices on the two short paths \(a,b\), and the internal vertices of the long path \(w_1,\ldots,w_{r-1}\), with \(w_0=u\) and \(w_r=v\). Thus \(G_r\) has \(r+3\) vertices. Define \(L=D-A\) and \(Q=D+A\), with \(A\) the adjacency matrix and \(D\) the diagonal degree matrix. A resolving set distinguishes every two vertices by their vectors of shortest-path distances to the selected landmarks. No claim concerns weighted Laplacians, arbitrary theta graphs or edge metric dimension.

## Proof
**1. Bipartite similarity and twin eigenvector.** All three terminal-to-terminal paths have even length, hence \(G_r\) is bipartite. Switching signs on one bipartition class gives a diagonal matrix \(S\) satisfying \(Q=SLS\). Therefore the two matrices have identical spectra and multiplicities. The false twins \(a,b\), of degree two, furnish the eigenvector \(e_a-e_b\) of \(L\) with eigenvalue \(2\). Its orthogonal complement is the subspace where the \(a\)- and \(b\)-coordinates agree.

**2. Symmetry-sector tridiagonal blocks.** On that complement, reflect the long path by interchanging \(u\leftrightarrow v\) and \(w_j\leftrightarrow w_{r-j}\), leaving \(a,b\) fixed. In the antisymmetric reflection sector, with orthonormal ordered basis proportional to
\[
(e_u-e_v),(e_{w_1}-e_{w_{r-1}}),\ldots,(e_{w_{s-1}}-e_{w_{s+1}}),
\]
\(L\) restricts to the \(s\times s\) symmetric Jacobi matrix \(J_-\) having diagonal \((3,2,\ldots,2)\) and every off-diagonal entry \(-1\). When \(s=1\), this is just \([3]\). In the symmetric sector use the normalized ordered basis
\[
(e_a+e_b)/\sqrt2,\quad(e_u+e_v)/\sqrt2,\quad(e_{w_1}+e_{w_{r-1}})/\sqrt2,\ldots,\quad e_{w_s}.
\]
The restriction \(J_+\), of order \(s+2\), has diagonal \((2,3,2,\ldots,2)\), first off-diagonal \(-2\), final off-diagonal \(-\sqrt2\), and all intervening off-diagonals \(-1\). For \(s=1\), the two off-diagonal entries are exactly \(-2,-\sqrt2\). Both blocks are real symmetric irreducible tridiagonal matrices, so each has simple spectrum.

**3. Exact continuants and cross-sector disjointness.** Put \(t=2-\lambda\) and define \(p_0(t)=1\), \(p_1(t)=t\), and \(p_{j+1}(t)=t p_j(t)-p_{j-1}(t)\) for every \(j\ge1\). The tridiagonal determinant recurrence gives
\[
\det(J_- -\lambda I)=p_s(t)+p_{s-1}(t)=:F_-(t),
\]
\[
\det(J_+ -\lambda I)=\bigl(t^2+2t-8\bigr)p_s(t)+\bigl(2t-t^2\bigr)p_{s-1}(t)=:F_+(t).
\]
In particular, \(\det(L-\lambda I)=t F_-(t)F_+(t)\). To see the second identity directly, the initial continuants of the symmetric sector are \(D_0=1\), \(D_1=t\), \(D_2=t(t+1)-4\); after the intervening unit-weight edges, \(D_{s+1}=t p_s+(t-4)p_{s-1}\) and \(D_s=t p_{s-1}+(t-4)p_{s-2}\), where \(p_{-1}=0\) is understood for \(s=1\). The last edge has squared weight two, so \(F_+=tD_{s+1}-2D_s\), yielding the displayed formula.

Consecutive \(p\)'s never have a common complex zero, since their recurrence would propagate a hypothetical common zero back to \(p_0=1\). At a zero of \(F_-\), \(p_{s-1}=-p_s\ne0\), and thus \(F_+=2(t^2-4)p_s\). The only possible shared zeros are \(t=2\) or \(t=-2\). But \(p_j(2)=j+1\) and \(p_j(-2)=(-1)^j(j+1)\), giving \(F_-(2)=2s+1\ne0\) and \(F_-(-2)=(-1)^s\ne0\). Hence the two Jacobi blocks have **disjoint spectra**. As each block is individually simple, the full Laplacian spectrum is simple except possibly at the twin eigenvalue \(2\).

**4. Exact collision at \(2\).** At \(t=0\), \(F_+(0)=-8p_s(0)\), whereas \(F_-(0)=p_s(0)+p_{s-1}(0)\ne0\). The recurrence gives \(p_s(0)=0\) exactly when \(s\) is odd. Therefore \(2\) occurs once more, in the symmetric sector, exactly when \(s\) is odd; the remaining eigenvalues are all simple. This proves the multiplicity formula, including the smallest \(s=1\) case.

**5. Metric dimension.** The vertices \(a,b\) are false twins, and a single landmark in \(\{a,b\}\) leaves \(u,v\) equidistant. Thus \(\dim(G_r)\ge2\) always. For even \(r\ge6\), \(\{a,w_1\}\) resolves the graph. In fact the distance pairs for \(u,v,a,b\) are respectively \((1,1),(1,3),(0,2),(2,2)\); for \(1\le j<r\), the long-path vertex \(w_j\) has
\[
\bigl(d(a,w_j),d(w_1,w_j)\bigr)
=\bigl(1+\min\{j,r-j\},\ \min\{j-1,r-j+3\}\bigr).
\]
These pairs are mutually distinct: two long-path vertices with the same first coordinate are either identical or lie at positions \(j\) and \(r-j\); for \(j<r/2\) their second coordinates differ, since \(j-1<\min\{r-j-1,j+3\}\). The long-path pairs also avoid the four exceptional pairs when \(r\ge6\). For \(r=2\), the graph is \(K_{2,3}\), whose two twin classes force metric dimension three; a three-landmark set resolves. For \(r=4\), every resolving pair must contain \(a\) or \(b\). Up to swapping these twins it contains \(a\); the six choices for its other vertex \(u,v,b,w_1,w_2,w_3\) fail respectively to distinguish the pairs \((b,w_1),(b,w_3),(u,v),(b,w_3),(u,v),(b,w_1)\). Conversely \(\{a,u,v\}\) resolves. Hence the metric-dimension formula, and the simultaneous equality criterion, follow.

## Verification
Run `python verify.py` in a Python environment with SymPy. The script constructs the graph edges independently for every even \(r\in\{2,4,\ldots,24\}\), computes characteristic polynomials exactly over the integers, verifies the displayed two-sector factorization, their polynomial gcd and simple roots, tests eigenvalue multiplicities, and computes graph distances to check metric bases and small exceptions. Exact output ends in `VERIFY_OK EVEN_THETA r=2,4,...,24 exact_spectral_factorizations, multiplicities, metric_bases`. These finite computations corroborate but do **not** prove the infinite claim; Steps 1–5 provide the universal argument.

## Relationship to prior work
Alfuraidan, Khan and Sauras-Altuzarra, arXiv:2610.26875v1 (public 2026-10-06), Theorem 25, establish analogous maximum-multiplicity formulas for \(\Theta_{2,2,r}\) **only when \(r\ge3\) is odd**; their Problem 29 explicitly requests a theta-graph equality classification. The present result handles the complementary **even** branch, including the two exceptional metric dimensions, and isolates an infinite subclass with simultaneous equality of both Laplacian multiplicity invariants and metric dimension. Knor, Sedlar and Škrekovski (2022) already classify theta-graph metric dimension, so this component is not claimed as new. Paone and Paone (2026), Corollary 8.1, already count the multiplicity of the single signless-Laplacian eigenvalue \(2\) for generalized theta graphs; this does **not** by itself establish that all other eigenvalues are simple or determine the maximum over the entire spectrum. Those additional conclusions are proved above. The reflection/continuant technique is related to the odd-branch proof; the even-branch block boundary and disjointness identities are distinct.

## Limitations
This is an exact theorem for unweighted simple graphs with short path lengths \(2,2\) and even third path length \(r\ge2\), not a general classification of \(\Theta_{p,q,r}\). No claim of historical-priority certification or independent validation is made. The finite checker assumes SymPy; the proof is mathematical and independent of that library. General theta-graph eigenvalue multiplicity classifications and unlocated equivalent spectral reductions remain potential historical-priority risks.

## References
1. M. R. Alfuraidan, S. Khan, L. Sauras-Altuzarra, *Metric dimension and maximum eigenvalue multiplicity of graph Laplacians*, arXiv:2610.26875v1 (2026-10-06), Section 8 and Problem 29. https://arxiv.org/html/2610.26875v1
2. M. Knor, J. Sedlar, R. Škrekovski, *Remarks on the Vertex and the Edge Metric Dimension of 2-Connected Graphs*, Mathematics 10 (2022), 2411, doi:10.3390/math10142411; arXiv:2203.07335.
3. A. Paone, M. Paone, *Line-graph inertia of roses and generalized theta graphs*, preprint (2026-08-01), doi:10.5281/zenodo.21744051, Corollary 8.1. https://aletheia-technologies.it/en/research/line-graph-inertia-roses-generalized-theta/reader/
