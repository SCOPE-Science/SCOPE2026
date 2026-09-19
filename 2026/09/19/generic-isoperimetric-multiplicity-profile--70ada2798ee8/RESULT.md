# Residual-volume uniqueness and multiplicity continuity for generic isoperimetry

Let \(M^d\) be a closed connected smooth manifold, \(d\ge 2\), and let
\(\operatorname{Met}^\infty(M)\) carry the \(C^\infty\) topology. For a
smooth metric \(g\), write \(V_g=\operatorname{Vol}_g(M)\). For
\(s\in(0,1)\), let \(\mathcal I_g(s)\) denote the set of isoperimetric
regions of \(g\)-volume \(sV_g\), modulo equality almost everywhere.

Equip finite-perimeter sets with the normalized symmetric-difference
distance
\[
d_g(E,F)=\frac{\operatorname{Vol}_g(E\triangle F)}{V_g},
\]
and define the **isoperimetric multiplicity diameter**
\[
\Delta_g(s)=\operatorname{diam}_{d_g}\mathcal I_g(s).
\]

The recent theorem of Gongping Niu proves generic uniqueness at each fixed
non-half volume fraction, exactly two complementary minimizers at half
volume, simultaneous uniqueness at every rational non-half fraction for a
generic metric, and generic uniqueness in the full metric-volume pair
space. The compactness statement in the same paper applies without
regularity assumptions on the minimizing boundaries.

The following consequence gives a simultaneous statement for an
uncountable set of volume fractions and a topological description of the
remaining multiplicity.

## Theorem

For every closed connected \(M^d\), \(d\ge2\):

1. For every smooth metric \(g\), the function
   \[
   \Delta_g:(0,1)\to[0,1]
   \]
   is upper semicontinuous and satisfies
   \[
   \Delta_g(s)=\Delta_g(1-s),\qquad
   0\le \Delta_g(s)\le 2\min\{s,1-s\}.
   \]
   Its zero set is exactly the set of fractions for which the
   isoperimetric region is unique.

