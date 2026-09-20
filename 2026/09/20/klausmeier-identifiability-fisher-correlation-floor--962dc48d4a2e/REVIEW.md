# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The main identities follow directly from the exact ODE.  For positive biomass, `(log n)'=wn-m`; integrating this and the water equation gives explicit formulas for both parameters on every nonzero-length observation interval.  If biomass starts at zero, uniqueness preserves the invariant set `n=0`, on which the mortality parameter is absent.  At positive equilibrium the inverse map is `a=w(1+n^2)`, `m=wn`, with determinant `w(1-n^2)`, so the only positive-equilibrium rank loss is the fold `n=1`.

For equilibrium-only isotropic Gaussian observations, the expected Fisher matrix is proportional to `S^T S`, where `S=(D Psi)^(-1)`.  Inverting gives a covariance proportional to `D Psi D Psi^T`.  Symbolic simplification yields the displayed correlation identity.  Its derivative in `x=n^2>1` factors into fixed-sign factors and one quadratic, giving the unique extremum `x=1+sqrt(2(1+m^2))`; substitution gives the stated sharp correlation floor.  The verification artifact checks these identities exactly and reproduces the numerical value for `m=0.45`.

The equilibrium sign-pairing correction was checked directly against `wn=m`.  It is also consistent with older Klausmeier literature, so it is treated as a source notation correction rather than a new equilibrium result.

## Originality — PASS, narrowly scoped

Generic structural/practical identifiability theory, inverse-function arguments, Fisher information, and Klausmeier equilibrium/stability formulas are prior art and are not claimed as new.  Köhnke and Malchow (2017) already give the correct nontrivial equilibrium pairing.  A 2023 generalized Klausmeier study includes a distinct inverse problem, and broader identifiability literature provides the standard conceptual framework.

Searches using the 2026 source identifier and title, `Klausmeier structural identifiability`, `Klausmeier parameter estimation`, `Klausmeier Fisher information`, `Klausmeier parameter correlation`, and equivalent steady-state inverse formulations did not locate a prior statement of the exact continuous full-state recovery dichotomy or the closed-form equilibrium correlation floor for this two-parameter non-spatial model.  The accepted originality claim is therefore restricted to those source-specific formulas and their use to separate structural identifiability from the practical near-collinearity reported in arXiv:2609.18231v1.

The search was not exhaustive over every ecology, inverse-problem, and systems-identification publication.  An algebraically equivalent formula could exist under different terminology.  This residual risk is why no broad priority claim is made for the underlying methods or for parameter identifiability in ecological ODEs generally.

## Value — PASS

The source paper's central numerical message is that joint inference becomes unreliable in its bistable regime and that parameter correlations become very strong.  The present result gives an exact explanation of what part of that phenomenon is structural and what part is conditioning: mortality is truly invisible only on the desert invariant set, while positive full-state trajectories identify both parameters exactly.  Yet on the stable positive equilibrium branch at the source's `m=0.45`, even ideal local Gaussian inference cannot reduce the parameter correlation below `0.99729144`.  This turns a numerical observation of near-collinearity into a sharp analytic bound and explains why repeated steady-state measurements alone can remain poorly directional despite nonzero Fisher determinant.

The correction of the source's same-sign equilibrium labels also prevents a simple algebraic inconsistency from propagating into subsequent uses of the printed formulas.

## Limitations

The integral reconstruction formulas concern exact continuous full-state observations and are not claimed to be statistically efficient estimators under noise.  The Fisher-correlation result is local and asymptotic for independent isotropic Gaussian observations of an exact equilibrium; transient data, different noise models, partial observations, priors, or finite-sample nonlinear effects can alter practical behavior.  No claim is made about the spatial Klausmeier PDE, and the source's numerical code was not inspected, so the printed equilibrium indexing error is not evidence that its computations used the wrong branch pairing.
