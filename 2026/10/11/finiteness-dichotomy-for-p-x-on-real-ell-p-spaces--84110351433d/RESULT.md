# Finiteness dichotomy for \(P(X)\) on real \(\ell_p\) spaces
## Finding
Let \(I\) be an index set with at least two elements. For the Zhou--Ni--Liu--Li quantity
\[
P(X)
=
\sup_{x\not\perp_P y}
\frac{\|x\|^2+\|y\|^2-\|x+y\|^2}
{\|x\|^2+\|y\|^2-\|x-y\|^2},
\]
where
\[
x\perp_P y
\quad\Longleftrightarrow\quad
\|x-y\|^2=\|x\|^2+\|y\|^2,
\]
the real sequence spaces satisfy the complete dichotomy
\[
P(\ell_p(I))
=
\begin{cases}
-1,&p=2,\\[4pt]
+\infty,&1\le p\le\infty,\ p\ne2.
\end{cases}
\]
Here \(+\infty\) is meant in the extended-real sense: the defining quotient is unbounded above on admissible pairs.

Consequently, the Hilbert exponent \(p=2\) is the unique finite point of the whole real \(\ell_p\) scale. In particular, unboundedness is not a polyhedral pathology: it occurs for every smooth uniformly convex \(\ell_p(I)\) with
\[
1<p<\infty,
\qquad
p\ne2.
\]

## Assumptions and scope
All spaces and scalars are real, and
\[
|I|\ge2.
\]
For \(1\le p<\infty\),
\[
\|(a_i)\|_p
=
\left(\sum_{i\in I}|a_i|^p\right)^{1/p},
\]
while
\[
\|(a_i)\|_\infty=\sup_{i\in I}|a_i|.
\]

Only two coordinates are used in the unboundedness construction. Therefore it is enough to work in \(\ell_p^2\), because every \(\ell_p(I)\) with \(|I|\ge2\) contains an isometric coordinate copy of \(\ell_p^2\), and the defining supremum over the larger space contains every quotient from that copy.

For \(1\le p<\infty\), set
\[
x=(1,0),
\qquad
y_b=(b,1),
\qquad
-1\le b\le1,
\]
and write
\[
A_p(b)=1+\left(1+|b|^p\right)^{2/p},
\]
\[
D_p(b)
=
A_p(b)
-
\left((1-b)^p+1\right)^{2/p},
\]
\[
N_p(b)
=
A_p(b)
-
\left((1+b)^p+1\right)^{2/p}.
\]
Whenever
\[
D_p(b)\ne0,
\]
the pair is admissible and its \(P\)-quotient is
\[
Q_p(b)=\frac{N_p(b)}{D_p(b)}.
\]

## Proof
First suppose
\[
2<p<\infty.
\]
At \(b=0\),
\[
D_p(0)
=
2-2^{2/p}
>
0.
\]
At \(b=-1\),
\[
D_p(-1)
=
1+2^{2/p}-(2^p+1)^{2/p}.
\]
Since \(p>2\),
\[
1+2^{2/p}<3
\]
and
\[
(2^p+1)^{2/p}>4,
\]
so
\[
D_p(-1)<0.
\]
By continuity, the open component of
\[
\{b\in(-1,0]:D_p(b)>0\}
\]
that contains \(0\) has a left boundary point
\[
b_p\in(-1,0)
\]
with
\[
D_p(b_p)=0.
\]
At that point,
\[
A_p(b_p)
=
\left((1-b_p)^p+1\right)^{2/p}.
\]
Because
\[
1-b_p>1+b_p>0,
\]
we have
\[
N_p(b_p)>0.
\]
Choose
\[
b_n\downarrow b_p
\]
inside the positive component. Then
\[
D_p(b_n)>0,
\qquad
D_p(b_n)\to0,
\qquad
N_p(b_n)\to N_p(b_p)>0,
\]
and therefore
\[
Q_p(b_n)\to+\infty.
\]
Hence
\[
P(\ell_p^2)=+\infty
\qquad
(2<p<\infty).
\]

Now suppose
\[
1\le p<2.
\]
At \(b=0\),
\[
D_p(0)
=
2-2^{2/p}
<
0,
\]
while
\[
D_p(1)
=
2^{2/p}
>
0.
\]
Thus the open component of
\[
\{b\in[0,1):D_p(b)<0\}
\]
that contains \(0\) has a right boundary point
\[
b_p\in(0,1)
\]
with
\[
D_p(b_p)=0.
\]
At the zero,
\[
A_p(b_p)
=
\left((1-b_p)^p+1\right)^{2/p}.
\]
Since
\[
1+b_p>1-b_p\ge0,
\]
we obtain
\[
N_p(b_p)<0.
\]
Choose
\[
b_n\uparrow b_p
\]
inside the negative component. Then
\[
D_p(b_n)<0,
\qquad
D_p(b_n)\to0,
\qquad
N_p(b_n)\to N_p(b_p)<0,
\]
and again
\[
Q_p(b_n)\to+\infty.
\]
Therefore
\[
P(\ell_p^2)=+\infty
\qquad
(1\le p<2).
\]

