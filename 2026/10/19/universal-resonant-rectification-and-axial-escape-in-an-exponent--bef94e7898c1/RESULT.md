# Global synchronization and axial escape in a weakly forced exponential Duffing lift

## Finding

Consider the system
\[
\dot x=y,\qquad \dot y=-y-x-Bx^3+\varepsilon\cos t,\qquad
\dot z=\alpha x e^{\beta x}.
\]
Suppose that \(B\ge0\), \(\varepsilon>0\), \(B\varepsilon^2\le 1/256\), \(\alpha\ne0\), and \(\beta\in\mathbb R\). There is a unique \(2\pi\)-periodic planar response \((X,Y)\), and it obeys \((X,Y)(t+\pi)=-(X,Y)(t)\). For **every** real initial condition of the three-dimensional system, the solution exists for all forward time and satisfies
\[
(x(t),y(t))=(X(t),Y(t))+O(e^{-t/8}),\qquad
z(t)=Jt+P(t)+L+O(e^{-t/8}),
\]
where \(L\) depends on the initial condition, \(P\) is \(2\pi\)-periodic with \(P(0)=0\), and the speed is independent of the initial condition:
\[
J=\frac{\alpha}{2\pi}\int_0^{2\pi}X(t)e^{\beta X(t)}\,dt
=\frac{\alpha}{\pi}\int_0^\pi X(t)\sinh(\beta X(t))\,dt.
\]
The speed has the sign of \(\alpha\beta\) and vanishes exactly at \(\beta=0\). At zero tilt, every axial coordinate remains bounded and is asymptotically periodic. For nonzero tilt every axial coordinate escapes linearly, and the phase-extended flow has no nonempty compact forward-invariant set. The significant feature is the **global** conclusion on an explicit forcing domain, not the existence of drift along a locally attracting cycle alone.

## Assumptions and scope

The model is the exactly linearly resonant, positively damped single-well slice of the exponential lift of Liu et al. [1], with their parameters \(a=\zeta=-1\), \(b=B\), \(c=\varepsilon\), \(d=1\), and \(g=0\). The initial state is arbitrary. The bound on \(B\varepsilon^2\) is sufficient, not asserted to be sharp. The axial coordinate is real, not taken modulo a period. The result does not concern the large-forcing parameter examples of [1].

## Proof

**Absorption.** Set
\[
V(x,y)=\tfrac12(y+x/2)^2+\tfrac58x^2+\tfrac B4x^4,
\qquad D=\{(x,y):V(x,y)\le8\varepsilon^2\}.
\]
Along a solution,
\[
\dot V=-\tfrac12(y^2+x^2+Bx^4)+\varepsilon(y+x/2)\cos t.
\]
Cauchy–Schwarz and Young's inequality give \(\varepsilon|y+x/2|\le(x^2+y^2)/8+(5/2)\varepsilon^2\). The bound \(V\le x^2+y^2+Bx^4\) implies
\[
\dot V\le-\tfrac38 V+\tfrac52\varepsilon^2.
\]
The coercive energy bound gives planar forward existence, and \(z\) is a finite integral of a smooth function of \(x\) on any finite time interval. Integration of the inequality gives
\[
V(t)\le V(0)e^{-3t/8}+\tfrac{20}{3}\varepsilon^2(1-e^{-3t/8}).
\]
Since \(20/3<8\), each trajectory enters \(D\) in finite time. At its boundary the derivative is at most \(-\varepsilon^2/2\); hence the compact sublevel is forward invariant.

**Contraction and periodicity.** For two planar solutions in \(D\), let \(w=x_1-x_2\), \(v=y_1-y_2\), and \(r=B(x_1^2+x_1x_2+x_2^2)\). They satisfy \(\dot w=v\), \(\dot v=-v-(1+r)w\). As \(V\ge5x^2/8\), we have \(0\le r\le(192/5)B\varepsilon^2\le3/20\). The quadratic form \(W(w,v)=\tfrac12(v+w/2)^2+\tfrac58w^2\) satisfies
\[
\begin{aligned}
\dot W&=-\tfrac12(v^2+w^2)-rw(v+w/2)\\
&\le-\bigl(\tfrac12-\tfrac r2\bigr)v^2-\bigl(\tfrac12-r\bigr)w^2
\le-\tfrac14(v^2+w^2)\le-\tfrac14 W.
\end{aligned}
\]
The time-\(2\pi\) map is a strict contraction of the nonempty compact set \(D\) in the metric induced by \(\sqrt W\). Its fixed point gives the periodic response. Every other trajectory eventually enters \(D\), and its difference from the periodic response then decays as \(O(e^{-t/8})\) in Euclidean norm. This also rules out any other periodic solution, since its periodic separation from \((X,Y)\) could not tend to zero unless it were identically zero. The half-period sign change and time shift send a periodic solution to a periodic solution, giving the claimed antisymmetry by uniqueness. The forcing with \(\varepsilon>0\) excludes \(X\equiv0\).

