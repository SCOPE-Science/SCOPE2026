# Exact activity–height law for the Wang–Chen perturbed Sprott-E flow
## Finding
Consider the Wang–Chen perturbation of the Sprott-E flow
\[
\dot x=yz+a,\qquad
\dot y=x^2-y,\qquad
\dot z=1-4x.
\]
For every compactly supported invariant Borel probability measure \(\mu\), define the mean-square vertical activity
\[
A:=\int \dot z^{\,2}\,d\mu.
\]
Then
\[
\int x\,d\mu=\frac14,
\qquad
\int y\,d\mu=\int x^2\,d\mu=\frac{1+A}{16},
\qquad
\int yz\,d\mu=-a.
\]
Every complete trajectory in \(\operatorname{supp}\mu\) also satisfies \(y(t)\ge0\). Since \(\int y\,d\mu=(1+A)/16>0\),
\[
d\nu:=\frac{y}{\int y\,d\mu}\,d\mu
\]
is a probability measure. Its mean height obeys the exact activity law
\[
\int z\,d\nu=-\frac{16a}{1+A}.
\]
Furthermore,
\[
A=0
\quad\Longleftrightarrow\quad
\mu=\delta_Q,
\qquad
Q=\left(\frac14,\frac1{16},-16a\right).
\]
Thus, for \(a>0\), every non-equilibrium compact recurrent statistical state satisfies
\[
-16a<\int z\,d\nu<0,
\]
whereas the equilibrium realizes the lower endpoint \(-16a\). At \(a=0.01\), where point, periodic, and strange attractors have been reported to coexist, the point equilibrium has \(y\)-weighted height \(-0.16\), while every compact invariant probability measure carried by a non-equilibrium periodic or strange branch has weighted height strictly in \((-0.16,0)\).

## Assumptions and scope
The vector field is the printed Wang–Chen system. The claim concerns compactly supported invariant Borel probability measures of its classical flow. Compact support guarantees bounded complete trajectories on the support and legitimizes the generator identities used below. No ergodicity assumption is needed. The strict interval statement assumes \(a>0\); the exact formula itself holds for every real \(a\).

The measure \(\nu\) is genuinely a probability measure rather than a signed reweighting. Indeed, along any bounded complete trajectory the variation-of-constants formula for \(\dot y=x^2-y\) is
\[
y(t)=e^{-T}y(t-T)+\int_{t-T}^t e^{-(t-s)}x(s)^2\,ds.
\]
Letting \(T\to\infty\) gives \(y(t)\ge0\). The identity for \(\int y\,d\mu\) below then gives a strictly positive normalizing constant.

## Proof
For an invariant probability measure with compact support, the integral of the Lie derivative of any polynomial test function is zero. Applying this to \(z\), \(y\), and \(x\) gives, respectively,
\[
0=\int(1-4x)\,d\mu,
\]
\[
0=\int(x^2-y)\,d\mu,
\]
and
\[
0=\int(yz+a)\,d\mu.
\]
Hence
\[
\int x\,d\mu=\frac14,
\qquad
\int y\,d\mu=\int x^2\,d\mu,
\qquad
\int yz\,d\mu=-a.
\]
Because \(\dot z=1-4x=-4(x-1/4)\),
\[
A
=16\int\left(x-\frac14\right)^2d\mu
=16\left(\int x^2\,d\mu-\frac1{16}\right).
\]
Therefore
\[
\int y\,d\mu=\int x^2\,d\mu=\frac{1+A}{16},
\]
and division of \(\int yz\,d\mu=-a\) by this positive quantity yields
\[
\int z\,d\nu
=\frac{\int yz\,d\mu}{\int y\,d\mu}
=-\frac{16a}{1+A}.
\]

It remains to identify the equality case. If \(\mu=\delta_Q\), then \(\dot z=0\) and \(A=0\). Conversely, if \(A=0\), continuity of \(\dot z^2\) implies \(x=1/4\) on \(\operatorname{supp}\mu\). Stationarity of \((y-1/16)^2\) then gives
\[
0=\int 2\left(y-\frac1{16}\right)\left(\frac1{16}-y\right)d\mu
=-2\int\left(y-\frac1{16}\right)^2d\mu,
\]
so \(y=1/16\) on the support. The support of an invariant measure is invariant, hence the vector field must be tangent to the set \(x=1/4\), \(y=1/16\). Its \(x\)-component there is \(z/16+a\), forcing \(z=-16a\). Thus \(\mu=\delta_Q\). For \(a>0\), every other invariant measure has \(A>0\), and the strict interval follows immediately.

## Verification
The proof uses only exact identities from the vector field and invariant-measure stationarity. The accompanying `verify.py` performs dependency-free polynomial checks of the three Lie derivatives, verifies the equilibrium, and checks the algebra relating activity, variance, and weighted height. Running

`python verify.py`

returns `VERIFY_OK`.

The equality case was checked separately in the proof: zero activity collapses the support first to \(x=1/4\), then to \(y=1/16\), and finally by invariance to \(z=-16a\). No finite-time numerical experiment is used as evidence for an infinite-time statement.

## Relationship to prior work
Wang and Chen introduced the perturbed Sprott-E system and established its single equilibrium, its stability changes with \(a\), and chaotic regimes. Sprott, Wang, and Chen later documented coexistence of point, periodic, and strange attractors, including \(a=0.01\). Chen, Liu, Wei, and Feng subsequently studied the same system globally at infinity and through KCC/Jacobi stability; their article lists MSC 34C28 first and was first published online on 18 June 2020. A separate geometrical study by Gupta, Yadav, and Gupta also develops KCC invariants for the Wang–Chen system.

The inspected primary texts analyze equilibria, Lyapunov exponents, bifurcations, basins, dynamics at infinity, and Jacobi stability. They do not state the invariant-measure identities above, the exact activity–height formula, or the characterization of the equilibrium as the unique zero-activity stationary state. The result therefore supplies a statistical structural invariant tailored to the same multistability phenomenon: it separates the point attractor from every non-equilibrium recurrent branch by an exact observable relation rather than by numerical classification alone.

## Limitations
The result does not prove existence of a chaotic or periodic invariant set for a given parameter, nor does it prove that a reported numerical trajectory is on a particular attractor. It applies to compactly supported invariant measures once such recurrent states exist. It gives a \(y\)-weighted mean of \(z\), not the ordinary mean of \(z\). The search and source inspection cannot exclude an unindexed prior statement of the same identity, so a residual originality risk remains.

## References
1. B. Chen, Y. Liu, Z. Wei, C. Feng, “New insights into a chaotic system with only a Lyapunov stable equilibrium,” *Mathematical Methods in the Applied Sciences* 43 (2020), 9262–9279. DOI: 10.1002/mma.6619.
2. X. Wang, G. Chen, “A chaotic system with only one stable equilibrium,” *Communications in Nonlinear Science and Numerical Simulation* 17 (2012), 1264–1272. DOI: 10.1016/j.cnsns.2011.07.017; public preprint arXiv:1101.4067.
3. J. C. Sprott, X. Wang, G. Chen, “Coexistence of point, periodic and strange attractors,” *International Journal of Bifurcation and Chaos* 23 (2013), 1350093. DOI: 10.1142/S0218127413500934.
4. M. K. Gupta, C. K. Yadav, A. K. Gupta, “A geometrical study of Wang-Chen system in view of KCC theory,” *TWMS Journal of Applied and Engineering Mathematics* 10 (2020), 1064–1073.
