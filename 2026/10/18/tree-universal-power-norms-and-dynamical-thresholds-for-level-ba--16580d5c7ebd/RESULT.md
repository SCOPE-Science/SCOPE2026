# Tree-universal power norms and dynamical thresholds for level-balanced Cesàro shifts

## Finding
Fix \(1<p<\infty\). Every infinite rooted, leafless, locally finite tree admits a canonical level-balanced weighted backward shift whose entire power-norm profile is independent of its branching. If \(\gamma\ne0\), then for every integer \(n\ge1\),
\[
\boxed{\|B_\gamma^n\|=|\gamma|^n\left(\frac{\zeta(p)}{\zeta(p,n+1)}\right)^{1/p}},
\qquad \zeta(p,n+1)=\sum_{j=n+1}^{\infty}j^{-p}.
\]
The nonzero norm-attaining vectors of \(B_\gamma^n\) are exactly those supported on the \(n\)-th level, with all nonzero coordinates sharing one complex phase. The sharp growth law is
\[
\|B_\gamma^n\|\sim ((p-1)\zeta(p))^{1/p}|\gamma|^n n^{1-1/p}.
\]
In particular, the spectral radius is \(|\gamma|\). If \(|\gamma|<1\) the powers converge to zero in operator norm; at \(|\gamma|=1\) the operator is mixing but has no nonzero periodic points and is not frequently hypercyclic; at \(|\gamma|>1\) it is mixing, chaotic and frequently hypercyclic.

## Assumptions and scope
Let \(T=(V,E)\) be a countably infinite rooted directed tree with root \(o\), no leaves, and finitely many children at each vertex. Let \(D_k=\{v\in V:|v|=k\}\), \(c_k=|D_k|\); hence \(c_0=1\) and \(1\le c_k<\infty\). For any complex-valued function on the vertices, put
\[
A_k(f)=\frac1{c_k}\sum_{v\in D_k}|f(v)|,
\qquad
\|f\|_{\operatorname{Ces}_p(T)}=
\left[\sum_{N=0}^\infty\left(\frac1{N+1}\sum_{k=0}^{N} A_k(f)\right)^p\right]^{1/p}.
\]
The Banach space consists of functions of finite norm. It contains finitely supported functions densely [1]. Fix \(\gamma\in\mathbb C\setminus\{0\}\) and define the bounded operator
\[
(B_\gamma f)(v)=\gamma\frac{c_{|v|}}{c_{|v|+1}}
\sum_{u\in\operatorname{Chi}(v)}f(u).
\]
Weights are constant within each level but the tree may have arbitrary uneven branching. In the real case, replace “common complex phase” by “common sign.” There is no assumption of bounded branching degrees or regularity of the sequence of level sizes.

## Proof
**1. A sharp one-dimensional Cesàro shift lemma.** For a nonnegative sequence \(a=(a_k)_{k\ge0}\) of finite Cesàro norm write \((La)_k=a_{k+1}\). Define the positive tails
\[
H_p(t)=\sum_{j=t}^{\infty}j^{-p}\qquad(t=1,2,\ldots).
\]
For every integer \(n\ge1\),
\[
\|L^n a\|_{\operatorname{ces}_p}\le
\left(\frac{H_p(1)}{H_p(n+1)}\right)^{1/p}
\|a\|_{\operatorname{ces}_p},
\]
with equality for a nonzero \(a\) exactly when \(a\) is concentrated at index \(n\).

