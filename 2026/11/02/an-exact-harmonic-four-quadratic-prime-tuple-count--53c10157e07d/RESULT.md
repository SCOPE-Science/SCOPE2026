# An exact harmonic four-quadratic prime-tuple count

## Finding
Let \(q\equiv7\pmod 8\) be any prime power, let \(K=\mathbb F_q\), and let \(t\in K\) satisfy \(t^2-6t+1=0\). These roots exist and are distinct because \(2\) is a square and the characteristic is odd. Define the four distinct constants \(S=\{-t,-1,1,t\}\). The number \(M_q(t)\) of monic quadratics \(f(X)\in K[X]\) for which the four polynomials \(f(X)+s\) with \(s\in S\) are all irreducible is exactly
\[
 M_q(t)=q\left\lfloor\frac{q-7}{16}\right\rfloor.
\]
This does not depend on the chosen root of the quadratic equation. It equals zero at \(q=7\) and is positive at every remaining prime power \(q\equiv7\pmod8\). The exact formula is valid for prime powers, not only prime fields.

## Assumptions and scope
The characteristic is odd. As \(q\equiv7\pmod8\), the quadratic character \(\chi\) on \(K\) satisfies \(\chi(-1)=-1\) and \(\chi(2)=1\). The equation \(t^2-6t+1=0\) has solutions \(3\pm2\sqrt2\). It has two distinct roots since its discriminant is \(32\), which is a nonzero square in these characteristics. Neither root equals \(0\), \(1\), or \(-1\); hence \(S\) consists of four distinct elements. For \(f(X)=X^2+uX+v\) put \(z=(u^2-4v)/4\). The discriminant of \(f+s\) is \(4(z-s)\). Thus all four translates are irreducible exactly when \(\chi(z-s)=-1\) for every \(s\in S\). For each \(z\), the parameter \(u\) has \(q\) choices and determines \(v\) uniquely. It suffices to count the permissible \(z\).

## Proof
Write \(P(Z)=(Z^2-1)(Z^2-t^2)\), and let \(N\) be the number of \(z\in K\) at which every \(\chi(z-s)=-1\). Introduce the product
\[
 H(z)=\prod_{s\in S}(1-\chi(z-s)).
\]
For \(z\notin S\), the value \(H(z)\) is \(16\) precisely at the desired points and zero otherwise. For \(z\in S\), the factor corresponding to \(s=z\) equals one. Therefore
\[
16N=\sum_{z\in K}H(z)-B,\quad B=\sum_{s\in S}\prod_{r\in S\setminus\{s\}}(1-\chi(s-r)).
\]

Expand \(H\). Each linear character sum vanishes. For distinct \(a,b\), the standard elementary quadratic character identity is \(\sum_z\chi((z-a)(z-b))=-1\), so the six pair terms contribute \(-6\). The four cubic terms cancel in opposite pairs under \(z\mapsto-z\): negating the variable exchanges \(S\) with itself, and multiplying a cubic polynomial by \(-1\) changes its quadratic character because \(\chi(-1)=-1\). Consequently,
\[
\sum_z H(z)=q-6+\sum_{z\in K}\chi(P(z)).
\]

We show that the quartic sum is \(-1\). Set \(A(Z)=(1-t)Z+2t\) and \(B_0(Z)=2Z+t-1\). The following polynomial identity holds whenever \(t^2-6t+1=0\):
\[
\bigl(A(Z)^2-B_0(Z)^2\bigr)\bigl(A(Z)^2-t^2B_0(Z)^2\bigr)
=-(t+1)^4 (Z^2-1)(Z^2-t^2).
\]
It can be verified by expansion; without imposing the equation for \(t\), the left side minus the right side factors as \(-2(t+1)^2(t+Z)^2(Z-1)^2(t^2-6t+1)\). The matrix \(\left(\begin{smallmatrix}1-t&2t\\2&t-1\end{smallmatrix}\right)\) has determinant \(-(t+1)^2\ne0\); hence it gives a permutation of \(\mathbb P^1(K)\). In homogeneous coordinates \(P_h(X,Y)=(X^2-Y^2)(X^2-t^2Y^2)\), the displayed identity says that its value is multiplied by \(-(t+1)^4\). This scalar is a nonsquare because \(\chi(-1)=-1\). The quadratic-character sum of \(P_h\) over projective points therefore equals its own negative, so it is zero. The point at infinity contributes \(\chi(P_h(1,0))=1\), and therefore \(\sum_{z\in K}\chi(P(z))=-1\). We conclude \(\sum_zH(z)=q-7\).

