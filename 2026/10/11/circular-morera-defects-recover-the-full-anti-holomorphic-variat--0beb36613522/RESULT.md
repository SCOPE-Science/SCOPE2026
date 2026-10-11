# Circular Morera defects recover the full anti-holomorphic variation

## Finding

Let \(D\subset\mathbb C\) be open, \(f\in L^1_{\mathrm{loc}}(D)\), and, for each sufficiently small \(r>0\), define the circular Morera defect for almost every center \(a\in D\) by
\[
J_r f(a)=\int_0^{2\pi}f(a+re^{it})\,ir e^{it}\,dt,
\qquad T_r f(a)=\frac{J_r f(a)}{2\pi i r^2}.
\]
The following assertions hold, with the statements on compact subsets interpreted locally inside \(D\).

**Exact characterization.** The distributional derivative \(\mu=\bar\partial f\) is a locally finite complex Radon measure if and only if, for each compact \(K\Subset D\), there exists \(r_K>0\) such that
\[
\sup_{0<r<r_K}\int_K |T_r f(a)|\,dA(a)<\infty.
\]
In this case, \(T_r f\,dA\) converges weakly to \(\mu\), and, more strongly, the nonnegative measures \(|T_r f|\,dA\) converge weakly to the total-variation measure \(|\mu|\): for every nonnegative \(\varphi\in C_c(D)\),
\[
\boxed{\lim_{r\downarrow0}\int_D \varphi(a)\frac{|J_r f(a)|}{2\pi r^2}\,dA(a)=\int_D\varphi\,d|\bar\partial f|.}
\]
In particular, for every relatively compact Borel set \(E\subset D\) with \(|\mu|(\partial E)=0\), the unweighted integrals over \(E\) have the same limit.

**Exact singular-mass diagnostic.** Write the Lebesgue decomposition \(\mu=h\,dA+\mu_s\). Then the **canonical disk-average representative** \(T_r^\mu(a)=\mu(B(a,r))/(\pi r^2)\) converges to \(h(a)\) for almost every \(a\in D\); for each fixed \(r\) it agrees almost everywhere with \(T_r f\). For each relatively compact Borel set \(E\subset D\) with \(|\mu_s|(\partial E)=0\),
\[
\boxed{\lim_{r\downarrow0}\int_E|T_r f(a)-h(a)|\,dA(a)=|\mu_s|(E).}
\]
Consequently, within the measure-derivative class, vanishing of the normalized circular defect at almost every center is equivalent to the derivative being purely singular; local strong \(L^1\) convergence detects the singular mass that pointwise almost-everywhere tests miss.

The distinction is sharp even near the Lipschitz regularity boundary. For every \(\beta>0\) there is a continuous nonholomorphic function \(f_\beta\) on the unit disk with modulus of continuity \(O(t(1+\log(1/t))^\beta)\) such that \(J_r f_\beta(a)=0\) for all sufficiently small \(r\) at almost every center \(a\), while \(\bar\partial f_\beta\) is a nonzero singular Radon measure. In contrast, a locally Lipschitz function satisfying \(T_r f(a)\to0\) almost everywhere must be holomorphic.

## Assumptions and scope

Here \(dA\) is planar Lebesgue area, \(\bar\partial=(\partial_x+i\partial_y)/2\) in the distributional sense, and \(\mathcal M_{\mathrm{loc}}(D)\) denotes locally finite complex Radon measures. Circular integrals of an \(L^1\)-equivalence class are defined for almost every center separately for each radius; this is enough for all local \(L^1\) and measure statements. No values along exceptional circles are asserted. A continuous function admits the standard pointwise circle integral for every admissible center and radius. Every almost-everywhere pointwise limit uses the canonical disk-average representative of \(T_r f\) when \(\bar\partial f\) is a measure; this avoids arbitrary radius-dependent exceptional-center choices for a merely \(L^1\) function. In the example \(t\) is a small positive Euclidean distance and constants depend on \(\beta\). The equalities are local, with convolution performed after restricting measures or functions to a slightly larger relatively compact neighborhood.

## Proof

