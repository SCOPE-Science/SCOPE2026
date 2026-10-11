# Universal concentration means and critical extinction in a conservative four-species oscillator

## Finding

**Theorem.** Let \(p,q,r,s,C>0\), and consider the four-species mass-action differential equation
\[
\begin{aligned}
\dot x&=xw-rx-pxy, & \dot y&=sz-qy,\\
\dot z&=rx-sz, & \dot w&=pxy+qy-xw
\end{aligned}
\]
with strictly positive initial concentrations satisfying \(x+y+z+w=C\). Define
\[
D=1+\frac{(1+p)r}{q}+\frac{r}{s},\quad
\alpha=\frac{1+p}{q},\quad \beta=\alpha+\frac1s,
\quad \Phi=\log x-\alpha y-\beta z.
\]
The following assertions hold for **every** such solution, in the original ODE time.

**Above the equilibrium threshold, \(C>r\):** The time average of the **entire** concentration vector tends to the unique interior equilibrium
\[
E_C=\left(\frac{C-r}{D},\frac{r(C-r)}{qD},
\frac{r(C-r)}{sD},r+\frac{pr(C-r)}{qD}\right),
\qquad
\frac1T\int_0^T(x,y,z,w)(t)\,dt=E_C+O(T^{-1}).
\]
The implicit bound is valid for each initial condition, but is not claimed uniform over all initial conditions. Every interior periodic orbit has **exactly** this vector as its period average, regardless of stability or period. Every flow-invariant probability measure with compact support entirely inside the positive stoichiometric simplex has barycenter \(E_C\). In fact, for each trajectory, the exact finite-time identity
\[
D\int_0^T x(t)\,dt=(C-r)T+\Phi(0)-\Phi(T)
\]
holds, and analogous exact linear endpoint corrections recover the other three averages.

**Exactly at the threshold, \(C=r\):** All initially positive solutions converge to the boundary equilibrium \((0,0,0,r)\). Their concentrations have universal algebraic limits
\[
\lim_{t\to\infty}t(x(t),y(t),z(t))
=\frac1D\left(1,\frac rq,\frac rs\right),
\qquad
\lim_{t\to\infty}t\,[r-w(t)]
=\frac{1+r/q+r/s}{D}.
\]
Moreover the critical cumulative production has an exact logarithmic centering:
\[
\lim_{T\to\infty}\left(D\int_0^T x(t)\,dt-\log T\right)=\Phi(0)+\log D.
\]

**Below the threshold, \(0<C<r\):** Every initially positive trajectory approaches \((0,0,0,C)\), and
\[
\lim_{t\to\infty}\frac{\log x(t)}{t}=C-r<0.
\]

## Assumptions and scope

All rate parameters and total mass are fixed positive real numbers. Initial states lie strictly inside the three-dimensional simplex \(\{(x,y,z,w)>0:x+y+z+w=C\}\). The displayed kinetic normalization (coefficient \(1\) of \(xw\)) is part of the model; no additional time rescaling is made. The \(O(T^{-1})\) constant is allowed to depend on the initial state and the four rate parameters. At \(C\le r\), \(D\) still denotes the positive parameter expression above. No statement concerns trajectories beginning on boundary faces.

## Proof

**1. Positivity and conservation.** Adding all four equations gives \(\dot x+\dot y+\dot z+\dot w=0\). Positivity is forward invariant: \(\dot x=x(w-r-py)\); whenever a vanishing face is approached from inside, the other equations have respective inward terms \(sz\), \(rx\), and \(pxy+qy\). The compact invariant simplex gives global forward existence and \(0<x,y,z,w\le C\).

**2. Exact logarithmic identity.** Since \(w=C-x-y-z\),
\[
\frac{\dot x}{x}=C-r-x-(1+p)y-z.
\]
On the other hand,
\[
\alpha\dot y+\beta\dot z
=r\beta x-(1+p)y-z.
\]
Subtracting gives the exact, unaveraged coboundary
\[
\boxed{\dot\Phi=(C-r)-Dx},\qquad D=1+r\beta.
\]
Also, independently,
\[
\dot z=rx-sz,\qquad \dot y+\dot z=rx-qy.
\]
These three identities contain all the averaging information.

