# Sharp four-regime partial-plank profile of the regular hexagon

## Finding
Let \(H=\operatorname{conv}\{(\cos(j\pi/3),\sin(j\pi/3)):j=0,\ldots,5\}\), the Euclidean regular hexagon of circumradius one, area \(A=3\sqrt3/2\), and minimum width \(w(H)=\sqrt3\). For \(0<W<\sqrt3\), let \(M(W)\) be the largest area of \(H\) covered by an arbitrary **finite** family of Euclidean planks whose total width is at most \(W\). A single centered plank of width \(W\) always attains \(M(W)\). Its maximizing **normal direction** is unique modulo the dihedral symmetries of \(H\), and undergoes the following four regimes.

Represent normals by an angle \(\theta\in[0,\pi/6]\) from a vertex direction, and put \(x=\tan\theta/\sqrt3\). Define
\[
 r(x)=\sqrt{1+3x^2},\qquad
 \kappa(x)=\frac{2}{r(x)}\left(3x+\frac{2}{1+x}\right).
\]
For \(\sqrt3/2<W<1\), let \(x(W)\in(0,1/3)\) be the unique solution of
\[
 \kappa(x(W))=W+\frac3W.
\]
Then the maximizing normal has parameter
\[
 x_*(W)=\begin{cases}
 1/3,&0<W\leq\sqrt3/2,\\
 x(W),&\sqrt3/2<W<1,\\
 0,&1\leq W\leq3/2,\\
 \sqrt{4W^2-9}/(3\sqrt3),&3/2<W<\sqrt3.
 \end{cases}
\]
In particular the direction moves from an edge normal to an oblique normal, to a vertex normal, stays there, and finally becomes oblique again; the sharp transition widths are \(\sqrt3/2\), \(1\), and \(3/2\).

The complete sharp maximal covered-area profile is
\[
 M(W)=\begin{cases}
 2W-\dfrac{W^2}{2\sqrt3},&0<W\leq\sqrt3/2,\\[3pt]
 \dfrac{3\sqrt3}{2}-\dfrac{\sqrt3}{2}\,G\!\left(x(W),\dfrac{W r(x(W))}{2}\right),&\sqrt3/2<W<1,\\[3pt]
 \dfrac{\sqrt3}{2}\bigl(3-(2-W)^2\bigr),&1\leq W\leq3/2,\\[3pt]
 \sqrt3\left(1+\dfrac{W^2}{6}\right),&3/2<W<\sqrt3,
 \end{cases}
\]
where
\[
 G(x,p)=\frac{4p^2-12p(1+x)+9x^2+12x+7}{2(1+3x)}.
\]
For \(W\geq\sqrt3\), covering all of \(H\) is possible and the optimum is its full area \(A\).

## Assumptions and scope
A plank is the (open or closed, immaterial for area) region between parallel Euclidean lines; its width is their ordinary distance. Width budgets add over finitely many planks, irrespective of their overlaps. Angles are Euclidean, and the direction of the normal is unoriented. The hexagon has side length and circumradius one. The angular maximizer assertion concerns single centered planks, not uniqueness of the family of all possible multi-plank maximizers. The theorem for finite plank families uses the planar single-plank reduction of Bakaev and Polyanskii (Theorem 12, 2026); the new calculation identifies the exact remaining optimal direction and its coverage value.

## Proof
**1. Reduction to centered strips.** Bakaev--Polyanskii, Theorem 12 of arXiv:2607.27483, proves that whenever \(0<W<w(K)\) for a planar convex body \(K\), no finite plank family of total width at most \(W\) covers more area than some single plank of width \(W\). For our centrally symmetric \(H\), at every fixed normal \(u\), the one-dimensional section-length profile \(\ell_u(t)=\operatorname{length}(H\cap\{y:\langle u,y\rangle=t\})\) is even and concave on its support by Brunn's section theorem. Thus it is nonincreasing for \(t\geq0\). Among intervals of a fixed length \(W\), the integral of \(\ell_u\) is maximal on the centered interval. Therefore it remains only to optimize centered planks over \(\theta\in[0,\pi/6]\), a fundamental dihedral sector.

**2. Exact complementary cap areas.** For \(0\leq x\leq1/3\) let
\[
 r=\sqrt{1+3x^2},\quad p=\frac{Wr}{2},\quad b=\frac{1+3x}{2},\quad c=\frac{1-3x}{2}.
\]
The three nonnegative projections of the hexagon's vertices on the normal, after multiplication by \(r\), are \(1,b,c\); their negatives give the other three vertices. Triangulating \(H\) into six triangles with a common central vertex, intersecting each triangle with the half-plane whose normalized threshold is \(p\), and adding the resulting similar-triangle areas gives that **each** of the two complementary caps has area \((\sqrt3/4)F(x,p)\), where
\[
 F(x,p)=\begin{cases}
 3-4p,&0\leq p\leq c,\\[2pt]
 \dfrac{4p^2-12p(1+x)+9x^2+12x+7}{2(1+3x)},&c\leq p\leq b,\\[3pt]
 \dfrac{4(1-p)^2}{1-9x^2},&b\leq p\leq1.
 \end{cases}
\]
The last case is understood for \(x<1/3\); at \(x=1/3\), the middle expression gives the continuous value. An equivalent direct finite-triangle certificate, for \(0\leq x<1/3\), is
\[
 F(x,p)=\frac{4(1-p)_+^2}{1-9x^2}
 -\frac{2(b-p)_+^2}{1-3x}
 -\frac{2(c-p)_+^2}{1+3x},\qquad z_+=\max\{z,0\}.
\]
This identity follows by the triangle-slice quadratic interpolation formula applied to the six center--edge triangles (or by splitting each clipped triangle into two similar triangles). Expanding the three active-set cases gives the displayed pieces; the expressions agree at both switching thresholds. Consequently a central plank covers
\[
 A_\mathrm{strip}(W,x)=\frac{3\sqrt3}{2}-\frac{\sqrt3}{2}F\left(x,\frac{Wr(x)}2\right).
\]
Maximizing this quantity is equivalent to minimizing \(F\) over \(0\leq x\leq1/3\).

