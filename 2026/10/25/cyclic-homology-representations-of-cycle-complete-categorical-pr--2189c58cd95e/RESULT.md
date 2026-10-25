# Cyclic homology representations of cycle–complete categorical-product independence complexes

## Finding
Let \(r\geq1\), \(n\geq2\), \(m=3r\), and \(q=n-1\). Give \(G_{r,n}=C_m\times K_n\) the categorical-product graph structure, and let \(X_{r,n}=\operatorname{Ind}(G_{r,n})\). The cyclic group \(C_m=\langle g\rangle\) acts by shifting the cycle coordinate by one. Its only nonzero reduced rational homology is in degree \(2r-1\), and the complete character on that homology is
\[
\chi_{r,n}(g^j)=q(-1)^d+\begin{cases}3q^{d/3},&3\mid d,\\0,&3\nmid d,\end{cases}\qquad d=\gcd(m,j),\quad 0\leq j<m.
\]
In particular, its dimension is \(3q^r+(-1)^r q\).

The character has a positive rational-module description. Put \(H=\langle g^3\rangle\cong C_r\). Let \(\Omega_r(q)\) be the set of words of length \(r\) in an alphabet of size \(q\), with \(H\) acting by cyclic rotation; let \(\Omega_r^*(q)\) remove the \(q\) constant words. Let \(\rho\) be the two-dimensional rational irreducible representation inflated from \(C_m/H\cong C_3\). When \(r\) is even, let \(\varepsilon\) be the one-dimensional character with \(\varepsilon(g)=-1\). Then, as rational \(C_m\)-modules,
\[
\widetilde H_{2r-1}(X_{r,n};\mathbb Q)\cong
\begin{cases}
\operatorname{Ind}_{H}^{C_m}\mathbb Q[\Omega_r(q)]\oplus\varepsilon^{\oplus q},&r\text{ even},\\
\operatorname{Ind}_{H}^{C_m}\mathbb Q[\Omega_r^*(q)]\oplus\rho^{\oplus q},&r\text{ odd}.
\end{cases}
\]
Consequently the cyclically invariant homology has dimension
\[
\dim\widetilde H_{2r-1}(X_{r,n};\mathbb Q)^{C_m}
=\frac1r\sum_{e\mid r}\varphi(r/e)q^e-\begin{cases}q,&r\text{ odd},\\0,&r\text{ even}.\end{cases}
\]
The sum is the usual necklace count for \(q\)-letter words of length \(r\).

## Assumptions and scope
The cycle \(C_m\) has vertices \(i\in\mathbb Z/m\mathbb Z\), and \(K_n\) has vertices \(a\in\{1,\ldots,n\}\). Distinct vertices \((i,a)\), \((i',a')\) of the product are adjacent exactly when \(i'=i\pm1\pmod m\) and \(a'\neq a\). The independence complex includes the empty face in its augmented chain complex. All homology representations and module decompositions are over \(\mathbb Q\). For \(r\geq1,n\geq2\), Antolín Camarena and Carnero Bravo proved that \(X_{r,n}\) is homotopy equivalent to a wedge of spheres of dimension \(2r-1\) [1, Theorem 22]. That previously known homotopy classification is a hypothesis imported from the cited published mathematical theorem, not a new assertion of this result.

## Proof
**Homological concentration.** By [1, Theorem 22], reduced homology is concentrated in the odd dimension \(2r-1\). In particular, if \(\widetilde L(g^j)\) is the *augmented reduced* simplicial Lefschetz trace, then \(\widetilde L(g^j)=-\chi_{r,n}(g^j)\).

**Fixed faces and signs.** Fix \(0\leq j<m\), and put \(d=\gcd(m,j)\), \(\ell=m/d\). Each vertex orbit under \(g^j\) has \(\ell\) vertices. A \(g^j\)-invariant independent face consists of whole orbits. If it comprises \(t\) orbits, it contains \(\ell t\) vertices; on its oriented simplex the permutation has sign \((-1)^{(\ell-1)t}\), and its augmented alternating-chain coefficient is \((-1)^{\ell t-1}\). Their product is \((-1)^{t-1}\), including the empty face with coefficient \(-1\). Therefore \(\widetilde L(g^j)\) is minus the independence polynomial at \(-1\) of the graph of allowed vertex orbits.

The orbits are indexed by residue classes \(i\in\mathbb Z/d\mathbb Z\) and colors \(a\in\{1,\ldots,n\}\). An orbit selection is encoded by a subset \(S_i\) of colors at each residue. Admissibility across adjacent residues requires either \(S_i\) or \(S_{i+1}\) to be empty, or both to equal the same singleton. For \(d=1\), the cyclic closure forces a single color or the empty selection; for \(d=2\), the two residues obey this same adjacency rule. Hence the same cyclic transfer computation below includes both short cases, without interpreting a one- or two-vertex cycle as an ordinary simple cycle.

