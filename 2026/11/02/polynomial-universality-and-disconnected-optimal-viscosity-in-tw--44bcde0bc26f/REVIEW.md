# Scientific review: polynomial universality in two-guru viscosity

## Correctness

**PASS.** The claim is exact for finite, fixed, acyclic delegation forests with two independent gurus and fair random ties. The coefficients of any integer polynomial vanishing at both viscosity endpoints are realized as differences of nonnegative level populations, with a unit baseline at each nonempty level. Equality of the total sizes follows from the endpoint condition. The probability of correct choice is the competence of the heavier guru, or the mean competence at a weight tie. The explicitly factored polynomials therefore establish an arbitrary number of separate global-optimum intervals and a fixed-grid accuracy gap of at least \(1/10\). A star and a three-vertex path establish the six-voter strict-interior example. The all-forests size-five lower bound is proved by separately considering the possible counts of gurus and the corresponding weighted-majority rule; any interior threshold is handled by fair averaging, so cannot exceed both endpoint accuracies. A standalone standard-library Python verifier performs exact rational tree construction and checks, plus a complete labeled-forest enumeration through five voters. Finite checks are corroboration, not substitutes for the universal polynomial and lower-bound arguments.

## Originality

**PASS with residual specialist-priority uncertainty.** Armstrong, Alouf-Heffetz and Talmon (arXiv:2405.06698, IJCAI 2024) introduce the exact viscosity-weighted epistemic voting framework, explain its piecewise-constant group-accuracy objective, and exhibit an interior optimum using nine gurus. Those observations are not claimed as new. The inspected primary statements do not assert realization of *every* integer polynomial with zero endpoint values by just two gurus and equal component sizes, nor an unbounded number of disjoint global-optimum intervals, a predetermined-grid impossibility gap, or the sharp size-six minimum. Boldi et al. (2011) establish attenuated path and ranking ideas, but the inspected relevant material does not supply this accuracy-universality theorem. Published mathematical-record searches and accessible prior claims yielded no equivalent statement; the search cannot prove absolute publication priority. General results on prescribed polynomial zero patterns or Katz-score rank crossings may imply a portion of the realization construction, and further specialist checking remains worthwhile.

## Mathematical value

**PASS.** The structural realization lemma answers a natural expressivity question in a model where the viscosity parameter is intended to tune collective decision accuracy. It shows no uniform bound on the number of accuracy-optimal parameter windows even on two-root forests; preselected finite grids can miss a constant accuracy improvement, while a six-voter example gives the exact first population size where both endpoint policies lose to an interior choice. These are concrete boundaries for parameter tuning and delegation-network design, not arbitrary coefficient enumeration. The finding deliberately does not rule out input-aware exact optimization algorithms.

## Closest literature and scope

1. B. Armstrong, S. Alouf-Heffetz, N. Talmon, *Optimizing Viscous Democracy*, arXiv:2405.06698, first public 2024-05-08, https://arxiv.org/abs/2405.06698 ; https://doi.org/10.24963/ijcai.2024/292 . Read the published full-text sections on viscosity weights, accuracy, and pathological parameter choices.
2. P. Boldi, F. Bonchi, C. Castillo, S. Vigna, *Viscous Democracy for Social Networks*, Communications of the ACM 54(6), 2011, pp. 129–137; author manuscript https://chato.cl/papers/boldi_bonchi_castillo_vigna_2011_viscous_democracy_social_networks.pdf . Read relevant path-weight, parameter and score-ranking material; this does not amount to an exhaustive priority investigation of all later Katz applications.
3. The MSC2020 classification 91B12 (Voting theory), https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=91B72 .

The claim does not treat cyclic delegations, endogenous or strategic changes to the fixed forest, correlated guru opinions, multiple alternatives, different tie-breaking, or realistic branching restrictions. The two-guru construction may be large. Independent external audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
