# Chirality-balanced phase-quotient means collapse and are discontinuously selected by elliptic perturbations

## Finding

A weighted ensemble of oppositely oriented unit-circle trajectories has a circle of inequivalent phase-quotient Fréchet means even though every input trajectory traces the same smooth circle. The minimizing curves are ellipses whose minor semiaxis is exactly the chirality imbalance. At equal total weights both orientations cancel, every mean retraces a diameter, and the result cannot be a nonconstant periodic solution of a locally Lipschitz autonomous planar flow. Crucially, arbitrarily small smooth elliptic perturbations make the means unique while retaining an order-one ambiguity: two datasets with maximal matched-observation distance \(2\varepsilon\) have unique means separated by distance \(1\) for every \(0<\varepsilon<1\).

## Assumptions and scope

Identify \(\mathbb R^2\) with \(\mathbb C\), set \(S^1=\mathbb R/(2\pi\mathbb Z)\), and equip \(H=L^2(S^1;\mathbb C)\) with the *normalized real Hilbert norm*
\[
\|f\|^2=\frac1{2\pi}\int_0^{2\pi}|f(t)|^2\,dt.
\]
The phase group acts by \((T_sf)(t)=f(t+s)\). The quotient metric is
\[
d([f],[g])=\min_{s\in S^1}\|f-T_sg\|.
\]
In particular, the quotient identifies time shifts but does **not** identify reversing the traversal orientation, spatial rotations, or general time warps. For a finite sample \(f_1,\dots,f_N\) with weights \(w_j>0\), \(\sum_jw_j=1\), let
\[
\mathcal F([c])=\sum_{j=1}^Nw_jd([c],[f_j])^2.
\]
Every initial sample in the first part is \(f_j(t)=e^{i\sigma_jt}\), with \(\sigma_j\in\{+1,-1\}\). These are unit-speed solutions of \(\dot z=\sigma_j iz\), and both signs must occur. Write \(p=\sum_{\sigma_j=+1}w_j\in(0,1)\) and \(q=1-p\). On equal-weight ordered datasets define \(D_{\infty}((a_1,a_2),(b_1,b_2))=\max\{d([a_1],[b_1]),d([a_2],[b_2])\}\). For the perturbation part use two observations, of weights \(1/2\) each, \(u(t)=e^{it}\) and \(b_{\varepsilon,\theta}(t)=e^{-it}+\varepsilon e^{i(t+\theta)}\) with \(0<\varepsilon<1\), \(\theta\in S^1\). Each perturbed observation is a nondegenerate smooth ellipse traversed clockwise.

## Proof

**1. Complete-square identity and minimizer exhaustion.** For arbitrary shifts \((s_1,\ldots,s_N)\), let \(g_j=T_{s_j}f_j\) and \(\overline g=\sum_j w_jg_j\). The Hilbert-space identity
\[
\sum_jw_j\|c-g_j\|^2=\|c-\overline g\|^2+\sum_jw_j\|g_j\|^2-\|\overline g\|^2
\]
shows that minimizing over \(c\) and all shifts is equivalent to maximizing \(\|\overline g\|\), and every minimizer is precisely a shifted-sample mean attaining this maximum. This joint minimization equals the original phase-quotient Fréchet minimization because the finite Cartesian product of phase circles is compact and minimization over independent shifts commutes with minimization over \(c\).

The orthogonality of the two Fourier characters \(e^{it}\) and \(e^{-it}\) gives
\[
\|\overline g\|^2=\left|\sum_{\sigma_j=+1}w_je^{is_j}\right|^2+\left|\sum_{\sigma_j=-1}w_je^{-is_j}\right|^2\le p^2+q^2.
\]
Because all weights are positive, equality in each triangle inequality requires the phases within that orientation class to coincide. Its two class phases are otherwise independent. Every minimizing curve can therefore be written \(Ae^{it}+Be^{-it}\) with \(|A|=p\), \(|B|=q\), and the minimum functional value is \(1-p^2-q^2=2pq\). A common time shift sends \((A,B)\) to \((Ae^{is},Be^{-is})\), preserving their product \(AB\). Choosing the time shift that makes \(A=p\), the entire minimizing family becomes
\[
m_\phi(t)=pe^{it}+qe^{i\phi}e^{-it},\qquad \phi\in S^1.
\]
Two normalized representatives with distinct \(\phi\) cannot be related by a time shift: equality of their positive-frequency coefficients first forces \(e^{is}=1\), after which equality of their negative-frequency coefficients forces equality of \(e^{i\phi}\). This proves completeness and inequivalence.

