# Five induced quintic tori for the sixteen-line boundary of a quartic del Pezzo surface

## Finding
Let \(k=\mathbb F_q\) be **any** finite field, and let \(S/k\) be a smooth degree-four del Pezzo surface. Suppose that Frobenius on the sixteen geometric \((-1)\)-curves has the conjugacy type of an ordinary five-cycle in \(W(D_5)\). Let \(D\subset S\) be the reduced union of all sixteen curves, and put \(U=S\setminus D\). Then \(D\) is a connected nodal curve of arithmetic genus \(25\), and its identity-component Picard scheme has the following **integral**, rather than merely isogeny-theoretic, description:

\[
\boxed{\operatorname{Pic}^{0}_{D/k}\;\cong\;
\left(\operatorname{Res}_{\mathbb F_{q^5}/\mathbb F_q}\mathbb G_m\right)^{5}.}
\]

In particular, as a finite abelian group,
\[
\boxed{\operatorname{Pic}^{0}_{D/k}(k)\cong
\left(\mathbb F_{q^5}^{\times}\right)^5\cong C_{q^5-1}^{\,5}.}
\]

With \(T\) a formal zeta variable, the complete rational zeta functions are
\[
\boxed{Z(D,T)=\frac{(1-T^5)^5}{(1-T)(1-qT)(1-q^5T^5)^3},\qquad
Z(U,T)=\frac{(1-q^5T^5)^2}{(1-q^2T)(1-T^5)^5}.}
\]

There is also an identity in the Grothendieck ring of varieties over \(k\). Write \(\mathbb L=[\mathbb A^1_k]\) and \(a=[\operatorname{Spec}\mathbb F_{q^5}]\). Then
\[
\boxed{[U]=\mathbb L^2+(5-2\mathbb L)a\quad\text{in }K_0(\operatorname{Var}_k).}
\]

For every positive integer \(n\), these formulas give
\[
\#U(\mathbb F_{q^n})=
\begin{cases}
q^{2n},&5\nmid n,\\
(q^n-5)^2,&5\mid n.
\end{cases}
\]

The theorem is nonvacuous for **every** finite field, including characteristic two: blow up \(\mathbb P^2_k\) in any closed point of degree five lying on a smooth \(k\)-conic. In characteristic different from two, the hypothesis is equivalently that the degree-five discriminant of the pencil of quadrics defining \(S\) is irreducible over \(k\).

## Assumptions and scope
A degree-four del Pezzo surface is a smooth projective surface with ample anticanonical bundle of self-intersection \(4\). Its geometric model is \(\operatorname{Bl}_{p_0,\ldots,p_4}\mathbb P^2\) for five points in general position. Its sixteen exceptional curves have classes
\[
E_i\quad(0\le i\le4),\qquad L_{ij}=H-E_i-E_j\quad(0\le i<j\le4),\qquad Q=2H-\sum_{i=0}^4 E_i.
\]
They meet transversely with no triple intersection. Their forty geometric intersection points are precisely
\[
Q\cap E_i\ (5),\qquad E_i\cap L_{ij}\ (20),\qquad
L_{ij}\cap L_{kl}\text{ with }\{i,j\}\cap\{k,l\}=\varnothing\ (15).
\]
The dual graph \(\Gamma\) therefore has \(16\) vertices and \(40\) edges. The Frobenius hypothesis means the element of \(W(D_5)\cong (\mathbb Z/2)^4\rtimes S_5\) is conjugate to \((0\;1\;2\;3\;4)\) acting on the five blowup labels. It is a condition on the Galois action, not on arbitrary chosen equations. The extension-field and motivic conclusions refer to the **reduced union of all geometric exceptional curves**, not only the curves individually defined over \(k\).

## Proof
**1. The five-cycle has a single relevant Weyl class.** The Weyl group of type \(D_5\) is the group of even signed permutations of five symbols. If its permutation part is the five-cycle \(\sigma\), an even sign vector lies in the four-dimensional even-parity subspace \(V\subset\mathbb F_2^5\). The linear map \(1+\sigma:V\to V\) has trivial kernel: a \(\sigma\)-fixed vector is constant, and the only constant vector of even parity in five coordinates is zero. Thus \(1+\sigma\) is bijective and the sign vector is removed by conjugation inside \(W(D_5)\). The action on all sixteen curves can therefore be computed in the displayed blowup labeling. In particular, Frobenius fixes \(Q\), cycles the five \(E_i\), and has two length-five orbits on the ten \(L_{ij}\).

