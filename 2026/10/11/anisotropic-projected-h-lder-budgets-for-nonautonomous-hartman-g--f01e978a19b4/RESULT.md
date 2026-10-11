# Anisotropic projected Hölder budgets for nonautonomous Hartman–Grobman conjugacies
## Finding
Consider a nonautonomous differential equation on a Banach space with linear evolution \(U(t,s)\) and nonlinear term \(f(t,x)\). Assume the same Carathéodory hypotheses used in the classical trivial-bundle application of Rogoll and Siegmund, with \(f(t,0)=0\). Suppose the linear evolution has a strong exponential dichotomy with invariant projections \(P(t)\) and \(Q(t)=I-P(t)\), dichotomy constant \(D\ge 1\), stable and unstable decay rates \(\delta_s,\delta_u>0\), and opposite-time growth rates \(\bar\delta_s,\bar\delta_u>0\).

Assume separate projected perturbation budgets: for almost every \(t\) and all \(x,y\),
\[
\|P(t)(f(t,x)-f(t,y))\|\le \varepsilon_s\min\{1,\|x-y\|\},
\]
\[
\|Q(t)(f(t,x)-f(t,y))\|\le \varepsilon_u\min\{1,\|x-y\|\}.
\]
For
\[
0<\alpha<\alpha_0:=\min\left\{\frac{\delta_s}{\bar\delta_s},\frac{\delta_u}{\bar\delta_u}\right\},
\]
put
\[
q:=D\left(\frac{\varepsilon_s}{\delta_s}+\frac{\varepsilon_u}{\delta_u}\right)
\]
and
\[
K_\alpha:=D^{1+2\alpha}\left[
\varepsilon_s\left(\frac{D^\alpha}{\delta_s-\alpha\bar\delta_s}+\frac{1}{\delta_s+\alpha\delta_u}\right)
+\varepsilon_u\left(\frac{1}{\delta_u+\alpha\delta_s}+\frac{D^\alpha}{\delta_u-\alpha\bar\delta_u}\right)
\right].
\]
If \(q<1\) and \(K_\alpha<1\), then the Green-operator conjugacy exists and can be written \(H=\mathrm{id}+\eta\), with
\[
[\eta]_\alpha\le \frac{K_\alpha}{1-K_\alpha}.
\]
Let \(\varepsilon:=\varepsilon_s+\varepsilon_u\). The inverse correction \(H^{-1}=\mathrm{id}+\zeta\) is fiberwise \(\beta\)-Hölder for every
\[
0<\beta<\min\left\{
\frac{\delta_s}{\bar\delta_s+2D^2\varepsilon},
\frac{\delta_u}{\bar\delta_u+2D^2\varepsilon}
\right\}.
\]
More precisely, with \(M=2D^2\), one may take
\[
[\zeta]_\beta\le
DM^\beta\left[
\frac{\varepsilon_s}{\delta_s-\beta(\bar\delta_s+M\varepsilon)}+
\frac{\varepsilon_u}{\delta_u-\beta(\bar\delta_u+M\varepsilon)}
\right].
\]

This is a genuinely less restrictive sufficient condition than applying a single common perturbation budget. In the symmetric case
\[
D=1,\qquad \delta_s=\bar\delta_s=\delta_u=\bar\delta_u=\lambda,
\]
with \(\varepsilon_u=0\), the new conditions reduce to
\[
\varepsilon_s<\frac{\lambda(1-\alpha^2)}2.
\]
The common-budget hypothesis in Theorem 4.17 of arXiv:2609.40039v1 instead requires
\[
\varepsilon_s<\frac{\lambda(1-\alpha)}4.
\]
The admissible perturbation size is therefore enlarged by the exact factor \(2(1+\alpha)\); for \(\alpha=1/2\), the sufficient bound improves from \(\lambda/8\) to \(3\lambda/8\).

