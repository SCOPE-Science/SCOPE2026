# Exact compact-recurrence threshold and invariant-measure laws for the Rössler system

## Result

Consider the classical Rössler system
\[
\dot x=-y-z,\qquad
\dot y=x+ay,\qquad
\dot z=b+z(x-c),
\tag{1}
\]
with \(a,b,c>0\). Let \(\mu\) be any compactly supported invariant probability measure and put
\[
m=\int z\,d\mu.
\]
Then
\[
\boxed{\int y\,d\mu=-m,\qquad \int x\,d\mu=am,\qquad cm=b+a\int y^2\,d\mu.}
\tag{2}
\]
Consequently every such measure forces
\[
\boxed{c^2\ge 4ab.}
\tag{3}
\]
When \(c^2\ge4ab\), define
\[
z_\pm=\frac{c\pm\sqrt{c^2-4ab}}{2a}.
\tag{4}
\]
The mean height and transverse variance obey the exact law
\[
\boxed{m\in[z_-,z_+],\qquad
\operatorname{Var}_\mu(y)=(m-z_-)(z_+-m).}
\tag{5}
\]
There are also exact covariance identities
\[
\boxed{
\operatorname{Cov}_\mu(x,z)=a\operatorname{Var}_\mu(y),\qquad
\operatorname{Cov}_\mu(x,y)=-a\operatorname{Var}_\mu(y).
}
\tag{6}
\]

The invariant measure is concentrated on \(z>0\), and \(1/z\) is integrable. Hence one additionally has
\[
\boxed{b\int\frac1z\,d\mu=c-am,}
\tag{7}
\]
and therefore the arithmetic-harmonic defect of the height is exactly
\[
\boxed{
 m\int\frac1z\,d\mu-1=\frac{a}{b}\operatorname{Var}_\mu(y).
}
\tag{8}
\]
Thus the ordinary and harmonic means of \(z\) coincide exactly when the invariant measure is supported on a single equilibrium.

## Global consequence: equilibrium threshold equals compact-recurrence threshold

The Rössler equilibria are
\[
p_\pm=(az_\pm,-z_\pm,z_\pm),
\tag{9}
\]
when \(c^2\ge4ab\), and no equilibrium exists when \(c^2<4ab\). Equations (2)--(5) upgrade this local algebraic discriminant into a global recurrence criterion:
\[
\boxed{
\text{a nonempty compact invariant set exists}
\iff c^2\ge4ab.
}
\tag{10}
\]
Indeed, every nonempty compact invariant set supports an invariant probability measure, so (3) is necessary; conversely an equilibrium supplies a compact invariant set when the discriminant is nonnegative.

In particular, if
\[
\boxed{c^2<4ab,}
\tag{11}
\]
then the classical positive-parameter Rössler flow has no periodic orbit, invariant torus, compact chaotic set, compact attractor, bounded complete orbit, or bounded forward orbit. For the last statement, any bounded forward solution is global and has a nonempty compact invariant omega-limit set, contradicting (10).

At the saddle-node boundary \(c^2=4ab\), write
\[
z_*=\frac{c}{2a}=\sqrt{\frac ba},\qquad
p_*=(az_*,-z_*,z_*).
\tag{12}
\]
Then (5) forces \(\operatorname{Var}_\mu(y)=0\), and invariance forces
\[
\boxed{\mu=\delta_{p_*}.}
\tag{13}
\]
Thus \(\delta_{p_*}\) is the unique compactly supported invariant probability measure at the threshold. Every bounded forward trajectory at the threshold is statistically attracted to \(p_*\): for every continuous observable \(\varphi\),
\[
\lim_{T\to\infty}\frac1T\int_0^T\varphi(x(t),y(t),z(t))\,dt=\varphi(p_*).
\tag{14}
\]
This is a time-average conclusion; pointwise convergence of every bounded trajectory is not asserted.

