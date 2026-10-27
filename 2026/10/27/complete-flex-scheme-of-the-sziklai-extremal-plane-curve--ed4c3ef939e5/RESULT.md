# Complete flex scheme of the Sziklai extremal plane curve

## Finding
Let \(q=p^e\ge3\), where \(p\) is an odd prime, and consider the smooth plane degree-\(q\) curve \(C_q\) over \(\mathbb F_q\) given by
\[
F=X^q-XZ^{q-1}+X^{q-1}Y-Y^q=0.
\]
Write \(P_0=[0:0:1]\) and \(Q_t=[1:t:0]\) for the \(q\) distinct solutions of \(t^q-t=1\) in \(\overline{\mathbb F}_q\). The full scheme-theoretic intersection of \(C_q\) with its classical projective Hessian is the divisor
\[
C_q\cdot\{\det(\operatorname{Hess}F)=0\}
= q(2q-3)P_0+(q-3)\sum_{t^q-t=1}Q_t.
\]
In particular, if \(q>3\), these \(q+1\) points are **all** the geometric inflection points; for \(q=3\), the sole geometric inflection point is \(P_0\). Tangent contact at \(P_0\) is exactly \(q\), while contact at each \(Q_t\) is exactly \(q-1\); every other tangent has contact exactly two. More precisely,
\[
C_q\cdot\{X=0\}=qP_0,\qquad
C_q\cdot\{Y-tX=0\}=P_0+(q-1)Q_t.
\]
Thus every inflection tangent belongs to the pencil through \(P_0\). Under the \(q\)-power Frobenius, the \(q\) points \(Q_t\) form exactly \(q/p\) disjoint cycles of length \(p\); none is \(\mathbb F_q\)-rational, and all are defined over \(\mathbb F_{q^p}\). This gives a complete arithmetic and scheme-theoretic description of the exceptional osculation of the classical Sziklai extremizer.

## Assumptions and scope
The base field is \(\mathbb F_q\) of **odd characteristic** with \(q\ge3\); geometric points are taken over its algebraic closure. A flex means a smooth point whose tangent line intersects the curve to order at least three. For \(q=3\), the \(Q_t\) have contact two and are not flexes. The Hessian is the ordinary determinant of the three-by-three matrix of second homogeneous partial derivatives; the assertion is about its intersection divisor on the smooth curve, not an unasserted intrinsic characteristic-free Weierstrass scheme. This curve is the standard Sziklai-bound extremizer of Homma–Kim. Their point bound and classification are background, not new claims.

## Proof
Because \(q=0\) in characteristic \(p\) and \(q-1=-1\), the first derivatives are
\[
F_X=-Z^{q-1}-X^{q-2}Y,\quad F_Y=X^{q-1},\quad F_Z=XZ^{q-2}.
\]
If the gradient vanished then \(X=0\), whence the equation forces \(Y=0\), and at \(P_0\) the derivative \(F_X=-1\) is nonzero. Hence \(C_q\) is smooth. Direct differentiation gives the Hessian matrix
\[
\begin{pmatrix}
2X^{q-3}Y&-X^{q-2}&Z^{q-2}\\
-X^{q-2}&0&0\\
Z^{q-2}&0&-2XZ^{q-3}
\end{pmatrix},
\]
whose determinant is exactly \(2X^{2q-3}Z^{q-3}\). The coefficient \(2\) is invertible because \(p\) is odd. On \(X=0\), the defining equation becomes \(-Y^q=0\), so the full intersection divisor is \(qP_0\). On \(Z=0\), setting \(X=1\) gives \(1+t-t^q=0\), whose derivative in \(t\) is \(-1\), and hence there are exactly \(q\) distinct geometric points \(Q_t\), each with multiplicity one. Multiplying these intersections by the displayed Hessian exponents proves the divisor identity. Its degree is \(q(2q-3)+q(q-3)=3q(q-2)\), the required Bézout degree.

At \(P_0\) the tangent is \(X=0\); its restriction is \(-Y^q\), proving contact \(q\). At \(Q_t\), the first derivatives give tangent \(Y-tX=0\). Substituting \(Y=tX\) into \(F\) and using \(t^q-t=1\) yields \(F|_{Y=tX}=-XZ^{q-1}\). Thus the complete tangent-line intersection is \(P_0+(q-1)Q_t\). For a smooth plane curve in odd characteristic, a tangent has contact at least three precisely where the homogeneous Hessian vanishes, provided its degree minus one is invertible in the field; here \(q-1=-1\ne0\). Consequently there are no other flexes and all remaining tangent contacts equal two.

Finally, if \(t^q-t=1\), then \((t^q)^q-t^q=1\); explicitly Frobenius sends \(t\) to \(t+1\). Its \(r\)-th iterate gives \(t+r\), returning to \(t\) first when the positive integer \(r\) is divisible by \(p\). Hence each orbit has length \(p\), the number of such orbits is \(q/p\), and their points are defined over \(\mathbb F_{q^p}\) but no proper subextension of degree dividing \(p\). No finite-field census is used as an infinite proof.

## Verification
The accompanying `verify.py` recomputes the homogeneous second derivatives and the three-by-three determinant in a sparse polynomial ring over the relevant prime fields, rather than assuming the factored Hessian. It checks representatives \(q=3,5,7,9,11,13,25,27\), the exact tangent substitutions, degrees, and smoothness simplification. Run `python3 verify.py`; successful output ends in `VERIFY_OK`. The **proof above** is symbolic in arbitrary odd \(q\); sampled arithmetic is only a reproducibility check.

## Relationship to prior work
Homma–Kim's 2009 study supplies a degree-\(q\) smooth Sziklai-bound example, and their 2012 uniqueness theorem identifies the standard displayed normal form and its \(q(q-1)+1\) rational points. Neither paper's bound or uniqueness is part of this claim. The result here classifies the full Hessian divisor, extraordinary tangent-contact multiplicities, and Frobenius orbit decomposition of the geometric inflection support. The searched abstracts and accessible full-text material did not exhibit this classification; the full text of the 2012 uniqueness paper could not be accessed during the comparison, so the novelty conclusion has an explicit limitation.

## Limitations
This statement is restricted to odd characteristic and the specified degree-\(q\) extremal curve, not arbitrary Sziklai extremizers in other degrees. The ordinary Hessian intersection divisor is specified without claiming an identification with all characteristic-dependent Hasse-Wronskian structures. The novelty comparison is best-knowledge, not an independent literature certification, and may be affected by inaccessible historical full text. No independent mathematical audit has been performed.

## References
1. M. Homma and S. J. Kim, *Sziklai's conjecture on the number of points of a plane curve over a finite field II*, arXiv:0907.1325 (first public version 2009-07-08), especially Section 5; https://arxiv.org/html/0907.1325v2.
2. M. Homma and S. J. Kim, *The uniqueness of a plane curve of degree q attaining Sziklai's bound over Fq*, Finite Fields Appl. 18 (2012), 567–580, DOI:10.1016/j.ffa.2011.12.002; https://doi.org/10.1016/j.ffa.2011.12.002.
