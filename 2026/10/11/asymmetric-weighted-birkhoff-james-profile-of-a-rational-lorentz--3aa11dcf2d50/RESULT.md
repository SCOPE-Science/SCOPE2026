# Asymmetric weighted Birkhoff–James profile of a rational Lorentz octagon

## Finding

Let \(X=\mathbb R^2\) with the absolute norm
\[
N(s,t)=\max\bigl\{|s|,|t|,\tfrac23(|s|+|t|)\bigr\}.
\]
For all \(0\le\lambda\le1\), the weighted Birkhoff–James constant introduced in [1] is
\[
J^\perp_\lambda(X):=\sup_{N(x)=N(y)=1,\ x\perp_B y}
\min\bigl\{N(\lambda x+(1-\lambda)y),N(\lambda x-(1-\lambda)y)\bigr\},
\]
where \(x\perp_B y\) means \(N(x+sy)\ge N(x)\) for every real \(s\). Its exact profile is
\[
\boxed{J^\perp_\lambda(X)=\max\left\{1-\frac{2\lambda}{3},\frac34,\frac25+\frac{3\lambda}{5}\right\}}
=\begin{cases}
1-2\lambda/3,&0\le\lambda\le3/8,\\
3/4,&3/8\le\lambda\le7/12,\\
2/5+3\lambda/5,&7/12\le\lambda\le1.
\end{cases}
\]
Thus a signed-permutation-invariant (absolute symmetric) Banach-plane norm need not produce a weight-reflection-symmetric Birkhoff–James profile: in fact
\[
\boxed{\max_{0\le\lambda\le1}
|J^\perp_\lambda(X)-J^\perp_{1-\lambda}(X)|=\frac1{40}},
\]
with equality at \(\lambda=3/8\) and \(\lambda=5/8\). The middle constant region is exactly \([3/8,7/12]\), and \(J^\perp_{1/2}(X)=3/4\).

## Assumptions and scope

The space is real, two-dimensional, and the ordered relation \(x\perp_B y\) uses Birkhoff–James orthogonality in the first variable. The unit ball is the rational octagon with vertices given by signed permutations of \((1,1/2)\); the point \((3/4,3/4)\) lies in the interior of a diagonal edge. The norm is also the two-dimensional Lorentz-predual model \(d_*(1,1/2)^2\). The theorem covers every *real* weight \(\lambda\in[0,1]\), including both endpoints; it does not assert a formula in higher dimensions or for other Lorentz parameters.

## Proof

**Step 1: Exhaust all ordered orthogonal pairs up to isometry.** The norm has the eight signed-permutation isometries, under which both the ordered orthogonality condition and the objective are invariant. Thus we may restrict the first unit vector to the sector \(0\le x_2\le x_1\). Its unit arc has two parameterizations, with \(0\le u\le1\):
\[
 x=(1,u/2),\qquad
 x=(1-u/4,1/2+u/4).
\]
The norm is the maximum of the following eight linear facets:
\[
\mathcal F=\{(\pm1,0),(0,\pm1),(\pm2/3,\pm2/3)\},
\]
where the last signs are chosen independently, and a facet acts by dot product.

For any unit \(x\), the finite-dimensional norming-functional criterion [2] states \(x\perp_B y\) precisely when some norm-one supporting functional at \(x\) annihilates \(y\). On the open vertical edge, that functional is \((1,0)\), so, up to \(y\mapsto-y\), the only admissible unit direction is \((0,1)\). On the open diagonal edge, it is \((2/3,2/3)\), giving \((-3/4,3/4)\). At the joint vertex \(x=(1,1/2)\), norming functionals form the interval spanned by those two facets, so the allowed orientation is exactly \(y_1\le0\le y_1+y_2\). Its unit arc splits into the two segments from \((0,1)\) through \((-1/2,1)\) to \((-3/4,3/4)\). Consequently every admissible ordered pair is represented (possibly redundantly at endpoints) by **one of four affine paths** \((x(u),y(u))\), \(0\le u\le1\):
\[
\begin{array}{c|c|c}
\text{path}&x(u)&y(u)\\\hline
1&(1,u/2)&(0,1)\\
2&(1-u/4,1/2+u/4)&(-3/4,3/4)\\
3&(1,1/2)&(-u/2,1)\\
4&(1,1/2)&(-1/2-u/4,1-u/4).
\end{array}
\]
The cases include all endpoints; no differentiability or strict-convexity assumption was made.

**Step 2: Three exact global lower bounds.** The three unit, ordered Birkhoff-orthogonal pairs
\[
\begin{aligned}
(x,y)&=((1,1/2),(-1/2,1)),\\
(x,y)&=((3/4,3/4),(-3/4,3/4)),\\
(x,y)&=((1,1/2),(-2/5,1))
\end{aligned}
\]
give, respectively,
\[
J^\perp_\lambda(X)\ge1-2\lambda/3,\qquad
J^\perp_\lambda(X)\ge3/4,\qquad
J^\perp_\lambda(X)\ge2/5+3\lambda/5.
\]
To check these inequalities for **every** weight, choose in the first pair the plus facet \((0,1)\) and minus facet \((2/3,-2/3)\); in the second the plus facet \((0,1)\) and minus facet \((1,0)\); and in the third the plus facet \((2/3,2/3)\) and minus facet \((1,0)\). Each chosen facet evaluates to at least the displayed linear bound at both endpoints \(\lambda=0,1\), hence for all intermediate weights by affinity. The first and third pairs satisfy the vertex normal-cone criterion, and the second pair is annihilated by the diagonal supporting facet.

