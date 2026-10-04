# Exact first-integral foliation behind extreme multistability in a five-dimensional chaotic flow

## Finding

For the Ahmadi–Wang–Nazarimehr–Alsaadi–Pham five-dimensional flow \(\dot x=y\), \(\dot y=z\), \(\dot z=w\), \(\dot w=\frac{41}{25}x^2-\frac{51}{50}w+v+\frac{7}{25}xy\), and \(\dot v=\frac{121}{50}xw-\frac{3}{10}yz\), the polynomial \(I=v-\frac{121}{50}xz+\frac{34}{25}y^2\) is a global first integral. Hence every trajectory lies on the smooth invariant four-manifold \(M_C=\{I=C\}\), on which the system reduces exactly to a four-dimensional flow with \(v=C+\frac{121}{50}xz-\frac{34}{25}y^2\). The equilibrium curve intersects \(M_C\) iff \(C\le 0\): for \(C<0\) the two intersections have \(x=\pm\sqrt{-25C/41}\), while \(C=0\) gives the origin. On a negative level, the positive-\(x\) equilibrium is unstable, whereas the negative-\(x\) equilibrium is asymptotically stable relative to \(M_C\) exactly when \(x<-213282/38297\), equivalently \(C<-1865057672484/36666505225\); equality produces a purely imaginary pair with \(\omega^2=8364/5471\). For the initial family used in the source, \(x_0=-2.77\), \(y_0=-0.53\), \(z_0=2.7\), \(w_0=-0.34\), varying \(v_0\) is exactly the leaf-parameter scan \(C=v_0+18.481204\), so every displayed case with \(v_0>-18.481204\) lies on a no-equilibrium leaf. Finally, if a compact invariant set \(K\subset M_C\), then every point whose forward orbit approaches \(K\) must already lie in \(M_C\); since \(M_C\) has empty interior in \(\mathbb R^5\), such an individual leafwise attractor cannot have an open basin in the full five-dimensional phase space. Thus the reported initial-condition-driven extreme multistability has an exact conserved-leaf mechanism, and its plotted individual attractors are necessarily relative attractors of distinct invariant leaves rather than full-space attractors with open basins.

## Assumptions and scope

The vector field is the autonomous system printed as Equation (1) in Ahmadi et al. (2019), with the decimal coefficients interpreted exactly as the terminating decimals used in that equation: \(1.64=41/25\), \(1.02=51/50\), \(0.28=7/25\), \(2.42=121/50\), and \(0.3=3/10\). The claim concerns the exact continuous-time ODE. “Attractor with an open basin” means a compact invariant set \(K\) for which the set of initial conditions satisfying \(\operatorname{dist}(\phi_t(p),K)\to0\) contains a nonempty open subset of \(\mathbb R^5\). The statement does not deny the existence of relative attractors inside the invariant hypersurfaces \(M_C\).

## Proof

Differentiate
\[
I=v-\frac{121}{50}xz+\frac{34}{25}y^2.
\]
Using \(\dot x=y\), \(\dot y=z\), \(\dot z=w\), and \(\dot v=\frac{121}{50}xw-\frac{3}{10}yz\),
\[
\begin{aligned}
\dot I
&=\frac{121}{50}xw-\frac{3}{10}yz
-\frac{121}{50}(yz+xw)
+\frac{68}{25}yz\\
&=0.
\end{aligned}
\]
Thus \(I\) is constant on every trajectory. Because \(\partial I/\partial v=1\), every level \(M_C\) is a smooth codimension-one hypersurface. Solving \(I=C\) for \(v\) gives
\[
v=C+\frac{121}{50}xz-\frac{34}{25}y^2,
\]
which substituted into the first four equations gives the exact four-dimensional leaf dynamics
\[
\dot w=\frac{41}{25}x^2-\frac{51}{50}w+C+\frac{121}{50}xz-\frac{34}{25}y^2+\frac{7}{25}xy.
\]

The source equilibrium curve is \(E_s=(s,0,0,0,-\frac{41}{25}s^2)\). On it,
\[
I(E_s)=-\frac{41}{25}s^2.
\]
Therefore \(M_C\) contains no equilibrium for \(C>0\), one degenerate equilibrium for \(C=0\), and exactly two equilibria \(s=\pm\sqrt{-25C/41}\) for \(C<0\).

At \(E_s\), direct determinant expansion gives
\[
\chi_s(\lambda)=\lambda\left(\lambda^4+\frac{51}{50}\lambda^3-\frac{121}{50}s\lambda^2-\frac{7}{25}s\lambda-\frac{82}{25}s\right).
\]
For \(s\ne0\), the zero eigenvector is tangent to the equilibrium curve and is transverse to the leaf because \(d(I(E_s))/ds=-\frac{82}{25}s\ne0\). Hence the quartic factor is exactly the characteristic polynomial of the linearization restricted to \(T_{E_s}M_C\).

