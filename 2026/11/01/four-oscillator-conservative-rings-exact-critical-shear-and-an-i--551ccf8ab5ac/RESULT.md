# Four-oscillator conservative rings: exact critical shear and an inverse-time period tail

## Finding

On a four-site periodic nearest-neighbor phase ring with mixed cosine and oriented sine interactions, the quotient by common-phase rotation is completely integrable. Exactly two alternate-bond-sum leaves have degenerate pure-shear dynamics. On either exceptional leaf, the primitive reduced-period distribution of Haar-uniform initial conditions has an explicit inverse-time tail and infinite mean, whereas on every other leaf the Haar-mean primitive reduced period is finite. The small-amplitude period in the regular neighboring leaves diverges with an explicit inverse-square-root coefficient.

**Theorem.** For every \(c,d>0\), consider four phases \(\theta_j\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\), indexed modulo \(4\), solving
\[
\dot\theta_j=c\bigl(\cos(\theta_{j+1}-\theta_j)+\cos(\theta_{j-1}-\theta_j)\bigr)
+d\bigl(\sin(\theta_{j+1}-\theta_j)-\sin(\theta_{j-1}-\theta_j)\bigr).
\]
Set \(y_j=\theta_{j+1}-\theta_j\) and define the conserved alternating-bond sum \(a=y_1+y_3\pmod {2\pi}\). On the leaf with a fixed representative \(0\le a<2\pi\), let
\[
y_1=a/2+u,\quad y_3=a/2-u,\quad y_2=-a/2+v,\quad y_4=-a/2-v\pmod {2\pi}.
\]
Then \(u,v\in\mathbb T\) evolve by the one-degree-of-freedom Hamiltonian system
\[
\dot u=A(a)\sin v,\qquad \dot v=B(a)\sin u,\quad
A(a)=2\bigl(c\sin(a/2)+d\cos(a/2)\bigr),\quad
B(a)=2\bigl(c\sin(a/2)-d\cos(a/2)\bigr),
\]
with first integral
\[
H_a(u,v)=B(a)\cos u-A(a)\cos v.
\]
Define
\[
a_-=2\arctan(d/c),\quad a_+=2\pi-2\arctan(d/c),\quad
\kappa=\frac{4cd}{\sqrt{c^2+d^2}},\quad P_{\min}=\frac{2\pi}{\kappa}.
\]
Exactly the leaves \(a=a_-\) and \(a=a_+\) contain two circles of equilibria each; all their other quotient trajectories are periodic. For initial \((u,v)\) selected according to normalized Haar measure on either leaf, the primitive reduced period \(P\) obeys
\[
\Pr(P>t)=\begin{cases}
1,&0\le t<P_{\min},\\[2pt]
\displaystyle\frac{2}{\pi}\arcsin\bigl(P_{\min}/t\bigr),&t\ge P_{\min}.
\end{cases}
\]
Consequently \(\Pr(P>t)\sim 2P_{\min}/(\pi t)\) and \(\mathbb E[P]=\infty\). Here, equilibria have Haar measure zero and are excluded from the random-period definition.

For every \(a\ne a_\pm\), the reduced Hamiltonian is Morse, with precisely two centers and two saddles. Its regular levels are finite disjoint unions of periodic circles; all non-periodic trajectories lie on the finitely many separatrices or equilibria, a Haar-null set. The primitive reduced period has finite expectation under normalized Haar measure on this leaf.

The period of infinitesimal oscillations near either center is exactly
\[
P_0(a)=\frac{2\pi}{\sqrt{|A(a)B(a)|}}
\]
and it satisfies the sharp law
\[
P_0(a)\sim\frac{\pi}{\sqrt{cd}}\,|a-a_\pm|^{-1/2}
\]
as \(a\to a_\pm\) from either side through nonexceptional leaves.

## Assumptions and scope

