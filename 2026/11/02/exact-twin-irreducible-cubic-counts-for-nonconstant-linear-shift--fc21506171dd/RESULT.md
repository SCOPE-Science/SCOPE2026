# Exact twin-irreducible cubic counts for nonconstant linear shifts

## Finding
Let \(q\) be an odd prime power with characteristic different from three and let \(u\in\mathbb F_q^\times\), \(v\in\mathbb F_q\). Among all monic cubic polynomials \(f\in\mathbb F_q[T]\), count those for which both \(f\) and \(f+uT+v\) are irreducible. Their number is independent of both \(u\) and \(v\), and is exactly
\[
C_q(u,v)=\frac{q^3-3q+2\chi_q(-3)}9
=\begin{cases}\dfrac{(q+2)(q-1)^2}{9},&q\equiv1\pmod3,\\[2pt]
\dfrac{(q-2)(q+1)^2}{9},&q\equiv2\pmod3.
\end{cases}
\]
Here \(\chi_q\) is the quadratic character on \(\mathbb F_q\), extended by \(\chi_q(0)=0\). This includes every finite field of odd characteristic greater than three, not just prime fields. In particular, at least one such pair exists for every choice of coefficients in the specified domain.

## Assumptions and scope
Every monic cubic is uniquely represented as \(f(T)=(T+s)^3+A(T+s)+B\) with \(s,A,B\in\mathbb F_q\), since three is invertible. Irreducibility of a cubic over a field is equivalent to having no root in that field. The theorem does not assert a formula in characteristics two or three, nor for shifts whose linear coefficient vanishes. It counts monic cubics with no normalization beyond leading coefficient one.

