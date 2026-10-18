# Integral symmetry lattice of the Morse complex of \(K_{2,n}\)
## Finding
For every integer \(n\ge3\), let \(X_n=\mathcal M(K_{2,n})\) be the ordinary simplicial complex of acyclic discrete vector fields on the graph \(K_{2,n}\). Its natural automorphism group is \(G_n=S_n\times C_2\), with \(S_n\) permuting leaves and \(C_2=\langle\tau\rangle\) swapping the two hubs.

Let \(A_n=\{(a_1,\ldots,a_n)\in\mathbb Z^n:\sum_i a_i=0\}\), with the natural integral leaf-permutation action, and let \(B_n=\bigoplus_{i\ne j}\mathbb Z b_{ij}\), with leaf permutations acting by \(\sigma b_{ij}=b_{\sigma(i),\sigma(j)}\). Then there is an integral \(G_n\)-module isomorphism
\[
\widetilde H_n(X_n;\mathbb Z)\;\cong\;\operatorname{sgn}_{S_n}\otimes_\mathbb Z (A_n\oplus B_n),
\]
where on the module inside the parentheses the hub interchange acts by
\[
\tau a=(-1)^n a\quad(a\in A_n),\qquad
\tau b_{ij}=(-1)^{n+1}b_{ji}.
\]
The sign tensor factor is trivial under hub interchange. This is an explicit classification over \(\mathbb Z\), not just over \(\mathbb Q\). It has rank \(n^2-1\), agreeing with the previously known nonequivariant sphere-wedge theorem and rational equivariant character.

The integral information is substantive: the natural exact sequence \(0\to A_n\to\mathbb Z^n\xrightarrow{\sum}\mathbb Z\to0\) does not split as an integral \(S_n\)-module for \(n\ge2\). Indeed, every invariant integral vector is constant, so its coordinate sum is divisible by \(n\). Moreover, after reduction modulo a prime \(p\), the augmentation lattice has a nonzero invariant line exactly when \(p\mid n\).

## Assumptions and scope
Write the graph vertices as hubs \(a,b\) and leaves \(v_1,\ldots,v_n\). An elementary discrete vector-field flag \((u,uv)\) is encoded by an arrow \(u\to v\); a simplex is a partial collection in which each vertex has at most one outgoing arrow, each undirected edge is used at most once, and there are no directed cycles. Put \(x_i:a\to v_i\), \(y_i:b\to v_i\), \(p_i:v_i\to a\), and \(q_i:v_i\to b\). Let \(P_i=\{p_i,q_i\}\) be the two-point simplicial complex. Simplicial joins are denoted by \(*\). All homology is reduced and integral. The group acts by graph automorphisms on flags, with the induced orientation signs on chains.

## Proof
**1. A one-hub skeleton.** Let \(X_0=*_{i=1}^nP_i\cong S^{n-1}\) be the subcomplex with no hub-outgoing flags. Form \(Y\subset X_n\) by adjoining every simplex containing at most one of the flags \(x_i,y_j\). The link of \(x_i\) in \(X_0\) equals \(q_i*_{k\ne i}P_k\), and the link of \(y_i\) equals \(p_i*_{k\ne i}P_k\). Each is contractible. Successively adjoining cones on these contractible links proves that \(X_0\hookrightarrow Y\) is a homotopy equivalence. Under leaf permutations, the fundamental homology generator of the join of \(n\) oriented zero-spheres has character \(\operatorname{sgn}(\sigma)\); under simultaneous interchange \(p_i\leftrightarrow q_i\), it acquires \((-1)^n\). Consequently \(\widetilde H_{n-1}(Y;\mathbb Z)\cong\mathbb Z\) with character \(\operatorname{sgn}(\sigma)(-1)^{ne}\) at \((\sigma,\tau^e)\).

**2. Every two-hub cell is an attached ball.** For each ordered \((i,j)\), the link in \(X_0\) of the permitted edge \([x_i,y_j]\) is
\[
L_{ii}=*_{k\ne i}P_k\cong S^{n-2},\qquad
L_{ij}=\{q_i,p_j\}*_{k\notin\{i,j\}}P_k\cong S^{n-2}\quad(i\ne j).
\]
In the off-diagonal case, \(\{q_i,p_j\}\) is two *isolated* vertices: choosing both would create the directed cycle \(a\to v_i\to b\to v_j\to a\). The full subcomplex \([x_i,y_j]*L_{ij}\) is a closed \(n\)-ball whose attaching sphere is \(\partial[x_i,y_j]*L_{ij}\subset Y\). Distinct interiors are disjoint. Thus
\[
H_n(X_n,Y;\mathbb Z)=\bigoplus_{i,j}\mathbb Z e_{ij},
\]
and the other relative homology groups vanish.

