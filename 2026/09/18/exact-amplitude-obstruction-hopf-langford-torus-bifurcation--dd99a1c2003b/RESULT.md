# Exact amplitude geometry obstructs Neimark-Sacker tori in the Hopf-Langford type system

## Result

Consider the Hopf-Langford type system studied in arXiv:2609.18010,
\[
\dot x=x(\mu-\alpha)-\beta y+xz,\qquad
\dot y=\beta x+y(\mu-\alpha)+yz,
\]
\[
\dot z=\mu z-\gamma(x^2+y^2+z^2),
\]
with \(\beta\neq0\). Put
\[
s=x^2+y^2>0,
\qquad
D=(1+2\gamma)\mu-2\gamma\alpha.
\]
Then the system reduces exactly to
\[
\dot s=2s(\mu-\alpha+z),\qquad
\dot z=\mu z-\gamma(s+z^2),\qquad
\dot\theta=\beta.
\]
This exact autonomous amplitude reduction imposes a structural obstruction on the Neimark-Sacker bifurcation asserted in Theorem 2 of arXiv:2609.18010v1.

### Theorem

Assume a circular periodic orbit exists in \(s>0\), equivalently
\[
z_*=\alpha-\mu,
\qquad
s_*=(\alpha-\mu)\left(\frac{\mu}{\gamma}-(\alpha-\mu)\right)>0,
\]
with \(\gamma\neq0\). Its transverse Floquet exponents are the roots of
\[
\lambda^2-D\lambda+2\gamma s_*=0.
\]
Hence, when \(\gamma s_*>0\), a conjugate pair can have unit-modulus Floquet multipliers only on the exact surface
\[
\boxed{D=0.}
\]

Moreover, for every real \(\gamma\), on the half-plane \(s>0\) the positive Dulac density
\[
B(s)=s^{\gamma-1}
\]
satisfies
\[
\boxed{\operatorname{div}(BF)=D\,B},
\]
where \(F\) is the planar \((s,z)\) vector field. Consequently, if \(D\neq0\), the time-\(T\) map of the amplitude flow, \(T=2\pi/|\beta|\), cannot possess an invariant Jordan curve bounding a region compactly contained in \(s>0\). Therefore no sufficiently local smooth invariant torus transverse to the angular flow can surround the circular periodic orbit when \(D\neq0\).

On the neutral surface \(D=0\), assume \(\gamma>0\) and \(\alpha\neq0\), and set
\[
c=\frac{\alpha}{1+2\gamma},
\qquad
\mu=2\gamma c.
\]
Then \((s_*,z_*)=(c^2,c)\) and the amplitude system has the first integral
\[
\boxed{
H(s,z)=s^\gamma\big((z-c)^2-c^2\big)
      +\frac{\gamma}{\gamma+1}s^{\gamma+1}.
}
\]
At \((c^2,c)\), the Hessian of \(H\) is positive definite:
\[
H_{ss}=\gamma(c^2)^{\gamma-1}>0,
\qquad
H_{zz}=2(c^2)^\gamma>0,
\qquad
H_{sz}=0.
\]
Thus the amplitude equilibrium is a nonlinear center and is surrounded by a continuum of closed level curves. Lifting them through the independent rotation \(\dot\theta=\beta\) gives a continuum of neutral invariant two-tori on \(D=0\), rather than a unique torus created on one side of a generic Neimark-Sacker bifurcation.

Therefore the source system has the exact local alternative
\[
\boxed{
D\neq0:\ \text{no surrounding local invariant torus},
\qquad
D=0:\ \text{a center foliation with a continuum of neutral tori}.
}
\]
In particular, the unique unstable torus asserted by Theorem 2 of arXiv:2609.18010v1 is incompatible with the exact amplitude dynamics.

## Proof

Writing \(x=r\cos\theta\), \(y=r\sin\theta\), \(s=r^2\) gives the displayed amplitude system directly. At a positive equilibrium, \(\mu-\alpha+z_*=0\), hence \(z_*=\alpha-\mu\), and the second equation yields the formula for \(s_*\). The amplitude Jacobian there is
\[
J_*=
\begin{pmatrix}
0&2s_*\\
-\gamma&D
\end{pmatrix},
\]
which proves the characteristic polynomial and the exact trace condition.

For the global local-torus obstruction, a direct calculation gives
\[
\partial_s(B\dot s)+\partial_z(B\dot z)=D B.
\]
Let \(\Phi_t\) denote the amplitude flow and let \(R\Subset\{s>0\}\). The weighted area
\[
A_B(R)=\iint_R B(s)\,ds\,dz
\]
therefore obeys
\[
A_B(\Phi_t(R))=e^{Dt}A_B(R).
\]
A smooth invariant torus surrounding the circular orbit and transverse to \(\theta\) intersects \(\theta=0\) in an invariant Jordan curve \(C\) for \(\Phi_T\). Its bounded interior \(R\) must satisfy \(\Phi_T(R)=R\), contradicting the weighted-area identity unless \(D=0\).

