# Unlabeled projection-width laws determine every Euclidean triangle

## Finding

**Theorem.** Let \(T\subset\mathbb R^2\) be any nondegenerate Euclidean triangle. Independently choose an unoriented unit direction \(U\) uniformly on \(\mathbb RP^1\), and let \(W_T\) be the length of the orthogonal projection of \(T\) on the line directed by \(U\). The probability distribution of \(W_T\), without knowledge of which direction produced each observed length, uniquely determines the three side lengths of \(T\), including multiplicities. Consequently it determines \(T\) up to Euclidean congruence, for acute, right, and obtuse triangles alike.

Moreover, the law has the exact density below; its square-root singularities and its finite signed jumps give an explicit reconstruction.

## Assumptions and scope

Label the vertices \(A,B,C\), write \(a=|BC|\), \(b=|CA|\), \(c=|AB|\), and let \(\mathsf A,\mathsf B,\mathsf C\in(0,\pi)\) be the three interior angles (Roman letters distinguish angle labels from vertex names). Put \(\Delta=\operatorname{Area}(T)>0\) and define the positive altitudes \(h_a=2\Delta/a\), \(h_b=2\Delta/b\), \(h_c=2\Delta/c\). Let \(f_T\) denote the Lebesgue density of \(W_T\), interpreted at its finitely many boundary levels by one-sided limits.

For \(s>0\), \(0\le u<v\le s\), and \(t\ne u,v\), set
\[
\mathfrak g_s(t;u,v)=\frac{\mathbf1_{\{u<t<v\}}}{\sqrt{s^2-t^2}}.
\]
With angle labels permuted as necessary so that the right or obtuse angle, if any, is \(\mathsf A\), all cases have an exact density, for almost every \(t>0\):

**Acute** \((\mathsf A,\mathsf B,\mathsf C<\pi/2)\):
\[
\pi f_T(t)=\mathfrak g_a(t;h_b,a)+\mathfrak g_a(t;h_c,a)
+\mathfrak g_b(t;h_c,b)+\mathfrak g_b(t;h_a,b)
+\mathfrak g_c(t;h_a,c)+\mathfrak g_c(t;h_b,c).
\]

**Right** \((\mathsf A=\pi/2)\):
\[
\pi f_T(t)=\mathfrak g_a(t;h_b,a)+\mathfrak g_a(t;h_c,a)
+\mathfrak g_b(t;h_a,b)+\mathfrak g_c(t;h_a,c).
\]

**Obtuse** \((\mathsf A>\pi/2)\):
\[
\pi f_T(t)=\mathfrak g_a(t;h_b,a)+\mathfrak g_a(t;h_c,a)
+\mathfrak g_b(t;h_a,h_c)+\mathfrak g_c(t;h_a,h_b).
\]

All these expressions are probability densities, not merely asymptotic approximations. Their supports are contained in \([\min(h_a,h_b,h_c),\max(a,b,c)]\). In fact the support endpoints equal those two extrema.

## Proof

**1. Direction sectors.** For almost every projection direction, exactly two of the three vertices attain the greatest and least projected coordinates. The pair is one of the three edges. Fix the pair \(B,C\), and orient the direction so that \(C\) is the maximizer. Write \(\theta\) for the signed angle from \(\overrightarrow{BC}\) to this projection direction. Elementary scalar-product comparisons with the third vertex show that the active directions form the interval
\[
\mathsf B-\frac\pi2<\theta<\frac\pi2-\mathsf C.
\]
On this interval the width is \(a\cos\theta>0\). Its interval length is \(\mathsf A\), as follows from the angle sum \(\mathsf A+\mathsf B+\mathsf C=\pi\). The analogous intervals for the other two edges are disjoint apart from endpoints and together have total angular length \(\pi\); thus they partition unoriented directions almost everywhere. Each interval has angular probability measure \(d\theta/\pi\).

For completeness, an exact cumulative distribution formula follows directly. For an edge of length \(s\) with endpoint angles \(J,K\), set \(\alpha=J-\pi/2\), \(\beta=\pi/2-K\), and \(z=\arccos(t/s)\). Its contribution to \(F_T(t)=\Pr\{W_T\le t\}\), when \(0<t<s\), is
\[
\frac{\bigl[\min(\beta,-z)-\alpha\bigr]_+
+\bigl[\beta-\max(\alpha,z)\bigr]_+}{\pi},
\qquad [v]_+=\max(v,0).
\]
For \(t\le0\) its contribution is zero; for \(t\ge s\) it is \((\pi-J-K)/\pi\). Sum the three edge contributions with \((s,J,K)=(a,\mathsf B,\mathsf C),(b,\mathsf C,\mathsf A),(c,\mathsf A,\mathsf B)\).

**2. Exact densities.** The one-variable map \(\theta\mapsto s\cos\theta\) has Jacobian magnitude \(\sqrt{s^2-t^2}\) on each strictly monotone branch. If the sector crosses \(\theta=0\), there are two such branches, beginning respectively at the two endpoint widths, which equal the altitudes from the two vertices not opposite the edge. If \(\theta=0\) is a sector endpoint there is one branch. If the sector lies to one side of zero, there is one branch between its two endpoint widths. Applying this classification to all three edge sectors gives exactly the three displayed density formulas, including right-angle boundary cases. Since they are pushforwards of a partition of a probability space, their total integrals are one and there are no atoms.

