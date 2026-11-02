# The exact one-or-three fiber spectrum of a nonpermutation trinomial family

## Finding
Let \(q\equiv3\pmod8\) be an odd prime power of characteristic other than \(3\). Fix \(t\in\mathbb F_q\) with \(t^2=-2\); it exists because \(\chi_q(-2)=1\). Consider
\[
F(X)=X^{2q-1}+tX^q-X\qquad (X\in\mathbb F_{q^2}).
\]
For a target \(y\) write \(m(y)=\#\{x\in\mathbb F_{q^2}:F(x)=y\}\), let \(\chi_q\) denote the quadratic character on \(\mathbb F_q\), and put \(\delta=\chi_q(3)\) and \(S=1+(q-1)(1-\delta)\). Then
\[
\#\{y:m(y)=1\}=S,\quad
\#\{y:m(y)=3\}=\frac{q^2-S}{3},\quad
\#\{y:m(y)=0\}=\frac{2(q^2-S)}{3},
\]
and no other multiplicity occurs. Thus the value-set size is \((q^2+2S)/3\). More precisely, \(m(0)=1\), and if \(\delta=-1\), every other singleton target has \(y^{q-1}\) equal to one of the two roots on the norm-one torus of \(v^2+5tv+1=0\); if \(\delta=1\), no other singleton target exists.

## Assumptions and scope
All finite fields have odd characteristic, and \(q\equiv3\pmod8\) and \(3\nmid q\). In particular \(\chi_q(2)=\chi_q(-1)=-1\). The property applies to both choices of \(t\); neither \(t=0\) nor \(t=\pm1\) is possible. The statement is about every target in \(\mathbb F_{q^2}\), not only targets in the subfield. It is not asserted for characteristic three or for other congruence classes of \(q\).

## Proof
Let \(\mu=\{u\in\mathbb F_{q^2}^{\times}:u^{q+1}=1\}\), and define \(h(u)=u^2+tu-1\), so that \(F(x)=xh(x^{q-1})\) for nonzero \(x\). If \(u\in\mu\) and \(h(u)=0\), conjugation gives \(1+tu-u^2=0\), since \(u^q=u^{-1}\). Subtracting the two equations yields \(2(1-u^2)=0\). The only possibilities are \(u=\pm1\), where \(h(\pm1)=\pm t\ne0\), a contradiction. Thus \(m(0)=1\) and \(F\) sends nonzero inputs to nonzero outputs.

Multiplication by any \(c\in\mathbb F_q^{\times}\) commutes with \(F\), hence the multiplicity for any nonzero \(y\) depends only on \(v=y^{q-1}\in\mu\). More precisely, each \(u\in\mu\) with \(u h(u)^{q-1}=v\) specifies exactly one preimage of each target with label \(v\). Consequently \(m(y)\le3\), as the following cubic reductions make explicit.

First consider \(v=\pm1\). Put
\[
\Phi(u)=u h(u)^{q-1}=\frac{1+tu-u^2}{u(u^2+tu-1)}.
\]
We have \(\Phi(1)=1\) and \(\Phi(-1)=-1\). Direct factorization of the numerator of \(\Phi(u)-1\), respectively \(\Phi(u)+1\), after removal of \(u-1\), respectively \(u+1\), yields, up to a nonzero constant, the quadratics
\[
Q_+(u)=u^2+(t+2)u+1,\qquad
Q_-(u)=u^2+(t-2)u+1.
\]
Their discriminants are \(2(t+1)^2\) and \(2(t-1)^2\), which are nonzero nonsquares in \(\mathbb F_q\). Their two roots are therefore distinct conjugates with product one, and lie in \(\mu\). Neither exceptional root coincides with the already counted root \(u=1\), respectively \(u=-1\), because coincidence would force \(t=\mp4\), hence \(18=0\) in the field. Therefore each of the \(2(q-1)\) nonzero targets with \(v=\pm1\) has exactly three preimages.

For \(v\in\mu\setminus\{\pm1\}\), set \(s=v+v^{-1}\in\mathbb F_q\) and \(\epsilon=v-v^{-1}\). Then \(\epsilon^q=-\epsilon\), \(\epsilon^2=s^2-4\) is a nonzero nonsquare in \(\mathbb F_q\), and \(s^2\ne4\). If \(F(x)=y\), put \(\tau=x^{-q}y=t+x^{q-1}-x^{1-q}=t+\epsilon U\) with unique \(U\in\mathbb F_q\). Conversely, \(\tau\ne0\) for every \(U\in\mathbb F_q\), and substitution \(x=(y/\tau)^q\) gives a bijection between preimages and roots in \(\mathbb F_q\) of the following monic cubic (the reduction of the equation in Hou's Section 3):
\[
G_s(U)=U^3-U^2+\frac{2-2ts}{s^2-4}U+\frac{2}{s^2-4}.
\]
The usual discriminant calculation, reducing powers of \(t\) with \(t^2=-2\), gives
\[
\operatorname{Disc}(G_s)=-\frac{16(s+5t)^2}{(s^2-4)^3}.
\]
Because \(\chi_q(-1)=\chi_q(s^2-4)=-1\), this is a nonzero square whenever \(s\ne-5t\). The Frobenius permutation on the three distinct roots of a separable cubic is even exactly when its discriminant is a square. Hence a cubic with such a discriminant has either three \(\mathbb F_q\)-roots or none: it cannot have exactly one. Accordingly, \(m(y)\in\{0,3\}\) for these nonspecial \(v\).

At \(s=-5t\), one has \(s^2-4=-54\ne0\), and the cubic simplifies exactly to
\[
G_s(U)=\bigl(U-\tfrac13\bigr)^3.
\]
Thus every target with this label has a unique preimage. The equation \(s=-5t\) on \(\mu\) is \(v^2+5tv+1=0\), with discriminant \(-54\), whose quadratic character is \(\chi_q(-54)=\chi_q(3)=\delta\). If \(\delta=-1\), it has two distinct conjugate inverse roots, both in \(\mu\), accounting for exactly \(2(q-1)\) nonzero singleton targets. If \(\delta=1\), both roots are in \(\mathbb F_q\), and cannot lie in \(\mu\), as \(\mathbb F_q\cap\mu=\{\pm1\}\) and neither is a root when the characteristic is not three. Counting zero then gives \(S=1+(q-1)(1-\delta)\) singleton targets.

Every other nonzero target has zero or three preimages. Summing their multiplicities over all \(q^2\) targets gives \(q^2=S+3T\), where \(T\) is the number of triple fibers. Thus \(T=(q^2-S)/3\), and subtracting \(S+T\) from the number of targets gives \(2(q^2-S)/3\) empty fibers. This proves the complete assertion.

## Verification
The accompanying standalone `verify.py` independently enumerates all polynomial values in the quadratic field \(\mathbb F_{p^2}=\mathbb F_p[i]/(i^2+1)\) for primes \(p=11,19,43,59\), and for both signs of a square root \(t^2=-2\). It compares all target-fiber multiplicities with the exact formulas and independently identifies the unique-preimage target lines. The polynomial discriminant identity can also be checked by symbolic expansion and reduction modulo \(t^2+2\). These finite tests support, but are not used as substitutes for, the proof for arbitrary prime powers.

## Relationship to prior work
Hou's 2013 paper introduced and classified permutations of precisely this trinomial: a permutation occurs for odd \(q\) only if \(q\equiv1\pmod8\) and \(t^2=-2\). Its Section 3 supplies the underlying cubic reduction and discriminant formula in the permutation case. The theorem above treats the complementary nonpermutation regime \(q\equiv3\pmod8\) and counts every fiber, including the repeated-root exceptions that arise precisely there. Hou's 2014 sequel classifies permutation cases with more general coefficients, but does not state the present value-set census. The new statement is not a reformulation of the permutation criterion, since the latter neither counts nonempty fibers nor identifies one-versus-three multiplicities.

## Limitations
No claim is made for characteristic three (where \(G_s\) degenerates differently), for \(q\not\equiv3\pmod8\), or for parameters not satisfying \(t^2=-2\). The theorem proves counts of fibers, not a closed-form listing of every triple-preimage target. Although no equivalent fiber-census theorem was found in the inspected literature and database searches, more general results on 3-to-1 polynomials or value sets could subsume this formula; an independent literature audit has not been performed.

## References
1. Xiang-dong Hou, *A Class of Permutation Trinomials over Finite Fields*, arXiv:1303.0568 (initial version 2013-03-03), especially Theorem 1.1 and Section 3, https://arxiv.org/abs/1303.0568.
2. Xiang-dong Hou, *Determination of a Type of Permutation Trinomials over Finite Fields, II*, arXiv:1404.1822 (initial version 2014-04-07), especially Theorems A and B, https://arxiv.org/abs/1404.1822.
