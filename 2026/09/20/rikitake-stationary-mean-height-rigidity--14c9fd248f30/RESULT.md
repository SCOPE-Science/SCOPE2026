# Rikitake stationary mean-height floor and sharp equality rigidity

## Result

Consider the classical Rikitake two-disc dynamo
\[
\dot x=-\mu x+yz,\qquad
\dot y=-\mu y+x(z-a),\qquad
\dot z=1-xy,
\tag{1}
\]
with \(\mu>0\) and \(a\ge 0\).  Let \(\nu\) be a compactly supported invariant Borel probability measure for (1), and write
\[
U=\int x^2\,d\nu,\qquad V=\int y^2\,d\nu,\qquad m=\int z\,d\nu.
\]
Define
\[
\Delta=\sqrt{a^2+4\mu^2},\qquad
z_+=\frac{a+\Delta}{2},\qquad
z_- =\frac{a-\Delta}{2},\qquad
r=\frac{\mu}{z_+}.
\]
Then every such invariant measure satisfies the exact stationary identities
\[
\boxed{\int xy\,d\nu=1},\qquad
\boxed{\mu(U-V)=a},\qquad
\boxed{m=\mu U=a+\mu V}.
\tag{2}
\]
Consequently
\[
\boxed{UV-1=\frac{(m-z_+)(m-z_-)}{\mu^2}}
\tag{3}
\]
and, more sharply,
\[
\boxed{
 m-z_+=\frac{\mu}{1+r^2}\int (y-rx)^2\,d\nu.
}
\tag{4}
\]
In particular,
\[
\boxed{m\ge z_+},\qquad
\boxed{U\ge \frac{z_+}{\mu}},\qquad
\boxed{V\ge \frac{\mu}{z_+}}.
\tag{5}
\]
The lower level \(z_+\) is exactly the \(z\)-coordinate of the two finite equilibria when \(a>0\):
\[
E_\pm=\left(\pm\sqrt{\frac{z_+}{\mu}},\ \pm\sqrt{\frac{\mu}{z_+}},\ z_+\right).
\tag{6}
\]

For the physical interior \(a>0\), equality is rigid:
\[
\boxed{m=z_+\quad\Longleftrightarrow\quad
\nu=p\delta_{E_+}+(1-p)\delta_{E_-}\ \text{for some }p\in[0,1].}
\tag{7}
\]
Thus, for \(a>0\), every compactly supported invariant measure that is not an equilibrium mixture has strict inequalities in all three parts of (5). In particular its support must meet each of
\[
\{z>z_+\},\qquad
\left\{|x|>\sqrt{z_+/\mu}\right\},\qquad
\left\{|y|>\sqrt{\mu/z_+}\right\}.
\tag{8}
\]
Every nonconstant periodic orbit therefore makes all three strict excursions (not necessarily at the same time).

The condition \(a>0\) in the rigidity statement is sharp. At the boundary \(a=0\), one has \(z_+=\mu\), \(r=1\), and (4) becomes
\[
 m-\mu=\frac{\mu}{2}\int (y-x)^2\,d\nu.
\tag{9}
\]
Hence equality holds exactly for compactly supported invariant measures supported on the invariant plane \(x=y\). Classical global analysis shows that this plane contains two families of periodic orbits when \(a=0,\mu>0\), so nonconstant recurrent states genuinely attain the floor there.

Finally, any bounded forward solution of (1) obeys the asymptotic time-average floor
\[
\boxed{
\liminf_{T\to\infty}\frac1T\int_0^T z(t)\,dt\ge z_+.
}
\tag{10}
\]
Indeed every weak limit of its empirical measures is compactly supported and invariant. Integrating the same four differential identities also gives the asymptotic defect formula
\[
\frac1T\int_0^T z\,dt-z_+
-\frac{\mu}{1+r^2}\frac1T\int_0^T (y-rx)^2\,dt\longrightarrow0.
\tag{11}
\]

## Proof

Invariance permits integration of Lie derivatives of polynomials over the compact support. Direct differentiation gives
\[
\frac{d}{dt}z=1-xy,
\tag{12}
\]
\[
\frac{d}{dt}\frac{x^2-y^2}{2}
=a xy-\mu(x^2-y^2),
\tag{13}
\]
\[
\frac{d}{dt}\frac{z^2}{2}=z-xyz,
\tag{14}
\]
and
\[
\frac{d}{dt}\frac{x^2+y^2}{2}
=-\mu(x^2+y^2)-a xy+2xyz.
\tag{15}
\]
Averaging (12)--(15) gives
\[
\int xy\,d\nu=1,\qquad
\mu(U-V)=a,\qquad
\int xyz\,d\nu=m,
\]
and then
\[
2m=\mu(U+V)+a.
\]
Combining the last two relations yields \(m=\mu U=a+\mu V\), proving (2).

Because \(z_\pm\) are the roots of \(z(z-a)=\mu^2\), substitution of
\[
U=\frac{m}{\mu},\qquad V=\frac{m-a}{\mu}
\]
gives (3). Cauchy--Schwarz and (2) imply \(UV\ge(\int xy\,d\nu)^2=1\). Since \(m=\mu U\ge0\) while \(z_-<0\), (3) forces \(m\ge z_+\), and the remaining inequalities in (5) follow from (2).

For (4), note
\[
\frac{z_+}{\mu}=\frac1r,\qquad
\frac{\mu}{z_+}=r,\qquad
\frac{a}{\mu}=\frac1r-r.
\tag{16}
\]
Writing \(U=1/r+d\), relation \(\mu(U-V)=a\) gives \(V=r+d\), while \(m-z_+=\mu d\). Hence
\[
\int(y-rx)^2\,d\nu
=V+r^2U-2r\int xy\,d\nu
=(1+r^2)d,
\]
which is (4).