The phases are points of \(\mathbb T\), with identical intrinsic frequencies removed by common rotation, and \(c,d\) are strictly positive real constants. All periodicity and random-period statements concern **phase differences modulo common phase**, not the absolute phases, which may undergo overall drift. The conditional initial distribution on a leaf is uniform in its \((u,v)\) torus coordinates; it is not a distribution on all three independent phase differences. Exactly at the exceptional leaves, the equilibrium circles have measure zero. On nonexceptional leaves, the singular energy levels and stationary points have measure zero. The quantities \(a\) and \(a_\pm\) are taken modulo \(2\pi\), with the representatives displayed above.

## Proof

**1. Two first integrals and a reduced Hamiltonian.** Define \(F(s)=c\cos s+d\sin s\). The original equations have the equivalent form \(\dot\theta_j=F(y_j)+F(y_{j-1})\), giving exactly \(\dot y_j=F(y_{j+1})-F(y_{j-1})\). Thus \(\dot y_1=-\dot y_3\), \(\dot y_2=-\dot y_4\), and \(a=y_1+y_3=-y_2-y_4\pmod{2\pi}\) is conserved. Substitution of the stated torus coordinates into these equations yields
\[
\dot u=F(-a/2+v)-F(-a/2-v)=2\bigl(c\sin(a/2)+d\cos(a/2)\bigr)\sin v,
\]
\[
\dot v=F(a/2-u)-F(a/2+u)=2\bigl(c\sin(a/2)-d\cos(a/2)\bigr)\sin u.
\]
These are Hamilton's equations for \(H_a=B\cos u-A\cos v\) with standard area form \(du\wedge dv\). The level \(H_a\) and the alternate sum are independent first integrals on regular points of the three-dimensional phase-difference flow.

**2. Exactly two exceptional leaves.** For \(c,d>0\), solving \(B(a)=0\) in \([0,2\pi)\) gives only \(a=a_-\); solving \(A(a)=0\) gives only \(a=a_+\). At either root the nonvanishing coefficient equals \(\kappa\). At \(a_-\) the equations are \(\dot u=\kappa\sin v\), \(\dot v=0\); at \(a_+\), \(\dot u=0\), \(\dot v=\kappa\sin u\). For any frozen angle not equal to \(0\) or \(\pi\) modulo \(2\pi\), the moving angle traverses its circle with constant nonzero speed. Its primitive reduced period is exactly \(2\pi/(\kappa|\sin w|)\), where \(w\) denotes the frozen angle.

**3. Exact critical period tail.** The frozen angle \(w\) is uniform on \(\mathbb T\) under the specified Haar distribution. For \(0\le z\le1\), the normalized measure of \(\{|\sin w|<z\}\) is \(2\arcsin(z)/\pi\). Taking \(z=P_{\min}/t\) yields the displayed distribution. Since \(\arcsin x\sim x\) as \(x\downarrow0\), the tail has order \(t^{-1}\), and integrating the tail over \(t\ge0\) proves its mean diverges. These are distributional statements for *individual periodic orbits* on each exceptional leaf, rather than a distribution over parameter values.

**4. Nonexceptional foliation and integrability of period.** If \(AB\ne0\), all stationary points satisfy \(u,v\in\{0,\pi\}\). Their Hessians are diagonal with nonzero entries \(-B\cos u\) and \(A\cos v\), making \(H_a\) Morse. The Jacobian of the Hamiltonian flow has squared eigenvalue \(AB\cos u\cos v\), yielding two centers and two saddles. Every regular energy level is a compact one-dimensional submanifold of \(\mathbb T^2\), hence a finite union of circles with nonvanishing tangent Hamiltonian velocity; every such component supports a periodic orbit. The finite union of stationary and separatrix levels has zero Haar area.

