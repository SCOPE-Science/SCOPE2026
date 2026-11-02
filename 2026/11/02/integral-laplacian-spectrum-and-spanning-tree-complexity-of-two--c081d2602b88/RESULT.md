# Integral Laplacian spectrum and spanning-tree complexity of two-token friendship graphs

## Finding
For every integer \(m\ge 2\), let \(W_m=K_1\vee mK_2\) be the friendship graph: \(m\) edge-disjoint triangles with one common hub. The two-token graph \(T_m=F_2(W_m)\) has as vertices the unordered pairs of distinct vertices of \(W_m\); a pair is moved to another when one member slides along an edge of \(W_m\) to an unoccupied vertex.

Set \(q=\binom m2\). The complete Laplacian spectrum, with eigenvalues written before their multiplicities, is
\[
\begin{array}{c|ccccccccc}
\lambda&0&1&2&3&4&6&2m&2m+1&2m+2\\\hline
\mathrm{mult}&1&m-1&q&m&m(m-2)&q&m-1&1&m.
\end{array}
\]
When entries in the eigenvalue row coincide (for example at \(m=2\) or \(m=3\)), their multiplicities are to be added. Zero multiplicities are omitted. Thus the Laplacian is integral for every \(m\ge2\), even though the graph is nonregular.

The two-token graph has exactly \(m(2m+1)\) vertices, \(3m(2m-1)\) edges, algebraic connectivity \(1\), and spanning-tree count
\[
\boxed{\tau(T_m)=2^{3m^2-3m-1}\,3^{m+\binom m2}\,m^{m-2}(m+1)^m.}
\]
The last formula counts ordinary unweighted spanning trees.

## Assumptions and scope
All graphs are finite, simple, undirected, unweighted. The join \(K_1\vee mK_2\) has one hub adjacent to each of \(2m\) peripheral vertices; each peripheral vertex also has precisely one peripheral neighbor, its mate. Tokens are indistinguishable and may not occupy the same vertex. The combinatorial Laplacian is \(L=D-A\), with each legal undirected move contributing one exchange edge. The theorem holds for each integer \(m\ge2\); it does not describe higher-token graphs or arbitrary windmills with larger blades.

## Proof
Write \(H=mK_2\), \(n=2m\), and designate the hub by \(h\). Partition the states of \(F_2(K_1\vee H)\) into the \(n\) hub-containing states \(\{h,u\}\) and the \(\binom n2\) hub-free states \(\{u,v\}\), where \(u,v\in V(H)\). Let \(L_H\) be the Laplacian of \(H\), \(L_2\) that of \(F_2(H)\), and let \(R\) be the \(n\)-by-\(\binom n2\) unsigned vertex-pair incidence matrix, so \(R_{u,\{v,w\}}=1\) if and only if \(u\in\{v,w\}\).

A hub-containing state has \(n-1\) hub-departure moves and its available peripheral moves are those in \(H\). A hub-free state has two hub-arrival moves and its remaining transitions are those of \(F_2(H)\). Consequently the full Laplacian is exactly
\[
L=\begin{pmatrix}(n-1)I+L_H&-R\\-R^{\mathsf T}&L_2+2I\end{pmatrix}.
\]
For any graph \(H\), and any function \(f\) on \(V(H)\), the function \((R^{\mathsf T}f)(\{u,v\})=f(u)+f(v)\) obeys \(L_2R^{\mathsf T}f=R^{\mathsf T}L_Hf\): each permitted move changes one of the two summands, while terms corresponding to an occupied neighbor cancel in pairs. Hence \(RL_2=L_HR\). We also have \(RR^{\mathsf T}=(n-2)I+J\), which is strictly positive definite for \(n\ge4\). Therefore the hub-free space splits orthogonally into \(\operatorname{im}R^{\mathsf T}\) and \(\ker R\), both invariant under \(L_2\).

Now \(L_H\) has eigenvalue \(0\) with multiplicity \(m\) and eigenvalue \(2\) with multiplicity \(m\). Its \(0\)-eigenspace contains the one-dimensional all-ones vector and its \((m-1)\)-dimensional orthogonal complement; every \(2\)-eigenvector is orthogonal to the all-ones vector. On a normalized matching pair of a hub-containing vector and its image under \(R^{\mathsf T}\), the block above restricts to
\[
M_{\alpha,s}=\begin{pmatrix}n-1+\alpha&-s\\-s&2+\alpha\end{pmatrix},
\]
where \(\alpha\in\{0,2\}\) is its \(L_H\)-eigenvalue and \(s^2\) is its \(RR^{\mathsf T}\)-eigenvalue. For the all-ones direction, \((\alpha,s^2)=(0,2(n-1))\), giving eigenvalues \(0,n+1\). For the other \(m-1\) zero-eigenvectors, \((\alpha,s^2)=(0,n-2)\), giving \(1,n\). For the \(m\) two-eigenvectors, \((\alpha,s^2)=(2,n-2)\), giving \(3,n+2\).

