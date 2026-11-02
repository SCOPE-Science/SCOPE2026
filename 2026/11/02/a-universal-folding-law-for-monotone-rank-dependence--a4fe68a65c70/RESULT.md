# A universal folding law for monotone rank dependence

## Finding

Let \(C\) be **any** bivariate copula, \(\Pi(u,v)=uv\), and let \(k\ge1\) be an integer. Define its \(k\)-fold predictor lift by
\[
(\mathcal F_k C)(u,v)=\frac{jv+C(ku-j,v)}{k},\qquad
\frac{j}{k}\le u\le\frac{j+1}{k},\quad j=0,\ldots,k-1.
\]
The two expressions at adjoining cell boundaries agree. Write \(\xi\) for population Chatterjee rank correlation, \(\xi^{\uparrow}\) and \(\xi^{\downarrow}\) for the increasing and decreasing projected components introduced by Siburg, and \(\rho_S\) for Spearman's rho. Then, **simultaneously for every copula \(C\)**,
\[
\boxed{\begin{aligned}
\xi(\mathcal F_k C)&=\xi(C),\\
\xi^{\uparrow}(\mathcal F_k C)&=\frac{\xi^{\uparrow}(C)}{k},\\
\xi^{\downarrow}(\mathcal F_k C)&=\frac{\xi^{\downarrow}(C)}{k},\\
\rho_S(\mathcal F_k C)&=\frac{\rho_S(C)}{k}.
\end{aligned}}
\]
Moreover,
\[
\boxed{\|\mathcal F_k C-\Pi\|_\infty\le\frac1{4k},}
\]
and the constant is attained for the comonotone copula \(C(u,v)=\min(u,v)\). The residual non-monotone component therefore obeys
\[
\xi^{\circ}(\mathcal F_k C)=\xi(C)-\frac{\xi^{\uparrow}(C)+\xi^{\downarrow}(C)}{k}.
\]
Thus every fixed dependence law can be made uniformly close to independence while retaining exactly the same full Chatterjee dependence: its two directional monotone components decay at the **exact universal factor** \(1/k\).

## Assumptions and scope

No smoothness, density, symmetry, or moment condition is imposed on \(C\). All assertions concern population copula functionals with uniform continuous coordinate marginals. The operation \(\mathcal F_k\) introduces an independent uniformly chosen branch of the predictor: if \((U,V)\) has copula \(C\) and \(J\) is uniform on \(\{0,\ldots,k-1\}\), independent of \((U,V)\), then the pair \(((J+U)/k,V)\) has copula \(\mathcal F_k C\). It does not fold the response coordinate.

For almost every \((u,v)\), the coefficients can be defined without differentiating \(C\) classically:
\[
\begin{split}
\xi(C)&=6\int_0^1\!\int_0^1[\partial_1C(u,v)-v]^2\,du\,dv,\\
\xi^{\uparrow}(C)&=6\int_0^1\!\int_0^1[\partial_1\widehat{C(\cdot,v)}(u)-v]^2\,du\,dv,\\
\xi^{\downarrow}(C)&=\xi^{\uparrow}(C^-),\qquad C^-(u,v)=v-C(1-u,v),\\
\rho_S(C)&=12\int_0^1\!\int_0^1[C(u,v)-uv] \,du\,dv.
\end{split}
\]
Here the hat denotes the least concave majorant on \([0,1]\), and derivatives exist almost everywhere because copula sections are Lipschitz. The displayed definitions of the two projected parts use the source's projection theorem; their provenance is explicitly acknowledged below.

## Proof

**1. Copula construction and full dependence.** The random-branch construction proves \(\mathcal F_k C\) is a copula. On the interior of its \(j\)-th predictor cell,
\[
\partial_1(\mathcal F_k C)(u,v)=\partial_1 C(ku-j,v).
\]
Integration over the \(k\) cells immediately gives \(\xi(\mathcal F_k C)=\xi(C)\).