It remains to count the boundary contribution \(B\). For any \(s\ne r\) in \(S\), \(\chi(s-r)\in\{-1,1\}\). The product indexed by \(s\) in the definition of \(B\) is therefore either zero or eight, and it equals eight precisely when \(\chi(s-r)=-1\) for every other \(r\). Two different \(s\) cannot both have this property, because \(\chi(r-s)=-\chi(s-r)\). Consequently \(B\in\{0,8\}\). As \(16N=q-7-B\), divisibility by sixteen forces \(B=0\) if \(q\equiv7\pmod{16}\) and \(B=8\) if \(q\equiv15\pmod{16}\). Hence \(N=\lfloor(q-7)/16\rfloor\) in both cases. Multiplication by the \(q\) possible monic quadratic linear coefficients proves the theorem. \(\square\)

## Verification
Run `python3 verify.py` with Python 3 and no additional dependencies. It independently enumerates the character conditions, confirms the quartic sum and boundary term, and verifies the involution polynomial identity pointwise for both possible values of \(t\), over all 25 prime fields \(7\le p<500\), \(p\equiv7\pmod8\), and over \(\mathbb F_{7^3}\). The extension field is represented as \(\mathbb F_7[U]/(U^3+U+1)\); the defining cubic has no root in \(\mathbb F_7\), so it is irreducible. Expected terminal marker: `VERIFY_OK field_cases=26`. These finite checks are supplementary to the uniform proof.

## Relationship to prior work
L. Bary-Soroker, *Hardy–Littlewood tuple conjecture over large finite field* (arXiv:1206.3930, first submitted 18 June 2012), Theorem 1.1, establishes \(\pi(q,n;\mathbf a)=q^n/n^r+O_{n,r}(q^{n-1/2})\) for distinct translates. It includes degree two and four translates but not the exact count or harmonic involution; the present identity sharpens that asymptotic for the specified symmetric harmonic configuration. E. Bank and L. Bary-Soroker, *Prime polynomial values of linear functions in short intervals* (arXiv:1410.1283, first submitted 6 October 2014), gives more general asymptotic independence results, not this exact arithmetic formula. Previously known exact three-term and four-term arithmetic-progression counts provide a relevant comparison. A centered four-term progression with shifts \(\{\pm a,\pm3a\}\) would require \(t=\pm3\) or \(t=\pm1/3\); these possibilities satisfy \(t^2-6t+1=0\) in odd characteristic precisely when the characteristic is seven. Consequently the earlier arithmetic-progression result already covers the characteristic-seven subfamily, but it does not imply this harmonic formula in any of the other admissible characteristics, which form an infinite family.

## Limitations
Only the harmonic symmetric configuration \(\{-t,-1,1,t\}\) over fields of size \(7\pmod8\) is counted. Arbitrary four shifts have an elliptic character-sum contribution that need not vanish. The proof does not classify higher-degree prime polynomial tuples or claim the absence of an unlocated equivalent formula in earlier character-sum literature. The mathematical review here is not an independent audit.

## References
- L. Bary-Soroker, *Hardy–Littlewood tuple conjecture over large finite field*, arXiv:1206.3930, first submitted 2012-06-18, https://arxiv.org/abs/1206.3930.
- E. Bank and L. Bary-Soroker, *Prime polynomial values of linear functions in short intervals*, arXiv:1410.1283, first submitted 2014-10-06, https://arxiv.org/abs/1410.1283.
