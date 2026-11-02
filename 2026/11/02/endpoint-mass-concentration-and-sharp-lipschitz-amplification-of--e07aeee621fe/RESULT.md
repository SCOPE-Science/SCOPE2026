# Endpoint-mass concentration and sharp Lipschitz amplification of discrete interval maximal averages

## Finding

For every integer \(n\ge2\) and positive numbers \(a,b\), put \(w^{(\varepsilon)}=(a,\varepsilon,\ldots,\varepsilon,b)\), with \(n-2\) interior masses and \(\varepsilon>0\). For the weighted uncentered interval maximal operator \(\mathcal M_w\) on the ordered path \(\{1,\ldots,n\}\), define its sharp Lipschitz-seminorm gain \(K_n(w)\) as below. Then

\[
\boxed{\lim_{\varepsilon\downarrow0}K_n(w^{(\varepsilon)})=(n-1)\frac{\max\{a,b\}}{a+b}.}
\]

In fact, for all \(\varepsilon>0\),

\[
\boxed{\left|K_n(w^{(\varepsilon)})-(n-1)\frac{\max\{a,b\}}{a+b}\right|\le\frac{2(n-1)(n-2)\varepsilon}{\min\{a,b\}}.}
\]

Both limiting branches have explicit one-Lipschitz witnesses: the increasing and decreasing affine ramps. Consequently, for every \(n\ge2\),

\[
\boxed{\sup_{w\in(0,\infty)^n}K_n(w)=n-1,\qquad K_n(w)<n-1\text{ for every fixed positive }w.}
\]

By contrast, for equal positive vertex masses on any such path, the exact constant is \(K_n(1,\ldots,1)=1/2\). Therefore imposing no control on vertex-mass imbalance changes the sharp amplification scale from a fixed contraction factor to linear growth with path length.

## Assumptions and scope

The vertex set is \(V_n=\{1,\ldots,n\}\) with consecutive unit edges. For positive masses \(w_1,\ldots,w_n\), define, on real inputs \(f\),

\[
(\mathcal M_wf)(i)=\max_{1\le u\le i\le v\le n}
\frac{\sum_{j=u}^v w_j|f_j|}{\sum_{j=u}^v w_j},\qquad
\operatorname{Lip}(f)=\max_{1\le i<n}|f_{i+1}-f_i|,
\]

and

\[
K_n(w)=\sup_{\operatorname{Lip}(f)>0}\frac{\operatorname{Lip}(\mathcal M_wf)}{\operatorname{Lip}(f)}.
\]

All contiguous nonempty intervals containing the evaluated vertex are admitted; no restriction to graph balls centered at vertices is imposed. Nonnegative data suffice, since \(\operatorname{Lip}(|f|)\le\operatorname{Lip}(f)\), and taking the modulus does not change \(\mathcal M_wf\). On nonnegative inputs the operator commutes with adding a nonnegative constant, and equivalently one can optimize raw (non-modulus) interval averages over all real inputs by a large positive translation. The parameter \(\varepsilon\) approaches zero through strictly positive values; the limit operator is defined by limiting interval averages, not by treating zero-mass interior intervals as ordinary probability averages.

## Proof

**1. The limiting interval operator.** Let \(T_{\varepsilon}\) denote the maximum of raw weighted interval averages with the specified masses. For each interval consisting entirely of interior vertices, its average is the usual arithmetic mean for every \(\varepsilon>0\). For an interval containing exactly one endpoint, its average tends to the value at that endpoint. An interval containing both endpoints necessarily is \([1,n]\), and its average tends to \(\bar f=(af_1+bf_n)/(a+b)\).

For \(n\ge3\), let \(U\) be the ordinary uncentered interval maximal operator on the interior subpath \(\{2,\ldots,n-1\}\), using raw averages. Pointwise the limit \(T_0\) is therefore

\[
\begin{aligned}
(T_0f)(1)&=\max\{f_1,\bar f\},\\
(T_0f)(i)&=\max\{f_1,f_n,(Uf)(i)\},\quad2\le i\le n-1,\\
(T_0f)(n)&=\max\{f_n,\bar f\}.
\end{aligned}
\]

