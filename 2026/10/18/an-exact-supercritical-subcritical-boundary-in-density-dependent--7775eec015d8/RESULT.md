# An exact supercritical/subcritical boundary in density-dependent ecological oscillations

## Finding

A concrete two-population density-dependent interaction law has a sharp analytic boundary separating locally attracting from locally repelling oscillatory onsets. The bifurcation may create a periodic trajectory entirely inside an antagonistic ecological regime even though the complete model admits a region of strict mutualism. In particular, identical imaginary-axis eigenvalues do not determine whether an emerging periodic orbit attracts or repels.

Consider the ecological law
\[
\dot x=x[a_1-b_1(y-c_1)^2-d_1x],\qquad
\dot y=y[-a_2-b_2(y-c_2)^2+d_2x].
\]
For the positive coefficient family in the next section, the equilibrium \((1,1)\) has a transverse Hopf crossing at \(\mu=0\) and frequency \(\omega=\sqrt{BD-1}\). Its **Cartesian radial cubic coefficient** is
\[
L=-\frac{D[B(D+2)-3]}{8B(BD-1)}.
\]
If \(B(D+2)>3\), a locally unique orbitally attracting cycle is born for sufficiently small \(\mu>0\). If \(B(D+2)<3\), a locally unique orbitally repelling cycle is born for sufficiently small \(\mu<0\). Both are strictly positive and confined to the antagonistic region \(y>1/2\). In the rotating coordinates below, their leading radius is \(\sqrt{-\mu/L}\), and their period tends to \(2\pi/\omega\).

## Assumptions and scope

Fix \(B>0\), \(D>1/4\), and \(BD>1\). Choose the original population parameters
\[
\begin{aligned}
a_1&=1+B/4,& b_1&=B,& c_1&=1/2,&d_1&=1,\\
a_2&=D-(1/2+\mu)^2,&b_2&=1,&c_2&=3/2+\mu,&d_2&=D.
\end{aligned}
\]
Take \(|\mu|\) sufficiently small, depending on the fixed \((B,D)\), that \(a_2,c_2>0\). All eight parameters are then positive. The state space is the nonnegative population quadrant; the stated Hopf cycles remain in its interior. The analysis is local near \((1,1)\) and \(\mu=0\), not a classification of all positive equilibria, global trajectories, or larger cycles.

For any fixed \(B,D\) satisfying these inequalities, the per-capita cross-effects have signs
\[
\partial_y f=B(1-2y),\qquad \partial_x g=D>0.
\]
Thus \(0<y<1/2\) is a strict-mutualism region, and \(y>1/2\) is an antagonistic region (positive effect of \(x\) on \(y\), negative effect of \(y\) on \(x\)). No periodic trajectory is claimed to remain in the mutualistic region.

## Proof

**1. Positive equilibrium and crossing.** Write \(u=x-1\) and \(v=y-1\). Direct substitution gives the exact shifted equations
\[
\begin{aligned}
\dot u&=-u-Bv-u^2-Buv-Bv^2-Buv^2,\\
\dot v&=Du+(1+2\mu)v+Duv+2\mu v^2-v^3.
\end{aligned}
\]
In particular, \((u,v)=(0,0)\) is an equilibrium for every small \(\mu\), with Jacobian
\[
J_\mu=\begin{pmatrix}-1&-B\\D&1+2\mu\end{pmatrix},\qquad
\operatorname{tr}J_\mu=2\mu,\qquad
\det J_\mu=BD-1-2\mu.
\]
Since \(BD>1\), its eigenvalues at \(\mu=0\) are \(\pm i\omega\), with \(\omega=\sqrt{BD-1}\). For sufficiently small \(\mu\) the pair is complex, and its real part equals \(\mu\), so the crossing speed is exactly one.

**2. An independently checkable focal-coefficient calculation.** Put
\[
U=u,\qquad V=\frac{u+Bv}{\omega},\qquad
v=\frac{\omega V-U}{B}.
\]
At \(\mu=0\), these coordinates transform the linear terms to the standard rotation \(\dot U=-\omega V\), \(\dot V=\omega U\). Let
\[
H=-U^2-BUv-Bv^2-BUv^2,\qquad K=DUv-v^3,
\]
where the symbol \(v\) on the right means \((\omega V-U)/B\). The exact nonlinear terms in rotating coordinates are
\[
F=H,\qquad G=\frac{H+BK}{\omega},\qquad
\dot U=-\omega V+F,\quad \dot V=\omega U+G.
\]
All derivatives below are at \((U,V)=(0,0)\). For a planar analytic vector field with this rotation, the conventional real Cartesian radial cubic coefficient is
\[
\begin{split}
L={}&\frac{F_{UUU}+F_{UVV}+G_{UUV}+G_{VVV}}{16}\\
&+\frac{F_{UV}(F_{UU}+F_{VV})-G_{UV}(G_{UU}+G_{VV})
-F_{UU}G_{UU}+F_{VV}G_{VV}}{16\omega}.
\end{split}
\]
Substituting the displayed polynomials and using \(\omega^2=BD-1\) yields exactly
\[
L=-\frac{D[B(D+2)-3]}{8B(BD-1)}.
\]
The package's symbolic checker verifies this identity directly by differentiation and independently through the complex-eigenvector multilinear formula. The nonzero denominator follows from the assumptions; hence the sign of the first nonzero radial cubic term is determined precisely by \(B(D+2)-3\).