## Proof
**1. Fiber separation for a nonconstant linear shift.** Put \(X=T+s\). The pair \(f(T),f(T)+uT+v\) becomes
\[
X^3+AX+B,\qquad X^3+(A+u)X+(B+v-us).
\]
For \(A\in\mathbb F_q\), write \(m(A)=\#\{B\in\mathbb F_q:X^3+AX+B\text{ has no root in }\mathbb F_q\}\). For each fixed \(A\), the transformation \((s,B)\mapsto(B,B+v-us)\) is a bijection of \(\mathbb F_q^2\) because \(u\ne0\). Consequently the desired count is exactly
\[
C_q(u,v)=\sum_{A\in\mathbb F_q}m(A)m(A+u). \tag{1}
\]
This is why nonzero linear shifts, rather than constant shifts, are essential.

**2. Root-free depressed cubics with nonzero linear coefficient.** Fix \(A\ne0\). The discriminant of \(X^3+AX+B\) is \(\Delta_B=-4A^3-27B^2\). Put \(\varepsilon=\chi_q(-3)\in\{1,-1\}\). The elementary quadratic-character identity
\[
\sum_{y\in\mathbb F_q}\chi_q(y^2-c)=-1\quad(c\in\mathbb F_q^\times)
\]
follows by counting \((y,z)\) with \(z^2=y^2-c\): the substitution \((y-z,y+z)\) bijects those pairs with the \(q-1\) factor pairs of \(c\). It gives \(\sum_B\chi_q(\Delta_B)=-\varepsilon\).

Let \(Z=\#\{B:\Delta_B=0\}\). Since \(A\ne0\) and the characteristic is neither two nor three, each \(\Delta_B=0\) cubic has exactly two distinct rational roots (one double root, one simple root). For \(\Delta_B\ne0\), nonsquare discriminant means exactly one rational root and square discriminant means either zero or three rational roots. (For a separable cubic the discriminant character is the sign of its Frobenius permutation.) Thus precisely \(R_1=(q-Z+\varepsilon)/2\) coefficients \(B\) yield one root. If \(R_3\) coefficients yield three roots, double-counting the pairs \((x,B)\) satisfying \(x^3+Ax+B=0\) gives \(q=R_1+2Z+3R_3\). Therefore the number \(m(A)\) of coefficients with no root is
\[
m(A)=q-R_1-Z-R_3=\frac{q-\varepsilon}{3}\qquad(A\ne0). \tag{2}
\]
In this computation no particular value of \(Z\) is needed.

**3. The special coefficient.** If \(A=0\), the number of values attained by the cube map \(X\mapsto X^3\) on \(\mathbb F_q\) is \(q\) when \(q\equiv2\pmod3\) and \(1+(q-1)/3\) when \(q\equiv1\pmod3\). Hence
\[
m(0)=\begin{cases}0,&q\equiv2\pmod3,\\ 2(q-1)/3,&q\equiv1\pmod3.\end{cases} \tag{3}
\]
The character \(\varepsilon=1\) exactly when the field has nontrivial cube roots of unity (equivalently \(-3\) is a square), i.e. precisely when \(q\equiv1\pmod3\).

**4. Evaluation.** Since \(u\ne0\), exactly two choices of \(A\), namely \(0\) and \(-u\), have either \(A=0\) or \(A+u=0\), and they are distinct. Equations (1)--(3) therefore give
\[
C_q(u,v)=(q-2)\bigl((q-\varepsilon)/3\bigr)^2+2m(0)(q-\varepsilon)/3.
\]
For \(\varepsilon=1\) this equals \((q+2)(q-1)^2/9\); for \(\varepsilon=-1\) it equals \((q-2)(q+1)^2/9\). Both equal the asserted unified formula. Since \(q\ge5\), both expressions are positive. This completes the proof.

## Verification
Run `python3 verify_cubics.py` using Python's standard library. The verifier computes arithmetic in six prime fields and two genuine nonprime fields \(\mathbb F_{25},\mathbb F_{49}\), constructs the root-avoiding sets for all monic cubic coefficients directly, and counts simultaneous irreducibility for 84 coefficient-shift cases. The observed result is `VERIFY_OK fields=8 cases=84 monic_cubics=149042`. The exhaustive checks are finite corroboration, not substitutes for the algebraic proof.

## Relationship to prior work
Bary-Soroker, *Hardy-Littlewood tuple conjecture over large finite field* (initial arXiv posting 18 June 2012), Theorem 1.1, covers polynomial shifts of degree less than the polynomial degree but provides only the asymptotic \(q^3/9+O(q^{5/2})\) for this setting. Bender and Pollack's 2009 preprint gives earlier asymptotic twin-prime results. Bary-Soroker and Stix, *Cubic twin prime polynomials are counted by a modular form* (initially posted 2017), Theorems 1.2 and 1.4, derive **exact** formulas for constant shifts. In particular, cubic-character/elliptic-curve fluctuations occur in that scalar case; those formulas do not supply the present count for nonconstant linear shifts. An affine change of the polynomial variable preserves the degree of the difference between two polynomials and cannot turn a linear shift into a constant one.

A related previous finite-field classification computes simultaneous **squarefreeness** of shifted monic cubics. That weaker condition includes reducible squarefree cubics; its counts cannot determine simultaneous irreducibility. The present result addresses a different arithmetic indicator. Relevant older literature includes Effinger--Hicks--Mullen (2002), for which the complete chapter text could not be accessed; equivalent coverage there has not been ruled out.

## Limitations
The characteristic exclusions matter: the depressed-cubic and discriminant computations require \(6\) invertible. This theorem does not classify characteristic-two/three cases, nonlinear shifts, or degree greater than three. The arithmetic steps are exact but the assessment of originality is qualified by incomplete access to the 2002 chapter and the possibility of unlocated general polynomial-tuple identities. An independent audit has not been performed.

## References
1. L. Bary-Soroker, *Hardy-Littlewood tuple conjecture over large finite field*, arXiv:1206.3930 (first posted 2012-06-18), https://arxiv.org/abs/1206.3930 . Theorem 1.1.
2. A. O. Bender and P. Pollack, *On quantitative analogues of the Goldbach and twin prime conjectures over \(\mathbb F_q[t]\)*, arXiv:0912.1702 (first posted 2009-12-09), https://arxiv.org/abs/0912.1702 .
3. L. Bary-Soroker and J. Stix, *Cubic twin prime polynomials are counted by a modular form*, arXiv:1711.05564 (first posted 2017-11-15), https://arxiv.org/abs/1711.05564 . Theorems 1.2 and 1.4.
4. G. W. Effinger, K. H. Hicks, and G. L. Mullen, *Twin Irreducible Polynomials over Finite Fields*, in *Finite Fields with Applications to Coding Theory, Cryptography and Related Areas* (2002), DOI:10.1007/978-3-642-59435-9_8. Complete text not inspected.
