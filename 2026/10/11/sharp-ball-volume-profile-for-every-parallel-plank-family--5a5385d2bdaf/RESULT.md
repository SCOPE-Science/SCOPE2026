# Sharp ball-volume profile for every parallel plank family
## Finding
Let \(B^d\subset\mathbb R^d\) be the Euclidean unit ball with \(d\ge2\). Let \(\{P_i\}\) be a finite or countable family of pairwise parallel planks whose widths \(w_i\) satisfy
\[
W=\sum_iw_i<2.
\tag{1}
\]
Then
\[
\boxed{
\operatorname{vol}_d\!\left(B^d\cap\bigcup_iP_i\right)
\le
\kappa_{d-1}\int_{-W/2}^{W/2}(1-t^2)^{(d-1)/2}\,dt
}
\tag{2}
\]
and equivalently
\[
\boxed{
\frac{\operatorname{vol}_d\!\left(B^d\cap\bigcup_iP_i\right)}{\kappa_d}
\le
I_{W^2/4}\!\left(\frac12,\frac{d+1}{2}\right)
}.
\tag{3}
\]
Here \(\kappa_j\) denotes the volume of the Euclidean unit \(j\)-ball and \(I_x(p,q)\) is the regularized incomplete beta function.

A single plank of width \(W\) concentric with the ball attains equality. More generally, equality occurs exactly when the family uses all of its available width inside the ball and its union there is, up to a null set, the same centered plank.

There is a sharp stability refinement. Suppose the one-dimensional normal-coordinate union \(E\subset[-1,1]\) has
\[
|E|=W.
\]
Put
\[
E_*=[-a,a],
\qquad
a=\frac W2,
\qquad
\delta=\frac12|E\triangle E_*|.
\tag{4}
\]
Then
\[
0\le\delta\le\min\{W,2-W\},
\]
and the loss from the optimum satisfies
\[
\boxed{
D(E)
\ge
2\kappa_{d-1}
\left[
\int_{a-\delta/2}^{a}(1-t^2)^{(d-1)/2}\,dt
-
\int_a^{a+\delta/2}(1-t^2)^{(d-1)/2}\,dt
\right]
}.
\tag{5}
\]
For every admissible \(\delta\), equality in (5) is attainable.

Thus the complete parallel-direction subclass of the plank-volume question has an exact all-dimensional solution, equality classification, and optimal placement-deficit profile.

## Assumptions and scope
A plank is the closed region between two parallel hyperplanes, and its width is the Euclidean distance between those hyperplanes. Pairwise parallel means that all planks have one common unit normal, up to sign.

The family may be finite or countable. The sum in (1) is assumed finite. The restriction \(W<2\) is the natural regime of the source problem and keeps the optimal centered slab strictly narrower than the unit ball's diameter.

After a rotation, write each plank as
\[
P_i=\{x\in\mathbb R^d:\alpha_i\le x_1\le\beta_i\},
\qquad
w_i=\beta_i-\alpha_i.
\]
Only the set
\[
E=\left(\bigcup_i[\alpha_i,\beta_i]\right)\cap[-1,1]
\tag{6}
\]
matters for coverage inside the ball. By countable subadditivity,
\[
|E|\le W.
\tag{7}
\]

The theorem does not address families whose plank normals are different. In particular, it is a sharp aligned-direction theorem inside the broader open problem posed by Bezdek, Deza, and Ye.

## Proof
At height \(x_1=t\), the section of the unit ball is a \((d-1)\)-ball of radius \(\sqrt{1-t^2}\). Its \((d-1)\)-volume is therefore
\[
\kappa_{d-1}(1-t^2)^{(d-1)/2}
\]
for \(|t|\le1\). Fubini's theorem gives
\[
\operatorname{vol}_d\!\left(B^d\cap\bigcup_iP_i\right)
=
\kappa_{d-1}\int_E f_d(t)\,dt,
\tag{8}
\]
where
\[
f_d(t)=(1-t^2)^{(d-1)/2}.
\]
For \(d\ge2\), the function \(f_d\) is even and strictly decreases as \(|t|\) increases on \([0,1]\).

Among measurable subsets of \([-1,1]\) of prescribed measure \(s\), the integral of this even strictly radially decreasing function is maximized uniquely up to null sets by the centered interval \([-s/2,s/2]\). This is the one-dimensional symmetric-decreasing rearrangement principle. Using (7), then monotonicity in \(s\),
\[
\int_E f_d(t)\,dt
\le
\int_{-|E|/2}^{|E|/2}f_d(t)\,dt
\le
\int_{-W/2}^{W/2}f_d(t)\,dt.
\]
Together with (8), this proves (2).