**2. The repeated-envelope lemma.** Let \(F:[0,1]\to\mathbb R\) be Lipschitz with \(F(0)=F(1)=0\), and put \(F_k(t)=F(kt-\lfloor kt\rfloor)\), with the continuous endpoint interpretation. Let \(H\) and \(H_k\) be the respective least concave majorants. Then
\[
\boxed{\int_0^1|H_k'(t)|^2\,dt
 =k\int_0^1|H'(t)|^2\,dt.}
\]
To prove it, let \(M=\max_{[0,1]}F\), necessarily \(M\ge0\). If \(M=0\), both majorants are the zero chord. Otherwise, let \(a\) and \(b\) be the first and last maximizers of \(F\). Since the constant function \(M\) is a concave majorant and the least majorant touches \(F\) at \(a,b\), \(H=M\) on \([a,b]\). Concavity forces \(H\) to be nondecreasing before \(a\) and nonincreasing after \(b\).

The least concave majorant of the \(k\)-fold repeated graph is **exactly**
\[
H_k(t)=\begin{cases}
H(kt),&0\le t\le a/k,\\
M,&a/k\le t\le(k-1+b)/k,\\
H(kt-k+1),&(k-1+b)/k\le t\le1.
\end{cases}
\]
Indeed, this function is concave and dominates each repeated cell: the first and last pieces dominate their corresponding fragments of \(F\), and the middle constant dominates the remaining fragments. To establish minimality, any concave majorant of \(F_k\) is at least \(M\) at the earliest and latest repeated maxima and hence throughout the intervening interval. On the first fragment, its restriction is a concave majorant of \(F\) on \([0,a]\), where \(H\) is the least concave majorant; the analogous statement holds on \([b,1]\). The latter restriction facts follow by grafting their local least concave majorants to the plateau \(M\) and the opposite tail: the local envelopes end at their maximal endpoint and have the needed monotone slopes. Thus every concave majorant dominates the displayed piecewise function. Differentiation on the two edge fragments yields the boxed integral identity; the plateau has zero derivative. The identity is valid also for \(k=1\).

**3. Increasing dependence.** For fixed \(v\), apply the lemma to
\[
F_v(t)=C(t,v)-tv,\qquad F_v(0)=F_v(1)=0.
\]
Because addition of an affine function commutes with taking least concave majorants, and
\[
(\mathcal F_k C)(u,v)=uv+\frac1kF_{v,k}(u),
\]
the centered derivative of the least concave majorant of the new section is \(H_{v,k}'(u)/k\), where \(H_v=\widehat{F_v}\). Hence
\[
\begin{split}
\xi^{\uparrow}(\mathcal F_k C)
&=\frac6{k^2}\int_0^1\!\int_0^1|H_{v,k}'(u)|^2\,du\,dv\\
&=\frac6k\int_0^1\!\int_0^1|H_v'(u)|^2\,du\,dv
=\frac{\xi^{\uparrow}(C)}k.
\end{split}
\]
All sectionwise terms are bounded, so integration over \(v\) is justified.

**4. Decreasing dependence.** Reflection commutes with folding:
\[
(\mathcal F_k C)^-=\mathcal F_k(C^-).
\]
This follows directly from the formula on each cell (the reflected cell index becomes \(k-1-j\)); continuity handles grid endpoints. Apply step 3 to \(C^-\).

**5. Concordance, sharpness, and residual.** The deviation \((\mathcal F_k C)(u,v)-uv\) equals \(F_v(ku-\lfloor ku\rfloor)/k\). Integrating the repeated section gives \(\rho_S(\mathcal F_k C)=\rho_S(C)/k\). Fréchet bounds \(\max(u+v-1,0)\le C(u,v)\le\min(u,v)\) imply \(|C(u,v)-uv|\le1/4\), giving the displayed uniform bound; equality is realized by \(C=\min(u,v)\) at predictor phase \(1/2\) and response level \(1/2\). Finally substitute the three proved coefficient laws into the definition \(\xi^{\circ}=\xi-\xi^{\uparrow}-\xi^{\downarrow}\).

## Verification

A standalone exact-rational checker, \`verify.py\`, computes non-increasing least-squares projections by pooled adjacent violators and exhaustively tests every nonzero centered integer step profile of lengths two through six with entries from \(\{-2,-1,0,1,2\}\), under three independent fold factors. It also checks explicit Farlie–Gumbel–Morgenstern and upper Fréchet examples, including nonnegative residuals. Running \`python3 verify.py\` produces \`verification_output.txt\`. The checker passed 13,796 assertions. The continuum proof is steps 1–5 above, not the finite tests.

For example, the positive-parameter Farlie–Gumbel–Morgenstern copula \(C_\theta(u,v)=uv[1+\theta(1-u)(1-v)]\), \(0<\theta\le1\), is absolutely continuous and satisfies
\[
\xi(\mathcal F_k C_\theta)=\frac{\theta^2}{15},\qquad
\xi^{\uparrow}(\mathcal F_k C_\theta)=\frac{\theta^2}{15k},\qquad
\xi^{\downarrow}(\mathcal F_k C_\theta)=0.
\]
Thus the attenuation is not confined to singular or deterministic copulas.

## Relationship to prior work

Siburg's *The monotone part of Chatterjee's rank correlation* (arXiv:2610.35340v1, first public October 26, 2026) establishes the general least-concave-majorant projection and the three-part dependence decomposition. Its Example 5.4 proves \(\xi^{\uparrow}=1/k\) for the special sawtooth copula generated by a deterministic \(k\)-fold map of a uniform predictor. This result uses that framework, but proves a **general arbitrary-copula lifting law**, with a new repeated-envelope identity and both directed components. It does not claim to have introduced \(\xi^{\uparrow}\), the concave-majorant projection, or the sawtooth special case.

Ansari's *On a copula product characterizing independence and perfect functional dependence* (arXiv:2604.09950, first public April 10, 2026, primary MSC 60E15) motivates the study of transformations of copulas that separate functional predictive dependence from monotone concordance. It concerns upper products and increasing rearrangements, however, not the repeated-envelope metric projection. The present branch-lifting problem is a distinct natural dependence-preserving copula transformation. Standard isotonic-regression results underpin the least-concave-majorant method. The present statement was compared against these full-text sources and available published mathematical-record summaries, but independent historical-priority review remains necessary.

## Limitations

The exact identity applies to integer numbers of **equal-length, independent** predictor branches and to the specific increasing/decreasing projected components. It is not asserted for nonuniform branch lengths, arbitrary reparametrizations, or empirical finite-sample estimators. The fold may be singular even when the base copula is singular; smoothness is not preserved at cell boundaries. The result proves population identities only. Its scientific review is not an independent validation or a guarantee of global historical novelty.

## References

1. J. Ansari, *On a copula product characterizing independence and perfect functional dependence*, arXiv:2604.09950, first public April 10, 2026, primary MSC 60E15; https://arxiv.org/html/2604.09950v2, Sections 1, 3 and 6 (v2 revised August 26, 2026).
2. K. F. Siburg, *The monotone part of Chatterjee's rank correlation*, arXiv:2610.35340v1, first public October 26, 2026, https://arxiv.org/html/2610.35340v1, particularly Sections 3–5 and Example 5.4 (later supporting framework, not the date-owning source).
3. S. Chatterjee, *A new coefficient of correlation*, Journal of the American Statistical Association 116 (2021), 2009–2022; definition of the population correlation.
4. R. E. Barlow et al., *Statistical Inference under Order Restrictions* (1972); classical isotonic regression and least-concave-majorant principles (background only).
