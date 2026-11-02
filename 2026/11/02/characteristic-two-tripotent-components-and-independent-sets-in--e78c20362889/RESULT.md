# Characteristic-two tripotent components and independent sets in radical-square-zero quiver algebras

## Finding
Let \(Q=(V,E,s,t)\) be any finite directed multiquiver (loops, repeated arrows and isolated vertices allowed). For a field \(k\) of characteristic \(2\), set \(A=kQ/J^2\), where \(J\) is the arrow ideal. Define \(m=|E|\) and, for every \(U\subseteq V\),
\[
e_Q(U)=|\{\alpha\in E:s(\alpha),t(\alpha)\in U\}|.
\]
The reduced algebraic variety of elements satisfying \(a^3=a\) is the disjoint union of \(2^{|V|}\) geometrically irreducible affine-space components:
\[
\mathcal T(A)_{\mathrm{red}}\cong\coprod_{U\subseteq V}\mathbb A_k^{\,m-e_Q(U)}.
\]
The component indexed by \(U\) has zero vertex coefficients exactly on \(U\). The largest dimension is \(m\), and the number of components of this largest dimension is exactly the number \(i(Q)\) of vertex subsets \(U\) containing no arrow with both endpoints in \(U\). In particular, for a simple loopless graph with any chosen orientation, \(i(Q)\) is its usual independent-set count.

Over \(\mathbb F_q\) for every even prime power \(q\), the exact number of tripotents is
\[
N_Q(q)=\sum_{U\subseteq V}q^{\,m-e_Q(U)}.
\]
Thus the coefficient of \(T^m\) in \(N_Q(T)=\sum_U T^{m-e_Q(U)}\) is \(i(Q)\). This is a dimension-profile invariant, not merely a total count.

There is also an explicit conjugacy refinement. Put \(S=V\setminus U\). Let \(b(S)\) be the number of arrows with both endpoints in \(S\), and \(c(S)\) the number with exactly one endpoint in \(S\). In the \(U\)-component, the group \(1+J\) has exactly \(q^{b(S)}\) conjugacy orbits, each of size \(q^{c(S)}\), when \(k=\mathbb F_q\); over an arbitrary characteristic-two field, each orbit is an affine space of dimension \(c(S)\), parametrized by its crossing-arrow coefficients, and the internal-\(S\) coefficients label the orbits.

## Assumptions and scope
The quiver is finite, its arrow ideal is truncated at paths of length two, and the base field has characteristic two. The algebra is the finite-dimensional unital quotient \(kQ/J^2\), even if \(Q\) contains directed cycles or loops. Different arrows form distinct basis vectors. All geometric assertions concern the **reduced** variety of labelled elements, not the potentially nonreduced defining scheme. A component refers to a geometric irreducible component. No quotient by the full automorphism group is taken.

## Proof
Write every element uniquely as \(a=s+r\), where \(s=\sum_{v\in V}c_ve_v\), and \(r=\sum_{\alpha\in E}r_\alpha\alpha\in J\). Since \(J^2=0\), the vertex component of \(a^3=a\) says \(c_v^3=c_v\). In characteristic two the only roots of this equation in every field extension are \(0\) and \(1\). The coefficient of an arrow \(\alpha:u\to v\) in \(a^3-a\) is
\[
(c_u^2+c_uc_v+c_v^2-1)r_\alpha.
\]
For \(c_u,c_v\in\{0,1\}\), this coefficient forces \(r_\alpha=0\) precisely when both endpoints have coefficient zero, and imposes no condition in the other three cases. Therefore for each set \(U=\{v:c_v=0\}\), exactly \(m-e_Q(U)\) independent arrow coefficients remain. These are affine linear subspaces, and the distinct vertex-root conditions separate them as open-and-closed subsets of the reduced variety. Each is therefore a geometrically irreducible component. Because choosing \(U=\varnothing\) leaves every arrow free, the maximal dimension is \(m\); equality holds exactly when \(e_Q(U)=0\). Summing finite-field points proves the census and its leading coefficient.

For the intrinsic idempotent description, if \(a^3=a\), set \(e=a^2\) and \(n=a+a^2\). In characteristic two, \(e^2=e\), \(n^2=0\), and \(en=ne=n\). Since the semisimple quotient is a product of copies of \(k\), the image of \(a\) there is the vertex indicator of \(S=V\setminus U\); consequently \(n\in J\), and \(n=en e\in eJe\). Conversely, every idempotent \(e\) and every \(n\in eJe\) satisfy \((e+n)^2=e\) and \((e+n)^3=e+n\), because \(J^2=0\). Hence \(a\mapsto(e,n)=(a^2,a+a^2)\) is a bijective polynomial parametrization of the reduced tripotent locus by the pairs \(e^2=e\), \(n\in eJe\), with inverse \((e,n)\mapsto e+n\).

