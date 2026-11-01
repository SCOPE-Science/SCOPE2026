# Klein-four homology characters of even ladder dominance complexes

## Finding
For every even integer \(n\ge4\), the full rational homology character of the natural four-element symmetry group of the dominance complex of the ladder \(L_n=P_n\square K_2\) is explicitly determined. Let \(s(i,a)=(i,1-a)\) exchange layers, \(r(i,a)=(n-1-i,a)\) reverse the path, and \(V=\langle r,s\rangle\cong C_2\times C_2\). Write \(X_n=\mathcal D(L_n)\), where a face is a vertex subset whose complement is a dominating set. The only nonzero reduced rational homology is \(\widetilde H_{n-1}(X_n;\mathbb Q)\), of dimension \(n+1\), and the ordered character on \((1,s,r,rs)\) is
\[
\chi_n=\begin{cases}
(4m+1,\ 1,\ 2m+1,\ 2m+1),&n=4m\quad(m\ge1),\\
(4m+3,\ -1,\ -(2m+1),\ -(2m+1)),&n=4m+2\quad(m\ge1).
\end{cases}
\]
Equivalently, for the four one-dimensional characters \(\epsilon_{ab}\) with \(\epsilon_{ab}(s)=a\) and \(\epsilon_{ab}(r)=b\), the multiplicities in the order \((\epsilon_{++},\epsilon_{+-},\epsilon_{-+},\epsilon_{--})\) are
\[
\begin{cases}
(2m+1,0,m,m),&n=4m,\\
(0,2m+1,m+1,m+1),&n=4m+2.
\end{cases}
\]
In particular, the rational quotient \(X_n/V\) has reduced homology only in degree \(n-1\), of rank \(n/2+1\) for \(n\equiv0\pmod4\), and no reduced rational homology for \(n\equiv2\pmod4\). This last statement is about rational homology, not contractibility.

## Assumptions and scope
The graph is the ordinary Cartesian product of the length-\((n-1)\) path on vertices \(0,\ldots,n-1\) and a two-vertex edge on \(\{0,1\}\). Its edges are the vertical rungs and the two horizontal paths. All groups act simplicially by permuting these \(2n\) graph vertices. The dominance complex includes the empty face and excludes every vertex subset containing an entire closed neighborhood of a graph vertex. The theorem concerns even \(n\ge4\), ordinary homology over \(\mathbb Q\), and the subgroup \(V\) (the full graph automorphism group when \(n\ge4\)). No integral group-lattice classification is claimed.

## Proof
**Homological degree and dimension.** Thapper's matching-tree computation for the four-wide cylinder gives \(\mathcal I(P_n\square C_4)\simeq\bigvee^{n+1}S^{n-1}\) when \(n\) is even (Proposition 3.3 of the cited paper). The graph construction and suspension equivalence in Matsushita–Wakatsuki identify \(\Sigma\mathcal D(L_n)^\vee\simeq\mathcal I(P_n\square C_4)\), where \((\cdot)^\vee\) denotes the combinatorial Alexander dual on the \(2n\) vertices of \(L_n\). Combinatorial Alexander duality gives
\[
\widetilde H_i(\mathcal D(L_n);\mathbb Z)\cong\widetilde H^{2n-i-3}(\mathcal D(L_n)^\vee;\mathbb Z).
\]
Thus it vanishes outside \(i=n-1\), where it is free of rank \(n+1\). This degree follows directly from the duality shift and does not require a separate homotopy claim about \(\mathcal D(L_n)\).

**Reduced Lefschetz trace.** If \(g\) is a simplicial automorphism and \(\sigma\) a \(g\)-invariant face, its contribution to the reduced simplicial Lefschetz number is \((-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)=-(-1)^{o_g(\sigma)}\), where \(o_g(\sigma)\) counts vertex-orbits of \(g\) included in \(\sigma\). The empty face contributes \(-1\). Let \(Z_g\) be the sum of \((-1)^{o_g(\sigma)}\) over invariant faces, including empty. Then \(\widetilde L(g)=-Z_g\). Since the unique reduced homology degree \(n-1\) is odd, \(\chi_n(g)=Z_g\).

