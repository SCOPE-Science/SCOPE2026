# Square-zero commuting graphs for the five modular group algebras of order eight

## Finding
Let \(k=\mathbb F_q\), \(q=2^f\), \(f\geq1\). For each of the five groups \(G\) of order eight, put \(Z_G=\{x\in kG:x^2=0\}\). Form the simple undirected graph \(\mathcal C_G\) with vertex set \(Z_G\) and edges between distinct commuting elements. Then the complete graph-isomorphism classification is
\[
\begin{array}{c|c}
G&\mathcal C_G\\\hline
C_8&K_{q^4}\\
C_4\times C_2&K_{q^6}\\
C_2^3&K_{q^7}\\
Q_8&K_{q^4}\\
D_8&K_{q^5}\cup_{K_{q^4}}K_{q^5}.
\end{array}
\]
Here the last expression means two complete graphs identified along one common induced clique; there are no edges between their disjoint complements. The latter graph has \((2q-1)q^4\) vertices, precisely \((2q^2-1)q^8\) ordered commuting pairs (including equal pairs), clique number \(q^5\), and exactly \(2(q-1)^2q^8\) ordered noncommuting pairs. The complement induced on the noncentral square-zero vertices is \(K_{(q-1)q^4,(q-1)q^4}\). Every noncentral square-zero element of \(kD_8\) has conjugacy orbit of cardinality \(q^2\) under \((kD_8)^\times\), while each central square-zero element has a singleton orbit; there are \(q^4+2(q-1)q^2\) such orbits in total.

## Assumptions and scope
The group \(D_8\) has presentation \(\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), and \(Q_8=\{\pm1,\pm i,\pm j,\pm ij\}\) denotes the quaternion group. Products, commutators and conjugation are taken in the full associative group algebra, not in the underlying finite group. The graph has no loops, but ordered commuting-pair counts include equal pairs. The result holds over every finite field of characteristic two, and the structural clique decomposition remains true over any field of characteristic two with cardinal quantities replaced by affine-space families.

## Proof
For any central element \(z\) of order two in a characteristic-two group algebra, write \(t=1+z\), so \(t^2=0\). For either \(D_8\) or \(Q_8\), the center contains \(z\) and its quotient by \(\langle z\rangle\) is \(C_2^2\). Choose representatives \(1,u,v,uv\); the eight group elements decompose into those representatives and their multiples by \(z\). Thus each algebra element is uniquely \(A+tB\), with \(A,B\) in the four-dimensional span of these representatives. The group commutator ideal lies in \(tkG\), hence \(tkG\) is central, \((tkG)^2=0\), and \((A+tB)^2=A^2\).

For \(D_8\), choose \(u=r\), \(v=s\), and write \(A=a_0+a_1r+a_2s+a_3rs\). Put \(S=a_0+a_1+a_2+a_3\). Direct expansion using \(srs=r^{-1}\) gives
\[
A^2=S^2+t(a_1^2+a_1a_2rs+a_1a_3s+a_2a_3r).
\]
The four vectors \(t,tr,ts,trs\) are linearly independent. Since \(k\) is a field, \(A^2=0\) is equivalent to \(S=0\), \(a_1=0\) and \(a_2a_3=0\). Consequently the square-zero locus is precisely the union
\[
Z_{D_8}=\bigl(tkD_8+k(1+s)\bigr)\ \cup\ \bigl(tkD_8+k(1+rs)\bigr).
\]
Both subspaces have dimension five and their common intersection is the four-dimensional central subspace \(tkD_8\). Furthermore
\[
[1+s,1+rs]=srs-r=(r^{-1}-r)=t\,r^{-1}\ne0.
\]
Commutators with \(tkD_8\) vanish. Therefore every pair of elements of the same subspace commutes, whereas a pair from their respective complements does not commute. This proves the clique amalgamation and its pair-count formulas. The noncommuting complements each have \((q-1)q^4\) elements.

