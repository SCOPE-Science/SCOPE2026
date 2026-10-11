# The two sharp close-to-convex harmonic Bohr radii cross exactly once

## Finding

Let
\[
M_c=\frac{1}{2(\log4-1)}.
\]
For
\[
0<M<M_c,
\]
define \(r_1(M)\) and \(r_2(M)\) as the unique roots in \((0,1)\) of
\[
r+2M\bigl(r-(1-r)\log(1-r)\bigr)
=
1+2M(1-2\log2)
\]
and
\[
r+2M\bigl(r+(1-2r)\log(1-r)\bigr)
=
1+2M(1-2\log2),
\]
respectively.

These are the two sharp radii appearing in Corollaries 2.1 and 2.2 of the recent close-to-convex harmonic Bohr theorem: \(r_1\) corresponds to the classical basis \(r^n\), while \(r_2\) corresponds to the differentiated basis \((n+1)r^n\).

Both functions are \(C^1\) and strictly decreasing on \((0,M_c)\). They satisfy
\[
\lim_{M\downarrow0}r_j(M)=1,
\qquad
\lim_{M\uparrow M_c}r_j(M)=0
\]
for \(j=1,2\).

There is exactly one parameter at which the sharp radii agree:
\[
M_*=
\frac{1}{2(\log192-1)}
=
0.117439939755438\ldots,
\]
and at this parameter
\[
r_1(M_*)=r_2(M_*)=\frac23.
\]

The ordering reverses there:
\[
0<M<M_*
\quad\Longrightarrow\quad
r_2(M)<r_1(M),
\]
whereas
\[
M_*<M<M_c
\quad\Longrightarrow\quad
r_1(M)<r_2(M).
\]

The endpoint approaches are also inequivalent. As \(M\downarrow0\),
\[
1-r_1(M)
\sim
4(\log2)M,
\]
but
\[
1-r_2(M)
\sim
2M\log\frac1M.
\]
Thus the second radius has a logarithmically larger deficit from \(1\) at small \(M\).

At the opposite endpoint, put
\[
\eta=1-\frac{M}{M_c}.
\]
Then, as \(M\uparrow M_c\),
\[
r_1(M)
\sim
\frac{\eta}{1+4M_c},
\qquad
r_2(M)
\sim
\eta.
\]

Hence the two sharp generalized Bohr inequalities undergo an exact one-crossing phase transition, with different asymptotic scales at both ends of the admissible parameter interval.

## Assumptions and scope

The underlying harmonic class is the class denoted
\[
\mathcal P_{\mathcal H}^{0}(M)
\]
in the source. The source assumes
\[
0<M<M_c
=
\frac{1}{2(\log4-1)}
\]
and proves that the displayed equations have unique roots in \((0,1)\), each giving a sharp Bohr radius.

The present result compares exactly those two already-sharp source radii. It does not claim that either generalized Bohr functional dominates the other pointwise for every harmonic mapping. The comparison is solely between the largest universal radii certified by the two sharp inequalities.

The source uses the classical basis
\[
\varphi_n(r)=r^n
\]
for \(r_1\), and the choice
\[
\varphi_0(r)=1,
\qquad
\varphi_n(r)=(n+1)r^n
\]
for \(n\ge1\) in the inequality producing \(r_2\).

## Proof

Put
\[
c=1-2\log2<0,
\]
and define
\[
A_1(r)
=
r-(1-r)\log(1-r),
\]
\[
A_2(r)
=
r+(1-2r)\log(1-r).
\]
The two root equations are
\[
H_j(r,M)
=
r+2MA_j(r)-(1+2Mc)
=
0,
\qquad
j=1,2.
\]

At either root,
\[
1-r
=
2M\bigl(A_j(r)-c\bigr).
\]
Hence
\[
A_j(r)-c>0
\]
and
\[
\frac{\partial H_j}{\partial M}
=
2\bigl(A_j(r)-c\bigr)
=
\frac{1-r}{M}
>
0.
\]

For \(j=2\),
\[
A_2'(r)
=
\frac{r}{1-r}
-
2\log(1-r)
>
0,
\]
so
\[
\frac{\partial H_2}{\partial r}>1.
\]

For \(j=1\), write
\[
\varepsilon=1-r.
\]
Then
\[
A_1(r)-c
=
2\log2-\varepsilon(1+\log\varepsilon).
\]
Using
\[
2M
=
\frac{\varepsilon}
{2\log2-\varepsilon(1+\log\varepsilon)}
\]
at the root gives
\[
\frac{\partial H_1}{\partial r}
=
1+2M(2+\log\varepsilon)
=
\frac{2\log2+\varepsilon}
{2\log2-\varepsilon(1+\log\varepsilon)}
>
0.
\]

The implicit-function theorem therefore applies to both roots, and
\[
r_j'(M)
=
-
\frac{\partial_M H_j}
{\partial_r H_j}
<
0.
\]
Thus both sharp radii are \(C^1\) and strictly decreasing.

Now compare the two equations at the same \(r\):
\[
H_2(r,M)-H_1(r,M)
=
2M(2-3r)\log(1-r).
\]
The difference vanishes in the open unit interval exactly at
\[
r=\frac23.
\]
Substituting \(r=2/3\) into either root equation gives
\[
\frac23
+
2M
\left(
\frac23+\frac{\log3}{3}
\right)
=
1+2M(1-2\log2).
\]
Equivalently,
\[
\frac13
=
\frac{2M}{3}(\log192-1),
\]
so the unique common parameter is
\[
M_*=
\frac{1}{2(\log192-1)}.
\]