**3. Above threshold: explicit persistence of \(x\).** Put \(\delta=C-r>0\). Since \(0\le\alpha y+\beta z\le\beta C\), one has
\[
x=e^{\Phi+\alpha y+\beta z}\le e^{\Phi+\beta C}.
\]
Set \(L=\log[\delta/(2D)]-\beta C\). Whenever \(\Phi\le L\), the last inequality gives \(x\le\delta/(2D)\), hence \(\dot\Phi\ge\delta/2\). Thus \(\Phi(t)\ge\min(\Phi(0),L)\) for all time and \(\Phi(t)\ge L\) after some finite time depending on the initial state. In particular \(x(t)\ge e^L>0\) eventually, while \(\Phi(t)\le\log C\). This provides a self-contained lower bound; the remaining linear equations also give eventual positive lower bounds for \(z\), then \(y\), then \(w\), if desired.

Integrating the boxed identity and using boundedness of \(\Phi\) proves
\[
\frac1T\int_0^T x(t)\,dt=\frac{\delta}{D}+O(T^{-1}).
\]
Integrating the two linear balances yields the exact endpoint formulas
\[
q\int_0^T y\,dt=r\int_0^T x\,dt-[y(T)+z(T)-y(0)-z(0)],
\]
\[
s\int_0^T z\,dt=r\int_0^T x\,dt-[z(T)-z(0)].
\]
All state variables lie between \(0\) and \(C\), so the endpoint contributions are bounded. The total-mass conservation gives the average of \(w\). These imply the stated four-component formula. If the trajectory is periodic, all endpoint corrections over one full period vanish exactly. If \(\mu\) is any invariant probability measure with support compactly contained in the interior, \(\Phi\) is continuously differentiable and bounded there; invariance implies \(\int\dot\Phi\,d\mu=0\) and the two corresponding linear balance integrals vanish. Consequently \(\int(x,y,z,w)\,d\mu=E_C\) even when the invariant state is not an equilibrium.

**4. At the threshold: rates and integrated mass.** For \(C=r\),
\[
\dot x=-x\bigl(x+(1+p)y+z\bigr)\le -x^2.
\]
Thus \(x(t)\to0\), indeed \(x(t)\le[x(0)^{-1}+t]^{-1}\). Solving the stable linear equations \(\dot z+sz=rx\) and \(\dot y+qy=sz\) by variation of constants shows \(z(t),y(t)\to0\); the conservation law gives \(w(t)\to r\). Put \(\lambda(t)=x+(1+p)y+z\), so that \(-\dot x/x=\lambda(t)\to0\). For every fixed \(v\ge0\),
\[
\frac{x(t-v)}{x(t)}=\exp\left(\int_{t-v}^t\lambda(u)\,du\right)\longrightarrow1.
\]
Choose any \(0<\eta<\min(q,s)\). For sufficiently late times, \(0\le\lambda\le\eta\); hence the ratio above is bounded by \(e^{\eta v}\) on the late-time convolution interval. The initial-data tails divided by \(x(t)\) decay as \(e^{-(s-\eta)t}\) or \(e^{-(q-\eta)t}\). Applying dominated convergence first to
\[
z(t)=e^{-s(t-t_0)}z(t_0)+r\int_{t_0}^t e^{-s(t-u)}x(u)\,du
\]
gives \(z(t)/x(t)\to r/s\). Repeating for \(y\), with \(z/x\) now bounded eventually, gives \(y(t)/x(t)\to r/q\). This remains valid when \(q=s\).

