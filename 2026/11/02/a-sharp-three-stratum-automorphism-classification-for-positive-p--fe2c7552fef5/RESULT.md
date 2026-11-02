# A sharp three-stratum automorphism classification for positive-parameter quaternion-core pentarnion algebras

## Finding
For every quadruple \(a,b,c,d>0\), consider the real five-dimensional quadratic algebra \(A_0(a,b,c,d)\) introduced in [1] (its parameter \(\gamma\) is zero). Its full real algebra automorphism group has exactly three possibilities:
\[
\operatorname{Aut}_{\mathbb R}A_0(a,b,c,d)\cong
\begin{cases}
O(2), & a=b=c,\\
C_2, & \text{exactly two of }a,b,c\text{ agree},\\
\{1\}, & a,b,c\text{ are pairwise distinct}.
\end{cases}
\]
This is a classification of the **full** automorphism group, not merely a subgroup. In every case the answer is independent of \(d>0\). More precisely, for any \(d_1,d_2>0\), the map fixing \(1,i,j,k\) and sending \(\ell_{d_1}\) to \(\sqrt{d_1/d_2}\,\ell_{d_2}\) gives an algebra isomorphism \(A_0(a,b,c,d_1)\simeq A_0(a,b,c,d_2)\).

## Assumptions and scope
The base field is \(\mathbb R\). All four coefficients are **strictly positive** and \(\gamma=0\). The multiplication table of [1, Section 2] has unit \(1\), squares \(i^2=-a\), \(j^2=-b\), \(k^2=-c\), \(\ell^2=-d\), and anticommuting distinct pure basis elements, with
\[
\begin{aligned}
ij&=\sqrt{ab/c}\,k,&ik&=-\sqrt{ac/b}\,j,&jk&=\sqrt{bc/a}\,i,\\
i\ell&=-\sqrt{ad/(b+c)}(j+k),&
j\ell&=-\sqrt{bd/(a+c)}(k+i),&
k\ell&=-\sqrt{cd/(a+b)}(i+j).
\end{aligned}
\]
Write the orthonormal pure basis \(X=i/\sqrt a\), \(Y=j/\sqrt b\), \(Z=k/\sqrt c\), \(W=\ell/\sqrt d\), and \(U=\operatorname{span}_{\mathbb R}\{X,Y,Z\}\). Use \(x=\sqrt a\), \(y=\sqrt b\), \(z=\sqrt c\) and \(u=\sqrt{a+b}\), \(v=\sqrt{a+c}\), \(w=\sqrt{b+c}\). Define
\[
H=\begin{pmatrix}
0&-x/v&-x/u\\
-y/w&0&-y/u\\
-z/w&-z/v&0
\end{pmatrix}.
\]
An explicit, exact description of the automorphism group is
\[
\{\operatorname{diag}(1,R,1):R\in SO(3),\ RH=HR\},
\]
where the diagonal blocks act on \(\mathbb R1\oplus U\oplus\mathbb RW\).

## Proof
**Intrinsic orthogonality and the commutant reduction.** For \(q=s+p\) with \(p\) pure, the multiplication obeys \(q^2-2sq+(s^2+\|p\|^2)1=0\). For non-scalar \(q\), the coefficients of \(1,q\) in this monic quadratic identity are uniquely determined, hence an automorphism preserves \(s\) and \(s^2+\|p\|^2\) and acts orthogonally on the pure subspace. Polarization gives pure multiplication \(p q=-\langle p,q\rangle+p\times q\).

On \(U\), \(\times\) is the ordinary oriented three-dimensional cross product, while \(v\times W=Hv\) for \(v\in U\). In particular, the image of the pure cross product is exactly \(U\), since \(X\times Y=Z\), \(Y\times Z=X\), \(Z\times X=Y\). Thus any automorphism preserves \(U\) and its orthogonal line \(\mathbb RW\), so its pure matrix is \(\operatorname{diag}(R,\varepsilon)\), with \(R\in O(3)\), \(\varepsilon\in\{\pm1\}\). Cross-product preservation on \(U\) forces \(R\in SO(3)\), and preservation of products with \(W\) becomes \(RH=\varepsilon HR\). Directly,
\[
\det H=-\frac{2xyz}{uvw}\ne0.
\]
Taking determinants (the dimension of \(U\) is odd) yields \(\varepsilon=1\). Conversely, an \(R\in SO(3)\) commuting with \(H\) preserves all pure products and inner products, and therefore the original unital multiplication. This proves the displayed centralizer identity.

**The isotropic stratum.** If \(a=b=c\), then \(H=-(J_3-I_3)/\sqrt 2\), with one real eigenline \(\mathbb R(1,1,1)\) and its perpendicular two-dimensional eigenspace. The subgroup of \(SO(3)\) stabilizing this decomposition is canonically isomorphic to \(O(2)\).

**The non-isotropic strata: rotations and their axis.** When the three coefficients are not all equal, write \(H=S+K\), where \(S=\tfrac12(H+H^T)\) is symmetric and \(K=\tfrac12(H-H^T)\) is skew. The latter equals half the cross-product matrix of the nonzero vector
\[
\kappa=\left(\frac{y}{u}-\frac{z}{v},\ \frac{z}{w}-\frac{x}{u},\ \frac{x}{v}-\frac{y}{w}\right)^T.
\]
Its three component signs are respectively those of \(b-c\), \(c-a\), \(a-b\). Every \(R\in SO(3)\) centralizing \(H\) separately centralizes \(S\) and \(K\), and must therefore be a rotation about the oriented axis \(\mathbb R\kappa\).

