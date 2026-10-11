# Periodic cylinders and two-end algebraic period laws in even-kinetic skew flows

## Finding

For every **even integer** \(p\geq4\), consider the autonomous polynomial system in its displayed physical time:
\[
\dot x=u-1,\qquad \dot u=v^{p-1},\qquad \dot v=u(u-2). \tag{1}
\]
Set \(V(u)=u^2-u^3/3\), \(H(u,v)=v^p/p+V(u)\), \(\alpha=1-1/p\) and \(\beta=1/2-1/p>0\). For each \(h\in(0,4/3)\), let \(a(h)\in(-1,0)\) and \(b(h)\in(0,2)\) be the two indicated roots of \(V(u)=h\), and let \(\gamma_h\) be the closed component of \(\{H=h\}\) with \(a(h)\leq u\leq b(h)\). Write
\[
I_k(h)=\int_{a(h)}^{b(h)}u^k(h-V(u))^{-\alpha}\,du\quad(k=0,1,2),
\qquad T_p(h)=2p^{-\alpha}I_0(h),
\qquad d_p(h)=\frac{I_1(h)}{I_0(h)}-1. \tag{2}
\]
Every projected orbit on \(\gamma_h\) has minimal physical-time period \(T_p(h)\). Along every lifted orbit in the invariant cylinder \(\mathcal C_h=\mathbb R_x\times\gamma_h\), the axial coordinate satisfies
\[
x(t)=d_p(h)t+\psi(t),\tag{3}
\]
where \(\psi\) is a bounded \(T_p(h)\)-periodic function (depending on its initial point). **The set**
\[
\mathcal Z_p=\{h\in(0,4/3):d_p(h)=0\} \tag{4}
\]
**is nonempty and finite**, is contained in \((2/3,4/3)\), and the complete three-dimensional system has a nonconstant periodic orbit exactly on \(\mathcal C_h\) with \(h\in\mathcal Z_p\). Each such cylinder is entirely foliated by periodic orbits of the same minimal period \(T_p(h)\); on every other oval cylinder, \(x(t)\) is unbounded linearly in both time directions.

The two *opposite* ends of the projected period annulus have **sharp, algebraic** periods. As \(h\downarrow0\),
\[
\boxed{T_p(h)\sim 2p^{-\alpha}\mathrm B\left(\frac12,\frac1p\right)h^{-\beta}},\qquad
\boxed{d_p(h)=-1+\frac{p}{2(p+2)}h+o(h)}.\tag{5}
\]
As \(\delta=4/3-h\downarrow0\),
\[
\boxed{T_p(h)\sim p^{-\alpha}\mathrm B\left(\frac1p,\beta\right)\delta^{-\beta}},\tag{6}
\]
\[
\boxed{d_p(h)=1-\frac{2\,3^{2/p}\mathrm B(1/p,2/p)}{\mathrm B(1/p,\beta)}\,\delta^\beta+o(\delta^\beta)}.\tag{7}
\]
Here \(\mathrm B\) is Euler's beta function. In particular \(T_p\) tends to infinity at **both** ends and attains an interior global minimum. Neither the number of elements of \(\mathcal Z_p\) nor uniqueness of that minimum is asserted.

## Assumptions and scope

All claims hold for each fixed even integer \(p\ge4\), real initial data and the original time of (1), with no time change. The planar Hamiltonian component has a degenerate center at \((u,v)=(0,0)\) and a degenerate saddle at \((2,0)\). The level \(h=0\) is an equilibrium, not a nonconstant cycle; \(h=4/3\) is the separatrix energy and is excluded from the periodic annulus. The values of \(\mathrm B\) are finite and positive because \(1/p>0\) and \(\beta>0\). The lifted system is a skew-product, not a globally nilpotent polynomial vector field for \(p\ge4\). No classification of maximal solutions on unbounded energy components is required for the stated periodic-orbit classification.

## Proof

**First integral and planar geometry.** Direct differentiation gives
\[
\frac{dH}{dt}=(2u-u^2)v^{p-1}+v^{p-1}u(u-2)=0.
\]
Since \(p\) is even, the kinetic term is nonnegative, strictly increasing away from zero on each velocity half-axis, and the potential \(V\) increases from its strict minimum at \(u=0\) to its strict maximum at \(u=2\). The first integral therefore has exactly one regular compact oval component \(\gamma_h\) for each \(0<h<4/3\), with turning points as stated. Other components are unbounded, the only planar equilibria are \((0,0)\) and \((2,0)\), and there are no other planar closed orbits. The vector field on each oval is nonzero, so it traverses the oval periodically.