**Exact transfer computation.** At each residue allow the empty state of signed weight \(1\), the \(n\) singleton-color states of weight \(-1\), and a lumped multi-color state of signed weight
\[
\sum_{t=2}^n(-1)^t\binom nt=n-1=q.
\]
The multi-color state is compatible only with an empty neighbor; a singleton state is compatible with the empty state and itself. If \(T\) has entries \(T_{a,b}=\mathbf1_{a\sim b}\,w_b\), the signed orbit-selection sum on a cyclic word of length \(d\) is \(Z_d=\operatorname{tr}(T^d)\). The \(n-1\)-dimensional difference space among singleton colors has eigenvalue \(-1\). On the span of the empty state, the uniform singleton state, and the multi-color state, the matrix is
\[
\begin{pmatrix}1&-n&q\\1&-1&0\\1&0&0\end{pmatrix},
\]
whose characteristic polynomial is \(\lambda^3-q\). Its three eigenvalues have power-sum \(3q^{d/3}\) when \(3\mid d\) and zero otherwise. Therefore
\[
Z_d=q(-1)^d+\mathbf1_{3\mid d}\,3q^{d/3}.
\]
Since \(\widetilde L(g^j)=-Z_d\), odd-dimensional homological concentration yields \(\chi_{r,n}(g^j)=Z_d\). Setting \(j=0\) yields the rank formula. The displayed character formula holds for every \(j\), not merely generators.

**Actual representation and invariant dimension.** The induced permutation module from \(H\) on \(q\)-letter length-\(r\) words has trace \(3q^{\gcd(r,j/3)}\) for \(3\mid j\), and zero otherwise. If \(r\) is even, \((-1)^{\gcd(m,j)}=(-1)^j\), giving the sign-summand formula. If \(r\) is odd, this parity factor is constantly \(-1\). Splitting the word module into its \(q\) constant words and all remaining words shows that the contribution of each constant-word induced permutation module, after subtracting one trivial character, equals \(\rho\). Thus the stated positive module decomposition has precisely the derived character. Maschke's theorem and rational character rigidity for the finite cyclic group give the module isomorphisms. Frobenius reciprocity and Burnside's necklace count yield the invariant-dimension formula.

## Verification
A standalone standard-library Python verifier (`verify_cycle_product.py`) enumerates every independent face and every cycle rotation for the cases \((m,n)=(3,2),(3,3),(3,4),(6,2),(6,3),(9,2)\), computing signed simplicial Lefschetz traces directly. It also checks a separate orbit-cycle sign simplification, computes the cyclic transfer matrix independently for \((m,n)=(12,2)\) as well as the smaller tests, compares both positive representation formulas, and checks character orthogonality and necklace invariants. Successful recorded output:

`CYCLIC_PRODUCT_CHARACTERS_VERIFIED [(3, 2, 17, 0), (3, 3, 33, 0), (3, 4, 61, 0), (6, 2, 323, 1), (6, 3, 1649, 3), (9, 2, 5777, 0), (12, 2, -1, 1)]`

The third entry of each tuple is the number of nonempty independently enumerated faces, or \(-1\) where enumeration was deliberately omitted; the fourth is the invariant-homology dimension. These are finite checks, not a proof of the uniform theorem; the preceding transfer and Lefschetz argument proves the all-parameter statement.

## Relationship to prior work
Antolín Camarena and Carnero Bravo [1, Theorem 22, and Section 3.2] proved the underlying wedge-of-spheres homotopy classification for \(C_{3r}\times K_n\); its Betti numbers do not determine nonidentity rotation traces or the rational cyclic representation. Goyal, Shukla and Singh [2, Proposition 3.2] proved the earlier complete-graph-product case and tabulated sphere ranks but did not classify cyclic homology actions. The present finding determines the full rotation action, a positive induced-module description, and the necklace-count invariant space, without re-claiming the earlier homotopy results. The standard homological Lefschetz theorem and finite-group character theory are proof tools rather than new developments.

## Limitations
The representation decompositions are over \(\mathbb Q\). There is no assertion of an integral module splitting, equivariant homotopy equivalence, a dihedral or color-permutation action classification, or analogous concentration when the cycle length is not divisible by three. Finite enumerations cover only the explicitly stated cases. Published and indexed searches did not reveal the identical rotation-character formula, but cannot exclude an unindexed equivalent formulation or material not accessible in full text.

## References
[1] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first publicly submitted 2023-07-23, Theorem 22 and Section 3.2. https://arxiv.org/abs/2307.12401

[2] S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first publicly submitted 2019-05-16, Proposition 3.2. https://arxiv.org/abs/1905.06926
