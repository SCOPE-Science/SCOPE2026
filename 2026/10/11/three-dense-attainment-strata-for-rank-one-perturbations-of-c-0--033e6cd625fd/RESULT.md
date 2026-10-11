# Three dense attainment strata for rank-one perturbations of \(c_0\hookrightarrow\ell_\infty\)

## Finding
For \(\mathbb K\in\{\mathbb R,\mathbb C\}\), \(A,t>0\), and \(a=(a_n)\in\ell_1(\mathbb N)\) satisfying \(a_n\ge0\) and \(\sum_n a_n=A\), consider the bounded operator
\[
T_{a,t}:c_0(\mathbb K)\longrightarrow\ell_\infty(\mathbb K),\qquad
(T_{a,t}x)_n=\sum_{k=1}^{\infty}a_kx_k-tx_n.
\]
Its norm is \(\|T_{a,t}\|=A+t\), and it is bounded below by \(t/2\). With the canonical weak-star topology \(\sigma(\ell_\infty,\ell_1)\), the precise attainment classification is
\[
\begin{array}{rcl}
T_{a,t}\in\operatorname{NA}&\Longleftrightarrow&a\text{ has finite support},\\
T_{a,t}\in\operatorname{QNA}&\Longleftrightarrow&a\text{ has finite support},\\
T_{a,t}\in\mathrm{w^{*}QNA}&\Longleftrightarrow&a\text{ has at least one zero coordinate}.
\end{array}
\]
Consequently the three mutually exclusive possibilities—ordinary norm attainment, weak-star quasi norm attainment without quasi norm attainment, and failure of weak-star quasi norm attainment—are **each norm dense** inside the fixed-norm affine rank-one family \(\{T_{a,t}:a_n\ge0,\sum_n a_n=A\}\).

More precisely, the weak-star closure is
\[
K_{a,t}:=\overline{T_{a,t}(B_{c_0})}^{\sigma(\ell_\infty,\ell_1)}
=\bigl\{\bigl(\textstyle\sum_{k\ge1}a_kz_k-tz_n\bigr)_{n\ge1}:z\in B_{\ell_\infty}\bigr\}.
\]
If every \(a_n>0\), the weak-star compact convex set \(K_{a,t}\) has supremal distance \(A+t\) from the origin, but no point of \(K_{a,t}\) realizes that distance.

## Assumptions and scope
All sequence spaces use their standard norms over the stated scalar field. \(\operatorname{NA}\) means existence of \(x\in B_{c_0}\) with \(\|Tx\|=\|T\|\). \(\operatorname{QNA}\) means the norm closure of \(T(B_{c_0})\) meets the sphere of radius \(\|T\|\). \(\mathrm{w^{*}QNA}\) means its \(\sigma(\ell_\infty,\ell_1)\)-closure meets the same sphere. All three notions use the unit ball, not an assumed maximizing sequence in the dual. Coefficients \(a_n\) are nonnegative real numbers even over the complex scalar field; both \(t\) and \(A\) are strictly positive. The result classifies this specific one-direction rank-one perturbation of the canonical inclusion, not arbitrary operators into dual spaces.

## Proof
**1. Exact norm and bounded-below estimate.** Let \(\varphi_a(x)=\sum_k a_kx_k\). The \(n\)-th coordinate functional of \(T_{a,t}\) is \(\varphi_a-t\delta_n\). By the standard identification \(c_0^*=\ell_1\), its norm is
\[
\|\varphi_a-t\delta_n\|
=\sum_{k\ne n}a_k+|a_n-t|
=A+t-2\min\{a_n,t\}.
\]
Because \(a_n\to0\), \(\|T_{a,t}\|=\sup_n\|\varphi_a-t\delta_n\|=A+t\). For \(x\in c_0\), write \(c=\varphi_a(x)\). Since \((T_{a,t}x)_n=c-tx_n\to c\), we have \(|c|\le\|T_{a,t}x\|_\infty\). Thus
\[
t\|x\|_\infty\le|c|+\|T_{a,t}x\|_\infty
\le2\|T_{a,t}x\|_\infty.
\]
In particular, \(T_{a,t}\) is a monomorphism with closed range. If \(T_{a,t}x_j\) converges in norm for \(x_j\in B_{c_0}\), then \((x_j)\) is norm Cauchy, so its limit in \(B_{c_0}\) is a norm-attaining point whenever the image limit has norm \(A+t\). Hence \(\operatorname{QNA}\) and \(\operatorname{NA}\) coincide for these operators.

