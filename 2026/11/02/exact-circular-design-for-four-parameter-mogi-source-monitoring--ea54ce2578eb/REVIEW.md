# Scientific review: exact circular Mogi monitoring design

## Correctness — PASS

The claim is a local four-parameter, three-component, equal-Gaussian-noise Fisher D-optimality statement under a common station radius. The Mogi forward-model Jacobian has been differentiated independently and its ten unique inner products are displayed in `RESULT.md`. Angular rotational averaging bounds the determinant, with attainable equality at every regular polygon with at least three stations; strict concavity and the explicit first/second angular blocks characterize all angular optima. The balanced Fisher determinant is positive for nonzero source strength and positive radius. The derivative of its one-dimensional radius profile is factored exactly, and its sign proves one global radial maximizer. The accompanying executable checked four-station and three-station Fisher blocks, the determinant, a strict angular-loss example, and the radial polynomial identity. No numerical sampling is used as proof of the global result.

## Originality — PASS, subject to historical priority

Mogi's displacement field, the use of three-component GPS to infer four source parameters, and general Fisher D-optimality are established prior methods. Masterlark (2007; DOI: 10.1029/2006JB004860) treats physical departures from the ideal Mogi model; Fournier, Freymueller and Cervelli (2009; DOI: 10.1029/2008JB005837) study source-position/strength estimation and uncertainty for an observed GPS network. The inspected primary sections do not present the exact common-radius Fisher determinant, necessary-and-sufficient angular moment conditions, or algebraic global optimal radius. A 2008 USGS station-placement simulation report is closer in application, but its complete PDF could not be accessed. A distinct exact analysis of coaxial Mogi-source peak splitting concerns a different objective. Targeted equation-, alias- and implication-level searches found no equivalent or strictly covering theorem. An unlocated exact special-case design and consequences of more general invariant-design theorems remain plausible priorities, not verified absences.

## Mathematical value — PASS

This is a complete experimental-design classification for a natural restricted geometry: any number of equally noisy full-vector instruments on one selectable radius. It separates a universal angular balance criterion from a unique physically dimensioned radius, jointly estimating depth, strength and two unknown horizontal coordinates. The polynomial radius and the sufficiency/necessity of two angular harmonics are reusable benchmarks for simulation-based volcano-monitoring network placement. It does not claim optimality among arbitrary mixed-radius arrays, unequal/colored noise models, or field networks with topography, elastic heterogeneity and constrained access. The application is mathematical, not a validated deployment recommendation.

## Closest literature and residual limits

Masterlark (2007) cautions that model error may dominate precision; Fournier et al. (2009) use four-parameter Mogi inversion with observed and bootstrap network uncertainties; USGS Scientific Investigations Report 2008-5114 describes network placement/uncertainty simulations. These sources support the motivation and model but do not, in the material inspected, imply the exact joint theorem. The strongest unresolved historical comparison is the inaccessible full 2008 report and potentially other specialized survey-design results. The determinant maximizes local information, not global nonlinear inverse precision.

Self-review: passed. Independent audit: not yet performed.
