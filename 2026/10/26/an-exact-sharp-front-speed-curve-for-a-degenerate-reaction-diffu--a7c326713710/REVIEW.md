# Review

## Correctness

The profile is checked by substituting it into the traveling-wave ODE. The residual reduces to a quadratic polynomial in the profile value; its three coefficient equations give the wave speed and the necessary-and-sufficient parameter relation. The interface fluxes match, so the piecewise profile is a weak solution. The symbolic verification script independently checks the algebraic identities. The proof does not claim more than the exponential-front ansatz.

## Originality

The closest primary source studies the same degenerate reaction–diffusion–advection family and presents numerical sharp-wave-speed exploration. The exact curve \(k=3eta\lambda_eta\) and profile derived here were not found in the sections inspected. General Abel-based exact-wave methods are relevant, but their explicit cases inspected do not state this curve. This is a bounded novelty assessment, not a claim of exhaustive novelty.

## Value

The curve supplies an exact benchmark for checking phase-plane and numerical computations of sharp fronts in a model where the cited study emphasizes numerical wave-speed exploration. The complete if-and-only-if statement is limited to the natural exponential-front ansatz; it is not a general classification of all traveling waves.

## Closest literature and limitations

- Sánchez-Garduño and Pérez-Velázquez (2016), DOI 10.1155/2016/5620839: same model family; numerical speed exploration for nonlinear degenerate advection.
- Harko and Mak (2015), arXiv:1510.08163v1: general Abel-equation approach with exact solutions under specified integrability conditions.
- Sherratt (2010), DOI 10.1051/mmnp/20105505: smooth-front asymptotics for the boundary case with diffusion \(D(u)=u\) and no nonlinear advection.

The main residual risk is that a broader exact-wave method may implicitly encode the same parameter curve. No claim is made about wave stability, attraction, or exclusion of other profiles.

Self-review: passed. Independent audit: not yet performed.
