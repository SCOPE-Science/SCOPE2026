# Symplectic rank census of square-zero derivations of complete-bipartite evolution algebras

## Finding

Let \(k\) be **any field of characteristic two**, and let \(E_{a,b}(k)\) be the evolution algebra of the complete bipartite graph \(K_{a,b}\), where \(a,b\geq1\). Its natural basis consists of \(u_1,\ldots,u_a,v_1,\ldots,v_b\), with all mixed products of distinct basis elements zero and
\[
 u_i^2=\sum_{j=1}^b v_j,\qquad v_j^2=\sum_{i=1}^a u_i.
\]
Let \(\mathcal N_{a,b}(k)=\{D\in\operatorname{Der}_k(E_{a,b}):D^2=0\}\), where the square is composition as a linear endomorphism. The **reduced affine variety** \((\mathcal N_{a,b})_{\mathrm{red}}\) is geometrically irreducible and rational, of dimension
\[
 \boxed{\left\lfloor\frac{a^2}{4}\right\rfloor+\left\lfloor\frac{b^2}{4}\right\rfloor.}
\]
For every \(q=2^e\), the *complete* labeled rank generating polynomial is
\[
 \boxed{\sum_{D\in\mathcal N_{a,b}(\mathbb F_q)}z^{\operatorname{rank}D}
 =P_a(q,z)P_b(q,z),}
\]
where the polynomials \(P_m\) are given explicitly below, with no implicit matrix enumeration.

For integers \(0\le r\le h\), set
\[
 I_{h,r}(q)=\prod_{i=0}^{r-1}\frac{q^{2h-i}-q^i}{q^r-q^i},\qquad
 S_0(q)=1,\quad S_r(q)=q^{r(r+1)/2}\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)})\ (r\ge1).
\]
The empty product is one. The integer \(I_{h,r}(q)\) counts totally isotropic \(r\)-planes in a symplectic \(2h\)-space; \(S_r(q)\) counts invertible symmetric \(r\)-by-\(r\) matrices over \(\mathbb F_q\). Define \(P_1(q,z)=1\), and, for \(h\ge1\),
\[
 \boxed{P_{2h+1}(q,z)=\sum_{r=0}^{h} I_{h,r}(q)S_r(q)z^r,}
\]
\[
 \boxed{P_{2h}(q,z)=\sum_{r=0}^{h-1}I_{h-1,r}(q)S_r(q)
 \left[q^r z^r+(q-1)q^r z^{r+1}
 +q\bigl(q^{2h-2-r}-q^r\bigr)z^{r+2}\right].}
\]
The last coefficient in the final summand automatically vanishes when \(r=h-1\). The degree of \(P_m\) is \(\lfloor m/2\rfloor\). These formulas hold for every \(a,b\ge1\), including the one-vertex part boundaries.

For example, at \(q=2\),
\[
 P_3(2,z)=1+3z,\quad P_4(2,z)=1+7z+12z^2,\quad
 P_5(2,z)=1+15z+60z^2,\quad
 P_6(2,z)=1+31z+300z^2+420z^3.
\]
Thus \(E_{3,5}(\mathbb F_2)\) has \(304\) square-zero derivations, with ranks distributed as \(1,18,105,180\), while its full derivation space has \(2^{13}=8192\) elements.

## Assumptions and scope

Everything in the geometric assertion is over an arbitrary characteristic-two field, after reduction and with geometric irreducibility understood after extension to an algebraic closure. The enumerative statement uses a finite field \(\mathbb F_q\) of characteristic two, not necessarily prime. Ranks and point counts are for *labeled linear derivations*, not automorphism-conjugacy orbits. The prescribed algebra is the unweighted adjacency evolution algebra of \(K_{a,b}\); no statement is asserted for arbitrary weighted or nonbipartite graphs, or for other characteristics.

For \(m\ge1\), define a linear space
\[
 \mathcal L_m(k)=\{P\in M_m(k):P^T=P,\ P\boldsymbol1=0\},
\]
with \(\boldsymbol1=(1,\ldots,1)^T\), and let \(\mathcal Z_m=\{P\in\mathcal L_m:P^2=0\}_{\mathrm{red}}\). The derivation variety is \(\mathcal Z_a\times\mathcal Z_b\).

## Proof

**1. Derivation equations.** Since different natural basis elements multiply to zero, the Leibniz rule gives, for distinct basis indices \(i,j\),
\[
 D(e_i)e_j+e_iD(e_j)=d_{ji}e_j^2+d_{ij}e_i^2=0.
\]
For indices in opposite parts the two displayed square vectors have disjoint nonzero supports, so both coefficients vanish. Within either part they coincide, and characteristic two gives \(d_{ji}=d_{ij}\). Applying the Leibniz rule to \(u_i^2=\sum v_j\) and \(v_j^2=\sum u_i\) gives \(D(\sum v_j)=D(\sum u_i)=0\), because \(2u_iD(u_i)=2v_jD(v_j)=0\). Hence all derivations, and only derivations, are block diagonal \(D=P\oplus Q\) with \(P\in\mathcal L_a\), \(Q\in\mathcal L_b\). In particular \(D^2=0\) exactly when \(P^2=Q^2=0\), and ranks add. It remains to analyze \(\mathcal Z_m\).