To prove this, first delete all coordinates preceding index \(n\). This does not affect the numerator and cannot increase the denominator; equality for a nonzero vector requires all deleted coordinates to vanish. Put \(y_j=a_{n+j}\), \(U_k=\sum_{j=0}^{k}y_j\), \(U_{-1}=0\), and \(d_j=U_j^p-U_{j-1}^p\ge0\). By Tonelli's theorem,
\[
\|L^na\|_{\operatorname{ces}_p}^p
=\sum_{j\ge0}d_jH_p(j+1),\qquad
\|a\|_{\operatorname{ces}_p}^p
=\sum_{j\ge0}d_jH_p(n+j+1).
\]
These identities hold in the extended nonnegative reals; here the right-hand denominator is finite. The strictly decreasing property of the ratios
\[
R_j=\frac{H_p(j+1)}{H_p(n+j+1)}
\]
shows that the quotient of these two sums does not exceed \(R_0\), with equality only when \(d_j=0\) for all \(j\ge1\). To verify strict decrease, use
\[
H_p(t)=\frac1{\Gamma(p)}\int_0^\infty
\frac{s^{p-1}e^{-ts}}{1-e^{-s}}\,ds.
\]
Strict Cauchy–Schwarz makes this moment sequence strictly log-convex, hence \(H_p(t+1)/H_p(t)\) strictly increases in \(t\), and \(R_{j+1}<R_j\). Equality requires \(y_j=0\) for \(j\ge1\). The vector supported at index \(n\) attains the displayed constant, completing the lemma.

**2. Exact reduction from the tree to levels.** Telescoping the level-balanced weights gives, for \(v\in D_k\),
\[
(B_\gamma^nf)(v)=\gamma^n\frac{c_k}{c_{k+n}}
\sum_{u\in\operatorname{Chi}^n(v)}f(u).
\]
As the descendant sets partition \(D_{k+n}\), the triangle inequality yields
\[
A_k(B_\gamma^nf)\le |\gamma|^n A_{k+n}(f).
\]
Apply the scalar lemma to the nonnegative sequence \((A_k(f))\):
\[
\|B_\gamma^nf\|\le |\gamma|^n
\left(\frac{H_p(1)}{H_p(n+1)}\right)^{1/p}\|f\|.
\]
Choose any nonzero \(f\) supported on \(D_n\), with all values aligned in phase. Then \(B_\gamma^nf\) is supported at the root and has modulus \(|\gamma|^n A_n(f)\) there. The input has norm \(A_n(f)H_p(n+1)^{1/p}\), and the output has norm \(|\gamma|^n A_n(f)H_p(1)^{1/p}\); the bound is attained.

Conversely, equality in the scalar lemma forces all level means \(A_k(f)\) to vanish except \(A_n(f)\), hence \(f\) is supported on \(D_n\). Equality in the sole remaining triangle inequality at the root forces its nonzero coefficients to share one complex phase. This proves the complete norm-attainment classification.

**3. Growth and dynamics.** Integral comparison gives
\[
H_p(n+1)=\frac{n^{1-p}}{p-1}(1+O_p(n^{-1})),
\]
which proves the asserted asymptotic, spectral radius, and operator-norm convergence when \(|\gamma|<1\).

Choose one child \(\chi(v)\) of each vertex, with choices made independently across parents. Define a right inverse \(S\) on finitely supported functions by
\[
(Sf)(\chi(v))=\frac{c_{|v|+1}}{\gamma c_{|v|}}f(v),
\]
and zero at vertices not selected. Then \(B_\gamma Sf=f\). For each vertex \(v\in D_m\),
\[
\|S^n e_v\|=\frac{|\gamma|^{-n}}{c_m}H_p(m+n+1)^{1/p}.
\]
Thus \(S^n f\to0\) for each finitely supported \(f\) whenever \(|\gamma|\ge1\). For finitely supported \(x,y\) and sufficiently large \(n\), \(B_\gamma^n x=0\), while \(B_\gamma^n(x+S^ny)=y\) and \(x+S^ny\to x\). Density of finitely supported vectors proves topological mixing.

If \(|\gamma|>1\), \(\sum_{n\ge0}\|S^nf\|<\infty\) for every finitely supported \(f\). Also \(\sum_{n\ge0}B_\gamma^n f\) is a finite sum and \(B_\gamma S f=f\). The standard Frequent Hypercyclicity Criterion [3,4] implies frequent hypercyclicity. For density of periodic points, take a finitely supported \(x\) and an integer \(q\) larger than its support depth. The convergent vector \(h_q=\sum_{j\ge0}S^{jq}x\) satisfies \(B_\gamma^q h_q=h_q\) and \(h_q\to x\) as \(q\to\infty\). Thus periodic points are dense and the shift is chaotic.

