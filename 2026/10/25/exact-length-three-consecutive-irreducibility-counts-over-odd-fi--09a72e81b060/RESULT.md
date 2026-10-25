# Exact length-three consecutive irreducibility counts over odd finite fields

## Finding

Let \(q\) be an odd prime power and \(\mathbb F_q\) the field with \(q\) elements. For each \((u_0,u_1,u_2,u_3)\in(\mathbb F_q^\times)^4\), set
\[
f_j(X)=\sum_{i=0}^{j}u_iX^i,\qquad j\in\{1,2,3\}.
\]
Write \(I_3(q)\) for the number of coefficient tuples for which all three polynomials are irreducible over \(\mathbb F_q\). Then
\[
I_3(q)=
\begin{cases}
\dfrac{(q-1)^4}{6},&q\equiv1\pmod3,\\[4pt]
\dfrac{(q-1)^2(q-3)(q+1)}6,&q\equiv2\pmod3,\\[4pt]
\dfrac{q(q-1)^3}{6},&3\mid q.
\end{cases}
\]
The first two cases describe a congruence-class split; the characteristic-three formula covers every extension field of characteristic three.

More precisely, let \(A_q\) be the set of \(a\in\mathbb F_q\) such that \(X^2+X+a\) is irreducible and set
\[
C_q(a)=\#\{t\in\mathbb F_q:X^3+X^2+aX+t\text{ is irreducible}\}.
\]
Then \(\#A_q=(q-1)/2\). For \(a\in A_q\), the exact values are
\[
C_q(a)=
\begin{cases}
(q-1)/3,&q\equiv1\pmod3,\\
(q+1)/3,&q\equiv2\pmod3,\ a\ne1/3,\\
0,&q\equiv2\pmod3,\ a=1/3,\\
q/3,&3\mid q.
\end{cases}
\]
The exceptional parameter \(a=1/3\) belongs to \(A_q\) if and only if \(q\equiv2\pmod3\) (when the characteristic is not three).

## Assumptions and scope

All coefficients \(u_i\) are nonzero, as in the consecutive irreducible polynomial-sequence definition of Gómez-Pérez, Ostafe and Sha. Finite fields have odd characteristic; no claim is made for characteristic two or for sequences of length at least four. Irreducibility is over the base field \(\mathbb F_q\), not over its algebraic closure.

## Proof

**Normalization.** Multiplication of every \(f_j\) by a nonzero scalar and substitution \(X\mapsto bX\) preserve irreducibility. For any nonzero \(u_0,u_1\), the substitution \(X\mapsto (u_0/u_1)X\) followed by division by \(u_0\) makes the constant and linear coefficients equal to one. The normalized quadratic and cubic are
\[
1+X+aX^2,\qquad 1+X+aX^2+tX^3,
\]
where \(a=u_2u_0/u_1^2\) and \(t=u_3u_0^2/u_1^3\). Since the constant terms are nonzero, reversal preserves irreducibility and gives
\[
Q_a(X)=X^2+X+a,\qquad G_{a,t}(X)=X^3+X^2+aX+t.
\]
Conversely each eligible pair \((a,t)\) corresponds to exactly \((q-1)^2\) original tuples, so
\[
I_3(q)=(q-1)^2\sum_{a\in A_q} C_q(a).
\]
Irreducibility of \(Q_a\) is equivalent to the discriminant \(1-4a\) being a nonsquare. Translation by \(a\mapsto1-4a\) is bijective, and zero is not a nonsquare; hence \(\#A_q=(q-1)/2\) and every eligible \(a\) is nonzero.

**Cubic root counting.** Fix \(a\in\mathbb F_q\), and let \(N_i\) denote the number of \(t\in\mathbb F_q\) for which \(G_{a,t}\) has precisely \(i\) distinct roots in \(\mathbb F_q\), for \(0\le i\le3\). Every \(x\in\mathbb F_q\) determines exactly one \(t=-x^3-x^2-ax\). Therefore
\[
\sum_{i=0}^{3}N_i=q,
\qquad\sum_{i=0}^{3}iN_i=q,
\qquad N_0=N_2+2N_3.
\]
A cubic over a field is irreducible exactly when it has no base-field root, so \(C_q(a)=N_0\).

Count ordered triples \((x,y,z)\in\mathbb F_q^3\) satisfying
\[
x+y+z=-1,\qquad xy+yz+zx=a.
\]
If \(G_{a,t}\) has two distinct base-field roots, all its roots lie in the base field (one is doubled), yielding exactly three ordered triples; if it has three distinct roots, it yields six triples. A triple root is possible only if the characteristic is different from three and \(a=1/3\), since it would require \(3x=-1\) and \(a=3x^2\). Thus, whenever a triple root is impossible, the number \(T(a)\) of such triples is
\[
T(a)=3N_2+6N_3=3C_q(a).
\]
Putting \(z=-1-x-y\) reduces the triple count to the conic
\[
x^2+xy+y^2+x+y+a=0.
\]

**Odd characteristic other than three.** Set \(X=x+1/3\) and \(Y=y+1/3\). The conic becomes
\[
X^2+XY+Y^2=1/3-a.
\]
For \(a\ne1/3\), the right side is nonzero. The quadratic form on the left is split over \(\mathbb F_q\) exactly when \(-3\) is a square, equivalently when \(q\equiv1\pmod3\). In the split case it is a product of two independent linear forms, and each nonzero level contains exactly \(q-1\) pairs. In the nonsplit case it is (up to an invertible linear coordinate change and nonzero scaling) the norm from \(\mathbb F_{q^2}\) to \(\mathbb F_q\); every nonzero level contains exactly \(q+1\) pairs because the norm kernel has order \(q+1\). Consequently,
\[
T(a)=\begin{cases}q-1,&q\equiv1\pmod3,\\q+1,&q\equiv2\pmod3.\end{cases}
\]
The triple-root case is excluded by \(a\ne1/3\), so dividing by three yields the claimed regular fiber counts.

The exceptional \(a=1/3\) is eligible precisely when \(1-4/3=-1/3\) is a nonsquare. As \(-1/3=(-3)/9\), this is equivalent to \(-3\) being a nonsquare, namely \(q\equiv2\pmod3\). Then
\[
G_{1/3,t}(X)=(X+1/3)^3+t-1/27.
\]
Because \(q\equiv2\pmod3\), cubing is a permutation of \(\mathbb F_q\), so every such cubic has a root and \(C_q(1/3)=0\).

**Characteristic three.** Here no cubic with coefficient one on \(X^2\) can have a triple root, because three times the putative root would have to equal \(-1\). The conic becomes
\[
(x-y)^2+x+y+a=0.
\]
Since two is invertible, choosing \(x-y\) freely uniquely determines \(x+y\) and hence the pair \((x,y)\). It has exactly \(q\) solutions, so \(C_q(a)=T(a)/3=q/3\) for every eligible \(a\).

**Summation.** When \(q\equiv1\pmod3\), each of the \((q-1)/2\) eligible values contributes \((q-1)/3\); hence
\[
I_3(q)=(q-1)^2\frac{q-1}{2}\frac{q-1}{3}=\frac{(q-1)^4}{6}.
\]
When \(q\equiv2\pmod3\), one of the \((q-1)/2\) eligible values has zero cubic extensions and each of the remaining \((q-3)/2\) values contributes \((q+1)/3\); hence
\[
I_3(q)=(q-1)^2\frac{q-3}{2}\frac{q+1}{3}.
\]
In characteristic three, every eligible value contributes \(q/3\); hence
\[
I_3(q)=(q-1)^2\frac{q-1}{2}\frac{q}{3}=\frac{q(q-1)^3}{6}.
\]
This completes the proof. \(\square\)

## Verification

The standalone `verify.py` computes irreducibility by exhaustive root tests for a quadratic and cubic over a finite field, without using the conic-count formula. It checks prime fields of orders \(3,5,7,11,13,17,19,23,29,31,37,41,43,47\) and quadratic extension fields of orders \(9,25,49,121\), comparing every eligible quadratic parameter's cubic fiber count and the resulting total to the theorem. It finishes with `VERIFY_OK`. Such finite checks are illustrations only; the proof above covers all odd prime powers.

## Relationship to prior work

Gómez-Pérez, Ostafe and Sha define these consecutive irreducible sequences and obtain an exact formula for \(I_2\), but only an explicit lower bound for \(I_3\) in Theorem 5.5 of their 2015 preprint (and 2018 revised version) [1]. Their proof already fixes the first two coefficients to one but estimates the cubic count using character sums. The conic root-triple reduction here supplies an exact evaluation, including the previously hidden exceptional quadratic coefficient in the \(q\equiv2\pmod3\) case. Chou and Cohen [2] prove general polynomial factorization-distribution estimates and construct long consecutive irreducible sequences; the reviewed relevant sections do not state this exact coefficient-restricted length-three count. This relationship is a bounded comparison, not a proof of global novelty.

## Limitations

The exact formula applies only to length three and odd characteristic. It neither determines the maximal length of consecutive irreducible polynomial sequences nor addresses characteristic two. The complete mathematical proof does not depend on numerical computation. An unindexed or otherwise unidentified equivalent enumeration remains a literature risk; no independent external audit has been performed.

## References

[1] D. Gómez-Pérez, A. Ostafe, M. Sha, *The Arithmetic of Consecutive Polynomial Sequences over Finite Fields*, arXiv:1509.01936v1, first public version 2015-09-07; revised arXiv:1509.01936v2 (2018-05-23); *Finite Fields and Their Applications* 50 (2018), 35–65, doi:10.1016/j.ffa.2017.11.002. Theorem 5.5 and Section 5.4.

[2] W.-S. Chou, S. D. Cohen, *Polynomial Distribution and Sequences of Irreducible Polynomials over Finite Fields*, *Journal of Number Theory* 75 (1999), 145–159, doi:10.1006/jnth.1998.2321, Sections 1 and 3.
