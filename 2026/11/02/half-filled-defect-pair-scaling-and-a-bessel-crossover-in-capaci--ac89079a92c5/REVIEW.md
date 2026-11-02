# Scientific review of the capacity-two exclusion crossover theorem

## Correctness: PASS

The claim uses a fixed total particle number on a capacity-two ring. The source's precise site weights are \((t,1+t,1)\), leading to the multinomial double-occupancy law through the invariant ratio \(z=t/(1+t)^2\). The exponential-family derivative proves finite-size strictness, the hypergeometric conditional sampling law gives its exact maximum, and strictly concave Stirling asymptotics prove thermodynamic concentration. The critical quadratic gives the continuous square-root crossover. Fixed integer doping and \(z=a/L^2\) admit a summable dominating sequence, rigorously giving the order-\(|k|\) Bessel distribution and its moment formula. The accompanying code verifies the small-state generator directly and passes 414 checks. Risks: the proof is scoped to these precise stationary and limiting settings; finite-state checks alone do not certify convergence.

## Originality: PASS, qualified

Ayyer–Misra's original source already establishes the stationary distribution, reciprocal-parameter symmetry and canonical partition function. Those are not claimed as new. Its Section 4 analyzes *most probable occupation*, not the strict variance and Bessel defect scaling asserted here. Evans–Waclaw provide the general misanthrope factorization criterion and condensation framework, with no matched two-capacity finite-size rare-pair formula in the examined paper. The facilitated ASEP literature has different jump constraints and stationary measure. Exact-claim, equivalent-reparameterization and broader-implication searches located no explicit covering finite-size crossover. Risk: special functions and canonical defect-pair distributions occur elsewhere in statistical mechanics; an unlocated equivalence could affect priority. Database and literature searches cannot prove novelty.

## Mathematical value: PASS

At integer filling, the zero-deformation limit concentrates on exactly one particle per site. There are two physically distinct ways to leave that limit: a continuous doping window of width \(\sqrt z\) and a finite-particle-number window with rare vacancy–double-occupancy pairs. The theorem rigorously identifies both and the complete order-\(|k|\) Bessel count in the latter, including sharp variance coefficients. The finite-site monotonicity locates the unique fluctuation optimum. These exact, naturally matched scale regimes are motivated by the onset of occupancy defects rather than arbitrary parameter slicing. No claim of a finite-parameter phase transition or extension to larger capacity is made.

## Closest literature and limitations

A. Ayyer and S. Misra, *An exactly solvable asymmetric K-exclusion process*, arXiv:2310.03343 (2023), Sections 2–4. M. R. Evans and B. Waclaw, *Condensation in stochastic mass transport models: beyond the zero-range process*, arXiv:1312.5642 (2013), Sections 1–3. The theorem is stationary, fixed capacity two, and only covers the two explicitly stated asymptotic limit procedures. Independent publication-priority checking and independent mathematical auditing remain outstanding.

Self-review: passed. Independent audit: not yet performed.