Fix \(S\). Every idempotent having quotient \(\sum_{v\in S}e_v\) has arbitrary arrow coefficients exactly on arrows crossing between \(S\) and \(U\), and zero coefficients on the other arrows, since the arrow coefficient of \(e^2-e\) is \((c_u+c_v-1)r_\alpha\). For any such idempotent, \(eJe\) has the fixed basis of arrows internal to \(S\): the identity \(eje=sjs\) for \(j\in J\) follows from \(J^2=0\). Thus the idempotent base is \(\mathbb A^{c(S)}\), its tripotent fiber is the constant vector space \(\mathbb A^{b(S)}\), and \(c(S)+b(S)=m-e_Q(U)\).

Finally, for \(h\in J\), the unit \(1+h\) has inverse \(1-h\). The conjugation action on \(a=s+r\) is
\[
(1+h)a(1-h)=s+r+hs-sh.
\]
The coefficient on \(\alpha:u\to v\) changes by \((c_v-c_u)h_\alpha\). It changes freely on crossing arrows and is fixed on arrows internal to \(S\); the internal-\(U\) coefficients already vanish for tripotents. Thus internal-\(S\) coefficients classify all \(1+J\)-orbits and each orbit has \(q^{c(S)}\) points over \(\mathbb F_q\).

For complexity, orient the edges of any finite simple undirected graph \(G\) arbitrarily to obtain \(Q_G\). Then the number of maximal-dimensional components equals the number of independent sets of \(G\), with a one-to-one correspondence \(U\leftrightarrow\) component. Counting independent sets is \(\#P\)-complete; membership in \(\#P\) for this component-counting problem follows by guessing \(U\) and checking that no edge has both endpoints in \(U\). Hence the component-count problem for the stated family is \(\#P\)-complete under parsimonious reductions. This does **not** assert hardness of a single fixed-field-size evaluation of \(N_Q(q)\).

## Verification
An independent exhaustive checker in `verify.py` constructs multiplication directly from the quiver, enumerates all coefficients in small finite fields, computes \(a^3\), and compares with the formula. It verifies twelve configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including loops, parallel arrows, a directed cycle, and a triangle. Odd-characteristic tests are auxiliary controls, not part of the claimed new theorem. It also checks that in characteristic two the internal-arrow fibers have \(q^{b(S)}\) orbits of \(q^{c(S)}\) elements for small binary cases. Run `python verify.py` from the directory containing the file. Expected final line: `TRIPOTENT_GRAPH_CENSUS_OK 12 exhaustive finite-field cases`.

For the oriented triangle with three arrows, the component dimensions are \(3\) (four components), \(2\) (three components), and \(0\) (one component). Therefore \(N_Q(2)=45\) and \(N_Q(4)=305\), and there are exactly four maximal-dimensional components, matching its four independent sets.

## Relationship to prior work
Ying, Koşan and Zhou (2016) study ring-wide decompositions into commuting tripotents and idempotents, not the distribution of **individual** tripotents in arbitrary radical-square-zero quiver algebras. Adachi (2014) and the representation-theoretic radical-square-zero literature provide the quiver-algebra setting rather than this incidence-stratified equation. General commuting-idempotent orbit formulas already imply the separable odd-characteristic analogy \(a^3=a\) by orthogonal idempotent decomposition; **that analogy is not claimed as new**. In characteristic two, commuting-idempotent sums remain idempotent, whereas nonidempotent tripotents such as \(1+r\), for nonzero \(r\in J\), are present. The new classification therefore concerns the inseparable characteristic-two case, including internal-arrow parameters invisible to an idempotent-only census. Published finite-ring tripotent counts in other families do not themselves supply the induced-edge profile for arbitrary quivers.

## Limitations
The result is a labelled element census for algebras with square-zero radical in characteristic two. It does not determine scheme nilpotent structure, conjugacy under the full unit group or all algebra automorphisms, or corresponding formulas for higher radical powers. The group-orbit assertion concerns only \(1+J\). The independent-set interpretation is for top-dimensional components of the **reduced** variety. Searches of prior work and mathematical records are not an exhaustive proof of publication priority; the decomposition into idempotent and nilpotent parts uses elementary established ring facts. No independent audit has been performed.

## References
- Z. Ying, T. Koşan, Y. Zhou, *Rings in which Every Element is a Sum of Two Tripotents*, Canadian Mathematical Bulletin 59 (2016), 661–672, DOI: 10.4153/CMB-2016-009-0; first electronic publication March 14, 2016.
- T. Adachi, *Characterizing \(\tau\)-rigid-finite algebras with radical square zero*, arXiv:1401.1438 (2014), quiver-algebra context.
- L. G. Valiant, *The Complexity of Enumeration and Reliability Problems*, SIAM Journal on Computing 8 (1979), 410–421, DOI: 10.1137/0208032 (counting-complexity context).
- L. A. Goldberg, J. Lapinskas, D. Richerby, *Faster Exponential-time Algorithms for Approximately Counting Independent Sets*, arXiv:2005.05070 (states the established exact \(\#P\)-completeness of independent-set counting).
