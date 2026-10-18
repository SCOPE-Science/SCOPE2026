# Fixed-space spectrum of automorphisms of nonsplit three-dimensional almost-abelian Lie algebras

## Finding
Let \(F=\mathbb F_q\) be any finite field, let \(V\) have dimension two over \(F\), and let \(A\in\operatorname{GL}(V)\) have an irreducible quadratic characteristic polynomial over \(F\). Form the three-dimensional Lie algebra \(L_A=Fe\ltimes V\), with \([e,v]=Av\) and \([V,V]=0\). For \(j\in\{0,1,2,3\}\), define
\[
 C_j(A)=\#\{\varphi\in\operatorname{Aut}_F(L_A):\dim_F\ker(\varphi-1)=j\}.
\]
The complete fixed-space distribution depends only on the vanishing of \(\operatorname{tr}A\):

| Fixed-space dimension | \(\operatorname{tr}A\ne0\) | \(\operatorname{tr}A=0\) (necessarily odd characteristic) |
|---|---:|---:|
| \(0\) | \(0\) | \(q^2(q+1)(q-2)\) |
| \(1\) | \(q^2(q^2-2)\) | \(q^2(q^2+q-1)\) |
| \(2\) | \(q^2-1\) | \(q^2-1\) |
| \(3\) | \(1\) | \(1\) |

Accordingly, a fixed-point-free automorphism exists exactly when \(q\) is odd and \(\operatorname{tr}A=0\). In this case its exact proportion among all automorphisms is
\[
 \frac{q-2}{2(q-1)}.
\]
In characteristic two every irreducible quadratic has nonzero trace, so no member of this nonsplit family admits a fixed-point-free automorphism.

## Assumptions and scope
The Lie bracket is bilinear and alternating, with the displayed brackets and their skew-symmetric counterparts; this defines a Lie algebra over every characteristic, including two. The irreducible characteristic-polynomial assumption implies that \(A\) is invertible, that \([L_A,L_A]=V\), and that \(V\) is a characteristic ideal. The theorem covers every prime-power field size and every irreducible quadratic similarity class; there is no restriction on the determinant or on a choice of basis. The count \(C_j(A)\) is of individual \(F\)-linear Lie algebra automorphisms, not conjugacy classes, and counts the dimension of the fixed-point subspace, not the number of fixed vectors.

## Proof
**Automorphism parametrization.** As \(V=[L_A,L_A]\) is characteristic, an automorphism must have the form
\[
 \varphi(e)=ce+w,\qquad \varphi|_V=T,
 \qquad c\in F^\times,\quad w\in V,\quad T\in\mathrm{GL}_2(F).
\]
Preservation of \([e,v]=Av\) is equivalent to \(TA=cAT\); preservation of \([V,V]=0\) adds no condition. Conversely, any such triple defines an automorphism because its underlying linear map is invertible and preserves all defining brackets. Every permissible pair \((c,T)\) therefore contributes exactly \(q^2\) automorphisms, indexed by \(w\).

**Possible scalars.** Similarity of \(A\) and \(cA\) implies \(c^2=1\) by their nonzero determinants, and \((c-1)\operatorname{tr}A=0\) by their traces. If \(\operatorname{tr}A\ne0\), then \(c=1\). In characteristic two, irreducibility of the quadratic polynomial forces its linear coefficient, hence \(\operatorname{tr}A\), to be nonzero: otherwise the polynomial \(X^2+d\) would have a root in the perfect field \(F\). If \(\operatorname{tr}A=0\), the characteristic is thus odd and \(c\in\{1,-1\}\), both of which occur, as shown below.

**Quadratic field realization.** Put \(E=F_{q^2}\). Irreducibility identifies \(V\) with the one-dimensional \(E\)-space \(E\) so that \(A\) acts as multiplication by some \(\lambda\in E\setminus F\). The centralizer of \(A\) in \(\mathrm{GL}_2(F)\) consists precisely of multiplication maps \(m_u:z\mapsto uz\) for \(u\in E^\times\), giving \(q^2-1\) possible \(T\) for \(c=1\).

If \(\operatorname{tr}A=0\), the two conjugate eigenvalues satisfy \(\lambda^q=-\lambda\). Thus the Frobenius map \(\sigma:z\mapsto z^q\) satisfies \(\sigma A=-A\sigma\). Every invertible solution of \(TA=-AT\) is uniquely \(T=m_u\sigma\), with \(u\in E^\times\), since composing two such intertwiners yields an element of the centralizer. This gives another \(q^2-1\) matrices for \(c=-1\).

