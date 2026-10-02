# Independent mathematical audit — 2026-10-01

## Final claim

Sharp catalyst-basin dichotomy for an irreversible reaction-diffusion system

## Correctness — PASS

PASS. The proof closes all asymptotic branches under the stated source hypotheses. The quadratic energy of the first and third components dissipates both spatial gradients and the catalyst-weighted reaction gap. Positive-time parabolic regularity justifies gradient decay; Poincare-Wirtinger reduces the first and third components to their means. The energy decomposition forces the catalyst-complement mean to converge, leaving only the positive and boundary equilibrium branches. A mean-zero energy estimate gives convergence of the catalyst field. If initial total catalyst is positive, boundary convergence would eventually make the reaction gap uniformly positive and force exponential growth of the catalyst mean, contradicting its conserved-mass bound. Zero initial catalyst instead gives the invariant catalyst-free face.

## Originality — PASS

PASS. The primary Nguyen-Tang article was inspected in accessible full text around the coexistence discussion. It explicitly states that boundary instability does not rule out a trajectory returning and converging to the boundary, labels that possibility unknown, and formulates global attraction as a conjecture. The audited theorem resolves exactly that open branch and identifies the invariant zero-catalyst face omitted by the literal conjecture. Searches found no later source-specific proof with the same basin decomposition.

### equivalent_formulations

Searches: reaction diffusion catalyst basin dichotomy boundary equilibrium positive catalyst Nguyen Tang exact basin; Nguyen Tang return boundary equilibrium coexistence catalyst

Evidence: The primary paper explicitly discusses possible return to the boundary equilibrium and states the corresponding conjecture.

Reasoning: The audited statement is the precise basin-resolution form of that open return question, with the catalyst-free invariant face separated.

### broader_coverage

Searches: irreversible reaction diffusion boundary equilibria global convergence Nguyen Tang; stability analysis irreversible chemical reaction diffusion 2026

Evidence: The source proves other mass regimes, local positive-equilibrium stability, and boundary instability in the coexistence regime.

Reasoning: Those results do not imply global exclusion of return to the boundary; the paper expressly says so.

### exact_database_or_table

Searches: published mathematical record semantic search exact catalyst basin

Evidence: No database/table is natural; the exact record search found no earlier matching basin theorem.

Reasoning: The claim is a continuum dynamical theorem rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: doi:10.1007/s00033-026-02847-0 coexistence theorem; arXiv:2410.22928 boundary equilibrium conjecture

Evidence: The source's local theorem gives exponential convergence only after entering a neighborhood; its instability theorem does not preclude later return.

Reasoning: The audited global mean argument supplies the missing implication from positive catalyst mass to positive-equilibrium selection.

## Scientific value — PASS

PASS. The exact basin boundary is a natural global-dynamics question explicitly left open in the motivating primary paper. The theorem converts local instability plus the Lyapunov identity into a complete coexistence-regime selection result and sharpens the conjecture by isolating the necessary invariant-face exception.

## Source inspections

- **Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria** — https://doi.org/10.1007/s00033-026-02847-0. Material read: Accessible full-text sections containing the coexistence equilibria, local stability and instability results, discussion of possible return to the boundary, and the global-attraction conjecture. Assessment: PRIMARY_SOURCE_EXPLICITLY_LEAVES_CLAIM_OPEN. Evidence: The article says boundary instability alone cannot rule out later convergence to the boundary and formulates global attraction as a conjecture.

## Limitations and residual risks

Restricted to the catalytic system with homogeneous Neumann boundary conditions, bounded classical solutions in the source setting, and the coexistence regime from the source. The equilibrium-collision endpoint and the source paper's second network are not covered. The global argument is qualitative; the eventual exponential rate invokes the source's local theorem.

- The proof relies on the source paper's global boundedness and regularity hypotheses and local exponential-stability theorem exactly as stated.
- The result does not treat the equilibrium-collision endpoint.

## Disposition

**passed**
