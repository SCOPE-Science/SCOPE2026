# Same-model review

## Correctness

PASS. The proof starts from the two printed prey equations with the predator coordinate set to zero. The infected-prey balance gives \(x=\nu(\alpha+y)/\beta\) exactly. Substitution into the susceptible-prey balance produces a quadratic. Its factor form immediately excludes positive roots when \(\beta K\le\alpha\nu\); when \(\beta K>\alpha\nu\), the sign of the constant term after multiplying by \(-1\) forces exactly one positive root. A symbolic checker reconstructs the identity and verifies exact feasible and infeasible examples.

## Originality

PASS. The primary 2024 paper prints a cubic Eq. (4), a sign table allowing three positive predator-free endemic roots, and Proposition 1 with condition \(\beta>\nu\alpha\). Exact-title, DOI, author, threshold-parameter, and model-family searches located no correction containing the quadratic classification. An older open Crowley--Martin disease-in-prey paper proves uniqueness for a different predator-absent SIS model, which does not imply the present saturated-incidence result. A 2019 nonlinear-incidence predecessor is a residual risk because only its abstract was accessible.

## Value

PASS. The result replaces a multiple-root boundary-equilibrium classification by a sharp invasion threshold and a unique branch. It also supplies a direct positive-parameter counterexample to the source's stated sufficient condition, so the correction affects biological feasibility and the boundary phase portrait.

## Closest literature and limitations

The closest fully inspected comparison is Naji and Hasan (2012), which has a predator-absent SIS subsystem with a unique endemic state but different incidence and recovery terms. Mortoja, Panja, and Mondal (2019) is closer in model ingredients but was not fully accessible. The accepted claim is therefore restricted to the exact predator-free equilibrium equations printed by Sarwardi et al. (2024); no claim is made about the interior equilibrium or Hopf calculations.

Same-model review: passed. Independent audit: not yet performed.
