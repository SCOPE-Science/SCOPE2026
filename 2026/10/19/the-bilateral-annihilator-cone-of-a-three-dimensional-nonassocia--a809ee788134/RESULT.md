# The bilateral annihilator cone of a three-dimensional nonassociative deformation

## Finding

Let \(K\) be any field, \(t\in K^\times\), and let \(A_t=K1\oplus Ki\oplus Kj\) be the unital algebra with \(i^2=j^2=-1\), \(ij=0\), and \(ji=t(i+j)\). Put
\[
S_t=\{x\in A_t:\; \text{there exist }y,z\ne0\text{ with }xy=0\text{ and }zx=0\}.
\]
Thus the witnesses for left and right annihilation may be different. For \(v\in A_t\), write \(Kv\) for the line spanned by \(v\), including zero.

If \(\operatorname{char}K\ne2\), define the sets
\[
Z_1=\{r\in K:r^2+1=0\},\quad Z_2=\{r\in K:r^2+2=0\},\quad Z_k=\{r\in K:r^2+tr+2=0\}.
\]
Then \(S_t\) is **exactly** the union of the following mutually distinct lines:
\[
K(i+j),\qquad \bigcup_{r\in Z_k}K(r1+i+j),\qquad
\bigcup_{r\in Z_1}\bigl(K(r1+i)\cup K(r1+j)\bigr),\qquad
\bigcup_{r\in Z_2}K(r1+i-j).
\]
If \(\operatorname{char}K=2\), the answer instead consists of precisely four distinct lines:
\[
S_t=K(i+j)\cup K(t1+i+j)\cup K(1+i)\cup K(1+j).
\]
For \(K=\mathbb F_q\) of odd order, let \(\chi\) be the quadratic character, with \(\chi(0)=0\). Then
\[
\boxed{|S_t|=1+(q-1)\bigl(5+2\chi(-1)+\chi(-2)+\chi(t^2-8)\bigr).}
\]
In even characteristic, \(|S_t|=1+4(q-1)\). These cones have at most nine distinct projective directions. The bound is sharp: for \(K=\mathbb F_9\) and \(t=1\), the number of lines is nine and \(|S_t|=73\). For odd \(q\), exactly \(q-1\) elements of \(S_t\) admit a two-sided multiplicative inverse; for even \(q\), none do.

## Assumptions and scope

All products are binary in the displayed order: no associativity is assumed. The parameter is nonzero. A two-sided inverse of \(x\) means \(xy=yx=1\) for the same \(y\); an annihilator condition is separate. The line theorem holds for every field. The explicit cardinality, quadratic-character statement and inverse-count refinement concern finite fields. We make no assertion about a **common** nonzero annihilator \(y\) with both \(xy=yx=0\), and none about multiplicative regularity in other nonassociative families.

## Proof

Write \(x=a1+bi+cj\) and \(y=d1+ei+fj\). Bilinearity gives
\[
xy=(ad-be-cf)1+(ae+bd+tce)i+(af+cd+tce)j.
\]
Let \(L_x(y)=xy\), \(R_x(y)=yx\). In the ordered basis \((1,i,j)\),
\[
L_x=\begin{pmatrix}a&-b&-c\\b&a+tc&0\\c&tc&a\end{pmatrix},\qquad
R_x=\begin{pmatrix}a&-b&-c\\b&a&tb\\c&0&a+tb\end{pmatrix}.
\]
An element belongs to \(S_t\) if and only if **both** determinants vanish, since each operator is an endomorphism of a three-dimensional vector space. Direct determinant expansion yields
\[
\begin{aligned}
D_L&=a^3+t a^2c+a(b^2+c^2)+tc^3-tbc^2,\\
D_R&=a^3+t a^2b+a(b^2+c^2)+tb^3-tb^2c,\\
D_L-D_R&=-t(b-c)(a^2+b^2+c^2).
\end{aligned}
\]
The last equality is a polynomial identity over \(\mathbb Z[a,b,c,t]\) and hence is valid in every characteristic. Since \(t\ne0\), a simultaneous zero necessarily has either \(b=c\) or \(a^2+b^2+c^2=0\).

On \(b=c\) the common determinant becomes
\[
D_L=D_R=a(a^2+tab+2b^2).
\]
This contributes \(K(i+j)\) and the root lines \(K(r1+i+j)\), \(r^2+tr+2=0\). For the other branch \(a^2+b^2+c^2=0\), the determinant simplifies to
\[
D_L=D_R=-tbc(b+c).
\]
The alternatives \(c=0\), \(b=0\), and \(b+c=0\) give respectively
\[
K(r1+i),\ r^2+1=0;\quad
K(r1+j),\ r^2+1=0;\quad
K(r1+i-j),\ r^2+2=0.
\]
These implications are reversible; every displayed line satisfies both determinant equations. In odd characteristic, their nonzero projective directions are distinct: the \(i\)- and \(j\)-axis lines have one of \(b,c\) zero; the diagonal and antidiagonal lines have \(b=c\ne0\) and \(b=-c\ne0\) respectively and therefore cannot coincide. Within each family, distinct roots give distinct directions. The extra line \(K(i+j)\) is not a \(Z_k\)-line because \(2\ne0\).

