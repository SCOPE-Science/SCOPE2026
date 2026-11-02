# Global Bernoulli mixing and boundary recovery for critical cusp maps

## Finding
Fix any two distinct parameters \(1<\theta_0<\theta_1<2\). Let \(P_p=(1-p)\mathcal L_{\theta_0}+p\mathcal L_{\theta_1}\) be the annealed Perron--Frobenius operator of the critical square-root cusp maps specified below. For **every** \(p\in[0,1]\), not merely for a small perturbation of either pure map, \(P_p\) has a unique normalized nonnegative fixed point \(h_p\in W^{2,1}(0,1)\). Its eigenvalue \(1\) is algebraically simple and is its only peripheral spectral value. There are constants \(C<\infty\) and \(0<\tau<1\), dependent on the fixed pair of maps but **independent of** \(p\), such that for every \(n\ge0\) and \(\phi\in W^{2,1}(0,1)\),
\[
\left\|P_p^n\phi-h_p\int_0^1\phi\,dx\right\|_{W^{2,1}}\le C\tau^n\|\phi\|_{W^{2,1}}.
\]
The map \(p\mapsto h_p\) extends real-analytically, as a \(W^{2,1}\)-valued map, to a real neighborhood of the **entire closed** interval \([0,1]\).

Furthermore, the right-endpoint Peano jet of \(h_p\) recovers \(p\) **for the entire parameter interval**. Specifically, if \(h_p(1-z)=\alpha_1z+\alpha_2z^2+\alpha_3z^3+o(z^3)\), put \(K_j=(1-\theta_j/2)/\sqrt 2\), \(a_j=K_j^{-2}\), \(r_j=\theta_j a_j\), and \(T=-4\alpha_2/(3\alpha_1)\). Then
\[
 p=\frac{a_0(T-r_0)}{a_0(T-r_0)+a_1(r_1-T)}\quad(0\le p\le1),
\]
with the endpoint convention given by continuous extension. Moreover,
\[
9\alpha_1\alpha_3-10\alpha_2^2=\frac{45}{8}h_p(1/2)^2p(1-p)a_0a_1(r_1-r_0)^2.
\]
Consequently the discriminant is strictly positive precisely for genuine mixtures \(0<p<1\), and vanishes at the two pure endpoints. The local near-zero recovery formulas are known in a preceding restricted analysis; the contribution here is their **global validity**, supported by a nonperturbative uniform spectral theorem.

## Assumptions and scope
Write \(I=[0,1]\), \(c=1/2\), and for each \(1<\theta<2\) define
\[
K_\theta=\frac{1-\theta/2}{\sqrt2},\qquad
 f_\theta(c\pm t)=1-\theta t-2K_\theta\sqrt t\quad(0\le t\le1/2).
\]
Each of the two monotone branches maps its closed half-interval onto \(I\) and has derivative magnitude \(\theta+K_\theta t^{-1/2}\ge1+\theta/2>1\). Denote by \(\mathcal L_\theta\) its Lebesgue transfer operator (positive and integral-preserving). For every Bernoulli parameter \(p\in[0,1]\), \(P_p\) acts on real or complex \(W^{2,1}(I)\) by convex combination. The maps and the distribution are fixed in time; the theorem concerns the annealed transfer operator, not samplewise/random quenched rates. Norms have no boundary conditions. Constants can depend on \(\theta_0,\theta_1\), not on \(p,n\).

## Proof
**1. A uniform second-order Doeblin--Fortet bound.** Proposition 4.1 of Oltiboev--Vafoyev supplies for each fixed \(\theta_j\) the crucial critical-cusp cancellation and
\[
\|\mathcal L_{\theta_j}\phi\|_{W^{2,1}}\le \lambda_j^2\|\phi\|_{W^{2,1}}+C_j\|\phi\|_{W^{1,1}},\qquad \lambda_j=(1+\theta_j/2)^{-1}<1.
\]
Both operators contract \(L^1\) and preserve its integral. Taking convex combinations, with \(\rho=\max_j\lambda_j^2<1\) and \(C_0=\max_jC_j\), yields uniformly in \(p\)
\[
\|P_p\phi\|_{W^{2,1}}\le\rho\|\phi\|_{W^{2,1}}+C_0\|\phi\|_{W^{1,1}}.
\]
The standard compact-interpolation inequality \(\|\phi\|_{W^{1,1}}\le\eta\|\phi\|_{W^{2,1}}+C_\eta\|\phi\|_1\) yields, with one fixed \(b\in(\rho,1)\),
\[
\|P_p^n\phi\|_{W^{2,1}}\le b^n\|\phi\|_{W^{2,1}}+\frac{C_b}{1-b}\|\phi\|_1.
\]
By compactness \(W^{2,1}(I)\hookrightarrow L^1(I)\) and the usual quasi-compactness criterion, the essential spectral radii of all \(P_p\) on \(W^{2,1}\) are at most \(b<1\). Here the constants \(b,C_b\) can be chosen simultaneously for all \(p\). Note that an elementary spectral-radius argument alone would not prove absence of additional unit-circle eigenvalues.

