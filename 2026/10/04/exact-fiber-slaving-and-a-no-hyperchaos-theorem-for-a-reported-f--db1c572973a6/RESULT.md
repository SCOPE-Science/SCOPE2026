# Exact fiber slaving and a no-hyperchaos theorem for a reported four-dimensional hidden-attractor flow

## Finding
Consider the autonomous system
\[
\dot x=ay+xz,\qquad
\dot y=-bx+yz,\qquad
\dot z=1-x^2-y^2,\qquad
\dot w=z(w-1),
\]
with \(a,b>0\). Define
\[
Q=bx^2+ay^2.
\]
On the open set \(Q>0\), the quantity
\[
I=\frac{(w-1)^2}{Q}
\]
is an exact first integral. More strongly,
\[
w(t)-1=(w(0)-1)\sqrt{\frac{Q(t)}{Q(0)}}.
\]
Every compact ergodic invariant probability measure \(\mu\) of this flow is supported in \(Q>0\), obeys
\[
\int z\,d\mu=0,
\]
and has Lyapunov spectrum
\[
\{\lambda,0,0,-\lambda\}
\]
for some \(\lambda\ge0\), counting multiplicity. Thus compact recurrent dynamics of the exact system can have at most one positive Lyapunov exponent. In particular, the system cannot be hyperchaotic in the standard sense of having two positive Lyapunov exponents.

The fourth coordinate is a slaved fiber. If two solutions start from the same \((x,y,z)\) point but different fourth coordinates, their base trajectories are identical and each fourth-coordinate displacement from \(w=1\) is a constant multiple of \(\sqrt Q\).

## Assumptions and scope
The parameters satisfy \(a,b>0\), as in the source model. The Lyapunov-spectrum statement concerns compact ergodic invariant probability measures and Oseledets-regular points. The source system has no equilibria for positive \(a,b\), so the autonomous flow direction is nonzero on every compact invariant support.

This theorem does not assert that every numerical trajectory is bounded, does not classify all invariant sets, and does not decide whether a particular finite-time numerical computation has converged. It gives an exact obstruction that any asymptotic Lyapunov spectrum of compact recurrent dynamics must satisfy.

## Proof
Direct differentiation gives
\[
\dot Q
=2bx\dot x+2ay\dot y
=2z\left(bx^2+ay^2\right)
=2zQ.
\]
Writing \(u=w-1\), the fourth equation is \(\dot u=zu\). Hence
\[
\frac{d}{dt}\left(\frac{u}{\sqrt Q}\right)=0
\]
whenever \(Q>0\), which proves both the first integral and the explicit fiber-slaving formula.

A compact invariant set cannot contain a point with \(Q=0\). Indeed, because \(a,b>0\), \(Q=0\) means \(x=y=0\); then \(\dot x=\dot y=0\) and \(\dot z=1\), so the corresponding orbit has \(z(t)=z(0)+t\) and is not contained in any compact set. Thus \(Q\) is bounded away from zero on every compact invariant support.

On such a support, \(\log Q\) is smooth and
\[
L(\log Q)=2z,
\]
where \(L\) is the generator. Invariance therefore gives
\[
0=\int L(\log Q)\,d\mu=2\int z\,d\mu.
\]

The variational matrix, in the coordinate order \((x,y,z,w)\), has block-lower-triangular form
\[
D f=
\begin{pmatrix}
z&a&x&0\\
-b&z&y&0\\
-2x&-2y&0&0\\
0&0&w-1&z
\end{pmatrix}.
\]
The pure fourth-coordinate subspace is invariant and satisfies \(\delta\dot w=z\,\delta w\), so its Lyapunov exponent is \(\int z\,d\mu=0\). The quotient cocycle is exactly the three-dimensional base variational equation. Its trace is \(2z\), hence the sum of its three Lyapunov exponents is
\[
2\int z\,d\mu=0.
\]
Because the base flow is autonomous and has no equilibrium on the compact support, the flow direction contributes one zero Lyapunov exponent. The other two base exponents therefore sum to zero, so they are \(\lambda\) and \(-\lambda\). Combining the quotient and invariant-fiber spectra yields
\[
\{\lambda,0,0,-\lambda\}.
\]

## Verification
The packaged checker `artifacts/verify_integral_spectrum.py` symbolically verifies
\[
\dot Q=2zQ,\qquad
\frac{d}{dt}\left(\frac{(w-1)^2}{Q}\right)=0,
\]
the three-dimensional divergence \(2z\), the four-dimensional divergence \(3z\), and the block-triangular Jacobian structure. It also verifies algebraically that the signed fiber ratio \((w-1)/\sqrt Q\) has zero logarithmic derivative wherever defined.

The Lyapunov-spectrum conclusion is proved analytically above; it is not inferred from a finite-time numerical experiment.

## Relationship to prior work
Liu, Du, Zhang, Li, and Shi introduced the four-dimensional extension in 2019 and explicitly described it as hyperchaotic for parameter/initial-condition ranges where their numerical Lyapunov calculation displayed two positive values. Their full open-access article gives exactly the vector field used here. For \(a=1.2\), \(b=0.05\), and initial condition \((2,0,0,0)\), it reports two small positive Lyapunov exponents and calls the state hyperchaotic. The same article also varies only the initial fourth coordinate while holding the base initial condition fixed and describes different projected attractor sizes/phases.

The exact identities above were not stated in the inspected primary article. Targeted searches by exact equation, source title, first-integral aliases, fiber slaving, Lyapunov-spectrum implications, and published-results semantic search found no source giving this first integral or the resulting no-hyperchaos theorem for this system. The closest published-results records concern structurally different flows.

The three-dimensional base system predates the four-dimensional article, but the present claim specifically concerns the added fourth equation, its exact slaving, and the resulting four-dimensional Lyapunov-spectrum obstruction.

## Limitations
The literature search is targeted rather than exhaustive, so an unindexed equivalent derivation remains possible. The theorem applies to compact ergodic invariant measures of the exact differential equations; finite-time simulations, discretized circuit models, or noncompact trajectories are outside its conclusion. It does not prove that the source's displayed bounded trajectories fail to be chaotic in the one-positive-exponent sense; it rules out two-positive-exponent hyperchaos for compact recurrent dynamics.

## References
1. L. Liu, C. Du, X. Zhang, J. Li, and S. Shi, “Dynamics and Entropy Analysis for a New 4-D Hyperchaotic System with Coexisting Hidden Attractors,” *Entropy* 21 (2019), 287. DOI: 10.3390/e21030287. PMCID: PMC7514767.
2. S. Vaidyanathan and C. Volos, “Analysis and adaptive control of a novel 3-D conservative no-equilibrium chaotic system,” *Archives of Control Sciences* 25 (2015), 333–353. DOI: 10.1515/acsc-2015-0022.