## Assumptions and scope
The statement is restricted to the classical trivial-bundle nonautonomous setting, where \(P(t)\) and \(Q(t)\) are projections on one Banach space and the standard Green integrals are available. The strong exponential-dichotomy conventions are those of Theorem 4.17 of arXiv:2609.40039v1: stable vectors contract forward at rate \(\delta_s\), unstable vectors contract backward at rate \(\delta_u\), and the opposite-time growth entering the Hölder estimates is controlled by \(\bar\delta_s\) and \(\bar\delta_u\). The projected min-bounds imply the full bound
\[
\|f(t,x)-f(t,y)\|\le (\varepsilon_s+\varepsilon_u)\min\{1,\|x-y\|\},
\]
which supplies existence, uniqueness, and the nonlinear-flow growth estimate used for the inverse conjugacy.

No necessity or sharpness claim is made. In particular, the inverse exponent uses the triangle-bound \(\varepsilon_s+\varepsilon_u\) and can be conservative.

## Proof
The proof keeps the stable and unstable Green branches separate instead of replacing both by one worst-case constant.

For the forward correction, let \(\mathcal F\) be the fixed-point Green operator used in the standard proof. If \(\eta,\xi\) are bounded corrections, its stable branch contains only the projected difference \(P(t)(f(t,\cdot)-f(t,\cdot))\). Integrating the stable dichotomy estimate gives
\[
\|\mathcal F_s\eta-\mathcal F_s\xi\|_\infty
\le \frac{D\varepsilon_s}{\delta_s}\|\eta-\xi\|_\infty.
\]
The unstable branch similarly gives
\[
\|\mathcal F_u\eta-\mathcal F_u\xi\|_\infty
\le \frac{D\varepsilon_u}{\delta_u}\|\eta-\xi\|_\infty.
\]
Hence \(\mathcal F\) is a contraction with constant at most \(q\). The condition \(q<1\) therefore yields the same unique bounded fixed point and topological conjugacy as the usual Green-operator construction.

For Hölder regularity, suppose \([\xi]_\alpha\le R\). The standard estimate for \(H_\xi=\mathrm{id}+\xi\) gives a factor \((1+R)\|x-y\|^\alpha\). In the stable Green branch, use \(\varepsilon_s\), not a common perturbation constant. The strong-dichotomy decomposition used in the source proof then gives
\[
I_s\le D\varepsilon_s(1+R)
\left[
\frac{(D^2)^\alpha}{\delta_s-\alpha\bar\delta_s}\|Pz\|^\alpha+
\frac{D^\alpha}{\delta_s+\alpha\delta_u}\|Qz\|^\alpha
\right].
\]
For the unstable branch,
\[
I_u\le D\varepsilon_u(1+R)
\left[
\frac{D^\alpha}{\delta_u+\alpha\delta_s}\|Pz\|^\alpha+
\frac{(D^2)^\alpha}{\delta_u-\alpha\bar\delta_u}\|Qz\|^\alpha
\right].
\]
Since \(\|Pz\|,\|Qz\|\le D\|z\|\), addition yields
\[
[\mathcal F\xi]_\alpha\le K_\alpha(1+R).
\]
When \(K_\alpha<1\), the closed Hölder ball with
\[
R=\frac{K_\alpha}{1-K_\alpha}
\]
is invariant under \(\mathcal F\). Starting the Banach iteration at zero keeps every iterate in that ball, so its uniform limit \(\eta\) obeys the claimed Hölder bound.

For the inverse, the full perturbation difference is bounded by \(\varepsilon=\varepsilon_s+\varepsilon_u\). The same variation-of-constants and Gronwall calculation as in the source gives, with \(M=2D^2\), forward and backward nonlinear-flow growth rates \(\bar\delta_u+M\varepsilon\) and \(\bar\delta_s+M\varepsilon\). Applying the separate projected bounds again inside the inverse Green integrals gives
\[
[\zeta]_\beta\le
DM^\beta\left[
\frac{\varepsilon_s}{\delta_s-\beta(\bar\delta_s+M\varepsilon)}+
\frac{\varepsilon_u}{\delta_u-\beta(\bar\delta_u+M\varepsilon)}
\right],
\]
whenever both denominators are positive. This is exactly the stated range for \(\beta\).

