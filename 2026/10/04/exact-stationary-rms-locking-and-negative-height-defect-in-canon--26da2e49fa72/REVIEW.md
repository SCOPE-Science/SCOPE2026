# Review of Exact stationary RMS locking and negative-height defect in canonical Sprott B

## Correctness
PASS. For a compactly supported invariant probability measure, \(\int LF\,d\mu=0\) is valid for the three polynomial test functions used. Direct differentiation gives \(Lz=1-xy\), \(L(y^2/2)=xy-y^2\), and \(L(xy)=x^2-xy+y^2z\). These identities imply the claimed moments and the nonpositive defect exactly. Equality forces \(x=y\) on the invariant support; compactness excludes the unbounded line through \(x=y=0\), and invariance then forces \(z=0\) and \(x^2=1\), leaving only the two equilibria.

## Originality
PASS. The canonical equations were checked against Sprott's original 1994 source. A full-text inspection of Mota–Oliveira's Sprott BC study found its main results to concern singularities, Hopf bifurcation, Poincaré compactification, and algebraic/Darboux integrability; text searches found no invariant-measure, average, mean-square, or periodic-orbit statement matching the claim. Exact semantic searches of published findings returned only analogous balance laws for different systems, not Sprott B. The 2015 generalized-Sprott-B delayed-feedback paper remains a residual risk because only its abstract was accessible, but its stated scope is delayed control and local Hopf bifurcation rather than unforced stationary moment identities.

## Value
PASS. Sprott B is a standard minimal chaotic benchmark, yet the theorem supplies a global, parameter-free constraint on every compact invariant statistical state: the \(y\)-RMS is locked exactly to the equilibrium amplitude. The rigidity and sign defect turn that identity into geometric recurrence information: every non-equilibrium invariant regime must straddle \(|y|=1\) and place positive mass at \(z<0\). This applies uniformly to periodic orbits and compact chaotic invariant measures and is not a numerical property of one simulated attractor.

Same-model review: passed. Independent audit: not yet performed.