For \(c^2>4ab\), equality at either endpoint of (5) occurs only for the corresponding equilibrium measure \(\delta_{p_-}\) or \(\delta_{p_+}\). In particular every other compact invariant probability measure has
\[
z_-<m<z_+,
\tag{15}
\]
and
\[
0<\operatorname{Var}_\mu(y)\le\frac{c^2-4ab}{4a^2}.
\tag{16}
\]
The upper bound shows that all invariant-measure fluctuations in \(y\) must collapse as the saddle-node discriminant closes.

## Proof

For a compactly supported invariant probability measure, the average Lie derivative of every polynomial is zero. Applying this to \(x\) and \(y\) gives
\[
0=-\int y\,d\mu-\int z\,d\mu,
\qquad
0=\int x\,d\mu+a\int y\,d\mu,
\]
which are the first two relations in (2).

Now set
\[
E=\frac{x^2+y^2}{2}+z.
\]
Direct differentiation along (1) gives the exact balance
\[
\boxed{\dot E=ay^2+b-cz.}
\tag{17}
\]
Averaging (17) proves the last relation in (2). Since \(\int y\,d\mu=-m\),
\[
a\operatorname{Var}_\mu(y)
=cm-am^2-b.
\tag{18}
\]
The right side is a concave quadratic in \(m\). Nonnegativity of variance gives (3), and factoring the quadratic using the two roots (4) gives (5).

Two further polynomial balances are
\[
\frac12\frac d{dt}(x^2+y^2)=ay^2-xz,
\qquad
\frac12\frac d{dt}y^2=xy+ay^2.
\tag{19}
\]
Hence
\[
\int xz\,d\mu=a\int y^2\,d\mu,
\qquad
\int xy\,d\mu=-a\int y^2\,d\mu.
\tag{20}
\]
Subtracting products of the means from (2) yields (6).

To prove the positivity statement needed for (7), decompose \(\mu\) into ergodic components. Almost every point of an ergodic component is both recurrent and Birkhoff generic. Since \(\dot z=b>0\) whenever \(z=0\), a trajectory can cross the plane \(z=0\) only from negative to positive. A recurrent generic point with \(z<0\) therefore cannot cross that plane; its long-time average of \(z\) would be nonpositive, contradicting the strictly positive value forced by
\[
c\int z\,d\mu=b+a\int y^2\,d\mu.
\]
The plane \(z=0\) itself has zero invariant measure because any trajectory meets it at most once, so distinct time-translates of this crossing section are disjoint and have equal invariant measure. Thus \(z>0\) almost everywhere for every compactly supported invariant probability measure.

For \(\varepsilon>0\), apply invariance to \(\log(z+\varepsilon)\) on a neighborhood of the compact support. This gives
\[
0=
 b\int\frac{1}{z+\varepsilon}\,d\mu
 +\int (x-c)\frac{z}{z+\varepsilon}\,d\mu.
\tag{21}
\]
Letting \(\varepsilon\downarrow0\), dominated convergence handles the second term and monotone convergence handles the first. Using \(\int x\,d\mu=am\) gives (7). Combining (7) with (18) gives (8).

For the endpoint statement, equality in (5) gives zero variance, hence \(y\) is constant almost everywhere. Invariance makes its value constant along almost every complete trajectory, so \(\dot y=0\) there and therefore \(x=am\). Then \(\dot x=0\) forces \(z=m\). The invariant measure is consequently the Dirac mass at the corresponding equilibrium. At \(c^2=4ab\) the two endpoints coincide, proving (13).

Finally, if a bounded forward orbit exists at the threshold, every weak limit of its empirical measures is a compactly supported invariant probability measure. Since (13) is the only possibility, all empirical measures converge weakly to \(\delta_{p_*}\), which is exactly (14).

## Relation to prior literature

Rössler introduced (1) as a minimal continuous-time chaotic prototype with one quadratic nonlinearity [1]. The equilibrium discriminant \(c^2-4ab\) is standard and is used throughout the later bifurcation literature; it is not claimed as new.

The closest older result located is Starkov and Starkov (2007) [2], devoted specifically to localization of compact invariant sets and periodic orbits of the Rössler system. Its accessible abstract states two relevant facts: algebraic conditions excluding compact invariant sets in specified half-spaces, and the theorem that absence of equilibria implies absence of periodic orbits. The present result strengthens that abstract-level nonexistence statement from periodic orbits to every nonempty compact invariant set and every bounded forward orbit, and adds the exact invariant-measure laws (5)--(8). The full 2007 article was not accessible for theorem-by-theorem comparison, so it remains the principal prior-coverage risk.