**2. The nodal graph and a Frobenius-invariant integral spanning tree.** Index the five labels modulo five, and put \(A_i=L_{i,i+1}\) and \(B_i=L_{i,i+2}\). The following fifteen graph edges form a tree on the sixteen vertices:
\[
\{Q,E_i\},\qquad\{E_i,A_i\},\qquad\{E_i,B_i\},\qquad i\in\mathbb Z/5.
\]
Every vertex other than \(Q\) has exactly one edge pointing toward \(Q\), so the graph is connected and the listed edges contain no cycle. This tree is invariant under simultaneous cyclic permutation of the indices. The complement in the forty-edge graph has twenty-five edges in five free length-five Frobenius orbits. For each edge outside the tree, adjoining its unique path in the tree gives an integral fundamental cycle. These twenty-five cycles form a \(\mathbb Z\)-basis of \(H_1(\Gamma,\mathbb Z)\). Since the tree is Frobenius invariant, orienting one edge from each free orbit and transporting that orientation by Frobenius makes their fundamental cycles permute in five regular blocks. Therefore
\[
\boxed{H_1(\Gamma,\mathbb Z)\cong\mathbb Z[C_5]^{\oplus5}}
\]
**as an integral Galois module**, with no passage to rational coefficients.

**3. The connected Picard scheme.** The normalization of \(D\) is the disjoint union of sixteen geometric \(\mathbb P^1\)'s. Hence its connected Picard variety is trivial, while the normalization/gluing exact sequence for ordinary double points identifies the character lattice of \(\operatorname{Pic}^0_{D/k}\) with \(H_1(\Gamma,\mathbb Z)\). The preceding integral permutation-module decomposition is precisely the character lattice of five copies of \(\operatorname{Res}_{\mathbb F_{q^5}/k}\mathbb G_m\). This proves the claimed **isomorphism of algebraic tori** and its rational group structure. Since the graph is connected, \(p_a(D)=40-16+1=25\).

**4. Orbit counts and zeta functions.** Frobenius has component-orbit lengths \(1,5,5,5\). Every one of the forty nodes has orbit length five, giving eight degree-five node orbits; every one of the eighty normalization branches has orbit length five, giving sixteen degree-five branch orbits. For the normalization \(\nu:\widetilde D\to D\), closed-point additivity gives
\[
Z(D,T)=Z(\widetilde D,T)\frac{Z(\operatorname{Sing}D,T)}{Z(\nu^{-1}\operatorname{Sing}D,T)}.
\]
Substituting the stated component, node and branch orbit data yields the displayed formula for \(Z(D,T)\).