**2. Exact geometry and loss of periodic-orbit representativeness.** With \(t'=t-\phi/2\),
\[
m_\phi(t)=e^{i\phi/2}\bigl((p+q)\cos t'+i(p-q)\sin t'\bigr).
\]
Hence the image has semiaxes \(1\) and \(|p-q|\), and its signed area is \(\pi(p^2-q^2)=\pi(p-q)\). When \(p\ne q\), the curve is regular and embedded, with ellipse maximal curvature \(1/|p-q|^2\). For \(p=q=1/2\), it reduces to \(e^{i\phi/2}\cos t'\), which traces a diameter forward and backward and has zero velocity at both endpoints. A nonconstant periodic solution of a locally Lipschitz autonomous planar vector field cannot do this: if its velocity vanished at any point, that point would be an equilibrium, and uniqueness of the initial-value problem would force the entire solution to be constant. No reparametrization of the already constant-speed input circles is needed to obtain the collapse.

**3. Unique means of perturbed clockwise ellipses.** For the two inputs \(u\) and \(b_{\varepsilon,\theta}\), the real Hilbert inner product satisfies
\[
\langle u,T_sb_{\varepsilon,\theta}\rangle_{\mathbb R}=\varepsilon\cos(s+\theta).
\]
The optimal relative phase is therefore uniquely \(s=-\theta\pmod{2\pi}\). Using the complete-square identity for equal weights, all minimizers belong to the sole phase-quotient class of the midpoint of these optimally aligned inputs:
\[
M_{\varepsilon,\theta}(t)=\frac{1+\varepsilon}{2}e^{it}+\frac12e^{i\theta}e^{-it}.
\]
The perturbed observation \(b_{\varepsilon,\theta}\) is a clockwise ellipse because its two Fourier-mode magnitudes are \(1\) and \(\varepsilon<1\); its semiaxes are \(1+\varepsilon\) and \(1-\varepsilon\). It converges to \(e^{-it}\) in \(H\) with norm error \(\varepsilon\), uniformly in \(\theta\).

**4. Exact order-one instability.** For two-mode curves \(f(t)=ae^{it}+be^{-it}\) and \(g(t)=ce^{it}+de^{-it}\) with real coefficients,
\[
d([f],[g])^2=a^2+b^2+c^2+d^2-2|ac+bd|,
\]
since the phase-aligned real correlation is \((ac+bd)\cos s\). Apply this first to \(b_{\varepsilon,0}=(\varepsilon,1)\) and \(b_{\varepsilon,\pi}=(-\varepsilon,1)\), obtaining \(d^2=4\varepsilon^2\); because the first observation is unchanged, the two datasets have \(D_{\infty}=2\varepsilon\). Apply it to the unique means \(M_{\varepsilon,0}=(a,1/2)\) and \(M_{\varepsilon,\pi}=(a,-1/2)\), where \(a=(1+\varepsilon)/2>1/2\), obtaining \(d^2=1\). Thus datasets of arbitrarily small mutual distance have unique means at fixed positive distance. In particular, there is no selection continuous at the common limit \(([e^{it}],[e^{-it}])\), since both families of datasets converge to it and their unique mean classes stay separated by \(1\).

## Verification

A standalone Python standard-library program, `verify.py`, independently checks the rational Fourier-coefficient identities for four perturbation sizes and three chirality weight splits, and samples the original curves on a 256-point Fourier grid for three perturbation sizes. Run `python verify.py`. All checks completed successfully. The exact, infinite-dimensional conclusion is established by the preceding analytic proof; finite-grid checks are diagnostic only, not a substitute for quantifier-complete proof.

## Relationship to prior work

Hering and Kuehn (2026) define the Hilbert-space quotient by phase shifts, establish existence of empirical Fréchet means, investigate phase versus arc-length parametrization, and describe geometry-based diagnostics for unrepresentative averages. Their framework supplies the directly comparable metric and scientific motivation. The present result specializes to counter-rotating circles and provides an exhaustive closed-form description of *all* mean classes, a sharp geometric loss of regularity, and an exact order-one selection instability under vanishing elliptic perturbations; these quantitative statements are not supplied by the inspected sections of that paper. Bigot (2011) develops Fréchet mean curve registration for signal averaging, but its analyzed ECG registration formulation does not imply the opposite-chirality Fourier decomposition or the exact instability in the phase-only quotient. General Hilbert midpoints and Fourier orthogonality are classical mathematical ingredients, not claimed as original. Published-record searches located no direct equivalent, but they do not prove historical priority.

## Limitations

The theorem uses normalized \(L^2\) phase alignment without orientation reversal, spatial rigid alignment, nonlinear time warps, or a derivative penalty. Allowing orientation reversal identifies the two opposite circles and changes the conclusion. It concerns input orbits from different orientation choices of planar rotation fields, not the existence of oppositely rotating periodic orbits within a single planar autonomous vector field. The quantitative instability is for the specified two-observation elliptic perturbations, not an assertion about every possible dataset or all definitions of trajectory means. Smooth finite-dimensional experiments cannot certify the infinite-dimensional results; the proof above supplies the required analytic argument. Priority remains subject to unindexed specialized work on phase-quotient shape means.

## References

1. P. Hering and C. Kuehn, *Fréchet Means of Periodic Orbits in Dynamical Systems: Geometry, Dynamics, and Diagnostics*, arXiv:2606.10748, first publicly available 2026-06-09; https://arxiv.org/abs/2606.10748.
2. J. Bigot, *Fréchet means of curves for signal averaging and application to ECG data analysis*, arXiv:1111.1855, first publicly available 2011-11-08; https://arxiv.org/abs/1111.1855.
