# Square-identity rigidity and torsion-sensitive derivation counts for finite poset incidence algebras

## Finding

Let \(P\) be any finite poset and \(R\) any commutative unital ring. Write \(A=I(P,R)\) for its incidence algebra. Every \(R\)-linear map \(D:A\to A\) satisfying the **square identity alone**
\[
D(a^2)=D(a)a+aD(a)\qquad(a\in A)
\]
is an associative derivation. No assumption about \(2\)-torsion is needed. In particular, this holds in characteristic \(2\), over \(\mathbb Z/4\mathbb Z\), and over nonreduced commutative rings. No separate identity involving \(D(aba)\) is assumed.

There is a natural explicit parametrization
\[
\operatorname{JDer}_{\mathrm{sq}}(A)
\cong R^{N-n}\oplus Z^1(\Delta(P);R),
\]
where \(n=|P|\), \(N=|\{(i,j)\in P^2:i\le j\}|\), \(\Delta(P)\) is the order complex, and \(Z^1\) denotes simplicial one-cocycles. The parametrization is as \(R\)-modules and uses a chosen canonical incidence basis; it is not claimed to be an algebra isomorphism.

If \(R\) is finite, let \(c\) denote the number of connected components of the order complex and let
\[
H_1(\Delta(P);\mathbb Z)\cong
\mathbb Z^b\oplus\bigoplus_{\ell=1}^{t}\mathbb Z/d_\ell\mathbb Z.
\]
Then the exact number of square-identity derivations is
\[
\boxed{
\#\operatorname{JDer}_{\mathrm{sq}}(A)
=|R|^{N-c+b}\prod_{\ell=1}^{t}|R[d_\ell]|,
\qquad R[d]=\{r\in R:dr=0\}.}
\]
In particular, over \(\mathbb F_q\) the dimension of the space of such derivations is \(N-c+\dim_{\mathbb F_q}H^1(\Delta(P);\mathbb F_q)\).

The torsion factor can distinguish coefficient rings of the **same cardinality**. Let \(P\) be the nonempty-face poset of the six-vertex triangulation whose ten triangular facets are
\[
123,\ 124,\ 135,\ 146,\ 156,\ 236,\ 245,\ 256,\ 345,\ 346.
\]
Here the strings denote vertex subsets, not integers. This triangulates the real projective plane, and its incidence poset has \(n=31\), \(N=121\), \(c=1\), and \(H_1\cong\mathbb Z/2\mathbb Z\). Therefore
\[
\#\operatorname{JDer}_{\mathrm{sq}}(I(P,\mathbb F_4))=4^{121},
\qquad
\#\operatorname{JDer}_{\mathrm{sq}}(I(P,\mathbb Z/4\mathbb Z))=2\cdot4^{120}.
\]
The counts differ by a factor of two despite both coefficient rings having four elements.

## Assumptions and scope

Throughout, \(P\) is a **finite antisymmetric poset**; \(R\) is a commutative ring with identity; and \(D\) is **\(R\)-linear**. Put \(e_{ij}\) for the incidence basis element indexed by \(i\le j\). The product is
\[
e_{ij}e_{kl}=\delta_{jk}e_{il},
\]
with the result understood to be zero unless the matching index exists. Set \(e_i=e_{ii}\). A one-cochain assigns \(c_{ij}\in R\) to every strict comparable pair \(i<j\); it is a cocycle precisely when \(c_{ik}=c_{ij}+c_{jk}\) for every chain \(i<j<k\). Empty posets, if permitted, give the zero algebra and the tautological zero-map case; the displayed proof and count apply directly with the usual empty-complex conventions.

The term *square-identity derivation* avoids conflating this single identity with the stronger Jacobson–Rickart definition of a Jordan derivation that assumes **both** a square and a triple-product identity. In characteristic two those definitions need not be equivalent for arbitrary algebras.

## Proof

**1. Idempotent constraints.** Each \(e_i\) satisfies \(e_i^2=e_i\), hence
\[
D(e_i)=D(e_i)e_i+e_iD(e_i).
\]
Comparing coefficients in the incidence basis shows that the support of \(D(e_i)\) lies exclusively in strict entries in row \(i\) or column \(i\); its diagonal coefficient vanishes because \(r=2r\) implies \(r=0\) in any additive group. This argument involves no division by two.

