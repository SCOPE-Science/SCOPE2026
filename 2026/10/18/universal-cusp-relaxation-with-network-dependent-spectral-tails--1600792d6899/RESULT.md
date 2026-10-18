# Universal cusp relaxation with network-dependent spectral tails in logistic threshold-response dynamics

## Finding

At the natural logistic threshold cusp of a normalized feedback network, the collective activation has universal critical aging even though the ordinary strict-contraction theorem is inapplicable. All activity levels converge to the same unique equilibrium for every finite row-stochastic network. For one-sided initial data, reciprocal squared deviations have the same leading linear and logarithmic terms on every node. Irreducible interaction networks force even the constant term to agree across all nodes, while the infinitesimal decay of heterogeneous disturbances retains exact spectral information about the network.

Precisely, consider the flow
\[
\dot x_i=-x_i+\frac{1}{1+\exp[-(-2+4\sum_{j=1}^N w_{ij}x_j)]},\quad 1\le i\le N,
\]
where \(N\ge1\) and the matrix \(W=(w_{ij})\) is nonnegative and row-stochastic. For every \(x(0)\in[0,1]^N\), the equilibrium \(\tfrac12\mathbf{1}\) is unique and globally attracting. If either \(x_i(0)>\tfrac12\) for all \(i\) or \(x_i(0)<\tfrac12\) for all \(i\), then, for each \(i\),
\[
\frac{1}{[x_i(t)-\tfrac12]^2}=\frac83t-\frac85\log t+O(1),\qquad
\lim_{t\to\infty}\sqrt t\,|x_i(t)-\tfrac12|=\sqrt{\frac38}.
\]
If, additionally, \(W\) is irreducible, there is a finite real constant \(C\), common to all nodes but dependent on the initial state, such that
\[
\frac{1}{[x_i(t)-\tfrac12]^2}=\frac83t-\frac85\log t+C+o(1)
\]
for every \(i\), and \(|x_i(t)-x_j(t)|=O(e^{-\eta t})\) for some \(\eta>0\). The common-constant conclusion cannot be asserted without irreducibility: for \(W=I\), different one-sided initial deviations produce generally different constants.

For each nonstationary homogeneous trajectory \(x(t)=s(t)\mathbf{1}\), the exact linearized flow from initial perturbation to time \(t\) is
\[
\Phi(t)=\exp\!\left[-tI+W\int_0^t\operatorname{sech}^2(2s(q)-1)\,dq\right].
\]
There is a finite \(C_a\) for that trajectory such that
\[
\int_0^t\operatorname{sech}^2(2s(q)-1)\,dq
=t-\frac32\log t+C_a+o(1),
\]
and hence, in any matrix norm,
\[
\Phi(t)=e^{(W-I)t}\,\exp[-(3W/2)\log t]e^{C_aW}(I+o(1)).
\]
In an eigenmode of \(W\) with eigenvalue \(\lambda\), its infinitesimal response has exponential factor \(e^{(\lambda-1)t}\) and algebraic factor \(t^{-3\lambda/2}\). This assertion concerns the variational equation; it is not a finite-amplitude nonlinear mode-decay formula.

## Assumptions and scope

The dimension \(N\) is any finite positive integer, and each row of the real \(N\times N\) matrix \(W\) sums to one with nonnegative entries. Directed, asymmetric, reducible, periodic, and self-interacting matrices are allowed for the global conclusion. Irreducibility is assumed only for the shared asymptotic constant and exponential synchronization assertion. The initial state is in the closed physical cube. The reciprocal-square formula requires the explicitly stated strictly one-sided initial data; mixed-side initial states are covered by global convergence but not assigned this asymptotic rate. For the variational formula the homogeneous initial scalar must differ from \(\tfrac12\). Time is the model's original continuous time without rescaling.

