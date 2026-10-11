# Exact inscribed-quadrilateral constant of real \(\ell_p\) above the Hilbert exponent
## Finding
Let \(I\) be any index set with at least three elements. For every
\[
2\le p<\infty,
\]
the inscribed-quadrilateral constant
\[
J_{\mathrm{in}}(X)
=
\sup\left\{
\sum_{1\le i<j\le4}\|x_i-x_j\|^2:
x_1,x_2,x_3,x_4\in S_X,\ 
x_1+x_2+x_3+x_4=0
\right\}
\]
satisfies
\[
\boxed{
J_{\mathrm{in}}(\ell_p(I))
=
24\left(\frac23\right)^{2/p}
}.
\tag{1}
\]
At the endpoint,
\[
\boxed{
J_{\mathrm{in}}(\ell_\infty(I))=24
},
\tag{2}
\]
which is the limit of (1) as \(p\to\infty\).

A common sharp configuration is the centered tetrahedral four-tuple
\[
x_1=3^{-1/p}(1,1,1),
\]
\[
x_2=3^{-1/p}(1,-1,-1),
\]
\[
x_3=3^{-1/p}(-1,1,-1),
\]
and
\[
x_4=3^{-1/p}(-1,-1,1),
\tag{3}
\]
embedded in any three coordinates of \(I\).

For every
\[
2<p<\infty,
\]
the value in (1) is strictly larger than the two-dimensional value
\[
J_{\mathrm{in}}(\ell_p^2)
=
8\left(1+2^{1-2/p}\right).
\tag{4}
\]
Thus the constant has a strict dimension jump between two and three available coordinates throughout the open super-Hilbert range.

## Assumptions and scope
All scalars are real.

For finite \(p\), \(\ell_p(I)\) has the usual norm
\[
\|x\|_p
=
\left(
\sum_{k\in I}|x(k)|^p
\right)^{1/p}.
\]
At \(p=\infty\),
\[
\|x\|_\infty=\sup_{k\in I}|x(k)|.
\]

The proof uses one finite-dimensional operator. Let
\[
D:\mathbb R^4\longrightarrow\mathbb R^6
\]
be the complete-graph difference operator
\[
D(a_1,a_2,a_3,a_4)
=
(a_i-a_j)_{1\le i<j\le4}.
\tag{5}
\]

## Proof
We first compute the exact \(\ell_p\)-operator norm of \(D\) for \(2\le p\le\infty\).

At \(p=2\),
\[
D^{*}D=4I-J,
\tag{6}
\]
where \(J\) is the \(4\times4\) all-ones matrix. Hence the eigenvalues of \(D^{*}D\) are
\[
0,4,4,4,
\]
so
\[
\|D\|_{\ell_2^4\to\ell_2^6}=2.
\tag{7}
\]

At \(p=\infty\), each output coordinate is the difference of two input coordinates, so
\[
\|Da\|_\infty\le2\|a\|_\infty.
\]
The vector
\[
a=(1,1,-1,-1)
\]
shows equality. Therefore
\[
\|D\|_{\ell_\infty^4\to\ell_\infty^6}=2.
\tag{8}
\]

Riesz--Thorin interpolation between (7) and (8) gives
\[
\|D\|_{\ell_p^4\to\ell_p^6}\le2
\qquad
(2\le p\le\infty).
\tag{9}
\]
The same vector \((1,1,-1,-1)\) has
\[
\|Da\|_p=2\|a\|_p,
\]
so in fact
\[
\boxed{
\|D\|_{\ell_p^4\to\ell_p^6}=2
}
\qquad
(2\le p\le\infty).
\tag{10}
\]

Now let
\[
x_1,x_2,x_3,x_4\in S_{\ell_p(I)}
\]
with
\[
x_1+x_2+x_3+x_4=0.
\]
For each coordinate \(k\in I\), apply (10) to
\[
a(k)=
(x_1(k),x_2(k),x_3(k),x_4(k)).
\]
For finite \(p\), summing the resulting nonnegative inequalities over \(k\) gives
\[
\sum_{i<j}\|x_i-x_j\|_p^p
=
\sum_{k\in I}
\sum_{i<j}|x_i(k)-x_j(k)|^p
\le
2^p
\sum_{k\in I}\sum_{i=1}^4|x_i(k)|^p.
\]
Because every \(x_i\) is a unit vector,
\[
\sum_{i<j}\|x_i-x_j\|_p^p
\le
4\cdot2^p.
\tag{11}
\]

Write
\[
d_{ij}=\|x_i-x_j\|_p.
\]
Since \(p\ge2\), the six-number power-mean inequality yields
\[
\sum_{i<j}d_{ij}^2
\le
6^{1-2/p}
\left(
\sum_{i<j}d_{ij}^p
\right)^{2/p}.
\tag{12}
\]
Combining (11) and (12),
\[
\sum_{i<j}d_{ij}^2
\le
6^{1-2/p}
(4\cdot2^p)^{2/p}
=
24\left(\frac23\right)^{2/p}.
\tag{13}
\]

