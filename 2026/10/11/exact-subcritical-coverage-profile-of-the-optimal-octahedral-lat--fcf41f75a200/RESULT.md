# Exact subcritical coverage profile of the optimal octahedral lattice

## Finding

Let
\[
O=\left\{x\in\mathbb R^3:\lVert x\rVert_1\le1}\right\},
\qquad
L_0=2\mathbb Z^3\cup\left((1,1,1)+2\mathbb Z^3\right).
\]
For \(0\le r\le3/2\), consider the periodic family \(rO+L_0\). Let \(u(r)\) be the fraction of a fundamental cell of \(L_0\) left uncovered, and let \(d(r)\) be the fraction covered by exactly two translates, ignoring measure-zero boundaries. Then
\[
(u(r),d(r))=
\begin{cases}
(1-r^3/3,0),&0\le r\le1,\\
(r(3-r)(3-2r)/3,(r-1)^3),&1\le r\le3/2.
\end{cases}
\]
For \(1<r<3/2\), every point outside a null set has covering multiplicity at most two. Consequently the singly covered fraction is
\[
1-u(r)-d(r)=\frac{r^3}3-2(r-1)^3.
\]
At the sharp covering radius \(r=3/2\),
\[
u(3/2)=0,
\qquad
d(3/2)=\frac18,
\qquad
1-u(3/2)-d(3/2)=\frac78.
\]
Thus the density excess of the optimal lattice covering,
\[
\frac98-1=\frac18,
\]
is exactly the fraction of space covered twice. The approach to covering is also explicit: for \(r=3/2-\varepsilon\),
\[
u(r)=\frac32\varepsilon-\frac23\varepsilon^3.
\]

## Assumptions and scope

The octahedron is normalized as the unit ball of the \(\ell_1\) norm. The lattice \(L_0\) has covolume \(4\). Lian and Xue prove that \((3/2)O+L_0\) covers \(\mathbb R^3\), and that the resulting density \(9/8\) is the optimal lattice covering density of the regular octahedron. The result here keeps their optimizer fixed and determines the complete volume-multiplicity profile along the natural radial path \(rO+L_0\) up to that covering radius.

All multiplicity statements are understood almost everywhere. At \(r=1\) and \(r=3/2\), additional contacts occur on lower-dimensional sets, but those contacts have zero three-dimensional volume and do not alter the stated fractions.

## Proof

The volume of \(rO\) is
\[
\operatorname{vol}(rO)=\frac43r^3.
\]
The nonzero vectors of \(L_0\) with \(\ell_1\)-norm at most \(3\) are exactly
\[
\{\pm2e_1,\pm2e_2,\pm2e_3\}
\]
with norm \(2\), together with the eight sign vectors
\[
(\pm1,\pm1,\pm1)
\]
with norm \(3\). Indeed, an even-coset vector has all coordinates even, so norm below \(4\) leaves only one coordinate equal to \(\pm2\); an odd-coset vector has all coordinates odd, so norm at most \(3\) forces all three absolute coordinates to equal \(1\).

For \(0\le r\le1\), interiors of distinct translates are disjoint because the minimum nonzero lattice distance in the \(\ell_1\) norm is \(2\). Hence the covered fraction is simply
\[
\frac{\operatorname{vol}(rO)}{\det L_0}=
\frac{(4/3)r^3}4=\frac{r^3}3,
\]
which gives \(u(r)=1-r^3/3\) and \(d(r)=0\).

Now let \(1\le r\le3/2\). Positive-volume pairwise intersections can occur only for center differences \(\pm2e_i\). The odd-coset vectors have distance \(3\), so at \(r=3/2\) they create only boundary contact, and longer lattice vectors cannot meet at all in this range.

It remains to compute one short-vector lens. Consider \(rO\) and \(rO+2e_1\). If \(x_1=1+t\) and \(a=r-1\), then the intersection condition is equivalent to
\[
|x_2|+|x_3|\le a-|t|,
\qquad
|t|\le a.
\]
The planar \(\ell_1\)-ball of radius \(q\) has area \(2q^2\), so the lens volume is
\[
V_2(r)=\int_{-a}^a2(a-|t|)^2\,dt
=\frac43(r-1)^3.
\]
Each lattice center has six such short neighbors, hence there are three unordered short-neighbor pairs per fundamental cell.

