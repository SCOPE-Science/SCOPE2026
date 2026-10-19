# Polynomial escape with full-rank directional convergence in entropic diagonal completion

## Finding

For every even integer \(d\geq 2\), integer depth \(N\geq 2\), inverse temperature \(\beta>0\), real orthogonal complex structure \(J\) satisfying \(J^\mathsf{T}=-J\) and \(J^2=-I_d\), and initial matrix \(W(0)=I_d+b_0J\) with \(b_0\ne 0\), the balanced finite-temperature deep-linear free-energy gradient flow for diagonal completion has an explicit invariant two-dimensional matrix plane. Writing \(W(t)=a(t)I_d+b(t)J\) and
\[
 c=\frac{(N-1)(d-1)}{2\beta}>0,
\]
its coordinates satisfy the **exact** differential equations
\[
 \dot a=(a^2+b^2)^{-1/N}\left[-N(a^2+b^2)(a-1)+ca\right],
 \qquad \dot b=cb(a^2+b^2)^{-1/N}.
\]
This solution exists for every \(t\geq0\), remains invertible, and obeys the asymptotic laws
\[
 \boxed{\displaystyle |b(t)|\sim\left(\frac{2c}{N}t\right)^{N/2}},\qquad
 \boxed{\displaystyle a(t)-1\sim\frac{c}{N b(t)^2}}.
\]
In particular,
\[
 \boxed{\displaystyle \frac{W(t)}{\|W(t)\|_F}\longrightarrow
 \frac{\operatorname{sgn}(b_0)}{\sqrt d}J},
 \qquad
 \boxed{\displaystyle E_d(W(t))\sim\frac d2\left(\frac cN\right)^2
 \left(\frac{2c}N t\right)^{-2N}}.
\]
Every singular value tends to infinity, and the limit direction is full rank. Up to a time-independent additive normalization of the entropy, the free energy satisfies
\[
 \boxed{\displaystyle F_\beta(W(t))=-\frac{d(d-1)(N-1)}{4\beta}\log t+O(1)}.
\]
These are statements for the specified invariant family, **not** for generic full-rank initial conditions.

## Assumptions and scope

Work in the real full-rank matrices \(\mathrm{GL}_d(\mathbb R)\). The observed-diagonal loss, full-rank balanced-fiber entropy, free energy, and end-to-end balanced gradient flow are
\[
 E_d(W)=\frac12\sum_{i=1}^d(W_{ii}-1)^2,
 \qquad F_\beta(W)=E_d(W)-\beta^{-1}S_N(W),
 \qquad \dot W=-\mathcal A_{N,W}(\nabla F_\beta(W)),
\]
where, for a matrix \(P\),
\[
 \mathcal A_{N,W}(P)=\sum_{k=1}^N(WW^\mathsf T)^{(N-k)/N}
 P(W^\mathsf TW)^{(k-1)/N}.
\]
For positive singular values \(\sigma_1,\ldots,\sigma_d\), the entropy is, modulo a constant depending only on \(N,d\),
\[
 S_N(W)=\frac12\sum_{i<j}\log\frac{\sigma_i^2-\sigma_j^2}
 {\sigma_i^{2/N}-\sigma_j^{2/N}},
\]
with the real-analytic continuation at coincident singular values. The statement concerns this deterministic **finite-\(\beta\)** Riemannian flow, not stochastic factor-space Langevin dynamics or unregularized gradient training. An orthogonal complex structure exists in each even dimension, for example the direct sum of \(2\times2\) quarter-turn matrices.

## Proof

**1. Exact invariant reduction.** Since \(J^\mathsf T=-J\) and \(J^2=-I_d\), a matrix \(W=aI_d+bJ\) satisfies
\[
 WW^\mathsf T=W^\mathsf TW=(a^2+b^2)I_d=:r^2I_d.
\]
Thus all \(d\) singular values equal \(r>0\) and \(\mathcal A_{N,W}(P)=Nr^{2-2/N}P\). Taking the equal-singular-value limit of each pair in the entropy gives
\[
 S_N(aI_d+bJ)=\binom d2\left[\tfrac12\log N+
 (1-1/N)\log r\right]+\text{constant}.
\]
Orthogonal invariance of the entropy implies that its ambient Euclidean gradient at this isosingular matrix is a multiple of \(W\). Differentiating the displayed expression along radial scaling fixes the coefficient:
\[
 \nabla S_N(W)=\frac{(d-1)(1-1/N)}{2r^2}\,W.
\]
Because the diagonal entries of \(J\) vanish, \(\nabla E_d(W)=(a-1)I_d\). Inserting both gradients into the exact balanced operator yields
\[
 \dot W=-Nr^{2-2/N}(a-1)I_d+cr^{-2/N}W,
\]
proving invariance of the plane and the two scalar equations in the finding.

**2. Forward bounds and escape.** Initially \(a=1\), and \(\dot a>0\) on the boundary \(a=1\). Define
\[
 A=\frac{1+\sqrt{1+4c/N}}2>1.
\]
When \(a\geq A\), using \(r^2\geq a^2\) gives
\[
 -Nr^2(a-1)+ca\leq a\,[c-Na(a-1)]\leq0.
\]
Therefore \(1\leq a(t)\leq A\). Meanwhile \(b\) keeps its initial sign and \(|b|\) increases strictly. Since \(r\geq |b|\),
\[
 \frac{d}{dt}|b|=c|b|r^{-2/N}\leq c|b|^{1-2/N};
\]
there is no finite-time blow-up, and \(r\geq |b_0|>0\) excludes loss of invertibility. Thus the solution is forward complete. If \(|b|\) remained bounded, its strictly positive derivative would have a uniform positive lower bound (using the bounds on \(a\)), a contradiction; hence \(|b|\to\infty\).