In characteristic two, the quadratic \(r^2+1\) has exactly one root \(r=1\), \(r^2+tr+2=r(r+t)\) has distinct roots \(0,t\), and \(r^2+2=r^2\) has only root zero. The antidiagonal equals the diagonal, and the root-zero \(Z_k\)-line equals \(K(i+j)\). After removing these duplications the four stated lines remain; their directions are distinct since \(t\ne0\).

Distinct one-dimensional \(K\)-subspaces intersect only at zero. In an odd-order finite field the three root counts are, respectively, \(1+\chi(-1)\), \(1+\chi(-2)\), and \(1+\chi(t^2-8)\); the last follows from completing the square because \(2\) is invertible. There are therefore \(5+2\chi(-1)+\chi(-2)+\chi(t^2-8)\) lines, yielding the formula by adding \(q-1\) nonzero points for each and counting zero once. In even characteristic the four-line formula gives the stated count. The maximum nine follows from the upper bound of two roots per quadratic. It is attained over \(\mathbb F_9\) with \(t=1\), since \(-1\), \(-2\), and \(1-8\) are all nonzero squares there.

For clarity, the inverse locus used in the last argument follows directly from the same multiplication law, without assuming associativity. If \(xy=yx=1\) with \(x=a1+bi+cj\), \(y=d1+ei+fj\), subtraction gives \(ce=bf\). When \(bc\ne0\) we may write \(e=\lambda b\), \(f=\lambda c\). The two non-scalar equations of \(xy=1\) then give \(d+\lambda(a+tc)=d+\lambda(a+tb)=0\). If \(\lambda=0\), these imply \(d=0\), contradicting \(xy=1\); hence \(b=c\). When \(bc=0\) the element already lies in one of the two axis planes. Conversely in any of the three planes direct multiplication with the quadratic conjugate shows that an inverse exists exactly when the corresponding norm is nonzero. In the diagonal plane, the inverse of \(a1+b(i+j)\) is \(((a+tb)1-b(i+j))/(a^2+tab+2b^2)\).

For the inverse refinement, any two-sided invertible element lies in one of the three quadratic subalgebras \(K1+Ki\), \(K1+Kj\), \(K1+K(i+j)\): equality of the non-scalar coordinates of \(xy\) and \(yx\) for an inverse \(y\) forces \(bc(b-c)=0\), followed by the familiar quadratic inverse identity. In each axis plane the inverse criterion is \(a^2+b^2\ne0\), and in the diagonal plane it is \(a^2+tab+2b^2\ne0\). Every common-singular axis root line has norm zero, as do the diagonal \(Z_k\)-lines. The antidiagonal nonzero lines lie in none of these subalgebras in odd characteristic. Finally on \(K(i+j)\) the norm is \(2b^2\), nonzero for nonzero \(b\) precisely in odd characteristic. Hence \(S_t\) contains exactly \(q-1\) two-sided units for odd \(q\) and none in characteristic two.

## Verification

The standalone `verify.py` implements the field multiplication, the actual algebra product and both multiplication matrices, and compares determinant singularity against the independent polynomial/line criterion for every element. It enumerates \(56\) nonzero parameter choices across fields of orders \(2,3,4,5,7,8,9,11,16\). For field orders at most five it additionally searches for annihilating witnesses directly on both sides. All tests passed. Reproduce with `python3 verify.py` in the extracted directory. This finite census corroborates, but does not replace, the symbolic proof for all fields and parameters.

## Relationship to prior work

Bermejo Valdés (2026, arXiv:2610.12483) introduced the real algebra and its nonzero-parameter family, proved the real two-sided-inverse classification and supplied the individual left and right determinant loci for the base member \(t=1\); those computations are prerequisites, not novelties of the present result. The new assertion concerns their **intersection** for all ground fields and all nonzero parameters, its unexpectedly reducible decomposition into at most nine lines, the exact finite-field character formula, and its characteristic-two collapse. Existing finite-field work on subalgebras and two-sided units of this deformation determines a different invariant; neither a count of the unit locus nor a count of subalgebras determines the intersection of the two determinant cubics. No claim is made to be the first to calculate the individual cubic determinants or the two-sided inverse locus.

## Limitations

The parameter \(t=0\) is excluded because the determinant difference loses its factor separating the two branches. The line decomposition is a set-theoretic statement about \(K\)-rational points; no assertion about multiplicities or nonreduced scheme structures is made. The original literature provides a closely related determinant calculation, so priority for equivalent reformulations beyond inspected sources remains an open bibliographic risk. Verification is computational over nine field orders plus the symbolic argument; independent mathematical assessment has not been undertaken.

## References

1. Alejandro Jesús Bermejo Valdés, *Complex slices, inverses, and deformations of a three-dimensional real algebra*, arXiv:2610.12483v1, first public version 2026-09-13. https://arxiv.org/abs/2610.12483
2. K. Abdurasulov, M. Eraliyeva, I. Kaygorodov, *Unital three-dimensional structurable algebras: classification, properties and AK-construction*, arXiv:2603.04391 (background classification restricted to structurable algebras). https://arxiv.org/abs/2603.04391
