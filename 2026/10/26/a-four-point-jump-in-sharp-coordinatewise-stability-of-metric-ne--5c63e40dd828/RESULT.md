# A four-point jump in sharp coordinatewise stability of metric nearness

## Finding

Let \(M_n\) be the cone of symmetric, zero-diagonal pseudometric arrays on \(n\) labelled points, identified with \(\mathbb R^{\binom n2}\) by listing the off-diagonal coordinates once. Write \(P_n\) for Euclidean nearest-point projection onto \(M_n\), and use the edgewise maximum norm on inputs and outputs. For \(n=3,4\), the exact global Lipschitz constants are

\[
\operatorname{Lip}_{\infty}(P_3)=\frac43,\qquad
\operatorname{Lip}_{\infty}(P_4)=\frac85.
\]

The same constants hold when the inputs are restricted to *strictly positive* symmetric dissimilarity arrays. In particular, the four-point constant is not an infinitesimal supremum: it is attained by two strictly positive finite input arrays. A maximizer occurs on a three-constraint face corresponding to one central point lying between each pair of the other three points.

## Assumptions and scope

There are no embedding, Euclidean-realizability, or strict-metric requirements on the output. Each off-diagonal entry is treated once, with the unweighted Euclidean least-squares objective

\[
P_n(y)=\arg\min_{x\in M_n}\frac12\sum_{i<j}(x_{ij}-y_{ij})^2.
\]

The cone consists exactly of \(x_{ij}\ge0\) satisfying \(x_{uv}\le x_{um}+x_{mv}\) for every distinct triple \((u,m,v)\); for \(n\ge3\), nonnegativity follows already from the triangle inequalities. The sensitivity norm is \(\|x\|_\infty=\max_{i<j}|x_{ij}|\), **not** the Euclidean norm used in fitting. All input pairs in the Lipschitz quotient are distinct.

For four points order the coordinates as

\[
(01,02,03,12,13,23).
\]

For each unordered triple \(\{a,b,c\}\), write the three inequalities in the order with middle vertex \(a\), \(b\), and \(c\). The resulting \(12\times6\) integer matrix \(A\) has row \(e_{um}+e_{mv}-e_{uv}\) for the chosen middle vertex \(m\). Thus \(M_4=\{x:Ax\ge0\}\).

## Proof

**Piecewise-orthogonal reduction.** For any subset \(S\) of the triangle inequalities, let \(B_S\) be a full-row-rank basis of the span of the selected normals and define

\[
Q_S=I-B_S^{\mathsf T}(B_SB_S^{\mathsf T})^{-1}B_S^{\vphantom{\mathsf T}}.
\]

For the empty basis put \(Q_S=I\). Whenever projection lands in the relative interior of a face with active normals \(S\) and strictly complementary multipliers, the KKT equations show that the projector is locally the linear map \(Q_S\). By the finite polyhedral cell decomposition of Euclidean projection, every line segment can be split into finitely many affine pieces (or approximated by generic segments and passed to the limit). Hence

\[
\operatorname{Lip}_\infty(P_n)
\le \max_{S\subseteq\mathcal T_n}\|Q_S\|_{\infty\to\infty},
\quad \|Q_S\|_{\infty\to\infty}=\max_i\sum_j|(Q_S)_{ij}|.
\]

The right-hand maximum may include spans not arising from feasible faces; this only strengthens its role as an upper bound. The formula is elementary linear algebra, with exact arithmetic.

**Exhaustive exact upper bound.** The attached standard-library checker constructs every triple normal and every one of the \(2^3=8\) and \(2^{12}=4096\) subsets of triangle inequalities for three and four points, respectively. It computes reduced row-echelon bases over rational numbers, then computes the projector and every row sum over rational numbers. Repeated spans are cached only after constructing their canonical bases, so none of the subsets is skipped. The complete rank-stratified output for the four-point case is:

| Rank of selected normals | Number of subsets | Distinct normal spans | Largest row sum |
|---:|---:|---:|---:|
| 0 | 1 | 1 | \(1\) |
| 1 | 12 | 12 | \(4/3\) |
| 2 | 66 | 66 | \(3/2\) |
| 3 | 238 | 166 | \(8/5\) |
| 4 | 639 | 171 | \(3/2\) |
| 5 | 1345 | 49 | \(10/7\) |
| 6 | 1795 | 1 | \(0\) |

Thus the upper bound is \(8/5\). The three-point rank maxima are \(1,4/3,1,0\), proving the upper bound \(4/3\). Each table entry is verified by explicit finite enumeration, not extrapolation from experiments. The checker asserts all computed values, symmetry, idempotence, and annihilation of each selected normal basis.

