# A universal marked large-circumradius law for three random points in a convex body

## Finding

Let \(K\subset\mathbb R^2\) be any compact convex set with nonempty interior, area \(A\), and let \(X_1,X_2,X_3\) be independent uniform points in \(K\). Write \(\mathcal R\) for their (almost surely finite) triangle circumradius. Parameterize unoriented affine lines by \(\theta\in[0,\pi)\) and \(p\in\mathbb R\), with unit normal \(n_\theta=(\cos\theta,\sin\theta)\), tangent \(e_\theta=(-\sin\theta,\cos\theta)\), and line \(\{p n_\theta+s e_\theta:s\in\mathbb R\}\). Let \(\ell_K(\theta,p)\) be the length of the chord cut out by \(K\); it is zero for a missing or degenerate chord. Define
\[
Q_6(K)=\int_0^\pi\!\int_{\mathbb R}\ell_K(\theta,p)^6\,dp\,d\theta.
\]
Then \(Q_6(K)>0\) and
\[
\boxed{\lim_{T\to\infty}T\Pr(\mathcal R>T)=\frac{Q_6(K)}{30A^3}.}
\]
More importantly, the *entire marked near-collinearity configuration* has a universal limit. Given the event \(\mathcal R>T\), let \((\Theta_T,P_T)\) be the unoriented line through \(X_1,X_2\), expressed in the above coordinates. Write \(s_i=e_{\Theta_T}\cdot X_i\), let \(a_T<b_T\) be the scalar endpoints of the corresponding chord of \(K\), and put \(\ell_T=b_T-a_T\). Let \(s_{(1)}\le s_{(2)}\le s_{(3)}\) be the sorted scalar projections and form four normalized gaps
\[
G_T=\frac1{\ell_T}\bigl(s_{(1)}-a_T,\ s_{(2)}-s_{(1)},\ s_{(3)}-s_{(2)},\ b_T-s_{(3)}\bigr).
\]
Finally set \(h_T=n_{\Theta_T}\cdot(X_3-X_1)\) and
\[
U_T=\frac{2T h_T}{|s_3-s_1|\,|s_3-s_2|}
\]
(the denominator is nonzero almost surely). As \(T\to\infty\), conditionally on \(\mathcal R>T\),
\[
(\Theta_T,P_T,G_T,U_T)\ \Longrightarrow\ (\Theta,P,G,U),
\]
where the four limiting components have **independent blocks**: the line \((\Theta,P)\) has density \(\ell_K(\theta,p)^6/Q_6(K)\) with respect to \(d\theta\,dp\); \(U\) is uniform on \([-1,1]\); and \(G\) has the equal-weight mixture
\[
\boxed{\frac12\operatorname{Dirichlet}(1,3,2,1)
+\frac12\operatorname{Dirichlet}(1,2,3,1).}
\]
(The six label permutations of the sorted points are independently uniform.) This gap law and the transverse-uniform law do not depend on \(K\); the shape is remembered only by the sixth-power chord-biased line distribution.

For a disk of radius \(a>0\), the direction is uniform, the normalized signed offset \((P/a+1)/2\) has the \(\operatorname{Beta}(4,4)\) distribution, and the leading tail is
\[
\Pr(\mathcal R>T)\sim\frac{1024a}{525\pi^2T}.
\]
For the unit square, the limiting line-direction density at diagonal directions is \(8\sqrt2/7\) times its value at side-parallel directions. Thus the line-direction bias is nontrivially shape-dependent even though the normalized gaps are universal.

## Assumptions and scope

The body \(K\) is fixed, compact, planar and convex, with positive finite area; its boundary need not be smooth or strictly convex. Sampling is independent and uniform with respect to planar area. All limits are for \(T\to\infty\) with \(K\) fixed. The line parameter \(\theta\) ranges over an interval of length \(\pi\); the coordinates \(p\) and \(s_i\) use the normal and tangent vectors defined above, fixing all normalization factors. For finite \(T\), the first or last component of \(G_T\) can be negative when the perpendicular projection of \(X_3\) falls beyond the chord; this event vanishes conditionally in the limit. Boundary and degenerate-chord configurations have zero relevant measure. Convergence means weak convergence of probability distributions, not a total-variation rate.

## Proof

