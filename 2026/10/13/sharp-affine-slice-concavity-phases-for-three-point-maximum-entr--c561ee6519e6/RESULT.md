# Sharp affine-slice concavity phases for three-point maximum-entropy sampling

## Finding

Let \(0<a<1\), let \(C_a=(1-a)I_3+a\mathbf 1\mathbf 1^{\mathsf T}\), and let \(\Delta=\{x\in[0,1]^3:x_1+x_2+x_3=2\}\). For every \(\gamma>0\), define the scaled NLP-Id objective
\[
\Phi_{a,\gamma}(x)=\log\det\bigl(I_3+\operatorname{Diag}(\sqrt{x})(\gamma C_a-I_3)\operatorname{Diag}(\sqrt{x})\bigr)-2\log\gamma.
\]
Its **exact global affine-slice concavity classification** is
\[
\boxed{\Phi_{a,\gamma}\text{ is concave on }\Delta\iff
0<\gamma\le\frac{1}{1+a}\quad\text{or}\quad\gamma\ge\frac{1}{1-a}.}
\]
Every scale strictly between these intervals has a positive second directional derivative at a relative-interior feasible point, and hence is not concave on \(\Delta\).

Throughout the entire lower concavity interval the relaxed optimum is attained at \(x=(2/3,2/3,2/3)\) and has the **closed form**
\[
Z_a(\gamma)=\max_{x\in\Delta}\Phi_{a,\gamma}(x)
=\log\!\left(\frac{(1+2\gamma(1-a))^2(1+2\gamma(1+2a))}{27\gamma^2}\right).
\]
This bound is strictly decreasing in \(\gamma\) on \(0<\gamma\le1/(1+a)\). Its complete certified convex-optimization range therefore extends past the standard spectral endpoint \(1/(1+2a)\) for every \(a>0\).

The additional interval is **structurally stable**: for each fixed
\[
\frac{1}{1+2a}<\gamma<\frac{1}{1+a},
\]
there is an open neighborhood of \(C_a\) among positive-definite symmetric matrices such that the same scaled objective is strongly concave on \(\Delta\), although \(\gamma C-I_3\) is indefinite. This neighborhood includes covariance matrices with unequal off-diagonal correlations.

## Assumptions and scope

The theorem is about the actual cardinality-two hypersimplex, not about concavity on the entire three-dimensional cube. The covariance \(C_a\) has unit diagonal and eigenvalues \(1+2a\) and \(1-a\) (the latter twice); it is positive definite for \(0<a<1\). The parameter \(\gamma\) is any strictly positive real number. The determinant inside the logarithm is positive at every \(x\in\Delta\), including its boundary: its matrix is the sum of \(I_3-\operatorname{Diag}(x)\succeq0\) and \(\gamma\operatorname{Diag}(\sqrt{x})C_a\operatorname{Diag}(\sqrt{x})\succeq0\), with zero common kernel.

A non-equicorrelated perturbation of \(C_a\) is not claimed to have the same exact scale endpoints. The neighborhood claim concerns a **fixed strictly interior scale** in the newly established lower range.

## Proof

**1. Polynomial reduction.** Put \(b=\gamma(1-a)-1\), \(k=\gamma a\), and write \(e_2(x)=\sum_{i<j}x_ix_j\), \(e_3(x)=x_1x_2x_3\). Sylvester's determinant identity converts the square-root expression into \(\det(I_3+(\gamma C_a-I_3)\operatorname{Diag}(x))\). Since \(\gamma C_a-I_3=bI_3+k\mathbf1\mathbf1^{\mathsf T}\), direct determinant expansion yields
\[
D(x):=\det(I_3+\operatorname{Diag}(\sqrt{x})(\gamma C_a-I_3)\operatorname{Diag}(\sqrt{x}))
=1+(b+k)e_1(x)+B e_2(x)+H e_3(x),
\]
where \(B=b(b+2k)\) and \(H=b^2(b+3k)\). On \(\Delta\), \(e_1(x)=2\), hence
\[
D(x)=1+2(b+k)+B e_2(x)+H e_3(x)>0. \tag{1}
\]
The subtraction \(-2\log\gamma\) does not affect concavity in \(x\).

