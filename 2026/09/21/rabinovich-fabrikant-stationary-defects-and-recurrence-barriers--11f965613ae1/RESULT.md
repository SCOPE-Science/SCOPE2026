# Heightwise stationary balance and sharp recurrence barriers in the Rabinovich–Fabrikant flow

Consider the Rabinovich–Fabrikant system
\[
\dot x=y(z-1+x^2)+\gamma x,\qquad
\dot y=x(3z+1-x^2)+\gamma y,\qquad
\dot z=-2z(\alpha+xy),
\]
with \(\alpha,\gamma>0\). Put
\[
R=x^2+y^2,\qquad W=R+4z.
\]

## Result

The elementary Lie-derivative identities
\[
\dot R=2\gamma R+8xyz,
\qquad
\boxed{\dot W=2\gamma R-8\alpha z}
\tag{1}
\]
lead to exact constraints on every compactly supported invariant probability measure.

### Theorem 1: sign decomposition and heightwise stationary law

Let \(\mu\) be a compactly supported invariant Borel probability measure. Then \(\mu\) gives no mass to \(\{z<0\}\), and its restriction to \(\{z=0\}\) is supported only at the origin. Consequently
\[
\mu=p\,\delta_0+(1-p)\nu,
\qquad 0\le p\le1,
\tag{2}
\]
where, if \(p<1\), \(\nu\) is invariant and \(\nu\{z>0\}=1\).

For this positive component,
\[
\boxed{\mathbb E_\nu[xy\mid z]=-\alpha}
\qquad \nu\text{-a.s.}
\tag{3}
\]
Equivalently, for every bounded continuous \(\varphi\),
\[
\int \varphi(z)(\alpha+xy)\,d\nu=0.
\tag{4}
\]
Thus the balance \(\langle xy\rangle=-\alpha\) is not merely a global time-average identity: it holds conditionally at almost every occupied height.

### Theorem 2: exact square defects and sharp stationary floors

For the same \(\nu\),
\[
\boxed{\int R\,d\nu
=2\alpha+\int (x+y)^2\,d\nu}
\tag{5}
\]
and
\[
\boxed{\int z\,d\nu
=\frac{\gamma}{2}+\frac{\gamma}{4\alpha}
\int (x+y)^2\,d\nu.}
\tag{6}
\]
In particular,
\[
\boxed{\int R\,d\nu\ge2\alpha,\qquad
\int z\,d\nu\ge\frac\gamma2.}
\tag{7}
\]
There is also a heightwise radial-energy refinement:
\[
\boxed{\mathbb E_\nu[R\mid z]
=2\alpha+\mathbb E_\nu[(x+y)^2\mid z]
\ge2\alpha}
\qquad \nu\text{-a.s.}
\tag{8}
\]

A second exact representation of the height defect is
\[
\boxed{
\int z\,d\nu-\frac\gamma2
=\int z\frac{(x+y)^2}{x^2+y^2}\,d\nu
=\frac{\gamma}{4\alpha}\int(x+y)^2\,d\nu,}
\tag{9}
\]
where the ratio can be defined arbitrarily on \(R=0\), a \(\nu\)-null set.

### Theorem 3: equality rigidity

Equality in either inequality in (7) occurs exactly in the following case:
\[
\boxed{\alpha=1+\frac\gamma2}
\tag{10}
\]
and \(\nu\) is a convex combination of the two equilibria
\[
E_\pm=
\left(\pm\sqrt\alpha,\mp\sqrt\alpha,\frac\gamma2\right).
\tag{11}
\]
Hence, away from the codimension-one relation (10), every positive compact invariant probability has both inequalities in (7) strict. Even on (10), a non-equilibrium invariant measure has strict defect unless it is supported on \(E_+\) and \(E_-\).

### Corollary: universal barriers for nonconstant periodic orbits

