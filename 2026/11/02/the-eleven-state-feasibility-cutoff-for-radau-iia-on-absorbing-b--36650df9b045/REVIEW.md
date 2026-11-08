# Independent mathematical audit

## correctness

PASS

For unit-rate absorbing pure-birth Qn the transient power-series coefficients c_k of R(h(z−1)) and absorbing-column tail b_k exactly characterize entrywise nonnegativity. The c0=2(3−h)/(h²+4h+6) sign forbids h>3; for 0<h≤3 an exact positive-amplitude sine expression for b_k has φ>π/12 and ψ>π/6, forcing a negative b_k at some k≤10 and thus forbidding all n≥12. Exact recurrence at h=3 gives positive required coefficients through index 9 and hence feasibility n≤11; small-step fifth Taylor coefficient excludes n≥6 near 0. For n6, b4 sign is quintic P with strictly positive derivative, yielding {0}∪[γ,3]. Independent SymPy exact matrix/recurrence checks passed. No claim of complete n7–11 safe sets.

## originality

PASS

General absolute-monotonicity or SSP perturbation results do not classify the unmodified method on a specified absorbing chain: in this problem small steps are unsafe while a larger interval is safe. Nearby SCOPE [2/2] Pade eight-state barrier concerns a different method. No stronger result showing the Radau eleven-state frontier was found.

## value

PASS

An exact feasibility cutoff on canonical absorbing CTMC generators, including a recovered positivity interval and an obstruction persisting at every positive step, is a meaningful method-specific sharp boundary, not a routine Taylor-sign deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
