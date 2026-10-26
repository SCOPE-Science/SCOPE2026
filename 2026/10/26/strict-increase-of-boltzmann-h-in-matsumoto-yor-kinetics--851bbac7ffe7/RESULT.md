# Strict increase of Boltzmann \(H\) in Matsumoto–Yor kinetics

## Finding

For the spatially homogeneous two-species kinetic collision equation built from the Matsumoto–Yor involution, the unweighted Boltzmann functional \(H=\int f_X\log f_X+\int f_Y\log f_Y\) **is not a Lyapunov functional**. For every \(p,c>0\), there is an explicit smooth one-parameter family of positive normalized initial marginals, converging to a stationary generalized-inverse-Gaussian/Gamma pair, for which \(\left.dH/dt\right|_{t=0}>0\). By contrast, relative entropy to that stationary pair has the exact nonpositive dissipation \(-D_{\mathrm{KL}}(g\Vert\mathcal Kg)\). The difference is an explicitly identified logarithmic-Jacobian expectation. This corrects the choice of entropy—not the probability-conserving kinetic model itself.

## Assumptions and scope

The state space is \(\Omega=(0,\infty)^2\). For \(z=(x,y)\), define
\[
\psi(x,y)=\left(\frac1{x+y},\frac{y}{x(x+y)}\right)=:(u,v),\qquad
j(x,y)=|\det D\psi(x,y)|=\frac1{x^2(x+y)^2}.
\]
The map is an involution. For a joint density \(g\), write \((\mathcal Kg)(x,y)=j(x,y)g(\psi(x,y))\). In the nonlinear collision system, the incoming pair is independent, \(g_t=f_X(\cdot,t)f_Y(\cdot,t)\), and
\[
\partial_t f_X(x,t)=\int_0^\infty(\mathcal Kg_t-g_t)(x,y)\,dy,\qquad
\partial_t f_Y(y,t)=\int_0^\infty(\mathcal Kg_t-g_t)(x,y)\,dx.
\]
Both collision rates are normalized to one. All entropy identities are asserted for positive normalized marginals with sufficient integrability for differentiation; the displayed smooth counterexample satisfies these hypotheses. In particular, no assumption of measure preservation for ordinary Lebesgue measure is made.

For fixed \(p,c>0\) let
\[
q_X(x)=Z_X^{-1}x^{-p-1}\exp\left[-\frac c2\left(x+\frac1x\right)\right],\qquad
q_Y(y)=Z_Y^{-1}y^{p-1}\exp(-cy/2),
\]
where \(Z_X,Z_Y\) are their positive finite normalization integrals, and \(q(x,y)=q_X(x)q_Y(y)\). This is the balanced-parameter generalized-inverse-Gaussian/Gamma pair. Define \(H(t)=\int f_X\log f_X+\int f_Y\log f_Y\) and \(F(t)=D_{\mathrm{KL}}(f_X\Vert q_X)+D_{\mathrm{KL}}(f_Y\Vert q_Y)\).

## Proof

**1. Invariant reference pair.** Direct substitution gives \(\psi^2=\mathrm{id}\), \(j(\psi z)j(z)=1\), and the pointwise invariants \(u+v+1/u=x+y+1/x\) and \(v/u=y/x\). The monomial transforms as
\[
u^{-p-1}v^{p-1}j(x,y)=x^{-p-1}y^{p-1}.
\]
Consequently \(\mathcal Kq=q\) everywhere. Hence \((q_X,q_Y)\) is stationary for the stated kinetic equation. The collision operator is a positive mass-preserving isometry on joint \(L^1\); its marginal gain maps are bilinear and locally Lipschitz on pairs of probability densities. The mild form with gain and unit-rate loss gives a nonnegative normalized local solution, extendible for all finite time by unit mass.

**2. Exact entropy identities.** Set \(g=f_Xf_Y\) and \(k=\mathcal Kg\). The gain-loss equation and the mass constraints give
\[
\frac{dF}{dt}=\iint_\Omega(k-g)\log\frac{g}{q}\,dx\,dy.
\]
Under \(\psi\), the invariance \(q(\psi z)j(z)=q(z)\) yields
\[
\iint k(z)\log\frac{g(z)}{q(z)}\,dz
=\iint g(z)\log\frac{k(z)}{q(z)}\,dz.
\]
Therefore
\[
\boxed{\frac{dF}{dt}=-D_{\mathrm{KL}}(g\Vert\mathcal Kg)\le0.}
\]
The same change of variables applied to \(\log q\) gives \(\iint(k-g)\log q=-\iint g\log j\). Thus the **unweighted Boltzmann functional** obeys the different exact identity
\[
\boxed{\frac{dH}{dt}=-D_{\mathrm{KL}}(g\Vert\mathcal Kg)-\iint_\Omega g(x,y)\log j(x,y)\,dx\,dy.}
\]
Involutivity also implies \(D_{\mathrm{KL}}(g\Vert\mathcal Kg)=D_{\mathrm{KL}}(\mathcal Kg\Vert g)\), so the first term equals the usual symmetrized production. The extra Jacobian term has no fixed sign. It vanishes in expectation at the stationary pair: \(\iint q\log j=0\), since \(\log j(\psi z)=-\log j(z)\) and \(q\) is invariant.