For an element \(x\) in either noncentral subspace, its adjoint linear map \(y\mapsto[x,y]\) has rank two: up to a nonzero scalar, the two independent nonzero images of the coset representatives lie in the span of \(tr\) and \(trs\). Thus the centralizer subspace in the eight-dimensional algebra has dimension six. Since the group algebra of a finite \(2\)-group is local, an element is invertible if and only if it has nonzero augmentation. The centralizer subspace contains \(1\), so its unit group has \((q-1)q^5\) members; the full unit group has \((q-1)q^7\) members. Orbit–stabilizer gives \(q^2\) for each noncentral conjugacy orbit. All \(q^4\) elements of \(tkD_8\) are central, giving the claimed orbit count.

For \(Q_8\), the same decomposition has each of \(u,v,uv\) squaring to \(z\). The coefficient of \(t\) in \(A^2\) contains \(a_1^2+a_2^2+a_3^2\), while the other three independent coefficients are \(a_1a_2,a_1a_3,a_2a_3\). Together with \(S=0\), these force \(a_1=a_2=a_3=a_0=0\). Hence \(Z_{Q_8}=tkQ_8\), a central four-dimensional subspace.

The three abelian groups have commutative group algebras, so their square-zero commuting graphs are complete. Their square-zero dimensions follow directly by Frobenius squaring in the standard truncated polynomial presentations: \(k[C_8]\cong k[X]/(X^8)\), \(k[C_4\times C_2]\cong k[X,Y]/(X^4,Y^2)\), and \(k[C_2^3]\cong k[X,Y,Z]/(X^2,Y^2,Z^2)\). The square-zero coefficient conditions leave respectively four, six and seven free coordinates.

## Verification
The included standalone `verify.py` constructs the eight-element multiplication table independently for each group and checks every element in \(\mathbb F_2G\) and \(\mathbb F_4G\) for square-zero. It confirms all ten cardinalities (five groups times two fields). It then exhausts all pairs of square-zero elements for \(D_8\) and \(Q_8\) over \(\mathbb F_2\), obtaining respectively \(1792\) and \(256\) commuting ordered pairs. Finally it enumerates all conjugacy orbits of square-zero elements under the \(128\) units of \(\mathbb F_2D_8\), finding sixteen singleton and eight four-element orbits. Invoke with `python3 verify.py`; success ends with `ORDER8_GROUP_ALGEBRA_SQZERO_OK`. These finite checks corroborate, but do not establish, the uniform assertions for arbitrary \(q\).

## Relationship to prior work
Creedon and Gildea describe the unit group of the characteristic-two algebra \(\mathbb F_q[D_8]\), providing relevant group-algebra structure; their paper does not state this square-zero commuting-graph classification. Classical and existing square-zero rank enumerations already determine the sizes of the square-zero sets and some left-multiplication rank spectra; those one-element invariants are not the claimed contribution and do not by themselves specify which pairs commute. The present claim is specifically about the induced commuting relation and unit-conjugacy orbit sizes among square-zero elements, uniformly across the five order-eight groups.

## Limitations
The theorem concerns order-eight group algebras over characteristic-two fields only, and graph vertices include zero and all central square-zero elements. It does not assert a classification for larger dihedral or quaternion groups or for higher nilpotency indices. Accessible primary literature is not an exhaustive priority search, and independent mathematical validation has not been performed.

## References
- L. Creedon and J. Gildea, “The Structure of the Unit Group of the Group Algebra \(\mathbb F_{2^k}D_8\),” *Canadian Mathematical Bulletin* **54** (2011), 237–243, DOI:10.4153/CMB-2010-098-5 (available electronic source dated 2010-08-26).
- L. Creedon and J. Gildea, “Unitary Units of the Group Algebra \(\mathbb F_{2^k}Q_8\),” *International Journal of Algebra and Computation* **19** (2009), 283–286, DOI:10.1142/S0218196709005081.