A rotation on \(\kappa^\perp\) through an angle different from \(0\) or \(\pi\) would force the symmetric matrix \(S\) to be axially symmetric: \(S=\alpha I_3+\beta\kappa\kappa^T\). Yet \(S\) has diagonal entries zero and all three off-diagonal entries strictly negative. If any coordinate of \(\kappa\) vanishes, the axial representation gives \(\alpha=0\) and thus forces some off-diagonal entry to vanish, impossible. If no coordinate vanishes, the zero diagonal and negative off-diagonal require \(\beta<0\) and all coordinates of \(\kappa\) to have the same sign. This contradicts the cyclic sign pattern \((b-c,c-a,a-b)\). Thus every nonidentity automorphism is necessarily the half-turn
\[
R_{\pi}=2\frac{\kappa\kappa^T}{\kappa^T\kappa}-I_3,
\]
which centralizes \(H\) exactly when \(H\kappa\) is proportional to \(\kappa\).

If precisely two parameters agree, assume by cyclic symmetry that \(a=b\ne c\). Then \(v=w\) and \(\kappa\) is a nonzero multiple of \((1,-1,0)\), while \(H(1,-1,0)^T=(x/v)(1,-1,0)^T\). Hence the half-turn exists and the full automorphism group is exactly \(C_2\).

**Exclusion of the half-turn for three distinct coefficients.** The matrix \(H\) is diagonally symmetrizable: the positive diagonal matrix
\[
D=\operatorname{diag}\left(1,\frac{xw}{yv},\frac{xw}{zu}\right)
\]
satisfies \(DH=H^TD\). Consequently \(D^{1/2}HD^{-1/2}\) is symmetric with diagonal zero and off-diagonal entries \(-\alpha,-\beta,-\delta\) where
\[
\alpha^2=\frac{xy}{vw},\qquad
\beta^2=\frac{xz}{uw},\qquad
\delta^2=\frac{yz}{uv}.
\]
Its characteristic polynomial is \(t^3-(\alpha^2+\beta^2+\delta^2)t+2\alpha\beta\delta\); its discriminant equals
\[
4\left[(\alpha^2+\beta^2+\delta^2)^3-27\alpha^2\beta^2\delta^2\right].
\]
By the arithmetic-geometric mean inequality this is positive unless \(\alpha=\beta=\delta\), which by the displayed positive ratios is equivalent to \(a=b=c\). Therefore \(H\) has three distinct real eigenvalues whenever the parameters are not all equal.

For pairwise distinct \(a,b,c\), every coordinate of \(\kappa\) is nonzero. If \(H\kappa=\lambda\kappa\), then \(K\kappa=0\) implies \(H^T\kappa=\lambda\kappa\). Since \(H^T=DHD^{-1}\), also \(D^{-1}\kappa\) is an eigenvector of \(H\) for the simple eigenvalue \(\lambda\). Simplicity forces \(D^{-1}\kappa\) proportional to \(\kappa\). As all its coordinates are nonzero, this makes \(D\) a scalar matrix, which directly implies \(a=b=c\). Contradiction. So no half-turn exists and the centralizer is trivial.

**Independence of \(d\).** The change \(W=\ell/\sqrt d\) removes \(d\) from the normalized multiplication table, proving the asserted explicit rescaling isomorphism for any two positive values of \(d\).

## Verification
The supplementary standalone exact-arithmetic script `verify.py` constructs the normalized matrix \(H\), checks its nonzero determinant and diagonal symmetrizer, tests the appropriate half-turn or obstruction in ten representative parameter regimes, and compares all orientation-preserving signed-permutation matrices in each case. Execute `python3 verify.py` with Python and SymPy installed. Observed output:

```
VERIFY_OK exact_parameter_cases= 10 signed_orthogonal_tests= 240
```

The finite tests are corroboration only. The proof of the complete real Lie-group classification is the symbolic argument above.

## Relationship to prior work
Poshtkohi and Pumplün [1] introduce these algebras, provide the full multiplication table (Section 2), and classify the **canonical isotropic** \(a=b=c=d=1\) family (Theorem 3.10), including \(\operatorname{Aut}A_0(1,1,1,1)\cong O(2)\). Remark 2.4 explicitly leaves the four-parameter automorphism groups untreated, and Section 7 poses their coefficient dependence as an open question. The present theorem uses their multiplication and retains their isotropic result as prior work; its new asserted content is the global positive-parameter \(O(2)/C_2/\{1\}\) trichotomy and \(d\)-independence at \(\gamma=0\). A classical description of orthogonal centralizers by itself does not supply the explicit parameter-stratum criterion without reducing the specified multiplication table.

## Limitations
The theorem concerns only \(\gamma=0\) and \(a,b,c,d>0\), not the full \(\gamma\)-family, sign-indefinite admissible coefficients, nuclei, or automorphism group schemes over other fields. No exhaustive claim of historical priority is made; implicit treatments in older quadratic-algebra or orthogonal-centralizer literature remain possible. Self-review is not an independent mathematical audit.

## References
[1] A. Poshtkohi and S. Pumplün, *From Quaternions to Pentarnions I: Algebra, geometry, and a spin model*, arXiv:2610.31485v1, first posted 22 October 2026, https://arxiv.org/html/2610.31485v1. Specifically Section 2, Remark 2.4, Theorem 3.10 and Section 7.
