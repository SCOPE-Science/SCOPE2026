# Stationary moment obstruction in a five-dimensional quartic cross-product flow

## Finding

Consider
\[
\dot x=ax-yzuv,\qquad
\dot y=-by+xzuv,\qquad
\dot z=-cz+xyuv,\qquad
\dot u=-du+xyzv,\qquad
\dot v=-ev+xyzu,
\]
with \(a,b,c,d>0\) and \(e\in\mathbb R\). For every compactly supported invariant probability measure \(\mu\),
\[
a\int x^2\,d\mu
=b\int y^2\,d\mu
=c\int z^2\,d\mu
=d\int u^2\,d\mu
=e\int v^2\,d\mu
=\int xyzuv\,d\mu.
\]
Hence:

* if \(e<0\), the only compactly supported invariant probability measure is \(\delta_0\);
* if \(e=0\), every compactly supported invariant probability measure is supported on the equilibrium line
  \[
  \mathcal E=\{(0,0,0,0,v):v\in\mathbb R\},
  \]
  and conversely every probability measure supported on \(\mathcal E\) is invariant;
* if \(e>0\), every nontrivial compactly supported invariant probability measure has a strictly positive common moment and therefore exact RMS ratios
  \[
  \sqrt a\,\|x\|_{L^2(\mu)}
  =\sqrt b\,\|y\|_{L^2(\mu)}
  =\sqrt c\,\|z\|_{L^2(\mu)}
  =\sqrt d\,\|u\|_{L^2(\mu)}
  =\sqrt e\,\|v\|_{L^2(\mu)}.
  \]

The source studies \((a,b,c,d,e)=(11.2,40,14.7,1.4,0)\) as a six-attractor hyperchaotic case and \((11.2,40,14.7,1,-0.1)\) as a four-attractor chaotic case. The theorem above excludes any compact non-equilibrium invariant probability measure in both regimes. In particular, those numerical traces cannot be compact recurrent chaotic or hyperchaotic attractors in the invariant-measure sense.

## Assumptions and scope

The vector field is the polynomial system printed as equation (2.1) in Yang, Feng, and Liu (2021). The result concerns compactly supported invariant Borel probability measures for its continuous flow. Compact support makes each quadratic observable and its Lie derivative integrable, so invariance gives zero mean Lie derivative.

The conclusion does not assert that every trajectory at \(e\le0\) converges to an equilibrium. It leaves open unbounded trajectories and bounded nonrecurrent complete trajectories such as possible connecting orbits. It rules out non-equilibrium compact recurrent statistical dynamics because such dynamics would support a nontrivial invariant probability measure.

## Proof

Put \(P=xyzuv\). Direct differentiation gives
\[
\frac{d}{dt}\frac{x^2}{2}=ax^2-P,
\qquad
\frac{d}{dt}\frac{y^2}{2}=-by^2+P,
\]
\[
\frac{d}{dt}\frac{z^2}{2}=-cz^2+P,
\qquad
\frac{d}{dt}\frac{u^2}{2}=-du^2+P,
\qquad
\frac{d}{dt}\frac{v^2}{2}=-ev^2+P.
\]
For an invariant probability measure \(\mu\) with compact support, integration of each Lie derivative gives zero. Therefore
\[
a\int x^2\,d\mu
=b\int y^2\,d\mu
=c\int z^2\,d\mu
=d\int u^2\,d\mu
=e\int v^2\,d\mu
=\int P\,d\mu.
\]

If \(e<0\), the common value equals \(b\int y^2\,d\mu\ge0\) and also \(e\int v^2\,d\mu\le0\). It must be zero. Since \(a,b,c,d>0\) and \(e<0\), all five coordinate second moments vanish, so \(\mu=\delta_0\).

If \(e=0\), the last equality forces the common value to zero. Positivity of \(a,b,c,d\) then gives
\[
\int x^2\,d\mu
=\int y^2\,d\mu
=\int z^2\,d\mu
=\int u^2\,d\mu=0.
\]
Thus \(\mu\) is supported on \(\mathcal E\). Every point of \(\mathcal E\) is an equilibrium when \(e=0\), so every probability measure supported there is invariant.

If \(e>0\), all five weighted second moments equal the same nonnegative number. If it vanishes, the measure is \(\delta_0\); otherwise it is positive and taking square roots yields the displayed RMS ratios.

## Verification

The five differential identities were checked by exact polynomial arithmetic in `verify.py`. The measure-theoretic step uses only the standard invariance identity
\[
\int L_F\phi\,d\mu=0
\]
for \(C^1\) observables \(\phi\) on the compact support of an invariant measure. No numerical orbit calculation is used in the proof.

At the two parameter sets emphasized by the source, the signs are decisive: \(e=0\) collapses stationary measures to the equilibrium line, while \(e=-0.1<0\) collapses them to the origin.

## Relationship to prior work

Yang, Feng, and Liu introduce the exact five-dimensional polynomial system, analyze equilibria, symmetry, divergence, Lyapunov exponents, bifurcations, and multistability, and numerically report six coexisting hyperchaotic attractors for \(e=0\) and four coexisting chaotic attractors for \(e=-0.1\). Their early Lyapunov-function argument treats a different sign regime with \(a<0\); it does not give the stationary moment chain above for the positive-\(a\) regimes.

Targeted literature-index searches for this exact vector field, its quartic coupling \(xyzuv\), invariant measures, and stationary second-moment identities returned only structurally analogous results for other systems. No inspected source stated the parameter-sign obstruction proved here.

## Limitations

The theorem is a statement about invariant probability measures with compact support and the recurrent statistical dynamics they encode. It does not classify all complete trajectories, prove global convergence for \(e\le0\), or determine whether the source's finite numerical traces are long transients or pieces of unbounded solutions.

Only the mathematically decisive part of the primary full text needed for the comparison was available for direct inspection: the model, parameter regimes, equilibrium discussion, Lyapunov-exponent tables, and the stated attractor claims. Later pages were not available in the same access attempt, leaving a residual literature risk that an equivalent observation appears elsewhere in that article, although targeted exact searches found none.

## References

1. J. Yang, Z. Feng, and Z. Liu, “A New Five-Dimensional Hyperchaotic System with Six Coexisting Attractors,” *Qualitative Theory of Dynamical Systems* 20, Article 18 (2021). DOI: 10.1007/s12346-021-00454-0. Published online 6 February 2021.
2. Institutional bibliographic record for the same article, University of Texas Rio Grande Valley ScholarWorks, publication date 6 February 2021.