For the remaining part, \(F_2(H)\) is a disjoint union of \(m\) isolated configurations \(\{a_i,b_i\}\) and \(q=\binom m2\) copies of the four-cycle (one for each pair of distinct blades). Thus \(L_2\) has eigenspaces of eigenvalues \(0,2,4\), with dimensions \(m+q,2q,q\), respectively. The intertwining relation and injectivity of \(R^{\mathsf T}\) show that \(R\) maps the first two eigenspaces onto the \(m\)-dimensional \(0\)- and \(2\)-eigenspaces of \(L_H\), while it vanishes on the \(4\)-eigenspace. Therefore the dimensions of their intersections with \(\ker R\) are \(q,2q-m=m(m-2),q\), respectively. On \(\ker R\), the full Laplacian acts as \(L_2+2I\), giving \(2^q,4^{m(m-2)},6^q\). Adding the paired-block contributions proves the displayed entire spectrum. The multiplicities sum to \(m(2m+1)\), including \(m=2\) and all coincidences.

The base graph has \(2m+1\) vertices and \(3m\) edges. Each base edge supports exactly \(2m-1\) two-token edges, accounting for \(3m(2m-1)\) edges. The single zero eigenvalue proves connectivity. Kirchhoff's matrix-tree theorem states that the number of spanning trees equals the product of all nonzero Laplacian eigenvalues divided by the number \(m(2m+1)\) of vertices. Substituting the above multiset gives
\[
\frac{2^q3^m4^{m(m-2)}6^q(2m)^{m-1}(2m+1)(2m+2)^m}{m(2m+1)}
=2^{3m^2-3m-1}3^{m+q}m^{m-2}(m+1)^m.
\]
For \(m\ge2\), a state using both endpoints of a single peripheral edge has degree \(2\); a state using the hub has degree \(2m\); a state using peripheral vertices from different blades has degree \(4\). At least two degrees differ, so \(T_m\) is nonregular. The smallest positive eigenvalue is \(1\).

## Verification
Run `python verify_exact.py` with SymPy. This constructs every token move directly from the base edge list and compares its integer characteristic polynomial with the proposed factorization for \(2\le m\le8\). It independently computes exact matrix-tree cofactors for \(m=2,3,4\), giving respectively \(7776\), \(18345885696\), and \(20289081908920320000\) spanning trees.

Compile and run `verify_modular.cpp` with a C++17 compiler. This separately reconstructs the graph, checks each distinct proposed eigenvalue's multiplicity as a modular nullity over \(\mathbb F_{1000000007}\), and checks a modular matrix-tree cofactor for \(2\le m\le9\). Modular checks are consistency tests, not a proof of real spectral multiplicity, and finite checks do not establish the infinite theorem. The preceding block decomposition supplies the proof for every parameter.

## Relationship to prior work
Audenaert, Godsil, Royle and Rudolph (first available in 2005) introduced the symmetric-power spectral viewpoint and established general construction and cospectrality results, particularly for strongly regular graphs. Fabila-Monroy and collaborators (2009) introduced the token-graph language and basic configuration properties. Dalfó and collaborators (2020) proved the general Laplacian intertwining/inclusion theorem, which is used and credited here; it does not itself specify the eigenspaces left over after lifting. Reyes and collaborators (2023) gave spectral methods for cycle token graphs and connectivity for other families. The present result resolves the previously unspecified residual eigenspaces for the nonregular family \(K_1\vee mK_2\), and evaluates its complete spectrum and tree count.

## Limitations
The theorem concerns only two indistinguishable tokens and friendship graphs with at least two triangular blades. It is a mathematical derivation with independent finite computational corroboration, not an independent scholarly audit. A comprehensive proof of absence from every publication or database is not possible; an equivalent result under other terminology may exist. Coincident eigenvalues must be combined, as explicitly stated.

## References
1. K. Audenaert, C. Godsil, G. Royle and T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251 (first posted 2005-07-12), later J. Combin. Theory Ser. B 97 (2007), 74–90. https://arxiv.org/abs/math/0507251
2. R. Fabila-Monroy et al., *Token Graphs*, arXiv:0910.4774 (first posted 2009-10-25), later Graphs Combin. 28 (2012), 365–380. https://arxiv.org/abs/0910.4774
3. C. Dalfó et al., *On the Laplacian spectra of token graphs*, arXiv:2012.00808 (first posted 2020-12-01). https://arxiv.org/abs/2012.00808
4. M. A. Reyes et al., *On the spectra of token graphs of cycles and other graphs*, arXiv:2309.07089 (first posted 2023-09-13). https://arxiv.org/abs/2309.07089
5. M. A. Reyes, C. Dalfó and M. A. Fiol, *On the spectra and spectral radii of token graphs*, arXiv:2310.16929 (first posted 2023-10-25). https://arxiv.org/html/2310.16929v1
