# Elliptic-curve enumeration of simultaneous irreducible quadratic-composition quartics

## Finding

For every odd prime power \(q\), let \(k=\mathbb F_q\). For any \(c,d\in k\), put
\[
I_q(c,d)=\#\{(a,b)\in k^2:(T^2+aT+b)^2+c\ \text{and}\ (T^2+aT+b)^2+d\ \text{are both irreducible in }k[T]\}.
\]
Let \(\chi\) be the quadratic character of \(k\), with \(\chi(0)=0\). Then the complete classification is:

1. If \(c=0\) or \(d=0\), or if \(\chi(-c)=1\) or \(\chi(-d)=1\), then \(I_q(c,d)=0\).
2. If \(c=d\ne0\) and \(\chi(-c)=-1\), then \(I_q(c,c)=q(q+1)/2\).
3. If \(c\ne d\), \(\chi(-c)=\chi(-d)=-1\), and
   \[
   E_{c,d}:\quad Y^2=X(X+c)(X+d),
   \]
   then \(E_{c,d}\) is a nonsingular elliptic curve and
   \[
   \boxed{I_q(c,d)=\frac q4\#E_{c,d}(k).}
   \]

In particular, the two quartics can be simultaneously irreducible **if and only if** both \(-c\) and \(-d\) are quadratic nonsquares. For distinct admissible constants, the exact count satisfies
\[
\frac q4(q+1-2\sqrt q)\le I_q(c,d)\le\frac q4(q+1+2\sqrt q),
\]
and is a strictly positive integer. The group \(E_{c,d}(k)\) has full rational two-torsion, so its order is divisible by four.

## Assumptions and scope

The field has odd characteristic; the constants are arbitrary field elements; the inner quadratic is monic and ranges over all \(q^2\) ordered coefficient pairs. An irreducible polynomial is understood over the base field \(k\). The elliptic-curve order includes its point at infinity. When \(c=d\), the curve in the displayed formula would be singular, so the separate branch is essential. For \(q=3\), there are no distinct admissible constants; the other branches still hold.

## Proof

**Reduction to two quadratic characters.** Fix a nonzero \(c\) with \(\chi(-c)=-1\), and let \(\alpha\in K=\mathbb F_{q^2}\) satisfy \(\alpha^2=-c\). Then \(T^2+c\) is irreducible over \(k\). For \(A(T)=T^2+aT+b\), the quartic \(A(T)^2+c\) is irreducible over \(k\) if and only if \(A(T)-\alpha\) is irreducible over \(K\): a root \(\beta\) of the latter has \(\alpha=A(\beta)\), and the tower degrees are exactly \(2\) and \(2\) in the irreducible case; conversely, a degree-four root of the quartic forces this tower condition.

Set \(x=a^2-4b\). The discriminant of \(A(T)-\alpha\) over \(K\) is \(x+4\alpha\). Its norm to \(k\) is \(x^2+16c\). For every \(z\in K^\times\), \(\chi_K(z)=\chi(\mathrm N_{K/k}(z))\), by comparing the exponents \((q^2-1)/2\) and \((q+1)(q-1)/2\). The norm above is never zero, because \(-c\) is a nonsquare. Thus the irreducibility indicator is exactly
\[
\mathbf 1_{A^2+c\text{ irreducible}}=\frac{1-\chi(x^2+16c)}2.
\]
For every \(a\), the substitution \(b\mapsto x=a^2-4b\) is a bijection of \(k\).

**The single-constant and degenerate branches.** If \(c=0\) or \(-c\) is a square, \(A^2+c\) factors over \(k\) for every \(A\). If \(-c\) is a nonsquare, then
\[
\sum_{x\in k}\chi(x^2+16c)=-1.
\]
Indeed, for each nonzero \(v\in k\), the equation \(y^2-x^2=v\) has exactly \(q-1\) ordered solutions, via \((y-x)(y+x)=v\), so its quadratic-character sum is \(-1\). Summing the indicator over \(a,b\) gives \(q(q+1)/2\).

**The two-distinct-constant branch.** Assume \(c,d\ne0\), \(c\ne d\), and \(\chi(-c)=\chi(-d)=-1\). Write \(U=16c\), \(V=16d\). Expanding both indicators yields
\[
I_q(c,d)=\frac q4\left(q+2+\sum_{x\in k}\chi((x^2+U)(x^2+V))\right).
\]
The number of square roots of \(z\in k\) is \(1+\chi(z)\), hence
\[
\begin{aligned}
\sum_{x\in k}\chi((x^2+U)(x^2+V))
&=\sum_{t\in k}(1+\chi(t))\chi((t+U)(t+V))\\
&=-1+\sum_{t\in k}\chi(t(t+U)(t+V)).
\end{aligned}
\]
The \(-1\) follows because \(U\ne V\) and the quadratic polynomial \((t+U)(t+V)\) has two distinct roots. Under \(t=16X\), its cubic character sum becomes \(\sum_{X\in k}\chi(X(X+c)(X+d))\), since \(16^3\) is a square. The affine point count on \(E_{c,d}\) is \(q\) plus this sum, and there is one additional point at infinity. This gives \(I_q(c,d)=q\#E_{c,d}(k)/4\).

The roots \(0,-c,-d\) of the cubic are distinct, so the curve is nonsingular in odd characteristic; its three nonidentity rational points of order two imply \(4\mid \#E_{c,d}(k)\). Hasse's bound \(|\#E_{c,d}(k)-(q+1)|\le2\sqrt q\) proves the displayed inequalities and strict positivity for every \(q>1\). This completes all cases.

## Verification

Run `python verify.py` with Python 3. The standard-library checker constructs prime fields and quadratic prime-power fields, explicitly forms the quartics, tests degree-four irreducibility using polynomial greatest common divisors against \(T^{q^2}-T\), and counts points on the stated elliptic curves independently by iterating over field coordinates. It checks zero, equal-constant, and distinct-admissible branches. Its recorded run passed 74 cases over 10 fields, with 65,828 direct quartic irreducibility tests. The finite checks do not prove the formulas for arbitrary fields; the proof above does.

## Relationship to prior work

Bender and Pollack (2009) and Bary-Soroker (2012) establish broad large-field twin-prime-polynomial asymptotics, whereas this theorem gives an exact fixed-field, two-parameter subfamily of degree-four pairs. The quartics are compositional; Heath-Brown and Micheli (2017) study dynamically irreducible sets of quadratic maps, not these simultaneous fixed-shift counts. The proof uses the classical quadratic-character and elliptic-point-count framework. No claim is made that the techniques themselves are new. An equivalent specialized enumeration in earlier literature remains possible.

## Limitations

Only monic inner quadratics and constant perturbations are covered, in odd characteristic. The elliptic order is an exact arithmetic expression, not a uniform elementary polynomial in \(q,c,d\). The theorem does not supply all degree-four twin-prime-polynomial counts, any higher-degree classification, or characteristic-two analogues. It has not undergone independent mathematical audit.

## References

- A. O. Bender and P. Pollack, *On quantitative analogues of the Goldbach and twin prime conjectures over Fq[t]*, arXiv:0912.1702, first posted 2009-12-09. https://arxiv.org/abs/0912.1702
- L. Bary-Soroker, *Hardy-Littlewood tuple conjecture over large finite fields*, arXiv:1206.3930, first posted 2012-06-18. https://arxiv.org/html/1206.3930v3
- D. R. Heath-Brown and G. Micheli, *Irreducible polynomials over finite fields produced by composition of quadratics*, arXiv:1701.05031, first posted 2017-01-18. https://arxiv.org/abs/1701.05031
- Classical Capelli irreducibility criterion, quadratic character sums and Hasse's elliptic-curve point bound (used as standard mathematical facts, with the needed quadratic case also proved above).
