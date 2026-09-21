# Universal amplitude barrier and strict period floor for Moore-Spiegel recurrence

## Result

Consider the classical Moore-Spiegel oscillator
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-z-(T-R+Rx^2)y-Tx,
\qquad R,T>0.
\tag{1}
\]

### 1. Exact stationary balances

Let \(\mu\) be any compactly supported invariant Borel probability measure of (1), and write \(\langle q\rangle=\int q\,d\mu\). Then
\[
\langle x\rangle=\langle y\rangle=\langle z\rangle
=\langle xy\rangle=\langle yz\rangle=0,
\tag{2}
\]
\[
\boxed{\langle y^2\rangle=T\langle x^2\rangle},
\tag{3}
\]
and
\[
\langle z^2\rangle=(T-R)\langle y^2\rangle
+R\langle x^2y^2\rangle.
\tag{4}
\]
Combining these relations gives the exact nonnegative defect identity
\[
\boxed{
R\langle (x^2-1)y^2\rangle
=\langle (z+Tx)^2\rangle.
}
\tag{5}
\]
Moreover, equality in (5) occurs only for the equilibrium measure \(\delta_0\). Hence every non-equilibrium compact invariant statistical state satisfies
\[
\boxed{\langle (x^2-1)y^2\rangle>0},
\tag{6}
\]
so it assigns positive measure to points with \(|x|>1\) and \(y\ne0\). It also obeys the strict acceleration-energy gap
\[
\boxed{\langle z^2\rangle>T\langle y^2\rangle=T^2\langle x^2\rangle.}
\tag{7}
\]

### 2. A compact-invariant slab obstruction

Define
\[
H(x)=\frac{T-R}{2}x^2+\frac{R}{4}x^4
\]
and
\[
W(x,y,z)=-yz-Txy+Txz+T H(x)
-\frac{T}{2}x^2-\frac{T+1}{2}y^2.
\tag{8}
\]
A direct differentiation along (1) gives
\[
\boxed{
\dot W=R(x^2-1)y^2-(z+Tx)^2.
}
\tag{9}
\]
Therefore the origin is the only compact invariant set contained in the closed slab
\[
\boxed{|x|\le1.}
\tag{10}
\]
Equivalently, every nontrivial compact invariant set of the Moore-Spiegel flow must cross the parameter-independent displacement threshold \(|x|=1\).

### 3. Periodic-orbit consequences

Let \(x(t)\) be a nonconstant periodic solution of least period \(P\). Its orbit measure specializes (2)--(5) to
\[
\int_0^P x(t)\,dt=0,
\qquad
\boxed{\int_0^P \dot x(t)^2\,dt
=T\int_0^P x(t)^2\,dt},
\tag{11}
\]
and
\[
\boxed{
R\int_0^P (x(t)^2-1)\dot x(t)^2\,dt
=\int_0^P(\ddot x(t)+Tx(t))^2\,dt>0.
}
\tag{12}
\]
Consequently every nonconstant periodic orbit satisfies the universal amplitude barrier
\[
\boxed{\max_t |x(t)|>1}
\tag{13}
\]
and the strict period floor
\[
\boxed{P>\frac{2\pi}{\sqrt T}.}
\tag{14}
\]
The amplitude threshold is independent of both \(R\) and \(T\); the period floor depends only on the linear restoring parameter \(T\).

## Proof

For an invariant measure, \(\int L\phi\,d\mu=0\) for every smooth observable used below, where \(L\) is the generator of (1). The identities \(Lx=y\) and \(Ly=z\) give \(\langle y\rangle=\langle z\rangle=0\). Put
\[
F(x)=(T-R)x+\frac R3x^3.
\]
Since \(LF=(T-R+Rx^2)y\), integration of the \(z\)-equation gives \(T\langle x\rangle=0\), hence \(\langle x\rangle=0\).

