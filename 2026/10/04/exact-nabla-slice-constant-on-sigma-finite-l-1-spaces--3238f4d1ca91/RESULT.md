# Exact \(\nabla\)-slice constant on \(\sigma\)-finite \(L_1\) spaces

## Finding
Let \((\Omega,\Sigma,\mu)\) be a real \(\sigma\)-finite measure space and let \(f\in S_{L_1(\mu)}\). Define the avoiding-slice, or \(\nabla\)-slice, constant by
\[
\operatorname{nsc}(f):=\inf_{\substack{S\subset B_{L_1(\mu)}\text{ a slice}\\ f\notin S}}\ \sup_{g\in S}\|f-g\|_1,
\]
and define the largest atomic mass carried by \(|f|\) by
\[
m(f):=\sup\left\{\int_A |f|\,d\mu:A\text{ is a }\mu\text{-atom}\right\},
\]
with the supremum of the empty set equal to \(0\). Then
\[
\operatorname{nsc}(f)=
\begin{cases}
2,&m(f)=0\text{ or }m(f)=1,\\[2mm]
2\bigl(1-m(f)\bigr),&0<m(f)<1.
\end{cases}
\]
Consequently \(\operatorname{nsc}(f)=2\) exactly when \(f\) is a \(\nabla\)-point: either the support of \(f\) contains no atom, or \(f\) is a signed normalized indicator of one atom. In particular, for \(x\in S_{\ell_1(I)}\),
\[
\operatorname{nsc}(x)=
\begin{cases}
2,&\|x\|_\infty=1,\\
2\bigl(1-\|x\|_\infty\bigr),&\|x\|_\infty<1.
\end{cases}
\]

## Assumptions and scope
The scalar field is real. The measure is \(\sigma\)-finite, so \(L_1(\mu)^*=L_\infty(\mu)\), and every slice can be written as
\[
S(\varphi,\alpha)=\left\{g\in B_{L_1(\mu)}:\int \varphi g\,d\mu>1-\alpha\right\}
\]
with \(\varphi\in S_{L_\infty(\mu)}\) and \(\alpha>0\). Distinct atoms are disjoint modulo null sets, and every measurable scalar function is essentially constant on an atom. The statement is pointwise; it does not assert a vector-valued \(L_1(\mu,X)\) formula.

## Proof
Assume first that \(0<m(f)<1\). The supremum defining \(m(f)\) is attained. Indeed, if atomic masses approached a positive supremum without attaining it, infinitely many distinct atoms would eventually carry more than half that supremum, contradicting \(\|f\|_1=1\). Choose an atom \(A\) with \(\int_A|f|\,d\mu=m(f)\), and let \(\theta\in\{-1,1\}\) be the sign of \(f\) on \(A\). Put \(\varphi=\theta\chi_A\). The slice
\[
S_0=\left\{g\in B_{L_1(\mu)}:\int_A\theta g\,d\mu>m(f)\right\}
\]
does not contain \(f\). If \(g\in S_0\) and \(q=\int_A|g|\,d\mu\), then \(g\) has the same sign as \(f\) on \(A\), \(q>m(f)\), and
\[
\|f-g\|_1\le \bigl(q-m(f)\bigr)+\bigl(1-m(f)\bigr)+(1-q)=2\bigl(1-m(f)\bigr).
\]
For \(0<\varepsilon<1-m(f)\), decompose \(f=f_A+f_R\) with \(f_A=f\chi_A\) and define
\[
g_\varepsilon=\frac{m(f)+\varepsilon}{m(f)}f_A-\frac{1-m(f)-\varepsilon}{1-m(f)}f_R.
\]
Then \(g_\varepsilon\in S_0\), \(\|g_\varepsilon\|_1=1\), and direct calculation gives
\[
\|f-g_\varepsilon\|_1=2\bigl(1-m(f)\bigr).
\]
Thus \(\operatorname{nsc}(f)\le 2(1-m(f))\).

For the reverse inequality, let \(S(\varphi,\alpha)\) be any slice avoiding \(f\), and put
\[
E=\{\omega:|\varphi(\omega)|>1-\alpha\}.
\]
The set \(E\) has positive measure. If \(E\) contains an atom \(B\), then \(\varphi\) is constant on \(B\). With \(\eta\) its sign there, the normalized atomic vector
\[
h=\frac{\eta}{\mu(B)}\chi_B
\]
belongs to the slice. Writing \(p_B=\int_B|f|\,d\mu\le m(f)\), one has \(\|f-h\|_1=2(1-p_B)\) when the signs agree and \(\|f-h\|_1=2\) otherwise. Hence the slice supremum is at least \(2(1-m(f))\).

