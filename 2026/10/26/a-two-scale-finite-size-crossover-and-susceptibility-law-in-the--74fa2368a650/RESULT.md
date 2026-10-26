# A two-scale finite-size crossover and susceptibility law in the cubic mean-field Ising model

## Finding

The cubic mean-field Ising model has a finite-size crossover connecting a nonsymmetric quartic critical law to a universal two-phase switching profile. At the critical scale, \(N^{1/4}m_N\) approaches an explicit quartic-density family. At the onset of coexistence, that family has a previously unobvious reflection symmetry: the two wells have exactly equal weight despite the cubic spin interaction. In the more sharply separated two-phase regime the finite-size magnetization has logistic switching probabilities, and the normalized equilibrium susceptibility has the exact \(\operatorname{sech}^2\) profile.

More precisely, for fixed \(\kappa\geq0\), \(j,\eta\in\mathbb R\), let
\[
K_N=\kappa N^{-1/4},\qquad J_N=1+jN^{-1/2},\qquad h_N=\eta N^{-3/4}.
\]
Then \(N^{1/4}m_N\) converges in law, with convergence of every fixed absolute moment, to the density
\[
\rho_{\kappa,j,\eta}(x)=\frac{1}{Z_{\kappa,j,\eta}}\exp\!\left(-\frac{x^4}{12}+\frac{\kappa x^3}{3}+\frac{j x^2}{2}+\eta x\right),\qquad x\in\mathbb R.
\]
At \(\eta=0\) and \(j=-2\kappa^2/3\), the exponent becomes \(-x^2(x-2\kappa)^2/12\). Thus for \(\kappa>0\) the maxima are \(0\) and \(2\kappa\), the minimum is \(\kappa\), the barrier is \(\kappa^4/12\), and \(\mathbb P(X<\kappa)=\mathbb P(X>\kappa)=1/2\) with \(\mathbb E X=\kappa\). For \(\kappa=0\) both peaks merge.

For the separate mesoscopic regime let \(K_N>0\), \(K_N\to0\), \(NK_N^4\to\infty\), and fix \(t\in\mathbb R\). Let \(\gamma(K)\) be the zero-field coexistence value of \(J\) for which the variational free energy has global maximizers at zero and at a unique positive \(m_*(K)\). Set \(h_N=0\) and
\[
J_N=\gamma(K_N)+\frac{t}{N K_N^2}.
\]
Then, with convergence of all fixed absolute moments,
\[
\frac{m_N}{K_N}\Longrightarrow (1-p_t)\delta_0+p_t\delta_2,\qquad p_t=\frac{e^{2t}}{1+e^{2t}}.
\]
In particular, for \(\chi_N=\partial_h^2[N^{-1}\log Z_N]\vert_{h=0}=N\operatorname{Var}(m_N)\),
\[
\frac{\mathbb E[m_N]}{K_N}\to1+\tanh t,\qquad \frac{\chi_N}{N K_N^2}\to\operatorname{sech}^2t.
\]
The coexistence curve and positive magnetization admit
\[
\gamma(K)=1-\frac{2K^2}{3}+\frac{16K^4}{15}+O(K^6),\qquad m_*(K)=2K-\frac{32K^3}{5}+O(K^5).
\]
All assertions hold with no spatial interactions beyond the stated mean-field Hamiltonian.

## Assumptions and scope

There are \(N\ge1\) spins \(\sigma_i\in\{-1,+1\}\), magnetization \(m_N=N^{-1}\sum_i\sigma_i\), and exactly the Gibbs distribution
\[
\mu_{N,K,J,h}(\sigma)=\frac{1}{Z_N(K,J,h)}\exp\!\left\{N\left(\frac K3m_N^3+\frac J2m_N^2+h m_N\right)\right\}.
\]
Couplings are dimensionless at inverse temperature one, with no additional entropy factor hidden in their definitions. A coexistence branch is only needed for sufficiently small positive \(K\); its existence and uniqueness as a global phase boundary follow from the small-\(K\) argument in the proof. The two limits refer to distinct parameter sequences, not an assertion of uniform convergence when \(\kappa\) grows simultaneously with \(N\).