There is no positive-volume triple intersection in this range. If two distinct short neighbors of the same center are chosen, their difference has \(\ell_1\)-norm \(4\), while \(2r\le3\), so their translates are disjoint. Any translate whose center is an odd-coset vector can meet a given translate only on a null boundary set at \(r=3/2\). Therefore the three pairwise lens volumes per cell are disjoint up to null sets.

The double-covered volume per fundamental cell is thus
\[
3V_2(r)=4(r-1)^3,
\]
and division by \(\det L_0=4\) gives
\[
d(r)=(r-1)^3.
\]
Inclusion-exclusion has no positive-volume term beyond pairs, so the union volume per fundamental cell is
\[
\frac43r^3-4(r-1)^3.
\]
Dividing by \(4\) gives the covered fraction
\[
\frac{r^3}3-(r-1)^3,
\]
and hence
\[
u(r)=1-\frac{r^3}3+(r-1)^3
=\frac{r(3-r)(3-2r)}3.
\]
At \(r=3/2\), Lian and Xue's covering theorem makes this zero, while \(d(3/2)=1/8\). Finally, substituting \(r=3/2-\varepsilon\) into the exact factorization gives
\[
u(r)=\frac32\varepsilon-\frac23\varepsilon^3.
\]

## Verification

The proof is analytic and does not infer any infinite statement from a finite experiment. A standalone exact-arithmetic checker included with this result verifies the short-vector classification through the only norm range relevant to the proof, the polynomial identities for \(u(r)\), and the endpoint values \(u(3/2)=0\), \(d(3/2)=1/8\), and single-coverage fraction \(7/8\). The checker was replayed from the embedded package bytes after the ledger file was reopened.

## Relationship to prior work

Lian and Xue prove that the lattice covering density of the regular octahedron is \(9/8\). In their normalization \(K=(3/2)O\), they exhibit the body-centered cubic lattice
\[
L_0=2\mathbb Z^3\cup\left((1,1,1)+2\mathbb Z^3\right)
\]
of covolume \(4\), and verify directly that \(K+L_0\) covers. Their main contribution is the matching global lower bound on the determinant of every lattice covering. The inspected source states the optimizer and density, but not the subcritical union-volume formula, the exact double-coverage fraction, or the almost-everywhere multiplicity distribution along \(rO+L_0\).

Dougherty and Faber connected the degree-diameter problem for Abelian Cayley graphs with lattice coverings by octahedra and conjectured the three-dimensional optimum later settled by Lian and Xue. Their inspected abstract and the historical discussion in the 2026 paper concern the covering optimization, not the subcritical multiplicity profile derived here.

Targeted semantic searches were made for the exact formulas \(r(3-r)(3-2r)/3\) and \((r-1)^3\), for the statement that the \(9/8\) density excess is exactly the double-covered fraction, and for aliases involving the body-centered cubic octahedral covering. No checked result stated or implied this profile. The closest indexed records concern a planar parallelogram covering-radius profile, a \(D_5^+\) packing-covering ray, and overlap formulas for spherical caps; their objects and implications are different.

## Limitations

The theorem fixes the Lian--Xue optimal lattice and varies only the common scale of the octahedron. It does not establish stability with respect to arbitrary lattice deformations, classify all lattices attaining density \(9/8\), or describe multiplicities for \(r>3/2\), where the odd-coset contacts become positive-volume overlaps and higher-order intersections must be included. The originality search cannot exclude an unindexed historical calculation of the same periodic union profile; that remains the principal residual risk.

## References

Y. Lian and F. Xue, “The lattice covering density of the regular octahedron,” arXiv:2609.23210v1, first submitted 2026-09-19. Primary MSC 52C17.

R. Dougherty and V. Faber, “The degree-diameter problem for several varieties of Cayley graphs, I: the Abelian case,” arXiv:math/9412223; SIAM Journal on Discrete Mathematics 17 (2004), 478–519.
