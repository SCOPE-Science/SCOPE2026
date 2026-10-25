# Self-review

## Correctness
**PASS.** All parameters have explicit domains: \(a\ge b>0\), \(s=b^2/a^2\in(0,1]\), \(t=1-s\), and \(0<U<1\). The geometric moments are exactly the trace and determinant of the arclength covariance. The key lemma bounds the covariance of \(U\) with \(U/(1-tU)\), proving strict global monotonicity of its inertia ratio, including circular and thin-limit behavior. The circular expansion and its square-root inverse follow from the beta-arcsine variance. The Python cross-check passed 27 configurations; the infinite claims rest on the proof, not numerical enumeration.

## Originality
**PASS under present evidence, with an explicit historical-priority risk.** Prior work gives the forward principal inertia integrals of elliptical wires. The accessible Tatum exposition was read through the relevant section; it does not state the global strict ratio sandwich, a two-statistic rigid reconstruction theorem, or the optimal inverse square-root exponent. Lord's closely relevant 2014 article is a plausible priority risk: its abstract and bibliographic materials were examined, but the full text was unavailable. The quantitative strict inversion and distortion are not inferred to be historically unique merely because searches failed. Claims are limited to these additions, not the known forward inertia formulas or covariance determinant identity.

## Mathematical value
**PASS.** The arclength law is not an affine image of uniform circular measure, so inversion of its covariance anisotropy is not immediate from axis scaling. The theorem establishes global one-to-one determination of a natural shape from two rotation-invariant sampling statistics, a practical semiaxis-ratio distortion bound, and the exact loss of quadratic identifiability at a circle. No downstream result or large contribution is assumed.

## Closest sources and limits
Nick Lord, *The moment of inertia of an elliptical wire*, Mathematical Gazette 98 (2014), 121–125, DOI 10.1017/S0025557200000796; J. B. Tatum, *Ellipses and Ellipsoids*, section 2.20, elliptical hoop discussion. Source-priority uncertainty remains for Lord's uninspected full article and other historical elliptical-wire literature. The method does not reconstruct ellipse translation or absolute orientation, nor handle arbitrary convex ovals.

Self-review: passed. Independent audit: not yet performed.
