# Smooth connected autotopism groups of evolution algebras with one-dimensional square

## Finding

**Theorem.** Let \(K\) be any field, and let \(E\) be a finite-dimensional evolution algebra of dimension \(n\ge1\) for which \(\dim_K E^2=1\). Write \(r\ge1\) for the rank of its multiplication form and \(s=n-r\). The algebraic group of ordered invertible autotopisms
\[
\mathcal T(E)(L)=\{(H,F,G)\in\operatorname{GL}(E_L)^3:H(xy)=F(x)G(y)\text{ for all }x,y\in E_L\}
\]
for every field extension \(L/K\) is split, smooth and geometrically connected, with an explicit Levi decomposition
\[
\boxed{\mathcal T(E)\cong \mathbb G_a^{\,2rs+n-1}\rtimes
\bigl(\operatorname{GL}_r\times \operatorname{GL}_s\times \operatorname{GL}_s\times\operatorname{GL}_{n-1}\times\mathbb G_m\bigr).}
\]
Here \(\operatorname{GL}_0\) is the trivial group. Its dimension is
\[
\boxed{\dim \mathcal T(E)=2n^2-n+s^2+1.}
\]
For every finite field \(\mathbb F_q\) and every such algebra, independently of the actual coefficients of its multiplication,
\[
\boxed{|\mathcal T(E)(\mathbb F_q)|=(q-1)q^{2rs+n-1}
|\operatorname{GL}_r(\mathbb F_q)|\,|\operatorname{GL}_s(\mathbb F_q)|^2\,
|\operatorname{GL}_{n-1}(\mathbb F_q)|.}
\]
More precisely, the entire algebraic group is determined up to isomorphism solely by the integers \(n,r\), not by the algebra-isomorphism class of \(E\). These statements include characteristic two and both possibilities that the generator of \(E^2\) lies inside or outside the annihilator.

## Assumptions and scope

An evolution algebra is a commutative, not necessarily associative, algebra admitting a basis \(e_1,\ldots,e_n\) such that \(e_i e_j=0\) whenever \(i\ne j\). Since \(\dim E^2=1\), choose \(0\ne u\in E^2\) and define the unique symmetric bilinear form \(b:E\times E\to K\) by \(xy=b(x,y)u\). The rank of \(b\) is \(r\), and \(R=\operatorname{rad}(b)=\operatorname{Ann}(E)\) has dimension \(s=n-r\). The symmetry follows from commutativity; its representing diagonal matrix in a natural basis also makes the rank well-defined in characteristic two. For a \(K\)-algebra \(L\), all definitions extend by scalar extension; the asserted group-scheme isomorphism is given by matrices over \(K\), not merely by point-counting.

The term *autotopism* denotes an ordered triple \((H,F,G)\) of invertible linear maps satisfying the displayed identity. There is no requirement that the three maps coincide. The first map acts on the product and may have a different matrix from those acting on the factors.

## Proof

**Step 1: reduction to a bilinear matrix identity.** Since products span \(Ku\), an autotopism must satisfy \(H(u)=tu\) for a unique \(t\in K^\times\). In fact, for all \(x,y\),
\[
b(Fx,Gy)u=F(x)G(y)=H(xy)=b(x,y)H(u)=t b(x,y)u.
\]
The converse is immediate. Thus the complete defining equations are \(H(u)=tu\) and \(F^TB G=tB\), where \(B\) is the Gram matrix of \(b\).

**Step 2: block parametrization, including degenerate forms.** Choose a complement \(U\) of \(R\). With respect to \(E=U\oplus R\),
\[
B=\begin{pmatrix}B_0&0\\0&0\end{pmatrix},\qquad B_0\in\operatorname{GL}_r(K),\quad B_0^T=B_0.
\]
The equation \(b(Fx,Gy)=t b(x,y)\) implies \(F(R)=R\): if \(x\in R\), then \(b(Fx,Gy)=0\) for every \(y\), and surjectivity of \(G\) forces \(Fx\in R\). Similarly \(G(R)=R\). Therefore the **unique** possible matrices are
\[
F=\begin{pmatrix}A&0\\C&D\end{pmatrix},\qquad
G=\begin{pmatrix}tB_0^{-1}A^{-T}B_0&0\\Z&W\end{pmatrix},
\]
where \(A\in\operatorname{GL}_r(K)\), \(D,W\in\operatorname{GL}_s(K)\), and \(C,Z\) are independent \(s\)-by-\(r\) matrices. The formula for the upper-left block of \(G\) follows by solving \(A^TB_0G_{UU}=tB_0\), and substitution shows that there are no additional constraints. The same argument holds functorially over arbitrary commutative \(K\)-algebras: the radical is the fixed direct summand \(R\) of the split matrix \(B\), and \(A,D,W\) are required to be invertible.

