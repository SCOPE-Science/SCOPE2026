# Temperature ordering and Beta boundary layers of two-site Sinkhorn geodesics

## Finding
Fix a two-site ground space with nonzero squared ground distance \(C>0\), and use the Riemannian length distance induced by the entropic Sinkhorn divergence with parameter \(\varepsilon>0\) (as defined in References [1,2]). Define
\[
B_\varepsilon=\exp(2C/\varepsilon)-1,\qquad
\beta_\varepsilon=(4B_\varepsilon)^{-1},\qquad
H_\beta(z)=\int_0^z [u(1-u)+\beta]^{-1/4}\,du,\qquad Z_\beta=H_\beta(1).
\]
The unique constant-speed geodesic between the opposite Dirac masses, written as the mass \(p_\varepsilon(t)\) at the destination site, is the *exact* inverse-integral curve
\[
H_{\beta_\varepsilon}(p_\varepsilon(t))=t Z_{\beta_\varepsilon}\quad(0\le t\le1).
\]
Its temperature ordering is strict: whenever \(0<\varepsilon_1<\varepsilon_2\),
\[
0<p_{\varepsilon_1}(t)<p_{\varepsilon_2}(t)<t\quad(0<t<1/2),
\qquad
1>p_{\varepsilon_1}(t)>p_{\varepsilon_2}(t)>t\quad(1/2<t<1).
\]
All midpoint masses equal \(1/2\). At vanishing regularization, the geodesics converge *uniformly* to the quantile function \(p_0\) of \(\operatorname{Beta}(3/4,3/4)\). Put \(K=\mathrm B(3/4,3/4)\) and \(\beta=\beta_\varepsilon\). For each fixed \(t\in(0,1)\),
\[
p_\varepsilon(t)=p_0(t)+\frac43(1-2t)[p_0(t)(1-p_0(t))]^{1/4}\beta^{3/4}+o(\beta^{3/4}).
\]
The endpoint behavior occurs on a distinct, explicitly resolved double scale: for each fixed \(s\ge0\),
\[
\lim_{\varepsilon\downarrow0}
\frac{p_\varepsilon(s\beta_\varepsilon^{3/4}/K)}{\beta_\varepsilon}
=\left(1+\frac{3s}{4}\right)^{4/3}-1.
\]
The other endpoint is its reflection \(p_\varepsilon(1-t)=1-p_\varepsilon(t)\). The endpoint distance has the exact quadrature
\[
d_{S,\varepsilon}(\delta_0,\delta_1)=\frac{\sqrt\varepsilon}{2}B_\varepsilon^{1/4}Z_{\beta_\varepsilon},
\]
and the sharp asymptotic \(d_{S,\varepsilon}\sim(K/2)\sqrt\varepsilon\,\exp(C/(2\varepsilon))\). These results concern the length metric, not the pointwise Sinkhorn divergence or a Schrödinger bridge.

## Assumptions and scope
Let \(X=\{x_0,x_1\}\), with cost \(c(x_i,x_i)=0\) and \(c(x_0,x_1)=c(x_1,x_0)=C>0\). Let \(\mu_p=p\delta_{x_1}+(1-p)\delta_{x_0}\), \(0\le p\le1\). Use entropic optimal transport with regularization \(\varepsilon>0\), kernel \(\exp(-c/\varepsilon)\), and the Riemannian metric derived from its Sinkhorn divergence in [1], Proposition 6.3. The required symmetric kernel is positive definite for every such \(C,\varepsilon\). Time \(t\) is constant-speed geodesic time on \([0,1]\). This is a statement for *every* \(C,\varepsilon\) satisfying the stated strict positivity assumptions and the specified Dirac endpoints; the asymptotic statements fix \(C\) and send \(\varepsilon\downarrow0\). The symbol \(\mathrm B\) denotes Euler's beta function, not the parameter \(B_\varepsilon\).