## Proof

**1. Exact magnetization weights and uniform entropy control.** For lattice magnetizations \(m=(2r-N)/N\),
\[
\mathbb P(m_N=m)\ \propto\ \binom Nr\exp\{N[K m^3/3+Jm^2/2+hm]\}.
\]
Let \(I(m)=[(1+m)\log(1+m)+(1-m)\log(1-m)]/2\), with the continuous endpoint interpretation, and \(F_{K,J,h}(m)=K m^3/3+Jm^2/2+hm-I(m)\). The entropy rate has
\[
I(m)=\sum_{q\ge1}\frac{m^{2q}}{2q(2q-1)}=\frac{m^2}{2}+\frac{m^4}{12}+\frac{m^6}{30}+O(m^8)
\]
for \(|m|<1\), and \(I(m)\ge m^2/2+m^4/12\) on \([-1,1]\). Stirling's formula uniformly on interior compact subintervals yields binomial weight \(2^N\sqrt{2/(\pi N(1-m^2))}\,e^{-NI(m)}(1+o(1))\). A standard uniform binomial upper bound controls the endpoints. These bounds and the quartic inequality give uniform integrable tails at the scales below.

**2. The quartic critical window.** Put \(m=N^{-1/4}x\). The critical Gaussian term cancels:
\[
N F_{K_N,J_N,h_N}(N^{-1/4}x)=-\frac{x^4}{12}+\frac{\kappa x^3}{3}+\frac{j x^2}{2}+\eta x+O(N^{-1/2}x^6)
\]
locally uniformly in \(x\). The lattice spacing in \(x\) is \(2N^{-3/4}\), and the Stirling prefactor tends uniformly to one on compact \(x\)-sets. For bounded fixed parameters, \(N F\le -x^4/12+|\kappa||x|^3/3+|j|x^2/2+|\eta||x|\), which is a global integrable envelope after allowing a harmless common normalization factor. The magnetization Riemann sums converge to the stated density, and the same quartic domination with polynomial factors gives convergence of all fixed moments. At \(j=-2\kappa^2/3\), completing the polynomial identity proves exact reflection and equal masses.

**3. Small-coupling coexistence location.** With \(m=Ky\) and \(J=1+aK^2\), uniformly for bounded \(y,a\),
\[
K^{-4}F_{K,J,0}(Ky)=\frac{ay^2}{2}+\frac{y^3}{3}-\frac{y^4}{12}+O(K^2).
\]
At \(a=-2/3\) the limit is \(-y^2(y-2)^2/12\), with exactly two nondegenerate global maxima, \(y=0\) and \(y=2\); its second derivatives there equal \(-2/3\). The two equations \(F(Ky)=0\) and \(\partial_mF(Ky)=0\), divided by \(K^4\) and \(K^3\) respectively, have a nonsingular Jacobian with respect to \((a,y)\) at \((-2/3,2,0)\): their diagonal entries are \(2\) and \(-2/3\), and their upper-right entry is zero. The analytic implicit-function theorem supplies \(a(K^2)\) and \(y(K^2)\). The limiting polynomial and entropy tail bound, together with continuity of the known cubic-model phase portrait, rule out a third competing global maximizer at sufficiently small positive \(K\). Expanding both equations to the next orders gives \(a=-2/3+(16/15)K^2+O(K^4)\) and \(y=2-(32/5)K^2+O(K^4)\), proving the stated expansions. In particular, at coexistence the two second derivatives obey \(F''(0)=-(2/3)K^2+O(K^4)\) and \(F''(m_*)=-(2/3)K^2+O(K^4)\).

