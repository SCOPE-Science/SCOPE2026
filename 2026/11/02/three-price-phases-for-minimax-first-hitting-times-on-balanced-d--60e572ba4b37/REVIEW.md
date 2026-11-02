# Scientific review

**Claim assessed:** Three price phases for minimax first-hitting times on balanced double stars. The mathematical scope is a balanced \(m\)-leaf-per-hub double star, symmetric continuous-time rates, positive class prices and linear rate budget.

## Correctness — PASS

The proof is a complete all-parameter argument. The source-component edge identity is derived from first-step equations; four averaged ordered-pair formulas give a universal lower bound; Cauchy inequalities with explicitly specified convex-combination coefficients match a feasible solution in each price region, and strict equality conditions show unrestricted uniqueness. The formulas have been checked against 12 exact absorbing-chain computations, 720 randomized dual-certificate cases, 8,640 sampled nonuniform full-edge allocations and 48 threshold continuity checks. Experiments do not replace the proof.

## Originality — PASS, with priority risk

The closest accessible published original, Xu--Yau (arXiv:1312.0065, 2013), develops discrete-time degree-normalized hitting-time identities; the complete relevant sections were read and do not present the rate-budget result. Ghosh--Boyd--Saberi (SIAM Review 2008) optimize total resistance, give analytic tree formulas, and mention maximum resistance as an extension; the accessible manuscript's Introduction and Sections 3.1, 5.1 and 8 were inspected. Neither objective implies maximum **oriented** continuous-time mean hitting with the dual crossing coefficients \(1\) and \(2m+1\). The adjacent path, single-star and double-star-resistance mathematical statements were checked for implication but do not contain the three-phase allocation. Fiedler's 1993 specialist graph-minimax paper could be examined only through abstract/metadata, which remains a residual risk. Semantic database search is corroborative, never absolute proof of novelty.

## Mathematical value — PASS

The balanced double star is a natural two-community tree and the smallest branching topology where within-class travel competes with two asymmetric cross-community hitting directions. It exhibits a bridge-price-independent equal-spoke threshold, a second bridge-sensitive threshold, and an exactly characterized fully asymmetric price phase, all with formulas and unique unrestricted allocations. These are substantive structural transitions, not just a numerical instance or a change of notation.

## Limitations and integrity

The result is not a theorem for unequal community sizes, arbitrary edge prices, discrete-time random walks, resistance diameter, or spectral-gap optimization. Specialist historical overlap risk remains; publication priority is not independently certified. Independent scientific audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
