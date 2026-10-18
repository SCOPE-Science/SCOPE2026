# Scientific assessment

## Correctness

PASS. The argument is for the exact mean-field ODE in equation (2.1) of Cao and Gong. Reflecting endpoints, mass conservation, and the deficit-coordinate transformation are explicit. The rank-one first-row linearization gives eigenvalues \(-(1-1/(2k))\) and \(-1\); exact positive left coefficients yield a nonvanishing slow amplitude. The nonlinear error is quadratic and the stable flow is exponentially small, so the logarithmic-amplitude correction is integrable. For more than three opinions, the source at the far extreme is integrable after multiplying by \(e^t\); descending exact integrating-factor identities then give all polynomial powers and factorial coefficients. The three-opinion boundary has nonintegrable resonant forcing and a different exact limit. Exact symbolic Jacobian/remainder checks for five opinion radii and numerical diagnostics for three radii were replayed from the provided verification program. Their finite range is not a substitute for the proof.

## Originality

PASS with historical-priority uncertainty. Direct inspection of Cao–Gong arXiv:2605.28984, especially (2.1), Proposition 3.2, Theorem 2, Theorem 3 and its Section 4 open questions, finds convergence regions and a weak three-state upper rate, but not exact all-radius decay amplitudes or the polynomial minority cascade. Nearby earlier Cao–Reed (2025) and Cao–Cortez (2025) papers use different opinion update rules. Existing related historical records address the same source's exploration-regularized model and its unstable uniform equilibrium, not the approach to the stable extreme and remote minority hierarchy. The scalar stable eigenvalue is a standard local linearization consequence; the substantive strict positive constants and joint hierarchy are not asserted to be novel in isolation from the complete theorem. Search limitations and the risk of an unidentified general triangular-flow asymptotic theorem remain.

## Value

PASS. Quantifying convergence for general integer opinion radius is an explicit open mathematical direction in the motivating paper. The theorem distinguishes the aggregate rate of near-consensus disagreement from the faster, polynomially structured survival of more distant opinions. It also discovers a dimension-specific resonance in the three-state model. These are natural observables within the original opinion system, not arbitrary numerical cutoffs or renamed generic bounds.

## Boundaries

Proven only for deterministic mean-field trajectories actually converging to one extreme, including known sufficient initial-mean basins. No global basin classification, finite-population absorption estimates, or independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
