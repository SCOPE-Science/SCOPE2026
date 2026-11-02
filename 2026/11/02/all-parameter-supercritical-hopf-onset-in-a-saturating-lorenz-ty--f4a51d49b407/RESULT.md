# All-parameter supercritical Hopf onset in a saturating Lorenz-type oscillator

## Finding

Consider the three-dimensional real analytic system
\[
\dot x=\sigma(y-x)-r,\qquad
\dot y=-xz+(\phi(x)-1)y,\qquad
\dot z=xy+(\phi(x)-1)z,
\quad \phi(x)=\frac{\kappa x^2}{1+\varepsilon x^2},
\]
for every \(\sigma>0\), \(\kappa>\varepsilon>0\), with real forcing \(r\). Put \(\Delta=\kappa-\varepsilon\) and \(r_H=\sigma/\sqrt\Delta\). At both \(r=\pm r_H\), the unique equilibrium undergoes a nondegenerate **supercritical Hopf bifurcation**. In particular, for each fixed admissible parameter triple there is a sufficiently small neighborhood of either threshold such that, on the side \(|r|>r_H\), exactly one nonconstant periodic orbit lies near the equilibrium, modulo temporal phase; it is orbitally asymptotically stable. The equilibrium is asymptotically stable on the nearby side \(|r|<r_H\) and unstable on the nearby side \(|r|>r_H\).

For the positive threshold, the real resonant cubic coefficient of the local amplitude equation in a complex coordinate equal to \(y+iz+O((y^2+z^2))\) at criticality is exactly
\[
\boxed{\nu=-\frac{\sigma\Delta^3[\sigma(\kappa+4\varepsilon)+4\Delta]}{2\kappa^2(1+\sigma^2\Delta)}<0.}
\]
If \(\Gamma_r\) is the small periodic orbit for \(r>r_H\), its physical transverse amplitude has the sharp law
\[
\boxed{\lim_{r\downarrow r_H}\frac{\max_{(x,y,z)\in\Gamma_r}\sqrt{y^2+z^2}}{\sqrt{r-r_H}}=
\sqrt{\frac{4\kappa(1+\sigma^2\Delta)}{\sigma^2\Delta^{3/2}[\sigma(\kappa+4\varepsilon)+4\Delta]}}.}
\]
The period tends to \(2\pi\sqrt\Delta\). The same amplitude law holds at the negative threshold with \(r-r_H\) replaced by \(|r|-r_H\). The sign of \(\nu\) never vanishes throughout the stated parameter domain, precluding a generalized-Hopf degeneracy *on either of these threshold surfaces*.

## Assumptions and scope

Only real, finite states and the smooth ODE above are considered. \(\varepsilon\) is the saturation parameter and is distinct from a perturbation amplitude. The assertions concern periodic orbits within a parameter-dependent neighborhood of the equilibrium and are not global statements about attractors for large forcing. The normal-form coefficient \(\nu\) is normalized using the physical complex signal \(q=y+iz\) and a near-identity coordinate \(Z=q+O(|q|^2)\); a differently scaled classical first Lyapunov coefficient has the same strictly negative sign.

## Proof

**Equilibrium and crossing.** The complex signal \(q=y+iz\) obeys the exact equation
\[
\dot q=(\phi(x)-1+ix)q.
\]
An equilibrium with \(q\ne0\) would require \(\phi(x)=1\) and \(x=0\), impossible since \(\phi(0)=0\). Thus the unique equilibrium is \((-r/\sigma,0,0)\). Its eigenvalues are
\[
-\sigma,\qquad \phi(-r/\sigma)-1\pm i(-r/\sigma).
\]
The only nonzero-frequency crossings are \(r=\pm\sigma/\sqrt\Delta\). At the positive crossing \(x_0=-1/\sqrt\Delta=:\omega\), the growth-rate derivative is
\[
\left.\frac{d}{dr}[\phi(-r/\sigma)-1]\right|_{r_H}
=\frac{2\Delta^{3/2}}{\kappa\sigma}>0.
\]
The stable eigenvalue remains \(-\sigma\) and the oscillatory frequency has magnitude \(1/\sqrt\Delta\).

**Center-manifold reduction.** Put \(u=x+r_H/\sigma\), \(q=y+iz\), and specialize temporarily to \(r=r_H\). Taylor expansion gives
\[
\dot u=-\sigma u+\frac\sigma2(q+\bar q),\qquad
\dot q=i\omega q+(c+i)uq+du^2q+O(|u|^3|q|),
\]
where
\[
\omega=-\Delta^{-1/2},\quad c=\phi'(\omega)=-\frac{2\Delta^{3/2}}\kappa,\quad
d=\frac{\phi''(\omega)}2=\frac{\Delta^2(\kappa-4\varepsilon)}{\kappa^2}.
\]
The two-dimensional center manifold can be written as \(u=h(q,\bar q)\), whose linear coefficients are \(h_1=aq+\bar a\bar q\) with
\[
a=\frac{\sigma}{2(\sigma+i\omega)}.
\]
The coefficient of \(q\bar q\) in the quadratic part of \(h\) follows by inserting the invariance equation \(D h\cdot(\dot q,\dot{\bar q})=-\sigma h+\sigma(q+\bar q)/2\):
\[
h_{11}=-\frac{2c|a|^2}{\sigma}.
\]
For reference, the other quadratic coefficient is \(h_{20}=-a^2(c+i)/(\sigma+2i\omega)\), and \(h_{02}=\bar h_{20}\). Both are nonresonant for the cubic radial coefficient.