**2. Both spectral intervals.** If \(0<\gamma\le1/(1+2a)\), then \(Q=I_3-\gamma C_a\succeq0\) and
\[
D(x)=\det(I_3-Q^{1/2}\operatorname{Diag}(x)Q^{1/2}).
\]
The matrix inside this determinant is positive definite and affine in \(x\), so its log determinant is concave on the cube. If \(\gamma\ge1/(1-a)\), the analogous formula using \(P=\gamma C_a-I_3\succeq0\) is \(D(x)=\det(I_3+P^{1/2}\operatorname{Diag}(x)P^{1/2})\), giving cube concavity again.

**3. New lower interval.** Suppose \(1/(1+2a)\le\gamma\le1/(1+a)\). Then \(b<0\), \(b+2k\le0\), and \(b+3k\ge0\), so \(B,H\ge0\). On the constant-sum plane, \(e_2(x)=(4-\|x\|^2)/2\), which is concave. To see that \(e_3\) is concave specifically on \(\Delta\), set \(u=x_1\), \(v=x_2\), \(x_3=2-u-v\). Its coordinate Hessian is
\[
\nabla^2_{(u,v)}e_3=-2
\begin{pmatrix}v&u+v-1\\u+v-1&u\end{pmatrix}.
\]
The diagonal entries of the displayed positive-semidefinite matrix are nonnegative, and, putting \(p=1-u\), \(q=1-v\), \(r=u+v-1=1-x_3\), its determinant equals \(uv-r^2=pq+r(p+q)\ge0\). Thus \(e_3\) is concave on \(\Delta\). Equation (1) shows that \(D\) is positive and concave; since the logarithm is increasing and concave, \(\log D\) is concave. Combining this interval with Step 2 gives the complete lower sufficiency range.

**4. Sharp nonconcavity between the two ranges.** Now let \(1/(1+a)<\gamma<1/(1-a)\). Here \(b<0<b+2k\), and therefore \(B<0\). With \(u=x_1\), \(v=x_2\) and \(x_3=2-u-v\), equation (1) gives
\[
\partial_vD=(B+Hu)(2-u-2v),\qquad
\partial_{vv}D=-2(B+Hu).
\]
Choose a real \(0<\delta<1/4\) small enough that \(B+H\delta<0\), and take \(u=\delta\), \(v=1-\delta/2\). All three components lie strictly between zero and one and sum to two. At that point \(\partial_vD=0\) while
\[
\partial_{vv}\log D=\frac{-2(B+H\delta)}{D(\delta,1-\delta/2,1-\delta/2)}>0.
\]
The direction \((0,1,-1)\) is feasible in a neighborhood of this interior point, proving nonconcavity for every scale in the claimed gap. At the upper endpoint \(\gamma=1/(1-a)\), one has \(b=B=H=0\), so \(D\) is constant on \(\Delta\), and the endpoint is correctly included.

**5. Exact optimum and its scale dependence.** The lower-range objective is concave and invariant under all coordinate permutations. Averaging the permutations of any feasible point gives \((2/3,2/3,2/3)\), so Jensen's inequality places a maximizer there. At this point, the determinant's eigenvalues are \((1+2\gamma(1-a))/3\) twice and \((1+2\gamma(1+2a))/3\) once, proving the displayed closed form for \(Z_a(\gamma)\).

For \(0<\gamma\le1/(1+a)\), direct differentiation gives
\[
Z_a'(\gamma)=-\frac{2P_a(\gamma)}{\gamma(1+2\gamma(1-a))(1+2\gamma(1+2a))},
\quad P_a(t)=1+(1+2a)t-2(1-a)(1+2a)t^2.
\]
The polynomial \(P_a\) is concave on the positive half-line and satisfies \(P_a(0)=1\) and
\[
P_a\!\left(\frac1{1+a}\right)=\frac{a(7a+3)}{(1+a)^2}>0.
\]
Its minimum on the displayed closed interval occurs at an endpoint; thus \(P_a(\gamma)>0\) throughout and \(Z_a\) strictly decreases.

