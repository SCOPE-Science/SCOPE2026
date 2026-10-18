# Full dihedral automorphism groups of a characteristic-three Artin–Schreier family

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). For any integer \(m\geq5\) with \(m\equiv2\pmod3\) and any \(\lambda\in k^\times\), let \(C_{m,\lambda}\) be the unique smooth projective curve with function field defined by
\[
y^3-y=\frac{\lambda}{x^m-1}.
\]
Then
\[
g(C_{m,\lambda})=\gamma_3(C_{m,\lambda})=2m-2,
\qquad \operatorname{Aut}_k(C_{m,\lambda})\cong D_{3m},
\qquad |D_{3m}|=6m.
\]
Here \(\gamma_3\) means the geometric \(3\)-rank, and \(D_{3m}=C_{3m}\rtimes C_2\) denotes the dihedral group of order \(6m\), with the involution acting by inversion. In particular, the genus-eight model at \(m=5\), which has a cyclic subgroup of order \(15\) in the originating classification, has exactly \(30\) geometric automorphisms.

## Assumptions and scope
The ground field is algebraically closed of characteristic precisely \(3\), the pole parameter \(\lambda\) is nonzero, and the integer \(m\) ranges over \(m\geq5\) with \(m\equiv2\pmod3\). The notation refers to the smooth projective model, not the potentially singular affine plane closure. Write \(\mu_m=\{a\in k^\times:a^m=1\}\), a reduced set of \(m\) points because \(3\nmid m\).

## Proof
**1. Genus and degree-three map.** The rational function \(\lambda/(x^m-1)\) has exactly \(m\) simple poles, at the points of \(\mu_m\), and no pole at infinity. A nonzero simple pole is impossible for an Artin–Schreier coboundary \(h^3-h\), whose nonzero poles have orders divisible by \(3\). Thus the separable Artin–Schreier extension has degree \(3\) and defines a geometrically integral smooth projective curve. Each simple pole has ramification index \(3\) and different exponent \((3-1)(1+1)=4\). Riemann–Hurwitz gives
\[
2g-2=3(-2)+4m=-6+4m,
\qquad g=2m-2.
\]
The Deuring–Shafarevich formula for an Artin–Schreier cover with \(m\) poles gives \(\gamma_3=(3-1)(m-1)=2m-2\). In particular, the curve is ordinary.

**2. The degree-three rational subfield is unique.** We prove the special fact needed here, without assuming that every Artin–Schreier deck group is automatically normal. Let \(K=k(C_{m,\lambda})\), and let \(K_1=k(x)\subset K\). Suppose \(K_2\subset K\) is another rational subfield with \([K:K_2]=3\). The compositum \(L=K_1K_2\) is intermediate between \(K_1\) and \(K\); as \([K:K_1]=3\) is prime, either \(L=K_1\) or \(L=K\). If \(L=K_1\), then \(K_2\subseteq K_1\) and \([K_1:K_2]=[K:K_2]/[K:K_1]=1\), so \(K_1=K_2\). If \(L=K\), the two degree-three rational functions yield a birational map from \(C_{m,\lambda}\) to an integral divisor of bidegree \((3,3)\) on \(\mathbb P^1\times\mathbb P^1\). Such a divisor has arithmetic genus \((3-1)(3-1)=4\), hence normalization genus at most \(4\). This contradicts \(g=2m-2\ge8\). Therefore \(k(x)\) is the unique rational subfield of index \(3\). This argument uses function-field degrees and arithmetic genus and works in characteristic \(3\).

Every geometric automorphism of \(C_{m,\lambda}\) consequently restricts to an automorphism of \(k(x)\), hence induces a fractional linear transformation of \(\mathbb P^1_x\). The kernel of this restriction is exactly the Galois group of the Artin–Schreier extension, namely the three translations \(y\mapsto y+t\) with \(t\in\mathbb F_3\).

