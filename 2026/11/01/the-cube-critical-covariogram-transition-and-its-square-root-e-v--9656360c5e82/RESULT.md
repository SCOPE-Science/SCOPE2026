# The cube critical covariogram transition and its square-root-e volume anomaly

## Finding

Let \(C_n=[-1/2,1/2]^n\), where \(n\ge2\), and form the smooth radial-mean covariogram \(g_{n,p}\) defined below. At the critical volume deficit \(1/p\), its rescaled level set converges in Hausdorff distance to the explicit Orlicz body
\[
\mathcal T_n=\left\{y\in\mathbb R^n:\sum_{i=1}^n\log\cosh y_i\le1\right\}.
\]
Set \(B_n=\{y:\sum_i y_i^2\le2\}\) and \(R_n=\operatorname{vol}_n(\mathcal T_n)/\operatorname{vol}_n(B_n)\). Let \((T_1,\dots,T_n,S)\) have the Dirichlet distribution with parameters \((1/2,\dots,1/2,1)\), supported on \(T_i\ge0\) and \(S=1-\sum_iT_i\ge0\). Then an exact finite-dimensional identity is
\[
R_n=\mathbb E\prod_{i=1}^n\left(\frac{2T_i}{1-e^{-2T_i}}\right)^{1/2},
\]
where the factor at \(T_i=0\) is defined by continuity as \(1\). In particular, for every \(n\ge2\),
\[
1<R_n<\sqrt e,
\]
and, as \(n\to\infty\),
\[
\boxed{R_n=\sqrt e\left(1-\frac5{4n}+O(n^{-2})\right).}
\]
This exhibits a nontrivial limiting multiplicative volume anomaly although the defining function \(\log\cosh t\) has quadratic expansion at the origin. The limit theorem here applies directly to the nonsmooth cube; the recent general smooth-boundary critical-transition theorem does not assume polytopes.

## Assumptions and scope

Fix \(n\ge2\). For a star body \(K\) containing the origin write its radial function as \(\rho_K(v)=\sup\{r\ge0:rv\in K\}\), for \(v\in S^{n-1}\). For \(p>0\) and \(x\in(-1/2,1/2)^n\), define the star body \(M_{x,p}\) by
\[
\rho_{M_{x,p}}(v)^{-p}=\tfrac12\big(\rho_{C_n}(v)^{-p}+\rho_{C_n+x}(v)^{-p}\big).
\]
Set \(g_{n,p}(x)=\operatorname{vol}_n(M_{x,p})\) and
\[
L_{n,p}=\big\{x\in(-1/2,1/2)^n:1-g_{n,p}(x)\le p^{-1}\big\}.
\]
The Hausdorff limit concerns \(pL_{n,p}=\{px:x\in L_{n,p}\}\) as \(p\to\infty\) with dimension \(n\) fixed. The volume asymptotic concerns the independently defined limiting bodies \(\mathcal T_n\) as \(n\to\infty\). These two limits are not asserted to commute uniformly in \(n,p\).

## Proof

