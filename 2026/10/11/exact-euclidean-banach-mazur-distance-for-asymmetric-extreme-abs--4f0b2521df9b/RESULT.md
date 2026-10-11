# Exact Euclidean Banach–Mazur distance for asymmetric extreme absolute normalized planes
## Finding
For real parameters \(0<a,c<1\) with \(a\ne c\), let \(X_{a,c}=(\mathbb R^2,N_{a,c})\), where
\[
N_{a,c}(x,y)=\max\left\{|x|,|y|,\frac{1-a}{1-ac}|x|+\frac{1-c}{1-ac}|y|\right\}.
\]
These are exactly the interior asymmetric extreme absolute normalized norms after the reparameterization \(\alpha=a/(1+a)\), \(\beta=1/(1+c)\). Put \(s=a+c+ac\). Then the exact Euclidean Banach–Mazur distance satisfies
\[
d_{\mathrm{BM}}(X_{a,c},\ell_2^2)^2=
\begin{cases}
1+\max\{a^2,c^2\},&s\ge1,\\[3pt]
\dfrac{2(1+ac)}{(1+a)(1+c)},&s<1,\ a(c+2)\le1,\ c(a+2)\le1,\\[7pt]
\dfrac{2(1-ac)}{2-c-ac},&s<1,\ c(a+2)\ge1,\\[7pt]
\dfrac{2(1-ac)}{2-a-ac},&s<1,\ a(c+2)\ge1.
\end{cases}
\]
In the last three cases the overlapping equality boundaries agree, and under \(s<1\) the two one-sided conditions cannot both be strict. Optimal Euclidean pullback forms, up to an overall positive factor, are respectively \(x^2+y^2\); \(u_*x^2+v_*y^2\) with \(u_*=2(1-a)/((1+c)(1-ac))\), \(v_*=2(1-c)/((1+a)(1-ac))\); \(u_cx^2+y^2\) with \(u_c=(1-a)/(c(2-c-ac))\); and \(x^2+v_ay^2\) with \(v_a=(1-c)/(a(2-a-ac))\).

## Assumptions and scope
The scalar field is real. Parameters satisfy \(0<a,c<1\) and \(a\ne c\). Define
\[
A=\frac{1-a}{1-ac},\qquad B=\frac{1-c}{1-ac},
\]
so that
\[
N_{a,c}(x,y)=\max\{|x|,|y|,A|x|+B|y|\}.
\]
The first-quadrant vertices of the unit ball are \((1,0)\), \((1,a)\), \((c,1)\), and \((0,1)\). Under
\[
\alpha=\frac{a}{1+a},\qquad \beta=\frac{1}{1+c},
\]
we have \(0<\alpha<1/2<\beta<1\), and this is the norm \(\|\cdot\|_{\psi_{\alpha,\beta}}\) in the extreme-point classification of absolute normalized norms. The condition \(a\ne c\) is equivalent to \(\alpha+\beta\ne1\), so the theorem concerns the interior asymmetric part of that natural two-parameter extreme family.

## Proof
For a positive-definite quadratic form \(q(x)=x^TQx\), a distortion bound \(d\) after scaling is equivalent to
\[
N_{a,c}(x)^2\le q(x)\le d^2N_{a,c}(x)^2\qquad(x\in\mathbb R^2).
\]
Because \(N_{a,c}\) is invariant under both coordinate sign changes, conjugating \(Q\) by each sign matrix preserves these inequalities. Averaging the four conjugates cancels the off-diagonal term and preserves the same inequalities pointwise. Hence an optimal quadratic form may be taken diagonal:
\[
q_{u,v}(x,y)=ux^2+vy^2,
\qquad u,v>0.
\]

The lower comparison \(N_{a,c}^2\le q_{u,v}\) is equivalent to the three conditions
\[
u\ge1,\qquad v\ge1,\qquad \frac{A^2}{u}+\frac{B^2}{v}\le1.
\]
Indeed, the first two come from the coordinate functionals. For the third, weighted Cauchy--Schwarz gives
\[
(A|x|+B|y|)^2\le\left(\frac{A^2}{u}+\frac{B^2}{v}\right)(ux^2+vy^2),
\]
and the coefficient is also necessary by equality in Cauchy--Schwarz.

For such \((u,v)\), the sharp upper factor is the maximum of \(q_{u,v}\) on the unit ball. A convex quadratic function on a compact polygon attains its maximum at a vertex, and the two non-axis vertices dominate the axis vertices. Therefore
\[
d^2(u,v)=\max\{u+a^2v,\ c^2u+v\}.
\]
Consequently
\[
d_{\mathrm{BM}}(X_{a,c},\ell_2^2)^2
=\min_{u,v\ge1\atop A^2/u+B^2/v\le1}
\max\{u+a^2v,\ c^2u+v\}.
\]

First suppose
\[
A^2+B^2\le1.
\]
A direct factorization gives
\[
1-A^2-B^2=
\frac{(a-1)(c-1)(a+c+ac-1)}{(1-ac)^2},
\]
so this is equivalent to \(a+c+ac\ge1\). Then \((u,v)=(1,1)\) is feasible. Every feasible pair has \(u,v\ge1\), whence
\[
d^2(u,v)\ge\max\{1+a^2,1+c^2\}=1+\max\{a^2,c^2\},
\]
and equality holds at \((1,1)\).