**5. The motivic complement and its zeta function.** The Frobenius-invariant collection of five disjoint curves \(E_i\) contracts over \(k\) to a degree-nine del Pezzo surface. Every degree-nine del Pezzo surface over a finite field is \(\mathbb P^2\), since its Brauer group vanishes. Its contracted centre is a closed point of degree five. The blowup formula in \(K_0(\operatorname{Var}_k)\) gives
\[
[S]=[\mathbb P^2]+\mathbb L a=1+\mathbb L+\mathbb L^2+\mathbb L a.
\]
The normalization and node correction give
\[
[D]=(1+\mathbb L)+3(1+\mathbb L)a-16a+8a
=1+\mathbb L+(3\mathbb L-5)a.
\]
Subtracting proves the motivic identity for \([U]\). Taking rational points over finite extensions produces the piecewise point counts and the displayed zeta function of \(U\). In particular \(\#U(k)=q^2\); this first-field count was already implicit in earlier finite-field blowup constructions and is **not** claimed as the new part of the result.

**6. Existence for every finite field.** On the smooth conic \(XZ=Y^2\) take the five distinct Frobenius conjugates of \((t^2:t:1)\), where \(t\in\mathbb F_{q^5}\setminus\mathbb F_q\). Since five is prime, the closed orbit has degree five. A line meets the smooth conic in at most two geometric points, so the five points are in general position. Their blowup has the required five-cycle action. In odd characteristic, the equivalence to irreducibility of the discriminant quintic follows from the standard projection \(W(D_5)\to S_5\) acting on the five singular quadrics in the pencil, together with Step 1.

## Verification
Run `python3 verify.py` using only the Python standard library. The script reconstructs all sixteen exceptional curves as combinatorial vertices, checks the forty incidence edges and that the graph is triangle-free and five-regular, verifies all vertex/node/branch orbits, constructs the invariant fifteen-edge tree, and checks the twenty-five fundamental cycles as exact oriented integral one-chains. It independently realizes the graph inside the even half-cube and checks that every even-signed lift of a five-cycle is conjugate to the ordinary one. It also checks the point-count and motivic-specialization formulas for six values of \(q\) and extension degrees \(1\) through \(20\). The saved output ends in `VERIFY_OK`.

These finite checks support the proof but do not themselves establish an assertion for all finite fields. The all-field conclusions follow from the graph, Galois-module, blowdown, and normalization arguments above.

## Relationship to prior work
Hassett, Kresch and Tschinkel (2013) give the moduli construction, exceptional-curve geometry and signed-permutation action on the five singular quadrics of the degree-four del Pezzo surface. Banwait, Fité and Loughran (2016) provide arithmetic Frobenius-trace constructions; their Section 3 already uses a degree-five point on a conic, from which the first-field count \(\#U(k)=q^2\) follows. The first-field count is therefore **prior-implied**, rather than an originality claim. Rybakov's earlier work studies zeta functions of the ambient degree-four del Pezzo surface. Standard normalization theory identifies the generalized Jacobian of a nodal rational curve with the torus of its integral dual-graph cycle lattice.

A previous evaluation of all eighteen Weyl types for rational points outside the sixteen exceptional curves also covers the point-count part after extending scalars. A separate evaluation of integral Picard tori for the ten-curve boundary of degree-five del Pezzo surfaces concerns a *different* boundary graph (Petersen instead of the present sixteen-vertex graph). Published work on integral homology of the complex sixteen-line complement concerns ordinary homology of the open surface, not this arithmetic connected Picard scheme. The evaluated contribution here is the **integral** \(C_5\)-module decomposition of the genus-twenty-five curve's cycle lattice and hence the exact induced-torus isomorphism for the naturally irreducible-quintic Frobenius regime. No directly equivalent arithmetic torus classification was located in the inspected material.

## Limitations
The torus formula is asserted for one natural Frobenius class, not for all eighteen conjugacy classes of \(W(D_5)\). It describes the identity component of the Picard scheme of the reduced nodal curve, not the possibly disconnected full Picard scheme of all multidegrees. The group isomorphism is noncanonical; it depends on choices of an invariant blowdown and graph cycles. The direct geometric construction works in all characteristics, whereas the discriminant-quintic equivalence is claimed only in odd characteristic. General normalization theory and earlier finite-field point-count results supply substantial prior ingredients, and historical priority for the evaluated torus remains provisional. No independent mathematical audit has been performed.

## References
1. B. Hassett, A. Kresch and Y. Tschinkel, *On the moduli of degree 4 Del Pezzo surfaces*, arXiv:1312.6734v1, first public 2013-12-24; especially Sections 4 and 8.
2. B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300v1, first public 2016-06-01; especially Sections 2 and 3.
3. S. Yu. Rybakov, *Zeta functions of conic bundles and Del Pezzo surfaces of degree 4 over finite fields*, Moscow Mathematical Journal 5 (2005), 919–926, DOI:10.17323/1609-4514-2005-5-4-919-926.
4. *Integral homology of the five-point parabolic very-stable surface*, published published-finding corpus mathematical record, identifier `2026/10/4/SCOPE-integral-homology-of-the-five-point-parabolic-very-stable-surfac--7a46e6c434a8` (comparison of objects and implications only).