**Step 3: the first component.** Choose an arbitrary basis of \(E\) beginning with \(u\), independently of the preceding \(U\oplus R\) basis. All invertible maps with \(H(u)=tu\) have precisely the form
\[
H=\begin{pmatrix}t&h\\0&J\end{pmatrix},\qquad
h\in K^{1\times(n-1)},\quad J\in\operatorname{GL}_{n-1}(K).
\]
There is no constraint coupling \(h,J\) to \(A,C,D,Z,W\). In particular, the location of \(u\) relative to \(R\) does not change the group.

**Step 4: group structure.** Simultaneous multiplication of triples multiplies the diagonal parameters by the usual matrix group laws, and its upper/lower shears transform by linear representations. Setting \(C=Z=h=0\) defines a closed reductive subgroup
\(
\operatorname{GL}_r\times\operatorname{GL}_s^2\times\operatorname{GL}_{n-1}\times\mathbb G_m
\)
(the \(UU\)-block in \(G\) is determined by \(A,t\)). The subgroup of shears \(C,Z,h\) with all diagonal parameters equal to identities is normal, is isomorphic to an additive group, and has dimension \(2rs+n-1\). It has trivial intersection with the displayed reductive subgroup, and every element factors uniquely as a shear times a reductive element. This proves the claimed split semidirect product. General linear groups and additive groups are smooth and geometrically connected over every field; hence so is the semidirect product.

**Step 5: dimension and arithmetic.** Adding the dimensions gives
\[
r^2+2s^2+(n-1)^2+1+(2rs+n-1)=2n^2-n+s^2+1.
\]
Each of the \(2rs+n-1\) shear coordinates can be chosen independently in \(\mathbb F_q\); each invertible diagonal block can be chosen independently. The free parameter \(t\) has \(q-1\) possibilities, yielding the exact formula. Here
\[
|\operatorname{GL}_j(\mathbb F_q)|=\prod_{i=0}^{j-1}(q^j-q^i),\qquad |\operatorname{GL}_0(\mathbb F_q)|=1.
\]
All equalities are identities of finite sets and algebraic groups, not statistical extrapolations.

## Verification

The standalone file `verify.py` computes invertible matrices over small prime fields without using the block parametrization to test the autotopism condition. It independently checks \(F^TBG=tB\), counts possible \(H\), and compares the complete counts against the formula across rank, dimension, field, generator position, and a nontrivial diagonal bilinear form. The cases include all nonzero ranks in dimension three over \(\mathbb F_2\), dimension two over \(\mathbb F_3\), and rank-one radical cases. A successful run prints `VERIFY_OK`. The finite tests do not prove the general theorem; Steps 1–5 do.

## Relationship to prior work

The survey of Kaygorodov, Martín González, and Viruel (first publicly available October 15, 2026) highlights autotopy-group schemes as a structural topic for evolution algebras. Earlier work of Martín González, Rabie, and Sánchez-Ortega (2024) treats ternary automorphisms of *perfect* evolution algebras and ternary derivations of general finite-dimensional evolution algebras. This paper does not claim new ternary-derivation formulas; its object is the **full invertible triple group scheme for the nonperfect rank-one-square stratum**, including unipotent radical, connectedness, and exact finite-field group orders. Brache, Martín Barquero, Martín González, and Sánchez-Ortega (2021) classified one-dimensional-square evolution algebras via bilinear forms and distinguished their isomorphism types. The present description is independent of that finer isomorphism classification and computes a different invariant. General parabolic and bilinear-matrix stabilizer methods are standard ingredients, and prior equivalent presentations under autotopy, isotopy, or bilinear-form terminology remain possible.

## Limitations

The theorem applies to \(\dim E^2=1\) only and does not determine autotopisms of evolution algebras of higher square dimension. Isomorphic autotopism groups do not imply isomorphic evolution algebras: the triple group does not retain the finer bilinear-form/isomorphism invariants. No new classification of ternary derivations is asserted. The full historical priority of the explicit group-scheme decomposition has not been independently audited.

## References

1. I. Kaygorodov, C. Martín González, C. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (public October 15, 2026), https://arxiv.org/html/2610.22248v1.
2. C. Martín González, J. Rabie, J. Sánchez-Ortega, *Ternary mappings of some evolution algebras*, arXiv:2405.10241 (2024), https://arxiv.org/pdf/2405.10241.
3. C. Brache, D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Evolution algebras with one-dimensional square*, arXiv:2103.01625 (2021), https://arxiv.org/pdf/2103.01625.