**2. Topological exactness and peripheral rigidity.** For either fixed map \(f_{\theta_j}\), the inverse branches contract with Lipschitz constant at most \(\lambda_j\). Every nonempty open subinterval of \((0,1)\) therefore contains a full inverse cylinder for a sufficiently large iterate; each such cylinder maps onto \(I\). This is the full-branch topological-exactness property, also established in Oltiboev--Vafoyev, Proposition 4.2. If \(q_j>0\) is the Bernoulli probability of that map (at least one of the two probabilities is positive), then \(P_p^n\) contains the strictly positive summand \(q_j^n\mathcal L_{\theta_j}^n\). Consequently, for every nonzero nonnegative \(v\in C(I)\) satisfying \(P_pv=v\), there is a cylinder inside an interval on which \(v\) is bounded below, and \(v(x)>0\) at every \(x\in(0,1)\).

Integral preservation implies that the integral functional is fixed by \(P_p^*\), so \(1\) lies in the spectrum of \(P_p\). Quasi-compactness makes it an eigenvalue. For an eigenfunction \(\psi\in W^{2,1}\) with \(P_p\psi=\zeta\psi\), \(|\zeta|=1\), positivity gives \(P_p|\psi|\ge|\psi|\). Equality of integrals forces equality (as continuous functions); thus \(v=|\psi|\) is stationary and strictly positive on \((0,1)\). Let \(u(x)=\psi(x)/|\psi(x)|\), continuous on that open interval. Equality in the triangle inequality for the full positive inverse-branch sum implies, for **every** rank-\(n\) inverse cylinder \(J\) of the fixed positive-probability map, and every interior \(x\),
\[
u(g_J(x))=\zeta^n u(x).
\]
Choose a nested sequence of rank-\(n\) cylinders \(J_n\) contained in one compact interval strictly inside \((0,1)\). Their diameters tend to zero. For arbitrary \(x,y\in(0,1)\), both \(g_{J_n}(x)\) and \(g_{J_n}(y)\) lie in \(J_n\); continuity of \(u\) there therefore forces \(u(x)=u(y)\). Thus \(\psi\) has constant complex phase; positivity of \(v\) and \(P_pv=v\) then forces \(\zeta=1\).

For geometric simplicity, take any two normalized fixed functions; their difference \(\psi\) has zero integral and is again a fixed eigenfunction. The same constant-phase argument forces \(\psi\equiv0\). All spectral eigenfunctions at \(1\) are scalar multiples of a positive normalized \(h_p\). A Jordan chain at eigenvalue \(1\) would create linear growth of \(P_p^n\) in \(L^1\), contradicting its \(L^1\) contraction. Eigenvalues of modulus above one are similarly excluded. Thus \(1\) is algebraically simple and is the only unit-circle spectral value for **each** \(p\in[0,1]\).

**3. Uniformity and analyticity on the closed parameter range.** The family \(P_p\) is affine and norm-continuous in \(p\) on \(W^{2,1}\). At each \(p\), quasi-compactness plus Step 2 gives an isolated simple eigenvalue at \(1\) and a strictly smaller complementary spectral radius. The Riesz projections depend analytically on \(p\) in a complex neighborhood of each point. A finite subcover of compact \([0,1]\), together with resolvent bounds on the complementary subspaces, provides constants \(C<\infty\), \(\tau<1\) common to all parameters. Integral normalization identifies the simple Riesz projection with \(\phi\mapsto h_p\int\phi\), and provides the claimed analytic branch. Even at the endpoints this branch analytically extends slightly beyond the stochastic interval, without asserting positivity outside \([0,1]\).

