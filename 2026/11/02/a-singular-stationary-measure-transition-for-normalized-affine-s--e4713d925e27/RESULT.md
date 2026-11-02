# A singular stationary-measure transition for normalized affine sphere maps

## Finding

**Theorem (global cycles and stationary measures).** For any integer \(n\ge 2\), any unit vector \(e\in\mathbb R^{n+1}\), and every \(0<r<1\), \(0<\alpha<1\), the following normalized affine sphere map has a sharp stationary-measure transition at \(\alpha^2+r^2=1\):
\[
F(x)=\frac{\alpha e-[ee^{\mathsf T}+r(I-ee^{\mathsf T})]x}
{\left\|\alpha e-[ee^{\mathsf T}+r(I-ee^{\mathsf T})]x\right\|},
\qquad x\in S^n.
\]
Put \(h_*=\alpha/(1+r)\) and \(q(v)=h_*e+\sqrt{1-h_*^2}\,v\) for \(v\in S^{n-1}\subset e^\perp\). Denote the poles by \(p_+=e\), \(p_-=-e\), and the latitude by \(Q=\{q(v):v\in S^{n-1}\}\).

If \(\alpha^2+r^2\ne1\), the full least-period-two set is exactly \(Q\cup\{p_+,p_-\}\); there are no fixed points or orbits of higher least period. Every invariant Borel probability is of the form
\[
\mu=w\frac{\delta_{p_+}+\delta_{p_-}}2+
(1-w)\int_{\mathbb {RP}^{n-1}}
\frac{\delta_{q(v)}+\delta_{q(-v)}}2\,d\eta([v]),
\quad 0\le w\le1,
\]
where \(\eta\) is any Borel probability on \(\mathbb{RP}^{n-1}\) (with the harmless convention that \(\eta\) is immaterial when \(w=1\)). Consequently, no invariant probability is absolutely continuous with respect to the \(n\)-dimensional surface measure.

The attraction basins undergo an exact exchange. If \(\alpha^2+r^2<1\), then all initial points outside \(Q\) converge alternately to the polar pair; if \(\alpha^2+r^2>1\), every nonpolar initial point \(x=h e+\sqrt{1-h^2}v\) converges alternately to \(q(v)\) and \(q(-v)\). These statements specify the two limiting subsequences of the original iterates. In each case the empirical measures converge to the equally weighted measure on the limiting pair.

At \(\alpha^2+r^2=1\), the map satisfies \(F^2=I\) on all of \(S^n\) and has no fixed points. Thus **every point has least period two** and all orbit-pair probabilities are invariant. In particular there exists a smooth strictly positive invariant probability \(\rho\,d\sigma_n\), with \(\sigma_n\) normalized area and
\[
\rho(x)=\frac12\left[1+
\left(\frac{r}{1-\alpha\langle e,x\rangle}\right)^n\right].
\]
The set of parameters with an absolutely continuous invariant probability is therefore exactly the codimension-one curve \(\alpha^2+r^2=1\) within the stated range.

## Assumptions and scope

Here \(S^n\) is the Euclidean unit sphere in \(\mathbb R^{n+1}\), and \(S^{n-1}\) is the unit sphere perpendicular to \(e\). The map is smooth and invertible: the denominator never vanishes because \(0<\alpha<1\), and the axial coordinate map defined below is a strictly decreasing bijection of \([-1,1]\). The claims concern **all** Borel invariant probabilities, not only ergodic probabilities or probabilities having moments. The probability \(\eta\) parametrizes all antipodal-invariant laws on the latitude.

## Proof

**1. Exact skew-product coordinates.** A nonpolar point is uniquely \(x=h e+\sqrt{1-h^2}v\), with \(-1<h<1\) and \(v\in S^{n-1}\). Define
\[
D(h)=\sqrt{(\alpha-h)^2+r^2(1-h^2)},
\qquad f(h)=\frac{\alpha-h}{D(h)}.
\]
Then \(F(h,v)=(f(h),-v)\). Direct differentiation gives
\[
f'(h)=-\frac{r^2(1-\alpha h)}{D(h)^3}<0,
\qquad f(-1)=1,\quad f(1)=-1.
\]
Thus \(f\) is a decreasing homeomorphism, \(f^2\) is increasing, and the poles form a two-cycle. No nonpolar point can be fixed because \(v\mapsto-v\). The only fixed axial level of \(f\) is \(h_*=\alpha/(1+r)\), since at a fixed level the positive normalization must equal \(r\); accordingly \(Q\) is pointwise fixed under \(F^2\).

**2. No other two-cycles except at the resonance.** Suppose \(F^2(h,v)=(h,v)\) with \(-1<h<1\), and let \(D_0=D(h)\), \(D_1=D(f(h))\). The transverse components force \(D_0D_1=r^2\). The axial components then imply
\[
D_0=1-\frac{1-r^2}{\alpha}h.
\]
Comparison of its square with \(D(h)^2\) yields the **exact factorization**
\[
D(h)^2-\left(1-\frac{1-r^2}{\alpha}h\right)^2
=\frac{[\alpha-(1+r)h][\alpha-(1-r)h]
[\alpha^2+r^2-1]}{\alpha^2}.
\]
Off resonance, \(h=\alpha/(1+r)\) is valid and \(h=\alpha/(1-r)\) is invalid: at the latter value the required positive \(D_0\) would equal \(-r\). These exhaust the roots, together with the two poles. No other periodic orbit of any order is possible because \(f^2\) is increasing: an increasing interval map has no cycles of period greater than one, and odd-period points of \(F\) would be fixed by its direction flip (or would be poles, which swap).

