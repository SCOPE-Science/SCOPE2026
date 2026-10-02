# Independent scientific audit — SCOPE-20260920-05dd465b6b5b

Audited at: 2026-10-01T19:12:08.377982Z

Disposition: **passed**

## Correctness — PASS

Direct differentiation of \(J=yz+\frac a2y^2+\frac c2x^2-\frac13x^3\) along the Genesio flow gives exactly \(\dot J=z^2-b y^2\); the symbolic artifact independently reduces the residual to zero. Time averaging on bounded forward orbits gives the Cesàro balance, and integrating the generator against a compact invariant measure gives the same moment identity together with the stated mean constraints. For \(b\le0\), \(-J\) is nonincreasing with derivative \(-z^2+b y^2\le0\); LaSalle on a bounded omega-limit set leaves only equilibria, giving convergence to one equilibrium. For a nonconstant periodic orbit the balance and sharp Wirtinger inequality give \(P\ge2\pi/\sqrt b\); equality forces a pure first harmonic, and substitution leaves a nonzero second harmonic \(-R^2/2\), so the inequality is strict.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_genesio_balance.py
- Valls 2025 full text

### Correctness risks

- The convergence statement is conditional on forward boundedness and does not prove ultimate boundedness of arbitrary trajectories.

## Originality — PASS

The fully searchable Valls 2025 primary paper treats the phase portrait at infinity, Hopf bifurcations, and integrability and states the small-orbit Hopf period \(2\pi/\sqrt b\), but it contains no invariant-measure theorem, no Wirtinger minimum-period theorem, and no bounded-orbit \(b\le0\) recurrence barrier. Umut 2013 is explicitly a stability/region-of-attraction paper; its full theorem text and Barbasin's 1952 Russian article were not accessible, so they remain named risks for an auxiliary Lyapunov identity, not decisive coverage of the new global consequences.

### Equivalent formulations

The searched stability and Hopf results are not equivalent to these recurrence and invariant-measure statements.

### Broader coverage

Neither inspected material implies the invariant-measure identities or the sharp strict period bound; Valls's local Hopf period instead confirms local sharpness of the constant.

### Exact database or table

The result is analytic and dynamical rather than a tabulated quantity.

### Claim versus prior implication

The audited polynomial balance plus generator/Wirtinger arguments add genuinely different global consequences.

### Sources inspected

- Global dynamical aspects and integrability analysis of the Genesio system — https://doi.org/10.3934/dcdsb.2025016. NOT_COVERING: No invariant-measure, Wirtinger, or bounded-orbit recurrence theorem matching the assigned claim appears in the inspected text.
- On the stability of Genesio system — 2013 Far East Journal of Dynamical Systems 23(1). INACCESSIBLE_PLAUSIBLE_SOURCE: It may contain a related Lyapunov identity, but the available description is about stability and attraction regions rather than the assigned invariant-measure and minimum-period conclusions.
- On the stability of the solution of a certain nonlinear equation of third order — Barbasin, Prikl. Mat. Meh. 16 (1952), 629-632. INACCESSIBLE_PLAUSIBLE_SOURCE: A possible overlap in the auxiliary identity remains a risk, but it cannot override the absence of evidence for the Genesio-specific invariant-measure and sharp-period theorem.

### Checked sources

- https://doi.org/10.3934/dcdsb.2025016
- Umut 2013 stability article abstract
- Barbasin 1952 bibliographic record
- Resultary semantic search

### Residual risks

- Barbasin 1952 and the full Umut 2013 theorem text were not inspected and may contain an equivalent auxiliary Lyapunov identity.
- The originality claim is centered on the combined Genesio-specific invariant-measure, bounded-recurrence, and strict period-floor consequences rather than priority for the raw polynomial identity alone.

## Value — PASS

The theorem gives exact recurrence diagnostics for a standard chaotic model, a rigorous obstruction to non-equilibrium bounded recurrence for \(b\le0\), and a strict universal period floor whose constant is attained asymptotically at the known Hopf frequency. These are motivated dynamical boundaries, not arbitrary calculations.

### Value sources

- https://doi.org/10.3934/dcdsb.2025016
- Umut 2013 stability article abstract

### Value risks

- The bounded-orbit convergence result is conditional on boundedness and therefore does not classify all forward trajectories.

## Limitations

- The convergence theorem is conditional on forward boundedness and does not establish ultimate boundedness.
- Compact support is required for the invariant-measure generator identities.
- The full texts of Barbasin 1952 and Umut 2013 were not accessible, leaving a specific auxiliary-identity priority risk.
