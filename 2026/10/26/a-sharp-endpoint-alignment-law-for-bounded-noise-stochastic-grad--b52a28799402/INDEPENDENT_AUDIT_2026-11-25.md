# Independent mathematical audit

## correctness

PASS

Normalize q=1, set r=||g|| and let s be the noise component along g. For 0<r<=1 the proposed affine minorant is r/2+(1-r/2)s. Inside the clipping ball the excess is r(1+s)/2. Outside, s>-r/2, so the actual projected component is bounded below by F(s)=(r+s)/sqrt(1+r^2+2rs) using the positive numerator. Its second derivative has sign r^2-2-rs<0 on [-r/2,1]. The endpoint values r/2 and 1 exceed or equal the minorant's r^2/4 and 1, so concavity gives the bound. Centering removes the s term. For r>=1 the component is nondecreasing in r by monotonicity of Euclidean projection, so the r=1 bound suffices. Scaling restores q; the symmetric collinear two-point example attains equality for 0<||g||<=q. Below q=sigma, both clipped values are opposite constants on the closed plateau. Coupling to the independent-increment sum up to exit and applying the maximal probability bound V/(sigma-q)^2 gives positive nonexit probability for small amplitude. The square-summable sum converges almost surely and has no atom at zero (condition on everything except the first Gaussian); on sup|S_n|<sigma-q the limit is in the interval and agrees with the actual process. The numerical variance bound uses sum n^(-3/2)<=3 and is exact.

## originality

PASS

Pass the arbitrary-dimensional sharp endpoint inequality for all centered bounded errors, and the stated Gaussian post-clipping consequence of the subthreshold example on the evidence examined. The subthreshold zero-drift plateau itself is already known, and is explicitly credited as such; varying the two radii does not make that example new. No equivalence or implication covering the supported endpoint claim was established in the strongest inspected sources.

## value

PASS

At q=sigma the previous radius-gap bound provides no positive alignment and the subthreshold counterexample rules out such bounds just below it. A sharp dimension-free constant at that exact boundary, under centering rather than symmetry or interior mass, is useful in drift estimates for clipped algorithms and resolves a genuinely motivated threshold. The wrong-limit construction shows why unbiased post-clipping perturbations and finite total noise variance need not let a process escape the plateau; it supports rather than substitutes for the new inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