## Proof
**1. Reduction using the published two-point metric.** Write \(a=p(1-p)\), \(b=\exp(-2C/\varepsilon)\). Proposition 6.3 of [1] establishes that the off-diagonal mass \(w\) of the optimal symmetric self-coupling satisfies \(w^2=b(p-w)(1-p-w)\), and the Riemannian coefficient multiplying \(\dot p^2\) equals
\[
g_\varepsilon(p)=\frac\varepsilon2\frac{a-w}{w(2a-w)}.
\]
Since \(B_\varepsilon=(1-b)/b>0\), the coupling equation is \(B_\varepsilon w^2+w=a\). Thus \(a-w=B_\varepsilon w^2\) and \(1+2B_\varepsilon w=\sqrt{1+4B_\varepsilon a}\), giving the exact simplified coefficient
\[
g_\varepsilon(p)=\frac{\varepsilon B_\varepsilon}{2\sqrt{1+4B_\varepsilon p(1-p)}}.
\]
The same formula extends continuously with positive finite values to \(p=0,1\). Consequently
\[
\sqrt{g_\varepsilon(p)}=\frac{\sqrt\varepsilon}{2}B_\varepsilon^{1/4}[p(1-p)+\beta_\varepsilon]^{-1/4}.
\]
In one dimension, any absolutely continuous connecting path has length at least the integral of this positive line element between the endpoints, with equality precisely for monotone paths; its constant-speed parametrization is the unique inverse normalized arclength. This proves the exact geodesic and distance formulas. It does not claim novelty for the starting metric formula in [1].

**2. Temperature ordering.** Let \(f_\beta(u)=h_\beta(u)/Z_\beta\), with \(h_\beta(u)=[u(1-u)+\beta]^{-1/4}\). For \(0<\beta_1<\beta_2\), their density ratio is
\[
\frac{f_{\beta_1}(u)}{f_{\beta_2}(u)}
=\frac{Z_{\beta_2}}{Z_{\beta_1}}
\left(\frac{u(1-u)+\beta_2}{u(1-u)+\beta_1}\right)^{1/4}.
\]
It strictly decreases in \(u\in(0,1/2)\). Both densities are symmetric about \(1/2\), so each assigns exactly half its mass to \([0,1/2]\). The strict single-crossing (likelihood-ratio) argument then yields \(\int_0^z f_{\beta_1}>\int_0^z f_{\beta_2}\) for every \(z\in(0,1/2)\). On that half-interval, each density strictly decreases, hence its normalized cumulative distribution exceeds \(z\). Since \(\varepsilon\mapsto\beta_\varepsilon\) strictly increases, inversion yields the three strict inequalities for \(t<1/2\). Symmetry proves the other half. No sign ambiguity arises at the endpoints or midpoint, where the values are fixed.

**3. Weak-regularization quantile and interior expansion.** As \(\beta\downarrow0\), the nonnegative integrands \(h_\beta\) increase to \(h_0(u)=[u(1-u)]^{-1/4}\in L^1(0,1)\), and \(Z_\beta\to K=\mathrm B(3/4,3/4)\). Their distribution functions converge uniformly: the uniform error is at most the integral of \(h_0-h_\beta\) plus the normalization error. The continuous limit is strictly increasing from zero to one; therefore the inverse functions converge uniformly on \([0,1]\).

For a fixed \(z\in(0,1)\), the endpoint integral difference has the sharper asymptotic
\[
\int_0^z (h_0-h_\beta)\,du=\frac43\beta^{3/4}+o(\beta^{3/4}),\quad
K-Z_\beta=\frac83\beta^{3/4}+o(\beta^{3/4}).
\]
To justify the coefficient, split each integral into a fixed small endpoint neighborhood and its complement. On the complement the loss is \(O(\beta)=o(\beta^{3/4})\). In the endpoint neighborhood, put \(u=\beta v\). The rescaled difference converges on every bounded \(v\)-interval to \(v^{-1/4}-(1+v)^{-1/4}\). The difference is bounded above by a constant times \(v^{-1/4}\) near zero and \(v^{-5/4}\) for large \(v\), uniformly after choosing a sufficiently short endpoint neighborhood. Dominated convergence and a tail bound give the integral
\[
\int_0^\infty\big(v^{-1/4}-(1+v)^{-1/4}\big)\,dv=\frac43.
\]
The normalization has two identical endpoint contributions. For fixed \(t\in(0,1)\), set \(z=p_0(t)\) and expand the exact equation \(H_\beta(p_\varepsilon(t))=tZ_\beta\). The derivative of \(H_0\) at \(z\) is \([z(1-z)]^{-1/4}\), strictly positive and finite. Solving the first-order displacement equation gives the asserted coefficient \(\frac43(1-2t)[z(1-z)]^{1/4}\). This expansion is pointwise for interior time; it is not asserted uniformly up to the endpoints.

