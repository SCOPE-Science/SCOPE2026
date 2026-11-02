# An explicit infinite arithmetic automorphism group for the integral dihedral quandle algebra of order eight

## Finding

Let \(B=\mathbb Z[R_8]\) be the nonassociative integral quandle algebra with free basis \(e_i\), indexed by \(i\in\mathbb Z/8\mathbb Z\), and multiplication \(e_i\star e_j=e_{2j-i}\). Define \(b_i=e_i-e_{i+4}\), with \(b_{i+4}=-b_i\), and let \(I=\langle b_0,b_1,b_2,b_3\rangle_{\mathbb Z}\). Every algebra automorphism induces an automorphism of \(B/I\cong\mathbb Z[R_4]\). The resulting quotient map is surjective and has kernel consisting *exactly* of the maps \(\kappa_{a,b,c,d}\) with \(a,b,c,d\in\mathbb Z\) satisfying

\[
\big|(2a+1)(2c+1)+8bd\big|=1.
\]

Their action on the basis of \(B\) is \(\kappa(e_i)=e_i+\delta_i\), where

\[
\begin{aligned}
\delta_0&=a b_0-b b_1+b b_3, &\delta_1&=d b_0+c b_1+d b_2,\\
\delta_2&=a b_2-b b_1-b b_3, &\delta_3&=-d b_0+d b_2+c b_3,\\
\delta_{i+4}&=-\delta_i\quad(0\le i<4).
\end{aligned}
\]

In the ordered basis \((b_0,b_1,b_2,b_3)\), these maps restrict to the matrices

\[
U(a,b,c,d)=
\begin{pmatrix}
2a+1&2d&0&-2d\\
-2b&2c+1&-2b&0\\
0&2d&2a+1&2d\\
2b&0&-2b&2c+1
\end{pmatrix},
\qquad
\det U=\big((2a+1)(2c+1)+8bd\big)^2.
\]

Every automorphism has a **unique** normal form \(\kappa_{a,b,c,d}P^vQ^\varepsilon\), with \(v\in\{0,1,2,3\}\), \(\varepsilon\in\{0,1\}\), and admissible integers \((a,b,c,d)\); here \(P(e_i)=e_{i+1}\) and \(Q(e_i)=e_{-i}\). Consequently the entire automorphism group has an explicit faithful arithmetic matrix model inside \(\operatorname{SL}_4(\mathbb Z)\), consisting of all matrices \(U(a,b,c,d)P_I^vQ_I^\varepsilon\), where \(P_I,Q_I\) are the restrictions to \(I\).

In particular, the group is **infinite**: taking \(a=c=d=0\), \(b=n\in\mathbb Z\), gives a distinct integral automorphism for every integer \(n\). Thus the natural map from the finite quandle automorphism group \(\operatorname{Aut}(R_8)\) does not account for all algebra automorphisms.

## Assumptions and scope

All automorphisms are \(\mathbb Z\)-linear bijections preserving the indicated bilinear (generally nonassociative) multiplication; no associative-unit convention is imposed. The algebra is precisely the integral dihedral quandle algebra of order eight. The parameters are unrestricted integers subject only to the displayed norm-one equation. The quotient is over the integral ring, not a finite-field reduction.

## Proof

**1. Characteristic right annihilator and quotient.** For any \(x\in B\), \(x\star b_i=0\), since \(2(i+4)=2i\pmod8\). Conversely, writing an arbitrary right factor as \(y=\sum t_ie_i\), the condition \(e_j\star y=0\) says \(t_i+t_{i+4}=0\) for \(0\le i<4\), since the four distinct outputs \(e_{2i-j}\) are linearly independent. Hence \(I=\operatorname{Ann}_r(B)\); it is characteristic. The quotient identifies \(e_{i+4}\) with \(e_i\), so \(B/I\cong\mathbb Z[R_4]\). The known classification \(\operatorname{Aut}(\mathbb Z[R_4])=\operatorname{Aff}(\mathbb Z/4\mathbb Z)\) has eight elements; this last identification is the prior result cited below. Every affine quotient map lifts via \(e_i\mapsto e_{ui+v}\) for odd \(u\) modulo eight and arbitrary \(v\), giving surjectivity.

**2. Kernel equations.** Suppose \(\kappa\) acts trivially on the quotient. Then \(\kappa(e_i)=e_i+\delta_i\), with each \(\delta_i\in I\). The right-annihilator identity shows that multiplicativity is equivalent to

\[
\delta_{2j-i}=T_j\delta_i\qquad(i,j\in\mathbb Z/8\mathbb Z),\qquad T_j(x)=x\star e_j\quad(x\in I).
\]

Directly from \(b_i\star e_j=b_{2j-i}\), with \(b_{r+4}=-b_r\), the signed-permutation operators satisfy

\[
T_{j+4}=T_j,\qquad T_{j+2}=-T_j,\qquad T_0^2=T_1^2=1,\qquad T_0T_1=-T_1T_0.
\]