Every nonconstant periodic orbit lies in \(z>0\) and satisfies
\[
\boxed{\langle xy\rangle=-\alpha,}
\tag{12}
\]
\[
\boxed{\langle x^2+y^2\rangle>2\alpha,
\qquad \langle z\rangle>\frac\gamma2,}
\tag{13}
\]
so necessarily
\[
\boxed{\max_t(x^2+y^2)>2\alpha,
\qquad \max_t z>\frac\gamma2.}
\tag{14}
\]
These barriers are parameter-exact and do not depend on the orbit's period.

Moreover, no non-origin recurrent point can lie in \(z\le0\): on \(z<0\), (1) gives \(\dot W>0\), while on \(z=0\) one has \(\dot R=2\gamma R\).

## Proof

The sign of \(z\) is invariant because
\[
z(t)=z(0)\exp\!\left[-2\int_0^t(\alpha+x(s)y(s))\,ds\right].
\tag{15}
\]
If an invariant probability gave positive mass to \(z<0\), normalize its restriction to that invariant half-space. Integrating \(\dot W\) against this normalized invariant measure would give zero by invariance, but (1) is strictly positive on \(z<0\), a contradiction. On the invariant plane \(z=0\), (1) for \(R\) reduces to \(\dot R=2\gamma R\); invariance therefore forces \(R=0\) almost surely, giving only \(\delta_0\). This proves (2).

Assume now \(\nu\{z>0\}=1\). For a bounded continuous \(\varphi\), choose smooth cutoffs \(\chi_\varepsilon\) that vanish near zero and converge pointwise to one on \((0,\infty)\), and choose a smooth scalar observable \(q_\varepsilon\) with
\[
q_\varepsilon'(z)=\frac{\varphi(z)\chi_\varepsilon(z)}{z}
\]
on the compact \(z\)-range of the support. Invariance gives
\[
0=\int Lq_\varepsilon\,d\nu
=-2\int\varphi(z)\chi_\varepsilon(z)(\alpha+xy)\,d\nu.
\]
Dominated convergence gives (4), hence (3). Since
\[
R+2xy=(x+y)^2,
\]
conditional expectation and (3) give (8), and integration gives (5).

Integrating the second identity in (1) gives
\[
\gamma\int R\,d\nu=4\alpha\int z\,d\nu.
\tag{16}
\]
Combining (16) with (5) yields (6) and (7).

To prove (9), first note that \(\nu\{R=0\}=0\). Indeed \(R=0\) is the invariant \(z\)-axis; an invariant probability on its positive part would satisfy \(0=\int \dot z\,d\nu=-2\alpha\int z\,d\nu\), impossible for \(z>0\). Apply the same cutoff argument to a smooth approximation of \(\log R\). Since
\[
L\log R=2\gamma+\frac{8xyz}{R}
\]
for \(R>0\), and \(|xy|/R\le1/2\), dominated convergence yields
\[
\int\frac{xyz}{R}\,d\nu=-\frac\gamma4.
\tag{17}
\]
Therefore
\[
\int z\frac{(x+y)^2}{R}\,d\nu
=\int z\,d\nu+2\int\frac{xyz}{R}\,d\nu
=\int z\,d\nu-\frac\gamma2,
\]
which together with (6) proves (9).

For equality rigidity, (5) shows that equality is equivalent to \(x+y=0\) almost surely. On a full-measure invariant set of such trajectories, write \(y=-x\). Non-axis points then satisfy
\[
0=\frac d{dt}(x+y)=2x(z+1-x^2),
\]
so \(z=x^2-1\). Let \(q=x^2\). Consistency of the two equations for \(z'=q'\) forces
\[
3q^2-(\alpha+\gamma+3)q+\alpha=0.
\tag{18}
\]
Thus the continuous function \(q(t)\) takes values in a finite set and is constant. Since \(x\ne0\), the \(x\)-equation gives \(q=1+\gamma/2\), and the \(z\)-equation then gives \(q=\alpha\). Hence (10) holds and the orbit is one of (11). Conversely, (11) are equilibria when (10) holds, and every convex combination of their Dirac measures attains equality.

A nonconstant periodic orbit carries its normalized occupation measure. It cannot lie in \(z<0\) because \(W\) is then strictly increasing, and it cannot lie nontrivially in \(z=0\) because \(R\) grows exponentially. Hence it lies in \(z>0\), and Theorems 1–3 apply. Equality would force its occupation measure to be supported on equilibria, impossible for a nonconstant periodic orbit, proving (12)–(14).

