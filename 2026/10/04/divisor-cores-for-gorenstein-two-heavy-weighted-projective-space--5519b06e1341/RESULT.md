# Divisor cores for Gorenstein two-heavy weighted projective spaces
## Finding
For every integer \(r\ge2\), consider
\[
X_{r,a,b}=\mathbb P(\underbrace{1,\ldots,1}_{r},a,b),\qquad 1\le a\le b.
\]
The Gorenstein members of this family admit a finite divisor-core parametrization. They are in bijection with quadruples \((k,g,A,B)\) such that
\[
k\mid r,\qquad 1\le g\le k+2,\qquad AB=gk+1,
\]
\[
A\ge B\ge1,\qquad A\equiv B\equiv-1\pmod g,
\qquad \gcd(A+1,B+1)=g.
\]
The corresponding weights are
\[
a=\frac r k\frac{B+1}{g},\qquad
b=\frac r k\frac{A+1}{g}.
\]
Every Gorenstein member is canonical. It is terminal exactly when
\[
B>1\qquad\text{and}\qquad A>2.
\]
Moreover, the canonical but non-terminal Gorenstein members are precisely
\[
\mathbb P\!\left(1^r,\frac{2r}{t},r+\frac{2r}{t}\right)
\quad (t\mid 2r),
\]
together with \(\mathbb P(1^r,r,r)\). Thus their exact number is
\[
\tau(2r)+1,
\]
where \(\tau\) is the positive-divisor counting function.

## Assumptions and scope
The base field is \(\mathbb C\), \(r\ge2\), and the weighted projective spaces are ordinary well-formed weighted projective spaces. The notation \(1^r\) means that the weight \(1\) occurs \(r\) times. The theorem concerns the Gorenstein subfamily only; it does not classify arbitrary weight vectors with three or more non-unit weights.

## Proof
Put
\[
h=r+a+b.
\]
For a well-formed weighted projective space, the Gorenstein condition is that every weight divide \(h\). The unit weights do so automatically, hence here the condition is exactly
\[
a\mid h\qquad\text{and}\qquad b\mid h.
\]
Assume first that \(X_{r,a,b}\) is Gorenstein and set
\[
x=\frac h a,\qquad y=\frac h b.
\]
Because \(a\le b\), one has \(x\ge y\). Also
\[
\frac1x+\frac1y=\frac{a+b}{h}<1,
\]
so \(y\ge2\) and \(x\ge3\). Write
\[
x=gu,\qquad y=gv,
\]
where \(g=\gcd(x,y)\), \(u\ge v\), and \(\gcd(u,v)=1\). From
\[
1=\frac r h+\frac1x+\frac1y
\]
we obtain
\[
\frac r h=\frac{guv-u-v}{guv}.
\]
Define
\[
k=guv-u-v>0.
\]
Then
\[
h=\frac{rguv}{k},\qquad a=\frac{rv}{k},\qquad b=\frac{ru}{k}.
\]
Now
\[
\gcd(k,u)=\gcd(-v,u)=1,
\qquad
\gcd(k,v)=\gcd(-u,v)=1.
\]
Since \(a\) and \(b\) are integers, these coprimalities force \(k\mid r\).

Introduce
\[
A=gu-1,\qquad B=gv-1.
\]
Then
\[
AB=(gu-1)(gv-1)=g(guv-u-v)+1=gk+1.
\]
Also \(A\ge B\ge1\), both are congruent to \(-1\) modulo \(g\), and
\[
\gcd(A+1,B+1)=g\gcd(u,v)=g.
\]
Finally, since \(A,B\ge g-1\),
\[
(g-1)^2\le AB=gk+1,
\]
which implies \(g\le k+2\). Hence the stated divisor-core data are finite for each fixed \(r\).

Conversely, suppose \((k,g,A,B)\) satisfies the stated conditions. Set
\[
u=\frac{A+1}{g},\qquad v=\frac{B+1}{g}.
\]
The congruences make \(u,v\) positive integers; the gcd condition gives \(\gcd(u,v)=1\), and \(A\ge B\) gives \(u\ge v\). The factorization \(AB=gk+1\) expands to
\[
k=guv-u-v.
\]
Because \(k\mid r\), the displayed formulas for \(a,b\) are positive integers. Their sum satisfies
\[
r+a+b=\frac{rguv}{k}=:h,
\]
and therefore
\[
\frac h a=gu=A+1,\qquad \frac h b=gv=B+1.
\]
Thus \(a\mid h\) and \(b\mid h\), so the resulting weighted projective space is Gorenstein. This proves the bijection.