Setting \(i=0,j=0\) and \(i=1,j=1\) forces \(T_0\delta_0=\delta_0\), \(T_1\delta_1=\delta_1\). The plus-one eigenspaces are respectively \(\langle b_0,b_3-b_1\rangle\) and \(\langle b_1,b_0+b_2\rangle\). These give uniquely \(\delta_0=a b_0+b(b_3-b_1)\) and \(\delta_1=c b_1+d(b_0+b_2)\). The equations with \((i,j)=(0,1),(1,2)\) then give \(\delta_2=T_1\delta_0\), \(\delta_3=-T_0\delta_1\); comparing \(j\) and \(j+2\) gives \(\delta_{i+4}=-\delta_i\). Expanding yields the four displayed formulas. Conversely, the stated four operator identities verify \(\delta_{2j-i}=T_j\delta_i\) for every \(i,j\) (reduce \(j\) modulo four and \(i\) modulo four, using the sign rules). Thus these are *all* multiplicative kernel endomorphisms over \(\mathbb Z\).

**3. Integral invertibility.** Since \(\kappa(b_i)=b_i+2\delta_i\), the restriction to \(I\) has exactly the matrix \(U\) displayed above. Elementary determinant expansion gives the square formula. In a basis of \(B\) adapted to \(I\subset B\), \(\kappa\) has a block upper triangular matrix with diagonal blocks \(U\) and the identity of the free quotient \(B/I\). Thus \(\kappa\) is bijective exactly when \(\det U=\pm1\), or equivalently \(\big|(2a+1)(2c+1)+8bd\big|=1\). Its inverse then preserves multiplication automatically by bijectivity. This proves both necessity and sufficiency.

**4. Complete group and faithful four-dimensional model.** The maps \(P(e_i)=e_{i+1}\) and \(Q(e_i)=e_{-i}\) are quandle automorphisms. Their quotient actions generate the eight-element affine group on four residues, with unique representatives \(P^vQ^\varepsilon\), \(0\le v<4\), \(0\le\varepsilon<2\). Every automorphism is therefore uniquely \(\kappa P^vQ^\varepsilon\) for a kernel element \(\kappa\) classified above.

Restriction of the full group to \(I\) is faithful: if an automorphism fixes \(I\) pointwise, then conjugating the four distinct right operators \(T_0,T_1,-T_0,-T_1\) forces its affine quotient action to fix each of the four residues. It is consequently a kernel map with \(U=1\), forcing \(a=b=c=d=0\). On \(I\), \(P\) is the signed cycle \(b_0\mapsto b_1\mapsto b_2\mapsto b_3\mapsto-b_0\), while \(Q\) maps \(b_i\mapsto b_{-i}\). Both matrices have determinant one. Since admissible \(U\) also have determinant one, the promised full image is contained in \(\operatorname{SL}_4(\mathbb Z)\).

**5. Infinitude.** Setting \(a=c=d=0\) gives \(\det U(0,n,0,0)=1\) for every \(n\in\mathbb Z\), with distinct matrices. Indeed, \(U(0,n,0,0)=1+2nN\) for a fixed nonzero integral matrix \(N\) satisfying \(N^2=0\). Hence these maps form an infinite cyclic unipotent subgroup. This completes the proof.

## Verification

Run `python3 verify.py` using only the Python standard library. The program evaluates all \(625\) parameter quadruples in \([-2,2]^4\), checks the \(64\) multiplication identities for each candidate, verifies both determinant formulas and the restriction to \(I\), tests the \(32\) affine basis permutations, and checks a \(17\)-member sample of the infinite shear family and \(81\) compositions. The expected program output is supplied as `verification_output.txt`. The universal classification rests on the preceding integer-linear proof, not on finite enumeration.

## Relationship to prior work

Bardakov, Passi and Singh determine \(\operatorname{Aut}(\mathbb Z[R_4])\), used here as the quotient identification, but not the automorphism group for \(R_8\). Sangare and Ta (2026, Section 4.3, Problem 4.14 and Corollary 4.18) explicitly leave the even-half-order case open and prove an injection \(\operatorname{Aut}(\mathbb Z[R_8])\hookrightarrow\operatorname{GL}_4(\mathbb Z)\). The present result determines the **image**, its complete arithmetic normal form, and its infinitude. It treats the first smallest unsolved even-half-order instance of that problem, not all even orders. A stronger previously implicit equivalent in older specialized quandle-ring literature cannot be categorically excluded.

## Limitations

The result is confined to the integral coefficient ring and \(R_8\); no assertion is made about arbitrary \(R_{4m}\), noncommutative base rings, or a splitting of the exact extension. The matrix model gives a full presentation by explicit parameters and products, but is not a finite abstract generators-and-relations presentation. Independent mathematical validation has not been performed.

## References

1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (first public August 3, 2026), particularly Problem 4.14 and Corollary 4.18. https://arxiv.org/abs/2608.01550
2. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (2020), Theorem 6.4 and Problem 6.5; Osaka Journal of Mathematics 59 (2022). https://arxiv.org/abs/2001.06843
