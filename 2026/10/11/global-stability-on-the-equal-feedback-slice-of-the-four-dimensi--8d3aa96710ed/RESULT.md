# Global stability on the equal-feedback slice of the four-dimensional Rabinovich system
## Finding
Consider the four-dimensional Rabinovich system introduced by Li and Cui, restricted to the equal-feedback slice \(k_0=m=s>0\):
\[
\dot x=hy-ax+yz+su,\qquad
\dot y=hx-by-xz+su,
\]
\[
\dot z=-dz+xy,\qquad
\dot u=-k(x+y),
\]
where \(a,b,d,h,k,s>0\). If \(h^2<ab\), then the origin is globally asymptotically stable.

Every compactly supported invariant probability measure \(\mu\) also satisfies
\[
a\langle x^2\rangle_\mu+b\langle y^2\rangle_\mu
=2h\langle xy\rangle_\mu.
\]
Consequently, under \(h^2<ab\), the only compactly supported invariant probability measure is the Dirac mass at the origin. Thus non-equilibrium compact recurrence on the equal-feedback slice requires \(h^2\ge ab\).

## Assumptions and scope
The statement concerns the classical autonomous ordinary differential equation above with strictly positive parameters and exactly equal feedback coefficients \(k_0=m=s\). The strict inequality \(h^2<ab\) is essential to the proof given here. No assertion is made at the boundary \(h^2=ab\), for unequal feedback coefficients, or for fractional-order variants.

## Proof
Define
\[
V(x,y,u)=\frac12\left(x^2+y^2+\frac{s}{k}u^2\right).
\]
Along every solution, the quadratic interaction terms \(xyz\) cancel between the first two equations and the equal-feedback terms cancel against the \(u\)-equation. Therefore
\[
\dot V
=2hxy-ax^2-by^2
=-\left(ax^2-2hxy+by^2\right).
\]
The symmetric quadratic form \(Q(x,y)=ax^2-2hxy+by^2\) is positive definite exactly when \(a>0\) and \(ab-h^2>0\). Hence \(V\) is nonincreasing and \(x,y,u\) remain bounded for all forward time.

The remaining variable obeys the stable forced scalar equation
\[
\dot z=-dz+xy.
\]
Since \(x\) and \(y\) are bounded, variation of constants shows that \(z\) is bounded as well. Thus every forward trajectory is precompact and exists for all positive time. LaSalle's invariance principle applied to \(V\) gives approach to the largest invariant subset of \(Q=0\). Positive definiteness gives \(x=y=0\) there. Invariance then forces \(u=0\), while on the remaining \(z\)-axis one has \(\dot z=-dz\). Therefore \(x(t),y(t),u(t),z(t)\to0\).

Lyapunov stability follows from the same estimate: small initial \(V\) keeps \(x,y,u\) small, and
\[
|z(t)|\le e^{-dt}|z(0)|+\int_0^t e^{-d(t-\tau)}|x(\tau)y(\tau)|\,d\tau
\]
keeps \(z\) small when the initial state is small. Hence the origin is globally asymptotically stable.

For a compactly supported invariant probability measure \(\mu\), stationarity gives \(\int \dot V\,d\mu=0\), hence
\[
a\langle x^2\rangle_\mu+b\langle y^2\rangle_\mu
=2h\langle xy\rangle_\mu.
\]
When \(h^2<ab\), positive definiteness of \(Q\) forces \(x=y=0\) almost surely. Invariance then forces \(u=0\), and stationarity of \(z^2\) on the \(z\)-axis gives \(\langle z^2\rangle_\mu=0\). Thus \(\mu\) is the Dirac mass at the origin.

## Verification
A dependency-free exact polynomial checker, `verify.py`, expands the derivative identity after clearing the harmless factor \(1/k\). It verifies
\[
k\frac{d}{dt}(x^2+y^2)+s\frac{d}{dt}(u^2)
=-2k\left(ax^2-2hxy+by^2\right)
\]
identically in all variables and parameters. Running `python verify.py` returns `VERIFY_OK`.

The proof also independently checks the boundedness step for \(z\) by variation of constants and distinguishes global attraction from Lyapunov stability. No finite numerical experiment is used as evidence for the infinite-time claim.

## Relationship to prior work
Li and Cui introduce this exact four-dimensional vector field and prove an ultimate-bound theorem only under the strict assumption \(k_0>m\). Their numerical hyperchaos study nevertheless uses the equal slice \(k_0=m=0.8\), so the slice treated here is a natural parameter regime left outside that boundedness theorem. Their Hopf condition requires \(ab>h^2\) together with \(k_0(a-h)+m(b-h)<0\). On the equal slice this second inequality becomes \(s(a+b-2h)<0\), which is impossible when \(ab>h^2\) because \(a+b\ge2\sqrt{{ab}}>2h\). This is consistent with the global-stability region proved here but does not itself imply it.

Earlier four-dimensional Rabinovich variants place the added state differently. In particular, the generalized system studied by Wei, Yu, Zhang, and Yao does not have equal copies of the same feedback state in both the first and second equations and therefore does not yield the cancellation above. Exact-statement searches of the introducing article, earlier Rabinovich variants, and a semantic mathematical-results database found no stronger result covering this equal-feedback global-stability theorem or its invariant-measure identity.

## Limitations
The proof does not settle the critical surface \(h^2=ab\). It does not classify dynamics when \(h^2>ab\), and the necessary condition \(h^2\ge ab\) for non-equilibrium compact recurrence is not claimed to be sufficient. The result is specific to \(k_0=m\); unequal feedback coefficients destroy the exact cancellation used here.

## References
1. Junhong Li and Ning Cui, “A hyperchaos generated from Rabinovich system,” *AIMS Mathematics* 8(1), 1410–1426, DOI 10.3934/math.2023071. Publicly published 20 October 2022.
2. Zhouchao Wei, Pei Yu, Wei Zhang, and Minghui Yao, “Study of hidden attractors, multiple limit cycles from Hopf bifurcation and boundedness of motion in the generalized hyperchaotic Rabinovich system,” *Nonlinear Dynamics* 82, 131–141 (2015), DOI 10.1007/s11071-015-2144-8.
3. Yongjian Liu, “Circuit implementation and finite-time synchronization of the 4D Rabinovich hyperchaotic system,” *Nonlinear Dynamics* 67, 89–96 (2012), DOI 10.1007/s11071-011-9960-2.
4. Yongjian Liu et al., “A hyperchaotic system from the Rabinovich system,” *Journal of Computational and Applied Mathematics* 234(1), 101–113 (2010), DOI 10.1016/j.cam.2009.12.008.