**3. Singularities determine the angle class.** For each positive singular level \(s\) define its inverse-square-root weight
\[
\nu(s)=\lim_{t\uparrow s}\pi\sqrt{s^2-t^2}\,f_T(t),
\]
where the limit is taken through points not at density discontinuities. Let \(\mathcal S\) be the set of levels at which \(f_T\) is unbounded with this inverse-square-root behavior. Each term with index \(s\) contributes one unit to \(\nu(s)\), and terms with a different index cannot change that limit. In the acute case, \(\mathcal S\) is the set of distinct side lengths, each side contributing two units (thus \(\sum_{s\in\mathcal S}\nu(s)=6\)). In the right case it is again the set of distinct side lengths, but the hypotenuse contributes two units and each leg one unit (total four). In the obtuse case only the longest side, \(a\), gives such a singularity, and its weight is two (total two). Consequently the distribution itself distinguishes the three angle classes by the totals \(6,4,2\). For acute and right triangles, the side-length multiset is read directly from the singularity locations and weights; repeated side lengths are recovered through their accumulated weights.

**4. Obtuse reconstruction from finite jumps.** Suppose \(\mathsf A>\pi/2\). The side \(a\) is strictly the longest, so \(h_a<h_b,h_c\). The maximum support value and the unique singularity locate \(a\), while the minimum support value locates \(h_a\). At \(h_b\) the density has a finite negative jump of size
\[
\pi\bigl(f_T(h_b+)-f_T(h_b-)\bigr)
=\frac1{\sqrt{a^2-h_b^2}}-\frac1{\sqrt{c^2-h_b^2}}<0
\]
when \(h_b\ne h_c\), and analogously at \(h_c\), with \(b\) in place of \(c\). The inequality holds because \(a>c\) (and likewise \(a>b\)); denominators are positive for these nondegenerate triangles. If \(h_b=h_c\), the two negative jumps occur at the same level and add; no cancellation is possible. These are the only negative jumps away from the inverse-square-root singular level. Thus the set of their locations, counting the sole location twice when it occurs only once, recovers the multiset \(\{h_b,h_c\}\). Since \(2\Delta=a h_a=b h_b=c h_c\), the other side lengths follow as
\[
\{b,c\}=\left\{\frac{a h_a}{h_b},\frac{a h_a}{h_c}\right\}.
\]
This includes obtuse isosceles triangles. All three angle classes therefore have unique side-length reconstruction. The side-side-side congruence theorem finishes the proof.

## Verification

The independent geometric computation `verify.py` derives the density for each angle class and the sector cumulative distribution using different implementations, then compares the predicted CDF against direct uniform-angle projection of three vertices. The 24 tested nondegenerate triangles (acute, right, and obtuse, including isosceles cases) use 75 CDF thresholds each and 140,000 deterministic mid-angles per shape. Direct numerical density quadrature checks total mass one and the mean-width identity \(\mathbb EW_T=(a+b+c)/\pi\). Additional direct checks probe the singularity weights and the signed jumps. The script prints `VERIFY_OK` and `SINGULARITY_CHECKS_OK` on successful completion. These finite numerical checks do **not** establish the theorem for arbitrary triangles; the preceding angle-sector and singularity arguments do.

## Relationship to prior work

Kim, Yaskin and Zvavitch introduced and investigated the loss of directional labels in section and projection distributions, including nonuniqueness among general planar origin-symmetric convex bodies. Their arXiv manuscript of 22 December 2015, Sections 1 and 3, does not state the complete reconstruction for the restricted class of all triangles, nor the density classification by angle type. More generally, a direction-indexed width function determines a body's difference body, but removing directional labels can destroy injectivity among general convex bodies. The special three-edge structure here restores injectivity within triangles.

The comparison with published general projection results is limited to the claims inspected; it is not a proof that no equivalent earlier formulation exists.

## Limitations

The theorem applies to a nondegenerate Euclidean triangle with Haar-uniform unoriented projection directions and its **exact** distribution. It does not establish stability under measurement noise, finite-sample identifiability rates, or uniqueness for arbitrary polygons or smooth convex bodies. There is a genuine historical-overlap risk from older specialized width-distribution computations not identified in the checked literature. The argument establishes identifiability only for the mathematical ideal of an exact distribution.

## References

1. J. Kim, V. Yaskin, and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1 (first public version 22 December 2015), https://arxiv.org/abs/1512.07289 . See especially the introduction and Section 3.
2. Á. G. Horváth, *On Convex Bodies That Are Characterizable by Volume Function*, survey (2020), https://doi.org/10.1007/s40598-020-00132-0 . See the discussion of widths and difference bodies.
3. P. Goodey, R. Schneider, and W. Weil, *On the Determination of Convex Bodies by Projection Functions* (1997), https://doi.org/10.1112/S0024609396001968 . Direction-indexed projection information; only the accessible abstract was checked.
