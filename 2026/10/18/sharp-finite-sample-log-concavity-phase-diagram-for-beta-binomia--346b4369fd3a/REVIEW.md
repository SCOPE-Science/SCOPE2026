# Independent mathematical audit

## correctness

PASS

The adjacent ratio p_{k+1}/p_k=(n-k)(alpha+k)/[(k+1)(beta+n-k-1)] is exact. Writing u=alpha−1, v=beta−1, clearing positive denominators shows r_{k-1}−r_k has numerator (n-k)(n-k+1)u+k(k+1)v+(n+1)uv. With u>0>v this decreases strictly in k, so nonnegative curvature is equivalent to its value at k=n−1, yielding threshold u>=n(n−1)(−v)/(2+(n+1)v) and strict denominator requirement. Reflection handles v>0>u; u,v>=0 gives all curvatures nonnegative. For u,v<0, setting a=−u,b=−v∈(0,1) bounds numerator by −ab(F+G−n−1)<0. Independently simplified the ratio-difference identity symbolically and read the all-rational n=2..31 verifier including explicit n=3 equality and n=4 failure; finite grid alone does not certify real continuum.

## originality

PASS

General beta-binomial/Pólya–Eggenberger laws and standard sufficient shape>=1 log-concavity were known. The new finite-trial complete necessity-sufficiency rescue wedges, exact edge equality and integer ceiling are not stated by the inspected Martin et al. paper (whose Appendix B concerns regression likelihood in coefficients) or Johnson et al. compound-Poisson framework. Searches for the same under Pólya urn terminology did not yield an equivalently quantified finite-n classification; an older equivalent rational-ratio inequality may exist and is explicitly a risk.

## value

PASS

Provides a full finite-sample shape classification for a canonical overdispersed count law, including an exact finite n ceiling where a single adverse prior parameter cannot be rescued. This changes the applicability of discrete log-concavity-based concentration and algorithmic tools, rather than reparametrizing a standard sufficient condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
