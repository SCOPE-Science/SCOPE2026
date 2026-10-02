# Independent audit — 2026-10-01

## Final claim

Positive Neumann steady patterns at a degenerate porous-diffusion resonance

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

The stated coefficient identities make \(V=\alpha U\) an exact stationary reduction. The scalar equation \((UU_x)_x-b(U-U_-)(U-U_+)=0\) has the displayed first integral; when \(U_->U_+/2\), the center-to-homoclinic period annulus stays in \(U>0\), with half-period tending to \(L_c=\pi\sqrt{U_-/(b(U_+-U_-))}\) at the center and to infinity at the separatrix, so continuity yields a positive nonconstant Neumann profile for every \(L>L_c\). Independent symbolic recomputation for the source example reproduced \(\det(J_- -\mu D_-)=3(\mu-1)^2/4\), trace \(-2\mu-4\), the positive upper-state determinant, and the expansion \(y_{xx}+y-14y^2+56y^3+O(y^4)=0\), giving the stated half-period coefficient \(182/3\).

## Originality

The primary paper explicitly says that nonconstant steady-state solutions satisfying zero Neumann conditions exist but that their search and analysis lie beyond its scope. It does not give this proportional reduction, the all-length existence theorem, the \(L_c\) threshold, or the perfect-square dispersion touch. A nearby 2026 degenerate predator-prey bifurcation paper treats a different Allee-effect model and ordinary Turing/Turing-Hopf phenomena.

### Equivalent formulations

Searches:
- Resultary semantic search for proportional porous-diffusion Neumann steady patterns and degenerate Turing resonance
- Web searches on the exact source title with nonconstant steady states, zero Neumann, stationary patterns and resonance

Evidence:
- The primary paper itself states the steady-pattern problem is beyond scope; no matching theorem for its coefficient family was found.

Reasoning: The stationary theorem is not equivalent to the source's time-dependent exact solutions satisfying a one-sided Neumann condition.

### Broader coverage

Searches:
- Cherniha and Kriukova, DOI 10.3390/axioms14090655 full text
- Yang and Fan, DOI 10.1002/mma.70728

Evidence:
- Cherniha-Kriukova analyze homogeneous stable nodes and time-dependent exact solutions, then explicitly defer nonconstant zero-Neumann steady states; Yang-Fan study a different degenerate predator-prey model with Allee effects.

Reasoning: General phase-plane and Turing bifurcation theory provide tools but do not state the source-specific invariant line, domain threshold or degenerate dispersion identity.

### Exact database or table

The claim is a proof about a continuous boundary-value problem, not a known-table recomputation.

Searches:
- Resultary and web searches for the exact \(L_c\), \(\mu=1\) double determinant touch, and source coefficient tuple

### Claim versus prior implication

The final theorem is a substantive completion of the source's deferred stationary analysis, not an immediate restatement of its homogeneous stability computation.

Evidence:
- The source states existence in general terms but supplies neither the proportional stationary reduction nor existence for every \(L>L_c\); the latter requires the first-integral/period argument.

### Source inspections

- **A Reaction-Diffusion System with Nonconstant Diffusion Coefficients: Exact and Numerical Solutions** — INPUT_NOT_COVERING. Material read: Full-text steady-state analysis, zero-Neumann exact-solution discussion, the source example, and the paragraph stating nonconstant zero-Neumann steady states are beyond scope. Evidence: The paper explicitly defers the search for and analysis of nonconstant steady states satisfying zero Neumann conditions. Source: https://doi.org/10.3390/axioms14090655
- **Bifurcation Analysis of a Predator–Prey Model With Degenerate Diffusion and Multiple Allee Effects in Predators** — DIFFERENT_MODEL_NOT_COVERING. Material read: Abstract and model scope. Evidence: It studies Allee-effect/hunting-cooperation dynamics and Turing/Turing-Hopf bifurcations, not the Cherniha-Kriukova proportional family. Source: https://doi.org/10.1002/mma.70728

### Residual risks

- Generic nonlinear-diffusion stationary-pattern literature is broad, but no source was found that implies this exact proportional family and all-length threshold.

## Value

The theorem answers a source-stated open stationary problem, gives a sharp small-amplitude domain scale and infinitely many positive pure-Neumann patterns, and explains how nonlinear steady structure can coexist with a dispersion determinant that only touches zero instead of producing a conventional Turing-unstable interval.

## Limitations

Only one-dimensional stationary pure-Neumann profiles are proved; temporal stability and classification of all stationary states are not established, and the all-length statement uses \(U_->U_+/2\).
