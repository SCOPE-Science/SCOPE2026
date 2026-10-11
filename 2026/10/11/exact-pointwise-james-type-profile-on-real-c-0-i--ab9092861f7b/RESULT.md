# Exact pointwise James type profile on real \(c_0(I)\)
## Finding
Let \(I\) be an infinite index set and let
\[
X=c_0(I;\mathbb R).
\]
For \(x=(x_i)_{i\in I}\in S_X\), write \(s_2(x)\) for the second-largest member of the multiset
\[
\{|x_i|:i\in I\},
\]
counted with multiplicity. Because \(x\in c_0(I)\), its largest and second-largest coordinate moduli are attained.

For every parameter
\[
-\infty\le t<\infty,
\]
the pointwise James type constant of Rincón--Villamizar is
\[
\boxed{
J(x,X,t)=M_t\bigl(2,1+s_2(x)\bigr)
},
\tag{1}
\]
where \(M_t\) is the generalized two-variable power mean. Thus, when
\[
t\in\mathbb R\setminus\{0\},
\]
\[
\boxed{
J(x,X,t)
=
\left(
\frac{2^t+(1+s_2(x))^t}{2}
\right)^{1/t}
},
\tag{2}
\]
while
\[
\boxed{
J(x,X,0)=\sqrt{2(1+s_2(x))}
}
\tag{3}
\]
and
\[
\boxed{
J(x,X,-\infty)=1+s_2(x)
}.
\tag{4}
\]

Consequently, for every fixed \(t\), the pointwise profile on \(S_X\) has the complete range
\[
\left[M_t(2,1),2\right].
\tag{5}
\]
Its minimum \(M_t(2,1)\) is attained exactly at the signed coordinate vectors, and its maximum \(2\) is attained exactly at unit vectors having at least two coordinates of modulus \(1\).

## Assumptions and scope
For positive \(a,b\), the generalized mean is
\[
M_t(a,b)
=
\left(\frac{a^t+b^t}{2}\right)^{1/t}
\qquad
(t\ne0),
\]
with
\[
M_0(a,b)=\sqrt{ab},
\qquad
M_{-\infty}(a,b)=\min\{a,b\}.
\]

The pointwise James type constant is
\[
J(x,X,t)
=
\sup_{y\in S_X}
M_t\bigl(\|x+y\|,\|x-y\|\bigr).
\tag{6}
\]

For an arbitrary index set \(I\), \(c_0(I)\) consists of scalar families that vanish at infinity: for every \(\varepsilon>0\), only finitely many coordinates have modulus at least \(\varepsilon\). This implies that every nonzero element has a largest coordinate modulus. After removing one maximizing coordinate, the remaining family again has a largest modulus unless it is identically zero; this gives \(s_2(x)\).

The theorem is stated for infinite \(I\). Finite-dimensional \(\ell_\infty^n\) has an analogous formula in the parameter range \(t\ge1\), but its standard proof uses a finite-dimensional extreme-point reduction. Formula (1) does not use that reduction and covers the complete parameter interval on \(c_0(I)\).

## Proof
Fix
\[
x\in S_X.
\]
Choose a coordinate \(k\in I\) such that
\[
|x_k|=1.
\]
Put
\[
s=s_2(x).
\]

Take arbitrary
\[
y\in S_X.
\]
Choose
\[
\sigma\in\{-1,1\}
\]
so that
\[
|x_k+\sigma y_k|\le1.
\tag{7}
\]
For every \(j\ne k\),
\[
|x_j+\sigma y_j|
\le
|x_j|+|y_j|
\le
s+1.
\]
Together with (7), this yields
\[
\|x+\sigma y\|_\infty\le1+s.
\tag{8}
\]
For the opposite sign, the triangle inequality gives
\[
\|x-\sigma y\|_\infty\le2.
\tag{9}
\]

The generalized power means are increasing in each positive argument. Therefore (8)--(9), without needing to know which chord is the longer one, give
\[
M_t\bigl(\|x+y\|_\infty,\|x-y\|_\infty\bigr)
\le
M_t(2,1+s)
\tag{10}
\]
for every
\[
-\infty\le t<\infty.
\]
Taking the supremum over \(y\in S_X\) proves the upper bound in (1).