**Axial asymptotics.** Pair the two half periods in the definition of \(J\) to obtain the integral with \(\sinh\). For any nonzero real \(u\), \(u\sinh(\beta u)\) has the strict sign of \(\beta\) when \(\beta\ne0\). Since the continuous orbit is nonzero on a set of positive measure, the signed integral is strict, and it vanishes when \(\beta=0\). Put
\[
P(t)=\int_0^t\bigl(\alpha X(s)e^{\beta X(s)}-J\bigr)\,ds.
\]
Its integrand has zero mean over one period, so \(P\) is periodic. By planar convergence and local Lipschitz continuity on the eventual compact range, the difference \(d(t)=\alpha[x(t)e^{\beta x(t)}-X(t)e^{\beta X(t)}]\) is \(O(e^{-t/8})\). Then \(L=z(0)+\int_0^\infty d(s)\,ds\) is well defined and the error is \(-\int_t^\infty d(s)\,ds=O(e^{-t/8})\). For an arbitrary initial phase, the same energy and contraction estimates apply with \(\cos(t+\theta_0)\); the periodic response is the corresponding time translate and the speed is unchanged. Nonzero speed therefore rules out a compact forward-invariant set in the phase extension, because any orbit contained in such a set would have bounded \(z\).

## Verification

The Lyapunov and difference-energy computations, the contraction bound, and the integral error estimate are the proof for all real initial conditions. The accompanying `verify.py` contains archival symbolic identity checks and numerical tests for representative periodic responses. It also checks a perturbation expansion of the periodic drift, which is not a new claim of this theorem. These finite tests do not verify an infinite initial-condition or parameter range.

## Relationship to prior work

Liu et al. [1, Eq. (1)] give the exponential-fiber model and study numerical diagnostics, including bifurcation plots and Poincaré sections. The theorem above is on a different, rigorously controlled weak-forcing regime and does not dispute their large-drive examples. Duffing periodic-response and symmetry methods are background [3,4]. The exact sign of the cycle-average axial drift from half-period symmetry and the perturbative quartic drift law are covered on the local branch by [2]. In particular, setting its damping, linear stiffness, and drive frequency to one in its general coefficient removes the cubic stiffness from the quartic term. No separate originality claim is made for that formula or for the sign argument on a periodic orbit. The additional result here is an explicit all-initial-data attracting domain in parameter space, with a quantitative transient, which yields escape of **every** lifted trajectory and excludes other compact forward dynamics at nonzero tilt. The local branch theorem alone does not give those properties.

## Limitations

The stated cutoff is not sharp and no assertion about asymptotic behavior beyond it is made. The rate and drift are exact consequences in the stated resonant slice, not a general forced Duffing classification. Some related older periodic-response papers were not available in full for comparison; priority is not asserted.

## References

1. S. Liu, Q. Wang, C. Liu, Y. Sun, and L. He, *Natural Exponential and Three-Dimensional Chaotic System*, Advanced Science **10** (2023), 2204269. https://doi.org/10.1002/advs.202204269.
2. *Positive exponential-fiber drift and a sharp quartic response reversal on forced Duffing cycles*. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-positive-exponential-fiber-drift-and-a-sharp-quartic-response-re--800af0f580fc.
3. H. Chen and Y. Li, *Bifurcation and stability of periodic solutions of Duffing equations*, Nonlinearity **21** (2008), 2485–2505. https://doi.org/10.1088/0951-7715/21/11/001.
4. Y.-P. Lin, *A Postverification Method for Solving Forced Duffing Oscillator Problems without Prescribed Periods*, Journal of Applied Mathematics (2014), 317460. https://doi.org/10.1155/2014/317460.
