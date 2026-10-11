# Independent mathematical audit

## correctness

PASS

Starting from the frozen RESULT.md and the primary paper equations for scheme 3, write r=1-d and y=1-q. Then C_3(y)=2r sqrt(y)/(r+y) has derivative \(r(r-y)/(\sqrt{y}(r+y)^2)\), so the unique maximum on y in (0,1] occurs at y=r, i.e. q=d. Substitution gives C_max=sqrt(r) and P=r. At the paper's \(q=2d-d^2\) one has \(y=r^2\), C=2r/(1+r), P=r(1+r)/2; both are strictly smaller for 0<r<1. The efficient branch is y in [r,1], equivalently q in [0,d], and eliminating y gives C=r sqrt(2P-r)/P. A fresh independent numerical replay over 99 damping values confirmed the symbolic identities and strict inequalities, while the proof itself is analytic rather than experimental.

## originality

PASS

The primary source explicitly states the conflicting optimizer \(q=2d-d^2\); fresh exact-phrase, DOI, correction/erratum, and Resultary searches did not locate a later publication stating q=d or the Pareto frontier. Because the checked source asserts the opposite conclusion, its displayed formula is evidence enabling the correction but is not a prior statement of the corrected optimum.

## value

PASS

The published operating point is strictly dominated in both concurrence and success probability, so the correction changes a quantitative benchmark rather than merely renaming a parameter. The exact Pareto branch is directly useful for reuse of the protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