Because both radii are strictly decreasing, they are greater than \(2/3\) for \(M<M_*\) and smaller than \(2/3\) for \(M>M_*\).

If \(M<M_*\), then at \(r=r_1(M)>2/3\),
\[
H_2(r_1(M),M)-H_1(r_1(M),M)>0.
\]
Since \(H_1(r_1(M),M)=0\) and \(H_2(\,\cdot\,,M)\) is strictly increasing,
\[
r_2(M)<r_1(M).
\]

If \(M>M_*\), then \(r_1(M)<2/3\), so
\[
H_2(r_1(M),M)<0.
\]
Again using strict increase of \(H_2\) gives
\[
r_2(M)>r_1(M).
\]

For the small-\(M\) endpoint, put
\[
\varepsilon_j=1-r_j(M).
\]
The first root equation becomes exactly
\[
\varepsilon_1
=
2M
\left(
2\log2
-
\varepsilon_1(1+\log\varepsilon_1)
\right).
\]
Since
\[
\varepsilon_1\log\varepsilon_1\to0,
\]
it follows that
\[
\varepsilon_1
\sim
4(\log2)M.
\]

For the second root,
\[
\varepsilon_2
=
2M
\left(
2\log2
-
\log\varepsilon_2
-
\varepsilon_2
+
2\varepsilon_2\log\varepsilon_2
\right).
\]
The bracket equals
\[
\log\frac1{\varepsilon_2}+O(1).
\]
The equation implies
\[
\log\frac1{\varepsilon_2}
=
\log\frac1M
+
O\!\left(\log\log\frac1M\right),
\]
and therefore
\[
\varepsilon_2
\sim
2M\log\frac1M.
\]

Finally,
\[
1+2Mc
=
1-\frac{M}{M_c}
=
\eta.
\]
As \(r\downarrow0\),
\[
A_1(r)
=
2r-\frac{r^2}{2}+O(r^3),
\]
while
\[
A_2(r)
=
\frac32r^2+O(r^3).
\]
The two root equations therefore give
\[
\eta
=
(1+4M)r_1
-
Mr_1^2
+
O(r_1^3),
\]
and
\[
\eta
=
r_2
+
3Mr_2^2
+
O(r_2^3).
\]
Letting \(M\uparrow M_c\) yields
\[
r_1(M)
\sim
\frac{\eta}{1+4M_c},
\qquad
r_2(M)
\sim
\eta.
\]

## Verification

The source equations were checked directly against Corollaries 2.1 and 2.2 of arXiv:2606.29810v1.

The crossing calculation is exact:
\[
A_2(r)-A_1(r)
=
(2-3r)\log(1-r),
\]
so the only possible interior equality point is
\[
r=2/3.
\]
Substitution then gives the exact parameter
\[
M_*=
1/[2(\log192-1)].
\]

The sign of each implicit derivative is proved symbolically at the root. In particular, the potentially non-obvious derivative for \(r_1\) reduces to a ratio with numerator
\[
2\log2+\varepsilon>0.
\]

The asymptotic expansions use exact transformed root equations and Taylor expansions around \(r=1\) or \(r=0\). No finite numerical table is used to infer the global ordering or endpoint laws.

As a numerical consistency check only,
\[
M_*=0.117439939755438\ldots,
\]
and the source equations return
\[
r_1(M_*)=r_2(M_*)=0.666666666666\ldots.
\]

## Relationship to prior work

Ahamed and Roy introduced the generalized basis formulation for the close-to-convex harmonic class and proved that the two displayed equations define sharp radii. Their paper also presents numerical values and figures for these roots. In the inspected full text, however, no theorem compares the two radius functions, no exact crossover parameter is stated, and no endpoint comparison of their parameter dependence is derived.

The \(r_1\) equation is a previously known classical-basis radius recovered in the recent paper as a special case, while the \(r_2\) equation comes from a different generalized basis. Earlier close-to-convex harmonic Bohr papers establish sharp radii for related functionals but do not imply the one-crossing law between these two 2026 radius functions.

The new point is therefore not another coefficient estimate or another isolated radius computation. It is a complete comparative phase diagram for two sharp radii already placed side by side by the source.

## Limitations

The theorem compares only the two specific sharp radii defined by the source equations. Other admissible generalized bases can produce different sharp-radius functions and need not share the same crossing behavior.

The logarithmic endpoint law for \(r_2\) is first-order. A fuller expansion would involve iterated logarithmic corrections.

The source is a recent preprint. The originality comparison used its full accessible text, targeted searches for the exact equations and crossover, and nearby harmonic Bohr literature, but older literature may use different notation for analogous implicit-radius comparisons.

## References

1. M. B. Ahamed and P. P. Roy, *The Bohr Phenomenon for Close-to-Convex Harmonic Mappings*, arXiv:2606.29810v1, first posted 29 June 2026.
2. V. Allu and H. Halder, *Bohr phenomenon for certain subclasses of harmonic mappings*, Bulletin des Sciences Mathématiques 173 (2021), 103053.
3. M. B. Ahamed, V. Allu, and H. Halder, *Bohr radius for certain classes of close-to-convex harmonic mappings*, Analysis and Mathematical Physics 11 (2021), Article 111.
