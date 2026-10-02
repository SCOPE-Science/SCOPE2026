# Uniform small-noise entropic \(K\)-convexity on compact \(\mathrm{RCD}(K,\infty)\) spaces

## Finding

Let \((X,d,m)\) be compact \(\mathrm{RCD}(K,\infty)\), with \(m(X)=1\), diameter \(D\), and endpoints \(\mu_0,\mu_1\) of finite entropy \(H_i=H(\mu_i\mid m)\). Define the entropic interpolation by the dynamic Schrödinger problem: \(\mu^\varepsilon\) minimizes
\[
\mathcal J_\eta(\mu)=\frac12\int_0^1\bigl(|\dot\mu_t|_{W_2}^2+\eta^2 I(\mu_t)\bigr)\,dt,
\qquad \eta=\varepsilon/2.
\]
This is the standard reversible Brownian normalization with generator \((\varepsilon/2)\Delta\). Bounded endpoint densities and finite endpoint Fisher information, as in the original formulation, may be retained but are not required for the metric estimate below.

### Estimate

For \(0<\varepsilon\leq1\) and all \(t\in[0,1]\),
\[
H(\mu_t^\varepsilon\mid m)\leq(1-t)H_0+tH_1-\frac K2t(1-t)W_2(\mu_0,\mu_1)^2+C\varepsilon,
\]
where an explicit choice is
\[
C=\frac58|K|C_0,\qquad C_0=\frac12K^-e^{K^-/2}D^2+H_0+H_1,\qquad K^-=\max\{-K,0\}.
\]
For \(K=0\), the entropy is exactly convex along every such interpolation. This is a small-noise theorem; no uniform all-noise claim is made.

## Assumptions and scope

The reference measure is a probability measure of full support. Entropy means \(H(\rho m\mid m)=\int\rho\log\rho\,dm\), and is \(+\infty\) for measures not absolutely continuous with respect to \(m\). Fisher information is \(I(\rho m)=4\int|D\sqrt\rho|^2\,dm\) when \(\sqrt\rho\) belongs to the Cheeger Sobolev space, and is \(+\infty\) otherwise. The optimization is over \(AC^2([0,1],(\mathcal P_2(X),W_2))\) curves with the prescribed endpoints, interpreting infinite Fisher action as inadmissible. On compact \(X\), Wasserstein space is compact and geodesic; entropy has an \(\mathrm{EVI}_K\) heat flow and its squared slope is \(I\). The primary existence theorem therefore gives finite-action minimizers for finite-entropy endpoints. Uniqueness is not needed: the estimate applies to EVERY minimizer. There is no assumption of finite-dimensional curvature or endpoint smoothness.

## Proof

### Metric first variation