Finally, in the symmetric one-sided case \(D=1\), all four rates equal \(\lambda\), and \(\varepsilon_u=0\). Then \(q=\varepsilon_s/\lambda\) and
\[
K_\alpha=\frac{\varepsilon_s}\lambda\left(\frac1{1-\alpha}+\frac1{1+\alpha}\right)
=\frac{2\varepsilon_s}{\lambda(1-\alpha^2)}.
\]
Thus \(K_\alpha<1\) is equivalent to \(\varepsilon_s<\lambda(1-\alpha^2)/2\), while the source's displayed common-budget condition gives \(\varepsilon_s<\lambda(1-\alpha)/4\). Their ratio is \(2(1+\alpha)\).

## Verification
The argument was checked term by term against the Green-operator proof of Theorems 4.14 and 4.17 in arXiv:2609.40039v1. In that proof the stable and unstable contributions are already written as separate integrals; replacing the common perturbation constant by \(\varepsilon_s\) in the stable branch and \(\varepsilon_u\) in the unstable branch gives the displayed formulas without changing any dichotomy estimate. The inverse estimate was independently reconstructed from the source's variation-of-constants inequality using the full bound \(\varepsilon_s+\varepsilon_u\).

The symmetric specialization was simplified algebraically:
\[
\frac1{1-\alpha}+\frac1{1+\alpha}=\frac2{1-\alpha^2}.
\]
No finite experiment, numerical fit, or unproved limiting argument is used.

## Relationship to prior work
Rogoll and Siegmund prove a common-budget Hölder theorem on Banach bundles and, in their classical nonautonomous application, explicitly observe that the topological Green-operator proof can use projected perturbations \(P(t)f\) and \(Q(t)f\) instead of a full perturbation bound. Their projected remark still uses one common constant for both branches and does not state a Hölder theorem with unequal projected budgets. The present result combines the two proof features and retains separate stable and unstable constants throughout both the contraction and Hölder estimates.

Barreira and Valls established Hölder Grobman–Hartman linearization and later a direct nonuniform-flow theorem. Their accessible abstracts confirm Hölder regularity and Lyapunov-ratio control but do not state the branchwise projected budget criterion above. A bounded search did not locate an implication-equivalent published statement.

## Limitations
The result is only a sufficient theorem. It does not prove that \(q<1\), \(K_\alpha<1\), or the stated inverse exponent is optimal. The inverse estimate deliberately uses \(\varepsilon_s+\varepsilon_u\) in the nonlinear-flow Gronwall bound, so additional structure could improve it. The theorem is stated only for the classical trivial-bundle setting; extending the unequal projected budgets to the full abstract Banach-bundle framework requires checking the corresponding bundle regularity hypotheses and is not claimed here.

The full text of the 2011 Barreira–Valls flow paper was not available through the lawful sources inspected in the bounded comparison search. Its abstract and bibliographic record were checked, leaving a residual possibility that an equivalent componentwise estimate appears there under different notation.

## References
1. B. Rogoll and S. Siegmund, *A Hartman–Grobman theorem on Banach bundles*, arXiv:2609.40039v1, 2026.
2. L. Barreira and C. Valls, *A simple proof of the Grobman-Hartman theorem for nonuniformly hyperbolic flows*, Nonlinear Analysis 74 (2011), 7210–7225, doi:10.1016/j.na.2011.07.036.
3. L. Barreira and C. Valls, *Hölder Grobman-Hartman linearization*, Discrete and Continuous Dynamical Systems 18 (2007), 187–197, doi:10.3934/dcds.2007.18.187.