The logistic threshold density is \(f(z)=F(z)(1-F(z))\); its maximum is \(1/4\) at \(z=0\). Thus the chosen feedback \(\beta=4\) and stimulus \(\alpha u=-2\) are the exact natural scalar cusp where \(F(0)=1/2\). These values are fixed by the bifurcation geometry, not selected by an arbitrary numerical fit.

## Proof

**Invariant cube, comparison, global convergence.** The logistic response belongs strictly to \((0,1)\), so the vector field points inward at each face of \([0,1]^N\). Nonnegative off-diagonal Jacobian entries make the flow cooperative. Row-stochasticity gives exact invariance of the homogeneous subspace \(x=s\mathbf{1}\), on which, with \(y=s-\tfrac12\),
\[
\dot y=g(y):=\frac12\tanh(2y)-y.
\]
For \(y>0\), \(\tanh(2y)<2y\); the opposite strict inequality holds for \(y<0\). Therefore every scalar orbit tends monotonically to zero. Let the two homogeneous scalar solutions start at the minimum and maximum of the initial node values. Cooperative comparison squeezes every node between them. Consequently all physical solutions tend to \(\tfrac12\mathbf{1}\), which is therefore the only equilibrium. If the initial state is strictly on one side, these scalar bounds also preserve its sign for all finite times.

**Scalar critical coefficient.** Expansion at the cusp is exact to the displayed orders:
\[
 g(y)=-\frac43y^3+\frac{32}{15}y^5-\frac{1088}{315}y^7+O(y^9).
\]
For any nonzero scalar orbit define \(Z=y^{-2}\). Its derivative is
\[
\dot Z=\frac83-\frac{64}{15Z}+O(Z^{-2}).
\]
Scalar convergence implies \(Z\to\infty\), hence first \(Z(t)/t\to8/3\). Substitution into the derivative establishes \(Z(t)=\frac83t+O(\log t)\). It follows that
\[
\dot Z-\frac83+\frac{8}{5t}=O\left(\frac{\log t}{t^2}\right),
\]
which is integrable, proving \(Z(t)=\frac83t-\frac85\log t+C_y+o(1)\) for a finite scalar constant \(C_y\). Comparison between the homogeneous envelopes, with the inversion order reversed above the cusp and accounted for below it, proves the componentwise \(O(1)\) formula without irreducibility.

**Irreducible networks, synchronization, and common constant.** Assume \(W\) irreducible. Its unique normalized positive stationary left vector \(\pi\) satisfies \(\pi^TW=\pi^T\) and \(\pi^T\mathbf{1}=1\). Decompose \(x=s\mathbf{1}+r\), with \(s=\pi^Tx\) and \(\pi^Tr=0\). On the transverse subspace, \(W-I\) is exponentially stable because Perron–Frobenius theory gives \(\operatorname{Re}\lambda<1\) for all non-Perron eigenvalues of \(W\), even if \(W\) is periodic. Taylor expansion of the exact vector field yields
\[
 \dot r=(W-I)r+O(|s-\tfrac12|^2\|r\|+\|r\|^2),
\qquad
 \dot s=g(s-\tfrac12)+O(\|r\|^2).
\]
Here the first-order term in the mean equation vanishes identically because \(\pi^TWr=0\). Global convergence already proved ensures these perturbations tend to zero; exponential stability of the transverse linear operator and a standard variation-of-constants/Gronwall estimate therefore give \(\|r(t)\|=O(e^{-\eta t})\) for some \(\eta>0\). Under one-sided initial data, the comparison envelopes imply \(|s(t)-\tfrac12|\asymp t^{-1/2}\). Thus \(Z_s=(s-\tfrac12)^{-2}\) obeys the scalar \(Z\)-equation with an additional absolutely integrable error \(O(t^{3/2}e^{-2\eta t})\). The same integration proves a finite constant \(C\) for \(Z_s\). Moreover \(x_i-s=O(e^{-\eta t})\) and \(|s-\tfrac12|\asymp t^{-1/2}\), so \(Z_i-Z_s=O(t^{3/2}e^{-\eta t})=o(1)\), proving the claimed common constant.