**2. Eliminate idempotent values by an inner derivation.** Polarizing the square identity gives, for arbitrary \(x,y\),
\[
D(xy+yx)=D(x)y+xD(y)+D(y)x+yD(x).
\]
For \(i<j\), apply this to the orthogonal diagonal idempotents \(e_i,e_j\). The \((i,j)\)-entry is
\[
[D(e_i)]_{ij}+[D(e_j)]_{ij}=0.
\]
Define \(h=\sum_{i<j}[D(e_j)]_{ij}e_{ij}\). Then the inner derivation \(\operatorname{ad}_h(x)=hx-xh\) satisfies \(\operatorname{ad}_h(e_i)=D(e_i)\) for each \(i\): for a strict pair \(i<j\), its coefficient is \(-h_{ij}\) at \(e_i\) and \(+h_{ij}\) at \(e_j\). Set \(D_0=D-\operatorname{ad}_h\); it still satisfies the square identity and now \(D_0(e_i)=0\) for every \(i\).

**3. Scalarize each strict interval.** Fix \(i<j\) and set \(z=e_{ij}\). The identities
\[
e_iz+ze_i=z,\qquad e_jz+ze_j=z
\]
combined with polarization and \(D_0(e_i)=D_0(e_j)=0\) imply
\[
D_0(z)=e_iD_0(z)+D_0(z)e_i
=e_jD_0(z)+D_0(z)e_j.
\]
The simultaneous Peirce support conditions leave only the basis entry \(e_{ij}\): an incidence algebra of an antisymmetric poset has no reverse \(e_{ji}\) for \(i<j\). Consequently
\[
D_0(e_{ij})=c_{ij}e_{ij},\qquad c_{ij}\in R.
\]
For diagonal entries put \(c_{ii}=0\).

**4. Transitivity.** For a strict chain \(i<j<k\), we have \(e_{ij}e_{jk}=e_{ik}\) and \(e_{jk}e_{ij}=0\). Polarization yields
\[
c_{ik}=c_{ij}+c_{jk}.
\]
These are exactly the ordered one-cocycle equations on \(\Delta(P)\).

**5. Converse and uniqueness.** Given any cochain \(c\) obeying those equations, the coefficientwise operator \(\delta_c(e_{ij})=c_{ij}e_{ij}\) satisfies the Leibniz rule on every ordered pair of incidence basis vectors: when their product is nonzero, the cocycle equation applies, and when it is zero, the right-hand side is zero. Therefore \(\delta_c\) is a derivation. We have \(D=\operatorname{ad}_h+\delta_c\). The strictly offdiagonal coefficients of \(h\) are uniquely recovered from the values of \(D(e_j)\), while \(c\) is recovered from the residual values on \(e_{ij}\). Thus every such \((h,c)\) gives exactly one square-identity derivation, and every square-identity derivation arises this way. This proves the rigidity theorem and the \(R\)-module decomposition.

**6. Count over finite rings.** The offdiagonal coefficients of \(h\) contribute \(|R|^{N-n}\). For the simplicial cochain complex of \(\Delta(P)\), the zeroth coboundary has kernel isomorphic to \(R^c\), so the first coboundaries have cardinality \(|R|^{n-c}\). Universal coefficients and freeness of integral \(H_0\) give
\[
H^1(\Delta(P);R)\cong\operatorname{Hom}_{\mathbb Z}(H_1(\Delta(P);\mathbb Z),R).
\]
Hence \(|H^1|=|R|^b\prod_\ell|R[d_\ell]|\), which proves the displayed formula after multiplying the cardinalities of the first coboundaries, the first cohomology group, and the inner-derivation parameters.

**7. Torsion witness.** In the explicit ten-facet complex, every one of the fifteen edges belongs to exactly two facets. With a star at vertex one as spanning tree of the complete one-skeleton, the ten triangle-boundary cycles give a rank-ten integral presentation on the ten remaining chord-edge coordinates. Its Smith diagonal is
\[
(1,1,1,1,1,1,1,1,1,2),
\]
so \(H_1\cong\mathbb Z/2\mathbb Z\). Its nonempty-face poset contains six vertices, fifteen edges and ten facets, yielding \(n=31\) and \(N=121\) by direct comparable-pair enumeration. Finally \(|\mathbb F_4[2]|=4\) while \(|(\mathbb Z/4\mathbb Z)[2]|=2\), as asserted.