**3. Rigidity of the branch set.** A descended base transformation must preserve the branch set \(\mu_m\). The associated homogeneous binary form is \(F(U,V)=U^m-V^m\). Its binary Hessian satisfies
\[
\begin{split}
H_F&=F_{UU}F_{VV}-F_{UV}^{2}\\
&=-m^2(m-1)^2\,U^{m-2}V^{m-2}.
\end{split}
\]
The coefficient is nonzero in characteristic \(3\), because \(m\equiv2\pmod3\). Under an invertible linear substitution the Hessian transforms by the square of the determinant, so a projective transformation stabilizing the reduced zero divisor of \(F\) must also preserve the zero set of \(H_F\). The latter set is exactly \(\{0,\infty\}\). Every such transformation therefore has form \(x\mapsto ax\) or \(x\mapsto a/x\). Preserving \(\mu_m\) forces \(a^m=1\). Thus the branch-set stabilizer has exactly \(2m\) elements, and
\[
|\operatorname{Aut}_k(C_{m,\lambda})|\le3\cdot2m=6m.
\]

**4. Every possible lift exists.** Choose a primitive \(m\)-th root \(\zeta\) and a solution \(c\in k\) of \(c^3-c=-\lambda\) (existence follows from algebraic closedness). The transformations
\[
R:(x,y)\longmapsto(\zeta x,y),\qquad
T:(x,y)\longmapsto(x,y+1),\qquad
S:(x,y)\longmapsto(x^{-1},-y+c)
\]
preserve the function-field relation. In particular,
\[
\frac{\lambda}{x^{-m}-1}
=-\lambda-\frac{\lambda}{x^m-1}
=(-y+c)^3-(-y+c).
\]
They satisfy \(R^m=T^3=S^2=1\), \(RT=TR\), \(SRS=R^{-1}\), and \(STS=T^{-1}\). Because \(3\nmid m\), \(\langle R,T\rangle\cong C_m\times C_3\cong C_{3m}\); adding \(S\) gives the dihedral group \(D_{3m}\) of order \(6m\). This reaches the upper bound, proving equality and exhausting all geometric automorphisms. \(\square\)

## Verification
The standalone script `verify.py` checks the exact rational-function involution identity, the binary-Hessian identity, nonvanishing of its coefficient modulo \(3\), the genus arithmetic, and dihedral group relations via exact permutation enumeration at \(m=5,8,11,14\). The script prints `VERIFY_OK` on success. These finite checks corroborate, but do not substitute for, the all-\(m\) proof in the preceding section.

## Relationship to prior work
Kazemifard and Tafazolian, *Cyclic automorphisms beyond the canonical bound* (arXiv:2610.04702v1, first publicly posted October 3, 2026), classify cyclic subgroups exceeding the canonical threshold. Their Proposition 4.5, Theorem 4.8, and Table 1 include the characteristic-three genus-eight model with a cyclic subgroup of order \(15\). Those statements determine the existence and form of the large cyclic action, not the complete geometric automorphism group. The present result computes that group exactly and extends the calculation to infinitely many degrees outside the boundary case.

Tafazolian and Kazemifard, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms* (arXiv:2610.13279v1, first posted October 9, 2026), develop descent and uniqueness of Artin–Schreier rational subfields outside exceptional families and construct different models with minimal automorphism group. Their Theorem 1.1 is an existence classification, not a formula for this highly symmetric family. The uniqueness step here is proved directly from the genus and the bidegree \((3,3)\) bound. The binary-Hessian argument then identifies the exact branch-set stabilizer and supplies the missing upper bound.

## Limitations
This theorem requires characteristic \(3\), nonzero \(\lambda\), and \(m\equiv2\pmod3\) with \(m\ge5\); the Hessian method used here does not cover all residue classes. It classifies geometric automorphisms over an algebraic closure, not rational automorphisms over a prescribed finite base field. It does not compute the full integral or \(\ell\)-adic cohomology representation, quotient ramifications for all subgroups, or moduli identifications among different parameters. The literature comparison is not proof of global priority: a generalized automorphism theorem for Artin–Schreier covers could implicitly contain this specialization.

## References
1. A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1 (2026), especially Proposition 4.5, Theorem 4.8 and Table 1.
2. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms*, arXiv:2610.13279v1 (2026), especially Section 2 and Theorem 1.1.
3. R. Hartshorne, *Algebraic Geometry*, Springer (1977), for arithmetic genus and normalization of curves on \(\mathbb P^1\times\mathbb P^1\).
4. H. Stichtenoth, *Algebraic Function Fields and Codes*, 2nd ed., Springer (2009), for Artin–Schreier ramification and the genus formula.