Finally,
\[
\frac{d}{dt}\frac1{x(t)}
=1+(1+p)\frac{y(t)}{x(t)}+\frac{z(t)}{x(t)}\longrightarrow D.
\]
Integrating and dividing by \(t\) yields \(t x(t)\to1/D\). The limits for \(y,z,w\) follow from the ratios and conservation. Since \(\dot\Phi=-Dx\), the exact integral identity and the limits imply \(\Phi(T)=-\log T-\log D+o(1)\), proving the displayed finite logarithmic centering. The endpoint formulas additionally show that the integrals of \(y,z\), minus \(r\log T/(qD)\), \(r\log T/(sD)\) respectively, have finite limits.

**5. Below threshold.** If \(\delta=C-r<0\), the scalar inequality \(\dot x/x\le\delta\) gives exponential decay of \(x\). The stable forced equations give \(y,z\to0\) and hence \(w\to C\). Since \(\dot{\log x}=\delta-x-(1+p)y-z\to\delta\), integration and division by \(t\) give the asserted logarithmic decay rate.

## Verification

The self-contained algebraic part is independently replayable with \(\texttt{python verify_mean.py}\) (requires SymPy). That script checks conservation, the exact nonlinear logarithmic coboundary, the integrated linear balances, the equilibrium coordinates, and the critical coefficient symbolically; its output is \(\texttt{CHECK_OK}\). The argument for the threshold ratios uses dominated convergence on exponentially weighted convolution kernels and is proved above, not inferred from a finite simulation. Numerical trajectories are neither needed nor used as a proof of the universal limits. In particular, a finite-time average does not generally coincide exactly with the equilibrium; the discrepancy is an endpoint term of order \(T^{-1}\).

## Relationship to prior work

Boros and Hofbauer's original full-text analysis of this precise homogenized Wilhelm–Heinrich network proves its positive equilibrium formula, stability regimes, existence of simultaneous stable and unstable limit cycles, and permanence above \(C=r\) (Theorem 14). Those conclusions are already established and are **not** claimed here. Their results motivate the nontrivial question of whether different recurrent regimes can be distinguished by their average species concentrations. The present theorem shows that they cannot: the full four-coordinate barycenter is fixed even when the equilibrium and multiple cycles coexist, and it gives exact finite-time and critical-threshold coefficients. Joshi and Craciun's dynamic absolute concentration robustness concerns pointwise convergence of designated species concentrations across compatible initial conditions; it does not imply the vector time-average law in a system with persistent nonconstant cycles. Related equilibrium robustness and general oscillation-inheritance results similarly have different conclusions.

## Limitations

The result is for the specified four-species deterministic mass-action equations, their positive stoichiometric classes, and the normalization written above; it does not imply that each supercritical trajectory converges to the equilibrium. It does not classify all recurrent attractors, prove robustness under network perturbations, or claim any coordinate is independent of the conserved total \(C\). The limit in the invariant-measure assertion requires compact support strictly inside the positive simplex; no assertion is made for boundary-supported invariant measures. For the time-average error, the hidden constant is not uniform across all positive initial states. The proof is analytical, while the code only checks symbolic identities. Priority over unindexed or unpublished literature is not certified.

## References

1. B. Boros and J. Hofbauer, *Some minimal bimolecular mass-action systems with limit cycles*, arXiv:2202.11034v1 (first publicly available 2022-02-22), revised v2 2022-09-13, especially Equation (8), Theorem 14 and its proof. https://arxiv.org/html/2202.11034v2 ; https://arxiv.org/abs/2202.11034 ; DOI:10.1016/j.nonrwa.2023.103839.
2. B. Joshi and G. Craciun, *Foundations of static and dynamic absolute concentration robustness*, arXiv:2104.14070, J. Math. Biol. 85:53 (2022), DOI:10.1007/s00285-022-01823-2. https://public.csusm.edu/bjoshi/Papers/FoundationsACR.pdf.
3. M. Banaji and B. Boros, *The smallest bimolecular mass action reaction networks admitting Andronov-Hopf bifurcation*, arXiv:2207.04971 (2022). https://arxiv.org/abs/2207.04971.
4. M. Banaji, B. Boros and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, arXiv:2304.02303 (2023). https://arxiv.org/abs/2304.02303.