**Exact period and translation.** On the upper half of \(\gamma_h\), \(v=(p(h-V(u)))^{1/p}\), so
\[
\frac{dt}{du}=p^{-\alpha}(h-V(u))^{-\alpha}.
\]
The lower half contributes the same elapsed time. This proves the period integral in (2). Integrating \(\dot x=u-1\) over one planar period yields \(x(t+T_p(h))-x(t)=T_p(h)d_p(h)\) with \(d_p\) given by (2). Subtracting the linear part proves (3). A periodic three-dimensional orbit must project to a planar periodic trajectory (or planar equilibrium). On the two planar equilibria, \(\dot x=-1\) and \(\dot x=1\), respectively, hence neither lift is periodic; on other projected trajectories periodicity is impossible. On \(\gamma_h\), the lift returns after one planar period exactly when \(d_p(h)=0\), proving the periodic-cylinder criterion and common minimal period.

**Small-energy end.** Scale \(u=\sqrt h\,s\). The turning points satisfy \(a(h)/\sqrt h\to-1\), \(b(h)/\sqrt h\to1\). Removing the two integrable algebraic endpoint singularities by a fixed-interval substitution (or factoring the other root of \(V(u)-h\)) gives
\[
I_0(h)\sim h^{1/2-\alpha}\int_{-1}^{1}(1-s^2)^{-\alpha}ds
=h^{-\beta}\mathrm B\left(\frac12,\frac1p\right),\tag{8}
\]
\[
\frac{I_2(h)}{hI_0(h)}\longrightarrow
\frac{\mathrm B(3/2,1/p)}{\mathrm B(1/2,1/p)}=\frac{p}{p+2}.\tag{9}
\]
Integrating \(\dot v=u(u-2)\) over any planar cycle gives the exact identity \(I_2(h)=2I_1(h)\), because the two half-orbits have identical time weight. Combining (8)–(9) with (2) proves both asymptotics in (5).

**Separatrix end and its constants.** Factor the *exact* difference from the saddle energy:
\[
\frac43-V(u)=\frac{(u+1)(2-u)^2}{3}.\tag{10}
\]
Put \(\delta=4/3-h\) and \(s=2-u\). The inner turning point satisfies \(s_b=2-b(h)=\sqrt\delta+O(\delta)\), and near it
\[
h-V(2-s)=s^2-\frac{s^3}{3}-\delta.
\]
Because \(1/2<\alpha<1\), a standard split into \(s\in[s_b,\varepsilon]\) and \(s\in[\varepsilon,2-a(h)]\), followed by \(s=\sqrt\delta\,t\) in the first integral, yields
\[
\lim_{\delta\downarrow0}\delta^{\beta}I_0(h)
=\int_1^\infty(t^2-1)^{-\alpha}dt
=\frac12\mathrm B\left(\frac1p,\beta\right).\tag{11}
\]
To justify the limit rigorously, on each fixed \(1+\eta\le t\le R\) the scaled integrand converges uniformly, while the segment adjacent to the moving simple root is bounded by an integrable \((t-t_b)^{-\alpha}\) majorant, and the tail by a multiple of \(t^{-2\alpha}\). The complementary region away from the saddle contributes \(O(1)\) to \(I_0\), negligible after multiplying by \(\delta^\beta\). Equation (11) proves (6).

To obtain the drift correction without subtracting divergent quantities, set
\[
J(h)=\int_{a(h)}^{b(h)}(2-u)(h-V(u))^{-\alpha}\,du.
\]
The factor \(2-u\) suppresses the saddle singularity, and endpoint splitting or the fixed-interval factorization shows \(J(h)\to J_*\). From (10), substituting \(r=(u+1)/3\) gives
\[
J_*=\int_{-1}^2(2-u)\left(\frac43-V(u)\right)^{-\alpha}du
=3^{2/p}\mathrm B\left(\frac1p,\frac2p\right).\tag{12}
\]
For example, at the saddle the right-end integrand behaves as \((2-u)^{1-2\alpha}\), which is integrable precisely because \(\alpha<1\); the left-end integrand behaves as \((u+1)^{-\alpha}\), also integrable. Since \(d_p(h)=1-J(h)/I_0(h)\), equations (11)–(12) prove (7).

