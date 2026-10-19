# A wrong-sign critical logarithm in quasi-static pairwise SIS reduction

## Finding

A quasi-static reduction of the classical pair-closed susceptible–infectious–susceptible (SIS) model predicts the correct epidemic threshold and the leading critical prevalence decay, but it does not predict the first logarithmic correction. Indeed, in every integer degree \(n\ge4\) it predicts the **opposite sign** of that correction. The discrepancy is independent of the recovery timescale \(\gamma>0\) and is a consequence of the curvature of the true slow invariant manifold, not of different threshold choices.

For all integers \(n\ge3\), put
\[
A_n=\frac{2(n-1)^2}{n(2n-1)},\qquad
L_n=\frac{4n-3}{(2n-1)^2},\qquad
\widetilde L_n=-\frac{2n^3-10n^2+9n-2}{n(2n-1)^2}.
\]
For the full system, and for any physical positive initial data sufficiently close to its critical disease-free point, there is a finite constant \(K_f\) such that
\[
\frac1{i(t)}=\gamma A_nt+L_n\log t+K_f+o(1),\qquad t\to\infty.
\]
For the corresponding scalar quasi-static approximation, every sufficiently small initial \(j(0)>0\) admits a finite \(K_q\) with
\[
\frac1{j(t)}=\gamma A_nt+\widetilde L_n\log t+K_q+o(1).
\]
The sharp, degree-dependent coefficient gap is
\[
L_n-\widetilde L_n=\frac{2(n-1)^3}{n(2n-1)^2}>0.
\]
At degree \(n=4\), the full coefficient is \(13/49\), whereas the quasi-static coefficient is \(-1/98\). For trajectories of the two systems with arbitrary fixed sufficiently small positive initial prevalences, the difference of inverse prevalences therefore has the universal logarithmic slope \(27/98\), after subtracting their (common) linear-in-time term.

## Assumptions and scope

Fix an integer network degree \(n\ge3\) and recovery rate \(\gamma>0\). At the critical transmission parameter \(\tau=\gamma/(n-1)\), let \(i\) be infection prevalence and \(p\) the susceptible-neighbor proportion conditional on infection. The pair-closed deterministic system from the cited primary model is
\[
\begin{aligned}
\dot i&=i(\tau np-\gamma),\\
\dot p&=\gamma(1-p)+\tau(n-2)p-\tau np^2
-\frac{2\tau(n-1)p^2i}{1-i}.
\end{aligned}
\tag{1}
\]
The critical disease-free point is \((i,p)=(0,p_c)\), where \(p_c=(n-1)/n\). It is a regular boundary point of system (1) when \(i=0\); nevertheless \(i>0\) is preserved by the factorization of \(\dot i\). A **physical local initial state** means \(0<i(0)<\varepsilon\), \(0<p(0)<1\), and \(|p(0)-p_c|<\varepsilon\), for a sufficiently small \(\varepsilon>0\); the usual pair constraints \(ip\le 1-i\) and \(ip\le i\) also hold automatically after shrinking \(\varepsilon\).

Define \(q(j)\), for \(j\) near zero, to be the unique root near \(p_c\) of the fast equation \(\dot p=0\) with \(i=j\). The **quasi-static comparison** is the exact scalar ODE
\[
\dot j=j(\tau n q(j)-\gamma),\qquad 0<j(0)<\varepsilon.
\tag{2}
\]
This theorem concerns (1) and (2) at exactly critical transmission, fixed \(n,\gamma\), and near the disease-free point. The constants \(K_f,K_q\) depend on the initial states and the time unit; the coefficients of \(\log t\) do not.

## Proof

