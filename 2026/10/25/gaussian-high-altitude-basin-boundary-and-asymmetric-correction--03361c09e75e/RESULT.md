# Gaussian high-altitude basin boundary and asymmetric correction in a polynomial saddle-cycle flow

## Finding
For the planar reduction of the polynomial flow introduced by Castañeda and Rebollo-Perdomo [1], the stable separatrix of the saddle periodic orbit has a *nonuniform small-parameter boundary layer*. When the initial axial height has order \(\mu^{-1/2}\), its radius does not approach the radius \(1\) of the saddle orbit. Instead, for every fixed \(M>0\), its unique graph \(r=h_\mu(z)\) satisfies, uniformly for \(|U|\le M\),
\[
\boxed{\log h_\mu(U/\sqrt\mu)=\frac{200}{21}U^2-\frac{40\sqrt\mu}{21}\int_0^U \exp\!\left(\frac{400}{21}s^2\right)\,ds+O_M(\mu).}
\]
In particular, \(h_\mu(U/\sqrt\mu)\to \exp(200U^2/21)\). The first correction is odd in \(U\), giving a quantitative asymmetry between large positive and negative starting heights, even though the limiting Gaussian profile is even. This result does not follow by inserting an unbounded height into the bounded-height perturbation formula of [1].

## Assumptions and scope
Fix \(\mu>0\). The reduced vector field on \(r>0\) is
\[
\dot r=-\frac{\mu r}{21}(21r^4-125r^2+400z^2+100),\qquad
\dot z=-z-\frac{r^2}{10}.
\]
Its saddle equilibrium is \(q_\mu=(1,-1/10)\), corresponding in the full rotational flow to the saddle periodic orbit. Let \(W^s(q_\mu)\) mean precisely the points converging to this equilibrium as forward time tends to infinity. Given any finite \(M>0\), for all sufficiently small \(\mu>0\) there is a connected piece of this stable manifold represented uniquely by a smooth positive graph \(r=h_\mu(z)\) on the entire height interval \(|z|\le M/\sqrt\mu\). The assertion is local in *rescaled height* \(U=\sqrt\mu z\) and has no uniformity claim when \(|U|\) tends to infinity with \(\mu\to0\).

The angular parameter \(e\) of the three-dimensional parent family drops out of these radial and axial equations. This independence does not assert that the full Cartesian field is pointwise Hurwitz for all sufficiently small \(\mu\); the established Hurwitz parameter region in [1] is more restrictive.

## Proof
Set \(\eta=\sqrt\mu\), \(U=\eta z\), and \(R=r\). With \(C(R)=21R^4-125R^2+100\) and \(k=400/21\), the rescaled *original-time* equations are exactly
\[
\dot R=-kRU^2-\frac{\eta^2}{21}RC(R),\qquad
\dot U=-U-\frac\eta{10}R^2.
\]
Their equilibrium is \((R,U)=(1,-\eta/10)\). At \(\eta=0\), the entire line \(U=0\), \(R>0\), consists of equilibria and is normally attracting: the transverse eigenvalue is \(-1\), whereas the tangential eigenvalue is \(0\). Its strong-stable leaves can be integrated **exactly**. Indeed,
\[
U(t)=U_0e^{-t},\qquad
R(t)=R_0\exp\!\left[-\frac{kU_0^2}{2}(1-e^{-2t})\right].
\]
Thus the strong-stable leaf ending at \((1,0)\) is \(R=\exp(kU^2/2)=\exp(200U^2/21)\).