**Exact spectral response.** Along a homogeneous orbit write \(y=s-\tfrac12\). Differentiation gives the variational coefficient \(a(t)=4F'(-2+4s(t))=\operatorname{sech}^2(2y(t))\), so \(\dot v=(-I+a(t)W)v\). All coefficient matrices commute; their fundamental matrix is the exact exponential integral displayed above, with no diagonalizability assumption on \(W\). Since
\[
 a(t)=1-4y(t)^2+O(y(t)^4)
 =1-\frac{3}{2t}+O\left(\frac{\log t}{t^2}\right),
\]
the integral of \(a(t)-1+3/(2t)\) converges at infinity. This defines \(C_a\) and proves the exact matrix asymptotic, including Jordan blocks via matrix exponentials.

## Verification

The included script `verify.py` checks the scalar Taylor coefficients and the logarithmic coefficient using exact symbolic algebra; independently integrates homogeneous and heterogeneous finite network examples, including a periodic irreducible network and a reducible network; and checks the approach of the integrated variational prefactor. Run it with `python verify.py` after installing the versions of NumPy, SymPy, and SciPy listed in `requirements.txt`. The symbolic identities are exact. Numerical integrations are corroboration only and are not used to justify the infinite-time assertions or exhaust all matrices.

The proof explicitly distinguishes the unconditional global convergence claim from one-sided asymptotics and from infinitesimal variational response. In the reducible test case the leading and logarithmic coefficients agree while constants need not.

## Relationship to prior work

Boudourides (2026, arXiv:2609.10580v1) introduces the row-stochastic network extension and proves cooperation, strict-feedback contraction, invariant homogeneous dynamics, and spectral ordering at the homogeneous cusp. Those established results are premises, not claimed here as discoveries. Its Theorem 2.2 requires \(\beta\sup f<1\), whereas the present parameters have equality. Its Theorem 3.2 concerns the equilibrium Jacobian; it does not provide a time-dependent integrated variational prefactor. The present result adds the closed critical boundary's global attraction, two-term inverse-square aging for arbitrary row-stochastic networks, the shared finite constant for irreducible networks, and the exact spectral transient along nonstationary cusp trajectories.

Kaye (2026) motivates the scalar threshold response with animal vocalization and a spatial extension. Classical Perron–Frobenius, cooperative comparison, and asymptotic ODE theory supply major proof ingredients; no claim is made that those methods are new. Other classical master-stability and center-manifold results may contain broader frameworks that subsume portions of the calculation.

## Limitations

The result is mathematical, not an empirical estimate of dawn-chorus times. It assumes finite row-stochastic networks, homogeneous logistic thresholds, an exactly tuned stationary cusp stimulus, and an autonomous deterministic model. No rate claim is made for mixed-side initial data, nonnormalized matrices, heterogeneous threshold distributions, stochastic finite populations, or slowly varying illumination. The matrix formula describes infinitesimal perturbations about a homogeneous nonstationary trajectory, not finite-amplitude nonlinear disturbances. The scalar Kaye source's accessible abstract and its summary in the network paper were examined, but its full PDF was not materially inspected; there remains a literature-coverage risk, as well as the possibility of an encompassing general theorem in network critical dynamics.

## References

1. M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580v1 (first public 2026-09-05), https://arxiv.org/abs/2609.10580 .
2. A. R. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, *Journal of the Royal Society Interface* **23** (2026), 20260267, https://doi.org/10.1098/rsif.2026.0267 .
3. H. L. Smith, *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*, American Mathematical Society (1995). Classical cooperative comparison background; this monograph was cited in Reference 1, not separately inspected here.
4. E. Seneta, *Non-negative Matrices and Markov Chains*, Springer (2006). Classical Perron–Frobenius background; this text was cited in Reference 1, not separately inspected here.