**3. Small periodic orbits.** For \(L\ne0\), the smooth nondegenerate Hopf theorem applies. In near-identity polar normal-form coordinates the radial equation is
\[
\dot r=\mu r+Lr^3+O(\mu^2r+|\mu|r^3+r^5).
\]
The local nonzero radial equilibrium satisfies \(r^2=-\mu/L+O(\mu^2)\). It exists exactly on the nearby side where \(\mu L<0\), is radially attracting if \(L<0\), and radially repelling if \(L>0\). The equilibrium is attracting for small negative \(\mu\) and repelling for small positive \(\mu\). The resulting limit cycle has physical period approaching \(2\pi/\omega\). In the fixed rotating Cartesian coordinates of step 2,
\[
\max_{t\text{ on cycle}}\sqrt{U(t)^2+V(t)^2}
=\sqrt{-\mu/L}+O(|\mu|).
\]
The cycles shrink to \((x,y)=(1,1)\) as \(\mu\to0\). Therefore, for sufficiently small admissible \(\mu\), they are entirely in \(x>0\), \(y>1/2\), where \(\partial_y f<0<\partial_xg\). They do not enter the strict-mutualism region \(0<y<1/2\), despite that region being nonempty.

**4. Exact boundary and contrasting examples.** The nondegenerate supercritical/subcritical boundary is \(B(D+2)=3\). If \(1/4<D\le1\), the restriction \(BD>1\) forces \(B(D+2)>3\), hence only supercritical onset is possible within this family. If \(D>1\), the interval \(1/D<B<3/(D+2)\) gives subcritical onset, while \(B>3/(D+2)\) gives supercritical onset. On the separating curve \(B=3/(D+2)\), the cubic coefficient vanishes and no classification of the resulting higher-order degeneracy is asserted.

The exact positive pairs \((B,D)=(1,2)\) and \((B,D)=(2/5,5)\) both have \(BD=2\), so both unit equilibria have the same Hopf eigenvalues \(\pm i\). Yet their cubic radial coefficients are respectively \(-1/4\) and \(5/16\), giving stable small cycles on the positive-\(\mu\) side in the first case and unstable small cycles on the negative-\(\mu\) side in the second. Thus linear oscillatory frequency alone cannot distinguish the two ecological outcomes.

## Verification

The standalone `verify.py` (Python 3 with SymPy) performs exact symbolic differentiation of the rotating-coordinate vector field, checks the simplified rational expression for \(L\), checks the independent multilinear-eigenvector formula, and verifies both rational examples. No floating-point calculation is needed for these identities. Run `python verify.py` after installing the dependency in `requirements.txt`. Its output is a supplementary algebraic replay; the proof of the existence and stability of the small periodic orbits is the analytic Hopf theorem as applied above, not a finite simulation.

## Relationship to prior work

Mian, Billiard, Llaurens, and Smadi introduce the general density-dependent interaction framework and the precise polynomial species system used here as their Eq. (4), with a numerical example of an attracting cycle that visits mutualistic and parasitic regions. Their discussion addresses qualitative existence of oscillations but does not calculate the parameter-wide rational Hopf criticality surface for the above normalization. The present finding quantifies a distinct local boundary: near-Hopf cycles can be entirely antagonistic although the same global ecological law admits strict mutualism elsewhere.

Morales, Morris, and Wilson previously exhibited both subcritical and supercritical ecological Hopf bifurcations in a different nonlinear protection-mutualism trophic-cascade system. Song and collaborators investigated oscillations in a different obligate-mutualism model with saturating benefit/cost responses. Both precedents are acknowledged: the general possibility of either Hopf type, the ordinary Hopf theorem, and oscillations due to nonmonotone interactions are not claimed as new. The asserted contribution is the exact sign surface, matched-spectrum opposing examples, and mutualism-region localization for this specific quadratic source family.

## Limitations

The coefficient-zero case \(B(D+2)=3\) is not proved to be a generalized Hopf (Bautin) point; the fifth-order coefficient and associated global cycle organization are unproved. The theorem does not establish that cycles of large amplitude stay outside strict mutualism or classify other positive equilibria. The negative-\(\mu\) subcritical cycle is locally repelling, not a claim of ecological multistability. The result concerns a deterministic two-species idealization and does not justify direct predictions for empirical mutualistic communities. Some potentially related literature is only abstract-accessible, so a later full-text comparison could identify broader coverage.

## References

1. C. Mian, S. Billiard, V. Llaurens, and C. Smadi, *Dynamics of Two Species with Density-Dependent Interactions and Application to Mutualism*, arXiv:2509.06062 (first public version 2025-09-07), especially Eq. (4), Example 4.7, and Section 4. DOI: 10.1007/s11538-026-01724-1.
2. M. A. Morales, W. F. Morris, and W. G. Wilson, *Allee dynamics generated by protection mutualisms can drive oscillations in trophic cascades*, Theoretical Ecology 1 (2008), 77–88. DOI: 10.1007/s12080-007-0006-9.
3. X.-M. Song et al., *Periodic Oscillations and Transient Dynamics Caused by Saturating Density-Dependent Benefits and Costs in Obligate Mutualisms*, Bulletin of Mathematical Biology 87 (2025), article 154. DOI: 10.1007/s11538-025-01531-0.
4. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer, standard nondegenerate Hopf bifurcation and first Lyapunov coefficient formula.