**Existence, finiteness and location of the periodic cylinders.** The Poincaré return section \(\{u=0,\ v=(ph)^{1/p}>0\}\) is transverse for \(h\in(0,4/3)\), so the physical-time return period and return translation, hence \(d_p\), are real analytic in \(h\). Formula (5) shows \(d_p(h)<0\) near \(0\); formula (7) shows \(d_p(h)>0\) near \(4/3\). The intermediate-value theorem makes \(\mathcal Z_p\) nonempty. For \(h\le2/3\), the right turning point \(b(h)\le1\), so \(u-1<0\) for almost all time on the cycle and \(d_p(h)<0\). Thus all zeros lie in \((2/3,4/3)\). The endpoint signs confine zeros to a compact subinterval of \((0,4/3)\); zeros of a nonzero real-analytic function are isolated, and a compact set cannot contain infinitely many isolated zeros without an accumulation point. Therefore \(\mathcal Z_p\) is finite. Since (5) and (6) both diverge, continuity of \(T_p\) gives an interior global minimum.

## Verification

The attached `verify.py`, whose dependencies are listed in `requirements.txt`, checks the exact polynomial first-integral and saddle-factorization identities symbolically for three even exponents. Independently implemented endpoint-weighted quadrature verifies the exact identity \(I_2=2I_1\), the signs of the drift, the displayed asymptotic coefficients at sample energies, and a numerical return of an orbit on a zero-drift cylinder for \(p=4\). From the extracted package directory, run `python verify.py`; successful replay prints `CHECK_OK`. Such finite checks corroborate but do not replace the uniform integral estimates, analyticity argument or existence proof.

## Relationship to prior work

Castañeda and Rebollo-Perdomo's 2022 preprint (and subsequent 2024 journal article) analyzes a family of nilpotent polynomial vector fields, including the physical-time system \(\dot x=u-1\), \(\dot u=v\), \(\dot v=u(u-2)\). Its Proposition 1.3 establishes one isochronous periodic cylinder for that **quadratic-kinetic** case. The present higher **even-kinetic** systems are deliberately different polynomial skew flows and need not be nilpotent; neither the higher-power cylinder criterion nor their two-end algebraic period and drift asymptotics is stated in that preprint. Fonda, Garrione and Sfecci (2026) develop a general separated-Hamiltonian period-map framework, but require a global center for their principal results; the present potential has a finite separatrix and the theorem also concerns the axial skew drift. General separated-variable period literature is discussed in Limitations.

## Limitations

No uniqueness or exact count of the zero-drift energy levels is proved, and no monotonicity of \(d_p\) or uniqueness of the period minimum is claimed. Numerical examples are not exhaustive root counts. The result does not classify global existence or escape rates on unbounded energy components; it does not assert perturbation stability or nilpotence. The general 2019 Villadelprat–Zhang paper on period functions of separable Hamiltonians could not be read in full, creating a genuine residual risk that related period asymptotics are implied by its general criteria. The present original-data comparison does not establish exhaustive priority. Independent audit has not been performed.

## References

1. Álvaro Castañeda and Salomón Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1, first submitted 2022-09-15, https://arxiv.org/pdf/2209.06986 (especially Section 4.1, normalized system (16) and Proposition 1.3). Journal version: *Archiv der Mathematik* 124 (2025), 415–434, DOI: 10.1007/s00013-024-02085-8.
2. Alessandro Fonda, Maurizio Garrione and Andrea Sfecci, *On the period map of planar Hamiltonian systems with separated variables*, *Annali di Matematica Pura ed Applicata*, published 2026-05-16, DOI: 10.1007/s10231-026-01709-w, https://link.springer.com/article/10.1007/s10231-026-01709-w.
3. Jordi Villadelprat and Xiang Zhang, *The Period Function of Hamiltonian Systems with Separable Variables*, *Journal of Dynamics and Differential Equations*, published 2019-05-18, DOI: 10.1007/s10884-019-09759-w, https://link.springer.com/article/10.1007/s10884-019-09759-w (abstract and bibliographic material accessed; full text not inspected).