For sharpness, first suppose
\[
s>0.
\]
Choose \(l\ne k\) with
\[
|x_l|=s.
\]
Define a finitely supported \(y\in S_X\) by
\[
y_k=\operatorname{sgn}(x_k),
\qquad
y_l=-\operatorname{sgn}(x_l),
\]
and
\[
y_j=0
\qquad
(j\notin\{k,l\}).
\]
Then
\[
\|x+y\|_\infty=2
\]
because of coordinate \(k\), whereas
\[
\|x-y\|_\infty=1+s
\]
because of coordinate \(l\).

If
\[
s=0,
\]
then \(x\) is a signed coordinate vector. Choose any \(l\ne k\) and put
\[
y_k=\operatorname{sgn}(x_k),
\qquad
y_l=1,
\]
with all other coordinates zero. Again,
\[
\|x+y\|_\infty=2,
\qquad
\|x-y\|_\infty=1.
\]
Thus equality holds in (10) in all cases, proving (1)--(4).

Finally, every
\[
s\in[0,1]
\]
occurs as the second-largest modulus of a unit vector: choose distinct \(k,l\in I\) and take
\[
x=e_k+s e_l.
\]
Since \(M_t(2,1+s)\) is increasing in \(s\), this proves the complete range (5). Moreover,
\[
s_2(x)=0
\]
exactly for signed coordinate vectors, while
\[
s_2(x)=1
\]
exactly when at least two coordinates have modulus \(1\). The extremizer statements follow.

## Verification
The proof is coordinatewise and valid on the full infinite-dimensional space. Its only structural inputs are:
\[
\|x\|_\infty=1,
\]
attainment of the two largest coordinate moduli in \(c_0(I)\), and coordinatewise monotonicity of generalized means.

The bundled `verify.py` performs deterministic finite-support stress tests. For many rational unit vectors \(x\), rational unit vectors \(y\), and parameters on both sides of zero, it verifies the upper bound
\[
M_t(\|x+y\|_\infty,\|x-y\|_\infty)
\le
M_t(2,1+s_2(x)).
\]
It also constructs the proof's two-coordinate witness and checks equality numerically for every tested parameter, including \(t=0\) and \(t=-\infty\).

The finite tests are supplementary. They are not used to infer the infinite-dimensional theorem.

## Relationship to prior work
Rincón--Villamizar introduced the pointwise James type constant and studied its continuity, isometric invariance, transitivity consequences, Hilbert-space behavior, and its relation to the global James type constant. The paper also proves an extreme-point formula for finite-dimensional spaces when \(t\ge1\).

The complete article text was inspected for \(c_0\), for infinite-dimensional \(\ell_\infty\)-type examples, and around the finite-dimensional extreme-point proposition. No \(c_0(I)\) formula is stated there. In particular, the finite-dimensional proposition assumes finite dimension and is confined to the section \(t\ge1\); it does not imply (1) for \(c_0(I)\) or the negative and zero parameters.

Targeted literature-index searches used the exact invariant, \(c_0\), the second-largest-coordinate description, the explicit formula, and infinite-dimensional aliases. The closest indexed pointwise-James result concerns constancy thresholds in \(\ell_p\) above the Hilbert exponent, not \(c_0\) and not formula (1). Separate exact results for pointwise \(\Delta\)-constants of \(c_0\) concern a different slice-based invariant.

The key distinction is that (1) is a complete pointwise classification on a nonreflexive infinite-dimensional space. Its proof directly controls the two opposite chords and therefore works for the entire generalized-mean scale, including parameters not reached by the finite-dimensional extreme-point argument.

## Limitations
The theorem is specific to the sup norm on \(c_0(I)\). It does not assert an analogous second-largest-coordinate formula for arbitrary \(C(K)\) spaces or other \(M\)-spaces.

No statement is made for a formal \(t=+\infty\) endpoint, since the defining source uses
\[
-\infty\le t<\infty.
\]

Bibliographic and semantic-index searches cannot establish absolute novelty. An equivalent formula could have appeared under older pointwise nonsquareness notation rather than the pointwise James type notation.

## References
1. M. A. Rincón-Villamizar, “The pointwise James type constant,” *Analysis Mathematica* 49 (2023), 651--659, doi:10.1007/s10476-023-0221-7.