To attain (13), use the four vectors in (3). Each has unit norm, their sum is zero, and every two differ in exactly two coordinates by magnitude
\[
2\cdot3^{-1/p}.
\]
Hence every pairwise distance is
\[
d_{ij}
=
2\left(\frac23\right)^{1/p}.
\tag{14}
\]
All six distances are equal, so both (11) and (12) are sharp. Summing their squares gives exactly
\[
6\cdot4\left(\frac23\right)^{2/p}
=
24\left(\frac23\right)^{2/p}.
\]
This proves (1).

For \(p=\infty\), every distance between unit vectors is at most \(2\), so
\[
J_{\mathrm{in}}(\ell_\infty(I))\le6\cdot2^2=24.
\]
The four sign vectors in (3), without scaling, have pairwise \(\ell_\infty\)-distance \(2\), so equality holds and (2) follows.

Finally, compare (1) with the known planar value (4). Put
\[
s=1-\frac2p.
\]
For
\[
2<p<\infty,
\]
one has \(0<s<1\), and the strict concavity of
\[
t\longmapsto t^s
\]
on \((0,\infty)\) gives
\[
\frac{1+2^s}{2}
<
\left(\frac32\right)^s.
\]
Equivalently,
\[
1+2^s
<
2\left(\frac32\right)^s.
\tag{15}
\]
Multiplying (15) by \(8\) and rewriting \(s=1-2/p\) gives
\[
8\left(1+2^{1-2/p}\right)
<
24\left(\frac23\right)^{2/p}.
\]
Thus the dimension jump in (4) is strict for every finite \(p>2\).

## Verification
The bundled `verify.py` independently checks the complete-graph incidence identity
\[
D^{*}D=4I-J,
\]
the endpoint norms
\[
\|D\|_{2\to2}=\|D\|_{\infty\to\infty}=2,
\]
the exact equality vector \((1,1,-1,-1)\), and the tetrahedral equality configuration for several representative exponents.

It also samples scalar inputs to the inequality
\[
\sum_{i<j}|a_i-a_j|^p
\le
2^p\sum_i|a_i|^p
\]
and checks the strict dimension-jump comparison numerically for representative \(p>2\).

These numerical samples are reproducibility aids only. The continuum theorem follows from the exact endpoint operator norms, Riesz--Thorin interpolation, the six-number power-mean inequality, and the explicit equality configuration.

## Relationship to prior work
Ahmad, Liu and Li introduced \(J_{\mathrm{in}}\) in 2021, proved the universal bounds
\[
16\le J_{\mathrm{in}}(X)\le24,
\]
characterized Hilbert spaces by the lower endpoint, and related the constant to other geometric parameters and normal structure. Their article discusses selected classical examples and the four-point geometry of the definition, but the inspected full text does not state the all-\(p\), dimension-at-least-three formula (1).

A later exact planar result gives
\[
J_{\mathrm{in}}(\ell_p^2)
=
8\left(1+2^{|2/p-1|}\right).
\]
That theorem is intrinsically two-dimensional. For every finite \(p>2\), inequality (15) shows that its value is strictly smaller than (1), so the planar formula cannot cover the higher-dimensional theorem.

A previously recorded special computation at \(p=4\) yields
\[
J_{\mathrm{in}}(\ell_4(I))=8\sqrt6
\]
when at least three coordinates are available. Formula (1) recovers that isolated exponent because
\[
24\left(\frac23\right)^{1/2}=8\sqrt6,
\]
but the \(p=4\) statement does not imply the continuum family, the sharp incidence-operator mechanism, or the strict dimension jump for every \(2<p<\infty\).

Targeted searches under the exact invariant, \(\ell_p\), tetrahedral and dimension-jump aliases, the candidate formula, and the complete-graph incidence formulation found no statement covering (1).

## Limitations
The theorem determines the super-Hilbert range
\[
2\le p\le\infty
\]
only. It does not determine \(J_{\mathrm{in}}(\ell_p(I))\) for \(1<p<2\) when three or more coordinates are available.

The proof gives one sharp tetrahedral orbit but does not classify every extremizing four-tuple.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent result could exist under a four-point energy, complete-graph incidence, or simplex terminology rather than the notation \(J_{\mathrm{in}}\).

## References
1. A. Ahmad, Q. Liu and Y. Li, “Geometric Constants in Banach Spaces Related to the Inscribed Quadrilateral of Unit Balls,” *Symmetry* 13 (2021), 1294, doi:10.3390/sym13071294. Published 19 July 2021. Mathematics Subject Classification: 46B20.
2. “Inscribed-quadrilateral collapse in strictly convex normed planes,” published research record, 2026.