It remains to determine the singularity type. Let \(d=b-a\). The only potentially singular affine charts are the two heavy charts, of cyclic quotient types
\[
\frac1a(1^r,b)\qquad\text{and}\qquad \frac1b(1^r,a).
\]
The Reid--Tai age calculation on these two charts gives the following elementary criterion:
\[
\text{canonical}\iff d\le r\ \text{and}\ a\le r+d,
\]
\[
\text{terminal}\iff d<r\ \text{and}\ a<r+d.
\]
For completeness, on the \(b\)-chart the age numerator for the \(j\)-th nontrivial group element is \(rj+[-jd]_b\). The element \(j=1\) forces \(d\le r\), and if this holds then either \(rj\ge b\), or \([-jd]_b=b-jd\), giving numerator \(b+j(r-d)\ge b\). The strict version is identical. On the \(a\)-chart the numerator is \(rj+[jd]_a\); when \(rj<a\), one has \([jd]_a=jd\), so the condition becomes \(a\le r+d\), again with the strict version for terminality. The equal-weight case \(d=0\) reduces to ages \(rj/a\) and gives the same combined inequalities.

For a Gorenstein member, express these inequalities through \(x=h/a\) and \(y=h/b\). Directly,
\[
r-d=\frac{hx(y-2)}{xy},
\qquad
r+d-a=\frac{hy(x-3)}{xy}.
\]
Since \(y\ge2\) and \(x\ge3\), both canonical inequalities always hold. They are strict exactly when
\[
y>2\qquad\text{and}\qquad x>3.
\]
Because \(y=B+1\) and \(x=A+1\), terminality is equivalent to \(B>1\) and \(A>2\).

Thus a Gorenstein member is non-terminal exactly when \(y=2\) or \(x=3\). If \(y=2\), then \(h=2b\), hence \(b=r+a\), and
\[
x=\frac{2(r+a)}{a}=2+\frac{2r}{a}.
\]
Writing \(t=2r/a\), integrality gives exactly \(t\mid2r\), and
\[
a=\frac{2r}{t},\qquad b=r+\frac{2r}{t}.
\]
If \(x=3\) and \(y>2\), then \(x\ge y\) forces \(y=3\), so \(a=b=h/3\); the identity \(h=r+a+b\) then gives \(a=b=r\). The case \((x,y)=(3,2)\) already belongs to the \(y=2\) family. Therefore the two displayed families are disjoint and exhaustive, and the count is \(\tau(2r)+1\).

## Verification
The proof is symbolic and establishes the infinite statement. The accompanying script `verify_gorenstein_two_heavy.py` provides an independent finite regression check for \(2\le r\le100\). It compares the divisor-core construction with direct Gorenstein divisibility, evaluates the two cyclic-quotient age tests, checks the terminal criterion, and verifies the complete non-terminal boundary and the formula \(\tau(2r)+1\). The executed output is:

`VERIFY_OK r=2..100; finite divisor-core parameterization, canonicality, terminal criterion, boundary family and count all agree with direct Gorenstein divisibility and chart ages`

The finite computation is not used to infer the universal quantifiers.

## Relationship to prior work
Nill relates reflexive simplices and Gorenstein toric Fano varieties to unit partitions and develops sharp global bounds from the arithmetic of unit fractions. Kasprzyk states that Gorenstein weighted projective spaces are characterized by unit partitions, gives general terminal fractional-part criteria, and classifies terminal Gorenstein weighted projective spaces computationally through dimension ten. These sources provide the general framework but do not state the divisor-core bijection above for the natural family with exactly two possibly non-unit weights.

The new point is that the unit-partition equations in this family collapse to a finite factorization problem \(AB=gk+1\) with \(k\mid r\) and \(g\le k+2\). This simultaneously gives a direct enumeration procedure in every dimension, proves automatic canonicity, reduces terminality to the two smallest denominator exclusions, and yields the exact divisor-function count of the Gorenstein canonical/non-terminal boundary.

A later literature on reflexive weighted-projective simplices with few weight values studies properties such as the integer decomposition property and unimodality. Those results impose different hypotheses and do not imply the stated divisor-core classification.

## Limitations
The theorem is restricted to the Gorenstein subfamily \(\mathbb P(1^r,a,b)\). It does not address fake weighted projective spaces, non-Gorenstein members, or families with three or more non-unit weights. The originality assessment is search-based: an equivalent elementary parametrization could exist under different notation in the older unit-fraction or weighted-projective literature. The verification script checks only finite ranges and is corroborative rather than a proof.

## References
1. B. Nill, *Volume and lattice points of reflexive simplices*, arXiv:math/0412480, first posted 2004-12-23.
2. A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10.
3. M. Reid, *Young person's guide to canonical singularities*, Proc. Sympos. Pure Math. 46 (1987), 345--414.
4. B. Braun and D. Hanely, *A regular unimodular triangulation of reflexive 2-supported weighted projective space simplices*, arXiv:2010.13720, 2020.
