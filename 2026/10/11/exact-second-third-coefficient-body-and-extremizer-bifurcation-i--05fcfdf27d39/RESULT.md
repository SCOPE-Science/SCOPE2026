# Exact second–third coefficient body and extremizer bifurcation in the Mocanu–Robertson class

## Finding

Let
\[
1<k<k_0,
\]
where
\[
k_0=1.808986\ldots
\]
is the unique positive root greater than \(1\) of
\[
1+(k^2-1)\log\frac{k}{k+1}=0.
\]
Consider
\[
g(z)=z+a_2z^2+a_3z^3+\cdots
\]
in the Mocanu–Robertson class
\[
\left|
\frac{1+zg''(z)/g'(z)}
{zg'(z)/g(z)}
\right|
<k
\qquad(z\in\mathbb D).
\]

Put
\[
A=k-\frac1k
\]
and
\[
\mu=4k-\frac5k.
\]
Then the exact joint coefficient body of
\[
(a_2,a_3)
\]
is
\[
|a_2|\le A
\]
together with the fiber inequality
\[
\left|
a_3-\frac{\mu}{4A}a_2^2
\right|
\le
\frac A4
\left(
1-\frac{|a_2|^2}{A^2}
\right).
\]

Conversely, every pair
\[
(a_2,a_3)
\]
satisfying these two conditions is realized by a function in the class.

The body gives an exact phase diagram for the sharp marginal problem
\[
\max |a_3|.
\]
For
\[
1<k<\frac54,
\]
all extremizers have Schwarz data
\[
w(\zeta)=e^{i\theta}\zeta^2
\]
and therefore
\[
a_2=0.
\]
For
\[
\frac54<k<k_0,
\]
all extremizers have
\[
w(\zeta)=e^{i\theta}\zeta
\]
and therefore
\[
|a_2|=A.
\]

At the transition
\[
k=\frac54,
\]
one has
\[
A=\frac9{20},
\qquad
\mu=1,
\]
and there is a continuum of extremizing degree-two Blaschke products
\[
w_{r,\theta}(\zeta)
=
e^{i\theta}\zeta
\frac{r-e^{i\theta}\zeta}
{1-r e^{i\theta}\zeta},
\qquad
0\le r\le1.
\]
They interpolate between the quadratic and linear Schwarz extremizers and all satisfy
\[
|a_3|=\frac9{80}.
\]

Thus the separate second- and third-coefficient estimates from the recent source are projections of an exact family of disks in the
\[
a_3
\]
variable over the
\[
a_2
\]
disk. The marginal extremizer changes type exactly at
\[
k=\frac54.
\]

## Assumptions and scope

The class and normalization are those of the cited 2026 source. The range
\[
1<k<k_0
\]
is the source range in which its dominant for
\[
g/(zg')
\]
has positive real part. That positivity is used below to construct a class member from arbitrary admissible first two Schwarz coefficients.

The theorem determines exactly the first two nontrivial Taylor coefficients. It does not classify higher coefficients.

The endpoint
\[
k=k_0
\]
is not included. No assertion is made here about exact coefficient-body sufficiency for
\[
k\ge k_0.
\]

## Proof

The source parameterizes the differential inequality by a Schwarz function
\[
w(\zeta)=c_1\zeta+c_2\zeta^2+\cdots
\]
and obtains
\[
a_2=-Ac_1,
\]
\[
a_3
=
-\frac A4
\left(
c_2-\mu c_1^2
\right).
\]
Hence
\[
c_1=-\frac{a_2}{A}
\]
and
\[
c_2
=
\mu\frac{a_2^2}{A^2}
-\frac{4a_3}{A}.
\]

For every Schwarz function,
\[
|c_2|
\le
1-|c_1|^2.
\]
Substitution gives
\[
|a_2|\le A
\]
and
\[
\left|
a_3-\frac{\mu}{4A}a_2^2
\right|
\le
\frac A4
\left(
1-\frac{|a_2|^2}{A^2}
\right).
\]
This proves necessity.

For sufficiency, take any pair satisfying the displayed coefficient-body inequalities and define
\[
c_1=-\frac{a_2}{A},
\qquad
c_2
=
\mu\frac{a_2^2}{A^2}
-\frac{4a_3}{A}.
\]
Then
\[
|c_1|\le1,
\qquad
|c_2|\le1-|c_1|^2.
\]

If
\[
|c_1|<1,
\]
put
\[
\eta=\frac{c_2}{1-|c_1|^2}.
\]
Then
\[
|\eta|\le1,
\]
and
\[
w(\zeta)
=
\zeta
\frac{c_1+\eta\zeta}
{1+\overline{c_1}\eta\zeta}
\]
is a Schwarz function with
\[
w(\zeta)=c_1\zeta+c_2\zeta^2+\cdots.
\]
If
\[
|c_1|=1,
\]
then the coefficient-body condition forces
\[
c_2=0,
\]
and one takes
\[
w(\zeta)=c_1\zeta.
\]

Define
\[
H_w(z)
=
\frac{1-kw(z)}
{1-w(z)/k}.
\]
Also define
\[
q(z)
=
1+
A\int_0^z
\frac{w(t)}
{t(1-w(t)/k)}
\,dt.
\]
The integrand is analytic at the origin, and direct differentiation gives
\[
zq'(z)=1-H_w(z).
\]

The source's differential-subordination argument gives
\[
q(z)
\prec
P_k(z)
=
1+(k^2-1)\log\frac{k}{k-z}.
\]
For
\[
1<k<k_0,
\]
the same source proves
\[
\operatorname{Re}P_k(z)>0
\qquad(z\in\mathbb D).
\]
Therefore
\[
\operatorname{Re}q(z)>0,
\]
so
\[
q
\]
has no zeros.

Now set
\[
g(z)
=
z
\exp
\left(
\int_0^z
\frac{q(t)^{-1}-1}{t}
\,dt
\right).
\]
Then
\[
\frac{zg'(z)}{g(z)}
=
\frac1{q(z)}.
\]
Differentiating
\[
q(z)=\frac{g(z)}{zg'(z)}
\]
shows that
\[
\frac{1+zg''(z)/g'(z)}
{zg'(z)/g(z)}
=
1-zq'(z)
=
H_w(z).
\]
Because
\[
w(\mathbb D)\subset\mathbb D,
\]
the Möbius map defining
\[
H_w
\]
has modulus less than
\[
k.
\]
Thus
\[
g
\]
belongs to the Mocanu–Robertson class and has the prescribed
\[
a_2,a_3.
\]
This proves exact sufficiency.

For the marginal
\[
|a_3|
\]
problem, the exact body is equivalent to maximizing
\[
|c_2-\mu c_1^2|
\]
over the Schwarz coefficient body
\[
|c_2|\le1-|c_1|^2.
\]
Writing
\[
r=|c_1|,
\]
the sharp value at fixed
\[
r
\]
is
\[
1-r^2+|\mu|r^2
=
1+(|\mu|-1)r^2.
\]
Hence the maximizing radius is
\[
r=0
\]
when
\[
|\mu|<1
\]
and
\[
r=1
\]
when
\[
|\mu|>1.
\]

The function
\[
\mu(k)=4k-\frac5k
\]
is strictly increasing,
\[
\mu(1)=-1,
\]
and
\[
\mu\!\left(\frac54\right)=1.
\]
Thus
\[
|\mu|<1
\]
throughout
\[
1<k<\frac54,
\]
where equality requires
\[
c_1=0,
\qquad
|c_2|=1.
\]
Schwarz's lemma applied to
\[
w(\zeta)/\zeta
\]
then yields exactly
\[
w(\zeta)=e^{i\theta}\zeta^2.
\]

For
\[
\frac54<k<k_0,
\]
one has
\[
\mu>1.
\]
Equality requires
\[
|c_1|=1,
\]
and Schwarz's lemma yields exactly
\[
w(\zeta)=e^{i\theta}\zeta.
\]

At
\[
k=\frac54,
\]
one has
\[
\mu=1,
\]
so every radius
\[
0\le r\le1
\]
can maximize. Equality requires
\[
c_2=-(1-r^2)e^{2i\theta}
\]
when
\[
c_1=re^{i\theta}.
\]
The displayed Blaschke family
\[
w_{r,\theta}
\]
has exactly these first two coefficients, proving the full transition family.

## Verification

The coefficient-body formula was checked algebraically in both directions from
\[
a_2=-Ac_1
\]
and
\[
a_3
=
-\frac A4(c_2-\mu c_1^2).
\]

The Schur parametrization
\[
w(\zeta)
=
\zeta
\frac{c_1+\eta\zeta}
{1+\overline{c_1}\eta\zeta}
\]
has second coefficient
\[
(1-|c_1|^2)\eta=c_2,
\]
so every point of the disk fiber is realized by a Schwarz function.

The reconstruction of
\[
g
\]
uses the exact identity
\[
zq'=1-H_w
\]
and the source's positive-real dominant in the stated
\[
k
\]
range. Thus no formal coefficient solution is accepted without an analytic class member.

For the marginal phase transition,
\[
\max_{|c_2|\le1-r^2}
|c_2-\mu c_1^2|
=
1+(|\mu|-1)r^2
\]
was derived by aligning the phase of
\[
c_2
\]
against that of
\[
\mu c_1^2.
\]
This one-variable expression has its maximum at
\[
r=0
\]
or
\[
r=1
\]
except at
\[
|\mu|=1.
\]
Since
\[
\mu(k)
\]
is strictly increasing and first returns to
\[
1
\]
at
\[
k=5/4,
\]
the stated bifurcation follows.

Independent numerical substitutions in the disk body and in the Blaschke transition family were used only as consistency checks. No finite sampling is used to prove exactness.

## Relationship to prior work

Haq and Sokół introduce and analyze the Mocanu–Robertson type class used here. Their coefficient theorem derives separate sharp bounds for
\[
|a_2|
\]
and
\[
|a_3|
\]
from the first two coefficients of a Schwarz function, and their following theorem treats a Fekete–Szegő functional.

The inspected article does not state the joint
\[
(a_2,a_3)
\]
coefficient body. In particular, it does not give the disk fiber of admissible
\[
a_3
\]
over a prescribed
\[
a_2,
\]
nor a sufficiency construction proving that every point of that fiber occurs.

The source discusses linear and quadratic Schwarz extremal templates for its projected coefficient bounds. The exact joint body above locates the full marginal transition and shows that at
\[
k=5/4
\]
the two endpoint templates are joined by a continuum of degree-two Blaschke extremizers.

The classical Keogh–Merkes coefficient inequality supplies the sharp Schwarz two-coefficient constraint underlying the calculation. It does not by itself identify the coefficient body of this 2026 differential class, because exact sufficiency requires reconstruction through the class's differential subordination.

Targeted searches for a Mocanu–Robertson coefficient body, independent second–third coefficient fibers, the
\[
k=5/4
\]
transition, and equivalent Schwarz-parameter formulations did not locate an implication-equivalent result.

## Limitations

Exact sufficiency is proved only in
\[
1<k<k_0,
\]
where the cited source supplies a positive-real dominant for the reconstruction.

The theorem concerns only
\[
(a_2,a_3).
\]
It does not determine higher-dimensional coefficient bodies.

The transition classification concerns extremizers of
\[
|a_3|.
\]
Other coefficient functionals can have different extremal geometries.

No statement is made about whether a similar exact body persists past
\[
k_0.
\]

## References

1. W. Ul Haq and J. Sokół, *Starlikeness and strong starlikeness of functions satisfying Mocanu-Robertson type inequalities*, Journal of Inequalities and Applications, published 18 September 2026, DOI: 10.1186/s13660-026-03542-4.
2. F. R. Keogh and E. P. Merkes, *A coefficient inequality for certain classes of analytic functions*, Proceedings of the American Mathematical Society 20 (1969), 8--12, DOI: 10.1090/S0002-9939-1969-0232926-9.
3. D. J. Hallenbeck and S. Ruscheweyh, *Subordination by convex functions*, Proceedings of the American Mathematical Society 52 (1975), 191--195.
