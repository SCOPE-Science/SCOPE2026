# Independent mathematical audit

## correctness

PASS

For N=d+1 real finite-metric points with sole distance 0<t<=1 shortened, the primal transport norm is m-(1-t)min(|x0|,|x1|) exactly when x0 and x1 have opposite signs; otherwise m. A positive-negative sign chamber has equilateral volume binomial(d-1,p-1)/d!, and the short-edge opposite-sign chambers universally expand by 1/t, proved using U=min(A,B) with survival (1-u)^(d-1) and exact integral. Vandermonde yields vol P=binom(2d,d)/d! [d+(d-1)t]/[(2d-1)t]. In polar Q1, ordering of N potential values gives (d+1)! unit-gap simplices; the distinguished difference has beta-mixture density 2[d-(d-1)u]/(d+1). Restricting |f0-f1|<=t yields vol Q=t[2d-(d-1)t]. Differentiate product: M_d proportional to [d+(d-1)t][2d-(d-1)t], unique maximum t=d/[2(d-1)] for d>=3, exact gain and 1/8 asymptotic. Independently checked both closed profiles using exact rational identities d=2..15 and SciPy geometric primal/polar computations d=2,3,4 at t=1/2,3/4,1; finite hull topology does not replace analytic proof.

## originality

PASS

Alexander--Fradelizi--Garcia-Lirola--Zvavitch (2019) already give equilateral t=1 product and qualitative nonmaximality, explicitly credited. Their Theorem 5.8 does not entail this one-edge exact primal/polar profile, interior maximizing t or limiting gain. Matching-shortening published result computes facets only; exactly identical four-site one-edge deformation published result computes Hilbertian Banach--Mazur distortion, a different invariant. Best-of-knowledge PASS, recognizing unindexed weighted-root-polytope volume literature risk.

## value

PASS

The theorem quantifies a natural one-edge perturbation of canonical equilateral finite metrics, obtaining closed primal and polar volumes, a genuinely interior sharp Mahler maximum for every d>=3 and a nonzero limiting 12.5% relative improvement. It strengthens the earlier qualitative nonmaximality result without falsely claiming global Mahler extremality over all metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