For \(n=2\) the formula comprises only the two endpoint expressions, without an interior path.

**2. Interior half-contraction.** Suppose \(\operatorname{Lip}(f)\le1\). Consider adjacent interior indices \(i,i+1\). Every interval containing \(i\) either also contains \(i+1\), in which case the same average is available at both, or is \([u,i]\). In the latter case extend it to \([u,i+1]\); with \(k=i-u+1\),

\[
\frac1k\sum_{j=u}^{i}f_j-\frac1{k+1}\sum_{j=u}^{i+1}f_j
=\frac{\frac1k\sum_{j=u}^{i}f_j-f_{i+1}}{k+1}
\le\frac{(k+1)/2}{k+1}=\frac12.
\]

The reversed inequality follows by reflecting the path. Taking maxima yields \(\operatorname{Lip}(Uf)\le1/2\). Adding the same two constant competitors \(f_1,f_n\) to both neighboring maxima cannot increase their difference, so the interior Lipschitz gain of \(T_0\) is at most \(1/2\).

**3. Boundary edges.** Write \(A=\max\{f_1,\bar f\}\). Since \(\bar f\) lies between \(f_1,f_n\), the second output \((T_0f)(2)\) is at least \(A\). Also, any interior interval containing vertex \(2\) is \([2,v]\), where \(2\le v\le n-1\). By \(f_j-f_1\le j-1\),

\[
(Uf)(2)-f_1\le\max_{2\le v\le n-1}\frac{1+\cdots+(v-1)}{v-1}=\frac{n-1}{2}.
\]

Moreover, \(f_n-A\le\frac a{a+b}(f_n-f_1)_+\le\frac{a(n-1)}{a+b}\). Thus

\[
0\le (T_0f)(2)-(T_0f)(1)
\le\max\left\{\frac{n-1}{2},\frac{a(n-1)}{a+b}\right\}.
\]

Reflection gives

\[
0\le (T_0f)(n-1)-(T_0f)(n)
\le\max\left\{\frac{n-1}{2},\frac{b(n-1)}{a+b}\right\}.
\]

The larger of \(a/(a+b)\) and \(b/(a+b)\) is at least \(1/2\). Combining the two boundary estimates with the interior half-contraction proves \(\operatorname{Lip}(T_0f)\le R\operatorname{Lip}(f)\), where \(R=(n-1)\max\{a,b\}/(a+b)\). For \(n=2\), the two endpoint maxima directly yield the same bound.

**4. Attainment in the limit.** Set \(f_j=j-1\). All input values are at most \(n-1\), and \(T_0f(2)=n-1\), while \(T_0f(1)=b(n-1)/(a+b)\). Hence the first output edge has jump \(a(n-1)/(a+b)\). On the decreasing ramp \(f_j=n-j\), the final edge has jump \(b(n-1)/(a+b)\). One ramp attains the upper bound \(R\). For \(n=2\) use its unique edge. This proves the exact limiting norm without relying on experiments.

**5. Uniform error for positive interior masses.** After normalizing \(\operatorname{Lip}(f)\le1\), the range of \(f\) is at most \(n-1\). For intervals containing an endpoint, the limiting endpoint-weight sum is at least \(\min\{a,b\}\). Writing an interval's \(\varepsilon\)-average as the convex mixture of its endpoint-only average and its interior average gives an absolute difference at most

\[
\delta=\frac{(n-1)(n-2)\varepsilon}{\min\{a,b\}}.
\]

On interior-only intervals the difference is zero. Hence \(\|T_{\varepsilon}f-T_0f\|_\infty\le\delta\), and therefore \(\left|\operatorname{Lip}(T_{\varepsilon}f)-\operatorname{Lip}(T_0f)\right|\le2\delta\). Both operators are translation equivariant on raw averages, so the normalized suprema over inputs obey \(|K_n(w^{(\varepsilon)})-R|\le2\delta\). This proves convergence and the asserted rate.

