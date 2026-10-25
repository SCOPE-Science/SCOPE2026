# Lorentzian Hessian of the area of convex cyclic polygons

## Finding

Let \(n\ge 3\), and let \(d=(d_1,\ldots,d_n)\) be the side-length vector of a nondegenerate convex cyclic polygon, away from the semicyclic locus. Write \(\mathcal A(d)\) for its Euclidean area as a function of the side lengths. In each centered or non-centered chamber, the Hessian \(H(d)=D^2\mathcal A(d)\) is nonsingular and has exactly one positive and \(n-1\) negative eigenvalues. More precisely, the Hessian is a diagonal matrix plus an explicit rank-one term.

Let \(R\) be the circumradius, \(q_i=\sqrt{4R^2-d_i^2}>0\), and \(\alpha_i=\arcsin(d_i/(2R))\). For a centered polygon set \(\sigma_i=1\) for all \(i\). For a non-centered polygon, let \(k\) be the unique longest side, set \(\sigma_k=-1\), and set \(\sigma_i=1\) for \(i\ne k\). Define

\[
S=\sum_{i=1}^n\frac{\sigma_i d_i}{q_i}.
\]

Then the exact formula is

\[
\boxed{\displaystyle H_{ij}(d)=\frac{2R^2\sigma_i\sigma_j}{q_iq_jS}-\delta_{ij}\frac{\sigma_i d_i}{2q_i},\qquad 1\le i,j\le n,}
\]

where \(\delta_{ij}\) is the Kronecker delta. The signature statement holds throughout both open chambers, not only near regular polygons.

## Assumptions and scope

The side lengths satisfy the strict polygon inequalities, so a convex cyclic polygon exists and is nondegenerate. The semicyclic locus, where one side is a diameter and some \(q_k=0\), is excluded. In the centered chamber the circumcenter is inside the polygon and \(\sum_i\alpha_i=\pi\). In the non-centered chamber the unique longest side has index \(k\), and \(\alpha_k=\sum_{i\ne k}\alpha_i<\pi/2\). No assertion is made about the Hessian on the semicyclic boundary or at degenerate side-length vectors.

## Proof

The signed central-angle closure relation is \(\sum_i\sigma_i\alpha_i=c\), where \(c=\pi\) in the centered chamber and \(c=0\) in the non-centered chamber. Since

\[
\frac{\partial\alpha_i}{\partial d_j}=\frac{\delta_{ij}}{q_i}-\frac{d_i}{Rq_i}\frac{\partial R}{\partial d_j},
\]

differentiating the closure relation gives

\[
\frac{\partial R}{\partial d_j}=\frac{R\sigma_j}{q_jS}.
\]

The signed fan-area formula is

\[
\mathcal A(d)=\frac14\sum_i\sigma_i d_iq_i.
\]

Differentiating it and substituting the radius derivative yields

\[
\frac{\partial\mathcal A}{\partial d_i}=\frac{\sigma_iq_i}{2}.
\]

Differentiating once more gives the displayed Hessian formula. In matrix form,

\[
H=D+\frac{2R^2}{S}vv^{\mathsf T},\qquad D_{ii}=-\frac{\sigma_i d_i}{2q_i},\quad v_i=\frac{\sigma_i}{q_i}.
\]

In the centered chamber, \(S=2R\sum_i\tan\alpha_i>0\); in the non-centered chamber, \(S=2R(\sum_{i\ne k}\tan\alpha_i-\tan\alpha_k)<0\), because \(\alpha_k=\sum_{i\ne k}\alpha_i<\pi/2\) and tangent is strictly superadditive on positive angles whose sum is below \(\pi/2\). Thus, in the centered chamber, \(D\) is negative definite and the rank-one update is positive semidefinite. In the non-centered chamber, \(D\) has one positive diagonal entry and all remaining entries negative, while the rank-one update is negative semidefinite. In either case \(H\) has at most one positive eigenvalue.

