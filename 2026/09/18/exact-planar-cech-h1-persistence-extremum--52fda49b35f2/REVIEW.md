# Same-model review

## Correctness

**Assessment: PASS.**

The argument was checked against the main failure modes specific to planar Čech
persistence.

For a general-position point set, the alpha/Delaunay--Čech filtration gives the
same persistent homology as the Čech filtration while providing a planar
geometric one-skeleton. At an intermediate scale \(t\) inside an interval
\([b,d)\), a representing \(\mathbb Z_2\) one-cycle decomposes into finitely many
simple planar cycles. If every summand died before \(d\), their sum would die
before \(d\), so at least one simple polygonal summand \(C\) survives to a death
scale \(d_C\ge d\).

Every edge of \(C\) has length at most \(2t\). For any \(\delta>0\), a point
within \(\delta\) of an edge is within
\(\sqrt{t^2+\delta^2}\) of one of its endpoints. Therefore

\[
B_\delta(C)\subset
B_{\sqrt{t^2+\delta^2}}(V(C)).
\]

If the largest disk enclosed by \(C\) had radius less than
\(\sqrt{d_C^2-t^2}\), the entire polygonal interior would lie in the ball union
at some radius strictly below \(d_C\), contradicting survival of the cycle.
Hence

\[
r(C)\ge\sqrt{d_C^2-t^2}.
\]

The converse geometric estimate was checked separately. If \(C\) has \(q\)
vertices and perimeter \(L\), then its convex hull has perimeter at most \(L\)
and contains every disk contained by \(C\). A convex polygon with at most \(q\)
sides containing a radius-\(r\) disk has perimeter at least

\[
2qr\tan(\pi/q).
\]

This follows by moving its supporting lines inward until tangent to the disk,
then applying Jensen's inequality to the successive normal-angle gaps. Since
\(L\le2qt\), one gets \(r(C)\le t\cot(\pi/q)\). Combining the two bounds gives

\[
d/t\le\csc(\pi/q)\le\csc(\pi/m),
\]

and \(t\downarrow b\) proves the theorem.

Degenerate point sets are not silently excluded: labeled
\(\varepsilon\)-perturbations give general position, the two offset filtrations
are \(\varepsilon\)-interleaved, and barcode stability transfers the inequality
to the limit.

For the regular \(m\)-gon of circumradius one, the nearest-neighbor distance is
\(2\sin(\pi/m)\), so the main hole is born at
\(\sin(\pi/m)\). For every smaller-than-unit radius after birth, the disk union
contains the polygonal boundary but omits its center, so a bounded complementary
component survives. At radius one the union is star-shaped because every disk
contains the center. Thus the death time is exactly one and equality holds.

The inversion
\[
\csc(\pi/m)\ge\rho
\iff
m\ge \pi/\arcsin(1/\rho)
\]
was checked on the relevant branch \(m\ge3,\rho>1\).

## Originality

**Assessment: PASS, to the best of our knowledge.**

The most directly relevant source, Bobrowski--Skraba (arXiv:2609.19474), was
inspected at its deterministic point-count formulation, Proposition 4.3, and
the filling-radius argument in Section 7. It proves that the least number of
points needed for persistence at least \(\rho\) is asymptotic to
\(\mu_k^{\mathrm{cov}}s_k\rho^k\). For \(k=1,d=2\), this gives the leading
constant \(\pi\), but no exact finite formula. Its Lemma 7.3 contains the
inclusion that yields the exact square-root filling-radius lower bound, while
the paper only retains the asymptotic form required for its general theorem.

The earlier Bobrowski--Kahle--Skraba work gives coarse point-count lower bounds
for random-geometric persistence. Gómez--Mémoli give exact persistence-set
results for Vietoris--Rips filtrations and regular configurations on circles,
not a global Čech extremum over arbitrary planar \(m\)-point sets.
Edelsbrunner--Pach study extremal Betti numbers of Čech complexes, not the
death-to-birth ratio.

Targeted searches covered combinations of:
- maximal or multiplicative Čech persistence with planar point sets;
- regular polygons with Čech persistence and exact death-to-birth ratios;
- exact minimum point counts for a prescribed persistent one-cycle;
- the candidate \(\csc(\pi/m)\) and
  \(\lceil\pi/\arcsin(1/\rho)\rceil\) formulas;
- persistent-isoperimetric inequalities and planar polygon inradius bounds.

No prior statement of the finite extremal formula or its exact inverse threshold
was found. The current SCOPE archive was also searched by Čech, multiplicative
persistence, regular-polygon, arcsine, and the motivating arXiv identifier,
without finding an overlapping accepted record.

The regular-polygon barcode is not claimed as new. The claimed contribution is
its global optimality among all \(m\)-point planar clouds and the exact
finite-\(\rho\) point threshold.

The main residual originality risk is recency: the motivating September 2026
preprint is new enough that parallel or not-yet-indexed work may exist. No
specific inaccessible paper was identified as likely to contain the same exact
claim.

## Value

**Assessment: PASS.**

The result closes exactly the first nontrivial finite case of the deterministic
extremal problem underlying the new universal law for extreme Čech cycles.
Instead of only the large-persistence asymptotic

\[
N_\rho^{(1)}(2)\sim\pi\rho,
\]

it gives the complete staircase

\[
N_\rho^{(1)}(2)
=
\left\lceil\frac{\pi}{\arcsin(1/\rho)}\right\rceil
\]

for every \(\rho>1\). The proof also identifies why the regular polygon is
finite-scale optimal: persistence forces an exact filling-radius lower bound,
while a \(q\)-edge planar representative has a sharp polygonal filling-radius
ceiling.

This is more than a parameter substitution into the asymptotic theorem. The
finite correction depends on the sharp perimeter geometry of polygons and is
lost in the continuum covering-density limit.

## Scientific limitations

The theorem is specific to \(H_1\) of planar Euclidean Čech filtrations. It does
not solve the finite extremal problem in higher homological or ambient
dimensions. No uniqueness theorem for equality cases is asserted. The statement
is made over \(\mathbb Z_2\) to remain aligned with the source problem, even
though parts of the planar argument may extend to other coefficient fields.
The recent date of the motivating preprint leaves a residual risk of unindexed
parallel work.

Same-model review: passed. Independent audit: not yet performed.