Here is the justification of uniform persistence beyond an infinitesimal neighborhood of \(U=0\). Given \(M\), the displayed limiting leaf segment \(|U|\le M\) and all its nonnegative-time trajectories lie inside a bounded positive-\(R\) tube. Choose a compact segment of the normally attracting critical line containing their limiting base point \((1,0)\) in its relative interior. The smooth, parameter-dependent local strong-stable foliation theorem applies with a uniform spectral gap of one at \(\eta=0\). The equilibrium \((1,-\eta/10)\) lies on the continued slow invariant graph; its strong-stable leaf depends smoothly on \(\eta\). Each point of the chosen limiting segment enters a fixed local stable-foliation chart after a finite time bounded over \(|U|\le M\). Pulling back that local leaf by these bounded flow times, using finite overlapping charts if necessary, gives a smooth positive graph \(R=H_\eta(U)\) on \([-M,M]\) and a smooth joint expansion of \(\log H_\eta\) in \(\eta\), with remainder uniformly \(O_M(\eta^2)\). The graph equals \(h_{\eta^2}(U/\eta)\) for \(\eta>0\).

Write \(L_\eta(U)=\log H_\eta(U)=L_0(U)+\eta L_1(U)+O_M(\eta^2)\). The invariance equation is
\[
\left[-U-\frac\eta{10}e^{2L_\eta(U)}\right]L_\eta'(U)
=-\frac{400}{21}U^2-\frac{\eta^2}{21}C(e^{L_\eta(U)}).
\]
At zeroth order, \(L_0(U)=200U^2/21\). Equating the terms linear in \(\eta\) for \(U\ne0\) gives
\[
L_1'(U)=-\frac{40}{21}\exp\!\left(\frac{400}{21}U^2\right).
\]
Smoothness extends this identity through \(U=0\). Since the saddle belongs to its own stable leaf, \(L_\eta(-\eta/10)=0\). Differentiating at \(\eta=0\) and using \(L_0'(0)=0\) yields \(L_1(0)=0\). Hence
\[
L_1(U)=-\frac{40}{21}\int_0^U e^{400s^2/21}\,ds.
\]
This establishes the claimed uniform expansion and the positivity and uniqueness of the graph. In particular, for fixed \(U>0\),
\[
\log\frac{h_\mu(-U/\sqrt\mu)}{h_\mu(U/\sqrt\mu)}
=\frac{80\sqrt\mu}{21}\int_0^U e^{400s^2/21}\,ds+O_U(\mu).
\]

## Verification
The accompanying standalone `check_gaussian.py` implements the exact rescaled invariance identities and independently integrates the unreduced-parameter stable graph from the saddle eigenvector. The numerical residuals after subtracting both displayed terms are proportional to \(\mu\) over a decreasing sequence of \(\mu\) values and four signed nonzero scaled heights; `checks.txt` records the actual output. The uniform statement for all scaled heights in a fixed compact set follows from the analytical stable-foliation argument, **not** from numerical testing. The exact Jacobian eigenvector used by the checker comes from differentiation of the stated planar vector field at its saddle.

## Relationship to prior work
Castañeda and Rebollo-Perdomo [1] introduce the exact planar reduction, prove the saddle and attracting periodic orbits, and display the stable separatrix as the basin boundary. In Section 4, they already give its **first-order formula at bounded axial heights**, so that first-order formula is not claimed here. The present result instead resolves a singular height scaling, \(z=U/\sqrt\mu\), where the radius differs from unity by order one, and finds the first parity-breaking correction there. The full original source was compared against this precise asymptotic statement, including its proof, basin portrait, and Section 4. General normally hyperbolic stable-foliation theory supplies a proof mechanism but not the concrete height profile or its explicit odd coefficient for this polynomial system.

## Limitations
The estimate is uniform only on compact subsets of the rescaled \(U\)-axis; it does not classify separatrix geometry when \(|z|\) grows faster than \(\mu^{-1/2}\). It is a local-in-scaled-height stable-manifold result, not a new global classification of all forward trajectories. The parent paper's assertions about the two attracting basins are background, not newly proved here. No new pointwise-Hurwitz parameter range or independent historical-priority audit is claimed.

## References
[1] Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1 (first public release October 6, 2026), especially equation (5), Lemma 1, and Section 4. https://arxiv.org/abs/2610.09176
[2] N. Fenichel, *Geometric singular perturbation theory for ordinary differential equations*, J. Differential Equations 31 (1979), 53–98. Cited for the standard normal-hyperbolicity and invariant-foliation framework, not as a source of the explicit profile.