**1. Exact coordinates.** For fixed \(X_1\ne X_2\), the circumradius identity is
\[
\mathcal R=\frac{|X_1-X_3|\,|X_2-X_3|}{2|h|},\qquad
h=n_\theta\cdot(X_3-X_1),
\]
where \((\theta,p)\) is the line through \(X_1,X_2\). In the coordinates
\[
X_1=p n_\theta+s_1e_\theta,\quad
X_2=p n_\theta+s_2e_\theta,\quad
X_3=(p+h)n_\theta+s_3e_\theta,
\]
the exact change-of-variables Jacobian is \(|s_1-s_2|\). Thus, for any bounded measurable test function of the displayed coordinates, its expectation is an integral of the test function times
\[
\frac{|s_1-s_2|}{A^3}
\mathbf1_{\{X_1,X_2,X_3\in K\}}
\,d\theta\,dp\,ds_1\,ds_2\,ds_3\,dh.
\]
The variable \(\theta\in[0,\pi)\) counts every ordered pair exactly once, not twice.

**2. Thin-strip limit.** In these coordinates, \(\mathcal R>T\) is exactly
\[
2T|h|<\sqrt{(s_3-s_1)^2+h^2}\,
\sqrt{(s_3-s_2)^2+h^2}.
\]
Set \(t=Th\). Since every distance between points of \(K\) is at most its diameter \(D\), the event forces \(|t|<D^2/2\). The variables \(\theta,p,s_1,s_2,s_3,t\) consequently range in a fixed bounded region. For almost every such tuple, as \(T\to\infty\), the membership indicator converges to the indicator that all three \(s_i\) belong to the chord interval \([a(\theta,p),b(\theta,p)]\), and the circumradius event converges to
\[
|t|<\tfrac12|s_3-s_1|\,|s_3-s_2|.
\]
Convexity ensures that the section of \(K\) by every line is an interval, while endpoints and coincident scalar coordinates are null sets. Dominated convergence applies to the bounded Jacobian and the fixed bounded domain; hence its limit also holds for arbitrary bounded continuous marks. Integration in \(t\) supplies the interval length \(|s_3-s_1|\,|s_3-s_2|\). The unnormalized limiting measure on a line is therefore
\[
|s_1-s_2|\,|s_1-s_3|\,|s_2-s_3|\,ds_1\,ds_2\,ds_3.
\]

**3. The exact interval integral.** For a chord of length \(\ell\), scaling reduces this Vandermonde integral to \(\ell^6\) times its value on \([0,1]^3\). In sorted coordinates \(u_1<u_2<u_3\), introduce the gaps \(g_0=u_1\), \(g_1=u_2-u_1\), \(g_2=u_3-u_2\), \(g_3=1-u_3\). Because each of the six permutations has the same integrand,
\[
\int_{[0,1]^3}\prod_{i<j}|u_i-u_j|\,du_1du_2du_3
=6\!\int_{\substack{g_j\ge0\\\sum g_j=1}}
 g_1g_2(g_1+g_2)\,dg_0dg_1dg_2=\frac1{30}.
\]
The last identity follows from the elementary four-variable Dirichlet monomial integrals \(\int g_1^2g_2=\int g_1g_2^2=1/360\). This proves the stated scalar tail coefficient. Dividing the ordered-gap density by its total integral gives \(180g_1g_2(g_1+g_2)\), exactly the displayed equal mixture of the two Dirichlet distributions. Their mass-normalizing factors are each \(360\).

**4. Joint independence.** Before the \(t\)-integral, the rescaled coordinate \(U=2t/(|s_3-s_1||s_3-s_2|)\) runs over \((-1,1)\) with constant conditional density. Therefore it is uniform independently of all line and ordered-gap coordinates. The interval normalization \(\ell^6/30\) cancels in the conditional gap density, leaving a universal law independent of the line. Symmetry among the three original labels gives six equal permutation weights. The line itself retains density proportional to \(\ell^6\). Reapplying dominated convergence to bounded continuous test functions establishes joint weak convergence.