At \(|\gamma|=1\), suppose a frequently hypercyclic vector \(f\) existed. On a subset \(E\) of positive lower density its iterates would satisfy \(|(B_\gamma^n f)(o)-1|<1/2\), hence \(A_n(f)>1/2\). The Cesàro means of the nonnegative level sequence would then remain bounded below away from zero for all large indices, contradicting its \(\ell_p\)-summability. Finally, if \(0\ne f\) is periodic with period \(q\), choose a vertex \(v\in D_m\) with \(f(v)\ne0\). From \(f(v)=B_\gamma^{qj}f(v)\) one gets \(A_{m+qj}(f)\ge |f(v)|/c_m\) for every \(j\ge1\), contradicting the same Cesàro summability. Hence there are no nonzero periodic points at the critical modulus.

## Verification
All norm identities follow from explicit nonnegative series and a strict moment log-convexity inequality; no numerical experiment is needed for the infinite-dimensional argument. The accompanying script checks the scalar norm inequality on finite-support samples and the telescoping level-balanced tree formula on irregular finite-level examples. The checks are finite diagnostics, not proof of the infinite theorem. The argument applies separately to every \(p\in(1,\infty)\), without uniformity at either endpoint.

## Relationship to prior work
Chen–Cheng–Zhang–Zhou [1] introduce and analyze shifts on these level-mean Cesàro tree spaces, provide boundedness and dynamical criteria, and exhibit the constant-half-weight binary-tree shift as mixing but not frequently hypercyclic (Example 3.7). Those qualitative ingredients are prior work. The new quantitative statement is the branching-independent **exact norm of every power**, its complete norming-vector classification, and the resulting sharp critical polynomial amplification; the dynamical trichotomy organizes these quantitative findings for a canonical level-balanced family, rather than claiming the individual mixing/non-frequent binary example as new.

A related study of classical Cesàro sequence-space backward shifts [2] proves continuity and offers explicit upper and lower bounds for the single-step operator norm; these do not determine the present exact all-power profile on arbitrary rooted trees. Classical frequent-hypercyclicity criteria are used only as a stated external theorem [3,4]. The earlier construction of tree Cesàro spaces in [5] concerns multiplication operators, not the same weighted backward-shift family; its unavailable full text leaves a limited bibliographic risk rather than providing evidence of noncoverage.

## Limitations
The weights are explicitly level-balanced: arbitrary edge-dependent weights are not classified. The norms here use arithmetic level means of absolute values, not levelwise \(p\)-means or \(\ell_p\) graph norms. The theorem does not characterize invariant distributions, exact hypercyclic vectors, or the fine structure of arbitrary unbalanced tree shifts. Priority cannot be certified solely from searches; an equivalent earlier exact Cesàro shift-norm formula under different terminology remains possible. The frequent-hypercyclicity implication uses a classical criterion, not a newly proved criterion.

## References
[1] X. Chen, M.-H. Cheng, L. Zhang, Z.-H. Zhou, *Dynamics of Weighted Backward Shifts on Cesàro Spaces of Rooted Trees*, arXiv:2609.21752, first posted 18 September 2026; Section 2, Theorem 3.5, Example 3.7, Theorem 3.13. https://arxiv.org/abs/2609.21752

[2] *On the linear dynamics of shift operators on (PLB)-spaces*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales, Serie A: Matemáticas (2026), Section 4, Lemma 4.1 and Corollary 4.2. https://link.springer.com/article/10.1007/s13398-026-01935-0 (published 13 October 2026; postdates the primary source anchor).

[3] F. Bayart and S. Grivaux, *Frequently hypercyclic operators*, Transactions of the American Mathematical Society 358 (2006), 5083–5117, https://doi.org/10.1090/S0002-9947-06-04019-0.

[4] *A note on frequent hypercyclicity of operators that commute with the differentiation operator*, Journal of Mathematical Sciences (2022), Theorem 2.1 (explicit formulation of the standard Frequent Hypercyclicity Criterion). https://link.springer.com/article/10.1007/s10958-022-05989-4

[5] V. Kumar, M. Mursaleen, A. K. Sharma, *Multiplication operators on Cesàro function spaces on rooted trees*, Afrika Matematika 36 (2025), article 156, https://doi.org/10.1007/s13370-025-01369-8.
