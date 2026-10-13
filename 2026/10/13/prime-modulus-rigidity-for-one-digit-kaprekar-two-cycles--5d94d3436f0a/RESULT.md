# Prime-modulus rigidity for one-digit Kaprekar two-cycles
## Finding
Let \(\ell\) be prime and set
\[
b=\ell+1.
\]
For a positive one-digit base-\(b\) state \(x\), define the one-block square-split Kaprekar map
\[
T_b(x)
=
\left\lfloor\frac{x^2}{b}\right\rfloor
+
(x^2\bmod b).
\]

A nontrivial two-cycle
\[
x\longmapsto y\longmapsto x,
\qquad
x\ne y,
\]
with both \(x\) and \(y\) one-digit exists only if
\[
\ell\equiv1\pmod3.
\]
For every prime \(\ell\), there is at most one unordered nontrivial one-digit two-cycle.

When
\[
\ell\equiv1\pmod3,
\]
let
\[
1<u<v<\ell
\]
be the two nontrivial cube roots of unity modulo \(\ell\). Then
\[
u+v=\ell-1,
\]
and the unique possible pair \(\{u,v\}\) is a genuine two-cycle exactly when
\[
u^2-(3\ell-1)u+(\ell-1)^2\le0.
\tag{1}
\]
Equivalently,
\[
u\ge
\frac{3\ell-1-\sqrt{5\ell^2+2\ell-3}}2.
\tag{2}
\]

Examples include
\[
b=8:\quad 2\leftrightarrow4,
\]
\[
b=20:\quad 7\leftrightarrow11,
\]
and
\[
b=68:\quad 29\leftrightarrow37.
\]
The congruence condition alone is not sufficient: for
\[
b=14,\qquad \ell=13,
\]
the nontrivial cube roots are \(3\) and \(9\), but they do not form a two-cycle because (1) fails.

## Assumptions and scope
The map considered here is the one-block version of the classical Kaprekar square-splitting construction. For a one-digit input
\[
1\le x<b,
\]
write
\[
x^2=qb+r,
\qquad
0\le r<b.
\]
Then
\[
T_b(x)=q+r.
\]

The theorem classifies only period-\(2\) orbits whose two members are both positive one-digit states, under the arithmetic restriction that
\[
b-1
\]
is prime. It does not classify longer cycles, cycles containing larger states, or composite values of \(b-1\).

The states \(1\) and \(\ell=b-1\) are fixed, so neither can occur in a nontrivial two-cycle.

## Proof
Suppose
\[
T_b(x)=y
\]
with both \(x\) and \(y\) one-digit. Write
\[
x^2=qb+r,
\qquad
y=q+r.
\]
Subtracting gives
\[
x^2-y=q(b-1)=q\ell,
\]
hence
\[
x^2\equiv y\pmod\ell.
\tag{3}
\]

Now suppose \(x,y\) form a nontrivial two-cycle. Applying (3) in both directions gives
\[
x^2\equiv y\pmod\ell,
\qquad
y^2\equiv x\pmod\ell.
\]
Neither state is congruent to \(0\pmod\ell\), because the only positive one-digit state with that residue is \(\ell\), which is fixed. Therefore
\[
x^4\equiv x\pmod\ell
\]
implies
\[
x^3\equiv1\pmod\ell.
\]
Since \(x\ne1\), the residue class of \(x\) has exact order \(3\). Thus
\[
3\mid\ell-1,
\]
so
\[
\ell\equiv1\pmod3.
\]
The same holds for \(y\).

For prime \(\ell\equiv1\pmod3\), the polynomial
\[
z^2+z+1
\]
has exactly two roots in the nonzero residue classes, namely the two nontrivial cube roots \(u,v\). Hence any nontrivial one-digit two-cycle must be the unordered pair
\[
\{u,v\}.
\]
This proves uniqueness of the possible pair. Vieta's relation modulo \(\ell\) gives
\[
u+v\equiv-1\pmod\ell.
\]
Because
\[
2\le u+v\le2\ell-2
\]
and \(u+v\ne2\ell-1\), one has the exact integer identity
\[
u+v=\ell-1.
\tag{4}
\]