**Step 1: the exact disk-averaging identity.** Set \(\kappa_r=\mathbf1_{B(0,r)}/(\pi r^2)\). For smooth \(f\), Green–Stokes gives
\[
J_r f(a)=2i\int_{B(a,r)}\bar\partial f(z)\,dA(z),
\quad\text{hence}\quad T_r f=\kappa_r*(\bar\partial f).
\]
For general \(L^1_{\mathrm{loc}}\) data, approximate locally in \(L^1\) by smooth functions. For fixed \(r\), the circle operator is a bounded map between the relevant local \(L^1\) spaces, because
\[
\int_K|J_r g(a)|\,dA(a)\le 2\pi r\int_{K_r}|g(z)|\,dA(z),
\]
where \(K_r\) is the closed \(r\)-neighborhood. On the other side, the expression \(\kappa_r*\bar\partial f\) for a general distributional derivative is **defined here** as \(\bar\partial(\kappa_r*f)\); it is well-defined in \(L^1_{\mathrm{loc}}\), because the distributional derivative of the disk indicator is a finite circle measure. The local \(L^1\) limit of the smooth identity establishes
\[
T_r f=\kappa_r*\bar\partial f
\]
for each admissible \(r\), as distributions and as locally integrable functions. For every \(f\in L^1_{\mathrm{loc}}\), \(T_r f\to\bar\partial f\) in \(\mathcal D'(D)\) by the approximate-identity property.

**Step 2: characterization of measure derivatives.** If \(\mu=\bar\partial f\) is a measure, then, on each compact \(K\Subset D\),
\[
\int_K|T_r f|\,dA\le |\mu|(K_r)
\]
for sufficiently small \(r\), giving local uniform boundedness. Conversely assume the stated bounds. For any \(K\Subset D\), the distributions \(T_r f\,dA\) act on test functions supported in \(K\) with uniformly bounded sup-norm operator norm. Since these distributions converge to \(\bar\partial f\), the limiting distribution also has order zero on every compact; by the Riesz–Markov representation theorem it is a locally finite complex Radon measure. This proves both directions without any pointwise regularity assumption on \(f\).

**Step 3: recovery of variation.** Once \(\bar\partial f=\mu\) is a measure, \(\kappa_r*\mu\,dA\to\mu\) weakly on compactly supported continuous tests. Fix \(0\le\varphi\in C_c(D)\). The triangle inequality and Tonelli give
\[
\int\varphi|\kappa_r*\mu|\,dA\le\int(\varphi*\kappa_r)\,d|\mu|\longrightarrow\int\varphi\,d|\mu|.
\]
On the other hand, weak convergence of complex measures entails the weighted total-variation lower-semicontinuity inequality
\[
\int\varphi\,d|\mu|\le\liminf_{r\downarrow0}\int\varphi|\kappa_r*\mu|\,dA.
\]
This follows directly by expressing weighted variation as the supremum of the real parts of \(\int\psi\,d\mu\) over compactly supported continuous complex test functions satisfying \(|\psi|\le\varphi\). The two bounds coincide. Weak convergence of the positive variation measures follows, as do the conclusions for continuity sets by standard inner/outer regularity.

**Step 4: the singular deficit.** Decompose \(\mu=h\,dA+\mu_s\), where \(h\in L^1_{\mathrm{loc}}\) and \(\mu_s\perp dA\). The Lebesgue differentiation theorem for Radon measures gives
\[
T_r^\mu(a)=\frac{\mu(B(a,r))}{\pi r^2}\longrightarrow h(a)
\quad\text{for almost every }a.
\]
Also \(\|\kappa_r*h-h\|_{L^1(E)}\to0\) locally. Since \(T_r f-h=\kappa_r*\mu_s+(\kappa_r*h-h)\), the reverse triangle inequality yields
\[
\Big|\|T_r f-h\|_{L^1(E)}-\|\kappa_r*\mu_s\|_{L^1(E)}\Big|
\le\|\kappa_r*h-h\|_{L^1(E)}\to0.
\]
Step 3 applied to \(\mu_s\) gives \(\|\kappa_r*\mu_s\|_{L^1(E)}\to|\mu_s|(E)\) when \(|\mu_s|(\partial E)=0\). This proves the boxed singular-mass identity. In particular, almost-everywhere decay detects \(h=0\), whereas strong local \(L^1\) decay detects \(\mu=0\).

**Step 5: near-Lipschitz sharpness.** For \(\beta>0\), define \(\ell_n=2^{-n}(n+1)^{-\beta}\) for integers \(n\ge0\). Starting from \([0,1]\), at step \(n\) retain the two disjoint extreme child intervals of length \(\ell_n\) inside each surviving parent interval of length \(\ell_{n-1}\); the strict inequality \(2\ell_n<\ell_{n-1}\) makes this possible. Assign every one of the \(2^n\) level-\(n\) intervals mass \(2^{-n}\), coherently across levels. The resulting atomless probability measure \(\nu_\beta\) is supported on a compact set \(C_\beta\) of Lebesgue measure zero, since \(2^n\ell_n=(n+1)^{-\beta}\to0\). Its cumulative distribution \(H_\beta(t)=\nu_\beta([0,t])\) is continuous, nonconstant, and constant on each complementary interval.

For \(h=|s-t|\in(0,1)\), select \(n\ge1\) with \(\ell_n\le h<\ell_{n-1}\). An interval of length \(h\) meets at most two distinct level-\((n-1)\) intervals, each of mass \(2^{-(n-1)}\). Consequently
\[
|H_\beta(s)-H_\beta(t)|\le2^{2-n}
=4\ell_n(n+1)^\beta\le4h(n+1)^\beta
\le C_\beta h(1+\log(1/h))^\beta.
\]
(The equality in the middle is a direct consequence of the definition of \(\ell_n\).) Let \(f_\beta(z)=H_\beta((\operatorname{Re}z+1)/2)\) for \(|z|<1\). Its distributional \(\bar\partial\)-derivative is one-half the product of the pushforward of \(\nu_\beta\) under \(t\mapsto2t-1\) with the \(y\)-Lebesgue measure, restricted to the unit disk. This is a nonzero singular measure. Outside the zero-area set of centers whose real coordinate lies in \(2C_\beta-1\), the function is locally constant; for those centers \(J_r f_\beta(a)=0\) for every sufficiently small \(r\). Nonetheless, Step 3 recovers the full nonzero measure variation through spatial averages of \(|J_r f_\beta|/(2\pi r^2)\).

Finally, if \(f\) is locally Lipschitz, its distributional \(\bar\partial f\) is an \(L^\infty_{\mathrm{loc}}\) density. Thus almost-everywhere decay of \(T_r f\) forces \(\bar\partial f=0\); the distributional Cauchy–Riemann theorem then makes \(f\) holomorphic (as an everywhere-equal continuous representative). This proves the regularity contrast.

## Verification

The normalization has two independent checks: for \(f(z)=\bar z\), \(J_r f=2\pi i r^2\) and \(T_r f=1\); for \(f(z)=\bar z^2\), \(T_r f(a)=2\bar a\). The accompanying standalone checker tests these identities by high-accuracy circular quadrature, checks the exact rational nested-interval inequalities for integer \(\beta\), and verifies that the finite-level cover lengths tend monotonically to zero. These checks support but do not replace the analytic arguments above. In particular, no finite computation proves the measure-theoretic limits.

## Relationship to prior work

Guo and Xiao's 2026 infinitesimal circular Morera theorem assumes that a **continuous** function has defects \(o(r^2)\) at **every** center and concludes holomorphy. A published 2026 extension to locally integrable functions proves distributional convergence of normalized circle defects and a local averaged \(o(r^2)\) holomorphy criterion. Neither result states a measure-derivative if-and-only-if characterization, recovery of the **total variation** of the complex derivative measure, or the exact **singular-mass** residual after subtracting the pointwise limit. The earlier distributional convergence alone is weaker than convergence of variation: to obtain the latter one needs the positive disk-average structure and the lower-semicontinuity plus matching upper bound in Step 3. The near-Lipschitz Cantor construction identifies why almost-everywhere pointwise defects cannot replace spatial \(L^1\) control.

The variation argument is related to the classical strict approximation of measures and functions of bounded variation by nonnegative approximate identities; the essential measure-theoretic ingredients are standard. The contribution is the exact circle-integral diagnostic and its sharp pointwise-versus-variation dichotomy at the endpoint of the new circular Morera question. It is not claimed that generic strict convergence of mollified measures is new.

## Limitations

All identities are local. The characterizations require \(f\in L^1_{\mathrm{loc}}\); the measure-derivative hypothesis is indispensable for the singular-mass statement. The pointwise convergence is an almost-everywhere assertion, not one for every center. No rate of convergence of the recovered variation is claimed, and without a boundary-null hypothesis the unweighted integral over a discontinuity set need not converge. The logarithmic-Hölder examples do not contradict the everywhere-centered theorem of Guo and Xiao. The overlap assessment retains a risk that an older general result has explicitly formulated this special circular derivative diagnostic; the generic strict-convolution theorem itself is acknowledged rather than presented as novel.

## References

1. Q. Guo and A. Xiao, *An Infinitesimal Circular Morera Theorem*, arXiv:2608.04540v1, first posted 5 August 2026.
2. *An averaged infinitesimal Morera theorem for locally integrable data*, published mathematical record, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-averaged-infinitesimal-morera-theorem-for-locally-integrable--b70d8ef5227b .
3. Standard measure-theoretic results used: Riesz–Markov representation, Lebesgue differentiation of finite Radon measures, weighted lower semicontinuity of total variation, and strict approximation of Radon measures by positive approximate identities.