**Exact resonant coefficient.** Let \(C=c+i\). The quadratic terms of the reduced complex equation are \(Aq^2+Bq\bar q\), with \(A=Ca\) and \(B=C\bar a\). The raw coefficient of \(q^2\bar q\) at degree three is \(Ch_{11}+2d|a|^2\). Remove quadratic terms with the near-identity change
\[
q=Z+\frac{A}{i\omega}Z^2-\frac{B}{i\omega}Z\bar Z+O(|Z|^3).
\]
The induced cubic correction at \(Z^2\bar Z\) is
\[
2A\left(-\frac B{i\omega}\right)
+B\frac A{i\omega}
+B\overline{\left(-\frac B{i\omega}\right)}
=-\frac{AB}{i\omega}+\frac{|B|^2}{i\omega}.
\]
The last term is purely imaginary, while \(AB=C^2|a|^2\) has imaginary part \(2c|a|^2\). Therefore the real resonant cubic coefficient is
\[
\nu=\operatorname{Re}(Ch_{11})+2d|a|^2-\frac{2c|a|^2}{\omega}
=|a|^2\left(2d-\frac{2c^2}{\sigma}-\frac{2c}{\omega}\right).
\]
Using \(|a|^2=\sigma^2/[4(\sigma^2+\Delta^{-1})]\), direct simplification yields the displayed negative rational expression for \(\nu\). Every factor in its denominator is positive and so is the bracket \(\sigma(\kappa+4\varepsilon)+4\Delta\).

**Hopf and amplitude.** The ordinary smooth Hopf theorem applies because the crossing speed and \(\nu\) are nonzero, with \(\nu<0\). In the stated normalization the radial equation has leading terms
\[
\dot R=\left(\frac{2\Delta^{3/2}}{\kappa\sigma}(r-r_H)\right)R+\nu R^3+o(|r-r_H|R+R^3).
\]
Consequently the attracting periodic orbit satisfies \(R^2\sim -[2\Delta^{3/2}/(\kappa\sigma\nu)](r-r_H)\). Since \(Z=q+O(|q|^2)\), the maximum physical radius has the stated leading coefficient. Standard Hopf theory gives local uniqueness, orbital asymptotic stability, and convergence of the period to \(2\pi/|\omega|\). Finally, \((x,y,z,r)\mapsto(-x,-y,z,-r)\) is an exact conjugacy of the parameterized family, proving all negative-threshold assertions.

## Verification

Run `python3 verify_hopf.py` with SymPy installed. The script checks the generic coefficient simplification for positive \(\Delta\), the Hopf crossing derivative, the algebra of the quadratic elimination, and independent third-order Hopf normal-form calculations via the real multilinear eigenvector formula at two rational parameter points. Its exact-arithmetic test parameters are chosen to make the critical frequency rational; they are not substitutes for the symbolic proof for all admissible parameters.

## Relationship to prior work

Khodabandehlou and Maes introduced this specific saturating Lorenz-type system, computed the equilibrium and linear Hopf threshold, and reported numerical observations consistent with a supercritical onset for selected parameters. The threshold, the model, the existence of a numerical cycle, and generic Hopf theory are **prior work**. The contribution here is the explicit, strictly negative cubic coefficient for **every** \(\sigma>0\), \(\kappa>\varepsilon>0\), the uniform exclusion of a generalized-Hopf point on the threshold surfaces, and the leading physical oscillation amplitude.

The classical complex Lorenz equations of Fowler, Gibbon, and McGuinness contain a different complex coupling and do not have the same scalar saturation-gated system. General Hopf coefficient formulas provide the methodology, not an evaluation of the above expression. The nonidentity of two dynamical systems alone does not establish priority; the claim is limited to the explicitly inspected sources.

## Limitations

The result is local in state and forcing, for each fixed parameter triple. It does not prove a global attracting cycle or preclude distant chaotic or multiple attractors. The exclusion of generalized-Hopf degeneracy applies at the identified Hopf equilibria, not at unrelated bifurcations. The coefficient \(\nu\) is coordinate-normalized and is not presented as a universally normalized first Lyapunov coefficient. Published-priority assessment is best knowledge from the inspected material; independent verification has not been performed.

## References

1. F. Khodabandehlou and C. Maes, *Local Detailed Balance in the Lorenz Model: Replaces the Butterfly with Frenetic Bursting*, arXiv:2609.21415v1 (first posted 2026-09-18), Sections II and V and the Conclusion. https://arxiv.org/html/2609.21415v1
2. A. C. Fowler, J. D. Gibbon, and M. J. McGuinness, *The complex Lorenz equations*, Physica D 4 (1982), 139–163, doi:10.1016/0167-2789(82)90057-4.
3. *Andronov–Hopf bifurcation*, Scholarpedia, first-Lyapunov-coefficient and normal-form discussion. https://www.scholarpedia.org/article/Andronov-Hopf