Put \(a=W/2\). The substitution \(s=t^2\) gives
\[
\int_{-a}^{a}(1-t^2)^{(d-1)/2}\,dt
=
B_{a^2}\!\left(\frac12,\frac{d+1}{2}\right).
\]
Since slicing the whole unit ball gives
\[
\kappa_d
=
\kappa_{d-1}B\!\left(\frac12,\frac{d+1}{2}\right),
\]
formula (3) follows.

The two inequalities used above are both strict unless their equality conditions hold. Thus equality in (2) requires
\[
|E|=W
\]
and
\[
E=[-W/2,W/2]
\]
up to a null set. Conversely those conditions plainly give equality. A single centered plank realizes them, while a family may also realize equality by partitioning the centered interval without positive-length overlap.

For the stability statement assume \(|E|=W\) and use the notation (4). Let
\[
A=E_*\setminus E,
\qquad
C=E\setminus E_*.
\]
Then
\[
|A|=|C|=\delta.
\tag{9}
\]
The volume deficit divided by \(\kappa_{d-1}\) is
\[
\int_Af_d(t)\,dt-
\int_Cf_d(t)\,dt.
\tag{10}
\]
Among subsets of \(E_*\) of measure \(\delta\), the first integral in (10) is smallest when \(A\) consists of the two outermost boundary layers, each of thickness \(\delta/2\). Among subsets of \([-1,1]\setminus E_*\) of measure \(\delta\), the second integral is largest when \(C\) consists of the two immediately adjacent exterior layers, again each of thickness \(\delta/2\). Equation (5) follows.

The constraints in (4) imply
\[
\delta\le W
\]
and
\[
\delta\le2-W,
\]
so all four layers lie inside \([-1,1]\). Equality in (5) is realized, modulo endpoints, by
\[
E=
[-a-\delta/2,-a]
\cup
[-a+\delta/2,a-\delta/2]
\cup
[a,a+\delta/2].
\tag{11}
\]
These three intervals are themselves the normal-coordinate traces of three parallel planks, so the deficit bound is genuinely sharp within the plank class.

For reference, the first low-dimensional specializations of (2) are
\[
\operatorname{area}(B^2\cap\cup_iP_i)
\le
W\sqrt{1-\frac{W^2}{4}}
+2\arcsin\frac W2
\tag{12}
\]
and
\[
\operatorname{vol}_3(B^3\cap\cup_iP_i)
\le
\pi\left(W-\frac{W^3}{12}\right).
\tag{13}
\]

## Verification
The bundled `verify.py` independently checks the beta-normalization identity numerically in dimensions \(2\) through \(10\), the closed forms (12)--(13), the centered optimum against thousands of deterministic random interval unions, and the exact layer-swap equality construction for the stability bound.

The numerical tests are regression checks only. The all-dimensional theorem follows from the exact slice formula (8) and the one-dimensional rearrangement argument.

## Relationship to prior work
Bezdek, Deza, and Ye ask for the maximum volume of the part of the Euclidean unit ball covered by planks whose total width is less than the ball's diameter. Their stated expected extremizer is exactly the configuration appearing in (2): nonoverlapping planks whose union is one plank concentric with the ball. They also record that a stronger unrestricted statement is known in dimension three.

The theorem here proves that expected picture in every dimension under the natural aligned-direction restriction and additionally gives the exact incomplete-beta value, the full equality classification, and the sharp displacement-deficit law (5). The dimension-three inequality itself is therefore prior-covered by the stronger theorem cited in the source; the new content is the all-dimensional parallel-family theorem and its equality/stability profile.

Modern plank theorems principally control the total width required for complete coverage. They do not, in the sources inspected for this result, state the partial-volume formula (2) or the sharp stability profile (5). Targeted searches under parallel planks, slabs, ball coverage volume, centered-plank extremizers, rearrangement, and incomplete-beta formulations did not locate an implication-equivalent theorem.

## Limitations
The theorem does not settle the original plank-volume problem for differently oriented planks. Interactions between distinct directions are exactly the missing difficulty that disappears in the one-dimensional reduction (8).

The rearrangement step is classical. Consequently, an equivalent aligned-direction statement may exist as an unindexed observation in older plank or rearrangement literature. The originality claim is limited to the absence of a located implication-equivalent published statement after targeted searches and to the explicit equality/stability package given here.

The stability law (5) assumes no width is lost to positive-length overlap or to parts of planks outside the ball's normal-coordinate interval. It quantifies positional misalignment once the full available one-dimensional measure is used; it is not a stability theorem for arbitrary nonparallel plank families.

## References
1. K. Bezdek, A. Deza, and Y. Ye, *Selected Open Problems in Discrete Geometry and Optimization*, in *Discrete Geometry and Optimization*, Fields Institute Communications 69, Springer, 2013, 321--336. DOI: 10.1007/978-3-319-00200-2_18.
2. O. Ortega-Moreno, *The Complex Plank Problem, Revisited*, *Discrete & Computational Geometry* 71 (2024), 683--687. DOI: 10.1007/s00454-022-00423-7.
