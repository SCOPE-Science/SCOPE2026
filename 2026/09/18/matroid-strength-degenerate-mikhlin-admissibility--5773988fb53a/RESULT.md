# Matroid-strength characterization of degenerate Mikhlin admissibility

## Result

Let \(\Gamma'\subset\mathbb R^n\) be a \(k\)-dimensional singular subspace in the setting of Vandanjon, *Multilinear Mikhlin Multipliers with Degenerate Singularities* (arXiv:2609.18818). Remove the strongly degenerate coordinates and denote the remaining index set by \(E\).

Choose a basis of \(\Gamma'\), write its vectors as the columns of a matrix, and let \(v_e\in\mathbb R^k\) be the row indexed by \(e\in E\). Let \(M_{\Gamma'}\) be the rank-\(k\) linear matroid represented by the rows \(v_e\), with rank function \(r\).

Then Vandanjon's good \(k\)-directions are exactly the bases of \(M_{\Gamma'}\), and the set \(\Xi_{\Gamma'}\) appearing in Theorem 1.4 has the exact description
\[
\boxed{
\Xi_{\Gamma'}
=
B(M_{\Gamma'})\cap (0,\tfrac12)^E,
}
\]
where \(B(M)\) is the matroid base polytope. Equivalently,
\[
\boxed{
\Xi_{\Gamma'}
=
\left\{
\alpha\in(0,\tfrac12)^E:
\alpha(E)=k,\quad
\alpha(S)\le r(S)\ \text{for every }S\subseteq E
\right\}.
}
\]

This yields an exact all-dimensional criterion for nonemptiness. If \(\Phi(M)\) denotes matroid strength, in the normalization
\[
\Phi(M)
=
\min_{\substack{D\subseteq E\\ r(E\setminus D)<k}}
\frac{|D|}{k-r(E\setminus D)},
\]
then
\[
\boxed{
\Xi_{\Gamma'}\ne\varnothing
\quad\Longleftrightarrow\quad
\Phi(M_{\Gamma'})>2.
}
\]
Equivalently,
\[
\boxed{
|E\setminus S|>2\bigl(k-r(S)\bigr)
\quad\text{for every }S\subseteq E\text{ with }r(S)<k.
}
\]
Because the left side and rank defect are integral, this may be written
\[
|E\setminus S|\ge 2\bigl(k-r(S)\bigr)+1.
\]
It is enough to check proper flats.

There is also an exact elimination of the existential parameter \(\alpha\) from the exponent condition in Vandanjon's Theorem 1.4. For the non-strongly-degenerate coordinates put
\[
c_e(p)=\min\left\{\frac12,\ 1-\frac1{p_e}\right\}.
\]
Then an \(\alpha\in\Xi_{\Gamma'}\) satisfying
\[
\alpha_e<1-\frac1{p_e}\qquad(e\in E)
\]
exists if and only if \(p_e>1\) for every \(e\in E\) and
\[
\boxed{
\sum_{e\in E\setminus S} c_e(p)
>
 k-r(S)
\quad\text{for every }S\subseteq E\text{ with }r(S)<k.
}
\]
Again it suffices to check proper flats. Thus the geometric/exponent hypothesis of Theorem 1.4 can be tested entirely by rank inequalities of the linear matroid attached to \(\Gamma'\).

## Why the matroid is intrinsic

Let \(T:\mathbb R^k\to\Gamma'\) be the isomorphism determined by the chosen basis. The row \(v_e\) is the coordinate functional
\[
x\longmapsto (Tx)_e.
\]
For a \(k\)-subset \(I\subseteq E\), the coordinate projection \(\Gamma'\to\mathbb R^I\) is an isomorphism exactly when the rows \(\{v_e:e\in I\}\) are linearly independent. This is precisely Vandanjon's definition of a good direction. Changing the basis of \(\Gamma'\) right-multiplies the row matrix by an invertible matrix and leaves the represented matroid unchanged.

A coordinate is strongly degenerate exactly when its row is a loop. After deleting those coordinates, every remaining element is a nonloop and therefore belongs to at least one basis.

## Proof of the base-polytope formula

By definition, \(\alpha\in\Xi_{\Gamma'}\) precisely when there are coefficients \(\theta_B\ge0\), indexed by good directions, with
\[
\sum_B\theta_B=1,
\qquad
\alpha_e=\sum_{B\ni e}\theta_B,
\qquad
0<\alpha_e<\frac12.
\]
Since the good directions are the matroid bases, the vector \(\alpha\) is a convex combination of their incidence vectors. Hence the set of all such load vectors before imposing the open coordinate bounds is the matroid base polytope
\[
B(M)=\operatorname{conv}\{\mathbf 1_B:B\text{ a basis}\}.
\]
Edmonds' base-polytope theorem gives
\[
B(M)=\{x\ge0:x(E)=k,\ x(S)\le r(S)\text{ for all }S\subseteq E\},
\]
which proves the claimed description of \(\Xi_{\Gamma'}\).

## Proof of the strength criterion

Suppose first that \(\alpha\in\Xi_{\Gamma'}\), represented by a probability distribution \(\theta\) on bases. Let \(D\subseteq E\) satisfy \(r(E\setminus D)<k\), and put
\[
\delta=k-r(E\setminus D)>0.
\]
Every basis must contain at least \(\delta\) elements of \(D\). Averaging with respect to \(\theta\) gives
\[
\alpha(D)=\sum_B\theta_B|B\cap D|\ge\delta.
\]
But each \(\alpha_e<1/2\), so
\[
\delta\le\alpha(D)<\frac{|D|}{2},
\]
and therefore \(|D|/\delta>2\). Taking the minimum over \(D\) gives \(\Phi(M)>2\).

Conversely assume \(\Phi(M)>2\). The standard fractional base-packing theorem says that \(\Phi(M)\) is the largest reciprocal of the maximum element load attainable by a probability distribution on bases. Hence there is a distribution whose maximum marginal load is strictly below \(1/2\). If some nonloop element has zero marginal under this distribution, mix it by a sufficiently small amount with a full-support distribution on the finite set of bases. The strict upper slack is preserved and every marginal becomes positive. The resulting marginal vector belongs to \(\Xi_{\Gamma'}\).

Replacing \(D\) by \(E\setminus S\) gives the rank-defect formulation. Replacing \(S\) by its closure can only decrease \(|E\setminus S|\) while preserving rank, so it suffices to check proper flats.

There is an equivalent linear-algebra formulation. For every proper subspace \(W\subsetneq\mathbb R^k\), let \(\delta=\operatorname{codim}W\). Then
\[
\Xi_{\Gamma'}\ne\varnothing
\quad\Longleftrightarrow\quad
\#\{e\in E:v_e\notin W\}>2\delta
\quad\text{for every proper }W.
\]
It is enough to take \(W\) spanned by subsets of the rows.

## Exact exponent feasibility

We use a standard box-intersection form of Edmonds' matroid-polytope theorem. For capacities \(c_e>0\), there exists a point \(x\in B(M)\) with
\[
0<x_e<c_e\qquad(e\in E)
\]
if and only if
\[
\boxed{
c(E\setminus S)>k-r(S)
\quad\text{whenever }r(S)<k.
}
\]

Necessity is immediate: for \(x\in B(M)\),
\[
x(E\setminus S)=k-x(S)\ge k-r(S),
\]
while \(x(E\setminus S)<c(E\setminus S)\).

For sufficiency, the finitely many strict inequalities permit a common shrink factor \(0<\lambda<1\) such that
\[
\lambda c(E\setminus S)\ge k-r(S)
\]
for every \(S\). Edmonds' box-intersection formula for the matroid independence polytope then yields a vector \(y\le\lambda c\) with \(y(E)=k\); hence \(y\in B(M)\). The inequality \(y_e<c_e\) has uniform positive slack. Since every element of \(E\) is a nonloop, mixing \(y\) by a sufficiently small amount with the barycenter of all bases makes every coordinate positive without losing the strict upper bounds.

Applying this criterion with
\[
c_e=\min\left\{\frac12,1-\frac1{p_e}\right\}
\]
gives the stated exponent characterization.

## Consequences for examples in arXiv:2609.18818

### The \(k=3,n=7\) example

Vandanjon exhibits seven good directions in which every index occurs exactly three times and assigns equal weight \(1/7\). In matroid language this is a base distribution with constant load \(3/7\), so
\[
\Phi(M)\ge\frac{7}{3}>2.
\]
The nonemptiness of \(\Xi_{\Gamma'}\) is therefore an instance of the strength criterion.

### The empty example of Section 6

In Example 6.19, the first block has rank one and the complementary two blocks contain \(2(k-1)\) rows. Taking \(S\) to be the first block gives
\[
|E\setminus S|=2(k-1),
\qquad
k-r(S)=k-1.
\]
Thus the strength ratio is at most \(2\), and the criterion immediately forces
\[
\Xi_{\Gamma'}=\varnothing.
\]
This recovers the obstruction from a single rank-defect certificate.

### Rank two

For \(k=2\), proper rank-one flats are exactly the parallel classes of nonzero rows. If \(m=|E|\), the criterion becomes
\[
m>4
\quad\text{and}\quad
|P|\le m-3\ \text{for every parallel class }P.
\]
This gives a compact structural formulation of the complete rank-two case, including the exceptional \(m=6\) configurations that require separate case analysis when only the number of good pairs is recorded.

## Relation to Vandanjon's theorem

Vandanjon's Theorem 1.4 proves multilinear multiplier bounds once the stated analytic hypotheses hold and an admissible \(\alpha\in\Xi_{\Gamma'}\) exists. The paper gives a counting sufficient condition, a balanced-design sufficient condition for higher rank, a family with empty \(\Xi_{\Gamma'}\), and a complete rank-two analysis. It explicitly notes that its counting condition is not optimal for \(k\ge3\).

The result here identifies the exact finite-dimensional structure behind those cases: the good directions are bases of a representable matroid, \(\Xi_{\Gamma'}\) is a clipped matroid base polytope, and its nonemptiness threshold is precisely matroid strength \(>2\). The same identification removes the existential \(\alpha\) from the exponent condition through rank inequalities.

This does not assert that the multiplier itself is unbounded when \(\Phi(M)\le2\). It says exactly when the \(\Xi_{\Gamma'}\)-based hypothesis of Theorem 1.4 is available.

## Limitations

- The result characterizes the geometric/polyhedral hypothesis in Vandanjon's Theorem 1.4; it does not replace the analytic proof of that theorem.
- Failure of the rank inequalities means that this particular admissibility mechanism fails, not that the corresponding multiplier is necessarily unbounded.
- It does not address the difficult regime in which the singularity dimension is too large for the underlying time-frequency theorem.
- Edmonds' matroid base-polytope and box-intersection theorems, and the classical matroid-strength/base-packing theorem, are prior results and are not claimed as new.
- Originality is asserted only to the best of our knowledge. The source multiplier preprint is extremely recent, so contemporaneous observations not yet indexed remain a residual risk.

## References

1. H. Vandanjon, *Multilinear Mikhlin Multipliers with Degenerate Singularities*, arXiv:2609.18818 (2026). https://arxiv.org/abs/2609.18818
2. T. de Vos and M. Grilnberger, *Dynamic Matroids: Base Packing and Covering*, ESA 2026, LIPIcs 388, Article 57. https://doi.org/10.4230/LIPIcs.ESA.2026.57
3. J. Edmonds, *Submodular functions, matroids, and certain polyhedra*, in Combinatorial Structures and Their Applications (1970).
4. J. Edmonds' box-intersection theorem is restated as Theorem 2.2 in: E. Husić, Z. K. Koh, G. Loho, and L. A. Végh, *On the correlation gap of matroids*, Mathematical Programming 210 (2025), 407–456 (published online 2024). https://doi.org/10.1007/s10107-024-02116-w