**Finite sharpness with positive inputs.** For four points choose the active normals for the three triangles through central vertex \(0\), namely \(S=\{0,3,6\}\) in the checker's ordering. Put

\[
x=(1/2,1/2,1/2,1,1,1),\qquad
v=(1,1,-1,1,1,1),\qquad h=1/1000.
\]

Let \(A_S\) denote the corresponding three normal rows. Since

\[
y=x-\tfrac1{10}A_S^{\mathsf T}(1,1,1)^{\mathsf T}
=(3/10,3/10,3/10,11/10,11/10,11/10),
\]

this is a strictly positive input with \(P_4(y)=x\): all triangle inequalities hold at \(x\), the three active ones vanish, and the KKT multipliers are positive. For the orthogonal projector \(Q_S\), direct calculation gives

\[
Q_Sv=(4/5,4/5,-1/5,8/5,3/5,3/5).
\]

The perturbed output \(z=x+hQ_Sv\) remains feasible, and

\[
y+hv-z=-A_S^{\mathsf T}
\bigl(497/5000,251/2500,251/2500\bigr)^{\mathsf T}.
\]

All three displayed multipliers are strictly positive, so KKT again gives \(P_4(y+hv)=z\). Both \(y\) and \(y+hv\) have strictly positive entries. Consequently,

\[
\frac{\|P_4(y+hv)-P_4(y)\|_\infty}{\|hv\|_\infty}
=\frac85.
\]

For three points, a strictly positive point on a single triangle facet and a strictly complementary normal displacement give local projection matrix \(I-aa^{\mathsf T}/3\), where \(a\) has three signs of unit magnitude; its absolute row sum is \(4/3\). A sufficiently small sign-aligned finite perturbation therefore attains that lower bound on strictly positive inputs as well. This completes both sharp equalities.

## Verification

Extract `verify_metric_nearness.py` from this package and run `python3 verify_metric_nearness.py` with Python 3. The checker uses only `fractions.Fraction` and other standard-library components; no floating-point computation, optimization oracle, or data file is needed. It enumerates **all** candidate normal subsets, verifies the rank table and three-point comparison, and proves the displayed finite attainment pair by exact primal feasibility and positive KKT multipliers. Run output ends in `ALL EXACT CHECKS PASSED`.

The code is part of the finite upper-bound proof, not a numerical test supporting an unproved infinite generalization.

## Relationship to prior work

The 2004 technical report by Dhillon, Sra, and Tropp and the expanded 2008 treatment with Brickell formulate Euclidean metric nearness and give triangle-fixing optimization algorithms. Their solution framework is the baseline, not a novelty claim here. Deza, Goldengorin, and Pasechnik describe the four-point metric cone's seven cut rays and isometry group; that structural information alone does not state the edgewise Lipschitz modulus of the nonlinear nearest-point map. The new assertion is the exact perturbation factor \(8/5\), the three-versus-four-point comparison, and an explicit positive-input equality pair.

The usual Euclidean nonexpansiveness of convex projection implies only a dimension-dependent bound after switching to the edgewise maximum norm; it does not yield the exact constants above. General results about the local piecewise-linearity of projections supply the reduction method, not the table's values.

## Limitations

The sharp classification is proved only for three and four points, with **unweighted squared Euclidean fitting error** and the coordinatewise error norm. No bound, formula, or monotonicity is asserted for five or more points or for heterogeneous observation weights. The global input domain is all real symmetric off-diagonal arrays, and the exact same constants are attained even with strictly positive inputs; the outputs are pseudometrics and may have zero off-diagonal entries. No claim of an independent review or exhaustive historical priority search is made. Equivalent earlier formulations of this small-dimensional value may exist.

## References

1. I. S. Dhillon, S. Sra, J. A. Tropp, *Triangle Fixing Algorithms for the Metric Nearness Problem*, Technical Report TR-04-22, University of Texas at Austin, dated 10 September 2004. https://www.cs.utexas.edu/ftp/techreports/tr04-22.pdf
2. J. Brickell, I. S. Dhillon, S. Sra, J. A. Tropp, *The Metric Nearness Problem*, SIAM Journal on Matrix Analysis and Applications **30** (2008), 375–396, DOI: 10.1137/060653391. Author-accessible full text: https://www.cs.utexas.edu/users/inderjit/public_papers/metric-simax.pdf
3. A. Deza, B. Goldengorin, D. V. Pasechnik, *The isometries of the cut, metric and hypermetric cones*, arXiv:math/0306049 (2003), especially section 3.1.2. https://arxiv.org/abs/math/0306049