If \(E\) contains no atom, then the restricted measure on \(E\) is atomless. Given \(\delta>0\), \(\sigma\)-finiteness and atomlessness provide a measurable \(C\subset E\) with \(0<\mu(C)<\infty\) and \(\int_C|f|\,d\mu<\delta\). The vector
\[
h_C=\frac{\operatorname{sgn}(\varphi)}{\mu(C)}\chi_C
\]
belongs to the slice and satisfies
\[
\|f-h_C\|_1\ge 2-2\int_C|f|\,d\mu>2-2\delta.
\]
So in this case the slice supremum is \(2\). This proves the lower bound and hence the formula when \(0<m(f)<1\).

If \(m(f)=0\), the same two-case argument makes every avoiding slice have supremum \(2\): an atomic witness has zero overlap with \(f\), while on an atomless high-level set the preceding \(h_C\) tends to distance \(2\). Thus \(\operatorname{nsc}(f)=2\).

Finally suppose \(m(f)=1\). Then all \(L_1\)-mass of \(f\) lies on one atom \(A\), so \(f\) is a signed normalized indicator of \(A\). For an arbitrary avoiding slice, an atomic high-level witness supported on an atom different from \(A\), or with the opposite sign on \(A\), is at distance \(2\). The only remaining atomic possibility would reproduce \(f\), which is excluded because the slice avoids \(f\). If the high-level set is atomless, it is disjoint from \(A\) modulo null sets and again gives a distance-\(2\) witness. Hence \(\operatorname{nsc}(f)=2\).

## Verification
The proof is analytic and covers all real \(\sigma\)-finite scalar \(L_1\) spaces. The accompanying `verify_nabla_l1.py` performs an independent exact-rational stress test on finite atomic models: it enumerates crosspolytope slice vertices and edge intersections, checks arbitrary avoiding slices against the claimed lower bound, verifies the canonical upper-bound slice exactly, and checks the signed-basis endpoint. It uses no floating point arithmetic. Finite polyhedral checks support, but do not replace, the infinite-dimensional proof.

## Relationship to prior work
Haller, Langemets, Perreau and Veeorg introduced and studied \(\nabla\)-points and proved the qualitative scalar \(L_1\) classification: atom-free support gives a Daugavet, hence \(\nabla\), point, while a point whose support contains an atom is \(\nabla\) exactly when it is a signed normalized indicator of an atom. Choi and Jung introduced quantitative Daugavet and \(\Delta\)-constants; their constants take the infimum over all slices and over slices containing the point, respectively. For atomic \(L_1\) they obtained the exact Daugavet formula, and for \(\ell_1\) the Daugavet and \(\Delta\)-constants both equal \(2-2\|x\|_\infty\) on the unit sphere.

The present formula uses the complementary family of slices that avoid the point. For \(0<m(f)<1\) its numerical value agrees with the atomic Daugavet formula, but the endpoint behavior is different and essential: a normalized atom has Daugavet constant \(0\) while its avoiding-slice constant is \(2\). The formula also treats mixed atomic/nonatomic \(\sigma\)-finite measures directly. A later paper by Lee, Roldán and Tag gives further qualitative characterizations of \(\nabla\)-points in vector-valued function spaces; its inspected scalar \(L_1\) discussion remains qualitative.

## Limitations
The result is scalar and real. No vector-valued analogue is claimed. The literature comparison inspected the main papers defining \(\nabla\)-points, quantitative Daugavet/\(\Delta\)-constants, and the later vector-valued function-space treatment, together with targeted database searches; alternative terminology could conceal an equivalent quantitative invariant. The exact-rational script samples finite atomic geometry and is not a proof of the \(\sigma\)-finite theorem.

## References
1. R. Haller, J. Langemets, Y. Perreau, and T. Veeorg, *Unconditional bases and Daugavet renormings*, arXiv:2303.07037v1, first public 2023-03-13. See Definition 1.4 and Propositions 3.6--3.7.
2. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647v1, first public 2023-07-20. See Definition 2.1, Proposition 3.6, and Corollary 3.9.
3. H. J. Lee, Ó. Roldán, and H.-J. Tag, *On various diametral notions of points in the unit ball of some vector-valued function spaces*, arXiv:2410.04706v1, first public 2024-10-07. See Definition 1.2 and Section 4.4.