Next, \(L(x^2/2)=xy\) and \(L(y^2/2)=yz\), so \(\langle xy\rangle=\langle yz\rangle=0\). Also
\[
L(xy)=y^2+xz,
\]
which yields \(\langle xz\rangle=-\langle y^2\rangle\). Because \(H'(x)=x(T-R+Rx^2)\),
\[
L(xz+H)=yz-xz-Tx^2.
\]
After averaging and using \(\langle yz\rangle=0\), this gives \(\langle xz\rangle=-T\langle x^2\rangle\), proving (3). Finally,
\[
L(yz)=z^2-yz-(T-R+Rx^2)y^2-Txy,
\]
which proves (4). Using \(\langle xz\rangle=-\langle y^2\rangle\) and (3),
\[
\langle(z+Tx)^2\rangle
=\langle z^2\rangle-T\langle y^2\rangle
=R\langle(x^2-1)y^2\rangle,
\]
so (5) follows.

If the right side of (5) vanishes, continuity implies that the support of \(\mu\) lies in \(z+Tx=0\). Along such a complete orbit,
\[
\frac d{dt}(z+Tx)=-(z+Tx)+R(1-x^2)y.
\]
Thus invariance of the support forces \((1-x^2)y=0\). If \(y\) were nonzero at some time, it would remain nonzero on a short interval, forcing \(x^2=1\) throughout that interval, contradicting \(\dot x=y\ne0\). Hence \(y\equiv0\), then \(z\equiv0\), and \(z+Tx=0\) gives \(x\equiv0\). Therefore equality occurs only for \(\delta_0\), proving (6) and (7).

Differentiating (8) gives (9). Inside \(|x|\le1\), the right side of (9) is nonpositive. Its zero set has \(z+Tx=0\) and \((1-x^2)y=0\), whose largest invariant subset is the origin by the preceding argument. If a compact invariant set \(K\) were contained in the slab, every orbit in \(K\) would be complete and \(W(t)\) would be nonincreasing and bounded for all \(t\in\mathbb R\). Hence it has limits \(W_-\) and \(W_+\) as \(t\to-\infty\) and \(t\to+\infty\). The corresponding alpha- and omega-limit sets are nonempty compact invariant subsets on which \(W\) is constant, so they lie in \(\dot W=0\). The largest invariant subset of that zero set is the origin; therefore both limit sets equal \(\{0\}\), and \(W_-=W_+=W(0)=0\). Monotonicity then forces \(W(t)\equiv0\) along the whole orbit, so the orbit itself lies in the largest invariant zero-dissipation set and is the origin. Thus \(K=\{0\}\), proving (10).

For a periodic orbit, (11) follows from the invariant-measure identities. Since \(x\) has zero mean, Wirtinger's inequality gives
\[
\int_0^P\dot x^2\,dt\ge\left(\frac{2\pi}{P}\right)^2
\int_0^P x^2\,dt.
\]
Together with (11), this yields \(P\ge2\pi/\sqrt T\). Equality in Wirtinger's inequality would force \(x\) to be a single sinusoid with angular frequency \(\sqrt T\). Substitution into
\[
x'''+x''+(T-R+Rx^2)x'+Tx=0
\]
then reduces the equation to \(R(x^2-1)x'=0\), impossible for a nonconstant sinusoid when \(R>0\). Thus (14) is strict. Equation (12), and hence (13), follows from (5) and the equality classification.

## Relation to prior work and originality check

Moore and Spiegel introduced the thermo-mechanical oscillator in 1966 and numerically identified periodic and aperiodic regimes. Balmforth and Craster (1997) studied the same equations in detail, including symmetry breaking, period doubling, homoclinic behavior, periodic-orbit expansions, and extensive numerical period tables. Their full text was inspected; targeted searches of the accessible text did not locate the stationary defect identity (5), the compact slab obstruction (10), or the strict period bound (14).

Later work on generalized Moore-Spiegel equations has focused mainly on attractor topology, symmetry, multistability, bifurcation diagrams, Lyapunov spectra, hidden attractors, and topological classifications of periodic trajectories. In particular, Letellier and Malasoma (2014) study topology under changes of the nonlinear term; Negou, Kengne and Tchiotsop (2018) study periodicity, chaos and coexisting attractors; Azam et al. (2023) study hidden and multiscroll attractors; and Igra (2024) proves topological reduction results and a torus-knot classification for periodic trajectories.

To the best of our knowledge, the combination of the exact invariant-measure defect (5), its equality rigidity, the parameter-independent compact-invariant barrier \(|x|>1\), and the strict period floor (14) has not been stated previously. The 1966 primary paper could not be inspected at theorem-level full text, and the full texts of the 2014, 2018, 2023, and 2024 works were not all inspectable. They are therefore explicit residual priority risks rather than evidence of non-coverage.

## Verification

`artifacts/verify_identities.py` symbolically checks the generator identities and the polynomial Lyapunov identity (9). The proof itself is analytic; the symbolic computation is a consistency check, not a substitute for it.

## Scientific limitations

The invariant-measure statements assume compact support. The compact-set obstruction concerns compact invariant sets, not arbitrary bounded forward trajectories; a forward trajectory on a stable manifold can have different one-sided behavior. The result gives necessary constraints on recurrent dynamics and periodic orbits but does not prove that such objects exist for a given \((R,T)\), nor does it determine their stability or uniqueness.

## References

1. D. W. Moore and E. A. Spiegel, *A thermally excited nonlinear oscillator*, Astrophys. J. **143** (1966), 871--887. https://doi.org/10.1086/148562
2. N. J. Balmforth and R. V. Craster, *Synchronizing Moore and Spiegel*, Chaos **7** (1997), 738--752. https://doi.org/10.1063/1.166271
3. C. Letellier and J.-M. Malasoma, *Universalities in the chaotic generalized Moore & Spiegel equations*, Chaos Solitons Fractals **69** (2014), 40--49. https://doi.org/10.1016/j.chaos.2014.09.002
4. A. N. Negou, J. Kengne and D. Tchiotsop, *Periodicity, chaos and multiple coexisting attractors in a generalized Moore-Spiegel system*, Chaos Solitons Fractals **107** (2018), 275--289. https://doi.org/10.1016/j.chaos.2018.01.011
5. A. Azam, R. Naheed, M. Aqeel, S. Ahmad, J. Ayub and S. Khan, *Archive of novel hidden attractor with multistability and multidirectional chaotic attractors of Moore-Spiegel oscillator*, Eur. Phys. J. Plus **138** (2023), 938. https://doi.org/10.1140/epjp/s13360-023-04577-y
6. E. Igra, *Removable dynamics in the Nose-Hoover and Moore-Spiegel Oscillators* (2024), arXiv:2409.16624. https://arxiv.org/abs/2409.16624
