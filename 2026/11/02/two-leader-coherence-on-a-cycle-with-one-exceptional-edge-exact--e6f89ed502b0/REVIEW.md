# Independent mathematical audit

## correctness

PASS

The grounded arcs decouple. On a chain, unit current at an interior vertex sees its two resistance-to-ground paths in parallel, giving the diagonal s(T-s)/T. On the exceptional arc the two sets of distances measured from their respective leaders are 1,...,A and 1,...,B. Summing s-s²/(m-1+x), using A+B=m-1, gives (1), even for an empty arc. The sign of the AB coefficient forces endpoint incidence of one leader at x<1, a floor/ceiling split at x>1, and no within-separation preference at x=1. For an independent sign proof of the strong case, write t=n-ell-1 and R(t)=t(2t+1)/(t+x); the strong-branch correction to the uniform objective is -(1-x)R(t)/6. R is strictly increasing. Thus Q strictly increases to the right of floor(n/2), even across the uniform odd-n tie. For a step to its left, the uniform cost falls by at least 2/6 as ell increases. At the new t>=1, the correction rises by (1-x)[2-x(2x-1)/((t+x)(t+x+1))]/6, strictly less than 2/6: for x>=1/2 this is immediate, and for x<1/2 the bracket is at most 2+x/2. This proves the claimed unique separation for all real 0<x<1 including n=3. Substitution gives (3). The weak scalar scan is exhaustive and can emit all ties using two passes with constant extra workspace, counting arithmetic evaluations. Independently written exact matrix inversions corroborated 833 traces (n=3–9, seven rational x) and all corresponding optimizer sets; this finite check is not the general proof.

## originality

PASS

The distinct contribution is the one-defect classification for x≠1, especially the exact strong-edge separation and strict reversal of the location preference at fixed separation. The uniform case, chain Green function, and general weighted-ring algorithm are existing coverage and are not credited as novel.

## value

PASS

A single altered edge is a natural minimal perturbation of equally spaced optimal leaders on a homogeneous ring. The exact endpoint-to-centered switch answers a robust design question for every defect strength, and supplies an explicit strong optimum plus a full tie-aware linear scan for weak edges. It is neither a one-size example nor a speedup claimed without a structural explanation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