**Layer exchange.** An \(s\)-fixed face is encoded by bits \(b_1,\ldots,b_n\): \(b_i=1\) means both vertices in column \(i\) are chosen. The closed-neighborhood condition excludes \(b_1=b_2=1\), \(b_{n-1}=b_n=1\), and every internal triple \(b_{i-1}=b_i=b_{i+1}=1\). The orbit weight is \((-1)^{\sum b_i}\). On pair states \((a,b)\in\{0,1\}^2\), define a transfer matrix \(T_s\) by
\[
(T_s)_{(a,b),(b',c)}=\begin{cases}(-1)^c,&b=b'\text{ and }(a,b,c)\ne(1,1,1),\\0,&\text{otherwise.}\end{cases}
\]
Use initial row \(u_s(a,b)=(-1)^{a+b}\mathbf1_{(a,b)\ne(1,1)}\) and terminal column \(v_s(a,b)=\mathbf1_{(a,b)\ne(1,1)}\). Then \(Z_s(n)=u_sT_s^{n-2}v_s\). The exact four-by-four identity \(T_s^4v_s=v_s\), with initial values \(Z_s(2)=-1\), \(Z_s(4)=1\), implies \(Z_s(2k)=(-1)^k\).

**Path reversal.** For \(n=2k\), an \(r\)-fixed subset is determined by left-half column masks \(x_1,\ldots,x_k\in\{0,1,2,3\}\), where the two bits of each mask mark its selected vertices. Its weight is \(\prod_j(-1)^{\operatorname{popcount}(x_j)}\). The closed-neighborhood tests become: if \(x_1=3\), then \(x_2=0\); for internal indices, \(x_j=3\) forces \(x_{j-1}\mathbin{\&}x_{j+1}=0\); and \(x_k=3\) forces \(x_{k-1}=0\). On ordered pair states \((a,b)\in\{0,1,2,3\}^2\), put \(w(c)=(-1)^{\operatorname{popcount}(c)}\) and
\[
(T_r)_{(a,b),(b',c)}=\begin{cases}w(c),&b=b'\text{ and }[b\ne3\ \text{or}\ (a\mathbin{\&}c)=0],\\0,&\text{otherwise.}\end{cases}
\]
Define \(u_r(a,b)=w(a)w(b)\mathbf1_{[a\ne3\text{ or }b=0]}\) and \(v_r(a,b)=\mathbf1_{[b\ne3\text{ or }a=0]}\). For \(k\ge2\), \(Z_r(2k)=u_rT_r^{k-2}v_r\); for \(k=1\) it is \(-1\). Direct exact multiplication yields the sixteen-coordinate identity \((T_r^2-I)^2v_r=0\). The four initial values at \(k=1,2,3,4\) are \(-1,3,-3,5\); therefore the recurrence \(a_{k+4}-2a_{k+2}+a_k=0\) implies
\[
Z_r(2k)=(-1)^k(2\lfloor k/2\rfloor+1).
\]
For \(rs\), the right-half column masks are reflected and layer-swapped, rather than merely reflected. The same endpoint, internal and central conditions hold because the closed-neighborhood tests are invariant under the interchange of the two rows. Thus \(Z_{rs}(2k)=Z_r(2k)\).

**Representation and quotient.** The identity character is the known Betti rank \(n+1\). Substituting the three traces above gives the displayed character and its four irreducible multiplicities by orthogonality of characters of \(V\). For a finite simplicial group action, barycentric subdivision and rational transfer give \(\widetilde H_*(X_n/V;\mathbb Q)\cong\widetilde H_*(X_n;\mathbb Q)^V\). The trivial-character multiplicities give the quotient statement.

## Verification
The companion `checker.py` builds both exact transfer matrices, verifies \(T_s^4v_s=v_s\) and \((T_r^2-I)^2v_r=0\) with integer arithmetic, and checks the initial values and multiplicity formulas. Independently, it enumerates all dominance faces and all invariant faces for \(n=2,4,6,8,10\), obtaining character vectors \((3,-1,-1,-1)\), \((5,1,3,3)\), \((7,-1,-3,-3)\), \((9,1,5,5)\), \((11,-1,-5,-5)\). Direct simplicial mod-two boundary calculations for \(n=2,4,6\) yield single nonzero reduced Betti numbers \(3,5,7\) in degrees \(1,3,5\). The proof for unbounded \(n\) rests on the exact finite-state identities and the cited nonequivariant theorem, not on finite enumeration.

## Relationship to prior work
Thapper (arXiv:0812.1165, Proposition 3.3, December 2008) establishes the nonequivariant homotopy type of the relevant four-wide cylinder independence complex. Matsushita–Wakatsuki (arXiv:2312.02639, first posted December 5, 2023; §5) develop the dominance/independence duality and obtain nonequivariant ladder dominance results. Those papers supply the known Betti rank and degree after the correct Alexander-dual shift, not the four group-element traces or the quotient ranks above. The publicly indexed works on total three-cut ladder complexes, ordinary matching complexes of ladders and independence complexes of circular ladders involve different simplicial constructions. No matching statement or stronger implication was identified in the inspected source portions and available mathematical-index searches. Search absence is not uniqueness proof.

## Limitations
The claim is for even \(n\ge4\). It is rational-equivariant only; the integral representation on the free homology lattice and any integral torsion in the quotient are not determined. The result does not establish the homotopy type of the quotient. Although the exact matrix identities prove all parameter values, the source-dependent homology concentration and rank invoke published nonequivariant results. Equivalent unpublished or unindexed equivariant work may exist.

## References
1. Johan Thapper, *Independence Complexes of Cylinders Constructed from Square and Hexagonal Grid Graphs*, arXiv:0812.1165 (first public 2008-12-05), Proposition 3.3 and proof.
2. Takahiro Matsushita and Shun Wakatsuki, *Dominance Complexes, Neighborhood Complexes and Combinatorial Alexander Duals*, arXiv:2312.02639 (first public 2023-12-05), Sections 1 and 5, especially Example 5.9 and the suspension equivalence.
3. The ordinary combinatorial Alexander duality theorem and the rational homological transfer theorem for finite simplicial-group quotients (standard results used in the proof).