For
\[
p=\infty,
\]
keep
\[
x=(1,0),
\qquad
y_b=(b,1),
\qquad
-1\le b\le0.
\]
Then
\[
\|x\|_\infty=\|y_b\|_\infty=1,
\]
\[
\|x-y_b\|_\infty=1-b,
\]
and
\[
\|x+y_b\|_\infty=1.
\]
Thus
\[
D_\infty(b)=2-(1-b)^2,
\qquad
N_\infty(b)=1.
\]
The denominator vanishes at
\[
b_\infty=1-\sqrt2\in(-1,0).
\]
As
\[
b\downarrow b_\infty
\]
from above,
\[
D_\infty(b)\downarrow0
\]
while
\[
N_\infty(b)=1,
\]
so
\[
Q_\infty(b)\to+\infty.
\]

Finally,
\[
\ell_2(I)
\]
is a Hilbert space. The parallelogram identity gives, for every admissible pair,
\[
\|x\|^2+\|y\|^2-\|x+y\|^2
=
-\left(
\|x\|^2+\|y\|^2-\|x-y\|^2
\right),
\]
hence every defining quotient equals
\[
-1.
\]
Therefore
\[
P(\ell_2(I))=-1.
\]

Since the unbounded examples use only two coordinates, the same conclusion holds for every index set with at least two elements.

## Verification
The proof uses only continuity, explicit endpoint signs, and elementary comparisons of the two \(\ell_p\) chord lengths.

The bundled `verify.py` independently reconstructs the functions
\[
D_p(b)
\quad\text{and}\quad
N_p(b)
\]
for representative exponents on both sides of \(2\). It locates the sign-changing Pythagorean point by bisection and checks that the quotient exceeds a large threshold when approached from the appropriate side.

The script separately checks the exact \(p=\infty\) formula and verifies the Hilbert value \(-1\) on several nonorthogonal pairs.

These finite checks are reproducibility aids only. The all-\(p\) statement follows from the analytic sign arguments above.

## Relationship to prior work
Zhou, Ni, Liu and Li introduced \(P(X)\) in 2023 from the parallelogram law and Pythagorean orthogonality. Their paper proves the universal lower bound
\[
P(X)\ge-1,
\]
characterizes Hilbert spaces by
\[
P(X)=-1,
\]
derives further lower estimates, and discusses sequence-space constructions. The inspected \(P(X)\) section contains no finiteness theorem and no exact \(\ell_p\) classification.

The paper's sequence-space discussion therefore does not determine whether the defining supremum is finite. The present result gives the sharp answer on the most classical one-parameter Banach scale: finite exactly at the Hilbert exponent and unbounded everywhere else.

A previously available exact unboundedness example for a regular octagonal plane shows that divergence can occur in a polyhedral norm. The present classification is strictly stronger in geometric scope: it shows that divergence persists throughout the smooth and uniformly convex range
\[
1<p<\infty,
\qquad
p\ne2,
\]
and isolates \(p=2\) as the unique finite exponent.

Targeted searches under the defining notation, Pythagorean-orthogonality aliases, \(\ell_p\)-space terminology, and unbounded/infinite-supremum formulations found no published statement covering this dichotomy. The closest indexed \(\ell_p\) results concern different invariants such as the \(P\)-angle constant and generalized James constants.

## Limitations
The theorem concerns the specific Zhou--Ni--Liu--Li quotient \(P(X)\); similarly named \(P\)-angle and Pythagorean constants in the literature are different invariants.

The result classifies real \(\ell_p(I)\) spaces, not arbitrary \(L_p\) spaces or general uniformly convex spaces.

The proof establishes unboundedness rather than attainment: for
\[
p\ne2,
\]
the quotient diverges along admissible pairs approaching a Pythagorean-orthogonal pair at which the denominator vanishes.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent observation could appear under a reformulation of the same quotient without the notation \(P(X)\).

## References
1. Y. Zhou, Q. Ni, Q. Liu and Y. Li, “Geometric constants and orthogonality in Banach spaces,” Contributions to Mathematics 8 (2023), 38–47, doi:10.47443/cm.2023.045. Published online 11 September 2023.
