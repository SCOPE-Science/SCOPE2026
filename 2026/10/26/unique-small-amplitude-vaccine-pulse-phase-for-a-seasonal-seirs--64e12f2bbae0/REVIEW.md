# Scientific assessment: weak-pulse seasonal SEIRS invasion timing

## Correctness (C): PASS
The disease-free susceptible orbit and its jump condition are solved exactly. At the constant baseline the exposed/infectious linearization has a simple dominant real eigenvalue. Eliminating the exposed stage yields a Hill equation, and a periodic logarithmic-derivative Riccati equation provides an analytic perturbation expansion. The first two harmonics produce the explicit \(\epsilon\eta\) coefficient. Its prefactor is strictly positive for all allowed parameters, and the uniform \(C^2\) phase remainder proves exactly one annual minimum and one annual maximum for sufficiently small positive amplitudes. `verify.py` checks concrete Floquet coefficients and their predicted ordering independently of the analytic derivation. The finite checks are not substituted for the general proof.

## Originality (O): PASS, with stated residual risk
The motivating full 2024 SEIRS paper numerically compares selected vaccine phases and favors a rising-season inflection at finite pulse strength; it does not derive the joint weak-amplitude principal Floquet perturbation or uniqueness theorem. The older Onyango–Müller SIR literature optimizes a scalar seasonal invasion threshold and is credited; its scalar result does not imply a two-stage SEIRS result without a new noncommuting matrix analysis. Primary 2005 SEIRS periodic-control and 2014 impulsive SEIR extinction results address thresholds without the claimed continuous phase asymptotic. A 2026 SIRVS seasonal optimal-vaccination paper and 2019 constrained optimal-control work have different admissible controls and objectives. Full original texts of the 2014 Onyango–Müller and 2019 Wang studies were inaccessible, and concealed stronger coverage remains a real priority risk. Successful published-record searches found related but not covering statements; negative searches do not certify priority.

## Value (V): PASS
An existing biologically motivated SEIRS study reports that vaccine timing near rising seasonal transmission is favorable but offers only sampled phase simulations. An exact quantified law locates the unique locally invasion-optimal annual pulse, specifies the dependence on demographic susceptible replenishment, and proves that exposed and infectious stage times influence the improvement magnitude but not the leading phase. This can guide numerical sensitivity analyses and separates the invasion objective from cumulative infections and vaccine cost.

## Scientific boundaries
Small amplitudes \(\epsilon,\eta\) simultaneously; one instantaneous annually recurring pulse, no baseline susceptible vaccination, homogeneous deterministic fractions, sinusoidal transmission, linear disease invasion. No guarantee at the 2024 paper's finite amplitude or for nonlinear total case counts. Publication priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
