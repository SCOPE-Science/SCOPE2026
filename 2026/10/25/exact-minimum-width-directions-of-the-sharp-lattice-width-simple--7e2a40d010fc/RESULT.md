# Exact minimum-width directions of the sharp lattice-width simplex

## Finding

Let
\[
\Delta=\operatorname{conv}\left\{(0,0,0),\left(1,\tfrac12,\tfrac12\right),\left(\tfrac12,1,\tfrac12\right),\left(\tfrac12,\tfrac12,1\right)\right\}\subset\mathbb R^3.
\]
For an integer vector \(u=(a,b,c)\in\mathbb Z^3\setminus\{0\}\), define its lattice width by
\[
w_\Delta(u)=\max_{x\in\Delta}\langle u,x\rangle-\min_{x\in\Delta}\langle u,x\rangle.
\]
Define \(w(\Delta):=\min_{u\in\mathbb Z^3\setminus\{0\}}w_\Delta(u)\).
Then \(\min_{u\in\mathbb Z^3\setminus\{0\}}w_\Delta(u)=1\), and the complete set of oriented minimum-width lattice directions is
\[
\begin{aligned}
\mathcal W(\Delta)={}&\{\pm e_1,\pm e_2,\pm e_3\}\\
&\cup\{\text{the six permutations of }(1,-1,0)\}\\
&\cup\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{-1,1\}^3:\text{the coordinates are not all equal}\}.
\end{aligned}
\]
The three displayed families are disjoint and each has six elements. Thus \(|\mathcal W(\Delta)|=18\), or nine unoriented direction lines. Moreover, \(\operatorname{Vol}(\Delta)=1/12=(1/12)\,w(\Delta)^3\), so this is the exact direction-contact classification for the simplex attaining the sharp three-dimensional volume–lattice-width bound.

## Assumptions and scope

The lattice is the standard lattice \(\mathbb Z^3\), the width is computed against integer linear functionals, and vectors \(u\) and \(-u\) count as distinct oriented directions. The body is precisely the tetrahedron \(\Delta\) above; no classification of equality cases for other bodies is claimed.

## Proof

Write \(u=(a,b,c)\) and \(s=a+b+c\). The four vertex evaluations of \(u\) on \(\Delta\) are
\[
0,\quad \frac{s+a}{2},\quad\frac{s+b}{2},\quad\frac{s+c}{2}.
\]
Put \(x_1=s+a\), \(x_2=s+b\), and \(x_3=s+c\). Then \(x_i\in\mathbb Z\), \(x_1+x_2+x_3=4s\), and
\[
w_\Delta(u)=\frac12\left(\max\{0,x_1,x_2,x_3\}-\min\{0,x_1,x_2,x_3\}\right). \tag{1}
\]
Conversely, every integer triple \(x\) with \(x_1+x_2+x_3\equiv0\pmod4\) arises uniquely: set \(s=(x_1+x_2+x_3)/4\) and \((a,b,c)=(x_1-s,x_2-s,x_3-s)\). These are integers and their sum is \(s\). Thus this change of variables is a bijection between \(\mathbb Z^3\) and the congruence sublattice \(\{x\in\mathbb Z^3:\sum_i x_i\equiv0\pmod4\}\).

If the range in (1) were less than \(2\), then, because all values are integers and include zero, either every \(x_i\in\{0,1\}\) or every \(x_i\in\{-1,0\}\). In either case the sum is divisible by \(4\) and lies between \(-3\) and \(3\), so it must be zero. The sign restriction then forces \(x=(0,0,0)\), hence \(u=0\). Therefore every nonzero integer direction has width at least \(1\).

For equality in (1), the integer range must be exactly \(2\). There are three exhaustive cases.

1. If \(0\le x_i\le2\) and some \(x_i=2\), the sum is a positive multiple of \(4\) at most \(6\), hence is \(4\). The triples are precisely the permutations of \((2,2,0)\) and \((2,1,1)\). Mapping back gives the permutations of \((1,1,-1)\) and the coordinate vectors \(e_i\).
2. If \(-2\le x_i\le0\) and some \(x_i=-2\), the sum is \(-4\), and the triples are precisely the permutations of \((-2,-2,0)\) and \((-2,-1,-1)\). Mapping back gives the negatives of the directions in case 1.
3. If the values straddle zero without either endpoint being \(\pm2\), the range condition forces \(x_i\in\{-1,0,1\}\) with both signs present. The sum is a multiple of \(4\) in \([-3,3]\), so it is zero; the triples are exactly the permutations of \((-1,0,1)\). Mapping back leaves these triples unchanged.

The three cases produce respectively six sign-mixed cube diagonals, six opposite-sign coordinate pairs, and six coordinate directions. They are disjoint, and every listed vector has width one by (1), completing the classification.

Finally, the edge matrix with columns \((1,\tfrac12,\tfrac12)\), \((\tfrac12,1,\tfrac12)\), and \((\tfrac12,\tfrac12,1)\) has determinant \(1/2\). Hence \(\operatorname{Vol}(\Delta)=|\det|/6=1/12\). Since \(w(\Delta)=1\), the volume–lattice-width equality follows.

## Verification

The proof reduces the infinite minimum over integer directions to the exact integer range in (1), then classifies the range-two cases by three exhaustive sign patterns. The accompanying integer-only script enumerates the range-two congruence triples and checks that they map to exactly the 18 displayed vectors; it is a finite consistency check, not the proof that no smaller width occurs. The no-smaller-width argument above handles all integer vectors. The determinant and volume are exact rational calculations.

## Relationship to prior work

Aliev proved the sharp inequality \(\operatorname{Vol}(K)\ge\tfrac1{12}\,\omega(K)^3\) for convex bodies in \(\mathbb R^3\) and gave this \(\Delta\) as an equality example. The present claim adds the complete list of lattice directions attaining its minimum width. Draisma, McAllister, and Nill proved the general upper bound \(3^d-1\) for the number of oriented lattice-width directions, with equality only for a regular lattice cross-polytope; their theorem does not identify the directions of this particular tetrahedron. The value 18 is consistent with that general bound and is not implied by it.

## Limitations

This is a classification for one explicit equality simplex in the standard lattice. It does not characterize all equality bodies in the volume–lattice-width inequality, prove a stability theorem, or establish a general formula for minimum-width direction counts of arbitrary tetrahedra. An unindexed source could contain the same finite calculation; the literature search was targeted but not exhaustive.

## References

1. A. Aliev, “The exact bound for the reverse isodiametric problem in 3-space,” arXiv:2306.14576, first posted 2023-06-26. https://arxiv.org/abs/2306.14576
2. J. Draisma, T. B. McAllister, and B. Nill, “Lattice-width directions and Minkowski’s \(3^d\)-theorem,” *SIAM Journal on Discrete Mathematics* 26 (2012), 1104–1107. https://doi.org/10.1137/120877635 (preprint: https://arxiv.org/abs/0901.1375)