**5. Explicit checks and consequences.** For the disk of radius \(a\), the chord is \(\ell(\theta,p)=2\sqrt{a^2-p^2}\) for \(|p|<a\); hence
\[
Q_6=\pi\,64\int_{-a}^{a}(a^2-p^2)^3\,dp
=\frac{2048\pi a^7}{35}.
\]
Together with \(A=\pi a^2\), this yields the disk coefficient. The normalized line-offset density is \(35(1-u^2)^3/32\), \(-1<u<1\); the affine change \((u+1)/2\) gives \(\operatorname{Beta}(4,4)\).

For \(K=[-1/2,1/2]^2\), let \(J(e)=\int\ell_K(e,p)^6dp\) denote the line-direction marginal. A horizontal chord has length one for offsets \(|p|\le1/2\), so \(J_{\mathrm{side}}=1\). For a diagonal direction, \(\ell=\sqrt2-2|p|\) for \(|p|\le1/\sqrt2\), so
\[
J_{\mathrm{diagonal}}=2\int_0^{1/\sqrt2}(\sqrt2-2p)^6\,dp=\frac{8\sqrt2}{7}.
\]
The asserted ratio follows; this comparison uses the same angular measure at both directions.

## Verification

The standalone standard-library script `artifacts/verify.py` checks the Dirichlet/Selberg normalization, the disk's sixth-chord constant, and the square's directional ratio using an independent line-clipping integration. A deterministic simulation of \(750000\) independent triples in the unit disk, conditioned on circumradius exceeding \(8\), corroborates the large-radius tail, the four gap means \((1/7,5/14,5/14,1/7)\), the offset variance \(1/9\), and the rescaled transverse second moment \(1/3\). The reported finite-sample values cannot prove an asymptotic; the proof is the change-of-variables and dominated-convergence argument above. Run with `python3 artifacts/verify.py` in the directory containing this file. The script uses only Python 3 standard-library modules.

## Relationship to prior work

Classical chord-power integrals and their Blaschke–Petkantschin representations are treated by Heinrich (2009, 2012, 2014), including exact relations with interpoint-distance moments and inequalities for convex bodies. Those results motivate the sixth-power chord functional but do not state this marked circumradius-conditioned law. Kendall's 1985 study of random triangle shape densities and near-collinearity is a particularly relevant predecessor; its abstract and bibliographic treatment were inspected, but full text was not publicly accessible in this investigation, leaving a material historical-overlap risk. Importantly, normalized shape densities by themselves do not determine the chord line's Euclidean offset or its shape-dependent sixth-power bias. Bakó-Szabó, Besau and Fodor (2026) give the exact unit-disk circumradius distribution and its leading tail coefficient, so that scalar disk coefficient is acknowledged as previously known. The present claim is the **joint law** for every planar convex body, including the independent ordered-gap mixture, transverse law, and body-dependent line-direction distribution. It does not claim novelty for the preexisting one-dimensional disk tail or for generic Blaschke–Petkantschin formulas.

## Limitations

This is a fixed-body asymptotic for three area-uniform points, not an exact finite-threshold distribution or a rate of convergence. No theorem is asserted for a nonconvex region, for nonuniform sampling, or for more than three points. The exact numerical disk leading constant is covered by previous work; novelty is only asserted for the full joint marked law relative to inspected material. A plausible historical source (Kendall 1985) could not be fully read, so definitive priority requires further verification. Independent mathematical review has not been performed.

## References

1. L. Heinrich, *On Lower Bounds of Second-Order Chord Power Integrals of Convex Discs*, University of Augsburg preprint 2009-27, publicly deposited 19 October 2009, https://opus.bibliothek.uni-augsburg.de/opus4/1312.
2. L. Heinrich, *Some New Results on Second-Order Chord Power Integrals of Convex Quadrangles*, preprint 2011-22, https://opus.bibliothek.uni-augsburg.de/opus4/files/1598/mpreprint_11_022.pdf.
3. L. Heinrich, *Lower and Upper Bounds for Chord Power Integrals of Ellipsoids*, Applied Mathematical Sciences 8 (2014), 8257–8269, https://doi.org/10.12988/ams.2014.411913.
4. D. G. Kendall, *Exact distributions for shapes of random triangles in convex sets*, Advances in Applied Probability 17 (1985), 308–329, https://doi.org/10.2307/1427143.
5. A. Bakó-Szabó, F. Besau and F. Fodor, *Sylvester's four point problem for ball-convex bodies*, arXiv:2608.29975v1 (2026).