**2. Norm attainment is exactly finite support.** If \(a\) has finite support, choose \(j\) outside it. Set \(x_k=1\) for \(a_k>0\), \(x_j=-1\), and all other entries to zero. Then \(x\in B_{c_0}\) and \((T_{a,t}x)_j=A+t\).

Conversely, suppose \(\|T_{a,t}x\|=A+t\) for some \(x\in B_{c_0}\). The coordinates \(c-tx_n\) converge to \(c\) with \(|c|\le A<A+t\); therefore the supremum is achieved at a finite coordinate \(j\). At that coordinate
\[
A+t=|c-tx_j|\le |c|+t|x_j|\le A+t,
\]
so \(|\varphi_a(x)|=A\). Equality in the absolutely convergent weighted triangle inequality forces \(x_k=\omega\) for every \(k\) such that \(a_k>0\), for one scalar \(\omega\) of modulus one. Indeed, multiplying by \(\overline\omega\) and taking real parts shows \(\sum_k a_k\bigl(1-\operatorname{Re}(\overline\omega x_k)\bigr)=0\), hence each term vanishes. Since \(x\in c_0\), the set of such indices must be finite. Therefore \(T_{a,t}\in\operatorname{NA}\) exactly for finitely supported \(a\).

**3. Identify the entire weak-star closure.** Extend the formula to \(S_{a,t}:\ell_\infty\to\ell_\infty\) using the same series. It is \(\sigma(\ell_\infty,\ell_1)\)-continuous: for each \(b\in\ell_1\), the functional \(z\mapsto\langle S_{a,t}z,b\rangle\) is represented by the summable coefficient sequence \(\bigl((\sum_nb_n)a_k-tb_k\bigr)_{k\ge1}\). The ball \(B_{\ell_\infty}\) is weak-star compact, and the finite truncations of every element of this ball lie in \(B_{c_0}\) and converge weak-star to that element. Continuity and compactness therefore prove
\[
\overline{T_{a,t}(B_{c_0})}^{w^*}=S_{a,t}(B_{\ell_\infty}).
\]
If \(a_j=0\) for some \(j\), choose \(z_k=1\) on the support of \(a\) and \(z_j=-1\), arbitrarily assigning bounded values elsewhere. Then \((S_{a,t}z)_j=A+t\). This proves weak-star quasi norm attainment whenever any coefficient vanishes.

If, on the other hand, \(a_n>0\) for every \(n\), each fixed coordinate of \(S_{a,t}z\), for \(z\in B_{\ell_\infty}\), is strictly smaller in absolute value than \(A+t\), by the row-norm identity from step 1. Were \(\|S_{a,t}z\|=A+t\), there would be a sequence of distinct indices \(n_j\to\infty\) satisfying
\[
\left|\sum_k a_kz_k-tz_{n_j}\right|\to A+t.
\]
The triangle inequality forces \(|\sum_k a_kz_k|=A\). Equality in the same weighted triangle inequality, now with all weights strictly positive, forces \(z_k=\omega\) for **every** \(k\), with \(|\omega|=1\). But then \(S_{a,t}z=(A-t)\omega\mathbf1\) and its norm is \(|A-t|<A+t\), a contradiction. Thus there is no weak-star norm-maximizer. This establishes the complete trichotomy.

**4. All three cases are dense at constant operator norm.** Fix \(A,t>0\) and the positive \(\ell_1\)-simplex \(\mathcal P_A=\{a\in\ell_1:a_n\ge0,\sum_n a_n=A\}\). The map \(a\mapsto T_{a,t}\) is isometric:
\[
\|T_{a,t}-T_{b,t}\|=\|\varphi_a-\varphi_b\|=\|a-b\|_1.
\]
Finite-support vectors are dense in \(\mathcal P_A\): truncate after \(N\), and renormalize the retained positive mass to \(A\). Full-support vectors are dense by replacing \(a\) with \((1-\varepsilon)a+\varepsilon A p\), where \(p_n=2^{-n}\) and \(0<\varepsilon<1\).