**1. Hyperbolic fast mode and common tangent.** Divide the vector field by \(\gamma\), writing \(F(i,p)=\dot i/\gamma\) and \(G(i,p)=\dot p/\gamma\). Direct evaluation at \((0,p_c)\) gives \(F_i=0\), \(F_p=0\), and
\[
G_p(0,p_c)=-\frac{2n-1}{n-1}<0,\qquad
G_i(0,p_c)=-\frac{2(n-1)^2}{n^2}.
\]
The eigenvalues are zero and \(-\gamma(2n-1)/(n-1)\). The implicit-function theorem gives an analytic quasi-static graph \(p=q(i)\). The smooth center-manifold theorem gives an invariant graph \(p=h(i)\) tangent to the center eigendirection. Write
\[
q(i)=p_c+a_ni+b_{q,n}i^2+O(i^3),\qquad
h(i)=p_c+a_ni+b_{h,n}i^2+O(i^3).
\]
Implicit differentiation of \(G(i,q(i))=0\), or the order-one center invariance identity, gives the *same* slope
\[
a_n=-\frac{2(n-1)^3}{n^2(2n-1)}<0.
\tag{3}
\]

**2. Different invariant-graph curvatures.** The quasi-static graph is defined by \(G(i,q(i))=0\), whereas invariance of the actual center graph is \(G(i,h(i))=h'(i)F(i,h(i))\). On either graph, the prevalence equation starts at order two:
\[
F(i,p_c+a_ni+O(i^2))=-A_ni^2+O(i^3),\qquad
A_n=-\frac{n a_n}{n-1}>0.
\]
Since \(G_p(0,p_c)=-(2n-1)/(n-1)\), subtracting the order-two graph equations gives
\[
-\frac{2n-1}{n-1}(b_{h,n}-b_{q,n})=-a_nA_n,
\qquad
b_{q,n}-b_{h,n}=\frac{4(n-1)^6}{n^3(2n-1)^3}.
\tag{4}
\]
In particular, explicit expansion gives
\[
\begin{aligned}
b_{h,n}&=-\frac{2(n-1)^3(4n-3)}{n^2(2n-1)^3},\\
b_{q,n}&=\frac{2(n-1)^3(2n^3-10n^2+9n-2)}{n^3(2n-1)^3}.
\end{aligned}
\tag{5}
\]
These are the coefficients of the actual invariant graph and the algebraic nullcline, respectively; the latter is not generally invariant.

**3. Critical scalar equations.** Substitution into \(\dot i=\gamma i(np/(n-1)-1)\) gives the center-manifold and quasi-static equations
\[
\begin{aligned}
\dot i&=-\gamma A_ni^2+\gamma C_{h,n}i^3+O(i^4),\\
\dot j&=-\gamma A_nj^2+\gamma C_{q,n}j^3+O(j^4),
\end{aligned}
\tag{6}
\]
where
\[
\begin{aligned}
C_{h,n}&=-\frac{2(n-1)^2(4n-3)}{n(2n-1)^3},\\
C_{q,n}&=\frac{2(n-1)^2(2n^3-10n^2+9n-2)}{n^2(2n-1)^3}.
\end{aligned}
\tag{7}
\]
The positive quadratic damping \(A_n>0\) makes the center equilibrium attracting from positive \(i\); the exponentially stable fast eigenvalue makes the full equilibrium locally asymptotically stable on the physical half-neighborhood. More explicitly, for a sufficiently smooth local invariant graph \(h\), the transverse deviation \(e(t)=p(t)-h(i(t))\) satisfies \(\dot e=\gamma[-(2n-1)/(n-1)+O(i)+O(e)]e\), hence \(|e(t)|\le C e^{-ct}\) for some \(c>0\) once the orbit remains in a small forward-invariant neighborhood. Local center-manifold stability supplies such a neighborhood for the stated positive initial data.

**4. Full-trajectory asymptotics.** Let \(u=1/i\). Since \(i>0\), the exact equation and the transverse estimate give
\[
\dot u=\gamma A_n-\frac{\gamma C_{h,n}}u+O(u^{-2})+O(e^{-ct}u).
\tag{8}
\]
The integrable coefficient in the last term, together with \(u\ge1/\varepsilon\), yields \(u=O(1+t)\) by Grönwall's inequality. Consequently \(e^{-ct}u\) is integrable and \(\dot u=\gamma A_n+o(1)\), so \(u/(\gamma A_nt)\to1\). A second integration of (8) gives \(u=\gamma A_nt+O(\log t)\). Therefore
\[
\frac1{u(t)}=\frac1{\gamma A_nt}+O\!\left(\frac{\log t}{t^2}\right).
\]
Inserting this in (8) shows that the derivative of \(u-\gamma A_nt+(C_{h,n}/A_n)\log t\) is integrable on every sufficiently late half-line. It thus converges to a finite constant \(K_f\), proving
\[
\frac1{i(t)}=\gamma A_nt-\frac{C_{h,n}}{A_n}\log t+K_f+o(1).
\tag{9}
\]
The same reciprocal integration without a transverse error applies to (2), giving the coefficient \(-C_{q,n}/A_n\). Substitution of (7) yields the stated closed formulas.

**5. Strict sign reversal and sharp difference.** For \(n\ge3\), \(L_n=(4n-3)/(2n-1)^2>0\). The numerator of \(-\widetilde L_n\) is the polynomial \(P(n)=2n^3-10n^2+9n-2\). One has \(P(3)=-11\), \(P(4)=2\), and \(P'(n)=6n^2-20n+9>0\) for all real \(n\ge4\). Thus \(\widetilde L_n<0\) for every integer \(n\ge4\). Finally (4) or (7) yields
\[
L_n-\widetilde L_n=\frac{2(n-1)^3}{n(2n-1)^2},
\]
as claimed. There is no finite-size stochastic inference in this deterministic calculation.

## Verification

The standalone `verify.py` uses exact symbolic algebra to check the nullcline and center-invariance coefficients, both reciprocal-logarithm coefficients, their difference, and exact examples at degrees three and four. Execute `python verify.py` after installing `sympy` from `requirements.txt`; success prints its assertions-passed message. The proof of infinite-time asymptotics is analytic and does not rely on finite simulation. Independent high-accuracy integrations of the full and scalar systems at degrees three, four and six corroborated the opposing-sign and coefficient-gap behavior; finite-time slopes remain affected by the subleading remainder.

## Relationship to prior work

Hébert-Dufresne, Simon and Kiss (2026, equations (5)–(6), (17)–(23), Appendix 6.2.1 and Table 1) supply the exact pairwise ODE and the algebraic fast-variable reduction, and explicitly calculate the **first-order** effective-infection expansion determining the continuous threshold. This work does not claim the pairwise closure, threshold, quasi-static root, or leading critical quadratic damping as new. The additional finding is the higher-order distinction between the *actual center invariant graph* and the *fast nullcline* and the resulting opposite-sign logarithmic extinction correction at all degrees at least four.

Classical center-manifold methods explain why a fast nullcline may differ from the slow invariant graph; generic theory does not supply the specific degree-dependent coefficients without this computation. Other SIS pair-approximation research concerns network thresholds, quasistationary distributions, or endemic equilibria rather than the two critical reciprocal-prevalence logarithms for this precise deterministic closure. The 2021 super-compact pairwise model analyzes a distinct, higher-dimensional heterogeneous-degree approximation, not the same system.

## Limitations

The theorem is local near the critical disease-free equilibrium for fixed integer degree and deterministic pair closure; it does not establish global convergence from every feasible initial state. It does not compare with stochastic finite-graph SIS extinction, estimate observational noise, cover heterogeneous degrees or extra contagion channels, or claim uniformity in degree or recovery rate. The constants \(K_f,K_q\) are initial-state dependent. Analytically established mathematical coefficients do not constitute independent assessment of historical priority; a still-undetected more general prior theorem may imply them.

## References

1. Laurent Hébert-Dufresne, Péter L. Simon, and István Z. Kiss, *Fast-variable reduction to complex contagion unifies epidemic models*, arXiv:2610.05467v1, posted 2026-10-04, https://arxiv.org/abs/2610.05467. Full primary text, especially §3 and Appendix §6.2.1.
2. István Z. Kiss, Joel C. Miller, and Péter L. Simon, *Mathematics of Epidemics on Networks: From Exact to Approximate Models*, Springer, 2017.
3. *A Low-Dimensional Network Model for an SIS Epidemic: Analysis of the Super Compact Pairwise Model*, *Bulletin of Mathematical Biology*, 2021, https://doi.org/10.1007/s11538-021-00907-2.
4. George T. Cantwell and Cristopher Moore, *Threshold and quasistationary distribution for the susceptible-infectious-susceptible model on networks*, *Physical Review E* **113** (2026), 064305, https://doi.org/10.1103/385j-2f29.