**3. Global basin and stationary-law classification.** The normal derivative of \(F^2\) on \(Q\) and its scalar tangent derivative at each pole are respectively
\[
\Lambda_Q=\left(\frac{1-\alpha^2/(1+r)}r\right)^2,
\qquad \Lambda_P=\frac{r^2}{1-\alpha^2}.
\]
For \(\alpha^2+r^2<1\), the inequalities are \(\Lambda_Q>1>\Lambda_P\); for \(\alpha^2+r^2>1\), they reverse. Since \(f^2\) is strictly increasing, has no other fixed points, and fixes both endpoints, its iterates converge monotonically toward the appropriate attractive fixed level on each side of \(h_*\). The transverse coordinate alternates exactly. This proves the claimed basins, all orbit asymptotics, and convergence of empirical measures.

For an invariant Borel probability \(\mu\), invariance under \(F^2\) yields \(\int\psi\,d\mu=\int\psi\circ F^{2j}\,d\mu\) for every continuous test function \(\psi\). Dominated convergence and the pointwise basin limits imply that \(\mu\) is supported on \(Q\cup\{p_+,p_-\}\). Invariance under \(F\), which exchanges each pair, forces equal weights along each pair. Disintegration by the quotient \(Q/(v\sim-v)\cong\mathbb{RP}^{n-1}\) gives precisely the displayed simplex; conversely all its members are manifestly invariant. Since \(n\ge2\), \(Q\) and the poles have zero \(n\)-surface measure.

**4. Resonance and explicit smooth invariant density.** If \(\alpha^2+r^2=1\), then \(D(h)=1-\alpha h>0\) and
\[
f(h)=\frac{\alpha-h}{1-\alpha h},
\qquad f(f(h))=h,
\qquad F^2=I.
\]
There are still no fixed points. In meridional and latitude directions the map has the same absolute length scale \(s(h)=r/(1-\alpha h)\), because \(1-f(h)^2=r^2(1-h^2)/(1-\alpha h)^2\) and \(f'(h)=-r^2/(1-\alpha h)^2\). Hence its surface Jacobian is \(J_F(x)=s(h)^n\). By the involution, \(J_F(Fx)J_F(x)=1\) and \(F_*\sigma_n=J_F\,\sigma_n\). Therefore the average of area measure with its pushforward is invariant, has density \(\rho=(1+J_F)/2\), integrates to one, and is strictly positive and smooth. This proves the measure-type transition and all assertions.

## Verification

The standalone `verify.py` checks the nontrivial period-two factorization symbolically, the resonance involution, the latitude/pole multipliers and several finite-dimensional trajectories on both sides of the boundary. Reproduction: run `python verify.py` with Python 3 and SymPy installed. These checks are supplementary; the proof above establishes the statement for all parameters and dimensions in scope.

## Relationship to prior work

Choudhuri, Faraco and Yadav (arXiv:2209.05236v1, 2022) define and investigate normalized affine actions on spheres. Their Proposition 3 already gives a necessary and sufficient involution criterion **on the circle** \(S^1\) for two distinct negative eigenvalues, and their Corollary 9 treats the scalar negative case there. Applying the circle criterion to each invariant meridian immediately predicts the same resonant equation in this axisymmetric family; **that isolated equation is not claimed as new**. The present higher-dimensional finding is the complete stationary-law simplex and global attraction-basin exchange together with the precise absence/existence of a smooth full-support invariant probability at the resonance. Their inspected higher-dimensional distality and expansivity results do not establish this joint statistical classification.

The classical concept that a periodic diffeomorphism preserves the average of a smooth measure over its finite orbit explains the construction at resonance. The contribution is the precise characterization of when the periodic regime occurs and the complete invariant-probability classification on both sides. The earlier real-circle phase portrait may be used meridian by meridian, but the global family of invariant measures and measure-class transition require the additional classification given here.

## Limitations

No uniqueness of invariant probability is asserted, even at resonance. The singularity statement concerns \(n\)-dimensional surface measure, not measures supported on the latitude. The map is a special axisymmetric negative-diagonal subfamily, not an arbitrary normalized affine sphere map. The resonance involution equation itself is covered in dimension one by the cited Proposition 3 and follows meridianwise; only the complete higher-dimensional global statistical phase portrait and stationary-measure transition are advanced as the finding. Equivalent results in unindexed literature remain a publication-priority risk. No independent audit has been conducted.

## References

1. M. Choudhuri, G. Faraco and A. K. Yadav, *On the distality and expansivity of certain maps on spheres*, arXiv:2209.05236v1 (publicly posted 2022-09-12), `https://arxiv.org/abs/2209.05236` (especially Proposition 3, Corollary 9, and Section 3). Later publication: *Dynamical Systems* 39 (2024), 166–181, DOI `10.1080/14689367.2023.2248013`.
2. R. Shah and A. K. Yadav, *Distality of certain actions on p-adic spheres*, *Journal of the Australian Mathematical Society* 109 (2020), 250–261, DOI `10.1017/S1446788719000272`. This work is explicitly p-adic and is not the same real-sphere classification.
