# Scientific review: finite-horizon constant-load discharge

## Correctness — PASS

The assertion is about expected **net** work under the displayed two-state generator, not a sampled forward-jump count or a time-varying control. The master equation gives the exact finite-horizon work formula. The key nonstandard step is the strict logarithmic concavity of the truncated-exponential response: its tilted variance is strictly smaller than its mean divided by the decay rate, yielding a negative load curvature for the hyperbolic-cosine relaxation rate. The unique interior optimizer then follows from endpoint behavior. At the intrinsic energy gap the load-dependent relaxation derivative vanishes, leaving an exactly time-independent occupation threshold. Differentiation of the optimizer's defining equation proves strict monotonicity and establishes the short- and long-horizon limits. Charge and hold thresholds follow from separately solved finite-state master equations.

The supplied `verify.py` ran 6636 bounded numerical and analytical-consistency checks over 108 parameter families. These checks are corroboration; the all-parameter conclusion rests on the exact proof. Independent proof checking has not occurred. The result assumes a constant kinetic scale and symmetric local-detailed-balance rate splitting.

## Originality — PASS, qualified

The closest motivating manuscript is Lin, Liu and Ma, *Active-Matter Battery* (arXiv:2610.00428v1, 2026-09-30), whose full accessible main text and appendices were examined. Its discharge equations establish a fixed-occupation **instantaneous** optimal load and a quasistatic **variable-load** work limit. Neither is the fixed-load finite-horizon optimization statement: the strict log-concavity, occupation-controlled reversal of optimal load with horizon, and charge/hold switching times require an additional comparison argument.

Liu, Lin and Ma, *Finite-Time Thermodynamics of Battery Discharging* (arXiv:2607.03157; *Entropy* 28, 852, 2026), analyze circuit models and multistage constant-current scheduling. Their available abstract, introduction, overview and appendix material do not establish this binary Markov theorem. Complete access to all pages was unavailable, so stronger hidden coverage cannot be ruled out. General time-varying optimal-process papers, including Schmiedl and Seifert (2007), use materially different controls and objectives. Published research-record searches and accessible neighboring results did not identify a theorem implying this claim; failure to find one is not proof of priority.

Remaining originality risks: an unlocated general theorem for mixtures of load-dependent exponential relaxation kernels; possible treatment of fixed-load finite-time extraction elsewhere; incomplete access to the closest broader finite-time discharge article. The identity of the source model and its instantaneous maximum-power result are explicitly attributed, not claimed as new.

## Value — PASS

A finite discharge deadline and a single fixed load are operationally distinct from optimizing the instantaneous current or allowing a continuously adjusted load. The theorem gives an all-parameter unique optimizer, a sign classification of how that optimizer moves with available time, and a sharp occupation threshold exactly at which the optimum stays pinned to the intrinsic energy gap. The same threshold yields exact charging and retention durations at which the direction of the load adjustment switches. These are structural statements for a natural physical design question rather than an arbitrary finite parameter slice or a small numerical improvement.

The result does not quantify full-cycle fuel efficiency, stochastic reliability, nonlinear source costs, or the best time-varying discharge policy. The physical usefulness of the constant-load restriction depends on the device, and experimental relevance is untested.

Self-review: passed. Independent audit: not yet performed.
