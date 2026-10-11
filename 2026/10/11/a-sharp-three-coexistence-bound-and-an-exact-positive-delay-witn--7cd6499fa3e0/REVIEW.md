# Scientific review

## Correctness: PASS

The elimination defines \(z\in(0,1)\), reconstructs every strictly positive equilibrium bijectively, and reduces the only remaining equation to a degree-at-most-four polynomial. Opposite endpoint signs for \(\mathcal R_0>1\) exclude four distinct physical roots. For \(\mathcal R_0\le1\), the positive vector balance gives the opposite inequalities \(U>aK\) and \(U<aK\). For the positive-delay witness, four disjoint rational sign changes isolate the complete degree-four zero set; only three intervals lie in the physical range. Symbolic identities and rational signs replay with `check_equilibria.py` and do not substitute experimental finite sampling for the analytic bound. Limitation: no dynamical stability theorem is asserted.

## Originality: PASS

The closest source is Al Basir–Blyuss–Venturino (2023), eqs. (2.3), (3.1), Theorem 2. Its quartic and restricted one-root criterion do not themselves give the global physical bound with realized maximal triple multiplicity under two strictly positive delays. Venturino–Roy–Al Basir–Datta (2016), §3.1, already discusses the **possibility** of three positive formal polynomial roots for the same zero-delay interactions, without showing an exact feasible three-equilibrium parameter vector or proving the sharp bound for the delayed system. Accordingly no priority is claimed for merely noticing that multiplicity is possible. The 2020 two-delay paper uses constant recruitment rather than vector carrying capacity proportional to total plant biomass; its equilibrium analysis is not stronger coverage. Focused literature and published-finding searches found no directly dominating result. Residual risks: indexed search cannot establish absolute priority, and a hidden source may cover the constructive feasible example.

## Value: PASS

Maximum feasible equilibrium multiplicity is a natural structural question for a model whose source gives only one-root sufficient conditions. The proof closes the algebraic-versus-biologically-positive gap and determines a sharp, attained cutoff for *all* delay lengths. An exact positive-delay witness with simple roots, rather than a numerical scan or a special zero-delay degeneration, shows that three physical branches occupy a nonempty open parameter region. Such branch multiplicity is a relevant prerequisite for a global bifurcation diagram, while stability and basin consequences remain unproved.

Same-model review: passed. Independent audit: not yet performed.