**2. Odd block size.** Suppose \(m=2h+1\). On \(V=k^m\) put \(B(x,y)=\sum_i x_iy_i\). Since \(\operatorname{char}k=2\), the subspace \(W=\boldsymbol1^\perp\) is alternating: \(B(x,x)=(\sum_i x_i)^2=0\) on \(W\). Because \(B(\boldsymbol1,\boldsymbol1)=1\), it is nondegenerate of symplectic dimension \(2h\), with orthogonal decomposition \(V=k\boldsymbol1\oplus W\). Every symmetric \(P\) with \(P\boldsymbol1=0\) restricts to a self-adjoint \(T:W\to W\), and this is a bijection.

For \(T^2=0\), put \(U=\operatorname{im}T\), \(r=\dim U\). Self-adjointness implies \(\ker T=U^\perp\), and \(T^2=0\) implies \(U\subseteq U^\perp\). Thus \(U\) is an isotropic \(r\)-plane and \(r\le h\). Conversely, fix such a plane \(U\). The induced map \(W/U^\perp\simeq U^*\to U\) must be an isomorphism, and self-adjointness is exactly the symmetry of its associated nondegenerate bilinear form. Therefore the rank-\(r\) locus is an open bundle with fiber the invertible symmetric \(r\)-by-\(r\) matrices over the symplectic isotropic Grassmannian. Its finite-field count is \(I_{h,r}(q)S_r(q)\), proving the odd formula.

**3. Even block size and the rank shift.** Suppose \(m=2h\). Now \(\boldsymbol1\in\boldsymbol1^\perp\). Choose \(v\in V\) with \(B(v,\boldsymbol1)=1\), for example the first standard basis vector, and set \(W_0=\langle\boldsymbol1,v\rangle^\perp\). Its induced form is nondegenerate alternating, of dimension \(2h-2\). The ordered direct sum \(V=k\boldsymbol1\oplus kv\oplus W_0\) is orthogonal between its two summands, and the first Gram block is \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\). Every \(P\in\mathcal L_{2h}\) is uniquely specified by \(a\in k\), \(w\in W_0\), and a self-adjoint \(T\in\operatorname{End}(W_0)\) through
\[
 P(\boldsymbol1)=0,\qquad P(v)=a\boldsymbol1+w,\qquad
 P(x)=B(w,x)\boldsymbol1+T(x)\quad(x\in W_0).
\]
The relations \(B(w,w)=0\) and \(B(w,Tx)=B(Tw,x)\) show directly that
\[
 \boxed{P^2=0\iff T^2=0\text{ and }Tw=0;\quad a\text{ is unrestricted}.}
\]
Fix \(T\) of rank \(r\), with isotropic image \(U\). Its kernel \(U^\perp\) has \(q^{2h-2-r}\) elements, and \(U\) has \(q^r\) elements. If \(w\in U\), choose \(x\) with \(Tx=w\). The scalar \(c=B(w,x)\) is independent of the choice of \(x\), since \(w\in U=(\ker T)^\perp\). The image of \(P|_{W_0}\) then has dimension \(r\), and \(P(v)\) lies in that image exactly when \(a=c\). Thus there are \(q^r\) choices \((w,a)\) giving rank \(r\), and \((q-1)q^r\) giving rank \(r+1\). If \(w\in U^\perp\setminus U\), the functional \(B(w,-)\) does not vanish on \(\ker T\), so \(P(W_0)\) has dimension \(r+1\) and contains \(\boldsymbol1\); moreover \(P(v)\) adds an independent vector modulo \(U+k\boldsymbol1\). The rank is \(r+2\), for \(q(q^{2h-2-r}-q^r)\) choices. Multiplying these three contributions by \(I_{h-1,r}(q)S_r(q)\) proves the even rank polynomial, including its last zero coefficient.

**4. Exact finite-field factors.** Ordered bases of an isotropic \(r\)-plane in a symplectic \(2h\)-space can be chosen successively in \(q^{2h-i}-q^i\) ways at step \(i\), for \(i=0,\ldots,r-1\). Dividing by the number \(\prod_{i=0}^{r-1}(q^r-q^i)\) of ordered bases of an \(r\)-space yields \(I_{h,r}(q)\).

For \(S_r(q)\), a symmetric matrix with nonzero first diagonal entry has \((q-1)q^{r-1}S_{r-1}(q)\) invertible possibilities by Schur complement. When that diagonal entry is zero, its remaining first-row vector must be nonzero; congruence brings that vector to the first standard basis vector, leaving an invertible symmetric \((r-2)\)-by-\((r-2)\) block and \(r-1\) unconstrained scalars. Hence, over any finite field,
\[
 S_r=(q-1)q^{r-1}S_{r-1}+(q^{r-1}-1)q^{r-1}S_{r-2},\quad S_0=1,\ S_1=q-1.
\]
For characteristic two this recurrence gives precisely the product formula for \(S_r(q)\) above by induction.