Cândido, Novaes and Valls (2020) [3] prove local periodic-orbit and invariant-torus bifurcations near zero-Hopf families. Fowler and McGuinness (2023) [4] give an asymptotic analysis for large \(c\), including pulse dynamics and an approximate Poincaré map. Igra's recent rigorous work [5] proves chaos and infinitely many periodic trajectories under heteroclinic hypotheses in parameter regimes with equilibria. These works address existence and local/topological dynamics rather than a parameter-uniform compact-recurrence obstruction.

Bramburger and Fantuzzi (2024) [6] are especially relevant because they study invariant measures of the Rössler attractor directly. Their Rössler section uses data to approximate one physical measure and unstable periodic-orbit measures; it reports approximate moments through degree two. Their general framework uses the standard invariance relation \(\int Lg\,d\mu=0\), but the inspected Rössler section does not state the closed parameter-uniform mean/variance/covariance identities (2), (5), (6), the harmonic law (7)--(8), or the compact-recurrence threshold (10).

A September 2026 preprint by Llibre and Szumiński [7] studies zero-Hopf bifurcation, three families of periodic orbits, and local \(C^1\) non-integrability. Its accessible statement does not cover the global invariant-measure constraints above.

To the best of our knowledge, equations (5)--(8), the equivalence (10), the no-bounded-forward-orbit consequence below the equilibrium discriminant, and the unique invariant-measure statement at equality have not previously been stated for the classical positive-parameter Rössler system.

## Limitations

- The result assumes \(a,b,c>0\). Other sign choices are not covered.
- At \(c^2=4ab\), uniqueness of the compactly supported invariant probability measure implies statistical convergence of bounded trajectories, not necessarily pointwise convergence; compact invariant sets containing nonrecurrent connecting orbits are not excluded by (13).
- The 2007 Starkov--Starkov paper is the strongest residual originality risk because only its abstract and bibliographic record were accessible; inaccessible full text is not treated as evidence of non-coverage.
- The theorem does not classify which invariant measures or attractors occur when \(c^2>4ab\); it only gives exact constraints on all compactly supported invariant measures.
- Originality is asserted only to the best of our knowledge.

## Reproducibility

`artifacts/verify_identities.py` uses symbolic algebra to check the polynomial balance laws, the variance-gap factorization, and the arithmetic-harmonic defect identity. `artifacts/verification.txt` records zero residuals.

## References

1. O. E. Rössler, *An equation for continuous chaos*, Physics Letters A **57** (1976), 397--398. https://doi.org/10.1016/0375-9601(76)90101-8
2. K. E. Starkov and K. K. Starkov, *Localization of periodic orbits of the Rössler system under variation of its parameters*, Chaos, Solitons & Fractals **33** (2007), 1445--1449. https://doi.org/10.1016/j.chaos.2006.02.011
3. M. R. Cândido, D. D. Novaes and C. Valls, *Periodic solutions and invariant torus in the Rössler system*, Nonlinearity **33** (2020), 4512--4539. https://doi.org/10.1088/1361-6544/ab8bae
4. A. C. Fowler and M. J. McGuinness, *Bursting solutions of the Rössler equations*, ANZIAM Journal **65** (2023), 93--110. https://doi.org/10.1017/S144618112300010X
5. E. Igra, *Knots and Chaos in the Rössler System*, Journal of Differential Equations (2025), article 113290. https://doi.org/10.1016/j.jde.2025.113290
6. J. J. Bramburger and G. Fantuzzi, *Data-driven discovery of invariant measures*, Proceedings of the Royal Society A **480** (2024), 20230627. https://doi.org/10.1098/rspa.2023.0627
7. J. Llibre and W. Szumiński, *Zero-Hopf bifurcation, periodic orbits and C1 non-integrability of the classical Rössler system*, arXiv:2609.17336 (2026). https://arxiv.org/abs/2609.17336
