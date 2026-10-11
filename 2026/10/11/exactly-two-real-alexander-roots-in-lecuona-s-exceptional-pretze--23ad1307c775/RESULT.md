# Exactly two real Alexander roots in Lecuona's exceptional pretzel family
## Finding
For every odd integer \(a\ge 3\), let
\[
P_a=P\!\left(a,-a-2,-\frac{(a+1)^2}{2}\right)
\]
and write \(a=2m-1\), so \(m\ge2\). Using the normalization
\[
\Delta_a(t)=\frac{(t^{a+2}+1)(t^a+1)}{(t+1)^2}-m^2t^{a-1}(t-1)^2,
\]
the Alexander polynomial \(\Delta_a\) has exactly two real zeros. They are simple, negative, and reciprocal. Equivalently, there is a unique number \(\rho_m>1\) for which the real zero set is
\[
\{-\rho_m,-\rho_m^{-1}\}.
\]
In particular,
\[
\Delta_a(t)>0\qquad\text{for every real }t>0.
\]

## Assumptions and scope
The statement concerns the three-strand pretzel knot family \(P_a\) above and the Alexander-polynomial representative displayed in Saurabh's 2026 paper, where the same formula is recalled from Lecuona's earlier work. The restriction \(a\ge3\) odd is exactly the parameter range in which \(a=2m-1\) has \(m\ge2\) and the displayed pretzel has exactly one even parameter.

No assertion is made about the nonreal roots beyond reciprocity and complex conjugation. The result does not claim that these knots are fibered, nor does it use real-root information as a new sliceness obstruction.

## Proof
Put
\[
D=4m^2-1,\qquad
E_m(u)=\frac{(1+u)^{2m}+(1-u)^{2m}}2.
\]
Saurabh's change of variables
\[
t=\frac{1+u}{1-u}
\]
gives
\[
D_m(u):=(1-u)^{2a}\Delta_a\!\left(\frac{1+u}{1-u}\right)
=E_m(u)^2-u^2(1-u^2)^{2m-2}(u^2+D).
\]

First consider \(t>0\). Then \(-1<u<1\). Set \(r=u^2\), so \(0\le r<1\). Since \(E_m\) contains only even powers with nonnegative coefficients,
\[
E_m(u)\ge 1+\binom{2m}{2}u^2
=1+m(2m-1)r.
\]
Also
\[
u^2(1-u^2)^{2m-2}(u^2+D)
\le r(r+D)
\le 4m^2r.
\]
For \(r>0\),
\[
\bigl(1+m(2m-1)r\bigr)^2
\ge4m(2m-1)r
>4m^2r,
\]
because \(m(2m-1)>m^2\) for \(m\ge2\). At \(r=0\), \(D_m(0)=1\). Therefore \(D_m(u)>0\) for \(-1<u<1\), and the positive factor \((1-u)^{2a}\) shows
\[
\Delta_a(t)>0\qquad(t>0).
\]

Now consider negative arguments. Write
\[
t=-e^{2v}.
\]
For \(v\ne0\), direct substitution and
\[
\sinh((2m+1)v)\sinh((2m-1)v)
=\sinh^2(2mv)-\sinh^2v
\]
give
\[
\frac{\Delta_a(-e^{2v})}{e^{2av}}
=
\left(\frac{\sinh(2mv)}{\sinh v}\right)^2
-1-4m^2\cosh^2v.
\]
The right side extends continuously to \(v=0\) with value \(-1\), agreeing with \(\Delta_a(-1)=-1\).

For \(v>0\), define
\[
R(v)=\frac{\sinh(2mv)}{\sinh v}
=2\sum_{j=1}^{m}\cosh((2j-1)v).
\]
Then
\[
R(v)-2m\cosh v
=
2\sum_{j=2}^{m}
\bigl(\cosh((2j-1)v)-\cosh v\bigr).
\]
This function vanishes at \(v=0\), is positive for \(v>0\), and is strictly increasing there. The function \(R(v)+2m\cosh v\) is positive and strictly increasing for \(v>0\). Consequently
\[
\Psi_m(v):=
\left(R(v)-2m\cosh v\right)
\left(R(v)+2m\cosh v\right)-1
\]
is strictly increasing for \(v>0\), has limiting value \(-1\) as \(v\downarrow0\), and tends to \(+\infty\) as \(v\to\infty\). Hence it has a unique zero \(v_m>0\). That zero is simple because \(\Psi_m'(v)>0\) for \(v>0\).

Thus \(\Delta_a\) has exactly one real zero below \(-1\), namely
\[
-\rho_m,\qquad \rho_m=e^{2v_m}>1.
\]
The displayed formula for \(\Delta_a\) is reciprocal:
\[
t^{2a}\Delta_a(t^{-1})=\Delta_a(t).
\]
Therefore \(-\rho_m^{-1}\in(-1,0)\) is also a zero. Reciprocity maps every negative zero in \((-1,0)\) to one below \(-1\), so these are the only negative zeros. Together with the positive-axis argument, these are exactly the two real zeros of \(\Delta_a\).

## Verification
The proof is symbolic and valid for every \(m\ge2\). Its two critical reductions are independently checkable from elementary identities:

1. the positive-axis Cayley transform is exactly
\[
D_m(u)=E_m(u)^2-u^2(1-u^2)^{2m-2}(u^2+4m^2-1);
\]
2. the negative-axis substitution \(t=-e^{2v}\) is exactly
\[
e^{-2av}\Delta_a(-e^{2v})
=
\left(\frac{\sinh(2mv)}{\sinh v}\right)^2-1-4m^2\cosh^2v.
\]

No finite enumeration is used to infer the infinite-family statement. The strict inequalities and monotonicity arguments apply uniformly for all \(m\ge2\).

## Relationship to prior work
Saurabh studies the same Alexander polynomial in order to rule out Fox--Milnor factorizations for Lecuona's exceptional family. The paper introduces the Cayley-transformed polynomial \(D_m\), then a second auxiliary polynomial \(Q\), and proves a factor-descent contradiction. It does not state or prove the real-zero classification above.

Lecuona's earlier work supplies the Alexander-polynomial formula for the family and uses it in sliceness questions. Searches by the exact family, exact polynomial shape, and combinations of “real roots,” “negative roots,” and “Alexander polynomial” did not locate an earlier statement that the full family has exactly two real roots.

A classical comparison is the isolated pretzel knot \(P(-2,3,7)\), whose Alexander polynomial is known to have exactly two negative real roots. That example is a different knot and a different Alexander polynomial; it neither implies nor contains the uniform statement proved here.

## Limitations
The theorem classifies only the real zeros. It does not locate the remaining nonreal zeros, prove that any of them lie on the unit circle, or determine their limiting distribution as \(a\) grows.

The conclusion is an exact spectral property of the Alexander polynomial, not a new proof of nonsliceness. Saurabh's Fox--Milnor obstruction remains strictly stronger for the sliceness question addressed in that paper.

## References
1. S. Saurabh, *Exceptional pretzel knots are not algebraically slice*, arXiv:2609.34522v1, first submitted 2026-09-28.
2. A. G. Lecuona, *On the slice-ribbon conjecture for pretzel knots*, arXiv:1309.0550; *Algebraic & Geometric Topology* 15 (2015), 2133--2173.
