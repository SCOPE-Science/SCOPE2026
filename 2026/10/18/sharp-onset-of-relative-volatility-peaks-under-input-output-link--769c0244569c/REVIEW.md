# Review: sharp onset of relative-volatility peaks under input-output link changes

## Correctness — PASS
The mean-normalized covariance quadratic under Sherman–Morrison lies on a monotonically traversed affine segment, ruling out strict relative-volatility maxima for any one-coefficient increase. In two sectors the adjugate of every affine input-output pencil is affine; cancellation of the determinant gives the same convex quadratic line argument even for multiple simultaneous changes. A nilpotent three-sector two-edge technology has exact rational risk values at five input intensities which alternate high–low–high–low–high, and the real-analytic rational risk function has at least two strict local minima and one strict local maximum. `verify.py` independently recomputes all five rational values using exact 3x3 linear algebra, and checks the determinant-cancellation claim on a separate instance. Finite calculations certify the example; analytic identities prove the universal obstructions.

## Originality — PASS, with residual risk
Acemoglu, Carvalho, Ozdaglar, and Tahbaz-Salehi (MIT Working Paper 11-23, 2011; Econometrica 2012) derive economic-network shock exposure and aggregate fluctuations, but the materially read primary text does not state a full one-edge/no-peak global shape theorem or its sharp two-link/three-sector counterexample. Sonis and Hewings (1992; 1995) give coefficient-change sensitivity, not demonstrably the relative-volatility threshold; the full 1992 article was inaccessible, and no noncoverage is inferred from the abstract. Kelly, Tyler, and Crawford-Brown (2015/2016) analyze linkage dispersion and infrastructure exposure, but their article uses a different metric. The analytical proof uses classical formulas as inputs and claims novelty only for the classified mean-normalized variance response. Historical equivalent formulations may exist.

## Mathematical value — PASS
A substantive input-output risk question is whether strengthening technical interdependencies can initially diversify, then concentrate, then diversify gross-output shocks. The theorem gives exact rigidity under single-link changes, a dimension bound even under arbitrarily many links in two sectors, and a minimal constructive witness at exactly three sectors and two links. The sharp structural distinction separates mean amplification from relative uncertainty, and the witness has two protected valleys around a relative-volatility peak. It does not assert empirical typicality or GDP consequences.

## Limitations and related literature
Applies to fixed positive mean final demand, finite covariance, productive nonnegative Leontief systems, and gross-output squared coefficient of variation. One older coefficient-change article could not be inspected in full. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
