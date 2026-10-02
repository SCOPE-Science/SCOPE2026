    # Independent mathematical audit — 2026-10-01

    ## Record

    **Finite Euler step profiles converge to a universal self-similar rectangle**

    Disposition: **PASSED**.

    ## Correctness — PASS

    The endpoint argument is valid under the stated finite positive-step hypotheses. Proposition 2.4 of the motivating Euler paper gives the rightmost-endpoint scale and integrability of every other endpoint; positivity and monotonicity turn integrability into \(t x(t)\to0\). Substitution into the exact endpoint ODE gives \(b_n'=-c_*b_n^2(1+o(1))\), hence \(t b_n\to c_*^{-1}\). The mass, weighted moment, scaled-profile, and Green-kernel limits then follow by finite-step Taylor expansion and dominated convergence. The inspected numerical artifact is consistent with, but is not used in place of, this proof.

    ## Originality — PASS

    Best-of-knowledge originality survives. The motivating paper proves comparability, weighted-moment decay, and endpoint integrability, while the earlier relaxation paper gives qualitative finite-jump relaxation. Neither inspected statement gives the exact coefficient, rectangular similarity profile, or rescaled Green-field limit. The new limits require an additional asymptotic extraction from the endpoint ODE rather than merely renaming a prior theorem.

    ### Equivalent formulations

Searches: exact endpoint asymptotic finite step scale-invariant Euler t b_n 1/c; self-similar rectangle finite step 2D Euler scale invariant; published SCOPE search: Suleiman self similar Euler step

Evidence: No equivalent exact-limit statement was found in the inspected motivating source or targeted literature searches.

Reasoning: The closest equivalent formulation would be an exact \(t^{-1}\) coefficient or a scaled-profile convergence theorem. The source only supplies two-sided scale bounds plus integrability of the inner endpoints.

### Broader coverage

Searches: Ibrahim Suleiman arXiv:2609.20674 Proposition 2.4 finite steps; Elgindi Murray Said long-time scale-invariant Euler finite jumps

Evidence: Suleiman's finite-step proposition supplies comparability and integrability; Elgindi--Murray--Said supplies qualitative relaxation to finite-jump states.

Reasoning: Those broader results do not state the sharp constant or the explicit similarity field. The present claim is not a special case of a theorem giving a stronger exact asymptotic.

### Exact database or table

Searches: published SCOPE repository search: Suleiman self similar Euler step; published-record semantic query: finite Euler step self-similar rectangle exact endpoint mass

Evidence: Repository code search returned no additional matching published record. The semantic record-search service returned no usable result during this audit.

Reasoning: This is an analytic asymptotic statement rather than a database/table invariant; the relevant exact-record check found no separate table or duplicated exact theorem.

### Claim versus prior implication

Searches: arXiv:2609.20674 finite-step endpoint ODE and Proposition 2.4; arXiv:2211.08418 relaxation scale-invariant Euler

Evidence: The prior bounds do not themselves assert the exact limit; the proof must combine inner-endpoint integrability, monotonicity, the endpoint ODE, and a Taylor expansion.

Reasoning: The claim is a sharpening derived from prior ingredients, but the exact asymptotic conclusion is not an already-stated stronger theorem or automatic parameter specialization.

    ## Source inspections

    - **Dense orbits for scale-invariant rotationally symmetric solutions of the 2D Euler equations** (arXiv:2609.20674): trigger — same evolution equation and exact finite-step endpoint system; material read — reduced system and Green kernel; finite-step Proposition 2.4; endpoint ODE surrounding the finite-step proof; assessment — NOT_COVERING the exact constants/profile, but supplies the decisive prior estimates and ODE. Evidence: The inspected finite-step proposition gives \(O(t^{-1})\)-scale bounds and integrability of all endpoints except the rightmost one; the exact endpoint ODE is displayed separately.
- **On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications** (arXiv:2211.08418 / Ann. Sci. ENS 58 (2025)): trigger — broader qualitative relaxation theory for the same Euler reduction; material read — abstract/available theorem-level summaries describing relaxation to finite-jump states; assessment — NOT_COVERING the source-specific exact finite-step similarity constants. Evidence: The available statements are qualitative relaxation results, not the exact finite-step \(t^{-1}\) coefficient and rectangular scaling law.

    ## Checked sources

    - arXiv:2609.20674
- arXiv:2211.08418
- arXiv:2608.16755
- published SCOPE repository searches

    ## Residual risks

    - The semantic published-record search endpoint returned no usable result, so the repository/literature searches carry the usual indexing risk.
- A differently formulated exact asymptotic in older Euler literature could have escaped the targeted searches.

    ## Scientific value — PASS

    The sharp finite-step similarity law is a motivated structural refinement of the mechanism used in the motivating Euler construction. It identifies exactly which datum survives at leading order, gives a universal sector-mass constant, and supplies an explicit limiting transport field; this is more than a numerical sharpening or arbitrary finite slice.

    ## Limitations

    The theorem is limited to finite positive ordered step data in the stated \(m\ge4\) sector problem. It does not cover arbitrary regulated data, infinite stacks, or the \(m=3\) dynamics. Originality is best-of-knowledge with residual indexing risk.

    This document records a mathematical assessment of the stated claim and its literature context. It does not convert historical same-model review evidence into independent evidence.