Homogeneity, \(\mathcal A(\lambda d)=\lambda^2\mathcal A(d)\), gives \(d^{\mathsf T}H(d)d=2\mathcal A(d)>0\). Hence at least one eigenvalue is positive.

It remains to exclude zero eigenvalues. Put \(T=\sum_i\sigma_i/(d_iq_i)\). The matrix determinant lemma gives

\[
\det H=\det D\left(1-\frac{4R^2T}{S}\right),\qquad 4R^2T-S=\sum_i\frac{\sigma_iq_i}{d_i}.
\]

For a centered polygon, the last sum is \(\sum_i\cot\alpha_i>0\), while \(S>0\), so \(1-4R^2T/S<0\). For a non-centered polygon it is \(\sum_{i\ne k}\cot\alpha_i-\cot\alpha_k>0\): every \(\alpha_i\) with \(i\ne k\) is smaller than \(\alpha_k\), and cotangent is strictly decreasing on \((0,\pi/2)\). Since \(S<0\), this implies \(1-4R^2T/S>0\). The determinant is therefore nonzero in either chamber. Combined with the positive direction and the upper bound of one on the positive index, this proves the signature \((1,n-1)\).

## Verification

The proof is analytic and covers every \(n\ge3\) in the stated open chambers. The formulas were also checked numerically as sanity tests for an equilateral triangle with sides \((1,1,1)\), a centered pentagon with sides \((1,1.1,1.2,1.1,1)\), and a non-centered pentagon with sides \((1,1,1,1,3.5)\); in each case the computed Hessian had one positive eigenvalue and all other eigenvalues negative. These finite checks are not used as proof. The semicyclic boundary remains outside the claim because the displayed coordinates contain \(q_k\) in denominators.

## Relationship to prior work

DeBlois studied area and circumradius derivatives for hyperbolic cyclic polygons and noted that recorded Euclidean analogues of those derivative results were not known to him at the time. The present statement is about the Euclidean Hessian in side-length coordinates and its global inertia, rather than hyperbolic area or the Hessian on a polygon-linkage configuration space. Maley, Robbins, and Roskies derived generalized Heron polynomials encoding squared area for cyclic polygons. Khimshiashvili studied the signed-area Hessian and Morse indices on moduli spaces of polygons with fixed side lengths; those are different variables from the side-length-space Hessian here. Dulio and Laeng later gave an area identity in terms of edge segments determined by incircles of a triangulation. These works are closely related and determine or constrain area values, but the inspected statements do not give the rank-one Hessian formula and its one-positive-eigenvalue classification. An implicit area formula may allow additional derivative consequences, so the claim is limited to this explicit structural classification.

## Limitations

The Hessian is not asserted to extend continuously or finitely to the semicyclic boundary. The result gives the inertia, not closed-form individual eigenvalues or a global optimization theorem on every constrained slice. The prior area formulas are a residual overlap risk because they encode the same area function implicitly. Independent review has not been performed.

## References

1. J. DeBlois, “The geometry of cyclic hyperbolic polygons,” arXiv:1101.4971 (first posted 2011-01-25); published in *Rocky Mountain Journal of Mathematics* 46 (2016), 801–862. https://arxiv.org/abs/1101.4971
2. F. M. Maley, D. P. Robbins, and J. Roskies, “On the Areas of Cyclic and Semicyclic Polygons,” arXiv:math/0407300 (first posted 2004-07-16); *Advances in Applied Mathematics* 34 (2005), 669–689. https://arxiv.org/abs/math/0407300
3. G. Khimshiashvili, “Cyclic Polygons as Critical Points,” *Proceedings of I. Vekua Institute of Applied Mathematics* 58 (2008). https://rmi.tsu.ge/geo/open_science/annex4_docs_geo/Khimsh6.pdf
4. P. Dulio and E. Laeng, “Generalization of Heron’s and Brahmagupta’s equalities to any cyclic polygon,” *Aequationes Mathematicae* 95 (2021), 941–952. https://doi.org/10.1007/s00010-020-00771-w