**1. The facetwise critical limit.** For a unit vector \(v\), let \(m(v)=\max_i|v_i|\). Then \(\rho_{C_n}(v)=1/(2m(v))\), while for \(x\in(-1/2,1/2)^n\),
\[
\rho_{C_n+x}(v)=\min_{i:v_i\ne0}\frac{1/2+\operatorname{sgn}(v_i)x_i}{|v_i|}.
\]
At every \(v\) with a unique maximizing coordinate \(j\), and for each bounded \(y\), this minimum, for all sufficiently large \(p\), is attained at \(j\) when \(x=y/p\). Thus
\[
\frac{\rho_{C_n+y/p}(v)}{\rho_{C_n}(v)}=1+\frac{2\operatorname{sgn}(v_j)y_j}{p}.
\]
The excluded tie directions have spherical measure zero. Substitution into the polar volume formula gives, pointwise at such directions,
\[
\begin{aligned}
&\frac p n\left[\rho_{C_n}(v)^n-\rho_{M_{y/p,p}}(v)^n\right]\\
&\quad\longrightarrow\rho_{C_n}(v)^n\log\frac{1+e^{-2\operatorname{sgn}(v_j)y_j}}2.
\end{aligned}
\]
For \(y\) in a fixed compact set, the radial ratio differs from \(1\) by at most \(O(1/p)\), uniformly in \(v\). This bounds the displayed integrand uniformly and allows dominated convergence, including uniform convergence over compact sets of \(y\). Each of the \(2n\) sets of directions hitting one facet of \(C_n\) has radial integral \(\int\rho_{C_n}(v)^n\,d\sigma(v)=1/2\), by the cone-volume identity \(\operatorname{vol}(\operatorname{cone}(0,F))=(1/n)(1/2)\operatorname{area}_{n-1}(F)=1/(2n)\). Since
\[
\log\frac{1+e^{-2s}}2=\log\cosh s-s,
\]
the opposite-facet terms cancel the odd part. Consequently, locally uniformly on \(\mathbb R^n\),
\[
F_p(y):=p[1-g_{n,p}(y/p)]\longrightarrow\Phi_n(y):=\sum_{i=1}^n\log\cosh y_i.
\]
The local formula is valid for all \(y\) with \(y/p\) in the domain.

**2. Global Hausdorff convergence.** A radial negative power mean satisfies \(\rho_{M_{x,p}}\le 2^{1/p}\min(\rho_{C_n},\rho_{C_n+x})\). It follows that
\[
g_{n,p}(x)\le2^{n/p}\operatorname{vol}(C_n\cap(C_n+x))=2^{n/p}\prod_{i=1}^n(1-|x_i|)
\]
for \(|x_i|<1/2\). If \(x=y/p\in L_{n,p}\), then \(g_{n,p}(x)\ge1-1/p\), whence, for every \(i\),
\[
\frac{|y_i|}{p}\le1-(1-p^{-1})2^{-n/p}.
\]
For fixed \(n\), these bounds place every \(pL_{n,p}\) inside a single compact cube for large \(p\). Uniform convergence of \(F_p\) on that cube implies sandwiching between the sublevel sets \(\{\Phi_n\le1-\varepsilon\}\) and \(\{\Phi_n\le1+\varepsilon\}\), for arbitrary small \(\varepsilon>0\). Since \(\Phi_n\) is continuous, proper, and strictly increasing along every nonzero ray, these sublevel sets approach \(\mathcal T_n\) in Hausdorff metric as \(\varepsilon\downarrow0\). This proves the first assertion.

**3. An exact Dirichlet integral for volume.** Use coordinate signs and the transformation \(t_i=\log\cosh|y_i|\). As \(\frac{d}{dt}\operatorname{arcosh}(e^t)=(1-e^{-2t})^{-1/2}\),
\[
\operatorname{vol}_n(\mathcal T_n)
=2^n\int_{\sum t_i\le1}\prod_{i=1}^n(1-e^{-2t_i})^{-1/2}\,dt_1\cdots dt_n.
\]
For the ball \(B_n\) the parallel substitution \(t_i=y_i^2/2\) yields
\[
\operatorname{vol}_n(B_n)=2^{n/2}\int_{\sum t_i\le1}\prod_i t_i^{-1/2}\,dt
=\frac{(2\pi)^{n/2}}{\Gamma(n/2+1)}.
\]
Dividing gives the stated Dirichlet expectation with \(G(t)=\sqrt{2t/(1-e^{-2t})}\).

**4. Sharp nonasymptotic bounds.** For \(t>0\), \(1-e^{-2t}<2t\), so \(G(t)>1\). The identity \(G(t)=e^{t/2}\sqrt{t/\sinh t}\) and \(\sinh t>t\) imply \(G(t)<e^{t/2}\). The Dirichlet slack variable \(S>0\) almost surely, hence \(\sum_iT_i=1-S<1\); multiplying inequalities and taking expectations proves \(1<R_n<\sqrt e\).