For the negative branch write \(s=-u\), \(u>0\). Its quartic is
\[
q_u(\lambda)=\lambda^4+\frac{51}{50}\lambda^3+\frac{121}{50}u\lambda^2+\frac{7}{25}u\lambda+\frac{82}{25}u.
\]
All coefficients are positive. The nontrivial Hurwitz determinants reduce to
\[
\Delta_2=\frac{5471}{2500}u>0,
\qquad
\Delta_3=\frac{u(38297u-213282)}{62500}.
\]
Therefore the negative equilibrium is leafwise asymptotically stable exactly when \(u>213282/38297\). At equality, the imaginary part of \(q_u(i\omega)=0\) gives \(\omega^2=(14/51)u=8364/5471\). Converting the threshold through \(C=-\frac{41}{25}u^2\) yields \(C<-1865057672484/36666505225\). On the positive branch \(s>0\), the quartic has negative constant term, so continuity on the positive real axis gives at least one positive real eigenvalue; that branch is unstable.

For the source's one-parameter initial family,
\[
C=v_0-\frac{121}{50}x_0z_0+\frac{34}{25}y_0^2
=v_0+\frac{4620301}{250000}
=v_0+18.481204.
\]
Thus the apparent scan in one initial coordinate is exactly a scan through invariant leaves; in particular the source examples at \(v_0=-18\), \(v_0=-17.75\), and \(v_0=-16.5\) all satisfy \(C>0\) and therefore lie on leaves containing no equilibrium.

Finally let \(K\subset M_C\) be compact and invariant, and suppose \(\operatorname{dist}(\phi_t(p),K)\to0\). Since \(I(\phi_t(p))=I(p)\) for all \(t\) and \(I\) is continuous, approaching \(K\subset I^{-1}(C)\) forces \(I(p)=C\). Hence the full-space basin of \(K\) is contained in \(M_C\). The condition \(\partial I/\partial v=1\) makes \(M_C\) a smooth hypersurface with empty interior, so that basin cannot contain an open subset of \(\mathbb R^5\).

## Verification

The packaged checker uses exact rational arithmetic. It verifies \(\dot I\equiv0\), reconstructs the characteristic polynomial by an independent symbolic determinant over rational bivariate polynomials, checks the two Hurwitz determinants and the exact threshold, verifies the source initial-family offset \(4620301/250000\), and checks the no-equilibrium threshold. Its recorded output is `VERIFY_OK`.

The primary article's full open-access text was inspected directly for Equation (1), the equilibrium curve, its characteristic polynomial, the initial family, the reported period-one/period-two/period-four/chaotic cases, and the publication date. The source states that varying \(v(0)\) changes long-term behavior while holding the other four initial coordinates fixed; it does not state the first integral above or the resulting invariant-leaf reduction.

## Relationship to prior work

Ahmadi et al. introduce the exact five-dimensional system, report a curve of equilibria, and numerically interpret varying \(v(0)\) as initial-condition-driven extreme multistability. The present finding supplies the missing exact invariant that makes this dependence structural rather than merely numerical, gives the exact four-dimensional reduction, partitions the equilibrium content of every leaf, and qualifies the basin interpretation of each plotted invariant set.

Ngonghala, Feudel, and Showalter (2011) established in coupled chemical models that extreme multistability can be associated with an emergent conserved quantity and state-space slicing. Hens, Dana, and Feudel (2015) likewise relate extreme multistability in coupled systems to an emergent conserved quantity. Those papers provide a broader conceptual precedent, but they do not contain this vector field, this globally exact polynomial first integral, the leafwise equilibrium/Hurwitz partition, or the full-space basin obstruction proved here. The distinction is important: their conserved quantities arise in different coupled models, whereas here the source's published autonomous flow itself has an exact first integral for all times.

## Limitations

The theorem does not prove that every leaf contains a periodic or chaotic attractor, does not validate the numerical Lyapunov/Kolmogorov–Sinai calculations in the source, and does not determine basins within a fixed leaf. It also does not exclude a larger invariant attracting union spanning a continuum of \(C\)-levels; the basin obstruction applies to an individual compact invariant set contained in one level. The exact terminating decimals are treated as the coefficients defining the published mathematical model. Targeted semantic and web searches cannot rule out an unindexed equivalent derivation.

## References

A. Ahmadi, X. Wang, F. Nazarimehr, F. E. Alsaadi, F. E. Alsaadi, and V.-T. Pham, “Coexisting infinitely many attractors in a new chaotic system with a curve of equilibria: Its extreme multi-stability and Kolmogorov–Sinai entropy computation,” *Advances in Mechanical Engineering* 11 (2019), DOI 10.1177/1687814019888046. First published online 16 November 2019.

C. N. Ngonghala, U. Feudel, and K. Showalter, “Extreme multistability in a chemical model system,” *Physical Review E* 83, 056206 (2011), DOI 10.1103/PhysRevE.83.056206.

C. Hens, S. K. Dana, and U. Feudel, “Extreme multistability: Attractor manipulation and robustness,” *Chaos* 25, 053112 (2015), DOI 10.1063/1.4921351; arXiv:1505.02094.