**6. Sharp global mass effect and the equal-mass baseline.** For any fixed positive masses and nonconstant nonnegative input, every maximal output is at least the strictly intermediate whole-path average, while all outputs are at most \(\max_j f_j\). Consequently \(\operatorname{Lip}(\mathcal M_wf)<\max f-\min f\le(n-1)\operatorname{Lip}(f)\). Modulo constants, the unit Lipschitz sphere is compact and the gain is continuous; therefore \(K_n(w)<n-1\) for every fixed positive mass vector. Yet letting \(\varepsilon\downarrow0\) and then \(a/b\downarrow0\) (or symmetrically) makes the exact limiting ratio tend to \(n-1\), giving the unattained weight-uniform supremum.

For equal vertex masses, the interval-extension comparison in Step 2 works on the entire path, proving gain at most \(1/2\). The single-endpoint spike \(f=(1,0,\ldots,0)\) gives adjacent outputs \(1\) and \(1/2\), with input Lipschitz seminorm \(1\), proving sharpness.

## Verification

The included standalone script `verification/check_weighted_maximal.py` uses exact rational arithmetic to compare the limiting operator, positive-\(\varepsilon\) interval averages, both affine ramps, the equal-mass half bound, and the explicit perturbation estimate. Run `python verification/check_weighted_maximal.py` after extracting the files. It passed 17,682 finite exact-rational assertions. The finite tests verify examples and the rate but do not replace the all-\(n\) analytic argument above.

## Relationship to prior work

Aldaz, Colzani and Pérez Lázaro (arXiv:1009.1359, initially made public 2010-09-07), Theorem 4.3 and Corollary 4.5, obtain sharp Lipschitz half-contraction for the uncentered operator over Lebesgue intervals. That result uses translation-invariant measure and does not cover positive but strongly nonuniform discrete vertex masses. Bober, Carneiro, Hughes and Pierce (arXiv:1005.3030, initially public 2010-05-17), Theorem 1, establish a sharp total-variation inequality for the counting-measure noncentered discrete operator on the integers; this does not imply our weighted \(\ell^\infty\)-gradient profile. Grafakos and Kinnunen analyze sharp weak-type and \(L^p\) constants for arbitrary Borel measures, not Lipschitz-seminorm growth. Buckley studies modulus preservation under annular-decay assumptions and qualitative counterexamples in other metric-measure settings, without the present exact two-endpoint finite-path limit.

The formula is claimed for this precise weighted finite-path Lipschitz seminorm, not for maximal operators in general. Equivalent work in unindexed discrete weighted-maximal literature remains possible.

## Limitations

The theorem uses one-dimensional ordered contiguous intervals, uncentered averaging, one-step path Lipschitz seminorm, and two distinguished endpoint weights with equal vanishing interior masses. It gives a sharp \(\varepsilon\to0\) profile and a quantitative error bound, but not a closed formula for every positive \(\varepsilon\) or every arbitrary positive mass vector. The limiting formal operator is not the usual maximal operator with zero-mass interior vertices. The supremum \(n-1\) is over varying strictly positive measures and is not attained at any fixed such measure. Publication priority is qualified by possible inaccessible or unindexed equivalent calculations.

## References

1. S. M. Buckley, *Is the maximal function of a Lipschitz function continuous?*, Ann. Acad. Sci. Fenn. Math. **24** (1999), 519–528. Public repository deposit 2009-10-21, https://mural.maynoothuniversity.ie/1613/ .
2. J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1 (2010-05-17), Proc. Amer. Math. Soc. **140** (2012), 1669–1680, https://arxiv.org/abs/1005.3030 .
3. J. M. Aldaz, L. Colzani, J. Pérez Lázaro, *Optimal bounds on the modulus of continuity of the uncentered Hardy-Littlewood maximal function*, arXiv:1009.1359v1 (2010-09-07), https://arxiv.org/abs/1009.1359 .
4. L. Grafakos and J. Kinnunen, *Sharp inequalities for maximal functions associated with general measures*, publicly available author preprint, https://grafakos.missouri.edu/preprints/kinnunen.pdf .