2. There is a generic subset
   \(\mathscr G\subset\operatorname{Met}^\infty(M)\) such that, for
   every \(g\in\mathscr G\), the uniqueness set
   \[
   U_g:=\{s\in(0,1):\#\mathcal I_g(s)=1\}
   \]
   is a dense \(G_\delta\) subset of \((0,1)\), contains every rational
   fraction other than \(1/2\), and is invariant under
   \(s\mapsto1-s\). At \(s=1/2\),
   \[
   \mathcal I_g(1/2)=\{E_*,E_*^c\}
   \]
   for some isoperimetric region \(E_*\), and
   \[
   \Delta_g(1/2)=1.
   \]

3. For every \(g\in\mathscr G\),
   \[
   U_g=\operatorname{Cont}(\Delta_g).
   \]
   Consequently the exceptional set
   \(B_g=(0,1)\setminus U_g\) is a symmetric meagre \(F_\sigma\) set,
   contains no rational number except \(1/2\), and contains \(1/2\).
   More quantitatively, for every \(\eta>0\),
   \[
   B_{g,\eta}:=\{s:\Delta_g(s)\ge\eta\}
   \]
   is closed and nowhere dense, and
   \[
   B_{g,\eta}\subset
   \left[\frac{\eta}{2},1-\frac{\eta}{2}\right].
   \]

4. If \(s\in U_g\) and \(E_s\) is the unique minimizer, then the whole
   minimizer set collapses to \(E_s\) as the volume approaches \(s\):
   \[
   \lim_{t\to s}\ \sup_{F\in\mathcal I_g(t)}d_g(F,E_s)=0.
   \]
   In addition, the convergence is strict in \(BV_g\): for every
   \(t_i\to s\) and every choice \(F_i\in\mathcal I_g(t_i)\),
   \[
   \chi_{F_i}\to\chi_{E_s}\quad\hbox{in }L^1(M,g),
   \qquad
   P_g(F_i)\to P_g(E_s).
   \]
   Hence \(s\mapsto E_s\) is a continuous map from \(U_g\) into the
   strict-\(BV_g\) space, and is a topological embedding onto its image.

5. At half volume the same collapse holds modulo complementation. If
   \[
   d_g^\pm(F,E_*):=
   \min\{d_g(F,E_*),d_g(F,E_*^c)\},
   \]
   then
   \[
   \lim_{t\to1/2}\ \sup_{F\in\mathcal I_g(t)}
   d_g^\pm(F,E_*)=0.
   \]
   Thus the compulsory two-valued half-volume fiber becomes a continuous
   singleton after identifying a region with its complement.

There is also a pair-space version. Define
\[
\Delta(g,s):=\Delta_g(s)
\quad\text{on}\quad
\operatorname{Met}^\infty(M)\times(0,1).
\]
Then \(\Delta\) is upper semicontinuous. Niu's generic uniqueness theorem
for metric-volume pairs implies that \(\Delta^{-1}(0)\) is dense
\(G_\delta\). Therefore
\[
\boxed{\ \Delta^{-1}(0)=\operatorname{Cont}(\Delta)\ },
\]
so uniqueness of the isoperimetric region is exactly continuity of this
natural multiplicity observable on the full parameter space.

## Proof

### 1. Compactness gives upper semicontinuity

Fix a sequence \((g_i,s_i)\to(g,s)\) in
\(\operatorname{Met}^\infty(M)\times(0,1)\). Put
\(m_i=s_iV_{g_i}\) and \(m=sV_g\). Smooth convergence of the metrics
implies \(m_i\to m\).

Because \(\mathcal I_{g_i}(s_i)\) is compact in \(L^1\), choose
\(E_i,F_i\in\mathcal I_{g_i}(s_i)\) such that
\[
d_{g_i}(E_i,F_i)=\Delta_{g_i}(s_i).
\]
Take a subsequence along which the left side converges to the limsup.
Niu's compactness proposition, first for \(E_i\) and then for \(F_i\),
gives a further subsequence and
\(E,F\in\mathcal I_g(s)\) such that
\[
E_i\to E,\qquad F_i\to F
\]
in \(L^1\), with strict \(BV_g\) convergence as well. Since
\(g_i\to g\) smoothly,
\[
d_{g_i}(E_i,F_i)\longrightarrow d_g(E,F).
\]
Therefore
\[
\limsup_i\Delta_{g_i}(s_i)
\le d_g(E,F)\le\Delta_g(s).
\]
This proves upper semicontinuity of \(\Delta(g,s)\), and hence of every
fiber \(\Delta_g\).

Complementation is an isometric bijection
\(\mathcal I_g(s)\to\mathcal I_g(1-s)\), which proves the symmetry.
For two sets of normalized volume \(s\),
\[
d_g(E,F)\le2s;
\]
applying the same estimate to their complements gives
\(d_g(E,F)\le2(1-s)\). This proves the stated bound.

Finally, a compact metric space has diameter zero exactly when it is a
singleton. Hence \(\Delta_g(s)=0\) is equivalent to uniqueness.

### 2. Residual uniqueness for one generic metric

For any nonnegative upper-semicontinuous function,
\[
\{\Delta_g=0\}
=
\bigcap_{k=1}^\infty
\{\Delta_g<1/k\},
\]
so \(U_g\) is \(G_\delta\) for every \(g\).

Niu's simultaneous rational-fraction corollary supplies a generic set of
metrics for which every rational \(s\ne1/2\) belongs to \(U_g\), while the
half-volume minimizers are exactly a complementary pair. Call this
generic set \(\mathscr G\). For every \(g\in\mathscr G\), \(U_g\)
contains a dense subset of \((0,1)\). Since it is already \(G_\delta\),
it is dense \(G_\delta\).

At half volume the two complementary minimizers have symmetric
difference equal to \(M\) modulo null sets, hence
\(\Delta_g(1/2)=1\).

### 3. The exceptional set and the continuity set

If \(s\in U_g\), then \(\Delta_g(s)=0\). Upper semicontinuity and
nonnegativity imply
\[
\Delta_g(t)\to0\qquad(t\to s),
\]
so \(\Delta_g\) is continuous at \(s\).

Conversely, if \(s\notin U_g\), then \(\Delta_g(s)>0\). Rational
non-half fractions are dense, so there is a sequence
\(q_i\to s\) with \(q_i\ne1/2\) rational. For \(g\in\mathscr G\),
\(\Delta_g(q_i)=0\), and therefore \(\Delta_g\) is discontinuous at
\(s\). This proves
\[
U_g=\operatorname{Cont}(\Delta_g).
\]

Upper semicontinuity also makes every superlevel set
\(B_{g,\eta}\) closed. Since it is disjoint from the dense set
\(U_g\), it has empty interior and is nowhere dense. Moreover,
\[
B_g=\bigcup_{k=1}^\infty B_{g,1/k},
\]
so \(B_g\) is meagre \(F_\sigma\). The rational and symmetry statements
follow from the construction of \(\mathscr G\), and
\(\Delta_g(s)\le2\min\{s,1-s\}\) gives the displayed localization of
\(B_{g,\eta}\).

### 4. Strict-BV continuity of the minimizer

Let \(s_i\to s\in U_g\) and choose arbitrary
\(F_i\in\mathcal I_g(s_i)\). Every subsequence has, by Niu's compactness
proposition, a further subsequence converging in \(L^1\) and strictly in
\(BV_g\) to an element of \(\mathcal I_g(s)\). That fiber is the
singleton \(\{E_s\}\). Hence every subsequential limit is \(E_s\), so
the full sequence converges to \(E_s\). The usual contradiction argument
makes this uniform over all choices of \(F_i\), giving the supremum
formula in part 4.

The volume functional is continuous under \(L^1\) convergence, so the
inverse map from the image \(E_s\) back to \(s\) is continuous. Thus the
unique-minimizer map is a topological embedding.

At half volume the identical compactness argument shows that every
cluster point is either \(E_*\) or \(E_*^c\). Passing to
\(d_g^\pm\) therefore gives the uniform modulo-complement collapse.

The same proof with \(g_i\to g\) establishes the pair-space upper
semicontinuity. The homeomorphism
\[
(g,s)\longmapsto(g,sV_g)
\]
identifies normalized fractions with Niu's metric-volume parameter space,
so his pair theorem makes \(\Delta^{-1}(0)\) dense \(G_\delta\). A
nonnegative upper-semicontinuous function is continuous at each zero;
at every positive value, density of the zero set supplies a sequence
witnessing discontinuity. This proves the pair-space identity between
uniqueness and continuity points.

## Significance

The new generic-uniqueness theorem is stated simultaneously only for
rational volume fractions, and explicitly does not claim one generic
metric works for every real fraction. The result above identifies an
intermediate but substantially larger simultaneous statement: one generic
metric works for a dense \(G_\delta\), hence comeagre and uncountable, set
of real volume fractions. It also identifies the exceptional fractions
as the discontinuity set of an upper-semicontinuous multiplicity profile,
with quantitative closed nowhere-dense superlevel strata.

The strict-\(BV\) collapse adds a canonical continuity statement: on the
comeagre uniqueness set, the isoperimetric minimizer is not merely unique
pointwise but varies continuously, while the half-volume obstruction is
exactly removed by quotienting by complementation. No smoothness of the
minimizing boundary is required.

## Limitations

This does **not** prove uniqueness for every real volume fraction of a
generic metric. The exceptional set may be an uncountable meagre
\(F_\sigma\) set. No Hausdorff-dimension or measure estimate for that
exceptional set is obtained, and no regularity of the boundaries beyond
what is available in the underlying isoperimetric theory is asserted.

The residual-volume conclusion is a structural consequence of Niu's
new generic-uniqueness and compactness theorems together with elementary
Baire/set-valued arguments; it is not a new perturbative uniqueness proof.
The strict-\(BV\) continuity statement is likewise compactness-driven.
The value lies in the simultaneous uncountable-volume theorem and the
resulting multiplicity/continuity structure.

## References

1. G. Niu, *Generic Uniqueness of Isoperimetric Regions in Arbitrary
   Dimension*, arXiv:2609.20790 (2026).
   https://arxiv.org/abs/2609.20790

2. G. Antonelli, M. Pozzetta, D. Semola, *Uniqueness on average of large
   isoperimetric sets in noncompact manifolds with nonnegative Ricci
   curvature*, Communications on Pure and Applied Mathematics 78 (2025),
   1656--1702. https://doi.org/10.1002/cpa.22252

3. F. Maggi, *Sets of Finite Perimeter and Geometric Variational
   Problems*, Cambridge University Press (2012).
   https://doi.org/10.1017/CBO9781139108133