**3. A smooth strict counterexample arbitrarily near equilibrium.** Put
\[
\eta=\int_0^\infty q_X(x)\frac{x}{1+x}\,dx,\qquad
h(x)=\frac{x}{1+x}-\eta.
\]
Then \(h\) is strictly increasing, smooth, bounded by one in absolute value and centered under \(q_X\). For \(0<\varepsilon<1/2\) take \(f_X^{\varepsilon}(x,0)=q_X(x)(1+\varepsilon h(x))\), \(f_Y^{\varepsilon}(y,0)=q_Y(y)\). This is a strictly positive normalized smooth product pair. Define
\[
B=-\iint q(x,y)h(x)\log j(x,y)\,dx\,dy.
\]
For \(m(x)=\int q_Y(y)\log j(x,y)\,dy\),
\[
m'(x)=-\frac2x-2\int\frac{q_Y(y)}{x+y}\,dy<0.
\]
Since \(h\) is strictly increasing and \(m\) strictly decreasing, the independent-copy covariance identity yields \(\operatorname{Cov}_{q_X}(h(X),m(X))<0\). All logarithmic moments are finite from the GIG/Gamma tails, and so \(B>0\). Setting \(g_\varepsilon=q(1+\varepsilon h(x))\), invariance of \(q\) gives \(\mathcal Kg_\varepsilon=q(1+\varepsilon h(u))\). Hence
\[
\left.\frac{dH}{dt}\right|_{0}=\varepsilon B-D_{\mathrm{KL}}(g_\varepsilon\Vert\mathcal Kg_\varepsilon).
\]
The chi-square bound for KL and \(|h|<1\) show
\[
0\le D_{\mathrm{KL}}(g_\varepsilon\Vert\mathcal Kg_\varepsilon)
\le\frac{4\varepsilon^2}{1-\varepsilon}\le8\varepsilon^2.
\]
Thus, for every \(0<\varepsilon<\min\{1/2,B/8\}\), the initial derivative of \(H\) is **strictly positive**, whereas the initial derivative of \(F\) is **strictly negative**. This proves the counterexample and the corrected dissipation statement for each \(p,c>0\).

## Verification

The standalone `verify_kinetic_entropy.py` checks the involution, Jacobian and conserved energy symbolically with SymPy, checks the stationary product monomial symbolically for free positive parameters, and evaluates the two entropy-production formulas independently by deterministic quadrature in the exact special case \(p=1/2\), \(c=2\). The special case has \(X\) inverse Gaussian with mean one and shape two, and \(Y\) Gamma with shape one-half and scale one. The run found \(B\approx0.322978440288\). For perturbation sizes \(0.002,0.01,0.05\), unweighted production was positive, while relative-entropy production was negative. The program returned `all checks PASS`. Run with `python verify_kinetic_entropy.py` using Python, NumPy, SciPy and SymPy. Quadrature is corroboration; the strict signs for all \(p,c>0\) follow from the proof, not finite sampling.

## Relationship to prior work

Itoh (2026), arXiv:2610.18892v1, introduces precisely this kinetic equation, collision involution and nonconstant Jacobian. Its §3.3 defines the unweighted \(H\) and displays a nonpositive symmetrized production for it (Eq. 10). The calculation above identifies the absent Jacobian expectation, supplies a smooth strict sign counterexample, and locates that symmetrized production correctly in relative entropy to a stationary product. The original energy invariant, collision construction and density characterization are not claimed new.

Letac and Wesołowski (2000) characterize the GIG/Gamma independence property under this transformation; Matsumoto and Yor (2001) establish the original distributional phenomenon. Those distributional results underpin, but do not state, the model-specific sign counterexample to the unweighted kinetic entropy law. General data-processing and relative-entropy principles motivate the corrected functional, and are not claimed new. The contribution is the exact model-specific correction and its rigorous strictly positive unweighted production near every balanced stationary pair.

## Limitations

This is an initial entropy-production result and an exact dissipation identity, not a global rate of convergence, spectral-gap estimate or uniqueness classification of all kinetic stationary states. It assumes the source's collision rate normalization and a molecular-chaos product incoming density. Other collision clocks or correlation-preserving many-particle evolutions are not analyzed. The numerical quadrature is not a proof and the result has not undergone independent external review. Possible broader entropy frameworks could imply the relative-entropy half of the identity; the new claim is specifically the strict counterexample and corrected attribution for this collision model.

## References

1. Y. Itoh, *Two-Species Boltzmann--Kac Kinetics with Matsumoto--Yor Nonlinear Collisions: Conserved Energy and Conic Equilibria* (2026), arXiv:2610.18892v1, https://arxiv.org/html/2610.18892v1 . First public version: 2026-10-09.
2. G. Letac and J. Wesołowski, *An Independence Property for the Product of GIG and Gamma Laws*, Annals of Probability **28** (2000), 1371–1383, https://doi.org/10.1214/aop/1019160339 .
3. H. Matsumoto and M. Yor, *An analogue of Pitman's 2M–X theorem for exponential Wiener functionals, Part II*, Nagoya Mathematical Journal **162** (2001), 65–86.