When \(D=0\), substituting \(\alpha=(1+2\gamma)c\) and \(\mu=2\gamma c\) into the amplitude equations and differentiating the displayed \(H\) gives \(dH/dt=0\) identically. The Hessian computation makes the positive equilibrium a strict local minimum of \(H\), hence a center. Each nearby regular level curve is a closed amplitude orbit, and its product with the angular circle is an invariant two-torus.

## Consequence for the perturbative bifurcation curve

The source uses
\[
\alpha=\alpha_1\varepsilon+\alpha_2\varepsilon^2+O(\varepsilon^3),
\quad
\gamma=\gamma_0+\gamma_1\varepsilon+O(\varepsilon^2),
\]
\[
\mu=\mu_1\varepsilon+\mu_2\varepsilon^2+O(\varepsilon^3)
\]
and treats \(\mu_1\) as the bifurcation parameter. If
\[
\mu_1^{\rm crit}(\varepsilon)=M_0+M_1\varepsilon+O(\varepsilon^2),
\]
then the exact unit-modulus condition \(D=0\) forces
\[
\boxed{M_0=\frac{2\alpha_1\gamma_0}{2\gamma_0+1}},
\]
\[
\boxed{
M_1=
\frac{2\gamma_0\alpha_2}{2\gamma_0+1}
+\frac{2\alpha_1\gamma_1}{(2\gamma_0+1)^2}
-\mu_2.
}
\]
Notably this correction contains neither \(\beta\), \(\omega\), nor \(\pi\).

For the admissible choice
\[
\alpha_1=\gamma_0=\omega=1,
\qquad
\alpha_2=\gamma_1=\mu_2=0,
\]
the source assumptions (4) hold at \(M_0=2/3\): the two strict expressions are \(1/9>0\) and \(-8/9<0\). The exact neutral curve has \(M_1=0\), whereas Eq. (7) of arXiv:2609.18010v1 gives
\[
\widehat\mu_1=\frac{8\pi^2-2}{27}\approx2.85025315588.
\]
Thus the claimed Neimark-Sacker curve already disagrees with the exact Floquet-neutral surface at its first correction term.

## Numerical example in the source

The source's Example 2 takes
\[
\gamma=-1-\varepsilon+0.04\varepsilon^2,
\]
so its leading coefficient is \(\gamma_0=-1\), contrary to the standing hypothesis \(\gamma_0>0\) in condition (4). At \(\varepsilon=10^{-3}\), direct substitution gives
\[
s_*\approx2.98128987351\times10^{-6},
\]
\[
D\approx-1.99917616054\times10^{-3},
\qquad
2\gamma s_*\approx-5.96854208826\times10^{-6}.
\]
The positive-radius circular periodic orbit is therefore transversely saddle-type, not at a Neimark-Sacker point.

## Relation to prior literature

The cylindrical reduction and integrability mechanism are not claimed as new. Vassilev and Nikolov, *First and Second Integrals of Hopf-Langford-Type Systems* (Axioms 14(1):8), treat a seven-parameter generalization, reduce it to a planar amplitude/Lienard system, and give first-integral conditions. Under the parameter identification appropriate to the present source system, their integrability condition becomes exactly
\[
2\gamma(\mu-\alpha)+\mu=0,
\]
i.e. \(D=0\); their complementary equal-coefficient case covers \(\gamma=1\). This prior result strongly corroborates that the neutral surface is integrable rather than a generic Neimark-Sacker surface.

The source paper itself cites that integrability literature but nevertheless states a unique torus bifurcation. The contribution recorded here is the source-specific obstruction: the exact transverse spectrum, weighted-area identity, and center foliation jointly show that the asserted generic Neimark-Sacker scenario cannot occur in the stated SO(2)-symmetric system, and they give an explicit admissible coefficient set for which the published perturbative curve conflicts with the exact neutral curve.

## Verification

`artifacts/verify_obstruction.py` performs deterministic arithmetic checks of the neutral first-integral identity at sample points, the admissibility inequalities and bifurcation-curve mismatch above, and the source Example 2 transverse determinant. It was executed successfully; its reported values agree with the formulas in this record.

## Limitations

The no-torus statement concerns smooth local invariant tori lying in \(s>0\), transverse to the angular flow and surrounding the circular periodic orbit, which is precisely the geometry asserted in the source theorem. It does not classify invariant sets touching the rotation axis, the degenerate case \(\beta=0\), or generalized Hopf-Langford perturbations that break the exact rotational symmetry. The first-integral mechanism is prior literature, not a novelty claim. The source is a very recent arXiv v1, so a later revision may correct the issue.

## References

1. G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (2026). https://arxiv.org/abs/2609.18010
2. V. M. Vassilev and S. G. Nikolov, *First and Second Integrals of Hopf-Langford-Type Systems*, Axioms 14(1):8. https://doi.org/10.3390/axioms14010008
3. M. R. Cândido and D. D. Novaes, *On the torus bifurcation in averaging theory*, Journal of Differential Equations 268 (2020), 4555--4576. https://doi.org/10.1016/j.jde.2019.11.046
