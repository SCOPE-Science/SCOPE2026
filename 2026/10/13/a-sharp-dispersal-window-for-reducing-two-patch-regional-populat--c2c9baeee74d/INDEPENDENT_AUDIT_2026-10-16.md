# Independent mathematical audit

## correctness

PASS

For pinned RESULT.md, symmetric positive-definite drift A has det ab+(a+b)d>0 and unique stationary covariance solving AC+CA=diag(u,v). Independently derived V(d)=[(a+b+4d)(bu+av+d(u+v))]/[2(a+b+2d)(ab+(a+b)d)] and verified both nontrivial polynomial derivative identities exactly using independent SymPy (zero residuals). Ratio R=Pb/Pa has derivative sign(a−b) with strictly positive denominator; V prime crosses from negative to positive at most once and iff v/u strictly between b²/a² and (a+3b)/(3a+b). At a=b, V constant. For u=a,v=b, V=1−d(a−b)²/[2(s+2d)(ab+sd)], derivative optimum d=sqrt(ab/2), 0<1−V<1/2, limit sharp as b/a diverges. Independent exact witness V(1)=49/50 for a=u=1,b=v=2. Read packaged verify_ou.py (blob e40563...) and its standalone rational Lyapunov reconstruction: finite samples corroborate but do not prove signs.

## originality

PASS

In the specified two-patch additive-noise stationary OU model, covariance Lyapunov algebra yields an exact necessary-and-sufficient interior optimum iff the noise ratio lies between b²/a² and (a+3b)/(3a+b), with no possible interior maximum and a sharp half-suppression regime. Wang–Haegeman–Loreau 2015 studies nonlinear logistic dynamics with multiplicative environmental noise and qualitative stabilizing/destabilizing heterogeneity, which cannot be directly specialized to fixed additive-noise dynamics. No checked primary result establishes the same all-parameter ratio window; important part of that primary text remained inaccessible, a nondecisive risk.

## value

PASS

Provides an exact, interpretable environmental-noise asymmetry window where finite dispersal suppresses total regional variability, unique optimum and a sharp maximal proportional suppression in a natural calibration. It resolves a full two-patch stationary fluctuation optimization rather than an arbitrary two-number computation, with clear ecological model limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
