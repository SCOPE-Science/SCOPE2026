# Exact stationary balances and a recurrence-height barrier for the Shimizu–Morioka/Rucklidge family

Consider the three-parameter quadratic flow
\[
\dot x=y,\qquad
\dot y=x(\rho-z)-a y,\qquad
\dot z=x^2-bz,
\tag{1}
\]
with \(a,b,\rho>0\). The standard Shimizu–Morioka normalization is \(\rho=1\). After interchanging its first two coordinates, the standard Rucklidge system is the case \(b=1\). The equilibria of (1) are
\[
O=(0,0,0),\qquad P_\pm=(\pm\sqrt{b\rho},0,\rho).
\]

## Main theorem

Define
\[
A=xy+\frac a2x^2+\frac12z^2-\rho z,
\qquad
B=x^2z+y^2-\rho x^2-\frac b2z^2.
\]
Along every classical solution of (1),
\[
\boxed{\dot A=y^2-bz(z-\rho)},
\tag{2}
\]
and
\[
\boxed{\dot B=(x^2-bz)^2-2ay^2=\dot z^{\,2}-2a\dot x^{\,2}}.
\tag{3}
\]

Let \(\mu\) be any compactly supported invariant probability measure for (1). Then
\[
\boxed{\mathbb E_\mu[x^2\mid z]=bz}\qquad \mu\text{-almost surely},
\tag{4}
\]
so in particular \(z\ge0\) \(\mu\)-almost surely, and
\[
\boxed{\int y^2\,d\mu=b\int z(z-\rho)\,d\mu},
\tag{5}
\]
\[
\boxed{\int (x^2-bz)^2\,d\mu=2a\int y^2\,d\mu}.
\tag{6}
\]
Equivalently,
\[
\mathbb E_\mu\!\left[\operatorname{Var}_\mu(x^2\mid z)\right]
=2ab\,\mathbb E_\mu[z(z-\rho)],
\tag{7}
\]
and
\[
\operatorname{Var}_\mu(x^2)
=b^2\operatorname{Var}_\mu(z)+2ab\,\mathbb E_\mu[z(z-\rho)].
\tag{8}
\]

Equality in (5), in the sense \(\int y^2\,d\mu=0\), occurs if and only if \(\mu\) is supported on the three equilibria \(\{O,P_+,P_-\}\). Consequently every compactly supported invariant probability measure that is not equilibrium-supported satisfies
\[
\int y^2\,d\mu>0,
\qquad
\int z(z-\rho)\,d\mu>0,
\qquad
\boxed{\mu\{z>\rho\}>0}.
\tag{9}
\]
Thus every non-equilibrium ergodic recurrent state must visit the region above the nonzero-equilibrium height \(z=\rho\). In particular, no nontrivial recurrent invariant probability measure can be confined to the slab \(0\le z\le\rho\). Moreover, conditioning (4) on \(z>\rho\) gives
\[
\boxed{\mu\{x^2>b\rho\}>0},
\tag{10}
\]
so non-equilibrium recurrence must also exceed the nonzero-equilibrium amplitude \(|x|=\sqrt{b\rho}\).

If \(m=\int z\,d\mu\in(0,\rho)\), (5) also gives the strict fluctuation floor
\[
\boxed{\operatorname{Var}_\mu(z)>m(\rho-m)}.
\tag{11}
\]

## Periodic-orbit consequence

Every nonconstant periodic solution of minimal period \(P\) satisfies
\[
\boxed{\int_0^P \dot z(t)^2\,dt
      =2a\int_0^P \dot x(t)^2\,dt},
\tag{12}
\]
so that
\[
\frac{\|\dot z\|_{L^2(0,P)}}{\|\dot x\|_{L^2(0,P)}}=\sqrt{2a},
\tag{13}
\]
and necessarily
\[
\boxed{\max_{0\le t<P} z(t)>\rho,\qquad
\max_{0\le t<P}|x(t)|>\sqrt{b\rho}}.
\tag{14}
\]
The derivative-energy ratio (13) is independent of \(b\), \(\rho\), the orbit amplitude, and the period. The two geometric thresholds are sharp as uniform parameter-only barriers: known Hopf branches can shrink to \(P_\pm\), whose coordinates lie exactly on \(z=\rho\) and \(|x|=\sqrt{b\rho}\).