**4. The separated-well, shrinking-coexistence window.** Set \(K=K_N\) and \(\delta J=t/(NK^2)\). Since \(NK^4\to\infty\), \(\delta J/K^2=t/(NK^4)\to0\), so both nondegenerate wells persist on the natural \(K\) magnetization scale. Their Gaussian widths are \(O((NK^2)^{-1/2})=o(K)\). A Taylor expansion around each moving well has normalized cubic and quartic errors bounded on fixed Gaussian windows by \(O((NK^4)^{-1/2})\) and \(O((NK^4)^{-1})\), respectively; the global entropy bound controls the complement. The binomial Stirling prefactors at both wells tend to the same value, as does the ratio of their Gaussian curvature prefactors. To first order in \(\delta J\), the excess exponential weight of the positive well is
\[
N\delta J\,\frac{m_*(K)^2}{2}+o(1)=\frac{t}{K^2}\frac{(2K+O(K^3))^2}{2}+o(1)=2t+o(1).
\]
The well displacement is \(O(\delta J/K)\); its correction to the logarithmic well weight is \(O(N\delta J^2)=O((NK^4)^{-1})=o(1)\). Thus the relative masses tend to \(1:e^{2t}\) and the rescaled well centers to \(0:2\). Gaussian tail bounds on the scaled coordinates also yield convergence of every fixed absolute moment. Finally differentiating the finite partition function in \(h\) gives \(\chi_N=N\operatorname{Var}(m_N)\), and the variance of the limiting two-point law is \(4p_t(1-p_t)=\operatorname{sech}^2t\). This proves all claims.

## Verification

An accompanying standalone Python script, `CHECK.py`, computes normalized finite-\(N\) spin-count weights using log-gamma factorials, verifies representative reflection-symmetric quartic moments by quadrature, and checks the small-\(K\) coexistence expansions by solving the exact stationary and equal-energy equations numerically. These finite computations are corroboration only; the infinite-volume statements are proved by the entropy expansion, uniform localization and analytic implicit-function argument above.

## Relationship to prior work

Contucci, Mingione and Osabutey (2023) rigorously establish the cubic model's fixed-parameter phase structure, Gaussian fluctuation laws and quartic non-Gaussian law at the isolated critical point. The present claim instead treats moving, size-dependent cubic and quadratic couplings and identifies the explicit interpolation between overlapping critical wells and fully separated coexistence peaks, including the susceptibility switching profile. Contucci, Osabutey and Vernia (2022) study parameter inference and numerical finite-size behavior of the same cubic Hamiltonian, without the stated double-scaling limit. Gandolfo, Ruiz and Wouts (2008) provide closely related fixed-parameter saddle/coexistence limits for a different, Potts Hamiltonian; their stated nondegenerate-well coexistence theorem does not directly apply as the well curvatures vanish along a triangular array. The method remains classical Laplace asymptotics, and related general uniform saddle-point results remain a possible source of implicit prior coverage.

## Limitations

The theorem concerns the stated complete-graph mean-field equilibrium model and small nonnegative cubic coupling. It does not describe real-space Ising chains, dynamics, relaxation rates or universal results for other Hamiltonians. The two scaling regimes are separate: fixed finite quartic \(\kappa\) and shrinking positive \(K_N\) with \(NK_N^4\to\infty\). No convergence rate uniform over all triangular arrays is claimed. The source papers' thermodynamic coexistence picture is used to delimit the global small-coupling branch, but its small-coupling expansion, triangular-array localization and susceptibility law are derived here.

## References

1. P. Contucci, E. Mingione and G. Osabutey, *Limit theorems for the cubic mean-field Ising model*, arXiv:2303.14578v1 (first posted 2023-03-25), https://arxiv.org/abs/2303.14578 .
2. P. Contucci, G. Osabutey and C. Vernia, *The inverse problem beyond two-body interaction: the cubic mean-field Ising model*, arXiv:2210.03260v1 (2022), https://arxiv.org/abs/2210.03260 .
3. D. Gandolfo, J. Ruiz and M. Wouts, *Limit Theorems and Coexistence Probabilities for the Curie-Weiss Potts Model with an external field*, arXiv:0811.2735v1 (2008), https://arxiv.org/abs/0811.2735 .