It remains to classify equality. If \(m=z_+\), (4) implies \(y=rx\) on \(\operatorname{supp}\nu\). Put \(h=y-rx\). On the plane \(h=0\), direct differentiation and \(\mu(1-r^2)=ar\) give
\[
\dot h=\frac{ar}{\mu}\,x(z-z_+).
\tag{17}
\]
When \(a>0\), a compact invariant subset of \(h=0\) cannot contain a point with \(x=0\): then also \(y=0\), and the corresponding solution is \((0,0,z_0+t)\), which is unbounded. Thus \(x\ne0\) on the compact invariant support, and tangency to \(h=0\) forces \(z=z_+\). Tangency to this level then requires
\[
0=\dot z=1-rx^2,
\]
so the support is contained in \(\{E_+,E_-\}\). Conversely every convex combination of the two equilibrium point masses is invariant and attains equality. This proves (7).

If \(a=0\), then \(r=1\) and the plane \(x=y\) is itself invariant. Equation (9) therefore gives the stated exact equality classification at the boundary.

For a bounded forward orbit, its empirical probability measures are supported in a compact set and every weak subsequential limit is invariant. Applying (5) to each limit gives (10). Equation (11) follows directly by time-integrating (12)--(15): all endpoint terms divided by \(T\) vanish along a bounded orbit, and the same algebra used for (4) applies asymptotically.

## Context and originality

Rikitake introduced the coupled two-disc dynamo in 1958 to model magnetic-field reversals. Cook and Roberts (1970) developed a global geometric/asymptotic description and reversal mechanism. Barge (1984) proved stable and unstable manifolds for a distinguished noncompact Rikitake solution. Llibre and Valls (2008) classified Darboux integrability and algebraic invariant surfaces. Llibre and Messias (2009) gave a Poincare-compactified global analysis, including the escaping \(z\)-axis orbit and the special \(a=0\) invariant planes; their theorem explicitly identifies the periodic-orbit families in \(x=y\). More recent work continues to study reversal statistics and chaotic regimes, including rare-reversal chaos and non-autonomous forcing.

To the best of our knowledge, the checked literature does not state (2)--(5) as invariant-measure laws, the exact nonnegative defect identity (4), the equilibrium-only equality rigidity (7) for \(a>0\), or the resulting coordinatewise excursion barriers (8). Searches included time-average, stationary-moment, invariant-measure, periodic-orbit, balance-law, and synonymous dynamo formulations. The 2009 full-text article was checked for its principal theorems and for average/mean terminology and does not present these stationary laws.

Residual originality risk remains. The full theorem-level text of the 1958 Rikitake paper and the 1970 Cook--Roberts paper was not fully inspectable through the available source, and a short equivalent time-average identity could have appeared there or in other older dynamo literature without being indexed. The claim of originality is therefore explicitly limited to "to the best of our knowledge."

## Scientific limitations

The result gives necessary constraints on compact invariant statistical states; it does not prove that a periodic or chaotic attractor exists for a given \((a,\mu)\). The Rikitake flow also has unbounded solutions, so the forward-orbit corollary is deliberately restricted to bounded trajectories. The strict equality rigidity requires \(a>0\); the \(a=0\) periodic families show that this restriction cannot simply be dropped. The three excursion conditions in (8) need not occur simultaneously. No claim is made for non-autonomous forced variants.

## Reproducibility

`artifacts/verify_identities.py` symbolically checks the four Lie-derivative identities, the equilibrium algebra, the moment-gap factorization, and the equality-set tangency formula. `artifacts/verification.txt` records the executed zero residuals and the SymPy version.

## References

1. T. Rikitake, "Oscillations of a system of disk dynamos," *Math. Proc. Cambridge Philos. Soc.* **54** (1958), 89--105. https://doi.org/10.1017/S0305004100033223
2. A. E. Cook and P. H. Roberts, "The Rikitake two-disc dynamo system," *Math. Proc. Cambridge Philos. Soc.* **68** (1970), 547--569. https://doi.org/10.1017/S0305004100046338
3. M. Barge, "Invariant Manifolds and the Onset of Reversal in the Rikitake Two-Disk Dynamo," *SIAM J. Math. Anal.* **15** (1984), 514--529. https://doi.org/10.1137/0515039
4. M. Kono, "Rikitake two-disk dynamo and paleomagnetism," *Geophys. Res. Lett.* **14** (1987), 21--24. https://doi.org/10.1029/GL014i001p00021
5. J. Llibre and C. Valls, "Darboux integrability and algebraic invariant surfaces for the Rikitake system," *J. Math. Phys.* **49** (2008), 032702. https://doi.org/10.1063/1.2897983
6. J. Llibre and M. Messias, "Global dynamics of the Rikitake system," *Physica D* **238** (2009), 241--252. https://doi.org/10.1016/j.physd.2008.10.011
7. P. Frick and R. Pleshkov, "Rare-reversal chaos in two-disk dynamo models," *Phys. Rev. E* **110** (2024), 064203. https://doi.org/10.1103/PhysRevE.110.064203
8. M. Herein, L. Kuslits and D. Janosi, "Effect of time-dependent forcing on pole reversals in a conceptual dynamo model," *Sci. Rep.* **16** (2026), 18981. https://doi.org/10.1038/s41598-026-48443-0