**4. Complete-interval boundary jet.** The exact two inverse branches and their common Jacobian weight are
\[
 u_\theta(x)=\frac{\sqrt{K_\theta^2+\theta(1-x)}-K_\theta}{\theta},\quad
 g_{\pm,\theta}(x)=c\pm u_\theta(x)^2,\quad
 w_\theta(x)=\frac{u_\theta(x)}{K_\theta+\theta u_\theta(x)}.
\]
Since \(h_p\in W^{2,1}\hookrightarrow C^1\), the symmetric evaluation satisfies \(h_p(c+u^2)+h_p(c-u^2)=2h_p(c)+o(u^2)=2h_p(c)+o(z^2)\) as \(x=1-z\uparrow1\). A Taylor expansion of the **explicit** weight yields
\[
2w_{\theta_j}(1-z)=a_j z-\tfrac34 a_j r_j z^2+\tfrac58a_j r_j^2z^3+O(z^4).
\]
Stationarity and the extra \(z\) from the weight prove the Peano expansion with
\[
\alpha_1=h_p(c) A_p,\quad \alpha_2=-\tfrac34h_p(c) B_p,\quad \alpha_3=\tfrac58h_p(c)C_p,
\]
where \(A_p=(1-p)a_0+pa_1\), \(B_p=(1-p)a_0r_0+pa_1r_1\), and \(C_p=(1-p)a_0r_0^2+pa_1r_1^2\). Step 2 gives \(h_p(c)>0\), and \(r_1>r_0\) because \(\theta\mapsto\theta/K_\theta^2\) increases on \((1,2)\). Solving \(T=B_p/A_p\) for \(p\) proves the recovery formula throughout \([0,1]\), including endpoints. Expanding \(A_pC_p-B_p^2=p(1-p)a_0a_1(r_1-r_0)^2\) gives the discriminant identity. These coefficients are Peano asymptotic coefficients, not a claim that the density has three classical endpoint derivatives.

## Verification
Every step above is analytic; the required nonstandard cancellation/Lasota--Yorke estimate is sourced from Oltiboev--Vafoyev, Proposition 4.1, whose assumptions match the explicitly fixed maps. Its topological-exactness argument in Proposition 4.2 is reused for each positive-probability component. The finite source-independent script `verify_boundary.py` checks exact rational-arithmetic forms of the boundary coefficient expansion, inversion, monotonicity sign and discriminant at both endpoints and several interior mixing weights. Finite identities do **not** certify infinite-dimensional spectral properties; those are established by the proof above.

## Relationship to prior work
Oltiboev--Vafoyev prove critical-cusp cancellation, \(W^{2,1}\) spectral mixing for each single map, and analytic response under a **sufficiently small** Bernoulli perturbation (Theorem 6.1). Their statements do not provide simultaneous spectral mixing for every convex-mixture weight, uniform constants over the closed probability interval, or globally analytic response. The earlier Oltiboev--Rakhimov--Ruziboev random-map study assumes a strict cusp exponent less than \(-1/2\) and treats small changes of the law, so it does not cover the critical square-root case. An earlier restricted result gives precisely the boundary-jet recovery and discriminant formulas for sufficiently small \(p\); **those local formulas alone are not the new claim**. The new contribution is the global, nonperturbative spectral theorem and the consequent extension of the exact identification/diagnostic statement to all \(p\). General quasi-compactness and Riesz-projection tools are standard and not claimed as innovations.

## Limitations
The result concerns two fixed maps from the stated full-branch family and their **annealed** operator. It does not supply an explicit numerical formula for the optimal uniform spectral contraction rate, a quenched random-orbit decay rate, or a multi-map parameter identification theorem. The proof uses established second-order operator estimates that have been inspected in the source; it is not an independently formalized verification. While the original primary and closest records were inspected, broader historical random expanding-map theorems could offer a more general route to the global mixing portion; this priority risk remains.

## References
1. D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, **ACTA NUUz**, 2(2.3), 178--183 (issue published 2026-10-06); arXiv:2610.23180v1 (2026-10-16), https://borowiecki.dev/abs/2610.23180 . Proposition 4.1, Proposition 4.2 and Theorem 6.1 are especially relevant.
2. D. Oltiboev, K. Rakhimov, and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (2026-08-27), https://arxiv.org/abs/2608.26969 .
3. H. Hennion, *Sur un théorème spectral et son application aux noyaux lipschitziens*, Proc. Amer. Math. Soc. 118 (1993), 627--634. Quasi-compactness criterion, as used in reference 1.