**Step 3: Exhaustive rational upper certificate, valid on a continuum.** Write \(F(\lambda)\) for the maximum of the preceding three lines, whose breakpoints are \(3/8\) and \(7/12\). On each of its three closed linearity intervals, fix a path \((x(u),y(u))\) from Step 1 and two facets \(f,g\in\mathcal F\). Define
\[
 p(\lambda,u)=f\cdot[\lambda x(u)+(1-\lambda)y(u)]-F(\lambda),\qquad
 q(\lambda,u)=g\cdot[\lambda x(u)-(1-\lambda)y(u)]-F(\lambda).
\]
Each is affine in \(u\) at fixed \(\lambda\), with coefficients affine in \(\lambda\). If the minimum of the two weighted norms exceeded \(F(\lambda)\), some choice of \(f,g\) would make both \(p,q>0\). For fixed \(\lambda\), this simultaneous strict positivity can occur only at \(u=0\), \(u=1\), or at the interior crossing \(p=q\): the minimum of two affine functions reaches its maximum at an endpoint or their crossing.

For each of the \(4\times3\times8\times8=768\) path/weight-branch/facet-pair cases, write the endpoint polynomials in \(\lambda\) as \(p_0,p_1,q_0,q_1\). As the weight varies, the strict-feasibility status can change only at zeros of one of those four polynomials or of
\[
\Delta(\lambda)=p_0(\lambda)q_1(\lambda)-p_1(\lambda)q_0(\lambda).
\]
Indeed, a change must pass through a zero at an endpoint or through a simultaneous zero \(p=q=0\) at an interior parameter. These polynomials have rational coefficients and degree at most two. The standalone verifier `verify_weighted_james.py` generates **all 3840 polynomials**, finds every real root within each linearity interval in exact rational arithmetic (checking the rational square roots of all relevant discriminants), and evaluates the endpoint/crossing feasibility at **every critical weight and one rational point of each complementary interval**. All **2488 exact tests** rule out strict positivity for both facets. This is a finite *symbolic certificate of an all-real-parameter assertion*, not extrapolation from a numerical grid. It proves \(J^\perp_\lambda(X)\le F(\lambda)\) for every \(\lambda\in[0,1]\), establishing the profile.

**Step 4: Determine weight-reflection asymmetry.** On \([0,1]\), the continuous piecewise-affine difference \(J^\perp_\lambda(X)-J^\perp_{1-\lambda}(X)\) has breakpoints among \(0,3/8,5/12,7/12,5/8,1\). Checking these six points yields maximal absolute value \(1/40\), exactly at \(3/8\) and \(5/8\). This concludes the proof.

## Verification

With Python 3 and no third-party packages, execute `python3 verify_weighted_james.py` in the directory containing that file. The expected successful output is `WEIGHTED_JAMES_OCTAGON_ALL_PARAMETERS_EXACT_OK test_points= 2488 critical_polynomials= 3840 lower_families= 3`. This verifies all reduced facet-pair cases using exact rational arithmetic; it is **not** a proof about an arbitrarily chosen grid. The reduction in Step 1 and feasibility argument in Step 3 explain why the finite checks prove the continuously quantified upper bound. One may independently reconstruct all four paths and the 8 signed facets from their explicit coordinates above.

## Relationship to prior work

Qi–Yin–Liu–Li [1] introduced precisely the weighted Birkhoff-orthogonal James invariant and proved general geometric properties. The present theorem is an exact profile for an absolute symmetric rational octagonal plane, with a flat phase and a sharp weight-reflection asymmetry. The complete 17-page first version of [1] was inspected: Section 2 gives exact Hilbert values, an \(\ell_1^2\) example, and an \(\ell_p^n\) lower-bound example, while Section 3 develops inequalities (including Proposition 3.1), continuity, and geometric consequences. Neither its examples nor its statements classify an octagonal Lorentz-predual plane or determine a weight-reflection asymmetry. The general upper envelope from Proposition 3.1, using \(J_{\perp}(X)=3/2\), is \(|2\lambda-1|+\tfrac32\min\{\lambda,1-\lambda\}\), which is strictly above the exact profile at many weights. An unindexed equivalent result elsewhere remains possible.

Martín–Merí–Quero–Roy–Sain [2] give the standard norming-functional criterion and broader theory of Birkhoff–James orthogonality, but not this exact weighted invariant. Fang–Xu–Liu–Gu–Li [3] discuss *approximate-orthogonality* James families, a different parameterization, without evidence in the accessible abstract of this exact octagonal result. Related computations of Euclidean distortion, two-axis octahedrality, and parameterized von Neumann–Jordan invariants for octagonal spaces concern genuinely different functions; none mathematically implies the claimed weighted orthogonal James profile.

## Limitations

Only the named real two-dimensional norm is classified. The result does not compute \(J^\perp_\lambda\) on all Lorentz-predual planes, nor assert the same behavior in complex spaces. The proof is computer-assisted at the finite rational-facet elimination stage: its critical-polynomial enumeration is fully supplied as standalone readable Python code. Relevant full-text access gaps and the possibility of prior unindexed equivalent formulations limit the originality assurance; searches alone are not a novelty proof.

## References

[1] J. Qi, Z. Yin, Q. Liu, Y. Li, *A weighted Birkhoff orthogonal James-type constant*, arXiv:2606.01068v1, first publicly submitted 2026-05-31, https://arxiv.org/abs/2606.01068.

[2] M. Martín, J. Merí, A. Quero, S. Roy, D. Sain, *A numerical range approach to Birkhoff–James orthogonality with applications*, Banach Journal of Mathematical Analysis 18 (2024), article 24, https://doi.org/10.1007/s43037-024-00333-1.

[3] Z. Fang, Y. Xu, Q. Liu, Z. Gu, Y. Li, *James-type constants for Birkhoff--James orthogonality and approximate isosceles*, arXiv:2609.37502v1, first publicly submitted 2026-09-26, https://arxiv.org/abs/2609.37502.