**Fixed-space dimensions for \(c=1\).** Relative to the decomposition \(Fe\oplus V\), the matrix of \(\varphi-1\) has blocks
\[
 \begin{pmatrix}0&0\\w&T-1\end{pmatrix}.
\]
For \(T=m_u\) with \(u\ne1\), multiplication by \(u-1\) is invertible on \(E\), and the fixed space has dimension one, for all \(q^2\) values of \(w\). For \(u=1\) and \(w\ne0\), it has dimension two. The unique choice \(u=1,w=0\) is the identity and has three-dimensional fixed space. Hence the \(c=1\) contribution is \(q^2(q^2-2)\) at dimension one, \(q^2-1\) at dimension two, and \(1\) at dimension three.

**Fixed-space dimensions for \(c=-1\).** This branch occurs only in odd characteristic; its scalar diagonal block in \(\varphi-1\) is \(-2\), so an element fixed by \(\varphi\) lies in \(V\). For \(T=m_u\sigma\), the equation \(Tz=z\) for nonzero \(z\in E\) is \(z^{q-1}=u^{-1}\). The image of \(z\mapsto z^{q-1}\) in \(E^\times\) is exactly the norm-one subgroup \(\ker N_{E/F}\), of size \(q+1\); each soluble equation has exactly \(q-1\) nonzero solutions, forming one \(F\)-line together with zero. Thus exactly \(q+1\) choices of \(u\) give a one-dimensional fixed space, while \((q^2-1)-(q+1)=(q+1)(q-2)\) choices give a zero-dimensional one. Multiplying by the unrestricted \(q^2\) choices of \(w\) gives the dimension-zero and additional dimension-one entries displayed in the table.

Summing both branches gives the asserted distributions. Their totals are \(q^2(q^2-1)\) when \(\operatorname{tr}A\ne0\) and \(2q^2(q^2-1)\) when \(\operatorname{tr}A=0\); dividing the zero-dimensional count by the latter total proves the fraction. This exhausts every automorphism and every field characteristic.

## Verification
The accompanying `verify.py` uses only the Python standard library. It constructs an explicit quadratic-irreducible companion matrix in each tested finite field, enumerates every invertible \(2\times2\) matrix \(T\), tests the bracket equation \(TA=cAT\) for every \(c\ne0\), and enumerates every \(w\in F^2\). Direct finite-field Gaussian elimination computes \(\dim\ker(\varphi-1)\) for every resulting automorphism; no norm-one or centralizer formula is assumed by the checker. It tests ten configurations over fields of orders \(2,3,4,5,7,11\), covering both trace cases when available. A successful run ends with `VERIFY_OK`. These finite exhaustive checks corroborate, but do not replace, the proof for arbitrary prime-power fields.

## Relationship to prior work
Burde and Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras* (2026), classify existence for **complex** almost-abelian Lie algebras and discuss three-dimensional cases, including a split zero-trace example. The present theorem instead gives exact fixed-subspace multiplicities over every finite field for the **irreducible quadratic** nonsplit case. This restriction is essential: a split characteristic-polynomial calculation does not imply the nonsplit intertwiner counts, whose second branch is controlled by the norm-one subgroup of \(F_{q^2}^\times\). A published finite-field fixed-point-free count for the three-dimensional Heisenberg Lie algebra concerns a nilpotent algebra with one-dimensional derived ideal, not the present centerless solvable algebras with two-dimensional derived ideal. The basic normalizer and norm-map identities used in the proof are classical; they are not claimed as discoveries.

## Limitations
The result does not classify fixed-point spaces for reducible, noninvertible, or higher-dimensional adjoint operators; it does not enumerate automorphism conjugacy classes. Literature indexing is incomplete, so an equivalent older finite-field count cannot be ruled out categorically. Independent mathematical validation has not been performed.

## References
1. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916 (initial public version 2026-04-30); https://arxiv.org/abs/2604.27916 . Author-hosted open manuscript: https://homepage.univie.ac.at/dietrich.burde/papers/burde_83_fpf.pdf . See §4, Proposition 4.2, and §5, Theorem 5.4.
2. Standard finite-field facts: the multiplicative group of \(\mathbb F_{q^2}\) is cyclic, the norm onto \(\mathbb F_q^\times\) is surjective, and the kernel has size \(q+1\).