**5. Irreducibility, dimension, and rationality.** Over an algebraic closure, the maximal-rank locus of self-adjoint square-zero \(T\) on a symplectic \(2d\)-space is the bundle of invertible symmetric forms over the Lagrangian Grassmannian \(\operatorname{LG}(d,2d)\), so it is irreducible of dimension \(d(d+1)\). Every lower-rank \(T\) is in its closure: extend \(\operatorname{im}T\) to a Lagrangian \(L\subseteq\ker T\), then perturb the corresponding symmetric form on \(W/L\) to an invertible one while keeping \(L\) in the kernel.

For odd \(m=2h+1\), this yields one geometrically irreducible rational cone of dimension \(h(h+1)\). For even \(m=2h\), the triples \((T,w,a)\) with \(T^2=0\) and \(Tw=0\) have a dense locus with \(\operatorname{rank}T=h-1\). Indeed, for every lower-rank pair \((T,w)\), the isotropic subspace \(\operatorname{im}T+kw\) extends to a Lagrangian \(L\) in \(W_0\); perturb \(T\) within the symmetric forms with image in \(L\) and kernel containing \(L\), leaving \(w\in L\) fixed. The dense locus is a bundle over \(\operatorname{LG}(h-1,2h-2)\) of invertible symmetric forms, a vector \(w\in L\), and a free scalar \(a\). Its dimension is
\[
 \frac{h(h-1)}2+\frac{h(h-1)}2+(h-1)+1=h^2.
\]
These bundles are rational because Lagrangian Grassmannians admit affine big cells, and the fibers are nonempty opens in vector spaces. Thus \(\mathcal Z_m\) is geometrically irreducible and rational of dimension \(\lfloor m^2/4\rfloor\). The product \(\mathcal Z_a\times\mathcal Z_b\) is geometrically irreducible and rational, with the asserted dimension.

## Verification

The standalone file `verify_squarezero_evolution.py` uses explicit arithmetic in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). For each side size it enumerates **all** symmetric row-sum-zero matrices by their off-diagonal entries, computes their squares using independent finite-field multiplication, and computes ranks by Gaussian elimination. It matches the rank polynomials for 13 field/side-size configurations, including sizes through six over \(\mathbb F_2\). It separately enumerates **all** endomorphisms of the two smallest complete-bipartite evolution algebras over \(\mathbb F_2\), tests the Leibniz equations directly, and confirms the square-zero subcounts. The script terminates with `EVOLUTION_SQUARE_ZERO_RANK_OK 13 spectra; 2 full Leibniz enumerations`.

The exhaustive checks are finite checks of small cases only; the universal assertions rely on the preceding proof. No claims of independent mathematical validation or computer-formal proof are made.

## Relationship to prior work

Elduque and Labra (2013, arXiv:1312.4685v1) develop the graph/evolution-algebra correspondence and foundational geometry of evolution algebras, **not** this square-zero derivation census. Cadavid, Rodiño Montoya, and Rodríguez (2018, arXiv:1807.02493) describe derivation spaces for graph evolution algebras in characteristic zero. Reis and Cadavid (2020, arXiv:2006.11934v1, specifically the complete derivation characterization in Theorem 3.1) handle arbitrary characteristic, including the block conditions reused here. Neither the existence nor the full linear-space characterization of derivations is claimed as new. The added geometric and arithmetic questions impose the **nonlinear** equation \(D^2=0\); their even-part rank shifts, irreducible reduced cones, and complete finite-field rank polynomial are not stated in these inspected results.

Classical work on nilpotent orbits in characteristic-two symplectic Lie algebras, including Ting Xue's discussion (arXiv:0808.2995), overlaps with the odd-block symplectic background. The present derivation-family claim requires both parities, especially the even-block coupled condition \(T^2=Tw=0\), and a complete labeled rank count. Neither priority nor nonimplication from the entire wider literature is certified. See the accompanying self-review for the comparison scope and residual risks.

## Limitations

The result applies only to complete-bipartite unweighted graph evolution algebras in characteristic two. It does not count derivations over odd characteristic, graph automorphism orbits, conjugacy classes, or higher nilpotency indices. The variety is **reduced**: no claim is made that the quadratic scheme defined by \(D^2=0\) is reduced or smooth. The finite-field tests cannot establish the infinitely many field-size/side-size cases. Some relevant older and modern orbit-classification literature may implicitly recover individual component formulas; independent priority review remains outstanding.

## References

1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first posted 2013-12-17), https://arxiv.org/abs/1312.4685.
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493 (2018), https://arxiv.org/abs/1807.02493.
3. T. Reis and P. Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic*, arXiv:2006.11934v1 (2020), https://arxiv.org/abs/2006.11934.
4. T. Xue, *Nilpotent orbits in classical Lie algebras over finite fields of characteristic 2 and the Springer correspondence*, arXiv:0808.2995 (2008), https://arxiv.org/abs/0808.2995.