It remains to decide whether the modular pair is an actual square-split cycle. More generally, if
\[
n^2\equiv s\pmod\ell,
\qquad
1\le n,s<\ell,
\]
put
\[
q=\frac{n^2-s}{\ell}.
\]
Then
\[
n^2=q(\ell+1)+(s-q).
\]
Thus
\[
T_b(n)=s
\]
if and only if
\[
0\le q\le s.
\tag{5}
\]
Indeed, under (5) the remainder \(s-q\) lies between \(0\) and \(\ell<b\).

Order the roots so that
\[
u<v.
\]
For the transition \(u\mapsto v\), the integer
\[
q_u=\frac{u^2-v}{\ell}
\]
cannot be negative: if \(u^2-v<0\), its absolute value is less than \(\ell\), contradicting divisibility by \(\ell\), unless it is zero. Moreover,
\[
q_u<\frac{u^2}{\ell}<\frac u2<v,
\]
because (4) gives
\[
u<\frac{\ell-1}{2}.
\]
Hence (5) always holds for
\[
u\mapsto v.
\]

For the reverse transition,
\[
q_v=\frac{v^2-u}{\ell}\ge0
\]
by the same divisibility argument. Therefore
\[
v\mapsto u
\]
holds exactly when
\[
q_v\le u,
\]
or
\[
v^2-u\le\ell u.
\]
Using
\[
v=\ell-1-u
\]
from (4), this becomes
\[
u^2-(3\ell-1)u+(\ell-1)^2\le0,
\]
which is (1).

The discriminant of the quadratic in (1) is
\[
(3\ell-1)^2-4(\ell-1)^2
=
5\ell^2+2\ell-3.
\]
Since \(u<(\ell-1)/2\), the relevant root is the smaller one, and (1) is equivalent to (2). This completes the classification.

## Verification
The accompanying checker generates every prime
\[
\ell<20000.
\]
For each base
\[
b=\ell+1,
\]
it directly evaluates \(T_b\) on every positive one-digit state and records every unordered nontrivial one-digit two-cycle.

Independently, it computes the nontrivial cube roots of unity modulo \(\ell\) and applies criterion (1). It asserts exact equality between the directly observed cycle set and the theorem's predicted set for every tested prime.

The checker also verifies the displayed examples and the failure at \(\ell=13\). The computation is corroborative only: the unrestricted theorem follows from the congruence reduction and the exact digit-bound argument above.

## Relationship to prior work
Iannucci's 2000 paper gives the classical square-split framework in the form
\[
k^2=qN+r,
\qquad
k=q+r,
\]
and derives
\[
k(k-1)=q(N-1).
\]
It completely classifies fixed points through unitary divisors of \(N-1\) and explicitly specializes \(N=b^n\) to arbitrary bases. The present theorem studies period \(2\) rather than fixed points.

Iannucci and Foster's 2005 paper develops the corresponding cubic splitting problem and again emphasizes the modulus \(N-1\). That paper lists primary subject classification \(11A63\), confirming the number-theoretic classification of this Kaprekar setting.

Public reference tables for the Kaprekar square-split function explicitly record nontrivial cycles, including
\[
2\to4\to2
\]
in base \(8\). Such tables provide examples but not the prime-\(b-1\) classification proved here.

The new structural point is that when \(b-1\) is prime, composing the two transition congruences collapses every possible one-digit two-cycle to the two nontrivial cubic roots of unity. The only remaining issue is one exact base-digit inequality, producing criterion (1).

## Limitations
The primality of \(b-1\) is essential to the stated uniqueness argument. For composite \(b-1\), several independent cubic-root components can coexist and one base can have multiple one-digit two-cycles.

The theorem concerns only cycles whose two states are one-digit. The full Kaprekar square-split dynamical system can contain cycles involving larger states, and no classification of those is claimed.

Statement-level searches for the cubic-root formulation, the base-\(8\) cycle, amicable or sociable Kaprekar terminology, and prime \(b-1\) did not locate an equivalent theorem. An equivalent observation in unindexed recreational literature remains a residual originality risk.

## References
1. D. E. Iannucci, “The Kaprekar Numbers,” *Journal of Integer Sequences* 3 (2000), Article 00.1.2, published 13 January 2000.
2. D. E. Iannucci and B. Foster, “Kaprekar Triples,” *Journal of Integer Sequences* 8 (2005), Article 05.4.8.