**6. Uniform curvature and stability beyond the spectral region.** Fix \(1/(1+2a)<\gamma<1/(1+a)\); then \(B,H>0\). If \(w\in\mathbb R^3\) is tangent to \(\Delta\), so \(\sum_iw_i=0\), then \(e_2''(x)[w,w]=-\|w\|^2\) and \(e_3''(x)[w,w]\le0\). It follows that
\[
\nabla^2\Phi_{a,\gamma}(x)[w,w]\le-\frac{B}{D(x)}\|w\|^2
\le-\frac{B}{D_{\max}}\|w\|^2,
\]
where \(D_{\max}=(1+2\gamma(1-a))^2(1+2\gamma(1+2a))/27>0\) is the exact maximal determinant from Step 5. Therefore the objective is strongly concave with respect to the Euclidean metric on the affine plane. For a general symmetric positive-definite \(C\), the determinant \(\det(I_3+(\gamma C-I_3)\operatorname{Diag}(x))\) is polynomial in \(x\) and continuous in \(C\), and stays strictly positive uniformly on the compact \(\Delta\) near \(C_a\). Its log-determinant Hessian thus varies uniformly continuously with \(C\). The strictly negative curvature margin persists for all sufficiently small symmetric perturbations. Eigenvalues also vary continuously; since \(\gamma\in(1/(1+2a),1/(1-a))\), the perturbed \(\gamma C-I_3\) remains indefinite. Choosing an arbitrarily small unequal off-diagonal perturbation proves the last assertion.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to compare a direct three-by-three determinant against the polynomial identity for 770 configurations, check positive determinant values, verify the sharp positive-curvature witnesses across rational parameters in the middle interval, check the endpoint identity, and verify the derivative polynomial and slice-Hessian identities. Its observed output was `VERIFY_OK: 770 positive exact determinant identities, phase witnesses, monotonicity endpoints, and slice curvature checks`. These finite checks corroborate critical formulas; the quantifiers over all real \(a\), \(\gamma\), and feasible \(x\) are established by Steps 1–6, not by enumeration.

## Relationship to prior work

Anstreicher, Fampa, Lee, Li, and Ponte (arXiv:2609.01214v1, first public 2026-09-01) introduce the general scaled NLP-Id objective, derive the two spectral sufficient concavity intervals, and study Hessian conditions on the ambient cube. Their Theorem 17 proves a sufficient low-scale interval for an equicorrelation family with \(0<a<1/3\), while Remark 16 explicitly distinguishes the unresolved issue of checking curvature on the affine cardinality slice. The present result instead classifies the **entire** affine-slice scale range for \(n=3\), \(s=2\) and all \(0<a<1\), including necessity; it also gives an exact relaxation-value formula, strict lower-branch scale monotonicity, and stable non-equicorrelated examples of off-spectral concavity.

Ponte, Fampa, and Lee (arXiv:2511.04350v3) establish relationships between NLP-Id and natural bounds for associated D-optimal-design problems, notably at the identity spectral scaling. Those objective equivalences do not imply the present sharp all-scale affine-slice classification or its curvature margin. The historical 1996/1999 relaxation work motivates the model, not a claimed first introduction of the underlying determinant formulation.

## Limitations

The exact endpoints are proved only for three variables, two selected coordinates, and positive equicorrelation \(0<a<1\). The perturbation result asserts existence of an open neighborhood for fixed strictly interior lower-range scales, without a numerical perturbation radius or transferred sharp endpoints. For equicorrelated \(C_a\), all integral pairs have the same determinant \(1-a^2\), so the computational significance is chiefly in the relaxation's curvature and its transfer to nearby, non-equicorrelated matrices; no faster end-to-end discrete algorithm is claimed. Prior coverage cannot be excluded solely by unsuccessful searches; the complete 1996/1999 originals were not materially inspected. This manuscript supplies a self-review, not independent validation.

## References

1. K. Anstreicher, M. Fampa, J. Lee, Y. Li, and G. Ponte, *New insights into the NLP-Id bound for maximum-entropy sampling*, arXiv:2609.01214v1 (2026-09-01), Sections 2–5, particularly Theorem 17 and Remark 16. https://arxiv.org/html/2609.01214v1
2. G. Ponte, M. Fampa, and J. Lee, *On the relationship between MESP and 0/1 D-Opt and their upper bounds*, arXiv:2511.04350v3, Sections 3.1 and 3.3. https://arxiv.org/html/2511.04350v3
3. K. Anstreicher, M. Fampa, J. Lee, and J. Williams, *Using continuous nonlinear relaxations to solve constrained maximum-entropy sampling problems*, Mathematical Programming 85 (1999), 221–240, DOI:10.1007/s101070050055 (historical context; complete text not inspected).