## Proof

Differentiating \(A\) along (1) gives
\[
\begin{aligned}
\dot A
&=y^2+x\bigl(x(\rho-z)-ay\bigr)+axy+(z-\rho)(x^2-bz)\\
&=y^2-bz(z-\rho),
\end{aligned}
\]
which proves (2). Likewise,
\[
\begin{aligned}
\dot B
&=2xyz+x^2(x^2-bz)
 +2y\bigl(x(\rho-z)-ay\bigr)-2\rho xy-bz(x^2-bz)\\
&=(x^2-bz)^2-2ay^2,
\end{aligned}
\]
which proves (3).

For an invariant probability measure with compact support, \(\int Lf\,d\mu=0\) for every \(C^1\) test function \(f\), where \(L\) is the Lie derivative of (1). Applying this to \(A\) and \(B\) gives (5) and (6).

For any \(C^1\) function \(\Phi\) of one variable,
\[
L\Phi(z)=\Phi'(z)(x^2-bz).
\]
Hence
\[
\int \psi(z)(x^2-bz)\,d\mu=0
\]
for every continuous \(\psi\), by choosing \(\Phi' = \psi\). This is exactly the conditional-expectation statement (4). Since \(x^2\ge0\) and \(b>0\), (4) implies \(z\ge0\) almost surely. Equations (7) and (8) then follow from (4), (6), and the conditional-variance decomposition.

It remains to classify equality. If \(\int y^2d\mu=0\), then \(y=0\) almost surely. Equation (6) also gives \(x^2-bz=0\) almost surely. Invariance of \(\mu\) implies that almost every orbit starting in this full-measure set remains in \(y=0\); differentiating there yields \(x(\rho-z)=0\). Therefore almost every point satisfies
\[
y=0,\qquad x^2=bz,\qquad x(\rho-z)=0,
\]
which is precisely \(O\) or \(P_\pm\). The converse is immediate because all three points are equilibria. This proves the equality classification. If \(\mu\) is not equilibrium-supported, (5) is therefore strict. Because \(z\ge0\) and \(z(z-\rho)\le0\) on \([0,\rho]\), strict positivity forces positive mass in \(z>\rho\), proving (9). On that set, (4) gives conditional mean \(\mathbb E[x^2\mid z]=bz>b\rho\); hence positive measure must satisfy \(x^2>b\rho\), proving (10). Writing \(\mathbb E[z^2]-\rho\mathbb E[z]=\operatorname{Var}(z)-m(\rho-m)\) proves (11). The normalized time measure on a nonconstant periodic orbit is not equilibrium-supported, so (12)–(14) follow from (3), (9), and (10).

A related pointwise fact is useful geometrically: every bounded complete solution satisfies
\[
z(t)=\int_0^\infty e^{-bs}x(t-s)^2\,ds\ge0.
\tag{15}
\]
The only bounded complete solution for which the right-hand side vanishes at some time is the origin. Thus nontrivial bounded complete dynamics actually lie in \(z>0\).

## Context and originality

Shimizu and Morioka introduced the normalized system to study limit-cycle bifurcation in a simplified Lorenz-type model. Shilnikov subsequently developed the classical bifurcation and Lorenz-attractor picture, including homoclinic and periodic structures. Rucklidge derived the equivalent double-convection form with a free linear coupling parameter, and later work treated local multiplicity of Hopf-born cycles, dynamics at infinity, rigorous Lorenz-attractor existence, homoclinic/heteroclinic connections, and periodic-orbit topology. Darboux, analytic, and meromorphic integrability of the Shimizu–Morioka/Rucklidge family and invariant algebraic manifolds of the Rucklidge form have also been studied.

Within the sources checked, no statement was found of the paired coboundaries (2)–(3), their invariant-measure consequences (4)–(8), the equilibrium-only equality classification, or the resulting height-and-amplitude recurrence barriers (9)–(10) in either Shimizu–Morioka or equivalent Rucklidge variables. The conditional relation (4) by itself is a standard stationarity consequence of the scalar equation \(\dot z=x^2-bz\); the claimed contribution is the coupled package of exact balances, equality classification, and recurrence/periodic-orbit consequences.

The closest residual originality risks are the complete theorem-level contents of the original 1980 paper, the 2014 Rucklidge integrability paper, the 2020 Shimizu–Morioka integrability paper, and the 2023 Rucklidge invariant-algebraic-manifold paper. Their available descriptions concern limit-cycle bifurcation, first-integral/nonintegrability questions, equivalence transformations, and algebraic invariant manifolds, respectively, but not the stationary balance statements above. Originality is therefore asserted only to the best of our knowledge.

## Limitations

The theorem supplies necessary constraints on compact recurrent dynamics; it does not prove that a periodic orbit, chaotic attractor, or other non-equilibrium invariant state exists for a given parameter triple. It also does not classify compact invariant sets that carry only equilibrium-supported invariant probability measures, such as possible connecting structures. The assumptions \(a,b,\rho>0\) are essential to the sign interpretation of the recurrence barrier. No claim is made that the elementary conditional law (4), considered in isolation, is new.

## Reproducibility

`artifacts/verify_balances.py` was executed with SymPy 1.14.0 and uses exact symbolic differentiation to verify (2), (3), and the algebraic variance rewrite used in (11). `artifacts/verification.txt` records the zero residuals.

## References

1. T. Shimizu and N. Morioka, “On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model,” *Physics Letters A* 76 (1980), 201–204. https://doi.org/10.1016/0375-9601(80)90466-1
2. A. L. Shilnikov, “Bifurcation and chaos in the Marioka–Shimizu system,” *Selecta Mathematica Sovietica* 10 (1991), 105–117.
3. A. M. Rucklidge, “Chaos in a low-order model of magnetoconvection,” *Physica D* 62 (1993), 323–337. https://doi.org/10.1016/0167-2789(93)90291-8
4. L. Liu and B. Gao, “Conditions for appearance and disappearance of limit cycles in the Shimizu–Morioka system,” *International Journal of Bifurcation and Chaos* 21 (2011), 2489–2503. https://doi.org/10.1142/S0218127411029884
5. M. Messias, M. Gouveia, and C. Pessoa, “Dynamics at infinity and other global dynamical aspects of Shimizu–Morioka equations,” *Nonlinear Dynamics* 69 (2012), 577–587. https://doi.org/10.1007/s11071-011-0288-8
6. F. S. Dias and L. F. Mello, “Hopf bifurcations and small amplitude limit cycles in Rucklidge systems,” *Electronic Journal of Differential Equations* 2013(48), 1–9.
7. M. F. S. Lima, J. Llibre, and C. Valls, “Integrability of the Rucklidge system,” *Nonlinear Dynamics* 77 (2014), 1441–1453. https://doi.org/10.1007/s11071-014-1389-y
8. X. Huang, Y. Shi, and X. Li, “Integrability analysis of the Shimizu–Morioka system,” *Communications in Nonlinear Science and Numerical Simulation* 84 (2020), 105101. https://doi.org/10.1016/j.cnsns.2019.105101
9. M. V. Demina and D. O. Ilyukhin, “Invariant algebraic manifolds for the Rucklidge model of double convection,” *Siberian Mathematical Journal* 64 (2023), 1145–1152. https://doi.org/10.1134/S0037446623050075
10. M. J. Capiński, D. Turaev, and P. Zgliczyński, “Computer assisted proof of the existence of the Lorenz attractor in the Shimizu–Morioka system,” *Nonlinearity* 31 (2018), 5410–5440. https://doi.org/10.1088/1361-6544/aae032
11. O. Hénot and A. Takayasu, “Computer-Assisted Proofs in Dynamical Systems: A Case Study of a Heteroclinic Orbit in the Shimizu--Morioka System,” arXiv:2605.07500 (2026). https://arxiv.org/abs/2605.07500
12. A. Kazakov, V. Koryakin, K. Safonov, and A. L. Shilnikov, “Cascades of Lorenz attractors in the Shimizu-Morioka model,” arXiv:2512.14919 (2025). https://arxiv.org/abs/2512.14919