## Literature context and originality boundary

Rabinovich and Fabrikant's original 1979 paper derives the system from a three-mode wave interaction, records the conservative energy integral \(x^2+y^2+4z\), identifies \(z=0\) as an invariant plane, and studies periodic and complex regimes largely through qualitative and numerical analysis. V. V. Tsegel'nik later proved the related nonautonomous first integral \(x^2+y^2+4z=C e^{2at}\) for the special parameter relation \(a=-b\) in the common \((a,b)\) notation. Thus neither the conservative energy nor that special first-integral identity is claimed here as new.

Subsequent Rabinovich–Fabrikant literature has concentrated heavily on numerical bifurcation structure, hidden and transient attractors, generalized models, and parameter-space/statistical diagnostics. In particular, work from 2016, 2019, 2022 and 2026 explicitly emphasizes numerical integration, numerical bifurcation analysis, or ensemble statistical mapping.

To the best of our knowledge, targeted searches did not locate the conditional invariant-measure law (3), the paired exact defects (5), (6), and (9), the equality classification (10)–(11), or the resulting universal periodic-orbit barriers (14). The closest analytical predecessor found is Tsegel'nik's special first-integral theorem, which is explicitly separated above. The main residual priority risk is that an equivalent stationary identity may be implicit in older Russian-language or model-specific literature not indexed under invariant-measure terminology.

## Limitations

The measure statements require compact support. They do not assert existence or uniqueness of an attractor or invariant probability for arbitrary parameters. The conditional law is a stationary statement and should not be read as a pointwise identity along trajectories. The periodic-orbit conclusions are necessary constraints, not existence criteria. No claim is made about numerical parameter boundaries for chaos or about the complete classification of unbounded solutions.

## Reproducibility

The polynomial Lie-derivative and equality-manifold calculations can be checked with `artifacts/verify_identities.py` using SymPy 1.14.0. The proof of the invariant-measure statements is analytic and does not depend on numerical simulation.

## References

1. M. I. Rabinovich and A. L. Fabrikant, “Stochastic self-modulation of waves in nonequilibrium media,” *Sov. Phys. JETP* 50(2) (1979), 311–317. https://www.jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf
2. V. V. Tsegel'nik, “Analytical properties of solutions of three-dimensional nonlinear dynamical system,” in *Anosov Systems and Modern Dynamics: Abstracts* (2016), pp. 129–131. https://www.mathnet.ru/ConfLogos/812/Abstr_book.pdf
3. M.-F. Danca, M. Fečkan, N. V. Kuznetsov, and G. Chen, “Looking More Closely at the Rabinovich–Fabrikant System,” *Int. J. Bifurcation and Chaos* 26 (2016), 1650038. https://doi.org/10.1142/S0218127416500383
4. M.-F. Danca, N. Kuznetsov, and G. Chen, “Unusual dynamics and hidden attractors of the Rabinovich–Fabrikant system,” *Nonlinear Dynamics* 88 (2017), 791–805. https://doi.org/10.1007/s11071-016-3276-1
5. A. P. Kuznetsov, S. P. Kuznetsov, and L. V. Turukina, “Complex dynamics and chaos in the Rabinovich–Fabrikant model,” *Izv. Saratov Univ. Physics* 19 (2019), 4–18. https://doi.org/10.18500/1817-3020-2019-19-1-4-18
6. S. P. Kuznetsov and L. V. Turukina, “Generalized Rabinovich–Fabrikant system: equations and its dynamics,” *Izvestiya VUZ. Applied Nonlinear Dynamics* 30 (2022), 7–29. https://doi.org/10.18500/0869-6632-2022-30-1-7-29
7. H. Sajjad, A. Jhangeer, M. Imran, and A. R. Ansari, “Robust dynamical behavior identification in the Rabinovich Fabrikant system using statistical measures,” *AIMS Mathematics* 11 (2026), 10716–10743. https://doi.org/10.3934/math.2026441
