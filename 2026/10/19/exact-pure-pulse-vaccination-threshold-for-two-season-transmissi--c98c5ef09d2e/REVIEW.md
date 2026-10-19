# Scientific review: exact pure-pulse vaccination threshold

## Correctness
**PASS.** The susceptible orbit and adjoint boundary conditions were reconstructed for a periodic positive measure. Exact formulas for the two one-sided marginal derivatives lead to necessary endpoint inequalities. Strict negative curvature of the switching value in the high season and one-sided monotonicity in the low season show those inequalities are sufficient globally. Previously established strict convexity ensures that the first-order global condition identifies the unique minimizer. An independently coded two-pulse integration reproduced the marginal value calculations and the square-wave threshold. The calculation concerns log-dose atoms, not vaccinated fractions.

## Originality
**PASS, within the searched record and stated scope.** The 2026 motivating primary paper, fully inspected in its seasonal square-wave and discussion sections, reports a transition around vaccination effort \(0.4\) numerically rather than proving its exact location. The same authors' 2026 analytical paper establishes the general strictly convex functional and first-order characterization; this is explicitly prior mathematics, and not presented as new. The new claim is the exact closed-form necessary-and-sufficient transition throughout the two-season positive-parameter family plus the side-selection inequality. Searches of relevant mathematical records and closely related vaccination literature did not identify that specialization. Residual uncertainty remains for unindexed or inaccessible equivalent findings; the general source may make the derivation feasible but does not state the resulting cutoff.

## Mathematical value
**PASS.** The motivating paper presents pure-pulse optimality near its numerical boundary as an empirical feature of optimization output. This result locates the boundary exactly, proves optimality against arbitrary periodic nonnegative measures rather than discretized schedules, and discovers two distinct ways a pure pulse can cease to be optimal. It is a transparent control parameter that can be used as a benchmark for analytic and discretized seasonal vaccination policies. It does not resolve the optimal mixed schedule beyond the threshold or nonlinear epidemic behavior.

## Literature and limitations
Gavish–Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission* (2026), DOI 10.1007/s11538-026-01741-0, Sections 7 and 9; Gavish–Katriel, *Optimal Regulation in a Time-Periodic Environment: Insights from a Simple Model* (2026), DOI 10.1007/s00245-025-10374-z, Sections 2 and 4. The proof depends on the stated susceptible waning dynamics and the all-at-once dosing convention. A related broader equivalence not indexed by searches cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
