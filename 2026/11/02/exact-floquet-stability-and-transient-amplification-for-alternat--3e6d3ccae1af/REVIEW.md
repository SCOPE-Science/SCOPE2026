# Scientific review

## Correctness

PASS. The recurrence is reconstructed from genuine unequal time nodes, its Floquet cubic is checked by exact symbolic arithmetic, and four real-cubic Schur inequalities are proved with explicit coefficient bounds. At the boundary the simple unit multiplier and the strict stability of the other two multipliers follow from the quadratic factor. A real multiplier greater than one certifies instability beyond the boundary. The ratio phase diagram and the sharp one-step amplification are then direct consequences. The embedded verifier confirms the algebra and independently checks hundreds of cases, but finite experiments are not used to prove the universal theorem.

## Originality

PASS on inspected and accessible evidence, with a stated priority risk. Grote–Mitkova (2011, arXiv:1109.4480) work with constant-step Adams coefficients and spatial local substepping. Hadjimichael–Ketcheson–Lóczi–Németh (2015, arXiv:1504.04107) address optimal SSP multistep formulas, not the negative-real Floquet spectrum of fixed interpolatory AB3. Marciniak–Jankowska (2019, DOI:10.1007/s11075-019-00774-y) develop interval enclosures, not this scalar stability phase diagram. Related older Adams/Nordsieck works by Gear–Tu, Skeel–Jackson and Calvo–Lisbona–Montijano are material priority risks: full text for Calvo–Lisbona–Montijano (1989) was not accessible. None of the inspected material provides a covering implication. Absence from keyword searching alone is not novelty evidence.

## Value

PASS. The exact two-component stable-ratio regions, sharp 10% improvement in mean negative-real stability ceiling, and unbounded one-step perturbation amplification expose a concrete tension between spectral stability and usable adaptive-stepping robustness. This is a natural numerical-ODE stability question for a commonly used interpolatory method, not an arbitrary parameter slice. The result gives complete positive-step classification in this motivated periodic setting and a counterexample to interpreting improved Floquet stability as uniform transient safety.

## Scope and limitations

The theorem applies to the scalar real-negative test eigenvalue, period-two interpolation, and unrestricted histories. It makes no claims for nonlinear PDEs, complex spectra, nonperiodic grids or an SSP property. The contrast endpoint is a nonattained supremum. The 1989 specialist full-text priority comparison remains unresolved; the scientific assessment is not independent validation.

Self-review: passed. Independent audit: not yet performed.
