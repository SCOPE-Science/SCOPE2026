# Self-review: sharp Selkov period sensitivity

## Correctness — PASS
The exact spectral projection, quadratic/cubic derivatives and resolvent formula for the Hopf resonance give \(G_{21}=-1/2-i(2k^4+k^2+2)/(6k^3)\), with \(k=\sqrt{\gamma-1}>0\). The negative real part and transverse crossing prove the stable supercritical orbit. The first-substrate-Fourier normalization supplies the amplitude conversion; using the *actual-parameter* linear eigenfrequency avoids conflating drift along the Hopf parameter with genuine nonlinear detuning. The sharp bound is an exact square identity. The directly executed package checker verifies these symbolic claims. Direct finite-offset cycles agree asymptotically. Risks: each exponent is fixed before amplitude tends to zero, and no global period result follows.

## Originality — PASS with qualification
The original complete 1968 article derives \(\omega_0=1/\sqrt{\gamma-1}\) only in zero approximation and documents a numerical finite-amplitude departure. Brechmann and Rendall (2018) calculate supercritical Hopf and prove global limit-cycle alternatives for precisely the same system, but do not give the stated complex resonance or its unique exponent optimizer. Roy–Bhattacharjee–Mallik (2011) calculate actual frequency corrections in a different polynomial family with fixed power, and their displayed calculation does not imply the present variable-exponent theorem. The 2010 d'Onofrio paper was accessed indirectly through its abstract and the 2018 discussion, not completely, and creates residual historical-priority uncertainty. Named comparison queries and source-inspection details are recorded in AUDIT.json.

## Mathematical value — PASS
The original modeling question links feedback exponent to observable frequency. Here the coefficient is a natural nonlinear sensitivity invariant across the entire real-exponent Hopf family and has a sharp unique optimum; the unusual exponent-independent negative cubic saturation distinguishes amplitude growth from phase softening. These results improve on the original zero-order frequency rather than recomputing it. The same observable, time normalization and asymptotic scope are explicit and necessary.

## Limitations
No nonlinear period monotonicity away from Hopf, no conclusions about large cycles, and no uniform control as the feedback exponent approaches its endpoints. Historical novelty is supported by inspected comparisons, not independently certified. Publication dating of the original source is month-only (March 1968).

Self-review: passed. Independent audit: not yet performed.