For density of infinite-support vectors with a zero, take an index \(j\) with arbitrarily small \(a_j\), and a different index \(k\) with \(a_k>0\). Transfer the mass \(a_j\) to coordinate \(k\), making coordinate \(j\) zero and changing the \(\ell_1\)-norm by \(2a_j\). Mix the result with an arbitrarily small amount of the mass-\(A\) sequence \(A p^{(j)}\), where \(p^{(j)}_j=0\) and \(p^{(j)}_i=2^{-i}/(1-2^{-j})\) for \(i\ne j\). The resulting positive vector has mass \(A\), has infinitely many positive coefficients but retains its zero at \(j\), and approaches \(a\) in \(\ell_1\). This proves all three norm-density assertions without varying the common norm \(A+t\). Furthermore, the sets \(U_n=\{a\in\mathcal P_A:a_n>0\}\) are relatively open and dense, so the full-support stratum \(\bigcap_n U_n\) is a dense \(G_\delta\). Its complement, the weak-star quasi norm-attaining stratum \(\bigcup_n\{a\in\mathcal P_A:a_n=0\}\), is a dense meager \(F_\sigma\): each vanishing-coordinate set is closed and has empty interior. Thus the generic member of the fixed-norm affine family fails weak-star quasi norm attainment, although the set of members satisfying it is dense.

## Verification
Every step above is analytic. The exact row-functional identity verifies the operator normalization for both scalar fields, while the pointwise limit of \(T_{a,t}x\) supplies the lower bound and the finite-coordinate norm-attainment obstruction. The weak-star closure is checked through explicit finite truncations, weak-star continuity, and Banach--Alaoglu compactness. The only use of equality in an infinite sum is justified by the displayed nonnegative series. The density constructions preserve \(\sum_n a_n=A\) exactly, and the rank-one distance formula is an isometry rather than an asymptotic estimate.

As explicit examples, \(a_n=2^{-n}\) gives failure of weak-star quasi norm attainment; \(a_1=0\) and \(a_n=2^{1-n}\) for \(n\ge2\) gives weak-star quasi norm attainment without quasi norm attainment; and any finitely supported positive vector of mass \(A\) gives norm attainment. No computational sampling is used to infer the infinite-dimensional conclusion.

## Relationship to prior work
Choi--Jung--Kim--Martín introduced weak-star quasi norm attainment and proved its general density, including via rank-one perturbations (arXiv:2209.07763v1, Theorem 2.1). Their Example 3.4 supplies a diagonal \(c_0\)-domain example in which weak-star quasi norm attainment is strictly weaker than quasi norm attainment; Example 4.11 gives existence of nonremotal weak-star compact convex sets. Neither result classifies the fixed-norm affine family above or shows that all three attainment behaviors are norm dense within it.

Choi--Choi--Jung--Martín previously proved that a bounded-below quasi norm-attaining operator must attain its norm (arXiv:2004.11025v1, Lemma 2.5); that implication is background, independently recovered by the short estimate in step 1. Jung--Martínez-Cervantes--Rueda Zoca constructed rank-one perturbations failing ordinary norm attainment from reflexive domains (arXiv:2301.05003v1, Theorem 2.1), a different conclusion and domain hypothesis. The new content here is the support-exact third level of attainment and the simultaneous fixed-norm density and Baire-category stratification, not any of these previously established general facts.

## Limitations
The theorem requires positive \(\ell_1\) coefficients, a positive scalar multiple of the canonical inclusion, and the specific predual \(\ell_1\) of \(\ell_\infty\). It does not classify arbitrary signed coefficients, arbitrary rank-one output vectors, other dual topologies, or general operators between Banach spaces. The compact convex set is nonremotal specifically from the origin. Literature comparisons cannot exclude every differently worded or unindexed earlier proof, and no independent external validation is asserted.

## References
1. Geunsu Choi, Mingu Jung, Sun Kwang Kim and Miguel Martín, *Weak-star quasi norm attaining operators*, arXiv:2209.07763v1, publicly submitted 2022-09-16; especially Theorem 2.1, Example 3.4, Remark 3.5 and Example 4.11. https://arxiv.org/abs/2209.07763
2. Geunsu Choi, Yun Sung Choi, Mingu Jung and Miguel Martín, *On quasi norm attaining operators between Banach spaces*, arXiv:2004.11025v1, publicly submitted 2020-04-23; especially Lemma 2.5. https://arxiv.org/abs/2004.11025
3. Mingu Jung, Gonzalo Martínez-Cervantes and Abraham Rueda Zoca, *Rank-one perturbations and norm-attaining operators*, arXiv:2301.05003v1, publicly submitted 2023-01-12; especially Theorem 2.1 and its proof. https://arxiv.org/abs/2301.05003