Now assume \(a+c+ac<1\), so \((1,1)\) is not feasible. Since the objective is increasing in each coordinate, the curved constraint is active at an optimum. Write it as
\[
v(u)=\frac{B^2u}{u-A^2},\qquad u>A^2.
\]
Set
\[
L_1(u)=u+a^2v(u),\qquad L_2(u)=c^2u+v(u).
\]
The difference
\[
L_1(u)-L_2(u)=(1-c^2)u-(1-a^2)v(u)
\]
is strictly increasing because \(v'(u)<0\). Its unique zero is
\[
u_*=\frac{2(1-a)}{(1+c)(1-ac)},\qquad
v_*=\frac{2(1-c)}{(1+a)(1-ac)}.
\]
At this point
\[
L_1(u_*)=L_2(u_*)=\frac{2(1+ac)}{(1+a)(1+c)}.
\]
Moreover
\[
L_1'(u_*)>0,\qquad L_2'(u_*)<0.
\]
Since \(L_2'\) changes sign only after \(u_*\), \(L_2\) is decreasing to the left of the balance; similarly \(L_1\) is increasing to the right. Thus, whenever \((u_*,v_*)\) is feasible, it is the global minimizer. Directly,
\[
u_*\ge1\iff a(c+2)\le1,
\qquad
v_*\ge1\iff c(a+2)\le1,
\]
which gives the balanced regime.

If \(c(a+2)>1\), then \(v_*<1\). The feasible active arc terminates before the balance at \(v=1\), where
\[
u_c=\frac{A^2}{1-B^2}=\frac{1-a}{c(2-c-ac)}.
\]
Throughout that feasible arc one has \(L_2>L_1\) and \(L_2\) is decreasing, so the endpoint is optimal. Substitution gives
\[
d^2=L_2(u_c)=\frac{2(1-ac)}{2-c-ac}.
\]
The case \(a(c+2)>1\) is symmetric: the active arc starts after the balance at \(u=1\), where
\[
v_a=\frac{B^2}{1-A^2}=\frac{1-c}{a(2-a-ac)},
\]
and \(L_1\) is increasing there. Hence
\[
d^2=L_1(1)=\frac{2(1-ac)}{2-a-ac}.
\]
Finally, under \(a+c+ac<1\), the two strict inequalities \(a(c+2)>1\) and \(c(a+2)>1\) cannot hold simultaneously, because adding them would give \(a+c+ac>1\). Thus the regimes are exhaustive. The formulas agree on the equality boundaries by direct substitution.

## Verification
The proof is analytic and does not infer an infinite statement from finite computation. The key optimization is a two-variable convex feasibility problem reduced by sign symmetry to diagonal quadratic forms and then to a one-dimensional active curve. The displayed balance point satisfies the active constraint exactly and equalizes the two possible outer vertices. The factorization of \(1-A^2-B^2\), the feasibility equivalences for \(u_*\) and \(v_*\), and the endpoint substitutions were independently algebra-checked. Numerical minimization over randomly sampled \((a,c)\) was used only as a stress test before the proof and is not part of the justification.

## Relationship to prior work
Komuro, Saito, and Mitani classify the extreme points of the convex set of absolute normalized norms on \(\mathbb R^2\) by the two-parameter functions \(\psi_{\alpha,\beta}\), and calculate von Neumann--Jordan and James constants for substantial parts of the family. Their full-text exposition gives the same piecewise-linear extreme norms and identifies MSC 46B20, but does not state a Euclidean Banach--Mazur distance formula.

The symmetric slice \(a=c\) and the boundary slices \(a=0\) or \(c=0\) are excluded from the claim because exact Euclidean-distance formulas for those one-parameter cases are already covered in the checked prior record. The theorem instead gives the complete interior asymmetric two-parameter classification. A later paper of Zuo, Huang, and Wang uses Banach--Mazur distance to compare geometric constants of absolute normalized norms, but its theorem is a comparison inequality and does not determine the optimizing ellipse or the exact distance for this extreme family.

Database searches using the aliases “extreme absolute normalized norm,” “\(\psi_{\alpha,\beta}\),” “optimal ellipse,” and “Banach--Mazur distance” found no statement implying the four-regime formula. This is evidence of noncoverage among the inspected sources, not a proof that no equivalent result exists under unindexed convex-geometric terminology.

## Limitations
The theorem is for real two-dimensional spaces and for the interior asymmetric extreme family \(0<a,c<1\), \(a\ne c\). It does not claim a new result for the symmetric or boundary subfamilies. It determines distance to the Euclidean plane, not Banach--Mazur distances between two arbitrary members of the family. Older convex-body literature on optimal ellipses could contain an equivalent formulation that was not located by the checked aliases. The earliest exact day-level public date verified for the principal DOI record is 2010-07-20; older related proceedings records were located with only year or month precision and no day was invented for them.

## References
1. N. Komuro, K.-S. Saito, and K.-I. Mitani, “Extremal structure of the set of absolute norms on \(\mathbb R^2\) and the von Neumann--Jordan constant,” Journal of Mathematical Analysis and Applications 370 (2010), 101--106. DOI: 10.1016/j.jmaa.2010.04.016.
2. K.-I. Mitani, K.-S. Saito, and N. Komuro, “Extremal structure of the set of absolute norms,” RIMS Kôkyûroku 1737 (2011), 71--77.
3. Z.-F. Zuo, Y.-M. Huang, and J. Wang, “The generalized Gao's constant of absolute normalized norms in \(\mathbb R^2\),” Mathematical Inequalities & Applications 26 (2023), 109--129. DOI: 10.7153/mia-2023-26-09.