**3. Exact integral attaching degrees.** For \(i\ne j\), the attaching sphere bounds within \(Y\): the join \(M_{ij}=[q_i,p_j]*_{k\notin\{i,j\}}P_k\) is a ball, and both \(x_i*M_{ij}\) and \(y_j*M_{ij}\) belong to \(Y\). Their union fills \(\partial[x_i,y_j]*L_{ij}\). Therefore \(\partial e_{ij}=0\) for off-diagonal pairs. For \(i=j\), restrict to the four flags \(p_i,q_i,x_i,y_i\) together with \(*_{k\ne i}P_k\). Before adding the edge \([x_i,y_i]\), the first factor is two disjoint edges, homotopy equivalent to \(S^0\); after adding it, the first factor becomes a four-vertex path, hence is contractible. Its sole \(n\)-cell attachment has degree \(\pm1\) onto \(\widetilde H_{n-1}(Y)\). Leaf symmetry allows coherent orientation choices with \(\partial e_{ii}=1\) for every \(i\). Therefore the long exact sequence of the pair identifies
\[
\widetilde H_n(X_n;\mathbb Z)=\ker\left(\bigoplus_{i,j}\mathbb Z e_{ij}\xrightarrow{\partial}\mathbb Z\right),\qquad
\partial e_{ij}=\begin{cases}1&i=j,\\0&i\ne j.\end{cases}
\]
This kernel is exactly the sum of the diagonal augmentation lattice and the off-diagonal free lattice, integrally and as a direct sum of invariant subgroups.

**4. All integral orientation characters.** Orient the join factors by choosing \([p_k]-[q_k]\); permuting these factors has the leaf sign \(\operatorname{sgn}(\sigma)\). On the diagonal relative cells the hub swap acts by \((-1)^n\), forced also by equivariance of their unit boundary. For an off-diagonal pair, compose the hub swap with the transposition \((i\ j)\): this fixes the indexed relative ball and acts by \((-1)^n\) on its orientation, from swapping the two hub vertices, swapping the distinguished zero-sphere factors, and reversing the other \(n-2\) zero-sphere factors. Since the leaf transposition contributes its sign \(-1\), hub swap alone sends the orientation at \((i,j)\) to \((-1)^{n+1}\) times that at \((j,i)\). Coherently sign-normalized relative cell generators therefore yield precisely the action in the finding, proving an integral lattice isomorphism for every \(n\ge3\).

## Verification
The self-contained program `verify_integral_action.py` builds the integral oriented relative cycles as signed sums of simplices, applies all permutations of \(n\) leaves and both hub automorphisms for \(2\le n\le5\), and checks every coefficient and the stated normalized action. It also checks that relative link chains have the claimed combinatorial supports. Running `python3 verify_integral_action.py` gives `VERIFY_OK` for each tested \(n\). These exact finite tests check orientation conventions; the all-parameter proof is the preceding join, relative-homology and stabilizer argument.

## Relationship to prior work
Scoville and Zaremsky establish a structural connectivity framework for Morse complexes. An existing uniform theorem determines the nonequivariant wedge \(X_n\simeq\bigvee^{n^2-1}S^n\). A separately published equivariant Euler-character calculation determines the rational \(S_n\times C_2\)-character and decomposes its eigenspaces over \(\mathbb Q\), but explicitly does not classify integral \(\mathbb Z[S_n\times C_2]\)-lattices. The present construction computes the latter via an integral relative-cell model, and recovers the known rational character after extension of scalars. It neither reclaims the sphere-wedge result nor reclaims the rational character formula.

## Limitations
The statement is about ordinary graph Morse complexes of the two-hub complete bipartite family and their integral homology representations, not an equivariant homotopy equivalence or all complete bipartite graphs. Integral module equivalence is stronger than character agreement but does not by itself classify equivariant homotopy types. Equivalent unpublished integral models remain a bibliographic risk. No independent external mathematical audit has been performed.

## References
1. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907, first public 2019-04-24.
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first public 2020-04-22.
3. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first public 2022-07-27.
4. *The Morse complex of \(K_{2,n}\) is a wedge of \(n^2-1\) \(n\)-spheres*, publicly indexed mathematical result, 2026.
5. *Full equivariant Euler character of the \(K_{2,n}\) Morse complex*, publicly indexed mathematical result, 2026.