Write \(A_t=|\dot\mu_t|_{W_2}^2\), \(F_t=\eta^2I(\mu_t)\), \(S_t=A_t+F_t\), and \(H_t=H(\mu_t\mid m)\). Finite action implies \(A,I\in L^1\). The entropy slope is a strong upper gradient, so \(H_t\) is absolutely continuous and \(|H'_t|\leq\sqrt{A_tI(\mu_t)}\).

Let \(\mathsf S_s\) denote the \(\mathrm{EVI}_K\) heat flow on Wasserstein space. Its slope contraction is
\[
I(\mathsf S_s\nu)\leq e^{-2Ks}I(\nu).
\]
The metric heat-flow perturbation estimate of Monsaingeon–Tamanini–Vorotnikov, Proposition 3.11, applies to \(\widetilde\mu_t=\mathsf S_{h(t)}\mu_t\):
\[
\frac12|\dot{\widetilde\mu}_t|^2+\frac12|h'(t)|^2I(\widetilde\mu_t)+h'(t)\widetilde H'_t
\leq\frac12e^{-2Kh(t)}A_t.
\]
Take \(h(t)=s[\vartheta(t)+\delta t(1-t)]\), where \(\vartheta\geq0\) is smooth and compactly supported in \((0,1)\), and \(\delta>0\). This keeps the endpoints fixed and makes \(h>0\) in the open interval, as required by that proposition. More precisely, \(h\) is smooth, nonnegative, vanishes at both endpoints, has bounded derivative, and satisfies \(h'(0)=s\delta>0\), \(h'(1)=-s\delta<0\). The source's Lemmas 3.8 and 3.10 first give continuity of the perturbed curve on the closed interval and local absolute continuity of the curve and its entropy, with the prescribed endpoint entropy values.

The following argument supplies GLOBAL finite action, which local regularity alone would not give. At almost every differentiability point \(t\) with \(I(\mu_t)<\infty\), compare \(\mathsf S_{h(t+r)}\mu_{t+r}\) to \(\mathsf S_{h(t+r)}\mu_t\), then to \(\mathsf S_{h(t)}\mu_t\). The first distance is bounded by heat-flow contraction times \(W_2(\mu_{t+r},\mu_t)\). The second is the heat-flow length for the FIXED starting point \(\mu_t\), and its vertical speed is bounded by \(e^{K^-\|h\|_\infty}\sqrt{I(\mu_t)}\). Dividing by \(|r|\) and taking the limit gives
\[
|\dot{\widetilde\mu}_t|
\leq e^{K^-\|h\|_\infty}
\bigl(\sqrt{A_t}+|h'(t)|\sqrt{I(\mu_t)}\bigr),\qquad
I(\widetilde\mu_t)\leq e^{2K^-\|h\|_\infty}I(\mu_t).
\]
Both right-hand sides yield square-integrable speed and integrable Fisher information because \(h'\) is bounded and \(A,I\in L^1\). Integrating the local speed bound and using closed-interval continuity extends \(\widetilde\mu\) to \(AC^2([0,1])\). Cauchy--Schwarz makes \(\sqrt{I(\widetilde\mu)}|\dot{\widetilde\mu}|\) integrable. The strong-upper-gradient inequality therefore gives globally absolutely continuous entropy, including both endpoints. The perturbed curve is an admissible finite-action competitor, and integration by parts on the entire interval is justified. No bound on endpoint Fisher information or smooth Schrödinger potentials was used.

Adding the Fisher term, discarding the nonpositive \(-|h'|^2 I/2\) term, and using minimality gives
\[
0\leq\frac12\int_0^1(e^{-2Kh}-1)S_t\,dt-\int_0^1 h'\widetilde H'_t\,dt.
\]
The energy-dissipation equality and slope contraction give
\[
0\leq H_t-\widetilde H_t\leq h(t)e^{2K^-\|h\|_\infty}I(\mu_t)
\quad\text{for a.e. }t,
\]
so \(\widetilde H\to H\) in \(L^1\) as \(s\downarrow0\). Integrate the last term by parts, divide by \(s\), and pass to the limit. The exact boundary contribution after division by \(s\) is \(\delta(H_0+H_1)\), while \(h''/s=\vartheta''-2\delta\). Thus before removing \(\delta\) the limiting inequality is
\[
0\leq-K\int_0^1[\vartheta+\delta t(1-t)]S\,dt
+\int_0^1(\vartheta''-2\delta)H\,dt+\delta(H_0+H_1).
\]
All terms are integrable. First take \(s\downarrow0\) for fixed \(\delta>0\), using the displayed \(L^1\) entropy bound and bounded exponential difference quotients; only then let \(\delta\downarrow0\). The result, for every nonnegative test function \(\vartheta\), is
\[
\int_0^1\vartheta''H\,dt\geq K\int_0^1\vartheta S\,dt.
\]
Thus \(H''\geq KS\) in distributions. This establishes the required inequality directly on \(\mathrm{RCD}(K,\infty)\); it does not assume a finite-dimensional Schrödinger-potential Hessian formula.

### Conserved energy without smooth potentials

Fix any real \(\zeta\in C_c^\infty((0,1))\), and set \(r_s(t)=t+s\zeta(t)\). Choose either sign of \(s\) with \(|s|\|\zeta'\|_\infty<1/2\). Then \(r_s\) is an increasing, endpoint-fixing, smooth bi-Lipschitz bijection of \([0,1]\), with \(1/2<r_s'<3/2\). The competitor \(\mu_{r_s(t)}\) belongs to \(AC^2\), has finite Fisher action, preserves both endpoints, and has speed \(r_s'(t)|\dot\mu_{r_s(t)}|\) almost everywhere; bi-Lipschitz maps preserve null sets.

With \(u=r_s(t)\), its action is exactly
\[
\mathcal J_\eta(\mu\circ r_s)
=\frac12\int_0^1
\left[b_s(u)A_u+\frac{F_u}{b_s(u)}\right]du,\qquad
b_s(u)=1+s\zeta'(r_s^{-1}(u)).
\]
As \(s\to0\), both coefficient difference quotients are uniformly bounded and converge to \(\zeta'(u)\) and \(-\zeta'(u)\), respectively. Dominated convergence uses only \(A,F\in L^1\), not their derivatives. The first variation is therefore \(\frac12\int\zeta'(A-F)\,du\). Two-sided minimality makes it zero. Consequently the distributional derivative of \(A-F\) is zero, so \(A_t-F_t=E\) for a finite real constant \(E\), almost everywhere.

Put \(V_\varepsilon=2\mathcal J_\eta(\mu^\varepsilon)\), \(W=W_2(\mu_0,\mu_1)\), and \(B=\int_0^1F_tdt\). Then
\[
V_\varepsilon=E+2B,\qquad W^2\leq\int_0^1A_tdt=E+B.
\]
Theorem 3.12 of the same primary source, applied to a Wasserstein geodesic and heat-flow smoothing height \(\eta\min(t,1-t)\), gives
\[
V_\varepsilon\leq e^{K^-\varepsilon/2}W^2+\varepsilon(H_0+H_1),
\]
because entropy relative to the probability measure \(m\) is nonnegative. For \(\varepsilon\leq1\), this proves
\[
0\leq V_\varepsilon-W^2\leq C_0\varepsilon,\qquad
B\leq C_0\varepsilon,\qquad |E-W^2|\leq C_0\varepsilon.
\]

### Green-kernel estimate

Set \(h_0(t)=(1-t)H_0+tH_1-(K/2)t(1-t)W^2\) and \(e=H-h_0\). Importantly, \(h_0''=KW^2\), so
\[
e''=H''-KW^2\geq K(S-W^2).
\]
The Dirichlet Green kernel for the second derivative is
\(G(s,t)=-\min(s,t)[1-\max(s,t)]\). The continuous distributional comparison principle, or integration against this kernel, gives
\[
e(t)\leq-\frac K2t(1-t)(E-W^2)+2K\int_0^1G(s,t)F_sds.
\]
Indeed the difference from the displayed right-hand side has nonnegative distributional second derivative and zero endpoints, hence is convex and nonpositive. Using \(t(1-t)\leq1/4\), \(|G|\leq1/4\), and the integrated bounds yields \(e(t)\leq(5/8)|K|C_0\varepsilon\). No pointwise Fisher bound is needed. For \(K\geq0\) the Fisher term is nonpositive and the sharper \(KC_0\varepsilon/8\) bound also holds.

## Verification

The proof uses global finite-action bounds, exact endpoint terms, two-sided time variations and a signed Dirichlet comparison. It establishes an infinite-dimensional analytic inequality; no finite experiment is used to certify the general theorem. The coefficient \(5/8\) comes from \(1/8+1/2\), bounding the constant-energy and Fisher terms separately. When \(K=0\), both terms vanish.

## Relationship to prior work

The cited metric paper's Theorem 4.8 establishes convexity along geodesics, not along its positive-noise minimizing interpolations. Its Theorem 5.8 estimates optimal costs under a further finite-Fisher-geodesic hypothesis, not the entropy at every interpolation time under the present endpoint hypotheses. The heat-perturbation and competitor results are credited inputs; the application here keeps the Fisher variation in the actual minimizing problem and separately derives its conserved energy.

The general heat-flow variation strategy is also prior-known from the harmonic-map literature. There harmonicity means minimizing the kinetic Dirichlet energy alone; it does not mean minimizing the kinetic-plus-Fisher action here. The difference in the variational problem must not be omitted when transferring an entropy comparison.

## Limitations

Compactness and the metric Schrödinger \(\Gamma\)-convergence give subsequential zero-noise limits that are Wasserstein geodesics. Entropy lower semicontinuity then recovers the usual \(K\)-convexity inequality along these limits. Displacement convexity itself is prior-known and is not claimed as new.

The finite-dimensional second-derivative formulas and Euclidean Gaussian illustrations are not used to justify the infinite-dimensional theorem. Historical Gaussian artifacts can remain as illustrations, but they are not a verification of general \(K\neq0\) or all-noise claims. The restriction \(0<\varepsilon\leq1\) is essential to the constant proved here; extending it to all noise levels requires a separate large-noise argument.

## References

L. Monsaingeon, L. Tamanini and D. Vorotnikov, [The dynamical Schrödinger problem in abstract metric spaces](https://arxiv.org/html/2012.12005), Sections 3.1 and 3.2, Proposition 3.11, Theorem 3.12, Proposition 4.2, Section 4.1, and Section 6.2. The source supplies the EVI perturbation and competitor machinery; the first variations and signed Dirichlet comparison above supply the estimate for the actual minimizing interpolation.

H. Lavenant, L. Monsaingeon, L. Tamanini and D. Vorotnikov, [Convex functions defined on metric spaces are pulled back to subharmonic ones by harmonic maps](https://arxiv.org/html/2107.09589v1), Definition 2.2, Theorem 2.4 and Section 4.
