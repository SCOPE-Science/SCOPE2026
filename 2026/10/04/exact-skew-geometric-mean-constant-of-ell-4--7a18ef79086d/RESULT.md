# Exact skew geometric mean constant of \(\ell_4\)
## Finding
For every index set \(I\) with \(|I|\ge 2\) and every \(lpha,eta>0\), define
\[
A_{lpha-eta}(X)=\sup_{x,y\in S_X}rac{\|lpha x+eta y\|+\|eta x-lpha y\|}{2}.
\]
Then
\[
A_{lpha-eta}(\ell_4(I))=\left(lpha^4+3lpha^2eta^2+eta^4+lphaeta\sqrt{(lpha^2+2eta^2)(2lpha^2+eta^2)}ight)^{1/4}.
\]
Equivalently, if
\[
M_{lpha,eta}=egin{pmatrix}lpha&eta\ eta&-lpha\end{pmatrix},
\]
then \(A_{lpha-eta}(\ell_4(I))=\|M_{lpha,eta}\|_{\ell_4^2	o\ell_4^2}\). In particular, \(A_{1-1}(\ell_4(I))=2^{3/4}\).

## Assumptions and scope
The scalar field is real, \(lpha,eta>0\), and \(I\) has at least two coordinates. No finite-dimensionality of \(\ell_4(I)\) is assumed. The claim concerns the unrestricted skew geometric mean constant introduced by Ni, Liu and Zhou, not their isosceles-orthogonality-restricted variant.

## Proof
Write \(m=\|M_{lpha,eta}\|_{\ell_4^2	o\ell_4^2}\). For unit vectors \(x,y\in\ell_4(I)\), put \(P=\|lpha x+eta y\|_4\) and \(Q=\|eta x-lpha y\|_4\). Coordinatewise application of the two-dimensional operator gives
\[
P^4+Q^4\le m^4\sum_{i\in I}(|x_i|^4+|y_i|^4)=2m^4.
\]
The power-mean inequality therefore yields
\[
rac{P+Q}2\le\left(rac{P^4+Q^4}2ight)^{1/4}\le m.
\]
Thus \(A_{lpha-eta}(\ell_4(I))\le m\).

Conversely, let \((u,v)
e(0,0)\) attain the finite-dimensional operator norm \(m\), and put \(s=(|u|^4+|v|^4)^{1/4}\). On any two distinct coordinates of \(I\), define
\[
x=s^{-1}(u,v),\qquad y=s^{-1}(v,-u).
\]
Both are unit vectors. The two transformed vectors \(lpha x+eta y\) and \(eta x-lpha y\) have the same multiset of absolute coordinate values, and each has norm \(m\). Hence their averaged norm is \(m\), proving \(A_{lpha-eta}(\ell_4(I))=m\).

It remains to compute \(m\). For a real pair \((u,v)\), set \(r=u^2-v^2\) and \(q=2uv\). Every nonzero pair \((r,q)\) arises from some real \((u,v)\), since \(r+iq=(u+iv)^2\). Moreover,
\[
u^4+v^4=rac{2r^2+q^2}2.
\]
Writing \(c=lpha^2+eta^2\) and \(d=lpha^2-eta^2\), direct expansion gives
\[
\|M_{lpha,eta}(u,v)\|_4^4
=rac12\left[c^2(r^2+q^2)+(dr+2lphaeta q)^2ight].
\]
Thus \(m^4\) is the largest generalized eigenvalue of the quadratic form with matrix
\[
egin{pmatrix}
2(lpha^4+eta^4)&2lphaeta(lpha^2-eta^2)\
2lphaeta(lpha^2-eta^2)&lpha^4+6lpha^2eta^2+eta^4
\end{pmatrix}
\]
relative to \(\operatorname{diag}(2,1)\). Its characteristic equation, after removing a nonzero scalar factor, is
\[
\lambda^2-2(lpha^4+3lpha^2eta^2+eta^4)\lambda+(lpha^2+eta^2)^4=0.
\]
The discriminant term satisfies
\[
(lpha^4+3lpha^2eta^2+eta^4)^2-(lpha^2+eta^2)^4
=lpha^2eta^2(lpha^2+2eta^2)(2lpha^2+eta^2).
\]
Taking the larger root gives exactly the stated formula.

## Verification
The upper bound is dimension-free and uses only the coordinatewise \(\ell_4\) decomposition. The lower bound is attained on two coordinates, so the same value holds for every \(I\) with \(|I|\ge2\). The algebraic identities in the generalized-eigenvalue calculation are independently expanded with exact integer-coefficient polynomial arithmetic in `verify.py`; it returns `VERIFY_OK`.

## Relationship to prior work
Ni, Liu and Zhou introduced \(A_{lpha-eta}(X)\), established the Hilbert-space value \(\sqrt{lpha^2+eta^2}\), the general bounds \(\sqrt{lpha^2+eta^2}\le A_{lpha-eta}(X)\lelpha+eta\), and exact examples for the square plane and a mixed \(\ell_\infty\)-\(\ell_1\) plane. Their later journal version retains those concrete examples. The inspected source does not give an exact \(\ell_4\) value or the operator-norm reduction above. Targeted searches for the invariant together with \(\ell_4\), its two-parameter notation, and the closed algebraic expression did not locate a published formula covering this claim.

## Limitations
This result is specific to exponent \(4\); the quadratic reduction through \((u^2-v^2,2uv)\) is special to the fourth power and does not by itself give a closed formula for general \(\ell_p\). The literature search cannot prove absolute novelty, and future or poorly indexed work could contain an equivalent formula.

## References
1. Q. Ni, Q. Liu and Y. Zhou, *Skew geometric mean constants in Banach spaces*, preprint posted 18 August 2023, DOI 10.22541/au.169235474.44030928/v1.
2. Q. Ni, Q. Liu and Y. Zhou, *Some aspects of new skew geometric constants in Banach spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI 10.7153/mia-2025-28-22.