**3. Relaxation of the diagonal coordinate.** Fix \(\varepsilon>0\). For all sufficiently large \(|b|\), whenever \(a\geq1+\varepsilon\) the scalar equation gives \(\dot a<0\); the negative term dominates uniformly because \(a\in[1,A]\). Consequently \(a(t)\to1\).

Define a strictly increasing clock \(\tau\) by \(d\tau/dt=r^{2-2/N}\). It tends to infinity, since \(r\geq|b_0|\). Derivatives with respect to this clock obey
\[
 \frac{da}{d\tau}=-N(a-1)+\frac{ca}{r^2},
 \qquad \frac{db}{d\tau}=\frac{cb}{r^2}.
\]
With \(k=b^2(a-1)\geq0\), these identities give
\[
 \frac{dk}{d\tau}=
 \left(-N+\frac{2c}{r^2}\right)k+\frac{cab^2}{r^2}.
\]
For sufficiently large \(\tau\), its coefficient of \(k\) is at most \(-N/2\) and the source is bounded by \(cA\), so \(k\) is bounded. Since \(a\to1\) and \(b^2/r^2\to1\), the equation is a uniformly stable scalar linear equation with coefficient tending to \(-N\) and forcing tending to \(c\). Variation of constants yields \(k\to c/N\). This proves \(a-1\sim c/(Nb^2)\), with a positive leading coefficient.

**4. Precise polynomial rate and observable limits.** Differentiation of the strictly positive quantity \(|b|^{2/N}\) gives
\[
 \frac{d}{dt}|b|^{2/N}=\frac{2c}{N}
 \left(\frac{b^2}{a^2+b^2}\right)^{1/N}\longrightarrow\frac{2c}{N}.
\]
Taking time averages of this derivative proves \(|b|^{2/N}/t\to2c/N\), and hence the stated polynomial escape law. Since \(r\sim|b|\) and \(a\to1\), the normalized direction tends to \(\operatorname{sgn}(b_0)J/\sqrt d\). All singular values equal \(r\to\infty\). Also \(E_d(W)=d(a-1)^2/2\); substituting the two established asymptotics gives its precise \(t^{-2N}\) equivalent. Finally, the exact equal-singular entropy expression is \(\binom d2(1-1/N)\log r+O(1)\), while \(\log r=(N/2)\log t+O(1)\) and \(E_d(W)\to0\). This yields the asserted free-energy logarithmic law.

## Verification

Run the standalone standard-library program `verify.py` using `python3 verify.py`. It independently constructs block-skew matrices and checks \(J^\mathsf T=-J\), \(J^2=-I_d\), and equal singular radii at sample points. It compares the near-coincident original pairwise entropy quotient with the claimed analytic continuation. A fourth-order numerical integrator, in the exact reparametrized clock \(\tau\), tests representative systems at depths \(N=2,3,5\), including both signs of \(b_0\), and checks the invariant bounds, the scaled asymptotic \(b^2(a-1)\to c/N\), and the leading polynomial rate. Successful execution prints `VERIFY_OK`. The numerical finite-time checks are not substituted for any infinite-time argument.

## Relationship to prior work

Treviño, *Failure of entropic selection for diagonal matrix completion in deep linear networks* (arXiv:2610.05551v1, first public October 4, 2026), supplies the full-rank finite-temperature flow and proves generic unboundedness for \(N>2\). Section 12.4 explicitly asks about escape rates, limiting directions, and whether completion loss vanishes; it does not supply the specific rate or direction derived here. Section 12.5 treats depth two as a separate unresolved general case. The present result gives **explicit, nongeneric trajectories** with sharp rates for all even widths and all integer depths \(N\geq2\); it does not answer those generic questions.

Chen, Kotwal, and Menon, *Entropic regularization in the Deep Linear Network* (arXiv:2512.06137), analyze spectral losses and identify nonspectral matrix completion as an open challenge (Section 8.2). Menon and Yu, *An entropy formula for the Deep Linear Network* (arXiv:2509.09088), supply the balanced-fiber entropy and metric geometry on which the present specialization depends. Thus the underlying gradient-flow formula, entropy, and generic escape mechanism are **not** new; the invariant isosingular family and its exact finite-temperature escape asymptotics are the claims evaluated here.

## Limitations

The initial data lie on a natural but positive-codimension invariant family of the full matrix space. Neither almost-everywhere directional convergence nor generic loss decay is proved. The result excludes singular escape only for this family, not for arbitrary trajectories. The stated entropy depends on an arbitrary additive normalization, but its drift and logarithmic growth coefficient do not. Numerical integrations support, but do not independently certify, the analytical asymptotics. An equivalent construction in earlier specialized literature cannot be categorically ruled out.

## References

1. Rodrigo Treviño, *Failure of entropic selection for diagonal matrix completion in deep linear networks*, arXiv:2610.05551v1 (October 4, 2026). https://arxiv.org/html/2610.05551v1
2. Chen, Kotwal, and Menon, *Entropic regularization in the Deep Linear Network*, arXiv:2512.06137v1 (2025). https://arxiv.org/html/2512.06137v1
3. Govind Menon and Tianmin Yu, *An entropy formula for the Deep Linear Network*, arXiv:2509.09088 (2025). https://arxiv.org/html/2509.09088v3