For the mean-period claim, decompose regular energy values into finitely many intervals with fixed circular-level topology and label each circular component's period \(P_j(E)\). The coarea formula and \(|X_H|=|\nabla H|\) imply that its contribution to the uniform-area expectation is, up to the normalization \((2\pi)^{-2}\),
\[
\int P_j(E)^2\,dE.
\]
Near a nondegenerate center, \(P_j(E)\) is bounded. Near a nondegenerate saddle, smooth Morse coordinates reduce the energy locally to a nonzero multiple of a product of two local variables, and the time spent crossing the saddle neighborhood is bounded by \(C(1+|\log|E-E_s||)\). Therefore \(P_j(E)^2\) is locally integrable at every critical energy, including a level with two saddles. There are finitely many critical values and compact regular ranges, establishing \(\mathbb E[P]<\infty\) for every fixed nonexceptional leaf.

**5. Near-critical small-amplitude law.** The linearized reduced dynamics at each center has eigenvalues \(\pm i\sqrt{|AB|}\). An explicit product identity is
\[
A(a)B(a)=4\left(c^2\sin^2(a/2)-d^2\cos^2(a/2)\right).
\]
At the two exceptional roots its derivative in \(a\) has absolute value \(4cd\), so \(|A(a)B(a)|=4cd|a-a_\pm|+O(|a-a_\pm|^2)\). Substituting into the center period proves the coefficient \(\pi/\sqrt{cd}\).

## Verification

The accompanying standalone `check.py` performs 2,000 direct comparisons between the original four-phase vector field and the two-dimensional reduction; 12 independently integrated four-phase trajectories checking both first integrals; critical coefficient and center-period scaling checks at three positive parameter pairs; and five midpoint quadrature checks of the exact Haar tail (using 300,000 angles each). The program reports PASS when run with `python check.py` using Python 3, NumPy, and SciPy. These finite checks are diagnostic and are not substitutes for the universal analytic proof.

## Relationship to prior work

Pikovsky (2026, equations 17–18) already gives the general conservative nearest-neighbor phase-difference evolution and cites earlier Hamiltonian lattice work. Ahnert and Pikovsky (2008, sections II–IV) analyze waves and compactons in this kind of lattice. Burylko, Mielke, Wolfrum, and Yanchuk (2018, sections 4–5 and 7) provide earlier analysis of skew-symmetric phase-ring coupling and explicitly identify first integrals and periodic foliations for a four-oscillator special case. None of these structural or integrability observations is claimed as new. The result established here is the exact two-parameter location of the exceptional *mixed-coupling* four-site leaves, their primitive-period distribution and infinite mean, the finite-mean contrast on every nonexceptional leaf, and the sharp transverse small-amplitude divergence.

## Limitations

All claims are for a four-site ring with the stated oriented interaction and strictly positive \(c,d\). The long-period tail is conditional on a codimension-one invariant leaf, rather than a probability statement for generic initial conditions in the entire phase space. Periodicity is only modulo overall phase. The theorem does not address unequal frequencies, other ring sizes, perturbations away from conservation, higher-harmonic interactions, or statistical behavior of all phase-space orbits. Historical priority of the exact period distribution remains provisional against unindexed specialized studies; an independent external audit has not been performed.

## References

1. A. Pikovsky, *Conservative dynamics in phase oscillator networks*, arXiv:2603.25431v1 (first publicly available 2026-03-26), https://arxiv.org/abs/2603.25431.
2. K. Ahnert and A. Pikovsky, *Traveling waves and Compactons in Phase Oscillator Lattices*, arXiv:0806.1833 (2008), https://arxiv.org/abs/0806.1833.
3. O. Burylko, A. Mielke, M. Wolfrum, and S. Yanchuk, *Coexistence of Hamiltonian-Like and Dissipative Dynamics in Rings of Coupled Phase Oscillators with Skew-Symmetric Coupling*, SIAM Journal on Applied Dynamical Systems 17 (2018), 2076–2105, DOI:10.1137/17M1155685. Lawful author preprint: https://www.wias-berlin.de/people/mielke/preprints/wias_preprints_2447.pdf.