**5. First finite-size correction.** For \(0\le t\le1\), with an absolute uniform remainder,
\[
\log G(t)=\frac t2+\frac12\log\frac t{\sinh t}=\frac t2-\frac{t^2}{12}+O(t^4).
\]
Writing \(S=1-\sum_iT_i\), we obtain
\[
\prod_iG(T_i)=\sqrt e\exp\left(-\frac S2-\frac1{12}\sum_iT_i^2+O\big(\sum_iT_i^4\big)\right).
\]
For the above Dirichlet law the beta/gamma moment formulas give
\[
\begin{gathered}
\mathbb ES=\frac2{n+2},\qquad \mathbb E\sum_iT_i^2=\frac{3n}{(n+2)(n+4)},\\
\mathbb ES^2=O(n^{-2}),\quad \mathbb E(\sum_iT_i^2)^2=O(n^{-2}),\quad \mathbb E\sum_iT_i^4=O(n^{-3}).
\end{gathered}
\]
Because the exponent is nonpositive, and its squared expectation is \(O(n^{-2})\), expansion of the exponential under the expectation is justified with a uniform \(O(n^{-2})\) mean error. Therefore
\[
\begin{aligned}
R_n&=\sqrt e\left[1-\frac1{n+2}-\frac n{4(n+2)(n+4)}+O(n^{-2})\right]\\
&=\sqrt e\left[1-\frac5{4n}+O(n^{-2})\right],
\end{aligned}
\]
which completes the proof.

## Verification

The accompanying standard-library script `verify.py` tests the exact Dirichlet-moment identities for dimensions \(1\) through \(500\), compares direct angular quadrature of the two-dimensional radial-mean deficit with the limiting \(\log\cosh\) expression, compares an independent planar-volume quadrature with the Dirichlet prediction, and performs seeded Monte Carlo sanity checks through dimension \(400\). The completed run satisfied \(1015\) deterministic assertions. These finite computations are diagnostics, not proofs of the Hausdorff limit, strict bounds, or the high-dimensional asymptotic; those are proved analytically above.

## Relationship to prior work

Haddad, Jiménez and Resende (2026), Theorem 5, introduced the smooth radial-mean covariogram and proved a critical \(\log\cosh\) transition for convex bodies with \(C^3\) boundaries. That theorem's smoothness hypothesis does not cover cubes, and the paper does not give the dimension-dependent cube volumes. The cube statement above is established directly, not by invoking that smooth theorem beyond its hypotheses.

The Orlicz-ball asymptotic theories of Kabluchko–Prochno, Barthe–Wolff, and Sadok analyze energy thresholds proportional to dimension or corresponding exponential volume rates. Their respective general results do not supply the fixed total energy \(1\) exact Dirichlet identity and its normalized second-order coefficient. These works motivate, but do not by themselves imply, the asserted volume anomaly. Potential historical equivalents in unindexed literature cannot be ruled out.

## Limitations

The critical-level Hausdorff convergence is proved with \(n\) fixed; no error rate uniform over growing \(n\) or joint \((n,p)\)-limit is claimed. The ratio bounds and asymptotic concern the log-cosh transition body only; they do not establish extremality among arbitrary Orlicz or convex bodies. The ratio asymptotic has an \(O(n^{-2})\) remainder without its next coefficient. The numerical verification does not constitute independent formal validation, and historical priority is not certified.

## References

1. J. Haddad, C. H. Jiménez, M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, 8 October 2026, https://arxiv.org/html/2610.11700v1.
2. M. Sadok, *Exponential profiles for the intrinsic volumes of Orlicz balls*, arXiv:2610.16904v1, 12 October 2026, https://arxiv.org/html/2610.16904v1.
3. F. Barthe, P. Wolff, *Volume properties of high-dimensional Orlicz balls*, arXiv:2106.01675, https://arxiv.org/html/2106.01675v2.
4. Z. Kabluchko, J. Prochno, *The maximum entropy principle and volumetric properties of Orlicz balls*, arXiv:2007.05247, https://arxiv.org/abs/2007.05247.