**4. Boundary layer.** For any fixed \(y\ge0\), substitute \(u=\beta v\):
\[
\frac{H_\beta(\beta y)}{\beta^{3/4}}
=\int_0^y [1+v-\beta v^2]^{-1/4}\,dv
\longrightarrow\frac43[(1+y)^{3/4}-1],
\]
locally uniformly for bounded nonnegative \(y\). In the normalized geodesic equation set \(t=s\beta^{3/4}/K\); since \(Z_\beta/K\to1\), monotone inversion of the preceding locally uniform limit yields \(y=(1+3s/4)^{4/3}-1\). The identical reflected boundary law follows from the symmetry of the integrand.

**5. Distance and opposite regime.** The exact distance follows from step 1. With \(\beta_\varepsilon\to0\), \(Z\to K\), and \(B_\varepsilon\sim\exp(2C/\varepsilon)\), its stated sharp low-temperature asymptotic follows. As \(\varepsilon\to\infty\), \(B_\varepsilon\sim2C/\varepsilon\), \(\beta_\varepsilon\to\infty\) and \(h_\beta/Z_\beta\to1\) uniformly, hence the geodesic approaches \(p(t)=t\) and the endpoint distance tends to \(\sqrt C\). The low-temperature mass layer has scale \(\beta_\varepsilon\sim\exp(-2C/\varepsilon)/4\), whereas its time layer has scale \(\beta_\varepsilon^{3/4}\), yielding exponentially distinct resolution requirements.

## Verification
`verify.py` (Python 3 with `mpmath`) independently compares the two published-algebra metric expressions, numerically inverts the exact arclength equation for multiple regularization parameters, checks strict finite-temperature ordering, and tests the two predicted boundary coefficients and interior displacement asymptotic. It prints the number of supplementary checks and the exact beta normalization numerically. The mathematical proof is the five arguments above; finitely many numerical checks do not establish limits or universal inequalities.

## Relationship to prior work
Reference [1], Proposition 6.3 and its proof, already supply the two-site self-coupling and metric coefficient and establish qualitative small- and large-ground-distance behavior. This finding **does not** claim that metric, coupling, or existence of its geodesics as new. Its claim is the exact geodesic's *strict temperature ordering*, the full limiting beta-quantile path, its quantified fractional interior correction, and the distinct sharp endpoint mass/time boundary layer. Reference [2] studies general computation, chain discretization and convergence of the geodesic Sinkhorn distance, motivating an explicit stiff-regime benchmark. In its inspected examples (Gaussian, translations and spatial splitting), no counterpart of this precise two-site quantitative characterization was found. A generic one-dimensional arclength principle is of course established mathematics; the specialized estimates above are the added analysis. Other graph transportation metrics and Schrödinger entropic interpolations are different geometric constructions and do not by themselves imply this claim.

## Limitations
Only the fully supported two-site space, symmetric squared ground cost and specified entropic normalization are addressed. This provides an exact benchmark for numerical geodesic methods, but neither a convergence theorem for a chain solver nor a bound for larger discrete spaces. The temperature-ordering theorem does not imply analogous order in higher dimensions or for other notions of entropic interpolation. While the cited original works and targeted mathematical records were inspected for matching claims, historical priority across all papers and unpublished work is not certified. The fractional interior expansion is not uniform in endpoint-time neighborhoods.

## References
[1] H. Lavenant, J. Luckhardt, G. Mordant, B. Schmitzer and L. Tamanini, *The Riemannian geometry of Sinkhorn divergences*, arXiv:2405.04987, original preprint May 2024, Proposition 6.3 and Section 6.2. https://arxiv.org/pdf/2405.04987

[2] H. Lavenant, J. Luckhardt and B. Schmitzer, *Approximation and computation of the geodesic Sinkhorn distance*, arXiv:2610.02007v1, first posted 1 October 2026, Sections 1, 4–6. https://arxiv.org/html/2610.02007v1