**3. Directional derivatives and phase diagram.** Write \(F_1,F_2,F_3\) for the last, middle, and first cap formulas, respectively, after substituting \(p=Wr/2\). Direct differentiation gives, for \(0<x<1/3\),
\[
 \frac{\partial F_3}{\partial x}=-\frac{6Wx}{r}<0,
\]
\[
 \frac{\partial F_2}{\partial x}
 =\frac{3(1-3x)(1+x)}{2(1+3x)^2}
 \left[W\kappa(x)-(W^2+3)\right],
\]
and
\[
 \frac{\partial F_1}{\partial x}
 =\frac{12x(2W-3r)(Wr-2)}{(1-9x^2)^2r}.
\]
Since \(Wr<2\) for \(W<\sqrt3\), the sign of the last derivative is that of \(3r-2W\). Furthermore
\[
 \kappa'(x)=\frac{2(1-3x)(1+3x)}{(1+x)^2(1+3x^2)^{3/2}}>0,
 \qquad \kappa(0)=4,\quad\kappa(1/3)=\frac{5\sqrt3}{2}.
\]
The derivative formulas agree across the active-set boundaries, because they represent area of the same clipped polygon.

For \(W\leq\sqrt3/2\), \(W+3/W\geq5\sqrt3/2\); the applicable first and middle derivatives are nonpositive, so the unique minimum is \(x=1/3\). For \(\sqrt3/2<W<1\), the number \(W+3/W\) lies strictly between \(4\) and \(5\sqrt3/2\), and monotonicity of \(\kappa\) gives one minimum at its unique crossing. The first-cap derivative remains negative before its active-set transition, so the crossing occurs in the middle regime. For \(1\leq W\leq3/2\), both applicable middle- and last-cap derivatives are nonnegative, with their joint minimum only at \(x=0\). For \(3/2<W<\sqrt3\), the middle derivative remains positive and the last-cap derivative changes from negative to positive at the unique solution \(r=2W/3\), namely \(x=\sqrt{4W^2-9}/(3\sqrt3)\). This critical point is in the last-cap regime because at this value \(Wr-(1+3x)=(1-3x)^2/2>0\).

All boundaries have the stipulated unique normal parameter, with strict inequalities in the interior of the sectors. Substitution of \(x=1/3\), \(x=0\), the middle crossing, and \(r=2W/3\) into the exact area formula gives, respectively, the four displayed expressions for \(M(W)\). The formulas agree at the three transition widths and approach \(A\) as \(W\uparrow\sqrt3\). This completes the proof.

## Verification
The reproducible Python 3 checker `check_hex_planks.py` uses direct Sutherland--Hodgman clipping of the six-vertex polygon, followed by independent shoelace area evaluation. It checks 2,400 seeded random angle/width pairs against the exact three-branch area law, 32,400 candidate-orientation comparisons over 400 widths against the analytically predicted maximum, and 1,500 translated strips against centered strips. It also checks numerical continuity at the phase boundaries. Actual execution produced `HEX_PLANK_PROFILE_OK fan_clips=2400 orientation_grid=32400 translated=1500`.

Exact symbolic differentiation checks verify the three derivative identities, the formula for \(\kappa'(x)\), and agreement of the cap formulas on both switching lines. The analytical inequalities above, not the finite tests, establish the continuum result.

## Relationship to prior work
Bakaev and Polyanskii, *Optimal partial plank coverings* (arXiv:2607.27483, first public July 29, 2026), Theorem 12, already prove the planar single-plank existence principle that is used here. That theorem does not supply an optimal direction or a coverage formula for the regular hexagon. Bezdek's *Tarski's plank problem revisited* (arXiv:0903.4637; published 2013) discusses partial-plank optimization and supplies historical motivation, but its examined partial-plank section does not calculate this profile. The claimed new content is solely the sharp hexagonal four-regime maximization, the two nontrivial oblique direction ranges, and the three exact transition widths.

## Limitations
The optimizing-normal uniqueness is modulo dihedral symmetries for a **single centered plank**; it is not a classification of every optimal family of multiple planks. The result is Euclidean and specific to the regular six-gon. No higher-dimensional or arbitrary centrally symmetric hexagon extension is asserted. Full historical uniqueness against unindexed older strip-distribution calculations has not been independently certified. Numerical checks do not constitute an exhaustive proof.

## References
- E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483 (2026), Section 4, Theorem 12. https://arxiv.org/abs/2607.27483
- K. Bezdek, *Tarski's plank problem revisited*, arXiv:0903.4637 (2009); subsequently in *Geometry—Intuitive, Discrete, and Convex* (2013), Section 5. https://arxiv.org/abs/0903.4637
