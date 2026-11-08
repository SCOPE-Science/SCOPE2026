# Independent mathematical audit

## correctness

PASS

For F′=min(r(t),f(F)) with locally Lipschitz strictly positive nonincreasing cumulative capacity f and arbitrary finite positive-duration rainfall blocks r_j≥0, scalar flows exist globally and strictly preserve initial-state order. For high rate a>b>0, define v_a=min(a,f), v_b=min(b,f), h(x)=∫ du/v_b and R=v_a/v_b∘h^{-1}, which is nonincreasing because v_a/v_b equals a/b, f/b or 1 on successive capacity regimes. The low-rate flow translates y by duration t; high-rate flow Ψ_s has derivative Ψ_s′(w)=R(Ψ_s(w))/R(w)≤1. Hence high-then-low minus low-then-high in transformed terminal state is ∫_0^t [1−R(Ψ_s(w))/R(w)]dw≥0. Positivity on a positive-measure subset is necessary/sufficient for strict advantage. Zero-intensity intervals commute, and equal intensities tie. Adjacent swaps and strict subsequent order preservation give global descending-maximal infiltration and ascending-minimal infiltration, with opposite runoff. Exact witness f=max(1,3−F), high 4 for log(4/3), low 1 for 1/4 gives final 1 vs 15/16. Independently recomputed rational witness and derivative flow argument. Assumes no ponding, moisture recovery or hydraulic-storage extension.

## originality

PASS

PASS qualified: known variable-rainfall infiltration models and the numerical decreasing-rain advantage are prior, but the global all-permutation all-nonincreasing-capacity theorem with exact strict swap test was not shown to follow from inspected sources; generic scalar control rearrangement literature is the key priority risk.

## value

PASS

For hydrological infiltration-excess forecasts, holding rain volume and block durations fixed while changing event order is a natural physical comparison. Globally sharp ordering and an exact equality test across an infinite admissible capacity class provide a reproducible benchmark and clarify when decreasing intensity really matters; excludes ponding and soil recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