## Verification

Two standalone source files are included. `checker/check_jordan_poset.py` constructs the **original incidence multiplication** and independently compares the solution spaces to the linear square-equation system and to the entire Leibniz-equation system over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and, for five of the posets, \(\mathbb Z/4\mathbb Z\) via integral Smith forms. All seven posets and all 26 field/ring configurations pass. This is a check of **all** linear maps satisfying the respective linear systems in each test case, not a sample of maps.

`checker/check_rp2_torsion.py` computes the boundary presentation, its integral Smith form, and the exact comparable-pair count for the explicit torsion witness. Its output confirms the two finite-ring formulas. `checks/output.txt` records the actual checker output. Reproduce with `python checker/check_jordan_poset.py` and `python checker/check_rp2_torsion.py` (Python 3 with SymPy). The abstract theorem is proved above; finite computations alone do not establish it.

## Relationship to prior work

Zhankui Xiao, *Jordan Derivations of Incidence Algebras* (arXiv:1411.6123v1, November 22, 2014), defines Jordan derivations by precisely the **square identity** but establishes rigidity under an explicit \(2\)-torsion-free coefficient hypothesis (Theorem 3.3). The present statement drops that hypothesis for **finite posets** by a direct idempotent argument; it does not claim the same for preorders or infinitely many intervals. Xiao's earlier structure theorem and Baclawski's incidence-algebra derivation decomposition supply historical precedent for the inner-plus-transitive form, which is **not claimed independently new**.

Mykola Khrypchenko, *Jordan derivations of finitary incidence rings* (arXiv:1510.00944v1, October 4, 2015), treats arbitrary characteristic and much broader finitary incidence rings. However, its definition in Section 1 requires the **square identity AND the additional triple-product identity**; its concluding Remark 6 does not directly imply rigidity for maps assumed to satisfy only the square identity. The distinction in hypotheses is essential to the present claim, not merely terminology.

Cheng and Jing, *On Jordan Derivations of Triangular Algebras* (arXiv:0706.1942v1, 2007), assumes \(2\)-torsion freedom and faithful bimodules, neither of which is available uniformly for finite posets over arbitrary rings. Work on nonlinear incidence Jordan derivations likewise states \(2\)-torsion-free hypotheses. The dimension/count formula uses the classical cohomological interpretation of transitive functions and the universal coefficient theorem; its new assertion is the **uniform weak-square-rigidity consequence and explicit coefficient-ring-sensitive derivation census**, not a new computation of the integral homology of the projective plane. Published related results on idempotent algebras may overlap; priority is not independently established.

## Limitations

The theorem covers finite antisymmetric posets, commutative unital coefficient rings, and coefficient-linear maps. Its proof does not treat arbitrary noncommutative rings, additive maps that are not \(R\)-linear, infinite finitary incidence algebras, or preorders with nontrivial equivalence classes. The finite-ring count requires \(R\) to be finite, but rigidity itself does not. No statement is made about derivations modulo conjugacy or scheme structure. Priority against all historical literature and independent mathematical validation remain unresolved.

## References

1. Z. Xiao, *Jordan Derivations of Incidence Algebras*, arXiv:1411.6123v1 (2014), https://arxiv.org/abs/1411.6123.
2. M. Khrypchenko, *Jordan derivations of finitary incidence rings*, arXiv:1510.00944v1 (2015), https://arxiv.org/abs/1510.00944.
3. X. Cheng and W. Jing, *On Jordan Derivations of Triangular Algebras*, arXiv:0706.1942v1 (2007), https://arxiv.org/abs/0706.1942.
4. K. Baclawski, *Automorphisms and derivations of incidence algebras* (1972), cited and discussed in Xiao (2014).
5. Y. Yang, *Nonlinear Jordan derivations of incidence algebras*, Communications in Algebra 49 (2021), 3200–3213, DOI:10.1080/00927872.2021.1890106.
